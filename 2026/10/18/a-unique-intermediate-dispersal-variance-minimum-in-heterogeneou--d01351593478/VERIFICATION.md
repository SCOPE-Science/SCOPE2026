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

The exact rational stationary-covariance equations were independently solved in `check.py` for 480 positive-parameter configurations and matched the theorem's closed form. The program also checks the finite threshold samples and the exact witness \((a,b,A,B)=(1,2,1/2,1)\), giving \(d_*=1\), \(V(0)=1/2\), \(V(1)=49/100\), and \(V(\infty)=1/2\).

The unrestricted claim is certified by the written identities for the Lyapunov solution, \(V'(d)\), and the strictly positive derivative of \(R(d)\) when \(a<b\), not by the finite checks. Independent audit has not been performed. The model treats linear fluctuations; its trajectories are not constrained to nonnegative population abundance.
