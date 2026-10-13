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

The embedded `verify.py` uses exact symbolic arithmetic to reconstruct the resultant of the \(p=1/10\) boundary-law cubic and Kesten--Stigum equality, checks the factorization, counts roots of the degree-40 factor on \((1,\infty)\) by Sturm's theorem, and verifies \(1.47075929<r_*<1.47075930\). It also checks the exact rational sign certificate at \(r=2\) and the uniform bound \(|\lambda_2|<256/3125<1/\sqrt2\).

Successful replay output:

`VERIFY_OK resultant=exact roots_gt1=1 bracket=1 lambda2_bound=256/3125 r_star=1.47075929094322328177871715848549868507380143539141371779546 theta_star=6.88189437635365161332786339775379998579046070029962092235175`

Finite decimal evaluation only prints the isolated algebraic root. The uniqueness and sign classification are exact. No independent audit has been performed.
