# Sharp leaf-count transitions in one-point \(p\)-Banach Lipschitz extensions

## Finding
For every integer \(n\ge4\) and real exponent \(0<p\le1\), let \(N_n=\{v_1,\ldots,v_n\}\) be an equilateral metric space with \(d(v_i,v_j)=2\) for distinct leaves, and let \(M_n=N_n\cup\{o\}\) be the metric star with \(d(o,v_i)=1\). Define the universal \(p\)-trace \(\mathfrak t_p(N_n,M_n)\) as the least \(C\) such that every Lipschitz map \(f:N_n\to Y\) to every real \(p\)-Banach space admits an extension \(\widetilde f:M_n\to Y\) with \(\operatorname{Lip}(\widetilde f)\le C\operatorname{Lip}(f)\). Then
\[
\boxed{\mathfrak t_p(N_n,M_n)=\min\left\{2,\frac{2}{n}(n-1)^{1/p}\right\}.}
\]
The transition exponent is
\[
p_n=\frac{\log(n-1)}{\log n},\qquad 0<p_n<1,\qquad p_n\nearrow1.
\]
For \(0<p<p_n\), the trace is exactly \(2\); for \(p_n<p\le1\), it is \(2(n-1)^{1/p}/n<2\). At \(p=p_n\), both expressions agree. For the canonical extremizing boundary map into the real finite-dimensional Lipschitz-free \(p\)-space \(\mathcal F_p(N_n)\), the optimal new-center images are precisely the leaves when \(p<p_n\), precisely their arithmetic barycenter when \(p>p_n\), and precisely these \(n+1\) points at equality. For fixed \(0<p<1\), the universal trace equals \(2\) for every sufficiently large finite \(n\); for \(p=1\), it equals \(2-2/n<2\) for each finite \(n\).

## Assumptions and scope
All vector spaces and scalar coefficients are real. A \(p\)-Banach space is a complete real vector space with a homogeneous separating \(p\)-norm satisfying \(\|x+y\|^p\le\|x\|^p+\|y\|^p\). The domain metrics have exactly the specified \(n+1\) points. The trace quantifies over every such target and every Lipschitz boundary map; it is not a statement about extensions from arbitrary subsets of arbitrary metric spaces. The index restriction \(n\ge4\) deliberately excludes the previously established three-leaf instance.

## Proof
**Universal upper bound.** Normalize \(\operatorname{Lip}(f)=1\); the zero-Lipschitz case is trivial. Put \(y_i=f(v_i)\). Setting \(\widetilde f(o)=y_k\) for any \(k\) yields \(\|\widetilde f(o)-y_i\|\le2\) for every leaf and hence extension constant at most \(2\). Alternatively set \(\widetilde f(o)=n^{-1}\sum_{j=1}^n y_j\). For each \(i\), homogeneity and the \(p\)-triangle inequality give
\[
\left\|\frac1n\sum_{j=1}^ny_j-y_i\right\|^p
\le\frac1{n^p}\sum_{j\ne i}\|y_j-y_i\|^p
\le\frac{(n-1)2^p}{n^p}.
\]
Thus \(\mathfrak t_p\le\min\{2,2(n-1)^{1/p}/n\}\).

**One universal extremizer.** Let \(E=\mathcal F_p(N_n)\) be the real finite Lipschitz-free \(p\)-space (choose any leaf as base point), and set \(f(v_i)=\delta(v_i)\). Its Lipschitz constant is exactly one. Every \(z\in E\) is uniquely of the form \(z=\sum_{j=1}^n\lambda_j\delta(v_j)\), where the real barycentric coefficients satisfy \(\sum_j\lambda_j=1\); this representation is independent of the chosen base point. Since \(\|\cdot\|_{\mathcal F_p}\ge\|\cdot\|_{\mathcal F_1}\) and the Arens–Eells norm on an equilateral space of side two is the sum of absolute zero-mass coefficients, any \(\lambda_i<0\) satisfies
\[
\|z-\delta(v_i)\|_{\mathcal F_p}\ge
\|z-\delta(v_i)\|_{\mathcal F_1}
=\sum_{j=1}^n|\lambda_j-\mathbf1_{j=i}|
\ge2(1-\lambda_i)>2.
\]
Therefore a center improving on radius \(2\), or attaining the optimum, may be sought in the standard simplex \(\lambda_i\ge0\).

**Exact free \(p\)-norm on the simplex.** For every simplex vector \(\lambda\) and each leaf \(i\),
\[
\boxed{\left\|\sum_{j=1}^n\lambda_j\delta(v_j)-\delta(v_i)\right\|_{\mathcal F_p}^p=2^p\sum_{j\ne i}\lambda_j^p.}
\]
The upper inequality is the \(p\)-triangle inequality applied to \(\sum_{j\ne i}\lambda_j(\delta(v_j)-\delta(v_i))\). For the reverse inequality, use the finite spanning-tree formula for free \(p\)-norms [Cúth–Raunig, Theorem 2.2]: root each spanning tree at \(i\). The coefficient flowing along the edge from a nonroot vertex \(j\) toward its parent equals the sum of nonnegative coefficients \(\lambda_k\) in the subtree rooted at \(j\), so its magnitude is at least \(\lambda_j\). Every edge has length \(2\). Therefore every tree \(p\)-cost is at least \(2^p\sum_{j\ne i}\lambda_j^p\), proving equality after minimization over all trees.

**Finite but dimension-uniform minimax.** The optimal radius in \(E\) is \(2\) times the \(1/p\)-power of
\[
\inf_{\lambda_i\ge0,\ \sum\lambda_i=1}\ \max_i\sum_{j\ne i}\lambda_j^p.
\]
By permutation symmetry, sort the coefficients as \(0\le\lambda_1\le\cdots\le\lambda_n\). Then the objective is \(F(\lambda)=\sum_{j=2}^n\lambda_j^p\), a concave function on this ordered simplex. Its extreme points have exactly \(k\) final coordinates equal to \(1/k\), and the other coordinates zero, for \(1\le k\le n\): indeed the adjacent differences \(d_j=\lambda_j-\lambda_{j-1}\) (with \(\lambda_0=0\)) are nonnegative and satisfy \(\sum_{j=1}^n(n-j+1)d_j=1\), which defines a simplex with precisely these vertices. A concave function reaches its minimum at a vertex, whose objective value is
\[
F_k=\begin{cases}k^{1-p},&1\le k<n,\\
(n-1)n^{-p},&k=n.\end{cases}
\]
Since \(k^{1-p}\ge1\), the minimum equals \(\min\{1,(n-1)n^{-p}\}\). Its resulting radius equals the preceding universal upper bound, establishing the trace formula. For \(p<1\), strict concavity makes every nonvertex of the ordered simplex strictly worse than its minimizing vertices, and every intermediate vertex \(1<k<n\) has value strictly larger than \(1\). The only possible minimizers are thus leaves and/or the uniform barycenter, with the stated threshold. For \(p=1\), the objective is \(1-\lambda_1\), minimized uniquely by maximizing the smallest coordinate; this again forces the uniform barycenter.

**Threshold.** The equality \((n-1)n^{-p}=1\) is equivalent to \(p=\log(n-1)/\log n\). This threshold strictly increases toward \(1\) as \(n\) grows; in particular, \((n-1)/n^p\to\infty\) for fixed \(p<1\), whereas the Banach endpoint yields \(2(n-1)/n\).

## Verification
An accompanying standalone finite stress checker enumerates all labeled spanning trees by Prüfer sequences for dimensions \(n=4,5,6\), checks that the predicted optimal leaf/barycenter radius coincides with the finite tree expression for \(p\in\{0.45,0.7,0.83,1\}\), and tests twenty random simplex vectors per case. The checker is supplementary; its sampled centers cannot prove the universal claim. The preceding analytic spanning-tree/minimax argument proves all integers \(n\ge4\) and all real \(0<p\le1\).

## Relationship to prior work
Bíma [1] formulates the universal \(p\)-trace and analyzes other three-point examples, giving general quantitative extension bounds. Cúth and Raunig [2] supply the finite spanning-tree free \(p\)-norm theorem used here as a tool; that general norm algorithm does not itself state the sharp trace phase diagram of an arbitrary \(n\)-leaf star. Basso [3] establishes universal one-point bounds and examples of sharp factor two, but not this full \(n\)-dependent threshold. Bíma [4] analyzes Lipschitz-free \(p\)-spaces and cubical interpolation with a different domain geometry. Albiac and Ansorena [5] establish general inclusion embeddings/extension constructions, not an exact value for this leaf-to-star metric trace in the inspected introductory and relevant theorem sections. An earlier exact three-leaf case is excluded from the claim and does not imply the dimension-uniform minimax and sharp phase transition given here.

## Limitations
The result concerns real \(p\)-Banach target spaces, one-point extensions on the prescribed finite metric star, and the canonical extremizer's center geometry only. It does not supply universal optimal-center uniqueness for arbitrary target maps or extension constants for general trees. Previous and unindexed literature may express a logically equivalent formula under different terminology; mathematical novelty has not received independent review.

## References
[1] Jan Bíma, *Nagata Dimension and Lipschitz Extensions Into Quasi-Banach Spaces*, arXiv:2402.03189v1 (first posted 2024-02-05), especially Definition 2 and Proposition 26 / Theorem 30. https://arxiv.org/abs/2402.03189

[2] Marek Cúth and Tomáš Raunig, *Canonical Embedding of Lipschitz-Free \(p\)-Spaces*, arXiv:2311.02920v1 (2023), especially Theorem 2.2 and Theorem 2.8. https://arxiv.org/abs/2311.02920

[3] Giuliano Basso, *Lipschitz Extensions to Finitely Many Points*, arXiv:1707.06593v1 (2017), especially the one-point bound and Section 4. https://arxiv.org/abs/1707.06593

[4] Jan Bíma, *Lipschitz Free Spaces and Subsets of Finite-Dimensional Spaces*, arXiv:2303.03265v1 (2023). https://arxiv.org/abs/2303.03265

[5] Fernando Albiac and José L. Ansorena, *Lipschitz Extensions into \(p\)-Banach Spaces, and Canonical Embeddings of Lipschitz-Free \(p\)-Spaces for \(0<p<1\)*, arXiv:2603.28193v1 (2026), inspected for possible stronger coverage. https://arxiv.org/abs/2603.28193
