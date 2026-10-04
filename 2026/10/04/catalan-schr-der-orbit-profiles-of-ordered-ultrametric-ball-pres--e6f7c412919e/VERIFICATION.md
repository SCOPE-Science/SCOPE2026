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

# Verification

A separate finite replay checks the enumerative consequences of the proof.

For each of \(N=2,3,4,\infty\), it constructs canonical plane rooted trees recursively by ordered root-tuples and independently computes the same numbers from the composition recurrence. The two methods agree through \(n=8\). For \(N=2\), the values are \(1,1,2,5,14,42,132,429\), exactly \(C_{n-1}\). For \(N=\infty\), they are \(1,1,3,11,45,197,903,4279\), matching OEIS A001003 shifted by one leaf. Multiplication by \(n!\) reproduces the displayed injective orbit profiles.

The checker also computes Stirling numbers of the second kind and verifies the full-tuple profiles \(1,3,19,207,3211,64383\) for \(N=2\) and \(1,3,25,387,8521,241683\) for \(N=\infty\). It evaluates the coefficients of \(T_N(e^z-1)\) indirectly through the Stirling identity and ends with `VERIFY_OK`.

The replay does not independently prove that finite plane bp-types extend to global bp-automorphisms. That is the model-theoretic step, checked against Malicki's Fraïssé morphism framework and by the explicit one-point back-and-forth argument in RESULT.md. No independent audit has been performed.
