---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The coefficient-space verifier (`code/enumerate_direct.cpp`) processed all 2,097,151 nonzero ternary quintic equations over \(\mathbf F_2\), using exact degree-ten Macaulay rank and six-dimensional Cartier matrix arithmetic. It found exactly 688,128 geometrically smooth equations and reproduced every entry of the ten-stratum joint table in `data/direct_spectrum.txt`.

The independent orbit-based verifier (`code/enumerate_orbits.cpp`) generated the entire 168-element projective change-of-coordinates group from elementary generators, classified 4,204 smooth orbits and weighted them by orbit cardinality. Its weighted counts reproduce the direct enumeration; `data/orbit_spectrum.txt` and `data/representatives.csv` contain the results and representatives.

The exact extension-field verifier (`code/find_zeta_pair.cpp`) identified smooth coefficient masks 1064233 and 1064507 in the lexicographic degree-five monomial order \((x,y,z)\) with ascending \(x\), then ascending \(y\), and \(z=5-x-y\). They yield the same point counts \((0,2,6,14,60,74)\) and different \(a\)-numbers. The standalone `code/verify_zeta_pair.py` rechecked geometric smoothness via Buchberger's algorithm in all six chart–curve pairs, calculated each curve's Cartier matrix, and independently counted their rational points in six extension degrees. Exact output is in `data/pair_verification.txt`.

To reproduce, compile `code/enumerate_orbits.cpp`, `code/enumerate_direct.cpp` and `code/find_zeta_pair.cpp` separately with `c++ -O2 -std=c++17` and run their binaries. The orbit enumerator writes `representatives.csv` in the current directory; that file may instead be copied from `data/representatives.csv` before running the zeta-pair program. Then run `python3 code/verify_zeta_pair.py`.

The results are exact for the entire finite coefficient domain. The statement that a rank-66 Macaulay map is equivalent to geometric smoothness and the formula relating Cartier matrix ranks to \(a\)-number and \(2\)-rank are proved in `RESULT.md`; the finite calculations alone would not justify those geometric interpretations. Historic literature and priority cannot be certified by computations, and no independent mathematical audit has been performed.
