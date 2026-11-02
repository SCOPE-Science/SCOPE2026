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
The analytic proof uses the identity
\[
\left(1+2q^2/d\right)s^4+(4+4q)s^3u+\left(1+2/d\right)u^4-(s+u)^4
=2(u-as)^2(u+bs)^2/d.
\]
The parameters satisfy \(a-b=d\), \(ab=q=d(d+3)/2\), and \(t^4=q(d^2+q)\). Direct expansion yields zero symbolic difference. The positive root is unique by strict monotonicity. A numerical root test at \(t=1\) gave \(d=0.5031886736133129\), \(q=0.8813824310463318\), and \(F(1)=1.7350405262195225\). These decimals check the presentation but the theorem follows from the symbolic identity and the measure-theoretic construction.

The weak-null witness uses the atomless probability measure \(|x|^4\mu\); the two-valued independent multipliers have zero mean and exact fourth moment \(t^4\). Their orthogonality in \(L^2\), together with their boundedness, proves the asserted dual pairings without additional separability assumptions. The minimizing-distance selection supplies the claimed \(L^4\) rigidity. This is not independent external validation; no independent audit has been performed.
