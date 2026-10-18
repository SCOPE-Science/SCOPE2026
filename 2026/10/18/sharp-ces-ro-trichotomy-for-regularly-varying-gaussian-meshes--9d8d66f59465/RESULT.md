# Sharp Cesàro trichotomy for regularly varying Gaussian meshes
## Finding
For the firmly nonexpansive Gaussian-mesh orbit of Bauschke and Tung, let the admissible increments \(d_n\) be regularly varying of index \(-\alpha\), where \(1/2<\alpha\le1\), and suppose the extended limit \(a=\lim_{n\to\infty}n d_n\in[0,\infty]\) exists. Put \(\rho_\infty=\exp(-\sum_{k\ge1}d_k^2)\), and let \(Y_n=n^{-1}\sum_{k=1}^n T^{k-1}x_1\).

**Sharp strong-convergence regime.** If \(a=\infty\), then
\[
\lim_{n\to\infty}n d_n\,\|Y_n\|^2=\frac{\sqrt\pi}{1+\alpha}\rho_\infty^2,
\qquad
\|Y_n\|\sim\frac{\pi^{1/4}\rho_\infty}{\sqrt{(1+\alpha)n d_n}}.
\]
This includes every \(1/2<\alpha<1\), for which the extended limit automatically equals infinity.

**Critical and slow regimes.** If \(a<\infty\), necessarily \(\alpha=1\), and
\[
\lim_{n\to\infty}\|Y_n\|^2=\rho_\infty^2F(a),\qquad
F(a)=\int_0^1\exp\big(-a^2(\log r)^2\big)\,dr,\quad F(0)=1.
\]
In particular, the Cesàro means fail to converge strongly exactly when the finite density limit occurs within this class. The function is strictly decreasing on \([0,\infty)\), and \(F(a)\sim\sqrt\pi/(2a)\) as \(a\to\infty\), matching the strong-regime constant at \(\alpha=1\).

For \(d_n=c n^{-\alpha}\), \(1/2<\alpha<1\) and \(0<c\le1/16\), the increments satisfy the required admissibility condition, and the theorem specializes to the explicit sharp law
\[
\|Y_n\|\sim
\frac{\pi^{1/4}\exp\big(-c^2\zeta(2\alpha)\big)}{\sqrt{(1+\alpha)c}}\,n^{-(1-\alpha)/2}.
\]
The squared-norm limits are statements about the particular orbit of the constructed nonlinear operator, not uniform bounds for all firmly nonexpansive mappings.

## Assumptions and scope
Work in an infinite-dimensional real Hilbert space supporting a unit Gaussian feature curve \(u:[0,\infty)\to H\) with \(\langle u(s),u(t)\rangle=e^{-(s-t)^2}\). Assume \(d_n>0\), \(\sum_{n\ge1}d_n^2<\infty\), \(\sum_{n\ge1}d_n=\infty\), \(d_1\le1/8\), and
\[
 d_{n+1}\le \frac{d_n}{1+64d_n^2}\quad(n\ge1).
\]
These are the source's precise hypotheses for realizing \(x_n=\rho_nu(t_n)\), \(t_n=\sum_{k<n}d_k\), \(\rho_n=\exp(-\sum_{k<n}d_k^2)\), as \(x_n=T^{n-1}x_1\) for a firmly nonexpansive map \(T\) with the sole fixed point zero. The source proves \(x_n\rightharpoonup0\), while \(\|x_n\|\to\rho_\infty>0\). The present theorem adds regular variation, meaning
\[
\frac{d_{\lfloor sn\rfloor}}{d_n}\longrightarrow s^{-\alpha}\quad\text{for each }s>0,
\]
and the extended existence of \(a=\lim n d_n\). These conditions are not asserted for arbitrary admissible meshes. If \(\alpha<1\), regular variation forces \(n d_n\to\infty\). A finite \(a\) can only arise for \(\alpha=1\).

## Proof
**Exact Gram formula.** The Gaussian feature identity gives, without approximation,
\[
\|Y_n\|^2=\frac1{n^2}\sum_{i,j=1}^n\rho_i\rho_jK_{ij},\qquad
K_{ij}=\exp\big(-(t_i-t_j)^2\big).
\]
We establish asymptotics of this nonnegative double sum, keeping the amplitudes \(\rho_i\) throughout.

**1. Gaussian row estimate when \(n d_n\to\infty\).** For each \(i\ge1\), let \(R_i=\sum_{j\ge1}K_{ij}\). Regular variation and \(i d_i\to\infty\) imply \(d_i\to0\), \(1/d_i=o(i)\), and the local uniformity
\[
\sup_{|h|\le L/d_i}\left|\frac{t_{i+h}-t_i}{h d_i}-1\right|\longrightarrow0
\]
for each fixed \(L>0\) (with the ratio at \(h=0\) interpreted as one). Indeed \(|h|/i=o(1)\) and the uniform convergence theorem for regularly varying sequences makes the mesh steps uniformly equivalent to \(d_i\) on that window. Consequently the local part of \(d_iR_i\) is a Gaussian Riemann sum tending to \(\int_{-L}^{L}e^{-u^2}\,du\).

To control the omitted tails, monotonicity of the mesh gives \(t_i-t_j\ge(i-j)d_i\) when \(j<i\). When \(i<j\le2i\), the uniform convergence theorem gives \(d_{2i}\ge c_0d_i\) for some fixed \(c_0>0\) and all sufficiently large \(i\), whence \(t_j-t_i\ge c_0(j-i)d_i\). Both tails outside \(|j-i|\le L/d_i\) are therefore bounded after multiplication by \(d_i\) by Gaussian integrals tending to zero as \(L\to\infty\).

For \(j>2i\), regular variation gives \(t_{2i}-t_i\ge c_0i d_i\). Since \(k d_k\to\infty\), eventually \(d_k\ge1/k\), so \(t_j-t_{2i}\ge\log(j/(2i))\) for all large \(i\). The bound \((A+B)^2\ge A^2+B^2\) for nonnegative \(A,B\) yields
\[
\sum_{j>2i}K_{ij}\le e^{-c_0^2(i d_i)^2}
\sum_{j>2i}e^{-(\log(j/(2i)))^2}
\le C i\,e^{-c_0^2(i d_i)^2}.
\]
Its product with \(d_i\) tends to zero. Thus
\[
 d_iR_i\longrightarrow\sqrt\pi,
\qquad R_i\le C/d_i\quad(i\ge1)
\]
(the finitely many early indices are absorbed into the constant). The infinite row sums converge by the same tail estimates.

**2. Finite-sample kernel sum.** Fix \(\varepsilon\in(0,1/2)\). Uniformly for \(\varepsilon n\le i\le(1-\varepsilon)n\), the observation boundaries lie \(\gg1/d_i\) mesh indices away, so the preceding Gaussian estimates imply
\[
\sum_{j=1}^nK_{ij}=\frac{\sqrt\pi+o(1)}{d_i}
\]
uniformly on that bulk interval. All boundary rows satisfy \(\sum_{j\le n}K_{ij}\le C/d_i\). Karamata summation for the regularly varying sequence \(1/d_i\) of index \(\alpha\) gives
\[
\sum_{i=1}^n\frac1{d_i}\sim\frac{n}{(1+\alpha)d_n}.
\]
The initial and terminal \(\varepsilon\)-fractions contribute at most \(O(\varepsilon^{1+\alpha})\) and \(O(1-(1-\varepsilon)^{1+\alpha})\), respectively, relative to the full reciprocal-mesh sum. Letting \(\varepsilon\downarrow0\) proves
\[
\sum_{i,j\le n}K_{ij}\sim\frac{\sqrt\pi\,n}{(1+\alpha)d_n}.
\]
Since \(\rho_i\to\rho_\infty\) and \(0<\rho_i\le1\), the weighted replacement error is bounded by
\[
\left|\sum_{i,j\le n}(\rho_i\rho_j-\rho_\infty^2)K_{ij}\right|
\le2C\sum_{i=1}^n\frac{|\rho_i-\rho_\infty|}{d_i}
=o\!\left(\sum_{i=1}^n\frac1{d_i}\right).
\]
The final little-oh follows from weighted Cesàro convergence of the bounded null sequence \(|\rho_i-\rho_\infty|\). Dividing by \(n^2\) gives the sharp strong-regime limit.

**3. Finite-density limit.** Suppose \(a=\lim n d_n<\infty\). Necessarily \(\alpha=1\). For fixed \(0<s,t\le1\), uniform convergence of \(k d_k\) to \(a\) over proportional index windows yields
\[
t_{\lfloor ns\rfloor}-t_{\lfloor nt\rfloor}\longrightarrow a\log(s/t).
\]
Also \(\rho_{\lfloor ns\rfloor}\to\rho_\infty\). The Gram summand is bounded by one; discarding indices below \(\varepsilon n\) costs at most \(2\varepsilon\) in the normalized sum. On \([\varepsilon,1]^2\) ordinary two-dimensional Riemann summation applies. Let \(n\to\infty\) and then \(\varepsilon\downarrow0\) to get
\[
\lim_{n\to\infty}\|Y_n\|^2
=\rho_\infty^2\int_0^1\!\int_0^1
 e^{-a^2(\log(s/t))^2}\,ds\,dt.
\]
Splitting the square at \(s=t\) and writing \(s=rt\) in one triangle reduces this to \(\rho_\infty^2\int_0^1e^{-a^2(\log r)^2}\,dr\). The substitution \(u=-\log r\) gives \(F(a)=\int_0^\infty e^{-a^2u^2-u}\,du\). This is strictly decreasing, with \(F(0)=1\), and substituting \(v=au\) gives \(aF(a)\to\sqrt\pi/2\) as \(a\to\infty\).

**4. Explicit power-law subfamily.** For \(d_n=c n^{-\alpha}\), \(1/2<\alpha<1\), \(0<c\le1/16\), the square sum converges, the ordinary sum diverges, and \(d_1\le1/8\). The only non-obvious mesh requirement is equivalent to
\[
n^\alpha\big((n+1)^\alpha-n^\alpha\big)\ge64c^2.
\]
The mean-value theorem bounds the left-hand side below by \(\alpha 2^{\alpha-1}\ge1/(2\sqrt2)>1/4\ge64c^2\). Hence the family is admissible. Now \(n d_n=c n^{1-\alpha}\to\infty\) and \(\rho_\infty=e^{-c^2\zeta(2\alpha)}\). Substitution into the sharp strong-regime law proves the displayed power-law constant.

## Verification
The proof uses the exact Gaussian Gram matrix and the mesh admissibility conditions from the cited primary source. Its new analytic components are the row asymptotic with a quantitative far-tail bound, the Karamata sum, the amplitude-error estimate, and the finite-density two-dimensional Riemann limit. All are derived above; no finite computation is offered as proof of the asymptotic. At the pure-harmonic parameter \(d_n=c/n\), the finite-density formula agrees exactly with the separately published harmonic limit, serving as a non-novel consistency check. The \(\alpha=3/4\), \(c=1/16\) case sharpens the qualitative convergence example in the original paper.

## Relationship to prior work
Bauschke and Tung construct the orbit, prove its weak convergence and positive limiting orbit norm, show nonvanishing Cesàro norms for the harmonic mesh, and prove strong convergence under \(n d_n\to\infty\). Their Theorem 7.6 gives an upper bound proportional to \((n d_n)^{-1}\) for the squared Cesàro norm, without a sharp coefficient, and Example 7.7 gives only qualitative convergence at the power-law exponent \(3/4\). Their block-mesh oscillation example lies outside the regular-variation class studied here.

The separately published *Exact Cesàro norm limit for the harmonic firmly nonexpansive counterexample* determines the single harmonic mesh \(d_n=c/n\), and that pre-existing special case is expressly not claimed as novel. The added statements cover general regularly varying admissible meshes, yield the exact fast-mesh constant \(\sqrt\pi/(1+\alpha)\), and classify the vanishing-density boundary \(a=0\). Neither inspected prior statement implies these by specializing the harmonic formula or applying the published order bound alone.

## Limitations
The result concerns the specifically constructed Gaussian feature orbit, not arbitrary firmly nonexpansive maps. Regular variation and existence of the extended limit of \(n d_n\) are essential stated restrictions; admissible wildly oscillatory meshes are excluded. The asymptotic constant depends on the exact Gaussian normalization \(e^{-(s-t)^2}\). Publication priority remains conditional on available searches: an equivalent general localization lemma in earlier kernel-summation literature may exist and was not excluded by a global theorem.

## References
1. H. H. Bauschke and T. T. Tung, *Cesàro means of firmly nonexpansive iterates need not converge strongly*, arXiv:2605.25491v1 (public 2026-05-25); full text version 2 (2026-06-30), especially sections 5–7.
2. *Exact Cesàro norm limit for the harmonic firmly nonexpansive counterexample*, published 2026-10-04, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-ces-ro-norm-limit-for-the-harmonic-firmly-nonexpansive-cou--4fec08167fba .
