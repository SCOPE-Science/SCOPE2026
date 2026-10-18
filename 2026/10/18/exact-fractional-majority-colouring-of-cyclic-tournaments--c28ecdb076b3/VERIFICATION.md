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

# Reproducibility and boundaries
The standalone program `check_majority.py` uses Python 3 standard library and may be executed as `python3 check_majority.py` in the directory containing the two documents. It computes directed arcs by clockwise modular differences. Every majority-stable subset of each of the eight odd cyclic tournaments with \(3\le n\le17\) is checked by brute force, a total of \(174{,}760\) subsets. It checks that no stable set exceeds the asserted maximum, that a proposed witness attains this maximum, and that every vertex lies in exactly \(2\lfloor(n-1)/4\rfloor+1\) shifted copies of the witness. It also checks ordinary-colouring witness partitions for all odd orders \(3\le n\le501\), encompassing \(250\) graphs.

A separate independent numerical LP calculation, using all feasible majority-stable sets on orders \(3,5,7,9,11,13\), returned the predicted rational values \(3\), \(5/3\), \(7/3\), \(9/5\), \(11/5\), and \(13/7\) respectively. That optional numerical calculation is not a dependency of the standalone program.

The proof for all odd orders is the complete combinatorial counting and rotational translation argument in `RESULT.md`; finite checking alone is not a certificate of an infinite statement. Originality comparisons are research searches, not a certificate of nonexistence of a prior theorem. No independent external mathematical audit was performed.
