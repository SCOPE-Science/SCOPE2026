# Gaussian magnitude monotonicity and a singular centroid crossover for regular-simplex configurations

## Finding
Let \(m\ge3\), \(a,b>0\), and let \(X=\{o,v_1,\ldots,v_m\}\) carry the symmetric semimetric \(d(o,v_i)=a\) and \(d(v_i,v_j)=b\) for distinct leaves. Its distance matrix is of negative type exactly when \(0<b/a\le r_c:=2m/(m-1)\). Equivalently, \(X\) is realizable by squared Euclidean distances among the vertices of a regular simplex and one point on its perpendicular centroid axis.

On the **nonmetric negative-type subfamily** \(2<b/a\le r_c\), the Gaussian-kernel magnitude
\[
\mathcal M(t):=\boldsymbol1^{\mathsf T}(e^{-t d(x,y)})_{x,y\in X}^{-1}\boldsymbol1,\qquad t>0,
\]
exists and is **strictly increasing** on \((0,\infty)\). The proof also works for the metric subrange \(0<b/a\le2\), but monotonicity there already follows from the published one-negative-weight criterion and is not claimed as new. Writing \(r=b/a\), \(p=e^{-at}\), it is
\[
\mathcal M(t)=1+\frac{m(1-p)^2}{1+(m-1)p^r-mp^2}.
\]
The displayed rational-exponential expression is elementary from the symmetry reduction and is **not** by itself claimed as a new generic join formula; the all-scale strict sign and sharp degeneration profile are the asserted contribution.

At the critical geometric configuration \(r=r_c\), the additional point equals the simplex centroid, and
\[
\lim_{t\downarrow0}\mathcal M(t)=\frac{m+1}{2},\qquad
\mathcal M(t)=\frac{m+1}{2}+\frac{m+1}{6}at+O((at)^2).
\]
For every \(r<r_c\), the small-scale limit instead equals \(1\). More precisely, with \(\delta=r_c-r>0\) and \(at=\delta\tau\), as \(\delta\downarrow0\),
\[
\mathcal M(\delta\tau/a)\longrightarrow
1+\frac{m\tau}{m-1+r_c\tau},\qquad\tau>0,
\]
locally uniformly on compact subsets of \((0,\infty)\). Thus a sharp boundary layer interpolates between the one-point limit and the critical non-unit limit. At large scale, \(\lim_{t\to\infty}\mathcal M(t)=m+1\).

## Assumptions and scope
The number \(m\) of equidistant leaves is any integer at least three. The pairwise distances are strictly positive; the triangle inequality need not hold. The similarity kernel is \(K_t(x,y)=e^{-t d(x,y)}\), which is Gaussian when the negative-type semimetric is represented as squared Euclidean distances. The positive time variable \(t\) denotes inverse squared geometric length scale; the singular limit at \(t=0\) refers to \(t\downarrow0\) because \(K_0\) is singular. Strict increase is asserted for every \(t>0\), not merely sufficiently small \(t\).

## Proof
**1. Geometric and negative-type domain.** For a real coefficient vector of total sum zero, write its leaf coefficients as \(v=(s/m)\boldsymbol1+w\), where \(\sum_i w_i=0\); the hub coefficient is \(-s\). The semimetric quadratic form reduces exactly to
\[
\sum_{x,y\in X}c_xc_y d(x,y)
=-b\lVert w\rVert^2+
\left(\frac{m-1}{m}b-2a\right)s^2.
\]
It is nonpositive for all such vectors if and only if \(r\le r_c\). In the Euclidean realization, take centered regular-simplex vertices \(\xi_i=\sqrt{b/2}(e_i-\boldsymbol1/m)\) and hub \(\xi_o=h e_{m+1}\) in one additional orthogonal coordinate, where \(h^2=a-b(m-1)/(2m)\). Then \(\lVert\xi_i-\xi_j\rVert^2=b\) and \(\lVert\xi_o-\xi_i\rVert^2=a\); the hub reaches the centroid exactly when \(r=r_c\). The semimetric is a genuine metric exactly when \(r\le2\).

**2. Magnitude and invertibility.** Set \(p=e^{-at}\) and \(q=p^r\). The similarity matrix acts by \(1-q>0\) on the leaf-difference subspace, and on the hub and normalized leaf-sum by
\[
\begin{pmatrix}1&\sqrt m p\\\sqrt m p&1+(m-1)q\end{pmatrix}.
\]
Its determinant is \(D=1+(m-1)p^r-mp^2\). Since \(p^r\ge p^{r_c}\) and weighted AM--GM gives \(1+(m-1)p^{r_c}>mp^2\) for \(0<p<1\), we have \(D>0\). The leaf weight is \((1-p)/D\); the hub weight is \(1-mp(1-p)/D\). Their sum proves the magnitude formula.

**3. All-scale strict monotonicity.** Differentiation gives
\[
\mathcal M'(t)=\frac{ma p(1-p)}{D^2}
\left[2(1-mp)+(m-1)p^{r-1}(r+(2-r)p)\right].
\]
Fix \(0<p<1\) and define \(\Phi_r(p)=p^{r-1}[r(1-p)+2p]\). Its derivative with respect to \(r\) has the sign of
\[
(1-p)+[r(1-p)+2p]\log p,
\]
an affine, strictly decreasing function of \(r\). Consequently \(\Phi_r(p)\) is either monotone or increases and then decreases, and its minimum over \([0,r_c]\) occurs at an endpoint. At \(r=0\), the derivative bracket is \(2m(1-p)>0\). At \(r=r_c\), let \(k=m-1\ge2\), \(\alpha=1+2/k\in(1,2]\). The bracket becomes \(2H_k(p)\), with
\[
H_k(p)=1-(k+1)p+(k+1-p)p^\alpha.
\]
Direct differentiation gives \(H_k(1)=H_k'(1)=H_k''(1)=0\) and
\[
H_k'''(p)=\alpha(\alpha-1)p^{\alpha-3}
[(k+1)(\alpha-2)-(\alpha+1)p]<0\quad(0<p<1).
\]
Integrating three times from \(1\) backward proves \(H_k''(p)>0\), then \(H_k'(p)<0\), then \(H_k(p)>0\). Both endpoint brackets are strictly positive, so the intermediate one is too, proving \(\mathcal M'(t)>0\) for all admissible parameters and all \(t>0\).

**4. Small-scale limits and boundary layer.** Set \(s=at\), \(r=r_c-\delta\). For fixed \(\delta>0\), expansion gives \(D=(m-1)\delta s+O(s^2)\) and \(m(1-e^{-s})^2=ms^2+O(s^3)\); thus \(\mathcal M(t)=1+ms/((m-1)\delta)+O(s^2)\). At \(\delta=0\), cancellation of the linear denominator term yields \(D=r_cs^2-[4m(2m-1)/(3(m-1)^2)]s^3+O(s^4)\), giving \(\mathcal M(t)=(m+1)/2+(m+1)s/6+O(s^2)\). Finally, if \(s=\delta\tau\) with fixed \(\tau>0\), then
\[
D=\delta^2[(m-1)\tau+r_c\tau^2]+O_\tau(\delta^3),\quad
m(1-e^{-s})^2=m\delta^2\tau^2+O_\tau(\delta^3),
\]
which proves the claimed crossover, uniformly on compact positive \(\tau\)-intervals. The large-scale limit follows immediately from \(p\downarrow0\).

## Verification
The standalone `verify.py` uses exact fractions and Gaussian elimination to check the similarity-matrix inverse against the closed formula, including several critical rational exponents. It also performs high-precision independent numerical diagnostics for the strict derivative sign, analytic endpoint behavior and the critical function \(H_k\). The included diagnostic run passed 5,273 assertions. These tests are finite and do not establish the all-dimensional theorem; the derivative-factorization and endpoint argument above establish that theorem.

## Relationship to prior work
Gomi and Tsuji (2026) show that negative type alone does not ensure magnitude monotonicity for finite semimetrics with at least four points. Their Lemma 5.4 also gives a **general positive criterion** for every finite metric space whose magnitude weighting has at most one negative entry. The present equiradial configurations have positive leaf weights, hence this criterion already covers their entire metric subrange \(r\le2\), independently of cardinality. The new strict-monotonicity conclusion is confined to the negative-type **nonmetric** interval \(2<r\le r_c\), where that criterion does not apply. Their counterexample constructions do not furnish this positive nonmetric classification. Roff and Yoshinaga (2025, Theorem 3.3) derive a general join magnitude formula for homogeneous **metric** spaces whose within-part diameters are at most twice the cross distance. This supplies the basic algebraic formula in the metric portion \(r\le2\), but this earlier join formula does not itself assert strict monotonicity, and the cited metric-only criteria do not cover the nonmetric interval \(2<r\le r_c\) or its singular centroid transition. The novelty claim is restricted accordingly.

## Limitations
The result concerns only an equilateral leaf configuration together with one equiradial hub, not arbitrary semimetrics of negative type. It does not restore universal magnitude monotonicity, which is false in general. The small-scale critical limit is a property of **squared Euclidean distances**, not of ordinary Euclidean distances. The leading crossover is proved only in the stated simultaneous scaling; no uniform estimate for unbounded \(\tau\) is asserted. Although the relevant primary sources and indexed records were compared, unpublished or unindexed equivalent calculations may exist; independent assessment of originality has not been performed.

## References
- K. Gomi and H. Tsuji, *On the monotonicity of magnitude functions of negative type finite semimetric spaces*, arXiv:2608.15720v1 (first public version: 2026-08-16), https://arxiv.org/abs/2608.15720.
- E. Roff and M. Yoshinaga, *The small-scale limit of magnitude and the one-point property*, Bulletin of the London Mathematical Society 57 (2025), 1841–1855, Theorem 3.3, https://doi.org/10.1112/blms.70064.
- Y. Asao and K. Gomi, *Geometric interpretation of magnitude*, arXiv:2510.26118 (2025), https://arxiv.org/abs/2510.26118. Only its abstract was accessible during this comparison.
