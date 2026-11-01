# Least-common-multiple resonance and sharp rotation of regular-polygon Minkowski sums

## Finding

Let \(P\) and \(Q\) be nondegenerate regular Euclidean polygons with respectively \(n,m\ge3\) sides. Their circumradii may be arbitrary positive numbers. Put
\[
N=\begin{cases}n,&n\text{ even},\\2n,&n\text{ odd},\end{cases}\qquad
M=\begin{cases}m,&m\text{ even},\\2m,&m\text{ odd},\end{cases}
\qquad L=\operatorname{lcm}(N,M),\quad r=L/N,\quad s=L/M.
\]
For a polygon \(T\), write \(w_T(\theta)\) for its Euclidean width in direction \((\cos\theta,\sin\theta)\), and \(\mu_T=(2\pi)^{-1}\int_0^{2\pi}w_T(\theta)\,d\theta\). Choose \(\tau_P\) and \(\tau_Q\) to be respective directions of maximal width, defined modulo \(2\pi/N\) and \(2\pi/M\). Rotating \(Q\) through angle \(\varphi\) creates relative phase \(\psi=\tau_Q+\varphi-\tau_P\). Let \(\Theta\) be uniform on \([0,2\pi)\).

The normalized mixed-width covariance has the exact **least-common-multiple resonance law**
\[
\operatorname{Cov}\left(\frac{w_P(\Theta)}{\mu_P},\frac{w_{R_\varphi Q}(\Theta)}{\mu_Q}\right)
=K_L\left(\psi+\varepsilon\frac\pi L\right),\qquad
K_L(t)=2\sum_{j=1}^{\infty}\frac{\cos(jLt)}{(j^2L^2-1)^2},
\]
where \(\varepsilon\in\{0,1\}\) is the parity of \(r+s\). In particular, after normalization the entire dependence on the side counts is through their least common multiple and one parity bit.

For every pair of positive weights \(a,b\), the directional-width variance (and coefficient of variation) of the Minkowski sum \(aP+bR_\varphi Q\) is **globally minimized**, with all equality cases, precisely when
\[
\boxed{\quad
\psi\equiv\begin{cases}
\pi/L\pmod{2\pi/L},&r+s\text{ even},\\
0\pmod{2\pi/L},&r+s\text{ odd}.
\end{cases}\quad}
\]
The globally maximizing orientations exchange these two cases. There are no other maximizing or minimizing relative-phase classes.

Writing \(h=\pi/L\), the exact sharp minimum and maximum values of the normalized mixed covariance are
\[
K_L(h)=\frac{h^2\cos h}{2\sin^2h}+\frac{h}{2\sin h}-1<0,
\qquad
K_L(0)=\frac{h^2}{2\sin^2h}+\frac{h\cos h}{2\sin h}-1>0.
\]
They satisfy the sharp large-resonance laws
\[
K_L(0)=\frac{\pi^4}{45L^4}+O(L^{-6}),\qquad
K_L(h)=-\frac{7\pi^4}{360L^4}+O(L^{-6}).
\]
For instance, a square and a regular octagon have \(N=4,M=8,L=8,r+s=3\): the widths of the two polygons are *negatively* correlated when their maximal-width directions align, and that alignment uniquely minimizes the width variance of every positively weighted Minkowski sum of the two, modulo \(\pi/4\).

## Assumptions and scope

All polygons are planar, Euclidean, nondegenerate, and regular, with at least three sides. The angle \(\Theta\) is Haar-uniform and shared by the two width measurements. The second polygon is rotated deterministically; weights \(a,b\) are strictly positive and independently fixed. Width-maximizing directions of an odd-sided regular polygon are generally not its vertex directions: the phase uses vertices of the difference body. A phase is well-defined modulo the indicated period, which also makes every congruence above independent of its representative.

## Proof

**1. Difference-body reduction.** Width is the support function of the difference body: \(w_P(u)=h_{P-P}(u)\). For even \(n\), \(P-P=2P\) up to translation and has \(N=n\) vertices. For odd \(n\), extremal antipodal differences use vertex index separations \((n\pm1)/2\); their convex hull is a regular \(2n\)-gon of circumradius \(2R_P\cos(\pi/(2n))\). Thus in both cases, for an amplitude \(A_P>0\),
\[
w_P(\theta)=A_P\cos d_N(\theta-\tau_P),
\quad d_N(x)=\min_{k\in\mathbb Z}|x-2\pi k/N|\in[0,\pi/N].
\]
The corresponding formula holds for \(Q\). Since \(N,M\ge4\) are even, set \(h_N=\pi/N\). The width mean is \(\mu_P=A_P\sin h_N/h_N\). Hence every mean-normalized width is a periodic copy of
\[
f_N(x)=\frac{h_N}{\sin h_N}\cos d_N(x),\qquad \mathbb Ef_N(\Theta)=1.
\]

**2. Fourier calculation.** Direct integration over one cell \([-h_N,h_N]\) gives the absolutely convergent Fourier series
\[
f_N(x)=1+2\sum_{k=1}^{\infty}
\frac{(-1)^{k+1}\cos(kNx)}{k^2N^2-1}.
\]
Indeed the cosine coefficient follows from the identity
\[
\frac{1}{\sin h_N}\int_{-h_N}^{h_N}\cos x\cos(kNx)\,dx
=\frac{2(-1)^{k+1}}{k^2N^2-1}.
\]
In the product of the expansions for \(f_N(\Theta-\tau_P)\) and \(f_M(\Theta-\tau_Q-\varphi)\), orthogonality retains exactly frequencies \(kN=\ell M=jL\). These have indices \(k=jr\), \(\ell=js\) and sign \((-1)^{j(r+s)}\). Averaging proves
\[
\operatorname{Cov}(f_N(\Theta),f_M(\Theta-\psi))
=2\sum_{j\ge1}\frac{(-1)^{j(r+s)}\cos(jL\psi)}{(j^2L^2-1)^2},
\]
which is the displayed shifted \(K_L\) formula. Absolute Fourier convergence legitimizes multiplication and termwise averaging.

**3. Strict orientation rigidity.** \(K_L(t)\) is the autocovariance of \(f_L\), a periodic even function. It is even, periodic with period \(2h=2\pi/L\), and symmetric about \(h\). To prove it is *strictly decreasing* for \(0<t<h\), put \(g(x)=\cos d_L(x)\) and \(c=\sin h/h\). For \(0\le t\le h\), elementary cell-splitting yields the unnormalized autocorrelation
\[
R(t)=\frac1{2h}\int_{-h}^{h}g(x)g(x+t)\,dx
=\frac{(2h-t)\cos t+t\cos(t-2h)+\sin(2h-t)+\sin t}{4h},
\]
where the shifted argument is interpreted periodically. Consequently
\[
R'(t)=\frac{t\sin(2h-t)-(2h-t)\sin t}{4h}<0\quad(0<t<h),
\]
because \(0<t<2h-t<2h\le\pi/2\) and \(\sin z/z\) strictly decreases on \((0,\pi)\). Since \(K_L(t)=R(t)/c^2-1\), the same strict decrease holds for \(K_L\). Evenness and periodicity force exactly one maximum at \(t\equiv0\) and exactly one minimum at \(t\equiv h\) modulo \(2h\). Translating by \(\varepsilon h\) gives the asserted parity alternatives. The mean of the covariance over one period is zero, so the strict extrema also satisfy \(K_L(h)<0<K_L(0)\).

**4. Exact endpoints and asymptotics.** Substituting \(t=0,h\) in \(R(t)/c^2-1\) gives the displayed elementary formulas. Taylor expansion at \(h=0\) yields \(K_L(0)=h^4/45+O(h^6)\) and \(K_L(h)=-7h^4/360+O(h^6)\), and hence the stated powers of \(L\).

**5. Minkowski optimization.** Width is additive under Minkowski sum, so \(w_{aP+bR_\varphi Q}(\Theta)=a w_P(\Theta)+b w_{R_\varphi Q}(\Theta)\). Its mean is \(a\mu_P+b\mu_Q\), which does not depend on \(\varphi\). Its variance is the sum of two orientation-independent variances plus \(2ab\mu_P\mu_Q\) times the displayed cross-covariance. Strict positivity of these prefactors transfers the exact minima, maxima, and uniqueness classes to the width variance and coefficient of variation.

## Verification

Run the accompanying standard-library program with `python CHECK.py`. It independently computes widths as differences of extreme vertex projections for triangles, squares, hexagons, octagons, and further polygon pairs. Deterministic uniform-angle quadrature is compared against the absolute Fourier-series formula, including both parity cases and all critical phases. It also checks both elementary endpoint expressions and their large-order constants. It reports `ALL_CHECKS_PASSED`. These finite numerical checks corroborate the derived identities; the universal proof is the analytic argument above.

## Relationship to prior work

Akiyama and Kamae (2022) study the variance-to-mean width deviation of individual convex polygons, including sharp one-polygon extremizers. Their Theorem 1 gives a general pairwise edge-shadow second-moment kernel, and their Theorem 4 compares single regular-polygon deviation values. That general kernel can in principle compute any two-polygon mixed width moment by finite summation; this elementary covariance computability is **not** claimed as new. The distinct result established here is the all-pairs least-common-multiple collapse, the parity-dependent *global and unique relative-rotation optimizer* for Minkowski sums, and the exact extremal resonance asymptotics. Published treatments of planar Minkowski-sum construction provide the additive geometric setting but not this mixed-directional-variance phase diagram.

## Limitations

The claimed phase law is restricted to two regular polygons with positive weights and Haar-uniform, shared viewing direction. It is not a phase rule for arbitrary polygons, separate independent viewing directions, other width-loss functionals, or Minkowski sums of three or more independently rotated factors. The exact covariance formula is derivable from classical Fourier/projection principles; priority of its particular arithmetic optimizer has not been independently certified. The analytic proof does not rely on finite sampling. Independent review has not been performed.

## References

1. S. Akiyama and T. Kamae, *Width deviation of convex polygons*, arXiv:2201.06736v1, first posted 2022-01-18, especially §§2–4, Theorems 1 and 4. https://arxiv.org/abs/2201.06736
2. S. Arya, G. D. da Fonseca and D. M. Mount, *Approximate Convex Intersection Detection with Applications to Width and Minkowski Sums*, ESA 2018, DOI:10.4230/LIPIcs.ESA.2018.3. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2018.3
