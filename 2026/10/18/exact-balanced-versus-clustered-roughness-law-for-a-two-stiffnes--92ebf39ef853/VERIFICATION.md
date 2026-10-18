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

# Reproducibility and verification

Run `python roughness_checker.py` with SymPy installed (`requirements.txt`). Actual recorded results:

- PASS: 4,048 exact-rational evaluations comparing independently computed oriented-arc and marked-pair formulas.
- PASS: 4,048 exact-rational global bounds, each checking both equality classes against cyclic rotations of a contiguous inventory and the mechanical word.
- PASS: 238 independent exact-rational matrix inversions of the Laplacian on the mean-zero subspace for \(3\le n\le7\), compared with the arc formula.

All inventory subsets for \(3\le n\le10\) and two rational resistance profiles were checked by finite exhaustive computation. These checks cannot prove the theorem for unbounded ring size or all positive real contrasts. The proof for those quantifiers is analytical and given in `RESULT.md`. The eigenvalue zero mode is removed by the constraint \(\sum h_i=0\); the matrix computation forms \((L+J)^{-1}-J\) with \(J\) the normalized all-ones matrix. No external/human/independent review is represented by these tests.
