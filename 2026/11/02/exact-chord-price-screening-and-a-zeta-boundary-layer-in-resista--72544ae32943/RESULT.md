# Exact chord-price screening and a zeta boundary layer in resistance-optimal paths

## Finding

For a path on \(n\ge3\) vertices, with unit-priced path conductances and one optional edge \(\{i,j\}\) of price \(q>0\), the unique minimum-Kirchhoff-index network omits that edge if and only if \(q\ge Q_n(i,j)\), where \(Q_n(i,j)\) is the explicit discrete-variance formula below. Strict containment of chord intervals strictly increases the threshold. In the macroscopic limit the threshold has an explicit two-parameter arcsine variance kernel. For the endpoint chord, its exact next-order term is
\[
Q_n(1,n)=\left(\frac{\pi^2}{4}-2\right)n^2+2\pi\zeta(-\tfrac12)\sqrt n+O(\log n).
\]
The coefficient \(2\pi\zeta(-1/2)\) is negative. These conclusions concern the *sum of pairwise effective resistances*, not the spectral gap or resistance diameter.

## Assumptions and scope

Fix an integer \(n\ge3\), vertex set \(\{1,\ldots,n\}\), and indices \(1\le i<j\le n\), \(j-i\ge2\). Each path edge \(\{\ell,\ell+1\}\) has independently selected conductance \(c_\ell\ge0\) at unit price; one extra chord \(\{i,j\}\) has conductance \(t\ge0\) at price \(q>0\). The graph must be connected and
\[
 \sum_{\ell=1}^{n-1}c_\ell+qt\le B,\qquad B>0.
\]
Let \(R_{uv}\) denote effective resistance, and minimize \(J=\sum_{1\le u<v\le n}R_{uv}\) over feasible connected networks. Define
\[
 A_\ell=\ell(n-\ell),\quad d_\ell=A_\ell^{-1/2},\quad
 H_n=\sum_{\ell=1}^{n-1}\sqrt{A_\ell},\quad
 h_k=\sum_{\ell=1}^{k-1}d_\ell,\quad h_1=0.
\]
For any chord interval \([i,j]\), let
\[
 z_k=\min\{h_j,\max\{h_i,h_k\}\},\quad
 \bar z=\frac1n\sum_{k=1}^n z_k,\quad
 Q_n(i,j)=n\sum_{k=1}^n(z_k-\bar z)^2.
\]
The screening price is independent of the total budget \(B\). At or above the threshold, the optimal path conductances are uniquely \(c_\ell^0=B\sqrt{A_\ell}/H_n\) and \(t^0=0\). Below the threshold, the unique optimizer has \(t>0\) (no closed formula for those conductances is asserted). For proper interval containment \([i,j]\subsetneq[a,b]\), with both chords nonadjacent, \(Q_n(i,j)<Q_n(a,b)\).

If \(i=i_n,j=j_n\), \(i_n/n\to x\), \(j_n/n\to y\), \(0\le x<y\le1\), define \(\alpha=2\arcsin\sqrt{x}\), \(\beta=2\arcsin\sqrt{y}\),
\[
 m=\frac{\alpha+\beta+\sin\beta-\sin\alpha}{2},\qquad
 \Phi(x,y)=\frac{\alpha^2+\beta^2}{2}+\beta\sin\beta-\alpha\sin\alpha+\cos\beta-\cos\alpha-m^2.
\]
Then \(Q_n(i_n,j_n)/n^2\to\Phi(x,y)\). The result at \((x,y)=(0,1)\) holds together with the more precise \(\sqrt n\) correction stated above. Here \(\zeta\) is the Riemann zeta function, defined by its standard analytic continuation.

## Proof

**1. Strict optimization and the reference path.** Ground one vertex and let \(L\succ0\) be the reduced weighted graph Laplacian. Writing \(b_{uv}\) for grounded incidence vectors gives \(J=\operatorname{tr}(WL^{-1})\) where \(W=\sum_{u<v}b_{uv}b_{uv}^{\mathsf T}\succ0\). The Hessian in any nonzero Laplacian direction \(\Delta L\) is
\[
 2\operatorname{tr}(WL^{-1}\Delta L L^{-1}\Delta L L^{-1})>0.
\]
Indeed, conjugating by \(L^{-1/2}\) expresses it as the trace of a positive-definite matrix times the nonzero positive-semidefinite square of a symmetric matrix. Since all allowed edges are distinct and simple, a nonzero change in their conductances yields \(\Delta L\ne0\). Thus \(J\) is strictly convex in edge conductances on its connected domain. Approaching a disconnected network makes at least one effective resistance diverge, so a unique feasible minimum exists. Scaling all conductances scales \(J\) inversely; hence the entire budget is used.

When \(t=0\), series resistance on a path gives
\[
 J=\sum_{\ell=1}^{n-1}\frac{A_\ell}{c_\ell}\ge\frac{H_n^2}{B},
\]
with equality uniquely at \(c_\ell^0=B\sqrt{A_\ell}/H_n\). The budget shadow multiplier is \(\lambda=H_n^2/B^2\).

**2. Exact screening, including equality.** For an edge \(\{i,j\}\) of zero conductance, the derivative \(-\partial J/\partial t\) equals \(\sum_{u<v}(V_u-V_v)^2\), where \(V\) is the potential of a unit current through the endpoints in the reference path. The potential is constant outside \([i,j]\); inside it drops by one edge resistance \(1/c_\ell^0=(H_n/B)d_\ell\). Consequently
\[
 \left.\frac{\partial J}{\partial t}\right|_{(c^0,0)}
 =-\frac{H_n^2}{B^2}\sum_{u<v}(z_u-z_v)^2
 =-\lambda Q_n(i,j).
\]
The marginal cost is \(\lambda q\). The first-order constrained convex optimality condition at \((c^0,0)\) is therefore \(q\ge Q_n(i,j)\). Strict convexity makes it sufficient, even at equality, and ensures uniqueness. If \(q<Q_n(i,j)\), the feasible perturbation \(t=\varepsilon\), \(c_\ell=(1-q\varepsilon/B)c_\ell^0\) has derivative \(\lambda(q-Q_n(i,j))<0\), proving strict inclusion of the chord in the unique optimizer.

**3. Nested chord prices.** If \([i,j]\subsetneq[a,b]\), the sequence \(z_k^{a,b}-z_k^{i,j}\) is nondecreasing and nonconstant, while \(z_k^{i,j}\) is nondecreasing. Chebyshev's pair covariance identity shows their covariance is nonnegative. The difference has positive variance, giving
\(\operatorname{Var}(z^{a,b})>\operatorname{Var}(z^{i,j})\). Multiplying by \(n^2\) proves strict monotonicity of the price thresholds.

**4. Continuum arcsine kernel.** Because \(d_\ell=n^{-1}[(\ell/n)(1-\ell/n)]^{-1/2}\), the integral comparison for the two integrable endpoint singularities proves uniform convergence of the interpolated path profiles to \(F(s)=2\arcsin\sqrt s\). The clamped profiles then converge uniformly to \(\min\{F(y),\max\{F(x),F(s)\}\}\). Hence \(Q_n/n^2\) converges to the variance of that clamped profile at a uniform \(s\in[0,1]\). The variable \(u=F(s)\) has density \(\tfrac12\sin u\) on \([0,\pi]\). Elementary integration of its clipped first and second moments gives, respectively,
\[
 m=\frac{\alpha+\beta+\sin\beta-\sin\alpha}{2},\qquad
 \mathbb E[z^2]=\frac{\alpha^2+\beta^2}{2}+\beta\sin\beta-\alpha\sin\alpha+\cos\beta-\cos\alpha.
\]
Subtracting \(m^2\) gives \(\Phi\), including \(\Phi(0,1)=\pi^2/4-2\).

**5. Endpoint boundary-layer coefficient.** Put
\[
 a(s)=\sqrt{\frac{s}{1-s}},\quad b(s)=\sqrt{\frac{1-s}{s}},\quad
 A(s)=\int_0^s a(v)\,dv=\arcsin\sqrt s-\sqrt{s(1-s)},\quad f(s)=b(s)A(s).
\]
Expanding all pairs in the discrete variance, using \(d_\ell^2=1/[\ell(n-\ell)]\), gives the exact identity
\[
 Q_n(1,n)=n-1+2\sum_{j=1}^{n-1}b(j/n)\sum_{i=1}^{j-1}a(i/n).
\]
To retain the square-root endpoint correction, write \(a(s)=\sqrt s+r(s)\). The classical power-sum expansion, with a uniform remainder, is
\[
 \sum_{i=1}^{j-1}\sqrt i=\frac23j^{3/2}-\frac12\sqrt j+\zeta(-\tfrac12)+O(j^{-1/2}).
\]
The composite-trapezoid error for \(r\), whose second derivative is bounded by a constant times \((1-s)^{-5/2}\) near \(1\) and is integrable at \(0\), implies
\[
 \sum_{i=1}^{j-1}a(i/n)
 =nA(j/n)-\frac12a(j/n)+\frac{\zeta(-\tfrac12)}{\sqrt n}+E_{n,j},
\]
with an error controlled by
\[
 |E_{n,j}|\le C\left(\frac1{\sqrt{nj}}+\frac1{n(1-j/n)^{3/2}}\right),\quad
 \sum_{j=1}^{n-1}b(j/n)|E_{n,j}|=O(\log n).
\]
As \(a(s)b(s)=1\), the diagonal term \(n-1\) cancels the \(-a/2\) contribution, yielding
\[
 Q_n(1,n)=2n\sum_{j=1}^{n-1}f(j/n)
 +\frac{2\zeta(-\tfrac12)}{\sqrt n}\sum_{j=1}^{n-1}b(j/n)+O(\log n).
\]
At \(s\downarrow0\), \(f(s)=\tfrac23s+O(s^2)\); at \(s\uparrow1\), \(f(s)=\tfrac\pi2\sqrt{1-s}-2(1-s)+O((1-s)^{3/2})\). Subtracting \((\pi/2)\sqrt{1-s}\) leaves a function with integrable second derivative. The same square-root power-sum expansion and the trapezoidal rule therefore give
\[
 \sum_{j=1}^{n-1}f(j/n)=n\int_0^1f(s)\,ds
 +\frac\pi2\zeta(-\tfrac12)n^{-1/2}+O(n^{-1}).
\]
Also \(\sum_{j=1}^{n-1}b(j/n)=\frac\pi2 n+O(\sqrt n)\), by subtracting its \(s^{-1/2}\) singularity. Finally \(2\int_0^1f(s)\,ds=\pi^2/4-2\), as follows by \(s=\sin^2\theta\). Combining these identities proves the asserted \(2\pi\zeta(-1/2)\sqrt n\) correction and \(O(\log n)\) remainder.

## Verification

Run `python verify.py` in an environment with Python 3 and NumPy. The script independently evaluates the finite discrete variance, exact path Kirchhoff index, finite-difference chord derivatives, strict nesting, continuum formula, and the endpoint boundary-layer term. Numerical checks are consistency tests; the all-parameter results follow from the analytic proof above.

## Relationship to prior work

Ghosh, Boyd and Saberi (2006) already establish convexity, general edge-price optimality conditions, and resistance minimization over graph weights; Ghosh, Boyd and Saberi (2008) also give the optimal weighting of a tree. These general principles and the tree Cauchy inequality are not claimed as new. The new specific conclusions are the exact pairwise-voltage-variance screening kernel for all optional path chords, strict nesting, the explicit macroscopic arcsine kernel, and the zeta boundary-layer coefficient at the endpoint. Bhoite et al. (2026) study a different fixed-base edge-augmentation and cardinality-constrained effective-resistance formulation; they do not provide the stated path kernel or endpoint expansion in the inspected sections. Other equivalent specialist results may exist and require independent priority verification.

## Limitations

The chord is a single optional edge; joint addition of multiple chords is not classified. The formula gives the exact screening threshold and characterizes exclusion, not closed-form optimal conductances in the included-edge regime. The \(O(\log n)\) remainder does not identify the logarithmic coefficient. No claim about spectral-gap optimality, resistance diameter, or finite-time Markov mixing follows. Independent mathematical validation has not been performed.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, 2006 conference proceedings, https://stanford.edu/~boyd/papers/eff_res.html (public proceedings dated July 24, 2006).
2. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf .
3. Bhoite et al., *Network Design and Effective Resistance: An Edge Augmentation Problem*, arXiv:2609.29790 (2026), https://arxiv.org/abs/2609.29790 .
