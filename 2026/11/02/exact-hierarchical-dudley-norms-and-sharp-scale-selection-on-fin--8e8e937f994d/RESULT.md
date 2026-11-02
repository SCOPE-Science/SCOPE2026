# Exact hierarchical Dudley norms and sharp scale selection on finite ultrametrics

## Finding

Let \((X,d)\) be a finite ultrametric space with at least two points. Give its canonical cluster tree \(T\) the full-distance heights \(h(x)=0\) at leaves and \(h(v)=d(x,y)\) for leaves \(x,y\) from distinct children of an internal vertex \(v\). Its root has height \(D=\operatorname{diam}(X)\). For a real signed measure \(\sigma=\sum_{x\in X}\sigma_x\delta_x\) with \(\sum_x\sigma_x=0\), put \(M(v)=\sum_{x\in X_v}\sigma_x\), where \(X_v\) is the set of leaves below vertex \(v\). Define, for \(s>0\),

\[
 B_\sigma(s)=\sum_{v\ne\mathrm{root}}
 \bigl(\min\{h(\operatorname{parent}(v)),s\}-\min\{h(v),s\}\bigr)|M(v)|.
\]

Let \(H=\{h(v):v\text{ internal}\}\) be the set of distinct positive cluster heights. Then the dual **sum-norm** bounded-Lipschitz, or Dudley, norm is exactly

\[
 \boxed{\|\sigma\|_{BL^*}
 =\sup_{\|f\|_\infty+\operatorname{Lip}_d(f)\le1}
 \left|\sum_{x\in X}\sigma_x f(x)\right|
 =\max_{s\in H}\frac{B_\sigma(s)}{2+s}.}
\]

The maximum can be evaluated in \(O(|X|\log|X|)\) arithmetic operations from the cluster tree and signed leaf masses. A norming test function is explicitly constructible from the maximizing height and the signs of the subtree masses. Every height in \(H\) is indispensable as a candidate across the collection of zero-total-mass signed measures on the same ultrametric.

For a two-level ultrametric with two nonempty equilateral clusters \(A,B\), both containing at least two points, within-cluster distance \(a>0\) and between-cluster distance \(b>a\), set \(S=\tfrac12\sum_{x\in X}|\sigma_x|\) and \(P=|\sum_{x\in A}\sigma_x|\). Its norm is

\[
 \boxed{\|\sigma\|_{BL^*}
 =\max\left\{\frac{2aS}{2+a},
 \frac{2\bigl(aS+(b-a)P\bigr)}{2+b}\right\}.}
\]

For \(S>0\), the larger cluster scale \(b\) is strictly optimal precisely when \(P>aS/(2+a)\), while the smaller scale \(a\) is strictly optimal precisely when \(P<aS/(2+a)\); there is a tie at equality. The transition depends on \(a\), but not on the gap \(b-a>0\). Both strict regimes and the equality regime occur for signed masses on four points.

## Assumptions and scope

All functions and measures are real-valued, and \(\sigma(X)=0\). The underlying finite ultrametric has strictly positive distances between distinct points. A canonical finite cluster tree is obtained by merging all clusters simultaneously at each distinct occurring distance, so internal vertices have at least two children; equal-height unary vertices are removed. Its number of vertices is at most \(2|X|-1\). The formula uses full-distance heights, not radii or half-distances: the associated metric-tree edge from vertex \(v\) to its parent has length \((h(\operatorname{parent}(v))-h(v))/2\).

For a one-point space, or for \(\sigma=0\), the norm is zero. If \(X\) has two or more points but \(\sigma=0\), every scale in \(H\) yields zero. No claim is made for nonzero-total-mass measures or for infinite ultrametric spaces.

## Proof

**1. Convert the sum norm into a one-parameter transportation problem.** For \(r>0\), let \(d_r(x,y)=\min\{d(x,y),r\}\) for distinct points, and \(d_r(x,x)=0\). This is a metric; indeed it remains ultrametric. Define

\[
 F_\sigma(r)=\max\left\{\sum_x\sigma_x g(x):
 \operatorname{Lip}_d(g)\le1,\quad
 \operatorname{osc}(g)\le r\right\},
\]

where \(\operatorname{osc}(g)=\max g-\min g\). The two constraints are equivalent to \(\operatorname{Lip}_{d_r}(g)\le1\). Write \(\sigma=\sigma^+-\sigma^-\) with equal total masses. By finite Kantorovich--Rubinstein duality,

\[
 F_\sigma(r)=W_1^{d_r}(\sigma^+,\sigma^-),
\]

with the usual equal-mass transport normalization; when the common mass is zero both sides vanish. In fact the next step supplies an elementary direct proof of the needed transport formula.

The center of the range of \(g\) can be subtracted without changing its pairing with \(\sigma\), and the resulting function has sup norm \(\operatorname{osc}(g)/2\). Consequently

\[
 \boxed{\|\sigma\|_{BL^*}=\sup_{r>0}\frac{F_\sigma(r)}{1+r/2}.}
\]

For the inequality from left to right, take a feasible bounded-Lipschitz \(f\) with Lipschitz constant \(L>0\), put \(g=f/L\), and \(r=\operatorname{osc}(f)/L\). Then \(\sum\sigma_x f(x)\le L F_\sigma(r)\), while \(1\ge \|f\|_\infty+L\ge L(1+r/2)\). Constant \(f\) pair to zero. For the reverse inequality, center any maximizer of \(F_\sigma(r)\), then divide it by \(1+r/2\); this is a feasible test function because \(\operatorname{Lip}_d(g)\le1\) and \(\operatorname{osc}(g)\le r\). Absolute values are handled by replacing \(g\) with \(-g\).

**2. Evaluate truncated transportation through each tree cut.** Attach to each nonroot tree vertex \(v\) an edge of length

\[
 \ell_v(r)=\frac{\min\{h(\operatorname{parent}(v)),r\}-\min\{h(v),r\}}{2}.
\]

The distance between any two leaves in this edge-weighted tree equals \(d_r\): their paths meet at height \(\min\{h(\mathrm{LCA}),r\}\). For any leaf function \(g\) with \(\operatorname{Lip}_{d_r}(g)\le1\), extend \(g\) to the metric tree without increasing its Lipschitz constant. Telescoping along root-to-leaf paths and using \(\sum_x\sigma_x=0\) gives

\[
 \sum_x\sigma_xg(x)
 =\sum_{v\ne\mathrm{root}}M(v)
 \bigl(g(v)-g(\operatorname{parent}(v))\bigr)
 \le\sum_{v\ne\mathrm{root}}\ell_v(r)|M(v)|.
\]

This upper bound is attained simultaneously on all edges: set the root potential to zero and prescribe

\[
 g(v)-g(\operatorname{parent}(v))
 =\ell_v(r)\,\operatorname{sign}(M(v)),
\]

with \(\operatorname{sign}(0)=0\). Its restriction to leaves is \(1\)-Lipschitz for \(d_r\), because the absolute difference across any path is at most its length. Thus

\[
 F_\sigma(r)=\sum_{v\ne\mathrm{root}}\ell_v(r)|M(v)|
 =\frac{B_\sigma(r)}2.
\]

Together with Step 1, this proves the continuous-scale formula \(\|\sigma\|_{BL^*}=\sup_{r>0}B_\sigma(r)/(2+r)\).

**3. Prove that only cluster heights matter.** Each summand of \(B_\sigma(r)\) is linear in \(r\) on intervals that exclude vertex heights. Therefore \(B_\sigma(r)=u+vr\) on each such interval, and

\[
 \frac{d}{dr}\frac{u+vr}{2+r}=\frac{2v-u}{(2+r)^2}
\]

has constant sign. Hence there are no strict local interior maxima on a breakpoint-free interval. On \([D,\infty)\), the numerator is constant, so the ratio cannot increase. As \(r\downarrow0\), it tends to zero. The global maximum is therefore attained at a positive internal height \(s\in H\). Steps 1--3 prove the first boxed formula. Taking the constructive vertex potential at a maximizing scale, centering its leaf range, and dividing by \(1+s/2\) constructs a norm-attaining Dudley test function explicitly.

**4. Prove the algorithm and sharpness of the candidate heights.** Compute all \(M(v)\) bottom-up. Each edge \((v,\operatorname{parent}(v))\) contributes \(\bigl[\min(h(\operatorname{parent}(v)),r)-\min(h(v),r)\bigr]|M(v)|\) to the numerator. Its derivative is \(|M(v)|\) precisely on the interval \(h(v)<r<h(\operatorname{parent}(v))\), and zero elsewhere. A sweep through the sorted distinct positive heights, updating slope by \(+|M(v)|\) at \(h(v)\) and \(-|M(v)|\) at \(h(\operatorname{parent}(v))\), evaluates the numerator and every candidate ratio. Initial slope includes the contributions beginning at zero. This uses \(O(|X|\log|X|)\) comparisons and arithmetic operations and \(O(|X|)\) storage; when the heights are pre-sorted it is linear.

For each \(s\in H\), choose leaves \(x,y\) from different children of an internal vertex of height \(s\). Their distance is \(s\). For \(\sigma=\delta_x-\delta_y\), the first two steps yield \(B_\sigma(r)=2\min\{s,r\}\), so \(B_\sigma(r)/(2+r)\) increases strictly until \(r=s\) and decreases strictly afterwards. Thus no height in \(H\) can be universally omitted.

**5. Derive the two-level transition.** In the two-cluster setting, the leaf-edge contributions at the within-cluster height \(a\) are \(2aS\); the two cluster-to-root edges contribute \(2(b-a)P\) when saturated at \(b\). Consequently \(B_\sigma(a)=2aS\) and \(B_\sigma(b)=2[aS+(b-a)P]\). The height formula gives the second boxed identity. Comparing its two entries and dividing by the strictly positive \(b-a\) yields exactly \(P\gtrless aS/(2+a)\). For any \(S>0\) and \(0\le P\le S\), the four leaf weights

\[
 \sigma|_A=\bigl((S+P)/2,-(S-P)/2\bigr),\qquad
 \sigma|_B=\bigl((S-P)/2,-(S+P)/2\bigr)
\]

realize these parameters, proving sharp attainability of both regimes and their boundary.

## Verification

The standalone file `CHECKER.py` independently optimizes the original bounded-Lipschitz constrained linear program and compares it to the tree-height formula for 180 generated finite ultrametrics. It additionally checks 90 two-cluster instances against both the explicit formula and the linear program, and 11 atomic-pair examples against \(2d(x,y)/(2+d(x,y))\). All 281 supplementary checks passed with the numerical tolerances in the script. Reproduce using `python CHECKER.py` with Python 3, NumPy and SciPy. These finite numerical tests verify implementation and representative boundary cases; the proof above, not enumeration, establishes the universal statements.

## Relationship to prior work

Hille and Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions* (arXiv:2305.08500v1, public May 15, 2023), examine the same sum-type bounded-Lipschitz norm for general metric spaces, describing norming sets of extreme functions; Section 6 discusses the finite case, but does not provide the ultrametric height formula, scale reduction, or two-cluster threshold above.

Hille and Theewis, *The Fortet--Mourier distance to weighted sums of Dirac measures* (arXiv:2206.12234), Section 6, discuss general linear-programming computation of Dudley norms and explain that the sum-type constraint is coupled. That general program computes individual finite instances but does not itself state the closed hierarchical expression or the optimal-scale criterion.

Kloeckner, *A geometric study of Wasserstein spaces: ultrametrics* (arXiv:1304.5219), Section 3.1, Lemma 3.1, proves the known tree-cut expression for \(W_1\) on an ultrametric. This establishes the transportation ingredient; the conversion of the coupled bounded-Lipschitz sum norm into a truncated transport family, finite height reduction, efficient sweep, and sharp mass-imbalance switch are distinct statements. The source uses half-distance tree heights, so the factor-of-two normalization here has been checked directly in Step 2.

A publicly available calculation, *Exact Dudley norms and mass-imbalance thresholds on equiradial stars* (October 2026), gives an exact formula for equal-arm star metrics including the center. Its zero-center-mass specialization already covers the **one-height equilateral ultrametric** case, which is not claimed as new here. The star result does not contain the general multilevel formula or the two-cluster transition. The full scientific statement and proof were compared.

Leeb, *The mixed Lipschitz space and its dual for tree metrics* (Applied and Computational Harmonic Analysis, 2016, DOI:10.1016/j.acha.2016.06.008), Section 3, studies a different \(\max\)-norm coupling the Lipschitz seminorm with a mean functional, as well as tree transportation. Its norm is not the Dudley \(\|f\|_\infty+\operatorname{Lip}(f)\) used here. The generality of these earlier methods is acknowledged; no exclusive priority or independence is asserted.

## Limitations

The theorem requires a finite **ultrametric**, real signed coefficients of **zero total mass**, and precisely the sum-type test-function norm. It does not cover measures with nonzero total mass, arbitrary finite metrics, complex-valued dual norms, or infinite trees. It does not claim the underlying ultrametric Wasserstein tree formula or general finite-dimensional linear-programming duality is new. A hidden equivalent formulation under bounded transport, flat norms, or hierarchical optimal-transport terminology remains a literature-priority risk. Independent mathematical validation has not been performed.

## References

1. S. C. Hille and E. S. Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions*, arXiv:2305.08500v1 (May 15, 2023), https://arxiv.org/abs/2305.08500.
2. S. C. Hille and E. S. Theewis, *The Fortet--Mourier distance to weighted sums of Dirac measures*, arXiv:2206.12234, Section 6, https://arxiv.org/abs/2206.12234.
3. B. R. Kloeckner, *A geometric study of Wasserstein spaces: ultrametrics*, arXiv:1304.5219, Section 3.1, https://arxiv.org/abs/1304.5219.
4. W. A publicly available calculation, *Exact Dudley norms and mass-imbalance thresholds on equiradial stars* (October 2026), gives an exact formula for equal-arm star metrics including the center. Its zero-center-mass specialization already covers the **one-height equilateral ultrametric** case, which is not claimed as new here. The star result does not contain the general multilevel formula or the two-cluster transition. The full scientific statement and proof were compared.

Leeb, *The mixed Lipschitz space and its dual for tree metrics*, Applied and Computational Harmonic Analysis (2016), DOI:10.1016/j.acha.2016.06.008, https://williamleeb.com/papers/leeb_mixed.pdf.

5. *Exact Dudley norms and mass-imbalance thresholds on equiradial stars*, public record (October 2026), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-dudley-norms-and-mass-imbalance-thresholds-on-equiradial-s--ecc3b6450a54/RESULT.md.
