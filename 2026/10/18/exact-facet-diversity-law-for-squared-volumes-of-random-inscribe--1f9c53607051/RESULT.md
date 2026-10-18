# Exact facet-diversity law for squared volumes of random inscribed simplices

## Finding
Let \(d\ge2\) be any integer, \(m=d+1\), and \(S\subset\mathbb R^d\) be any nondegenerate Euclidean simplex with facets \(F_0,\ldots,F_d\). In the *stratified model*, draw independent \(X_i\), each uniformly with respect to normalized \((d-1)\)-dimensional Hausdorff measure on \(F_i\). In the *iid facet-mixture model*, draw independent \(Y_0,\ldots,Y_d\); for each draw select label \(i\) with probability \(\pi_i\ge0\), where \(\sum_{i=0}^d\pi_i=1\), and then draw uniformly from \(F_i\).

For the dimensionless volume fractions
\[
Z_{\mathrm{strat}}=\frac{\operatorname{vol}_d\operatorname{conv}(X_0,\ldots,X_d)}{\operatorname{vol}_d S},\qquad
Z_{\pi}=\frac{\operatorname{vol}_d\operatorname{conv}(Y_0,\ldots,Y_d)}{\operatorname{vol}_d S},
\]
put \(C_d=(d+1)!/((d+1)^d d^{d+1})\). Then the exact, shape-independent identities are
\[
\boxed{\ \mathbb E Z_{\mathrm{strat}}^2=C_d,\qquad
\mathbb E Z_{\pi}^2=C_d\Bigl(1-\sum_{i=0}^d\pi_i^2\Bigr).\ }
\]
The iid factor is exactly the probability that two independently selected facet labels differ. In particular,
\[
\boxed{\ \sup_{\pi}\mathbb E Z_{\pi}^2=\frac d{d+1}C_d,\qquad
\mathbb E Z_{\mathrm{strat}}^2\ge\frac{d+1}{d}\mathbb E Z_{\pi}^2.\ }
\]
Equality in the iid maximum and in the comparison holds precisely when every facet label has probability \(1/(d+1)\). If the iid points are distributed uniformly by surface area on the whole boundary, the label probabilities are proportional to the facet areas; equality therefore holds exactly when all facet areas are equal. Neither assertion requires a regular simplex.

## Assumptions and scope
The simplex is fixed, full dimensional and bounded; its facets have positive \((d-1)\)-area. All point draws are independent; uniform sampling on a facet means normalized Hausdorff area. The models draw precisely \(d+1\) points. Repeated facet labels are permitted only in the iid model. The formulas remain valid for probabilities equal to zero. The squared normalized volume, not mean volume or variance of volume, is the observable. All quantifiers are exact for each \(d\ge2\), not asymptotic in dimension or sample size. Because affine maps act with a constant Jacobian on each facet and on volume ratios, the laws are shape independent within each fixed probability vector.

## Proof
Write \(m=d+1\). Relative to the ordered vertices of \(S\), let \(r=(r_0,\ldots,r_{m-1})\) denote a point's barycentric coordinates. The rows of the \(m\times m\) barycentric matrix of \(m\) sampled points sum to one. Elementary affine determinant geometry gives
\[
\frac{\operatorname{vol}_d\operatorname{conv}(x_0,\ldots,x_d)}{\operatorname{vol}_d S}=|\det R|.
\]
For a uniformly sampled point on facet \(F_i\), \(r_i=0\) and the remaining \(d\) coordinates have the Dirichlet \((1,\ldots,1)\) distribution. Its second moment matrix \(A_i=\mathbb E(rr^{\mathsf T}\mid F_i)\) therefore satisfies
\[
(A_i)_{jk}=\begin{cases}
\frac{1+\mathbf1_{j=k}}{d(d+1)},&j\ne i,\ k\ne i,\\
0,&\text{otherwise}.
\end{cases}
\]
Indeed the diagonal second moments are \(2/(d(d+1))\) and the off-diagonal moments are \(1/(d(d+1))\).

Set \(c=1/(dm)\), \(T=\sum_{i=0}^{m-1}t_i\), \(t=(t_0,\ldots,t_{m-1})^{\mathsf T}\), and let \(\mathbf1\) be the all-ones column vector. Direct summation yields
\[
\sum_i t_i A_i=c\big[T(I+\mathbf1\mathbf1^{\mathsf T})-t\mathbf1^{\mathsf T}-\mathbf1t^{\mathsf T}\big]=cB.
\]
On the common orthogonal complement of \(\mathbf1\) and \(t\), \(B\) acts as \(T I\). The remaining action is
\[
B\mathbf1=m(T\mathbf1-t),\qquad Bt=(T^2-\sum_i t_i^2)\mathbf1.
\]
For linearly independent \(t,\mathbf1\), the resulting two-dimensional determinant equals \(m(T^2-\sum_i t_i^2)\). Thus, by polynomial identity and continuity also on the exceptional parameters,
\[
\boxed{\det\Big(\sum_i t_iA_i\Big)=c^m m T^{m-2}\Big(T^2-\sum_i t_i^2\Big).}\tag{1}
\]
This rank-two reduction is the critical structural step.

For independent not-necessarily-identically-distributed random row vectors \(R_i\) with second moments \(A_i\), expanding the two determinant permutations gives
\[
\mathbb E(\det R)^2=\sum_{\sigma,\tau\in\mathfrak S_m}
\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)
\prod_{i=0}^{m-1}(A_i)_{\sigma(i),\tau(i)}.
\]
Equivalently, this is the squarefree coefficient \([t_0\cdots t_{m-1}]\det(\sum_i t_iA_i)\). To see the equivalence, use the two-permutation expression for a determinant, with factor \(1/m!\), and expand every entry in the labeled matrices. Exactly \(m!\) assignments use each label once, and simultaneous permutation of the two determinant indices makes their contributions identical. In (1), the term \(T^{m-2}\sum_i t_i^2\) has no squarefree monomial, whereas \([t_0\cdots t_{m-1}]T^m=m!\). Consequently
\[
\mathbb E Z_{\mathrm{strat}}^2=c^m m\,m!=\frac{m!}{m^{m-1}d^m}=C_d.
\]

For the iid facet mixture all rows have second moment matrix \(A_{\pi}=\sum_i\pi_i A_i\). The same two-permutation identity reduces to the classical relation \(\mathbb E(\det R)^2=m!\det A_{\pi}\). Substituting \(t_i=\pi_i\) and \(T=1\) in (1) gives
\[
\mathbb E Z_{\pi}^2=m!c^m m\Big(1-\sum_i\pi_i^2\Big)=C_d\Big(1-\sum_i\pi_i^2\Big).
\]
Cauchy–Schwarz gives \(\sum_i\pi_i^2\ge 1/m\), with equality exactly for the uniform vector. This proves the unique maximizing iid law and the sharp comparison. Normalized boundary Hausdorff sampling selects a facet with probability equal to its area divided by total facet area, yielding the stated geometric equality condition.

## Verification
For \(d=2\), the exact stratified squared-volume fraction is \(1/12\) and the optimum iid value is \(1/18\). For \(d=3\), they are \(1/216\) and \(1/288\); for \(d=4\), \(3/16000\) and \(3/20000\). All satisfy the exact comparison ratio \((d+1)/d\).

The accompanying standalone \(\texttt{checker.py}\) evaluates squared determinants directly by independently expanding both determinant permutations using exact rational facet moments, for \(d=1,2,3,4\) and multiple probability vectors including degenerate mixtures. It also simulates fresh barycentric facet samples at dimensions \(2,3,4\) and compares six Monte Carlo estimates against the formulas using the measured standard error. The exact rational checks are finite corroborations of the stated all-dimensional proof; the simulation does not establish an infinite theorem.

## Relationship to prior work
Rademacher's earlier covariance-determinant treatment of iid random simplex squared volumes supplies the classical general iid identity; that identity and Dirichlet second moments are **not** claimed as new. The present result concerns a specific **facet-mixture family** and, importantly, a distinct **non-iid one-per-facet design**; it evaluates both models in every dimension and gives their exact sharp design comparison. Turchi–Wespi treat asymptotic intrinsic volumes for smooth-body boundary sampling, not this finite simplex-facet law. Reitzner–Schütt–Werner treat asymptotic expected quantities for iid samples on simple-polytope boundaries. Kunis–Reichenwallner–Reitzner calculate moments under a distinct tetrahedral sampling model involving interior points and a fixed face-center point. The identified works do not state the combined all-dimensional facet-diversity identities and optimization, but literature coverage is not exhaustive.

## Limitations
The theorem concerns second moments, not first moments, the full volume distribution, or stochastic dominance. Uniform surface-area sampling does not generally assign equal probabilities to faces of an arbitrary simplex. The optimal mixture is a design statement, not a classification of equal-facet-area simplices. The simple covariance determinant lemma is established prior work. An equivalent facet-mixture calculation in unindexed or inaccessible sources cannot be excluded; independent review has not been performed.

## References
1. L. Rademacher, *On the monotonicity of the expected volume of a random simplex*, arXiv:1008.3944 (2010), especially Lemma 4 on second moments and covariance determinants. https://arxiv.org/abs/1008.3944
2. N. Turchi and F. Wespi, *Limit theorems for random polytopes with vertices on convex surfaces*, arXiv:1706.02944 (first public 9 June 2017). https://arxiv.org/abs/1706.02944
3. M. Reitzner, C. Schütt and E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first public 14 November 2019). https://arxiv.org/abs/1911.05917
4. S. Kunis, B. Reichenwallner and M. Reitzner, *Monotonicity of the Sample Range of 3-D Data: Moments of Volumes of Random Tetrahedra*, arXiv:1612.01893 (2016). https://arxiv.org/abs/1612.01893
