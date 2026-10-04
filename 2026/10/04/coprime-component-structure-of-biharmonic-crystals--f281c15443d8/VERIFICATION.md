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

The unrestricted argument is symbolic.

For a crystal, the source gives the equivalence
\[
Q(a,b)=rac{(a+b)^2}{(a+1)(b+1)}\in\mathbb N
\]
and the positive-integer solution parametrization
\[
x=u_n,\qquad y=u_{n-1},\qquad
u_{k+1}=(w-2)u_k-u_{k-1}+2,
\]
after \(x=(a+1)/2\), \(y=(b+1)/2\). The proof checks both gcd conclusions directly
from these identities.

The packaged `verify.py` performs finite corroboration in two independent ways:

1. It generates recurrence solutions for \(3\le w\le100\) and \(3\le n\le18\),
   verifies the conic identity, and checks \(\gcd(a,b)=1\) and
   \(\gcd(a+1,b+1)=2\).
2. It exhaustively scans odd \(3\le a\le b\le1201\), selects every pair for which
   \(Q(a,b)\) is integral, and checks the same gcd conclusions.

These computations do not establish the infinite theorem; the proof in `RESULT.md`
does. No claim is made about uniqueness when \(\omega(N)\ge3\).
