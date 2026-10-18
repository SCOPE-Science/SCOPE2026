# A Bessel sign staircase and oscillatory sharp smoothing constants for lattice heat flow

## Finding

Let \(\Delta f(k)=f(k+1)-2f(k)+f(k-1)\) on sequences indexed by \(\mathbb Z\), and \(W_t=e^{t\Delta}\), \(t>0\). Define the endpoint temporal smoothing norm
\[
N(t)=\|\Delta W_t\|_{\ell^\infty(\mathbb Z)\to\ell^\infty(\mathbb Z)}=\|\Delta W_t\|_{\ell^1(\mathbb Z)\to\ell^1(\mathbb Z)}.
\]
Write \(I_n\) for the modified Bessel function of the first kind (nonnegative integer order). Then
\[
N(t)=4e^{-2t}\max_{m\in\mathbb Z_{\ge0}}\bigl(I_m(2t)-I_{m+1}(2t)\bigr).
\]
For every integer \(m\ge1\), exactly one number \(x_m>m^2\) satisfies \(I_m'(x_m)=I_m(x_m)\). Put \(\tau_0=0\), \(\tau_m=x_m/2\). These times increase strictly to infinity, with
\[
\tau_m=\frac{m^2}{2}+\frac14+O(m^{-2})\qquad(m\to\infty).
\]
On \(\tau_m<t<\tau_{m+1}\), the maximum in the exact norm formula occurs uniquely at index \(m\). At \(t=\tau_m\), the two adjacent indices \(m-1,m\) tie. Consequently the sharp \(\ell^\infty\) input is the sign of the time-derivative heat kernel: it is negative on a finite central interval and positive outside (translated or globally negated), with freedom on zeros.

Set \(C=\sqrt{2/(\pi e)}\) and \(\rho(t)=\operatorname{dist}(\sqrt{2t},\mathbb Z+\tfrac12)\), where \(0\le\rho(t)\le\tfrac12\). Then
\[
N(t)=\frac C t\left[1+\frac1t\left(\frac1{12}-\frac{\rho(t)^2}{2}\right)+O(t^{-3/2})\right]\qquad(t\to\infty).
\]
The normalized second-order defect \(t(tN(t)/C-1)\) has the full accumulation interval \([-1/24,1/12]\), so no constant second-order term exists.

## Assumptions and scope

All spaces and operators are over real or complex scalars, on the entire integer lattice with counting measure. The generator is the **unnormalized** nearest-neighbor Laplacian specified above. The time derivative is the bounded generator composition \(\partial_tW_t=\Delta W_t\). The two norm equalities concern the endpoint spaces \(\ell^1\) and \(\ell^\infty\), not general \(\ell^p\). At a threshold \(\tau_m\), signed heat-kernel entries at both \(\pm m\) vanish. The error terms are absolute along positive integer indices or positive real time, respectively.

## Proof

**1. Exact kernel and operator norm.** Fourier inversion or the Bessel generating function gives the probability kernel \(G_t(n)=e^{-2t}I_{|n|}(2t)\) of \(W_t\). Because \(\Delta\) is bounded, its time derivative has convolution kernel \(H_t=\Delta G_t\), which belongs to \(\ell^1\) and has total mass zero. For convolution on \(\ell^1\) and \(\ell^\infty\), the operator norm equals \(\sum_n|H_t(n)|\): the former equality uses an input point mass and the latter uses the bounded pointwise sign input \(f(-n)=\operatorname{sgn}H_t(n)\) at the origin. Put \(x=2t\) and \(L_n(x)=I_n'(x)/I_n(x)\). The Bessel recurrence yields
\[
H_t(n)=2e^{-x}I_{|n|}(x)\bigl(L_{|n|}(x)-1\bigr).
\]

**2. Strict ordering and the unique crossing.** Positivity of \(I_n(x)\) for \(x>0\) permits the logarithmic derivative. Its differential equation is
\[
L_n'(x)=1+\frac{n^2}{x^2}-\frac{L_n(x)}x-L_n(x)^2.
\]
For all \(n\ge0\), \(L_{n+1}>L_n\). Indeed the difference is positive near zero (\(L_n\sim n/x\) for \(n\ge1\), while \(L_0\sim x/2\)); at a hypothetical first zero its derivative would be \((2n+1)/x^2>0\), incompatible with a first nonpositive crossing. Further, \(L_0<1\), because \(I_1(x)<I_0(x)\) follows by integrating the positive weight \(e^{x\cos\theta}(1-\cos\theta)\) on \([0,\pi]\). For every integer \(n\ge1\), \(L_n(x)>1\) for sufficiently small positive \(x\), and \(L_n(x)=1-1/(2x)+O(x^{-2})<1\) for large \(x\). If \(L_n(x)=1\), the Riccati equation gives \(L_n'(x)=(n^2-x)/x^2\). A first zero of \(L_n-1\) cannot occur below \(n^2\), where the derivative points upward. A first zero at \(n^2\) is impossible, since there \(L_n''=-1/n^4<0\) and \(L_n-1\) would be negative immediately to the left. Every zero therefore lies beyond \(n^2\) and crosses strictly downward, so there is exactly one. Strict ordering in \(n\) gives \(x_{n+1}>x_n\), and \(x_n>n^2\) ensures escape to infinity.

**3. Single sign change and telescoping.** For \(\tau_m<t<\tau_{m+1}\), the ordering above implies \(H_t(n)<0\) precisely for \(|n|\le m\) and \(H_t(n)>0\) otherwise. At an equality time the two symmetric boundary entries are zero. Summation of the discrete Laplacian over the central interval gives
\[
\sum_{n=-m}^mH_t(n)=2\bigl(G_t(m+1)-G_t(m)\bigr).
\]
Since \(\sum_n H_t(n)=0\), the total variation is \(-2\) times this negative mass, namely \(4(G_t(m)-G_t(m+1))\). The same identity holds at a tie. This proves the formula, the staircase, and the input classification.

**4. Threshold asymptotics.** Let \(h=x^{-1/2}\), \(u=nh\), and \(\phi(u)=(2\pi)^{-1/2}e^{-u^2/2}\). Fourier inversion gives
\[
G_{x/2}(n)=\frac1{2\pi}\int_{-\pi}^{\pi}e^{x(\cos\theta-1)}e^{-in\theta}\,d\theta.
\]
Substitute \(\theta=hs\) and expand the exponent, splitting at a slowly growing \(|s|\) and bounding the remainder by Gaussian domination. Uniformly for \(u\) in compact sets, including the required finite numbers of \(u\)-derivatives, this yields
\[
G_{x/2}(n)=h\left[\phi(u)+\frac{h^2}{24}\phi^{(4)}(u)+h^4\left(\frac{\phi^{(6)}(u)}{720}+\frac{\phi^{(8)}(u)}{1152}\right)+O(h^6)\right].
\]
Consequently
\[
H_{x/2}(n)=h^3\phi(u)\left[u^2-1+h^2\left(\frac{\operatorname{He}_4(u)}{12}+\frac{\operatorname{He}_6(u)}{24}\right)+O(h^4)\right],
\]
where \(\operatorname{He}_j\) are the probabilists' Hermite polynomials. At \(u=1\) the coefficient in parentheses is \(1/2\). For each fixed \(\varepsilon\in(0,1)\), the leading term has opposite signs at \(x=(1-\varepsilon)m^2\) and \(x=(1+\varepsilon)m^2\) as \(m\to\infty\). The unique zero is therefore at \(x_m/m^2\to1\). The expansion is now uniform at that zero; using the nonzero derivative \(2\) of \(u^2-1\) at \(u=1\) gives \(x_m=m^2+1/2+O(m^{-2})\). This refines the preceding existence argument with no numerical assumptions.

**5. Uniform sharp oscillatory law.** For \(v=h(m+1/2)\), centered differencing of the same uniform Fourier expansion gives
\[
G_{x/2}(m)-G_{x/2}(m+1)
=h^2\phi(v)\left[v+\frac{h^2}{24}\bigl(\operatorname{He}_3(v)+\operatorname{He}_5(v)\bigr)+O(h^4)\right].
\]
The maximizing staircase index obeys \(m+1/2=\sqrt x+O(1)\) by the threshold expansion, and its squared deviation \((m+1/2-\sqrt x)^2\) differs from \(\rho(x/2)^2\) by at most \(O(x^{-1/2})\): the transition times differ from the nearest-midpoint rounding boundaries \(x=m^2\) by a bounded amount. With \(v=1+h\delta\), the function \(v\phi(v)\) has a strict quadratic maximum at \(v=1\), while \(\operatorname{He}_3(1)+\operatorname{He}_5(1)=4\). It follows uniformly that
\[
G_{x/2}(m)-G_{x/2}(m+1)
=h^2\phi(1)\left[1+h^2\left(\frac16-\rho(x/2)^2\right)+O(h^3)\right].
\]
Multiplying by four and substituting \(x=2t\) proves the claimed time expansion. As \(t\) varies, \(\rho(t)\) visits every point of \([0,1/2]\) on arbitrarily late intervals; its squared continuous image gives the asserted accumulation interval.

## Verification

The independent finite computations available in `check.py` evaluate Bessel values by a convergent positive power series, compare the telescoped expression with a direct \(\ell^1\)-sum of the signed heat derivative, locate several thresholds by scalar bracketing, and check the large-time coefficients and phase-index predictions. Executing `python3 check.py` reported **134 passed finite assertions**. This checker illustrates and independently stress-tests normalizations but is not used to replace the analytical argument for all dimensions, integer orders, or real times.

## Relationship to prior work

The Bessel representation of the integer-lattice heat kernel is classical and is used in Grünbaum–Iliev (2002) and explicitly by Ciaurri et al. (2014); no novelty is asserted for it. Ignat (2006) studies positivity and qualitative bounds for discrete heat schemes. Abadias–de León-Contreras (2022), Lemmas 2.4–2.6 and Remark 2.7, give spatial-difference bounds of the form \(\|\delta^lG_t\|_{\ell^1}\lesssim t^{-l/2}\) and connect even differences to time derivatives. Those generic bounds do not state the exact norm, the sequence of unique Bessel sign changes, or the second-order lattice oscillations. These three combined sharpenings are the subject of this finding. Abadias, González-Camus, Miana and Pozo (2021), Theorem 4.3(iii), prove the corresponding \(\ell^1\)-norm bound \(\|\Delta G_t\|_1\lesssim t^{-1}\), and their Section 7.2 explicitly discusses extending finite-difference order estimates. Their inspected full text does not compute the sharp coefficient, determine the Bessel sign staircase, or give the oscillatory second-order law. No novelty is claimed for their decay rate.

## Limitations

No statement is made for general inhomogeneous graphs, higher-dimensional lattices, nonlinear diffusion, or the full range of \(\ell^p\)-operator norms. The error term in the large-time formula is not claimed to be optimal. Even comparison with relevant accessible primary papers cannot establish global priority; historical equivalent statements under Bessel-ratio, Skellam signed total-variation or semigroup time-derivative terminology remain a bibliographic risk. The result has received a self-review only, not independent review.

## References

1. F. A. Grünbaum and P. Iliev, *Heat kernel expansions on the integers*, arXiv:math/0206089 (first public posting 2002-06-09), https://arxiv.org/abs/math/0206089 .
2. L. I. Ignat, *Qualitative Properties of a Numerical Scheme for the Heat Equation* (2006), DOI:10.1007/978-3-540-34288-5_56 .
3. Ó. Ciaurri, T. A. Gillespie, L. Roncal, J. L. Torrea and J. L. Varona, *Harmonic Analysis associated with a discrete Laplacian*, arXiv:1401.2091 (first posted 2014-01-09), https://arxiv.org/abs/1401.2091 .
4. L. Abadias and J. de León-Contreras, *Discrete Hölder spaces and their characterization via semigroups associated with the discrete Laplacian and kernel estimates*, DOI:10.1007/s00028-022-00851-1 (2022).
5. L. Abadias et al., *Large time behaviour for the heat equation on Z, moments and decay rates*, DOI:10.1016/j.jmaa.2021.125137 (2021; author manuscript at arXiv:2401.16377 posted in 2024 and inspected).
