# A finite-time transverse fluctuation dichotomy in two coupled logistic maps

## Finding

Consider the smooth planar map
\[
F_\varepsilon(x,y)=\left(4x(1-x)+\varepsilon(y-x),\ 4y(1-y)+\varepsilon(x-y)\right),\qquad -2<\varepsilon<2.
\]
The diagonal \(x=y\) is invariant, carrying the invariant arcsine probability \(d\nu(x)=dx/[\pi\sqrt{x(1-x)}]\) on \((0,1)\). For \(\nu\)-almost every diagonal initial value, define
\[
L_n(x)=\sum_{j=0}^{n-1}\log|4(1-2x_j)-2\varepsilon|,\qquad x_{j+1}=4x_j(1-x_j).
\]
The mean is \(\mathbb E_\nu[L_n]=n\log 2\) for every \(n\ge1\) and every parameter in the indicated range. Nevertheless its finite-time fluctuations have the following exact parameter-dependent law. Put \(\phi=\arccos(\varepsilon/2)\). Then
\[
\boxed{V(\varepsilon)=\lim_{n\to\infty}\frac{\operatorname{Var}_\nu(L_n)}{n}
=2\sum_{\substack{r\ge1\\r\ \mathrm{odd}}}\frac{1}{r^2}
\left(\sum_{j=0}^{\infty}\frac{\cos(2^j r\phi)}{2^j}\right)^2.}
\]
Both sums converge absolutely. In particular
\[
\boxed{V(0)=V(1)=0,\qquad V(-1)=\frac{\pi^2}{3}.}
\]
Indeed \(\sup_{n\ge1}\operatorname{Var}_\nu(L_n)<\infty\) for \(\varepsilon=0\) and \(\varepsilon=1\), while \(\operatorname{Var}_\nu(L_n)/n\to\pi^2/3\) when \(\varepsilon=-1\). Thus identical long-time mean transverse Lyapunov exponents conceal a sharp difference in finite-time uncertainty.

## Assumptions and scope

All initial values are sampled from the invariant diagonal with its stationary arcsine law. The planar map is not assumed to preserve the entire square away from the diagonal. Statements hold for each real \(-2<\varepsilon<2\), with no claim of global attraction or transverse stability. Logarithms at isolated zeros are interpreted almost everywhere; all observables below belong to \(L^2\) under the stated invariant measure. The sums \(L_n\) are logarithms of the magnitude of the transverse derivative product along the invariant diagonal, not nonlinear finite-distance errors.

## Proof

**Step 1: doubling-map representation.** Write \(x=\sin^2(\pi t)\) for uniformly distributed \(t\in[0,1)\). The logistic map becomes \(t\mapsto2t\pmod1\), and \(4(1-2x)-2\varepsilon=4\cos(2\pi t)-2\varepsilon\). With \(u=2\pi t\), set
\[
g_\varepsilon(t)=\log|2\cos u-\varepsilon|,
\qquad L_n=n\log2+\sum_{j=0}^{n-1}g_\varepsilon(2^jt).
\]
For \(\varepsilon=2\cos\phi\), \(0<\phi<\pi\), the elementary factorization
\[
2\cos u-2\cos\phi=e^{-iu}(e^{iu}-e^{i\phi})(e^{iu}-e^{-i\phi})
\]
and the standard circle logarithmic-potential Fourier expansion yield, with convergence in \(L^2([0,1])\),
\[
g_\varepsilon(t)=-2\sum_{k=1}^\infty\frac{\cos(k\phi)}{k}\cos(2\pi k t).
\]
In particular \(\int g_\varepsilon(t)dt=0\), proving the asserted exact mean. The \(L^2\) expansion follows by first taking radii \(\rho<1\), where the logarithmic series converges uniformly, and then passing to \(\rho\uparrow1\) in \(L^2\) using square-summability of its Fourier coefficients.

**Step 2: summable time correlations.** Put \(a_k=-2\cos(k\phi)/k\). The doubling map maps cosine frequency \(k\) to \(2^m k\). Orthogonality therefore gives, for \(m\ge0\),
\[
C_m=\int_0^1 g_\varepsilon(t)g_\varepsilon(2^m t)dt
=\frac12\sum_{k=1}^\infty a_k a_{2^m k}.
\]
Since \(|a_k|\le2/k\),
\[
|C_m|\le\frac{2}{2^m}\sum_{k\ge1}\frac1{k^2},
\]
so the Green--Kubo series converges absolutely. Stationarity gives
\[
\operatorname{Var}(L_n)=n C_0+2\sum_{m=1}^{n-1}(n-m)C_m,
\]
and dominated convergence yields \(V=C_0+2\sum_{m\ge1}C_m\).

**Step 3: dyadic-frequency classification.** Every positive integer has a unique expression \(2^j r\) with \(r\) odd. Grouping all ordered coefficient pairs with the same odd part in the preceding absolutely convergent covariance series yields
\[
V=\frac12\sum_{r\ \mathrm{odd}}\left(\sum_{j=0}^\infty a_{2^j r}\right)^2
=2\sum_{r\ \mathrm{odd}}\frac1{r^2}
\left(\sum_{j=0}^\infty2^{-j}\cos(2^j r\phi)\right)^2.
\]
Each inner sum has absolute value at most \(2\); the outer sum converges by \(\sum r^{-2}<\infty\).

**Step 4: exact exceptional values and strong bounded-variance statements.** For \(\varepsilon=0\), \(\phi=\pi/2\). If \(r\) is odd, \(\cos(r\phi)=0\), \(\cos(2r\phi)=-1\), and \(\cos(2^j r\phi)=1\) for \(j\ge2\). The weighted inner sum is \(-1/2+\sum_{j\ge2}2^{-j}=0\). More strongly, the double-angle identity gives the explicit \(L^2\) coboundary
\[
g_0(t)=H_0(2t)-H_0(t),\qquad H_0(t)=\log|\sin(2\pi t)|.
\]
For \(\varepsilon=1\), \(\phi=\pi/3\). For odd \(r\) divisible by three, its weighted cosines are \(-1\) at \(j=0\) and \(+1\) at all \(j\ge1\); otherwise they are \(+1/2\) at \(j=0\) and \(-1/2\) at all \(j\ge1\). Again the dyadic sums cancel. The stronger identity is
\[
g_1(t)=H_1(2t)-H_1(t),\qquad H_1(t)=\log|1+2\cos(2\pi t)|,
\]
which follows exactly from \(1+2\cos(2u)=(2\cos u-1)(1+2\cos u)\). Both transfer functions are \(L^2\), so telescoping and stationarity give \(\operatorname{Var}(L_n)\le4\lVert H_i\rVert_2^2\), uniformly in \(n\).

Finally, at \(\varepsilon=-1\), \(\phi=2\pi/3\). For odd \(r\) divisible by three every dyadic cosine is \(1\) and its weighted sum equals \(2\). For all other odd \(r\), every dyadic cosine equals \(-1/2\) and the weighted sum equals \(-1\). Hence
\[
V(-1)=2\left(4\sum_{\substack{r\ \mathrm{odd}\\3\mid r}}r^{-2}
+\sum_{\substack{r\ \mathrm{odd}\\3\nmid r}}r^{-2}\right)
=2\left(4\frac{\pi^2}{72}+\frac{\pi^2}{8}-\frac{\pi^2}{72}\right)
=\frac{\pi^2}{3}.
\]
All claimed assertions follow.

## Verification

The standalone `verify.py` checks rational cosine-residue tables for the three exceptional parameters, the two exact double-angle polynomial identities, the zeta-sum coefficient \(1/3\), and numerical convergence of the dyadic-frequency formula. These computations are reproducibility checks only; the infinite-time proof is the Fourier, correlation, and telescoping argument above. Run `python3 verify.py` using the Python standard library. Expected output: `VERIFY_OK`.

## Relationship to prior work

Maistrenko, Maistrenko, Popovich and Mosekilde (1998), *Transverse instability and riddled basins in a system of two coupled logistic maps*, studies precisely the above diffusive coupling and identifies its transverse derivative and mean transverse Lyapunov exponent, including an exponent plateau. The complete accessible original article was inspected: its focus is stability, bifurcation and riddled basins, not an exact finite-time log-multiplier variance or the parameter-specific \(L^2\) coboundaries. Prasad and Ramaswamy (1999), *Characteristic distributions of finite-time Lyapunov exponents*, treats the uncoupled logistic map's longitudinal finite-time exponent distribution; it can imply the zero-variance baseline \(\varepsilon=0\), but not the paired exact \(\varepsilon=1\) cancellation or \(\varepsilon=-1\) positive variance of the coupled transverse cocycle. These deductions are statement-level comparisons, not a claim of exhaustively proving novelty across all literature.

## Limitations

The result concerns variance under a specific invariant probability supported on the synchronization manifold. It does not establish any central limit theorem, characterize all coupling values where \(V(\varepsilon)=0\), or establish synchronization of off-diagonal trajectories. The transfer functions for the two cancellation parameters are \(L^2\) but unbounded; bounded *variance* does not mean uniform pointwise bounds. Other representations of these cocycles in older spectral or cohomological literature could cover pieces of the calculation; no independent audit has been performed.

## References

1. Yu. L. Maistrenko, V. L. Maistrenko, A. Popovich, and E. Mosekilde, "Transverse instability and riddled basins in a system of two coupled logistic maps," *Physical Review E* **57** (1998), 2713--2724. DOI: `10.1103/PhysRevE.57.2713`. Original full-text copy: `https://backend.orbit.dtu.dk/ws/files/4082564/Mos.pdf`.
2. A. Prasad and R. Ramaswamy, "Characteristic distributions of finite-time Lyapunov exponents," preprint `arxiv:chao-dyn/9906022` (1999). Full text: `https://arxiv.org/pdf/chao-dyn/9906022`.
