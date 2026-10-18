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

# Reproducibility

Run `python verify.py` (Python 3, standard library only). The program computes the generalized floor recurrence independently of the proper-divisor recurrence for \(0\le c\le8\) through \(n=240\), compares both computations, and tests the latter through \(n=2500\). It checks the Möbius congruence for integral slopes \(c\ge2\), exact squarefree layer values within range, prime-power values, the three sharp boundary witnesses, and exhaustive prime/composite classification through the finite cutoff for \(c\ge3\). The executable completed with a PASS line.

The analytic argument, including the squarefree generating function and its strict coefficient inequality, proves the unbounded assertions. The program is a consistency check rather than an exhaustive or independent proof. No independent audit has been performed.
