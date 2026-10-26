# Universal endpoint logarithms for zeros of band-limited stationary Gaussian analytic functions

## Finding

Let \(E\) be a nonempty finite union of disjoint closed circular arcs, with all arc lengths and intervening gap lengths strictly positive. Write \(\ell=|E|\in(0,2\pi)\) for total angular length and \(J\ge2\) for the number of endpoints, so \(J\) is even. Let \((\xi_n)_{n\in\mathbb Z}\) be a centered stationary proper complex Gaussian process with normalized spectral measure
\[
 d\mu_E(\phi)=\ell^{-1}{\mathbf1}_E(\phi)\,d\phi.
\]
Define \(f(z)=\sum_{n\ge0}\xi_nz^n\), and let \(N_f(r)\) count zeros in \(|z|<r\), including multiplicity. Then as \(r\uparrow1\),
\[
 \boxed{\mathbb E N_f(r)=\frac{\ell}{2\pi}\frac{r^2}{1-r^2}
 +\frac{J}{4\pi^2}\log\frac1{1-r}+O_E(1).}
\]
Thus the **positive** coefficient of the logarithmic correction is exactly one quarter of \(\pi^{-2}\) per spectral-band endpoint; it depends on the number of endpoints, not their locations or the band lengths.

There is also a universal interface profile. Let \(\theta_*\) be an endpoint and define \(\sigma=+1\) if the band lies locally on its increasing-angle side, and \(\sigma=-1\) otherwise. For the expected planar zero intensity \(\rho(z)\), put
\[
 F_\sigma(x)=\tfrac12+\pi^{-1}\arctan(\sigma x).
\]
Then, uniformly for \(x\) in every compact subset of \(\mathbb R\),
\[
 \boxed{\lim_{r\uparrow1}\pi(1-r^2)^2\rho\bigl(re^{i(\theta_*+(1-r)x)}\bigr)
 =1-\frac1{\pi^2(1+x^2)F_\sigma(x)^2}.}
\]
The right side tends to zero on the spectral-gap side and to one on the band side. In particular, at the endpoint it equals \(1-4/\pi^2\).

## Assumptions and scope

All angular integrations use Lebesgue measure on \(\mathbb R/(2\pi\mathbb Z)\). Arcs and gaps are fixed as \(r\) tends to one; no uniform claim is made when endpoints coalesce. Proper means that all Gaussian pseudocovariances vanish. The spectral probability measure above defines a stationary process with variance one and covariances \(\gamma(k)=\ell^{-1}\int_E e^{-ik\phi}\,d\phi\). Since each \(\xi_n\) has finite, fixed Gaussian variance, the series converges almost surely on the unit disk. The covariance is nondegenerate there and therefore \(\rho\) is well-defined. The statements concern the expected zero count and expected density, not almost-sure individual realizations, counting variance, or limiting point-process correlations.

## Proof

**1. Exact covariance and zero-count identity.** Put \(t=1-r\), let
\[
 P_r(s)=\frac{1-r^2}{1-2r\cos s+r^2},\qquad
 u_t(\theta)=\frac1{2\pi}\int_E P_{1-t}(\theta-\phi)\,d\phi.
\]
The Gaussian covariance on the diagonal is exactly
\[
 K(re^{i\theta},re^{i\theta})
 =\frac{2\pi}{\ell}\frac{u_t(\theta)}{1-r^2}.
\]
In particular \(0<u_t(\theta)<1\) for \(0<t<1\). The Edelman–Kostlan identity, followed by Green's theorem, gives
\[
 \mathbb E N_f(r)
 =\frac r2\,\partial_r\left\langle\log K(re^{i\theta},re^{i\theta})\right\rangle
 =\frac{r^2}{1-r^2}-\frac r2\left\langle\frac{\partial_tu_t}{u_t}\right\rangle,
 \quad\langle q\rangle=\frac1{2\pi}\int_0^{2\pi}q(\theta)\,d\theta.
\]
Here \(\partial_t\) is taken with the angular argument fixed.

**2. A uniform off-interface Poisson estimate.** Let \(d(\theta)\) be the shortest angular distance from \(\theta\) to an endpoint of \(E\). Choose a fixed large \(L\) and let \(B_t=\{\theta:d(\theta)<Lt\}\). The exact formula
\[
 P_{1-t}(s)=\frac{2t-t^2}{t^2+2(1-t)(1-\cos s)}
\]
shows, whenever the circular distance of \(s\) from zero is at least \(d\ge Lt\), that
\[
 P_{1-t}(s)=\frac{t}{1-\cos s}\left[1+O_E\left(t+\frac{t^2}{d^2}\right)\right],
 \qquad
 \partial_tP_{1-t}(s)=\frac{1}{1-\cos s}\left[1+O_E\left(t+\frac{t^2}{d^2}\right)\right].
\]
The constants here can be chosen independently of \(d,t,s\) in the displayed range. Also, directly differentiating the positive kernel shows
\[
 |\partial_tP_{1-t}(s)|\le\frac C tP_{1-t}(s).
\]
By positivity, \(|\partial_t\log u_t|\le C/t\) everywhere. Consequently, \(B_t\), whose measure is \(O_E(t)\), contributes only \(O_E(1)\) to integrals of \(\partial_t\log u_t\) and of its difference from \(t^{-1}\).

**3. The gap and band contributions.** On \(E^c\setminus B_t\), set
\[
 H_0(\theta)=\frac1{2\pi}\int_E\frac{d\phi}{1-\cos(\theta-\phi)}.
\]
The estimates in Step 2 yield \(u_t=tH_0[1+O_E(t+t^2/d^2)]\) and the analogous derivative relation. Hence
\[
 \frac{\partial_tu_t}{u_t}=\frac1t+O_E\left(1+\frac{t}{d^2}\right).
\]
The error integrates to \(O_E(1)\), because each gap endpoint contributes at most \(\int_{Lt}^{c}t d^{-2}\,dd=O(1)\). Adding back \(B_t\) gives
\[
 \int_{E^c}\partial_t\log u_t\,d\theta=\frac{2\pi-\ell}{t}+O_E(1).
\]
On \(E\setminus B_t\), let \(v_t=1-u_t\), and define
\[
 H_1(\theta)=\frac1{2\pi}\int_{E^c}\frac{d\phi}{1-\cos(\theta-\phi)}.
\]
Then \(v_t=tH_1[1+O_E(t+t^2/d^2)]\), with the analogous derivative estimate, and \(v_t\le C_Et/d\). Increasing the fixed constant \(L\) if necessary ensures \(v_t\le1/2\). Thus
\[
 \frac{\partial_tu_t}{u_t}=-H_1(\theta)
 +O_E\left(\frac t d+\frac{t^2}{d^3}+\frac t{d^2}\right).
\]
All displayed error terms are integrable over \(d\ge Lt\), with integrals bounded independently of \(t\). At each endpoint, when approached from within the band, elementary integration of \((1-\cos s)^{-1}\) gives
\[
 H_1(\theta)=\frac1{\pi d(\theta)}+O_E(1).
\]
There is exactly one such band-side singularity for each of the \(J\) endpoints. Therefore
\[
 \int_E\partial_t\log u_t\,d\theta
 =-\frac J\pi\log\frac1t+O_E(1).
\]
Combining the two disjoint regions proves the **integrated logarithmic-derivative law**
\[
 \left\langle\partial_t\log u_t\right\rangle
 =\frac{2\pi-\ell}{2\pi t}-\frac J{2\pi^2}\log\frac1t+O_E(1).
\]
Substitution into Step 1, together with \(r=1-t\) and \(r^2/(1-r^2)=1/(2t)+O(1)\), yields the claimed global asymptotic, including its bounded remainder.

**4. The local hard-edge profile.** Choose an endpoint \(\theta_*\) and use the rescaled angular coordinate \(\theta=\theta_*+tx\). On this scale,
\[
 tP_{1-t}(ty)\longrightarrow\frac{2}{1+y^2},
\]
with the corresponding differentiated kernel limits, uniformly under the integrals on compact rescaled sets. The other endpoints stay a fixed positive distance away. Hence, uniformly for bounded \(x\),
\[
 u_t(\theta_*+tx)\to F_\sigma(x),\qquad
 t\partial_\theta u_t(\theta_*+tx)\to\frac{\sigma}{\pi(1+x^2)},\qquad
 t\partial_t u_t(\theta_*+tx)\to-\frac{\sigma x}{\pi(1+x^2)}.
\]
The derivatives are evaluated before substituting \(\theta=\theta_*+tx\). Since \(u_t\) is a positive harmonic function on the disk, \(\Delta\log u_t=-|\nabla u_t|^2/u_t^2\). Applying Edelman–Kostlan once more gives the exact identity
\[
 \pi(1-r^2)^2\rho(re^{i\theta})
 =1-\frac{(1-r^2)^2}{4u_t(\theta)^2}
 \left[(\partial_ru_t)^2+r^{-2}(\partial_\theta u_t)^2\right].
\]
The three limits above now give the displayed universal interface profile and compact-uniform convergence.

## Verification

Run `python3 hard_edge_checker.py` (requires Python 3, NumPy and SciPy). The script compares the explicit arc Poisson-integral formula against independent numerical quadrature, checks its radial and angular derivatives and a finite geometric-series covariance approximation, verifies the local edge profile, and estimates the logarithmic coefficient for one- and two-band masks. On the reviewed package it passed 169 numerical assertions. These finite numerical checks do not establish the infinite-radius asymptotic or its \(O_E(1)\) remainder; these rely on Steps 1–4.

For a single half-circle spectral band, \(\ell=\pi\) and \(J=2\), so the logarithmic coefficient is \(1/(2\pi^2)\). For two separated bands it is \(1/\pi^2\), irrespective of their lengths or gaps. The conclusion applies to any fixed finite union as specified above, not only the tested examples.

## Relationship to prior work

Noda and Shirai [1] establish the stationary Gaussian analytic framework, the expected-zero inequality and sharp asymptotics when the spectral density is a nonnegative trigonometric polynomial. Such a polynomial cannot equal the discontinuous indicator of a proper union of arcs, and their stated asymptotics do not imply the endpoint logarithm here.

Shirai [2] treats stationary spectral densities and includes **the identical half-circle spectral mask** as Example 2.4, where a fixed-direction zero-intensity limit is calculated on the interior of a spectral gap. Its Theorem 2.1 assumes smoothness at the fixed approached direction; neither that theorem nor the example gives the joint scale \(\theta=\theta_*+(1-r)x\), the global logarithmic term, or a multi-band endpoint-count law. The overlap in the model is therefore acknowledged rather than treated as irrelevant.

Positive-to-positive spectral jumps also have a logarithmic zero-count correction, but both one-sided spectral values must be positive; setting one to zero makes its coefficient singular and does not produce this hard-edge theorem. The hard-edge coefficient here has the opposite sign relative to the support-fraction leading term.

## Limitations

The band indicator is exactly constant and positive on each component and zero on its complement; arbitrary edge-vanishing powers, rough fractal supports, different positive band heights, or a number of endpoints growing with \(r\) are not treated. The \(O_E(1)\) constant may deteriorate as two endpoints approach each other. Nothing is claimed about fluctuations or almost-sure zero counting. The proof is analytical and the included numerical checks are only corroborative. Although targeted literature and database searches did not identify an equivalent global endpoint logarithm, unindexed or implicit earlier derivations remain a historical-priority risk.

## References

[1] Kohei Noda and Tomoyuki Shirai, *Expected number of zeros of random power series with finitely dependent Gaussian coefficients*, arXiv:2106.02860v1 (first publicly posted 2021-06-05), Theorems 1.1–1.3, Section 2.

[2] Tomoyuki Shirai, *The density of zeros of random power series with stationary complex Gaussian coefficients*, arXiv:2501.02586v1 (first publicly posted 2025-01-05), Theorem 2.1, Example 2.4, Proposition 3.1. A later arXiv revision retains the relevant example and framework.
