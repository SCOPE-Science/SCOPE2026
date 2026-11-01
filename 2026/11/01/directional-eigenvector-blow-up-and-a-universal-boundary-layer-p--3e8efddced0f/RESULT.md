# Directional eigenvector blow-up and a universal boundary-layer profile for elliptic Bergman Toeplitz operators

## Finding

The eigenvectors of an elliptic, tridiagonal Bergman Toeplitz operator have an exactly computable direction-dependent norm-divergence exponent, coefficient, and probability-density profile. Specifically, for \(T=T_{a\bar z+b+cz}\) on the normalized analytic Bergman space with \(a\ne0\) and \(|c|<|a|\), take the interior spectral path
\[
\lambda_{r,\theta}=b+r(ae^{-i\theta}+ce^{i\theta}),\qquad 0<r<1.
\]
There is a unique eigenfunction \(f_{r,\theta}\) satisfying \(Tf_{r,\theta}=\lambda_{r,\theta}f_{r,\theta}\) and \(f_{r,\theta}(0)=1\). Put
\[
\rho=c/a,\quad q_\theta=\rho e^{2i\theta},\quad
\gamma_\theta=1+\frac1{1-q_\theta},\quad
s_\theta=\operatorname{Re}\frac1{1-q_\theta},\quad
\kappa_\theta=\operatorname{Re}\frac{1+q_\theta}{1-q_\theta}.
\]
Here \(s_\theta>0\) and \(\kappa_\theta>0\). For fixed \(\theta\), and uniformly over all \(\theta\in\mathbb R\),
\[
\lim_{r\uparrow1}(1-r)^{s_\theta}\|f_{r,\theta}\|_{A^2}
=C_\theta>0,
\qquad
C_\theta^2=
\frac{\Gamma(2s_\theta)}{|\Gamma(\gamma_\theta)|^2(2\kappa_\theta)^{2s_\theta}}
\left|(1-q_\theta)^{-(3-\gamma_\theta)}\right|^2.
\]
All complex powers use the principal logarithm, which is unambiguous since \(|q_\theta|<1\).

Writing \(\tau=|c/a|\), the directional exponents fill exactly the interval
\[
\frac1{1+\tau}\le s_\theta\le\frac1{1-\tau};
\qquad \frac1{2\pi}\int_0^{2\pi}s_\theta\,d\theta=1.
\]
Both bounds are attained. The sharp anisotropy determines \(\tau\) through \(\tau=(s_{\max}-s_{\min})/(s_{\max}+s_{\min})\).

There is also a **universal microscopic concentration law**. For \(r\) sufficiently close to \(1\), let \(u=u_{r,\theta}\) be the root near \(e^{-i\theta}\) of
\[
X^2-r(e^{-i\theta}+\rho e^{i\theta})X+\rho=0.
\]
Set \(\delta=1-|u|\), \(\zeta=\bar u/|u|\), and define the probability measure
\[
\nu_{r,\theta}(dz)=\frac{|f_{r,\theta}(z)|^2}{\|f_{r,\theta}\|_{A^2}^2}\,\frac{dx\,dy}{\pi},
\qquad W_{r,\theta}(z)=\frac{1-\bar\zeta z}{\delta}.
\]
The push-forward of \(\nu_{r,\theta}\) by \(W_{r,\theta}\) converges weakly on \(\mathbb C\) to the probability density on the open right half-plane \(H=\{X+iY:X>0\}\)
\[
\boxed{\;
\frac{2^{2s_\theta}|\Gamma(\gamma_\theta)|^2}{\pi\Gamma(2s_\theta)}
\left|1+X+iY\right|^{-2(1+s_\theta)}
\exp\!\big(2\operatorname{Im}(\gamma_\theta)\operatorname{Arg}(1+X+iY)\big)
\,dX\,dY\;},
\]
and has zero density outside \(H\). In the original disk coordinates, \(\nu_{r,\theta}\) converges weakly to the point mass at \(e^{i\theta}\).

## Assumptions and scope

The analytic Bergman space \(A^2(\mathbb D)\) uses normalized planar area \(dA=dx\,dy/\pi\), so \(\|z^n\|^2=1/(n+1)\). The Toeplitz operator \(T_\psi f=P_{A^2}(\psi f)\) is bounded because the affine harmonic symbol \(\psi(z)=a\bar z+b+cz\) is bounded on the disk. Parameters \(a,b,c\) are arbitrary complex numbers satisfying \(a\ne0\) and the strict sense-reversal assumption \(|c/a|<1\); \(\theta\) is any real angle. Limits concern \(r\uparrow1\) and are not asserted when \(|c|=|a|\). The boundary-layer measure statement is weak convergence against bounded continuous tests, and does not assert convergence of every unbounded moment.

## Proof

**1. Eigenfunction recurrence and local factorization.** Write \(f(z)=\sum_{n\ge0}f_n z^n\). The Bergman projection identity \(T_{\bar z}(z^{n+1})=(n+1)z^n/(n+2)\) shows that \(Tf=\lambda f\) is equivalent to
\[
a\frac{n+1}{n+2}f_{n+1}+bf_n+cf_{n-1}=\lambda f_n,\qquad n\ge0,\quad f_{-1}=0.\]
Fixing \(f_0=1\) determines the entire Taylor sequence, so any normalized eigenfunction is unique. Multiplying the recurrence by \((n+2)z^n\) and summing yields the first-order equation
\[
\big(a-(\lambda-b)z+cz^2\big)f'(z)
+\big(-2(\lambda-b)+3cz\big)f(z)=0.
\]
On the elliptic path, factor
\[
a-(\lambda_{r,\theta}-b)z+cz^2=a(1-uz)(1-vz),\quad
u+v=r(e^{-i\theta}+\rho e^{i\theta}),\quad uv=\rho.
\]
The letter \(u\) here denotes the root approaching \(e^{-i\theta}\); \(v\) approaches \(\rho e^{i\theta}\). For all \(r\) sufficiently near \(1\), these roots are distinct and lie strictly inside the disk. (Indeed at \(r=1\) their moduli are respectively \(1\) and \(|\rho|<1\); the inward radial derivative of the first root is strictly positive, computed below.) Define
\[
g_{r,\theta}=\frac{2u-v}{u-v}.
\]
The unique normalized analytic solution for \(r\) sufficiently near \(1\) is
\[
f_{r,\theta}(z)=(1-uz)^{-g_{r,\theta}}
(1-vz)^{-(3-g_{r,\theta})}.
\]
Both factors are holomorphic past the closed unit disk for each such \(r\), hence belong to \(A^2\). Uniqueness of the recurrence establishes the eigenvalue identity without importing any spectral completeness assertion.

**2. Root and exponent expansions.** Differentiating the two root identities at \(r=1\) gives
\[
\left.\frac{u'}u\right|_{r=1}
=\frac{1+q_\theta}{1-q_\theta},\qquad
u_{1,\theta}=e^{-i\theta},\quad v_{1,\theta}=\rho e^{i\theta}.
\]
Since \(\operatorname{Re}((1+q)/(1-q))=(1-|q|^2)/|1-q|^2>0\),
\[
1-|u|^2=2\kappa_\theta(1-r)+O((1-r)^2),\qquad
 g_{r,\theta}=\gamma_\theta+O(1-r).
\]
The error bounds are uniform in \(\theta\), since \(|\rho|<1\) keeps the two limiting roots uniformly apart. Moreover \(\operatorname{Re}\gamma_\theta=1+s_\theta>1\), uniformly in \(\theta\).

**3. Singular Bergman norm.** For \(\operatorname{Re}g>1\), the Taylor series of the singular factor gives the exact identity
\[
\left\|(1-uz)^{-g}\right\|_{A^2}^2
=\sum_{n=0}^\infty\frac{|(g)_n|^2}{(n!)^2(n+1)}|u|^{2n}.
\]
The Gamma ratio \((g)_n/n!=n^{g-1}\Gamma(g)^{-1}(1+O(1/n))\), uniformly for \(g\) in compact subsets of \(\{\operatorname{Re}g>1\}\), together with the Abelian theorem for power sums, implies
\[
\left\|(1-uz)^{-g}\right\|_{A^2}^2
\sim\frac{\Gamma(2\operatorname{Re}g-2)}{|\Gamma(g)|^2}
(1-|u|^2)^{-(2\operatorname{Re}g-2)}.
\]
The normalized squared kernel densities concentrate weakly at \(z=\bar u/|u|\): outside any fixed neighborhood of this point, the singular factor stays uniformly bounded, while its total norm tends to infinity. The other factor \(h_r(z)=(1-vz)^{-(3-g)}\) and its inverse are uniformly bounded and continuous on the closed disk, with \(h_r(\bar u/|u|)\to(1-q_\theta)^{-(3-\gamma_\theta)}\). Thus multiplying by \(h_r\) multiplies the leading squared norm by \(|h_0(e^{i\theta})|^2\).

Finally \((\operatorname{Re}g_{r,\theta}-\operatorname{Re}\gamma_\theta)\log(1-|u|^2)\to0\), so the variable exponents may be replaced by their limits. Substituting the root expansion gives the asserted \(C_\theta\) and the exponent \(s_\theta\). The compactness of the angle circle makes this argument uniform in \(\theta\).

**4. Directional extremizers.** Put \(\tau=|\rho|\). The elementary Poisson identity
\[
\operatorname{Re}\frac1{1-q}=
\frac12+\frac12\frac{1-\tau^2}{|1-q|^2}
\]
shows that the largest and smallest values, respectively, occur when \(q=\tau\) and \(q=-\tau\) (when \(\tau=0\) all angles are equivalent). Their values are \(1/(1-\tau)\) and \(1/(1+\tau)\). Expansion of \(1/(1-\rho e^{2i\theta})\) into a uniformly convergent geometric series proves the mean-one identity. Solving the endpoint equations gives the contrast-recovery formula.

**5. Exact half-plane concentration profile.** Write \(\delta=1-|u|\), \(\zeta=\bar u/|u|\). The transformation \(z=\zeta(1-\delta W)\) has Jacobian \(\delta^2\), maps the disk onto \(2\operatorname{Re}W>\delta|W|^2\), and gives the **exact** identity
\[
1-uz=\delta\big(1+(1-\delta)W\big).
\]
Its push-forward density, before normalization, is therefore
\[
\frac{\delta^{2-2\operatorname{Re}g}}\pi
|1+(1-\delta)W|^{-2\operatorname{Re}g}
 e^{2\operatorname{Im}g\operatorname{Arg}(1+(1-\delta)W)}
|h_r(\zeta(1-\delta W))|^2\,
\mathbf1_{\{2\operatorname{Re}W>\delta|W|^2\}}.
\]
The norm asymptotic in Step 3 with \(1-|u|^2\sim2\delta\) yields, after division by the squared norm, the stated limiting density. To justify limiting the full measures, note that inside their supports \(\operatorname{Re}W>0\) and
\[
|1+(1-\delta)W|\ge(1-\delta)|1+W|.
\]
For small \(\delta\), \(\operatorname{Re}g>1+\varepsilon\) uniformly, the imaginary parts of \(g\) are bounded, and \(h_r\) is uniformly bounded. The push-forward densities are consequently dominated by a constant multiple of \(|1+W|^{-2(1+\varepsilon)}\) on the right half-plane, an integrable function. Dominated convergence proves total-variation convergence of the rescaled densities after extension by zero (and hence weak convergence). The same kernel concentration argument in Step 3 proves the unscaled weak limit \(\delta_{e^{i\theta}}\). As the original densities have mass one, the limiting half-plane density is automatically normalized.

## Verification

The standalone program `check_boundary.py` reproduces the normalized Taylor recurrence, checks the associated first-order ODE coefficient residuals for a nonreal parameter, verifies the exact \(c=0\) Bergman norm, compares three different real-parameter asymptotic constants over shrinking radial gaps, and independently samples the sharp exponent extrema and its angular mean. Its passing finite tests corroborate, but do **not** certify, the infinite-dimensional asymptotic theorem. The arguments in the Proof establish the infinite limits independently of numerical experiments.

## Relationship to prior work

Abad, *On the dynamics of Toeplitz operators over Bergman spaces* (first posted 2026-09-18), supplies the sense-reversing point-spectrum/eigenvector setting and resolves eigenvector completeness and hypercyclicity for affine harmonic symbols. The differential equation and its eigenvector solutions belong to this prior setting; the present assertion is the sharp **directional norm asymptotic**, its explicit Gamma coefficient, complete anisotropy range, and microscopic half-plane profile of normalized eigenvector mass. Leng–Zhang–Zhao (2026) and Cui–Lu–Yang–Zu (2025) study Bergman Toeplitz dynamics and coefficient recurrences, but their inspected results do not supply these boundary-normalization laws. Related Bergman kernel boundary estimates do not imply the exponent \(s_\theta\) when \(c\ne0\). These comparisons support a best-knowledge originality judgment rather than guaranteeing priority against all unindexed work.

## Limitations

The strict \(|c|<|a|\) assumption is essential for the nondegenerate ellipse and root separation. The theorem concerns the specifically normalized eigenfunctions \(f(0)=1\); unit-norm eigenfunctions have no divergent norm. The microscopic profile is only a weak/total-variation limit of rescaled densities, not a convergence claim for arbitrary unbounded observables. The result does not classify Jordan chains, boundary eigenvalues, operator resolvent growth, or hypercyclic vectors. Earlier implicit equivalent estimates or unindexed literature remain a publication-priority risk. Independent mathematical validation has not been performed.

## References

1. O. Abad, *On the dynamics of Toeplitz operators over Bergman spaces*, arXiv:2609.22017v1 (first public 2026-09-18). https://arxiv.org/abs/2609.22017
2. Q. Leng, X. Zhang, and X. Zhao, *Hypercyclic Bergman-Toeplitz operators with some harmonic symbols*, arXiv:2609.32650v1 (2026). https://arxiv.org/abs/2609.32650
3. P. Cui, Y. Lu, R. Yang, and C. Zu, *Spectral properties of Toeplitz operators with harmonic function symbols on the Bergman space*, arXiv:2512.16952v1 (2025). https://arxiv.org/abs/2512.16952
4. K. Guo, X. Zhao, and D. Zheng, *The spectral picture of Bergman Toeplitz operators with harmonic polynomial symbols*, arXiv:2007.07532 (2020). https://arxiv.org/abs/2007.07532
