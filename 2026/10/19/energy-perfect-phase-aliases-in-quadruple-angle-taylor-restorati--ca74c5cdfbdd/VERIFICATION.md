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

# Reproducibility and limits

Install `requirements.txt`, then run `python verify.py` under Python 3. The standalone program requires `mpmath==1.3.0` and uses built-in exact rational arithmetic and 250-digit decimal-precision computations. It reports `VERIFY_OK 11669 assertions`. The test includes seven small-degree root censuses, exact rational defect identities at successive restorations, and root-solved approximate maximal phase aliases at \((m,s)=(1,16),(1,24),(1,36),(2,30),(2,45),(2,60),(4,64),(4,100),(20,512)\).

The proof in `RESULT.md`, not the finite checker, establishes the theorem for every fixed positive integer degree. The uniqueness step is a local analytic inversion, the energy census uses the exact Chebyshev factorization, and the no-exact-phase statement invokes the classical transcendence of \(\pi\). These checks do not establish behavior of any adaptive scaling/tolerance chooser, floating-point exactness, or a publication-priority certification. Independent audit has not been performed.
