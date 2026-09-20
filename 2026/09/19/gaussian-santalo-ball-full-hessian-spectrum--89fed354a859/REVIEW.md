# Review

## Correctness

**PASS.** The support-function calculation is internally consistent with the translated-ball expansion already established by Artstein-Avidan--Fradelizi--Wyczesany. For a perturbation \(h_t=1+tf\), the Gaussian first factor has
\[
A'(0)=a\int f,\qquad
A''(0)=a\left[-\int|\nabla f|^2+(n-1-q)\int f^2\right],
\]
while the polar factor, using \(\rho_{K_t^\circ}=1/h_t\), has
\[
B'(0)=-a\int f,\qquad
B''(0)=a(n+1-q)\int f^2.
\]
Their first variations cancel. After passing to normalized spherical measure, the resulting logarithmic Hessian is exactly equation (1) in RESULT.md.

Diagonalization by spherical harmonics gives the eigenvalue \(R(2(n-q)-\lambda_\ell)\) for every nonconstant degree \(\ell\), while the constant coefficient is \(2R(n-q-R)\). The identity
\[
R=n-q\frac{I_2}{I_0}>n-q
\]
proves strict negativity of the constant mode. Since \(\lambda_1=n-1\) and \(\lambda_2=2n\), only degree one can change sign, and it does so exactly at \(q=(n+1)/2\). This reproduces the known translated-ball threshold and proves that no other harmonic mode destabilizes first.

The fourth-order endpoint computation uses the exact spherical moments \(\mathbb E Y^2=1/n\) and \(\mathbb E Y^4=3/[n(n+2)]\). The displayed coefficient reduces to a positive bracket because \(R>(n-1)/2\); hence the Gaussian product decreases quartically along actual translations at the critical variance. The record does not infer full endpoint local maximality from this one branch.

## Originality

**PASS, to the best of our knowledge.** The full current version of arXiv:2609.18472 was inspected around its main theorems, Euler--Lagrange equation, and Section 5. Proposition 5.1 computes the quadratic expansion only for translated balls and uses it to show non-maximality for \(\sigma^2>2/(n+1)\). The paper explicitly leaves the higher-dimensional global interval \(1/n<\sigma^2\le2/(n+1)\) open. Searches within the paper found no occurrence of “second variation”, “Hessian”, “spherical harmonic”, or “local maximizer”, and no full support-direction spectrum is stated.

The literature check also covered combinations of Gaussian volume product / weighted Blaschke--Santaló with second variation, Hessian, support-function perturbation, spherical harmonics, and local maximality. No earlier statement of the spectrum (2), the assertion that translations are the unique unstable modes, or the critical fourth-order translated-ball coefficient was located. The 2024 weighted Blaschke--Santaló paper of Colesanti--Kolesnikov--Livshyts--Rotem studies a different symmetric functional framework; it does not provide the present uncentered set-functional Hessian. Cordero-Erausquin's theorem gives global optimality among centrally symmetric convex bodies, which is compatible with negativity of even modes but does not cover the odd non-symmetric translation instability central here.

No specifically identified inaccessible source gives concrete evidence of prior coverage. The principal residual risk is that the motivating September 2026 preprint is extremely recent, so a later revision or an unindexed parallel calculation may state the same second-variation spectrum.

An archive overlap check against the current SCOPE archive found no record indexed by the motivating arXiv identifier, “Gaussian Santaló”, or the corresponding Hessian/spherical-harmonic terminology.

## Value

**PASS.** The result converts a one-direction necessary instability test into the complete infinitesimal phase diagram. It shows that \(2/(n+1)\) is the exact quadratic stability threshold in every dimension and that the transition is purely translational. In the open higher-dimensional global gap \(1/n<\sigma^2<2/(n+1)\), every fixed smooth infinitesimal support perturbation decreases the product to second order, so any global failure of the ball there must be genuinely nonlinear or nonlocal. The critical fourth-order calculation additionally shows that the translation branch itself still points downward at equality.

The spectrum also explains the large-variance limit: degree two and the scaling mode become asymptotically neutral, recovering the affine degeneracies of the classical volume product, while finite Gaussian variance removes them.

## Limitations

This record does not solve the global maximization problem in dimensions \(n\ge3\) for \(1/n<\sigma^2\le2/(n+1)\). It does not establish a topology-uniform quantitative neighborhood of maximality from the Hessian alone. At the endpoint \(\sigma^2=2/(n+1)\), the fourth-order calculation is only for the translation branch; no complete fourth-order normal form is claimed. Very recent or unindexed parallel coverage remains possible.

**Same-model review: passed. Independent audit: not yet performed.**
