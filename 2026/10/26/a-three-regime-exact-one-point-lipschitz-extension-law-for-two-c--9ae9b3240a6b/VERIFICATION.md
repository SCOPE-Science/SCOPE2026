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

# Verification record

The theorem is proved analytically for all positive real admissible distances and every pair of finite cluster sizes at least two. The calculation uses only finite group averaging, source Lipschitz-free duality, explicitly Lipschitz distance/test potentials, two barycentric transport estimates, and minimization of two affine functions. The verification tests below corroborate computations without being treated as an infinite proof.

Run `python3 check_two_cluster.py` with SciPy installed. The checker constructs the full source metric and its Lipschitz-potential linear inequalities; it solves a master linear program over **arbitrary real signed coefficients**, adds constraints exposed by independent potential-optimization separation LPs, and compares the result to the claimed formula. It returned:

```
UNRESTRICTED_SIGNED_LP_OK 29 instances
EXACT_RATIONAL_SUPPORT_EXAMPLES_OK 3
```

The second check uses Python exact rational arithmetic to verify the distinct strict-support cases:
\((p,q,s,t,R,U)=(3,5,4/5,4/5,1,1/2)\), with \(a_*=0\) and \(\Lambda=32/25\); \((4,3,4/5,4/5,1/2,6/5)\), with \(a_*=1\) and \(\Lambda=6/5\); and \((3,3,4/5,4/5,3/5,3/5)\), with \(a_*=1/2\) and \(\Lambda=23/18\).

The LP solver uses floating-point arithmetic, so its 29 finite checks are numerical, not certified proofs. A finite collection of such checks cannot establish the formulas for unrestricted cardinalities and real parameters; that is supplied by the proof. No independent audit or external mathematical certification has been performed.
