#!/usr/bin/env python3
import json
import itertools
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = json.loads((HERE / 'strategy_certificate.json').read_text(encoding='utf-8'))


def vertices_in(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask -= bit


def allowed_responses(n, probe, robber):
    # Partial feedback: if the probe hits the robber, the probe vertex is returned.
    # Otherwise one neighbor of the probe lying on a shortest probe-robber path is returned.
    if probe == robber:
        return (probe,)
    diff = probe ^ robber
    return tuple(probe ^ (1 << i) for i in range(n) if (diff >> i) & 1)


def response_classes(n, state, probes):
    # Map each possible simultaneous response tuple to its exact consistency class
    # among the current possible robber vertices.
    classes = {}
    for robber in vertices_in(state):
        choices = [allowed_responses(n, p, robber) for p in probes]
        for response in itertools.product(*choices):
            classes[response] = classes.get(response, 0) | (1 << robber)
    return classes


def closed_neighborhood(n, mask):
    out = mask
    for v in vertices_in(mask):
        for i in range(n):
            out |= 1 << (v ^ (1 << i))
    return out


def verify_certificate(cert):
    n = cert['dimension']
    k = cert['cops']
    bound = cert['winning_round_bound']
    full = (1 << (1 << n)) - 1
    assert cert['initial_state_mask'] == full
    assert k == n
    policy = {}
    for key, entry in cert['policy'].items():
        state_s, depth_s = key.split(':')
        state, depth = int(state_s), int(depth_s)
        assert entry['state_mask'] == state and entry['depth'] == depth
        policy[(state, depth)] = entry
    assert (full, bound) in policy
    seen = set()
    response_count = 0
    transition_count = 0
    max_seen_depth = 0

    def rec(state, depth):
        nonlocal response_count, transition_count, max_seen_depth
        if state.bit_count() <= 1:
            return
        key = (state, depth)
        if key in seen:
            return
        seen.add(key)
        assert (state, depth) in policy, f'missing policy state-depth {(state, depth)}'
        entry = policy[(state, depth)]
        assert entry['depth'] == depth, (state, entry['depth'], depth)
        probes = tuple(entry['probes'])
        assert len(probes) == k and len(set(probes)) == k
        assert all(0 <= p < (1 << n) for p in probes)
        assert depth >= 1
        max_seen_depth = max(max_seen_depth, depth)
        classes = response_classes(n, state, probes)
        assert classes
        for response, cls in classes.items():
            response_count += 1
            assert cls != 0
            # Every listed response really is legal for exactly the vertices in cls.
            reconstructed = 0
            for robber in vertices_in(state):
                legal = True
                for probe, ans in zip(probes, response):
                    if ans not in allowed_responses(n, probe, robber):
                        legal = False
                        break
                if legal:
                    reconstructed |= 1 << robber
            assert reconstructed == cls
            if cls.bit_count() == 1:
                # Cops have uniquely located the robber before the robber's move.
                continue
            assert depth > 1, f'non-singleton response survives at depth 1: state={state}, response={response}'
            nxt = closed_neighborhood(n, cls)
            transition_count += 1
            assert (nxt, depth - 1) in policy, f'missing child policy state-depth {(nxt, depth - 1)}'
            rec(nxt, depth - 1)

    rec(full, bound)
    # Ensure the certificate has no unreachable filler states.
    assert seen == set(policy), (len(seen), len(policy), set(policy) - seen)
    return {
        'dimension': n,
        'cops': k,
        'policy_states': len(policy),
        'winning_round_bound': bound,
        'response_tuples_checked': response_count,
        'nonterminal_transitions_checked': transition_count,
        'max_certificate_depth': max_seen_depth,
    }


def main():
    assert CERT['schema_version'] == 1
    assert CERT['model'] == 'partial-feedback directional localization'
    results = [verify_certificate(c) for c in CERT['certificates']]
    assert [(r['dimension'], r['cops'], r['winning_round_bound']) for r in results] == [(3, 3, 2), (4, 4, 3)]
    for r in results:
        print(
            f"Q_{r['dimension']}: cops={r['cops']}; policy_states={r['policy_states']}; "
            f"winning_round_bound={r['winning_round_bound']}; "
            f"response_tuples_checked={r['response_tuples_checked']}; "
            f"nonterminal_transitions_checked={r['nonterminal_transitions_checked']}"
        )
    print('ALL CHECKS PASSED')

if __name__ == '__main__':
    main()
