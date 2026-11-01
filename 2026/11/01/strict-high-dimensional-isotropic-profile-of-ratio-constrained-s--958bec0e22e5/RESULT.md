# Strict high-dimensional isotropic profile of ratio-constrained simplex cores

## Finding
Let \(m\ge3\), \(s>0\), and let \(\Delta_m=\{x\in\mathbb R^m:x_i\ge0,\ \sum_{i=1}^m x_i=1\}\), a Euclidean simplex of dimension \(m-1\). Its ratio-constrained core is
\[
P_m(s)=\left\{x\in\Delta_m:\max_i x_i\le(1+s)\min_i x_i\right\}.
\]
For a full-dimensional convex body \(K\) in its affine span of dimension \(d\), write \(L(K)^{2d}=\det(\operatorname{Cov}(\operatorname{Unif}K))/\operatorname{vol}_d(K)^2\). The determinant and volume use the same Euclidean coordinates on the affine span. The theorem has a typical-point limit shape and an exact affine-invariant asymptotic. If \(X_m\) is uniform in \(P_m(s)\) and \(X_{m,(1)}\le\cdots\le X_{m,(m)}\) are its ordered barycentric coordinates, then for **every fixed** \(s>0\),
\[
\max_{1\le j\le m}\left|mX_{m,(j)}-g_s(j/m)\right|\xrightarrow[m\to\infty]{\mathbb P}0,
\qquad
g_s(t)=\frac{1+s}{s}\log(1+s)-\log(1+s-st),\quad 0\le t\le1.
\]
The **same theorem** determines the exact isotropic-constant limit
\[
\lim_{m\to\infty}\frac{L(P_m(s))}{L(\Delta_m)}
=F(s):=\frac{(1+s)^{(1+s)/s}}{s}
\sqrt{1-\frac{1+s}{s^2}\log^2(1+s)}.
\]
The expression under the square root is strictly positive. Moreover \(F\) is **strictly increasing** on \((0,\infty)\), and its exact endpoint range is
\[
\lim_{s\downarrow0}F(s)=\frac{e}{\sqrt{12}},\qquad
\lim_{s\to\infty}F(s)=1.
\]
In particular, the original edge-trisection central polytope corresponds to \(s=1\) and has the sharp dimension-asymptotic ratio
\[
\lim_{m\to\infty}\frac{L(P_m(1))}{L(\Delta_m)}
=4\sqrt{1-2\log^2 2}=0.790887826823\ldots.
\]
This exact profile holds for the corresponding core of **any** nondegenerate simplex, by affine invariance.

## Assumptions and scope
All limits in \(m\) are taken through positive integers with \(m\ge3\) at a **fixed** real parameter \(s>0\). The core has nonempty relative interior. The limit is not asserted to be uniform when \(s\) depends on \(m\). In the displayed endpoint limits, \(m\to\infty\) is taken first.

Define \(D_k=m+s(m-k)\), \(1\le k<m\), and
\[
q_j=\sum_{k=1}^{m-1}\frac{s\bigl(k-m\mathbf 1_{\{j\le k\}}\bigr)}{mD_k},\quad 1\le j\le m.
\]
An exact finite-dimensional formula needed for the theorem is
\[
R_m(s)=\frac1{m-1}\left[
\sum_{k=1}^{m-1}\frac{s^2k(m-k)}{mD_k^2}
+\sum_{j=1}^m q_j^2\right],
\qquad
\operatorname{Cov}(P_m(s))=R_m(s)\operatorname{Cov}(\Delta_m),
\]
and the exact volume fraction is
\[
f_m(s)=\frac{\operatorname{vol}_{m-1}(P_m(s))}{\operatorname{vol}_{m-1}(\Delta_m)}
=\prod_{j=1}^{m-1}\frac{sj}{m+sj}
=\frac{\Gamma(m)\Gamma(1+m/s)}{\Gamma(m+m/s)}.
\]
Consequently, \(L(P_m(s))/L(\Delta_m)=\sqrt{R_m(s)}f_m(s)^{-1/(m-1)}\) exactly. No all-dimensional strict monotonicity assertion about this last **finite** ratio is made.

## Proof
**1. Ordered chambers and volume.** Partition \(P_m(s)\), modulo zero-volume hyperplanes, into the \(m!\) chambers in which the coordinates are ordered. In one chamber write \(x_1\le\cdots\le x_m\), \(d_k=x_{k+1}-x_k\ge0\), and \(x_1=(1-\sum_{k=1}^{m-1}(m-k)d_k)/m\). The last-to-first ratio bound is equivalent to
\[
\sum_{k=1}^{m-1}\bigl(m+s(m-k)\bigr)d_k\le s.
\]
Thus that chamber is an \((m-1)\)-simplex with vertices \(v^{(0)}=c=(1/m,\ldots,1/m)\) and \(v^{(k)}\) for \(1\le k<m\): its first \(k\) entries are \(1/D_k\) and its remaining \(m-k\) entries are \((1+s)/D_k\). The unrestricted ordered chamber of \(\Delta_m\) is defined by \(\sum_{k=1}^{m-1}(m-k)d_k\le1\). The linear map from \(d\) to \(x\) has the same constant Jacobian in both chambers. Taking the ratio of the corresponding simplex volumes gives \(f_m(s)=\prod_{k=1}^{m-1}s(m-k)/D_k\). Symmetry gives the same fraction for the whole body. Re-indexing yields the gamma quotient above.

**2. Exact covariance.** Both uniform bodies are invariant under all coordinate permutations, with the same centroid \(c\). On the zero-sum hyperplane their covariance matrices must be scalar, since a permutation-invariant symmetric matrix has constant diagonal and off-diagonal entries. Let \(X\) be uniform in \(P_m(s)\). For a simplex with \(m\) vertices \(v^{(0)},\ldots,v^{(m-1)}\), standard Dirichlet barycentric integration gives
\[
\mathbb E\left\|X-c\right\|^2
=\frac{\sum_{k=0}^{m-1}\|v^{(k)}-c\|^2
+\left\|\sum_{k=0}^{m-1}(v^{(k)}-c)\right\|^2}{m(m+1)}
\]
when \(X\) is uniform in that chamber. This is also the global expectation: permuting the chamber does not change distance from \(c\). For \(1\le k<m\),
\[
(v^{(k)}-c)_j=\frac{s(k-m\mathbf1_{\{j\le k\}})}{mD_k},\qquad
\|v^{(k)}-c\|^2=\frac{s^2k(m-k)}{mD_k^2}.
\]
For the full simplex the corresponding expectation is \((m-1)/(m(m+1))\). Dividing proves \(R_m(s)\) and the covariance identity. Affine invariance and volume scaling then give the exact isotropic-constant quotient.

**3. Typical-point limit shape.** Conditional on any fixed coordinate-order chamber, a uniform random point has the barycentric representation \(X_m=\sum_{k=0}^{m-1}W_kv^{(k)}\), with \(W\sim\operatorname{Dirichlet}(1,\ldots,1)\). This point is already sorted. Its conditional mean satisfies \(m\mathbb E X_{m,(j)}=1+q_j\). Since every \(mv^{(k)}_j\) lies in the fixed interval \([1/(1+s),1+s]\), the Dirichlet covariance identity yields
\[
\operatorname{Var}(mX_{m,(j)})=\frac{m^{-1}\sum_{k=0}^{m-1}(mv^{(k)}_j-m\mathbb EX_{m,(j)})^2}{m+1}
\le\frac{(1+s)^2}{m+1}.
\]
For each fixed \(0\le t\le1\), the Riemann-sum formula below shows \(m\mathbb EX_{m,(\lceil mt\rceil)}\to g_s(t)\), with the natural index \(1\) at \(t=0\). Chebyshev's inequality proves convergence in probability at finitely many grid points. The random coordinate profile is nondecreasing, as is the continuous function \(g_s\). Sandwiching between finitely many grid points and then refining their mesh upgrades the convergence to uniform convergence in probability over all ranks. The same reasoning applies before and after random permutation, since ordering discards the permutation. The displayed typical-point limit shape follows.

**4. Sharp high-dimensional covariance limit.** For fixed \(s>0\), the first sum in the expression for \(R_m(s)\) is \(O_s(1)\), so its contribution after division by \(m-1\) vanishes. The remaining entries \(q_j\) are uniformly approximated, as \(m\to\infty\), by Riemann sums at \(t=j/m\) for
\[
q(t)=s\int_0^1\frac{u-\mathbf1_{\{t\le u\}}}{1+s(1-u)}\,du
=\frac{1+s}{s}\log(1+s)-1-\log(1+s-st).
\]
Consequently \(R_m(s)\to\int_0^1q(t)^2\,dt\). If \(Z\) is uniform on \([1,1+s]\), then \(q(t)=\mathbb E\log Z-\log(1+s-st)\). Direct integration gives
\[
\int_0^1q(t)^2\,dt=\operatorname{Var}(\log Z)
=1-\frac{1+s}{s^2}\log^2(1+s)=:V(s)>0.
\]
Positivity is strict because \(\log Z\) is nonconstant for \(s>0\).

**5. Volume entropy and isotropic limit.** The gamma quotient and Stirling's formula give
\[
-\lim_{m\to\infty}\frac{\log f_m(s)}{m-1}
=I(s):=\frac{1+s}{s}\log(1+s)-\log s.
\]
Therefore \(L(P_m(s))/L(\Delta_m)\to e^{I(s)}\sqrt{V(s)}=F(s)\).

**6. Strict monotonicity of the limit.** Let \(\ell=\log(1+s)\). Differentiation yields \(I'(s)=-\ell/s^2\) and \(V'(s)=\ell((s+2)\ell-2s)/s^3\). Thus \(F'(s)>0\) is equivalent to
\[
B(s):=2(1+s)\ell^2+s(s+2)\ell-4s^2>0.
\]
Put \(u=\log(1+s)>0\). A direct simplification gives
\[
\frac{B(s)}{2e^u}=u\sinh u+u^2-4(\cosh u-1)
=\sum_{k=3}^{\infty}\frac{2k-4}{(2k)!}u^{2k}>0.
\]
Each summand is positive, and the series converges absolutely. Thus \(F\) increases strictly on the entire parameter range. Finally, \(V(s)=s^2/12+O(s^3)\) and \(e^{I(s)}=e/s+O(1)\) as \(s\downarrow0\); while \(V(s)\to1\) and \(I(s)\to0\) as \(s\to\infty\). These prove both endpoints. The special value \(s=1\) follows by substitution.

## Verification
The standalone standard-library program `verify.py` also samples ordered-chamber typical points to corroborate the stated shape law. It checks the finite-dimensional formulas using exact rational arithmetic; independently integrates the planar hexagonal case by a fan decomposition; compares normalized chamber determinant volumes with the gamma quotient; tests chamber-Dirichlet Monte Carlo second moments; and tests numerical convergence to the displayed limit. It also checks positive Taylor coefficients in a finite range. These checks corroborate the identities but do not establish the infinite series inequality or the high-dimensional limits; those are proven above. Invoke `python3 verify.py` beside this document.

## Relationship to prior work
Kazakov's 2026 treatment of Marion's central polytope studies precisely the \(s=1\) barycentric-ratio core and establishes its exact volume fraction and combinatorial structure. Its displayed results do not determine a typical-point sorted-coordinate limit shape, the affine-invariant covariance contraction, the limiting isotropic constant, or the strict all-ratio limiting profile. The general-ratio volume product here is elementary and is **not** asserted to be the novel part. General isotropic-constant research (for example, Rademacher's 2014 theorem and Kipp's 2026 work on shadow systems) concerns extremality/structural conditions, not this explicit high-dimensional family. A recent global simplex inequality, even if applied, would imply at most an upper bound, not the exact strict profile or endpoint values. Literature searches did not identify a stronger formula covering this same family; priority should be checked independently against older permutahedral and order-statistic work.

## Limitations
No finite-dimensional monotonicity of the isotropic constant quotient in \(s\) is claimed. The limits are for fixed \(s\), and no rate or uniformity as \(s=s_m\) varies with dimension is proved. The limit shape is a typical-uniform-point law, not a Hausdorff limit of the entire convex body. The result is asymptotic, not an exact elementary finite-dimensional isotropic constant; the exact finite formula is the displayed rational sum. All mathematical originality and proof assessments are preliminary pending independent verification and historical-priority review.

## References
1. Yu. V. Kazakov, *Generalization of Marion's Theorem: Volumes of Central Polytopes Obtained by Trisecting the Edges of Simplices*, arXiv:2606.02087v1, June 1, 2026. https://arxiv.org/abs/2606.02087
2. L. Rademacher, *A simplicial polytope that maximizes the isotropic constant must be a simplex*, arXiv:1404.5662, 2014. https://arxiv.org/abs/1404.5662
3. C. Kipp, *Shadow Systems, Decomposability and Isotropic Constants*, Discrete & Computational Geometry, published March 5, 2026. https://doi.org/10.1007/s00454-026-00829-7
