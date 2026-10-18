# Sharp singularity tails and contrasting optimal designs for random rectangle support data

## Finding
Let \(K_{a,b}=[-a,a]\times[-b,b]\subset\mathbb R^2\), where \(a,b>0\). For \(m\ge2\) independently sampled support-function directions, fold their angles into \([0,L]\), where \(L=\pi/2\). Suppose the folded angle has a continuous probability density \(f\) on \([0,L]\), and form the \(m\)-by-\(2\) matrix \(X\) with rows \((\cos\theta_j,\sin\theta_j)\). Let \(\lambda=\lambda_{\min}(X^{\mathsf T}X)\), and let \(\omega_d=\pi^{d/2}/\Gamma(1+d/2)\) denote the volume of the unit \(d\)-ball.

The **exact small-conditioning tail** is
\[
\lim_{\varepsilon\downarrow0}\frac{\Pr\{\lambda\le\varepsilon^2\}}{\varepsilon^{m-1}}
=\sqrt m\,\omega_{m-1}\int_0^L f(t)^m\,dt.
\]
The coefficient is minimized uniquely among continuous probability densities by the uniform law \(f\equiv2/\pi\), with optimum \(\sqrt m\,\omega_{m-1}(2/\pi)^{m-1}\). In every such continuous design, \(\mathbb E[\lambda^{-s}]<\infty\) holds exactly when \(0<s<(m-1)/2\). Therefore, with centered Gaussian observation errors independent of the sampled directions, independent across observations, and of common variance \(\sigma^2>0\), the **unconstrained ordinary least-squares** estimator of \((a,b)\) exists uniquely almost surely for \(m\ge2\), but its unconditional squared Euclidean error is finite exactly when \(m\ge4\).

For contrast, let \(\nu\) be *any* probability distribution on folded angles, including atomic measures, and put \(\mu_\nu=\int_0^L e^{2it}\,\nu(dt)\). The expected Gram determinant obeys
\[
\mathbb E_\nu\det(X^{\mathsf T}X)
=\frac12\binom m2(1-|\mu_\nu|^2).
\]
It is maximized **uniquely** by \(\nu_*=(\delta_0+\delta_L)/2\). Under this mean-determinant-optimal design, the data matrix is singular with probability exactly \(2^{1-m}\), whereas every continuous angular law has rank two almost surely. Thus optimal *average determinant* and optimal *small-singularity tail* select opposed designs.

## Assumptions and scope
For each unit direction \(u=(u_1,u_2)\), the support function satisfies \(h_{K_{a,b}}(u)=a|u_1|+b|u_2|\). Folding a direction to \(\theta\in[0,\pi/2]\) makes its support observation a linear measurement \(a\cos\theta+b\sin\theta\). The family consists of centered, axis-aligned, nondegenerate rectangles; side half-lengths are regarded as unrestricted real regression parameters **only when defining ordinary least squares**, and the statistical risk theorem is not asserted for positivity-constrained estimators. All angular draws are independent and identically distributed; the initial density \(f\) is continuous, nonnegative, normalized to integral one, and may vanish at some angles. No Gaussian assumption is needed for the geometric tail or for the determinant identity.

## Proof
**1. Spectral identity and rank-loss set.** Set \(z_j=e^{2i\theta_j}\) and \(S=\sum_j z_j\). Elementary double-angle identities give
\[
X^{\mathsf T}X=\frac12\begin{pmatrix}m+\Re S&\Im S\\\Im S&m-\Re S\end{pmatrix},\qquad
\lambda=\frac{m-|S|}{2}.
\]
Because all angles belong to an interval of length \(\pi/2\), equality \(|S|=m\) holds precisely when all \(\theta_j\) coincide. Thus a continuous i.i.d. design is full rank almost surely.

**2. Orthogonal tubular coordinates.** Write \(\theta_j=t+z_j\), where \(t=m^{-1}\sum_j\theta_j\) and \(z\) belongs to the \((m-1)\)-dimensional Euclidean hyperplane \(H=\{z\in\mathbb R^m:\sum_j z_j=0\}\). The Euclidean Jacobian is \(\sqrt m\,dt\,dz_H\). Uniform Taylor expansion at \(z=0\) gives
\[
\sum_j e^{2iz_j}=m-2\|z\|^2+O(\|z\|^3),\qquad
\lambda(t+z)=\|z\|^2+O(\|z\|^4).
\]
The latter expansion uses that the cubic term is imaginary, so its contribution to the modulus begins at sixth order. Compactness of the angular cube and uniqueness of the rank-loss diagonal ensure that \(\{\lambda\le\varepsilon^2\}\) lies in a shrinking tubular neighborhood of \(z=0\). Rescale \(z=\varepsilon w\). Uniform quadratic control bounds \(w\), and the indicator of \(\lambda\le\varepsilon^2\) converges almost everywhere to the indicator of the unit ball in \(H\). The density product converges to \(f(t)^m\). Angular-cube boundary truncations affect only the endpoints \(t=0,L\), a null set. Dominated convergence proves
\[
\Pr\{\lambda\le\varepsilon^2\}=\varepsilon^{m-1}\sqrt m\,\omega_{m-1}\int_0^L f(t)^m\,dt+o(\varepsilon^{m-1}).
\]

**3. Sharp design and inverse moments.** Strict convexity of the power \(x\mapsto x^m\) and Jensen's inequality yield \(\int_0^L f^m\ge L^{1-m}\), with equality exactly for constant \(f\). Since a continuous probability density has strictly positive \(m\)-th integral, the displayed tail has a positive finite constant. The layer-cake integral for \(\lambda^{-s}\) consequently converges at the origin exactly if \(s<(m-1)/2\); away from the origin \(\lambda\) is bounded above and the integral is harmless. Conditionally on \(X\), the unconstrained least-squares coefficient error has covariance \(\sigma^2(X^{\mathsf T}X)^{-1}\). Its conditional squared Euclidean risk is \(\sigma^2(\lambda^{-1}+(m-\lambda)^{-1})\), and the second term is bounded by \(2\sigma^2/m\). Thus unconditional risk is finite precisely when \(m>3\).

**4. The opposed average-determinant optimum.** By Cauchy–Binet,
\[
\det(X^{\mathsf T}X)=\sum_{1\le i<j\le m}\sin^2(\theta_i-\theta_j).
\]
Independence gives \(\mathbb E\sin^2(\theta_i-\theta_j)=(1-|\mu_\nu|^2)/2\), proving the determinant formula. Since \(\Im\mu_\nu=\int_0^L\sin(2t)\,\nu(dt)\ge0\), the only way \(\mu_\nu\) can vanish is for \(\nu\) to be supported on \(\{0,L\}\), and vanishing of its real part then forces equal masses. A zero value of \(\mu_\nu\) is attainable, so this is the unique global maximizer. Under the resulting Bernoulli design the matrix has rank one exactly when all \(m\) rows select the same endpoint; this happens with probability \(2(1/2)^m=2^{1-m}\).

## Verification
The accompanying standalone `check.py` (Python standard library only) checks the spectral and Cauchy–Binet determinant identities on pseudorandom samples of \(m=2,\ldots,8\); checks numerical integration against the exact two-sample uniform CDF; and compares Monte Carlo tails and mean determinants with the derived asymptotic and expectation formulas. For two uniform folded angles, the exact special-case CDF is
\[
\Pr\{\lambda\le t\}=\frac{2\alpha(t)}L-\left(\frac{\alpha(t)}L\right)^2,\qquad \alpha(t)=\arccos(1-t),\quad0\le t\le1.
\]
This has leading constant \(4\sqrt2/\pi\) in the \(\varepsilon\)-tail, agreeing with the theorem at \(m=2\). Computational checks are corroborative only and are not offered as proofs of any all-sample-size or all-density statement.

## Relationship to prior work
Dostert and Jochemko [1] introduced fixed-facet-direction support-function regression, quadratic-program reconstruction, uniqueness criteria, and asymptotic convergence; the centered-rectangle design here is a two-parameter specialization. The new claims concern the *exact finite-sample conditioning tail*, its leading-coefficient design optimizer, the inverse-risk sample threshold, and the contrast with the globally optimal expected determinant. General random-matrix lower-tail estimates such as [2,3] concern substantially different entry/independence hypotheses and do not supply this constant or design classification. Classical optimal-design theory provides broader context for maximizing information-matrix determinants; the elementary mean-determinant identity alone should not be interpreted as a new general optimal-design principle.

## Limitations
The tail formula is proved for independent folded angles with a continuous density, not singular or mixed measures; the determinant statement does permit all measures. The regression-risk threshold assumes homoscedastic Gaussian noise independent of the sampled directions and *unconstrained* ordinary least squares; it does not establish a risk divergence for geometrically constrained, truncated, or regularized estimators. It also does not estimate noise variance or address unknown rectangle orientation or position. The same-order exponent and the four-sample risk threshold may have general statistical analogues; no claim is made that these broad phenomena were first discovered here. An equivalent earlier calculation in circular-design or tubular-neighborhood literature cannot be completely excluded.

## References
[1] M. Dostert and K. Jochemko, *Learning polytopes with fixed facet directions*, arXiv:2201.03419, initially posted 10 January 2022; sections 1, 3.2, 4, and 5. https://arxiv.org/abs/2201.03419

[2] M. Rudelson and R. Vershynin, *The smallest singular value of a random rectangular matrix*, Communications on Pure and Applied Mathematics 62 (2009), 1707–1739. https://doi.org/10.1002/cpa.20294

[3] M. Dabagia and M. Fernandez, *The smallest singular value of inhomogenous random rectangular matrices*, arXiv:2408.14389, initially posted 26 August 2024. https://arxiv.org/abs/2408.14389
