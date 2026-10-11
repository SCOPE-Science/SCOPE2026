# Exact all-order Hausdorff convexification profile of a raised-simplex set

## Finding
Fix an integer \(n\ge 2\). Let \(v_1,\ldots,v_n\) be the vertices of a centered regular \((n-1)\)-simplex in \(\mathbb R^{n-1}\), normalized by \(\|v_i\|_2=1\), and let \(T=\operatorname{conv}\{v_1,\ldots,v_n\}\). Embed \(T\) at height zero in \(\mathbb R^n\), and put
\[
A_\varepsilon=(T\times\{0\})\cup\{(v_i,\varepsilon):1\le i\le n\},
\qquad 0<\varepsilon<\frac1{(n-1)^2}.
\]
For every nonempty compact set \(A\), write \(A^{(k)}=\frac1k(A+\cdots+A)\) for the \(k\)-fold Minkowski average and
\[
d(A)=\sup_{x\in\operatorname{conv}(A)}\operatorname{dist}_2(x,A).
\]
Then **simultaneously for every integer \(k\ge1\)**,
\[
\boxed{\quad d(A_\varepsilon^{(k)})=\varepsilon\min\left\{1,\frac{n-1}{k}\right\}.\quad}
\]
In addition, the Schneider nonconvexity index \(c(A)=\inf\{s\ge0:A+s\operatorname{conv}(A)\text{ is convex}\}\) of this same set equals \(n-1\). Thus it attains equality at **every averaging order** in the general index-dependent bound \(d(A^{(k)})\le \min\{1,\lceil c(A)\rceil/k\}d(A)\) of Fradelizi--Madiman--Marsiglietti--Zvavitch. In particular, the first strictly contracting order is \(k=n\), where the exact ratio is \((n-1)/n\).

## Assumptions and scope
The ambient norm is Euclidean; all Minkowski sums are unweighted and use the same compact set. The simplex vertices lie in \(\mathbb R^{n-1}\) and have common Euclidean norm one. No assertion is made that the displayed upper restriction on \(\varepsilon\) is optimal, or that the constant \((n-1)/n\) is a universal upper bound for arbitrary compact sets. The statement applies to every integer \(n\ge2\) and all averaging orders \(k\ge1\), with a *single* \(\varepsilon\) satisfying the stated strict inequality.

## Proof
**Geometric coordinate inequality.** The regular simplex satisfies \(\langle v_i,v_j\rangle=-1/(n-1)\) for \(i\ne j\). If \(b=\sum_i\lambda_i v_i\) and \(b'=\sum_i\mu_i v_i\), where both coefficient vectors have nonnegative entries summing to one, then
\[
\|b-b'\|_2^2=\frac n{n-1}\sum_i(\lambda_i-\mu_i)^2.
\]
As \(\sum_i(\lambda_i-\mu_i)=0\), whenever one coordinate differs by at least \(a\ge0\), Cauchy--Schwarz on the other \(n-1\) coordinates implies
\[
\|b-b'\|_2\ge\frac n{n-1}a.\tag{1}
\]

**Accessible vertical levels.** We have \(\operatorname{conv}(A_\varepsilon)=T\times[0,\varepsilon]\). For \(b=\sum_i\lambda_i v_i\in T\), let \(f_i=\lfloor k\lambda_i\rfloor\) and \(F=\sum_i f_i\). Since \(\sum_i k\lambda_i=k\), the sum of the fractional parts equals the integer \(k-F\in\{0,\ldots,n-1\}\). Hence \(F\ge k-n+1\).

For every integer \(j\) with \(0\le j\le F\), select integers \(0\le c_i\le f_i\) summing to \(j\). If \(j<k\), the point
\[
s=\frac{\sum_i(k\lambda_i-c_i)v_i}{k-j}\in T
\]
permits the exact average of \(c_i\) copies of raised vertex \((v_i,\varepsilon)\) and \(k-j\) copies of \((s,0)\). It is \((b,j\varepsilon/k)\). If \(j=k\), there are no base copies and the same point is a valid average of raised vertices alone. Consequently
\[
\{(b,j\varepsilon/k):0\le j\le F\}\subseteq A_\varepsilon^{(k)}.\tag{2}
\]

**Upper estimate.** The base \(T\times\{0\}\) is contained in every \(A_\varepsilon^{(k)}\), so \(d(A_\varepsilon^{(k)})\le\varepsilon\). When \(k\ge n\), (2) supplies a vertical mesh from height zero through at least \((k-n+1)\varepsilon/k\). Every height in this meshed interval is within \(\varepsilon/(2k)\) of an accessible height, while all greater heights up to \(\varepsilon\) are within \((n-1)\varepsilon/k\) of the last accessible height. Since \(n\ge2\),
\[
d(A_\varepsilon^{(k)})\le \frac{n-1}{k}\varepsilon\quad(k\ge n).\tag{3}
\]

**Matching lower estimate below the threshold.** Suppose \(k<n\) and consider \(x=(0,\varepsilon)\in T\times[0,\varepsilon]\), where zero is the simplex centroid. An average of \(k\) base points lies at height zero, hence has distance at least \(\varepsilon\) from \(x\). Any average containing a raised vertex has a horizontal barycentric coefficient of at least \(1/k\) in some coordinate; the centroid has every coefficient equal to \(1/n\). By (1), its horizontal distance from zero is at least
\[
\frac{n-k}{k(n-1)}\ge\frac1{(n-1)^2}>\varepsilon.
\]
The base point \((0,0)\) attains distance \(\varepsilon\). Thus \(d(A_\varepsilon^{(k)})=\varepsilon\) for all \(k<n\).

**Matching lower estimate at and after the threshold.** Fix \(k\ge n\), set \(J=k-n+1\), and choose the barycentric vector
\[
\lambda_1=\frac{J+(n-1)/n}{k},\qquad
\lambda_i=\frac{n-1}{nk}\quad(2\le i\le n).
\]
These entries are positive, sum to one, and have floors \(\lfloor k\lambda_1\rfloor=J\) and \(\lfloor k\lambda_i\rfloor=0\) for \(i>1\). Set \(b=\sum_i\lambda_i v_i\) and \(x=(b,\varepsilon)\). If \(y\in A_\varepsilon^{(k)}\) uses \(j\le J\) raised vertices, its height is \(j\varepsilon/k\), so \(\|x-y\|_2\ge(n-1)\varepsilon/k\).

If instead \(j>J\), at least one count \(c_i\) of raised vertex \(i\) exceeds \(\lfloor k\lambda_i\rfloor\). Thus the horizontal barycentric coordinate \(\mu_i\) of \(y\) satisfies
\[
\mu_i-\lambda_i\ge\frac{\lfloor k\lambda_i\rfloor+1-k\lambda_i}{k}=\frac1{nk}.
\]
By (1), \(y\)'s horizontal distance from \(b\) is at least \(1/((n-1)k)\), which is **strictly greater** than \((n-1)\varepsilon/k\) by the hypothesis on \(\varepsilon\). Finally (2), with \(j=J\), supplies \((b,J\varepsilon/k)\in A_\varepsilon^{(k)}\) exactly \((n-1)\varepsilon/k\) from \(x\). This proves equality in (3) for all \(k\ge n\), and completes the exact distance formula.

**Schneider index and sharpness.** For \(s\ge0\), the convex hull of \(A_\varepsilon+s\operatorname{conv}(A_\varepsilon)\) is \((1+s)T\times[0,(1+s)\varepsilon]\). Its top horizontal slice is
\[
\bigcup_{i=1}^{n}(v_i+sT).
\]
A point \(b=(1+s)\sum_i\lambda_i v_i\) of the full top face belongs to the \(i\)th simplex exactly when \(\lambda_i\ge1/(1+s)\). The entire face is covered precisely when \(1/(1+s)\le1/n\), or \(s\ge n-1\). Thus convexity requires \(s\ge n-1\). Conversely, when \(s\ge n-1\), the base contribution \((1+s)T\times[0,s\varepsilon]\) covers all low heights, the top-vertex contributions cover every horizontal point at heights \([\varepsilon,(1+s)\varepsilon]\), and the intervals overlap because \(s\ge1\). The union is the whole prism, proving \(c(A_\varepsilon)=n-1\). Combining the exact distance law with the published index-dependent inequality identifies a single nonconvex example saturating that inequality for every \(k\).

## Verification
The self-contained standard-library program `check_profile.py` uses exact rational arithmetic. It tests all displayed barycentric and separation identities for \(2\le n\le30\) and \(1\le k\le150\). In thirteen selected full instances, it enumerates every feasible vector of raised-vertex multiplicities and solves the horizontal nearest-point quadratic program with exact fractions; all agree with the formula. Run `python3 check_profile.py` from the package directory. The **all-dimensional proof is the argument above**, not finite testing.

## Relationship to prior work
Peter van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition* (arXiv:2606.10815v1, first submitted 9 June 2026), introduced exactly this raised-simplex configuration for \(0<\varepsilon<1/n^3\). His Theorem 1.3 establishes the noncontraction regime \(1\le k\le n-1\), and his Theorem 1.4 gives a general \(k=n\) contraction by a different coefficient. The present result does **not** claim a new construction or re-prove those statements as novel: it determines the previously unstated exact profile for every averaging order, including the first post-threshold drop, for a wider displayed height range.

Fradelizi, Madiman, Marsiglietti and Zvavitch, *The convexification effect of Minkowski summation* (EMS Surveys in Mathematical Sciences 5, 2018), Theorem 7.10, established the general Schneider-index upper bound. The new equalities here identify a family attaining the bound simultaneously for all orders. In particular, the result provides the lower bound \(\sup_A d(A^{(n)})/d(A)\ge(n-1)/n\) for the optimal universal contraction coefficient; it does **not** establish the opposite universal inequality, which remains a separate question.

## Limitations
The parameter interval is sufficient, not proved largest. The argument uses Euclidean distances and a regular simplex; no affine-invariant or arbitrary-norm sharpness is claimed. Matching the index-dependent upper bound in one family does not settle universal best constants for all compact sets. The literature comparison cannot exclude unindexed equivalent treatments.

## References
1. P. van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition*, arXiv:2606.10815v1 (9 June 2026), https://arxiv.org/abs/2606.10815 ; complete public text also available at https://www.researchgate.net/publication/406875078_The_sharp_threshold_for_Hausdorff_convexification_under_Minkowski_addition .
2. M. Fradelizi, M. Madiman, A. Marsiglietti, A. Zvavitch, *The convexification effect of Minkowski summation*, EMS Surveys in Mathematical Sciences **5** (2018), 1–64, https://people.clas.ufl.edu/amarsiglietti/files/FMMZ_Convexification_Effect.pdf .
3. R. Schneider, *A measure of convexity for compact sets*, Pacific Journal of Mathematics **58** (1975), 617–625.
