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

Run `python3 verify.py` with Python 3.9 or later; it needs only the Python standard library. It constructs each matching-deleted complete bipartite graph, forms the actual edge-conflict relation, and tests all subsets in the stated finite ranges. A second common-edge test explicitly scans every candidate third edge and compares its answer with the cross-edge characterization.

Observed deterministic checks: 32 parameter triples with \(2\le m,n\le4\); 144444 edge subsets; 1112 feasible sets; 27 exceptional non-star pairs across the small test cases; 5062 independent two-edge conflict comparisons on graphs with \(2\le m,n\le5\); and 1048576 additional subsets of \(H_{5,5,5}\), yielding the enumerator \(1+20x+70x^2+40x^3+10x^4\).

The verifier also prints coefficients for larger parameter triples computed from the proved formula. This is a formula evaluation, **not** a brute-force certificate at those larger sizes. The theorem for all admissible integers is established by the case proof in `RESULT.md`, not by bounded enumeration. No external or independent audit has been performed.
