#!/usr/bin/env python3
"""Elementary exact certificate check for the binary order-eight orientable-period bound."""
import json
import itertools
from pathlib import Path


def reversal(integer, width):
    return int(f'{integer:0{width}b}'[::-1], 2)


def verify():
    data = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
    assert data['length'] == 8 and data['claimed_optimum'] == 92
    edges = [w for w in range(256) if w != reversal(w, 8)]
    pair_keys = [w for w in edges if w < reversal(w, 8)]
    pal_vertices = [v for v in range(128) if v == reversal(v, 7)]
    assert len(edges) == 240 and len(pair_keys) == 120 and len(pal_vertices) == 16
    raw = data['dual']
    def int_data(mapping):
        assert isinstance(mapping, dict)
        assert all(type(v) is int for v in mapping.values())
        return mapping
    flow_raw = int_data(raw['vertex_potentials'])
    turn_raw = int_data(raw['palindrome_potentials'])
    beta_raw = int_data(raw['reversal_pair_weights'])
    assert all(str(v) == k and 0 <= v < 128 for k in flow_raw for v in [int(k)])
    assert all(str(w) == k and w in pair_keys for k in beta_raw for w in [int(k)])
    assert all(isinstance(v, int) and v >= 0 for v in beta_raw.values())
    for key in turn_raw:
        v,b = map(int,key.split(':'))
        assert key == f'{v}:{b}' and v in pal_vertices and b in (0,1)
    flow = {int(k):v for k,v in flow_raw.items()}
    turn = {tuple(map(int,k.split(':'))):v for k,v in turn_raw.items()}
    beta = {int(k):v for k,v in beta_raw.items()}
    assert sum(beta.values()) == 92

    # Verify the palindromic-vertex implication by complete local enumeration.
    for v in pal_vertices:
        incoming = [(b << 7) | v for b in (0,1)]
        outgoing = [(v << 1) | b for b in (0,1)]
        incident_edges = sorted(set(incoming + outgoing))
        for masks in itertools.product((0,1), repeat=len(incident_edges)):
            x = dict(zip(incident_edges, masks))
            if any(x[w] for w in x if reversal(w,8) == w):
                continue
            if any(x[incoming[b]] + x[outgoing[b]] > 1 for b in (0,1)):
                continue
            if sum(x[w] for w in incoming) != sum(x[w] for w in outgoing):
                continue
            for b in (0,1):
                assert x[incoming[b]] == x[outgoing[1-b]]

    # Pure integer-arithmetic dual verification; no optimization package used.
    margins=[]
    for w in edges:
        reverse_pair = min(w, reversal(w,8))
        coefficient = beta.get(reverse_pair,0) + flow.get(w & 127,0) - flow.get(w >> 1,0)
        for (v,b), weight in turn.items():
            coefficient += weight * (int(w == ((b << 7) | v)) - int(w == ((v << 1) | (1-b))))
        margins.append(coefficient)
        assert coefficient >= 1, (w, coefficient)

    # An explicitly listed orientable cyclic word of the upper-bound length.
    witness = data['witness']
    assert len(witness) == 92 and set(witness) <= {'0','1'}
    windows = [(witness + witness[:7])[i:i+8] for i in range(92)]
    assert len(set(windows)) == 92
    assert all(w != w[::-1] for w in windows)
    assert len({min(w,w[::-1]) for w in windows}) == 92
    # Also check that the selected de Bruijn arcs are a balanced connected circuit.
    counts_in=[0]*128; counts_out=[0]*128
    for w in windows:
        integer=int(w,2)
        counts_out[integer>>1] += 1
        counts_in[integer&127] += 1
    assert counts_in == counts_out
    print('VERIFY_OK M_8=92, dual_bound=92, verified_edges=240, '
          f'nonzero_pair_weights={len(beta)}, min_dual_margin={min(margins)}')

if __name__ == '__main__':
    verify()
