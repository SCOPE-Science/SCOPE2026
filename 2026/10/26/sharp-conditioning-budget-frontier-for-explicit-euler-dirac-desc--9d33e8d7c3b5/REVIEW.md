# Mathematical review

## Correctness — PASS

The proof uses only finite-dimensional real Euclidean linear algebra, the chain identity \(B_1B_2=0\), and exact positive-parameter inequalities. Orthogonality of the lower- and upper-incidence singular spaces gives a complete block reduction. The two-by-two largest-singular-value identity is derived from the characteristic polynomial of \(T^\top T\), not inferred from examples. It yields the exact whole-matrix norm because the maximal singular mode is attained. Convexity, the strict boundary comparison, and the strictly monotone coupling constant give the sharp stepsize and metric-budget statements. The exact Euler eigenvalues separately prove the Schur interval. An independently executable numerical checker exercises full incidence matrices, including the filled-triangle witness; finite testing is not substituted for the universal proof.

## Originality — PASS, with bounded search uncertainty

Rodríguez-Camargo, Urquijo-Rodríguez, and Mojica-Nava, arXiv:2610.22628v1 (October 15, 2026), Sections 4.1–4.3, establish the directional Dirac flow's continuous-time spectral threshold and a fully symmetrizing weighted Lyapunov norm. The paper explicitly states the continuous-time unweighted arithmetic-mean restriction, and its experiments use fourth-order Runge–Kutta. It does not give the exact Euler-step singular norm, exact first-order contractivity interval and minimizer, or the optimal *condition-number-constrained* degree weight and its sharp budget threshold. Carletti et al., arXiv:2410.15338, contains the ancestral Hodge and master-stability decomposition for continuous synchronization, not this numerical discretization or optimization frontier. Targeted publication and mathematical-record searches showed no statement implying the complete claim; a comparison was made at the level of conclusions and parameters, not just titles. Generic numerical energy-stability and matrix-scaling results are relevant background, and potential implicit equivalences in that broad literature remain a residual risk.

## Mathematical value — PASS

For a directionally coupled gradient flow, an asymptotically stable discrete method can increase error in the ordinary Euclidean norm at **every** stepsize. The natural metric that certifies best spectral behavior can itself be poorly conditioned. The exact budget frontier provides a nontrivial engineering and analytical choice: how much norm distortion is needed for guaranteed one-step dissipation, how to select the best finite step under that restriction, and what transient Euclidean prefactor is certified. The filled-triangle example distinguishes a strict contractivity budget greater than \(256/9\) from the full-symmetrization budget \(256\). This is a natural complete classification rather than an arbitrary numerical cutoff or a rephrasing of the continuous-time spectral threshold.

## Closest literature and limitations

- Rodríguez-Camargo et al. (2026), arXiv:2610.22628v1, relevant primary full-text passages inspected, especially Sections 4.1–4.3 and 5.
- Carletti et al. (2024), arXiv:2410.15338, primary arXiv full text inspected at boundary-operator and singular-mode passages; not read cover-to-cover.
- Ranocha and Ketcheson (2020), arXiv:1909.13215, and Braatz and Morari (1994), DOI:10.1137/S0363012992238680, general energy-stability and matrix-scaling background; possible unindexed or implicit specialization has not been ruled out.

Only exact arithmetic, isotropic quadratic gradients, forward Euler, real chain matrices, and the reciprocal degree-weight family are covered. No independent verification or validation is asserted.

Self-review: passed. Independent audit: not yet performed.
