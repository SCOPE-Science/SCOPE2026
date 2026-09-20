# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The source formulation was checked against arXiv:2609.20641v1: its general weak tests define residual components by pairing with arbitrary functions in the elliptic energy space, and the parameter correction is obtained by ordinary finite-dimensional Gauss–Newton, i.e. Euclidean least squares in those components. The experimental section states that fixed test functions are normalized in the corresponding energy norm.

The frame identity follows directly from the analysis operator: if \(T_Zw=(a(w,z_i))_i\), then \(T_Z^*T_Z=S_Z\), hence \(\|T_Zw\|_2^2=a(S_Zw,w)\). The Gram-weighted identity \(T_Z^*(T_ZT_Z^*)^\dagger T_Z=P_W^a\) is the standard SVD projector identity. Therefore Euclidean measurement norm is a scalar multiple of energy norm on the test span exactly when the frame operator is scalar there, i.e. for a tight frame.

The explicit counterexample is exact. With energy-orthonormal \(\phi_1,\phi_2\), current error \(\phi_2\), tangent \(\phi_1\), and unit tests
\[
z_1=\phi_2,\qquad z_2=(\varepsilon\phi_1+\phi_2)/\sqrt{1+\varepsilon^2},
\]
the Euclidean least-squares data are
\[
b=(1,(1+\varepsilon^2)^{-1/2})^T,\qquad J=(0,\varepsilon(1+\varepsilon^2)^{-1/2})^T,
\]
so \(\xi=1/\varepsilon\). The source sign convention updates by subtracting \(\xi\), giving energy error \(\sqrt{1+\varepsilon^{-2}}\). The model is linear, so there is no omitted higher-order term. The exact condition-number formulas follow algebraically from the eigenvalues \(1\pm(1+\varepsilon^2)^{-1/2}\) of the two-test Gram matrix. The standalone numerical artifact reproduces all identities to floating-point precision.

## Originality

**PASS, narrowly scoped.** The broad phenomenon that classical variational neural residual losses depend on the chosen test basis is prior art. In particular, Rojas et al., *Robust Variational Physics-Informed Neural Networks* (CMAME 425, 2024; arXiv:2308.16910), explicitly identify basis dependence, note that rescaling a basis function can cause catastrophic behavior, and use a discrete dual norm with an inverse Gram matrix to obtain basis independence. The 2026 motivating paper itself cites this work. General frame-operator and tight-frame facts are also standard.

Accordingly, none of the following is claimed as new: basis dependence of classical VPINN losses, Gram-inverse/discrete-dual-norm correction, minimum-residual theory, frame operators, or tight frames. The accepted contribution is restricted to the new 2026 weak Gauss–Newton construction: an explicit family in which **every test is already energy-normalized and the test span is fixed**, yet ordinary weak-residual Gauss–Newton produces an unboundedly harmful one-step correction; together with the exact relation between the energy amplification and the test-frame condition number, and the tight-frame characterization of when the source Euclidean metric is energy-consistent.

Searches for the motivating arXiv identifier and for equivalent combinations of weak Gauss–Newton, Gram weighting, unit-normalized tests, fixed test span, frame conditioning, and tight frames found no matching SCOPE record or public correction stating this source-specific result. The full accessible text of RVPINN was inspected around its basis-dependence discussion and Gram-matrix formulation; it establishes the broader mechanism but no unit-normalized fixed-span Gauss–Newton amplification theorem was located. Because the motivating preprint is very recent and because closely related minimum-residual/VPINN literature is large, contemporaneous or specialized prior coverage remains possible. Originality is therefore asserted only to the best of our knowledge.

## Value

**PASS.** The result distinguishes two notions that can otherwise be conflated: normalizing each test vector and conditioning the test frame as a whole. The source's normalization removes arbitrary scalar weights but not near-linear dependence. The counterexample is strong enough to affect the actual Gauss–Newton correction, not merely the numerical value of a loss, and it occurs in a linear elliptic subproblem with a fixed test space. The exact \(\sqrt{\kappa}\)-scale amplification provides a concrete diagnostic: test-frame conditioning is the relevant quantity if ordinary Euclidean weak-residual Gauss–Newton is retained.

## Limitations and residual risk

The result is worst-case and does not establish failure on the motivating benchmarks. It does not analyze damped or regularized Gauss–Newton, trust-region safeguards, or adaptive test-family construction. It also does not prove a new convergence theorem for Gram-weighted Gauss–Newton; that weighting is a known discrete-dual-norm construction. The primary originality risk is an equivalent source-specific counterexample or conditioning estimate in the broader residual-minimization/VPINN literature that was not surfaced by the searches.
