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
The exact proof uses the conserved population simplex, risk-ratio equilibrium equations, the graph-energy identity, and a block Jacobian decomposition.

For the two-strain infected-lockdown equations,
\[
\mathcal V=\frac12\sum_j S_j^2+\sum_v r_vI_v
\]
satisfies
\[
\dot{\mathcal V}=-\frac d2\sum_{i,j}L_{ij}(S_i-S_j)^2-\sum_v\beta_vI_v(S_{j(v)}-r_v)^2.
\]
All zero-dissipation states are equilibria, so compactness and LaSalle imply approach to the equilibrium set. For every admissible endemic risk \(r<N/k\), the constant equilibrium value
\[
F(r)=Nr-\frac{k}{2}r^2
\]
is strictly increasing. This fixes one limiting risk component. An initially positive lower-risk infected cell cannot approach a larger susceptible limit because its growth rate would eventually be bounded strictly below by a positive constant. This gives the stated selected risk level.

For each endemic equilibrium, the symmetric susceptible block \(M=dL-\operatorname{diag}(D)\) is strictly negative definite by graph connectivity and at least one positive infected cell. After ordering the off-risk, susceptible, and risk-tied infection coordinates, the Jacobian diagonal blocks are the off-risk exponents, \(M\), and a zero block. The \(m(r)\) full-space zeros are semisimple, and one is removed by total-mass conservation.

The bundled `verify.py` requires only Python's standard library. It reconstructs exact rational Jacobians for an endemic unique-minimum vertex, an unstable higher-risk vertex, and two positions on a risk-tie equilibrium segment. Using the exact Faddeev–LeVerrier characteristic-polynomial recursion, it checks that the factors have the predicted eigenvalues, including the semisimple neutral composition dimension. It also checks population conservation and the Lyapunov identity at a rational non-equilibrium state.

These finite checks corroborate but do not establish the universal proof for all graph sizes, all positive parameters, and all initial states. No independent audit has been performed.
