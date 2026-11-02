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
# Computational verification

The standalone `verify.py` uses direct enumeration of finite-field RREF subspaces and an independent bracket-closure predicate. For the four exhaustive cases \((d,q)=(2,2),(2,3),(3,2),(3,3)\), it checks \(16,28,2825,56632\) subspaces respectively and agrees exactly with the formula for ideal dimensions and projection ranks. For \((d,q)=(3,2)\), it counts \(45\) ideals; for \((3,3)\), \(94\) ideals. Larger-rank checks evaluate the exact Gaussian formula and its theta approximation for \(q=2,3\), exhibiting convergence and conditional rank-one concentration.

Run `python verify.py` with Python 3.8 or later, in this directory; the code uses only the standard library. Its direct RREF closure enumeration applies to prime fields \(q=2,3\), not arbitrary extension fields; the mathematical argument proves the unrestricted prime-power case. Finite checks do not prove the \(d\to\infty\) theorem. The analytic proof and source overlap assessment are given in `RESULT.md` and `REVIEW.md`.
