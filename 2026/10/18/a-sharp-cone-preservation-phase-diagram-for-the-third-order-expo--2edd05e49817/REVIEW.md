# Self-review

## Correctness — PASS

The exact stage at a zero matrix is \(c_a(h)Q\) because its Jacobian operator is scalar; the only nonlinear defect equals \(-c_a(h)^2QGQ\). This derives the matrix factorization without any simultaneous diagonalization. Congruence on \(\operatorname{ran}Q\) proves the complete inertia statement; integral representations prove strict monotonicity, endpoint limits, uniqueness of the critical time and its damping asymptotic. Independently, splitting the normalized scalar domain at \(y=1\) proves **all-state** positivity below the bound; the exact boundary map \(\mathcal E_t(0)=t(1-t^2/3)\) proves sharpness and a false fixed point at equality. The proof includes degenerate \(Q\), \(G\), \(a=0\), and equality cases. The exact-flow comparison uses a fundamental-matrix representation, not finite experiments.

## Originality — PASS, with bibliographic risk

The third-order method and algebraic tools are established prior work. Li, Zhang and Liu's full 2019 preprint was additionally inspected: its `Erow3` equation (23) gives exactly the same third-order matrix method, so **the method itself is emphatically not new**. That paper studies implementation and numerical convergence, without a cone-preservation classification. Li, Li and Yang's 2026 manuscript was inspected for the embedded adaptive version (equation (22)), low-rank section and controller. Hochbruck, Ostermann and Schweitzer's foundational 2009 paper was inspected for the original `exprb32` method and convergence claims. Chen and Borzì's 2023 paper concerns different first-/second-order positivity-preserving schemes, according to its publisher abstract and first-page preview. No equivalent noncommutative `exprb32` spectral phase diagram or all-state scalar threshold was located in the inspected literature or checked published research records. The 2023 full text could not be inspected and remains a residual risk; a negative search is not a uniqueness proof.

## Mathematical value — PASS

The finding distinguishes high-order accuracy and tolerance acceptance from preservation of the positive-semidefinite cone, which is essential for covariance/control Riccati approximations. It gives an implementable sharp spectral step bound without requiring \(Q\) and \(G\) to commute, classifies when scalar damping protects **all** first-step sizes, and establishes a stronger global nonnegativity safety condition for a nonlinear scalar model. The equality endpoint has a concrete spurious equilibrium even though the exact flow immediately enters the positive interior. This goes beyond a single counterexample or textbook norm estimate, while not claiming a general convergence improvement.

## Scope and limitations

The exact full-matrix update is analyzed, not truncated low-rank implementations. General nonzero matrix initial data and general drift matrices are unproved. The novel spectral content has not received independent expert audit; older specialized sources may contain equivalent observations.

Self-review: passed. Independent audit: not yet performed.
