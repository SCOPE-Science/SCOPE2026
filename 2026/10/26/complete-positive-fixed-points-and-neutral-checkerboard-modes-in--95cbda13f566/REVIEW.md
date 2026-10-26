# Scientific review: positive fixed points of centered nonlinear diffusion

## Correctness — PASS

The fixed-point equation of the specified zero-reaction, reflected-Neumann update reduces exactly to a discrete reflecting Laplace equation for the product \(w=u|G_hu|^{p-2}\). A finite maximum principle makes \(w\) constant, its corner value is zero, and strict positivity forces every centered gradient to vanish. The resulting one- and two-dimensional parity recurrences are exhaustive, and the converse is immediate. The edge-energy coefficient follows by counting all horizontal and vertical edges. For \(p>3\), the coefficient map has zero derivative at zero gradient, yielding an identity Jacobian. All proof steps are independent of timestep size and of the finite-grid tests. The standard-library exact-rational checker passed 982 checks; finite checks are corroboration rather than an infinite proof.

## Originality — PASS, with stated residual historical risk

Zinihi–Ehrhardt–Sidi Ammi (arXiv:2607.00489, equations (5)–(7), Theorem 2) present the specific update and prove inclusion of constant equilibria, not a complete classification of all positive fixed points for the stated coordinatewise reflected boundary rule. Reiss (arXiv:1402.0998, §§1–2) explicitly explains classic odd–even decoupling of collocated central derivatives; that mechanism is acknowledged and not claimed as an invention. The 2004 Andreianov–Boyer–Hubert paper (doi:10.1051/m2an:2004045, Theorem 2.12) proves uniqueness for different coercive finite-volume schemes with Dirichlet conditions; it does not cover this two-time-level Neumann map. Searches of published mathematical records for equivalent parity-class fixed-point classifications found related but non-implicative diffusion and parity results. The exact stationary manifold, corner-pinning argument, all-step high-edge-energy family, and Jacobian at degenerate equilibria were not identified as covered. Possible historical equivalence in older centered nonlinear diffusion literature is a genuine remaining risk; search absence is not a novelty certificate.

## Mathematical value — PASS

The complete equilibrium classification answers a natural model-fidelity question: does the positivity-preserving numerical diffusion retain only the continuous zero-reaction Neumann equilibria? It does not. Every positive four-parity pattern remains exactly stationary independently of the timestep, and a fixed-contrast checkerboard has edge-gradient energy growing at the explicit rate \(h^{-p}\). When \(p>3\), first-order perturbation analysis cannot see damping at these equilibria because the entire update Jacobian is the identity. This is a structural obstruction relevant to diffusion discretization and testing, not an arbitrary small-grid calculation or an isolated numerical anomaly.

## Scope and priority limitations

The result is for the exact rational update displayed in the source, with a fully specified coordinatewise even-reflection ghost completion, zero reaction, \(p>2\), and strictly positive grid states. The printed source specifies corner ghosts but not every side ghost equation, so its other conceivable boundary implementations are not covered. The \(p>3\) derivative statement is local and does not assert nonlinear stability. Classical odd–even decoupling and source constant-equilibrium preservation are prior knowledge. Independent historical-priority and proof audit have not occurred.

Self-review: passed. Independent audit: not yet performed.
