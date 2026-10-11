# Independent mathematical audit

## correctness

PASS

The exact QP correction is the Euclidean projection of u=(0,-1) onto the active linearized disk half-space. Writing s as the squared half-step norm and d as the squared distance to u gives lambda=1-d/(2s) and the corrected full step x-plus=c h with c=1-eta+eta d/(2s). The submitted polynomial bound proves the full step is strictly inside the disk, while direct expansion proves the next half-step is strictly outside, so induction gives persistent alternation. The exact ratio formula for d_{t+1}/d_t and the uniform bound on its bracket yield the stated contraction rho(eta)<1; geometric decay then gives both pointwise limits and O(1/T) convergence of the averaged half-step to the boundary point. The inspected rational-arithmetic checker is consistent with representative trajectories, and an independent numerical replay across several eta values reproduced the outside/inside alternation and contraction.

## originality

PASS

The current OPCGM source publicly states the first-half-step infeasibility obstruction and a general averaged-iterate feasibility tradeoff, while the package's exact witness analysis proves the stronger and more specific phenomenon that every queried half-step stays infeasible even though the average converges to feasibility at rate O(1/T). Targeted Resultary search returned no equivalent exact trajectory theorem. The immediate predecessor studies a single-step primal constrained-gradient method and does not contain the two-QP OPCGM-Lipschitz trajectory law. A complete primary copy of the 2026 OPCGM paper was not obtained during this run after public and permitted institutional routes failed, so exact overlap with its internal Remark 4.6 remains an explicit residual risk; inaccessible literature alone is not treated as failure.

## value

PASS

The result resolves the behavior of the canonical curved-constraint witness used to motivate an averaged-feasibility obstruction: every sampled half-step remains infeasible, yet averaging removes the violation at an explicit O(1/T) rate. That distinction directly limits what this witness can prove about asymptotic averaged infeasibility and supplies a reusable exact trajectory benchmark for primal-QP extragradient methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
