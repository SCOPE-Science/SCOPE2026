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

The analytic proof specializes the published FFP2 recurrence to \(T=0\) and \(G(x)=\lambda x\). The critical checks are:

1. \(G_\eta=G\) because the resolvent of the zero operator is the identity.
2. With \(a=\eta\lambda\) and \(c=\nu\lambda/r\), the assumptions imply \(0<c<a<1\).
3. The ratio recurrence preserves \(0<x_k/z_k\le1\), so all logarithms in the product argument are well defined after taking absolute values of the common initial sign.
4. The stable inequality for \(q_k=x_k/z_k\) gives \(q_k=O(1/t_k)\), and the exact scaled recurrence gives \(t_kq_k\to r(1-a)/a\).
5. The multiplicative decrement of \(z_k\) is \(s/t_k+o(1/t_k)\), with a square-summable remainder, yielding the stated logarithmic exponent.

The bundled script replays the recurrence for \(\lambda=1\), \(\eta=1/2\), \(r=3\), \(\nu=1/2\), and \(t_0=10\). It checks the parameter inequalities and the finite-index approach to the three predicted scaled limits. Its output is `VERIFY_OK` when all checks pass.

The computation does not certify the infinite asymptotics by enumeration; those are proved algebraically. No claim is made outside the parameter and model scope stated in the result.
