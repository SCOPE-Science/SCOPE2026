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

The proof was checked symbolically from the defining quantile identities. For atomless states, the probability-integral identity \(F_\mu(Q_\mu(u))=u\) gives the resource-targeted quantile update. The exact cancellation of the common \(R(u)\) term was verified inside the one-dimensional \(W_1\) integral before the \(L\)-Lipschitz microscopic map is applied.

For the equilibrium law, the critical step is not merely \(Q_*(v)-Q_*(u)\ge\tau\varepsilon[R(v)-R(u)]\). The self-term was retained and solved:
\[
Q_*(v)-Q_*(u)
\ge
\frac{\tau\varepsilon}{1-\tau(1-\varepsilon)}[R(v)-R(u)].
\]
The matching upper inequality uses \(L\) in the same way. Integrating these inequalities over the \(N\) left-endpoint quantile cells gives the two-sided equilibrium estimate exactly.

For finite-time approximation, each ordered empirical quantile cell was compared with the continuum quantile after one update. Integration yields
\[
W_1(\eta_{N,n+1},\mu_{n+1})
\le L(1-\varepsilon)W_1(\eta_{N,n},\mu_n)+L\varepsilon e_N(\rho),
\]
and the displayed geometric-series bound follows.

Limits checked: \(0<\varepsilon<1\), \(0<\tau\le L<1\), one-dimensional monotone \(T\), atomless continuum states for the exact rank-quantile identity, and continuous strictly increasing bi-Lipschitz \(R\). No claim is made beyond these boundaries. No external independent validation has been performed.
