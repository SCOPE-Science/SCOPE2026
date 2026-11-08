# A hypergeometric all-vertex Löwner certificate for two-layer chain polytopes

## Finding
For every integer \(m\ge1\), let \(A_m\) denote an \(m\)-element antichain, and let \(P_m=\mathcal C(A_m\oplus A_m)\subset\mathbb R^{2m}\) be the chain polytope of their ordinal sum in its standard coordinate Euclidean realization. Equivalently,
\[
P_m=\operatorname{conv}\bigl(([0,1]^m\times\{0\})\cup(\{0\}\times[0,1]^m)\bigr)
=\{(x,y):x_i,y_j\ge0,\ x_i+y_j\le1\ \forall i,j\}.
\]
This is also the stable-set polytope of the balanced complete bipartite graph \(K_{m,m}\).

Write \(\mathbf1=\mathbf1_{2m}\), \(s=(\mathbf1_m,-\mathbf1_m)\), and \(J_m=\mathbf1_m\mathbf1_m^{\mathsf T}\). Define orthogonal projectors
\[
P_c=\operatorname{diag}(I_m-J_m/m,I_m-J_m/m),\qquad
P_+=\frac{\mathbf1\mathbf1^{\mathsf T}}{2m},\qquad
P_-=\frac{ss^{\mathsf T}}{2m}.
\]
They sum to the identity, and the first has rank \(2m-2\) (zero when \(m=1\)). Put
\[
\begin{aligned}
t&=\frac{m+1}{2(2m+1)},\\
q_c&=\frac{m(m+1)}{2(2m+1)},\\
q_+&=\frac{m(m+1)^2}{2(2m+1)^2},\\
q_-&=\frac{m(m+1)^2}{2(2m+1)},\\
Q&=q_cP_c+q_+P_++q_-P_-.
\end{aligned}
\]
**The unique minimum-volume ellipsoid containing \(P_m\)** is
\[
\boxed{\mathcal E_m=\{z\in\mathbb R^{2m}:(z-t\mathbf1)^{\mathsf T}Q^{-1}(z-t\mathbf1)\le1\}.}
\]
Its squared semiaxes are \(q_c\) (multiplicity \(2m-2\)), \(q_+\), and \(q_-\). In particular, its squared major-to-minor semiaxis ratio is exactly \(2m+1\) and diverges with the layer size. **Every vertex is a contact vertex**, so the complete contact set consists of all \(2^{m+1}-1\) vertices. The exact volume is
\[
\boxed{\operatorname{vol}_{2m}(\mathcal E_m)
=\frac{\pi^m m^m(m+1)^{m+1}}{m!\,2^m(2m+1)^{m+1/2}}.}
\]
The order polytope of \(A_m\oplus A_m\) is carried onto \(P_m\) by the Euclidean reflection \((x,y)\mapsto(x,\mathbf1_m-y)\); therefore the reflected formula also gives its unique Löwner ellipsoid.

## Assumptions and scope
All ellipsoids and volumes are taken in full \(2m\)-dimensional *standard Euclidean coordinate space*, not in a differently scaled affine model. The family comprises the complete two-rank posets with two equally sized antichains, one below the other. The parameter \(m\) is any positive integer, including \(m=1\) (a triangle); at \(m=1\), the contrast projector has zero rank. The shape convention is \((z-c)^{\mathsf T}Q^{-1}(z-c)\le1\), so the eigenvalues of \(Q\), not their reciprocals, are squared semiaxes. No assertion is made for unequal ranks, three or more ranks, or arbitrary posets.

## Proof
**1. Every vertex and a positive design.** A chain-polytope vertex is the indicator of an antichain. Every antichain of the complete two-rank poset lies entirely in one rank. Thus the vertex set consists of the origin and the nonzero zero-one vectors supported on exactly one coordinate block, and has cardinality \(2^{m+1}-1\).

Let \(N=\binom{2m+1}{m}\). Choose the first or second coordinate block with probability \(1/2\); within the chosen block, select a subset \(S\subseteq[m]\) with probability
\[
\mathbb P(S)=\frac{\binom{m+1}{|S|}}{N}.
\]
Vandermonde's identity \(\sum_{k=0}^m\binom mk\binom{m+1}k=N\) proves normalization. All \(2^{m+1}-1\) geometrically distinct vertices receive strictly positive weight (the origin is counted through both blocks). The random subset size has the hypergeometric law with population \(2m+1\), marked population \(m+1\), and sample size \(m\), giving
\[
\mathbb P(i\in S)=\frac{m+1}{2m+1},\qquad
\mathbb P(i,j\in S)=\frac{m+1}{2(2m+1)}\quad(i\ne j).
\]
Let \(X\) be the resulting random vertex in \(\mathbb R^{2m}\). Its mean is \(\mathbb EX=t\mathbf1\). Directly from the displayed one- and two-coordinate probabilities, its covariance matrix has diagonal entries \(t-t^2\), entries within a block but off the diagonal \(t/2-t^2\), and entries between different blocks \(-t^2\). Diagonalization in the mutually orthogonal spaces \(P_c\), \(P_+\), \(P_-\) yields
\[
\boxed{\operatorname{Cov}(X)=\frac1{2m}(q_cP_c+q_+P_++q_-P_-)=\frac Q{2m}.}
\]
All three coefficients of \(Q\) are positive, including when the first projector has rank zero.

**2. Exact containment and full vertex contact.** A vertex from the first block is \(v=(\mathbf1_S,0)\) with \(|S|=k\), \(0\le k\le m\). Its squared components after subtracting \(t\mathbf1\) along the three projectors are, respectively,
\[
\|P_c(v-t\mathbf1)\|^2=k-\frac{k^2}{m},\quad
\|P_+(v-t\mathbf1)\|^2=\frac{(k-2mt)^2}{2m},\quad
\|P_-(v-t\mathbf1)\|^2=\frac{k^2}{2m}.
\]
Substituting the three eigenvalues gives the **exact identity, for every integer \(0\le k\le m\)**,
\[
\boxed{\frac{k-k^2/m}{q_c}+\frac{(k-2mt)^2}{2m q_+}+\frac{k^2}{2m q_-}=1.}
\]
When \(m=1\), the first summand is zero for all admitted \(k\). Swapping the blocks preserves the same expression. Thus *every vertex* lies on the boundary of \(\mathcal E_m\); since the ellipsoid is convex and contains the entire vertex set, \(P_m\subseteq\mathcal E_m\). Every vertex is genuinely a contact point, not merely a facet midpoint or a numerical approximation.

**3. Global minimal-volume and uniqueness, without a symmetry assumption.** Let any full-dimensional ellipsoid containing \(P_m\) have center \(a\in\mathbb R^{2m}\) and positive-definite shape \(S\), so that \((z-a)^{\mathsf T}S^{-1}(z-a)\le1\) for every vertex. Taking the expectation with respect to the *positive vertex design* above yields
\[
\operatorname{tr}(S^{-1}Q)/(2m)
+(a-t\mathbf1)^{\mathsf T}S^{-1}(a-t\mathbf1)\le1.
\]
Writing \(d=2m\), the arithmetic–geometric mean inequality for eigenvalues of the positive-definite matrix \(S^{-1/2}QS^{-1/2}\) gives
\[
\left(\frac{\det Q}{\det S}\right)^{1/d}
\le\frac1d\operatorname{tr}(S^{-1}Q)\le1.
\]
Therefore \(\det S\ge\det Q\), proving that no enclosing ellipsoid, even nonsymmetric or with a displaced center, has smaller volume. Equality forces \(a=t\mathbf1\) and all eigenvalues of \(S^{-1/2}QS^{-1/2}\) equal to one, hence \(S=Q\). The optimal ellipsoid is therefore unique.

**4. Spectrum, volume, and order-polytope reflection.** Because \(P_c,P_+,P_-\) are pairwise orthogonal projectors summing to \(I_{2m}\), the squared semiaxis multiplicities are the projector ranks. For \(m\ge1\), \(q_-\ge q_c\ge q_+\) where the zero-multiplicity contrast term is irrelevant at \(m=1\); indeed \(q_-/q_+=2m+1\). Since \(\det Q=q_c^{2m-2}q_+q_-\) and the unit ball in \(2m\) dimensions has volume \(\pi^m/m!\), the volume formula follows. Reflection of the second rank turns all order inequalities into chain inequalities, giving the asserted Euclidean isometry.

## Verification
The self-contained standard-library program `check_balanced_chain_lowner.py` forms the complete vertex set for each \(1\le m\le8\), assigns exact rational hypergeometric design weights, and verifies their normalization, exact mean and covariance, positive-definiteness eigenvalues, every vertex-contact equation, and the shape condition number. It checks \(3,7,15,31,63,127,255,511\) vertices respectively, using only exact rational arithmetic. Execute `python3 check_balanced_chain_lowner.py`. It prints `BALANCED_CHAIN_LOEWNER_EXACT_CHECKS_PASSED`. This is finite corroboration; the four universal proof steps above establish the result for every positive integer.

## Relationship to prior work
Stanley established order and chain polytopes and their antichain vertices. Ahmad–Fourier–Joswig (arXiv:2309.01626, first posted 2023-09-04) study the maximal ranked-poset class containing the present two-level family and establish face-vector comparisons. Freij-Hollanti–Lundström (arXiv:2312.13890, first posted 2023-12-21) make the orthogonal-subdirect-sum presentation explicit for chain polytopes of ordinal sums and investigate face enumeration. Their results supply the underlying combinatorial model but do not evaluate its enclosing ellipsoid. An existing result on the **John ellipsoid** of the balanced two-layer order polytope determines the *largest contained* ellipsoid and its facet tangencies; another treats the unbalanced family. Neither assertion determines the *minimum-volume containing* ellipsoid established here, and polarity would require the John ellipsoid of the specifically centered polar, not of the original polytope. The contribution is the exact outer ellipsoid, an all-vertex hypergeometric contact design, and its unbounded anisotropy.

## Limitations
This result is restricted to two equal-size layers and their standard Euclidean realization. It does not classify unequal-size subdirect sums, general posets, or affine variants, and no claimed global priority follows merely from unsuccessful searches. The literature could contain an equivalent evaluation under enclosing-ellipsoid, D-optimal design, free-sum, or stable-set terminology. The finite exact checks alone do not certify the infinite theorem: the global argument depends on the explicit positive weights, all-vertex quadratic identity, and determinant inequality.

## References
1. Richard P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23, DOI: 10.1007/BF02187680.
2. Ibrahim Ahmad, Ghislain Fourier, Michael Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626 (first version 2023-09-04), https://arxiv.org/abs/2309.01626.
3. Ragnar Freij-Hollanti, Teemu Lundström, *f-vector inequalities for order and chain polytopes*, arXiv:2312.13890 (first version 2023-12-21), https://arxiv.org/abs/2312.13890.
4. Takayuki Hibi, Nan Li, *Unimodular equivalence of order and chain polytopes*, Mathematica Scandinavica 118 (2016), 5–12, DOI: 10.7146/math.scand.a-23291.
5. Areesh Mittal, Grani A. Hanasusanto, *Finding minimum volume circumscribing ellipsoids using generalized copositive programming*, Operations Research 70 (2022), 2867–2882, arXiv:1807.07507 (first version 2018-07-19).
