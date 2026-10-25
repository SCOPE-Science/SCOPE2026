# Sharp shortest-path screening and cancellation of distant code defects in a bistable Nagumo lattice

## Finding

Fix \(a\in(0,1)\), and put \(m=\min\{a,1-a\}\), \(r=m/16\), and \(\rho=m^2/256\). For each two-sided binary code \(s\in\{0,1\}^{\mathbb Z}\), the stationary cubic Nagumo lattice has a unique solution \(U(d;s)\) satisfying \(\|U(d;s)-s\|_\infty\le r\) for every complex \(|d|<\rho\). This solution is a holomorphic \(\ell^\infty(\mathbb Z)\)-valued function of \(d\).

If two codes \(s,t\) agree at all sites \(j\) with \(|j-i|<R\), where \(i\in\mathbb Z\) and \(R\ge1\), then their site-\(i\) Taylor coefficients agree in orders \(0,\ldots,R-1\). Their first potentially different coefficient is exactly

\[
[d^R]\big(U_i(d;s)-U_i(d;t)\big)=
\frac{s_{i-R}-t_{i-R}}{\prod_{j=i-R+1}^{i}\alpha_j}+
\frac{s_{i+R}-t_{i+R}}{\prod_{j=i}^{i+R-1}\alpha_j},
\qquad \alpha_j=\begin{cases}a,&s_j=0,\\1-a,&s_j=1.\end{cases}
\]

The products only involve sites where the two codes agree. Consequently, a single flipped symbol at distance \(R\) induces an **exact order-\(R\)** response with a nonzero, explicitly weighted coefficient, while two opposite flips can cancel to that order. If both boundaries are flipped in opposite directions, cancellation holds precisely when the two products are equal. For \(a\ne 1/2\) this is equivalent to the two length-\(R\) paths having equal numbers of zero symbols; at \(a=1/2\), all opposite boundary flips cancel to this order, regardless of the interior.

Moreover, if \(0<|d|<\rho\), the sensitivity is uniformly bounded over all binary configurations by

\[
|U_i(d;s)-U_i(d;t)|\le \frac{2r(|d|/\rho)^R}{1-|d|/\rho}.
\]

Thus coding influence has a finite Taylor propagation speed and a sharp weighted shortest-path leading term, even for arbitrary aperiodic backgrounds.

## Assumptions and scope

The lattice is indexed by all \(i\in\mathbb Z\); its reaction is the cubic \(g_a(u)=u(1-u)(u-a)\); the stationary equation is

\[
 d(U_{i-1}-2U_i+U_{i+1})+g_a(U_i)=0.
\]

The code \(s\) takes values only in the two stable zeros \(0,1\), not the unstable zero \(a\). The parameter \(a\) is fixed in \((0,1)\), with no claimed uniformity as it approaches the endpoints. Holomorphy concerns complex diffusion \(d\) close to zero; physically, sufficiently small positive real diffusion gives the corresponding pinned stationary states. Uniqueness is asserted in the specified \(\ell^\infty\) ball about each code, not among all stationary states.

## Proof

**1. Uniform holomorphic continuation.** Set \(U=s+v\). For \(s_i\in\{0,1\}\), let \(\alpha_i=-g_a'(s_i)\in\{a,1-a\}\) and \(\beta_i=1+a-3s_i\), so \(|\beta_i|\le2\) and

\[
 g_a(s_i+v_i)=-\alpha_i v_i+\beta_i v_i^2-v_i^3.
\]

The stationary equation is equivalent to the fixed point equation on complex \(\ell^\infty(\mathbb Z)\):

\[
 v_i=F_{d,s}(v)_i:=\alpha_i^{-1}\big[d(s_{i-1}-2s_i+s_{i+1}+v_{i-1}-2v_i+v_{i+1})+\beta_i v_i^2-v_i^3\big].
\]

In the closed ball \(\|v\|_\infty\le r\), \(\|\Delta s\|_\infty\le2\) and \(\|\Delta v\|_\infty\le4r\), so for \(|d|\le\rho\),

\[
 \|F_{d,s}(v)\|_\infty\le \frac{\rho(2+4r)+(2+r)r^2}{m}<r,
\]

and

\[
 \operatorname{Lip}(F_{d,s})\le\frac{4\rho+4r+3r^2}{m}<\frac12.
\]

Both strict inequalities follow directly from \(0<m\le1/2\), \(r=m/16\), \(\rho=m^2/256\). Banach contraction gives a unique fixed point in that ball for every allowed \(d,s\). Iteration starting from zero is holomorphic in \(d\) and converges locally uniformly, giving a holomorphic \(\ell^\infty\)-valued solution. Cauchy's estimate on disks approaching radius \(\rho\) gives \(|[d^n]v_i|\le r\rho^{-n}\) for every \(n\ge1\), uniformly in \(s,i\).

**2. Finite dependence of Taylor coefficients.** Write \(v_i(d;s)=\sum_{n\ge1}c_{i,n}(s)d^n\). Comparing powers in the fixed-point identity gives

\[
 \alpha_i c_{i,n}=\mathbf 1_{n=1}(s_{i-1}-2s_i+s_{i+1})+
 c_{i-1,n-1}-2c_{i,n-1}+c_{i+1,n-1}
 +\beta_i\sum_{k=1}^{n-1}c_{i,k}c_{i,n-k}
 -\sum_{\substack{k,\ell,h\ge1\\k+\ell+h=n}}c_{i,k}c_{i,\ell}c_{i,h},
\]

where the middle linear term is omitted for \(n=1\), equivalently \(c_{j,0}=0\). By induction, \(c_{i,n}\) depends only on \(s_j\) with \(|j-i|\le n\). Thus two codes agreeing on \(|j-i|<R\) have identical coefficients below order \(R\).

**3. The exact shortest-path coefficient.** At order \(R\), only differences in the two endpoint codes \(s_{i\pm R}\) can matter. The nonlinear terms at site \(i\) involve lower-order coefficients, whose dependence cannot reach these endpoints. Likewise, the onsite contribution \(-2c_{i,R-1}\) is unaffected. Repeatedly selecting the sole neighbor toward a changed endpoint gives a unique shortest chain of \(R\) nearest-neighbor steps and successively divides by \(\alpha\) at the \(R\) interior sites. Hence the coefficient of the right endpoint change is \(1/\prod_{j=i}^{i+R-1}\alpha_j\), and similarly on the left. Addition of both shortest chains establishes the displayed exact identity. The result holds for arbitrary remaining distant code differences since they cannot contribute before higher order.

With a single boundary flip the numerator is \(\pm1\) and all denominators are positive, so the order-\(R\) coefficient is nonzero. With two opposite flips, cancellation reduces to equality of the two denominators. For \(a\ne1/2\), each denominator is \(a^k(1-a)^{R-k}\); since \(a/(1-a)\ne1\), they agree if and only if the two counts \(k\) agree. For \(a=1/2\), all denominators are equal to \(2^{-R}\), making the opposite-flip cancellation automatic.

**4. Uniform screening.** Since the first \(R\) Taylor coefficients (orders \(0\) through \(R-1\)) coincide, and each positive-order coefficient of either solution is bounded by \(r\rho^{-n}\), the remaining geometric series gives

\[
 |U_i(d;s)-U_i(d;t)|\le\sum_{n\ge R}2r(|d|/\rho)^n=\frac{2r(|d|/\rho)^R}{1-|d|/\rho}.
\]

This also proves the sharp asymptotic \(U_i(d;s)-U_i(d;t)=C_{i,R}d^R+O_{a,R}(d^{R+1})\) whenever the computed coefficient \(C_{i,R}\) is nonzero.

## Verification

A standalone Python exact-rational coefficient checker is included as `check.py`, with its output in `check_output.txt`. It verifies orders through six for single flips across homogeneous sites, tests heterogeneous interior codes through order five, and checks two-sided opposite-flip cancellation. These finite tests corroborate the displayed coefficient formula; the infinite-lattice assertions follow from the analytic contraction proof, not the computations. The ball and contraction inequalities can also be checked directly for every \(0<m\le1/2\).

## Relationship to prior work

Hesoun, Stehlík, and Volek (2026), arXiv:2609.25868v1, identify the small-diffusion stationary solution space of bistable lattices with symbolic sequences, establish unique symbolic representation and stability classification, and analyze monotone fronts. Their explicitly inspected text treats topological coding and geometric localization; it does not state the weighted shortest-path coefficient or the cancellation criterion. Earlier Chow–Shen (1995) and Keener (1987) establish spatial topological chaos and weak-coupling pinned solutions; their accessible summaries do not establish the present quantitative code-defect response. General local implicit-function arguments already imply nearby branches, so analytic continuation alone is not asserted as the novel step.

The contribution is the **uniform exact first nonzero coupling-order law for arbitrary binary code backgrounds**, its explicit local-slope weights and sharp two-sided cancellation rule, and a uniform analytic screening estimate. Priority over uninspected full texts is not claimed as independently established.

## Limitations

The result concerns cubic local reactions, one-dimensional nearest-neighbor coupling, fixed \(a\in(0,1)\), and binary codes; it makes no claim about codes involving the unstable zero \(a\), nonlinearities without analyticity, arbitrary long-range coupling, or diffusion approaching the pinning threshold. For two opposite flips with matching path weights, the order-\(R\) coefficient cancels; no assertion is made about the first later nonzero order. The explicit analyticity radius is sufficient, not optimal. Partial accessibility of the older Keener and Chow–Shen full texts leaves a residual literature-priority risk.

## References

1. J. Hesoun, P. Stehlík, and J. Volek, *Characterization of spatial topological chaos for bistable lattice equation*, arXiv:2609.25868v1 (22 September 2026), https://arxiv.org/html/2609.25868v1.
2. S.-N. Chow and W. Shen, *Dynamics in a Discrete Nagumo Equation: Spatial Topological Chaos*, SIAM Journal on Applied Mathematics 55 (1995), 1764–1781, DOI: 10.1137/S0036139994261757.
3. J. P. Keener, *Propagation and Its Failure in Coupled Systems of Discrete Excitable Cells*, SIAM Journal on Applied Mathematics 47 (1987), 556–572, DOI: 10.1137/0147038.
