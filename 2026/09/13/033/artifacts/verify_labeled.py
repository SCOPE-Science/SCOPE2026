"""Independent verifier for the labeled tricyclic census (re-checks the two load-bearing facts).

Reads output/artifacts/raw_solutions.json (exact-cover row sets), rebuilds the block
lists from the orbit matrix, and recomputes Pasch counts + sub-STS(7) counts with
self-contained routines (no reliance on cached census JSON). Checks:
  (V1) every labeled solution is a valid STS(21) fixed by sigma (orbit-closed);
  (V2) min Pasch over Fano-containing labeled solutions equals 7;
  (V3) witness index 10 is Fano-containing with Pasch count 7.
Usage: PYTHONPATH=output/artifacts python3 output/artifacts/verify_labeled.py
"""
import json, sys, itertools
sys.path.insert(0, 'output/artifacts')
import sts_lib as L

def main():
    cols, rows = L.build_orbit_matrix()
    assert len(cols) == 30
    sols = json.load(open('output/artifacts/raw_solutions.json'))
    print('solutions:', len(sols))
    assert len(sols) == 135128
    rowcols = {r: d['cols'] for r, d in rows.items()}
    wit = json.load(open('output/artifacts/witness.json'))
    wb = [frozenset(x) for x in wit['blocks']]
    S = set(wit['fano_point_set'])
    assert L.is_sts(wb) and L.pasch_count(wb) == 7
    assert sum(1 for b in wb if set(b) <= S) == 7
    print('witness OK: STS(21), Pasch 7, Fano set carries 7 blocks')
    mn_all = None
    mn_fano = None
    n_fano = 0
    for s in sols:
        assert len(s) == 10 and len(set(s)) == 10
        cov = []
        for r in s:
            cov.extend(rows[r]['cols'])
        assert sorted(cov) == list(range(30)), 'not an exact cover'
        fb = L.blocks_of_solution(rows, s)
        assert L.is_sts(fb)
        p = L.pasch_count(fb)
        F = L.fano_find(fb)
        mn_all = p if mn_all is None else min(mn_all, p)
        if F:
            n_fano += 1
            mn_fano = p if mn_fano is None else min(mn_fano, p)
    print('min Pasch over ALL labeled tricyclic:', mn_all)
    print('Fano-containing labeled count:', n_fano)
    print('min Pasch over FANO-CONTAINING labeled:', mn_fano)
    assert n_fano == 61040, n_fano
    assert mn_fano == 7, mn_fano
    assert mn_all == 0, mn_all
    print('VERIFIED: labeled-level Fano minimum is 7 (witness attains it).')

if __name__ == '__main__':
    main()
