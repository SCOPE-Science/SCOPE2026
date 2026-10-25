# A sharp two-unit eigenspace transition in bipartite stable-set polytope inertia

## Finding
For integers \(p,q\ge2\), let \(d=p+q\), and consider the complete-bipartite stable-set polytope
\[
P_{p,q}=\{(x,y)\in\mathbb R_+^p\times\mathbb R_+^q:x_i+y_j\le1\text{ for all }i,j\}.
\]
Let \(Z\) be uniform with respect to \(d\)-dimensional Euclidean volume on \(P_{p,q}\), and let \(\Sigma=\operatorname{Cov}(Z)\). Put \(D=(d+1)^2(d+2)\) and
\[
\begin{split}
t_p&=\frac{(p+1)(p+2)}{12(d+1)(d+2)},\qquad
t_q=\frac{(q+1)(q+2)}{12(d+1)(d+2)},\\
u_p&=\frac{(p+1)(p^2+4pq+3p+2q+2)}{12D},\\
u_q&=\frac{(q+1)(q^2+4pq+3q+2p+2)}{12D},\\
h&=\frac{(p+1)(q+1)}{4D}.
\end{split}
\]
The **complete covariance spectrum** consists of \(t_p\) with multiplicity \(p-1\), \(t_q\) with multiplicity \(q-1\), and the two eigenvalues
\[
\lambda_\pm=\frac{u_p+u_q\pm\sqrt{(u_p-u_q)^2+4pqh^2}}2
\]
of the longitudinal block
\[
B=\begin{pmatrix}u_p&-\sqrt{pq}\,h\\-\sqrt{pq}\,h&u_q\end{pmatrix}.
\]
The largest eigenvalue is always \(\lambda_+\). The **smallest eigenvalue undergoes a sharp, strict transition**:
\[
\boxed{\lambda_{\min}(\Sigma)=
\begin{cases}
\lambda_-,&|p-q|\le1,\\
\min(t_p,t_q),&|p-q|\ge2.
\end{cases}}
\]
In particular, there are **no integer equality cases** at the transition. For balanced blocks \(p=q=r\ge2\), the global maximum eigenvalue is *exactly* \(1/12\) in every dimension, and the condition number is
\[
\boxed{\kappa(\Sigma)=\frac{(2r+1)^2}{r^2+r+1}\longrightarrow4.}
\]
Moreover, writing the Euclidean isotropic constant as
\[
L(P_{p,q})=\frac{(\det\Sigma)^{1/(2d)}}{\operatorname{Vol}_d(P_{p,q})^{1/d}},
\]
we have, **uniformly over all integer pairs** \(p,q\ge2\) with \(d=p+q\to\infty\),
\[
\boxed{L(P_{p,q})\longrightarrow\frac1{\sqrt{12}}.}
\]
More quantitatively, \(\log(12L(P_{p,q})^2)=O(\log(d+1)/d)\), with an absolute implied constant, including very unbalanced sequences.

## Assumptions and scope
The body is full dimensional and is the convex hull of the indicator vectors of stable sets of the graph \(K_{p,q}\); since the graph is bipartite, the edge inequalities above are exact. It is also the chain polytope of the complete height-two poset. Reflecting the second block by \(y\mapsto\mathbf1_q-y\) gives the corresponding order polytope by a Euclidean isometry, so all intrinsic metric statements transfer. The covariance concerns the **uniform volume measure on the whole polytope**, not the distribution uniform on its vertices, the John ellipsoid, or a discrete walk on its skeleton. Zero-sum block subspaces are defined with respect to the standard Euclidean coordinate inner product. Every theorem here assumes \(p,q\ge2\); the one-element-block degeneracies are not included.

## Proof
**1. Equal-volume simplicial chambers.** Choose a permutation of the first block and independently of the second. Require the entries in each permuted block to be nondecreasing. Write the successive coordinate differences of the first sorted block as \(a_1,\ldots,a_p\), of the second as \(b_1,\ldots,b_q\), and put \(s=1-\sum_i a_i-\sum_j b_j\). Each chamber is the standard \(d\)-simplex in the \(d+1\) nonnegative gap variables summing to one: the coordinate change is triangular with absolute Jacobian one. There are \(p!q!\) chambers, meeting only on null boundaries, hence
\[
\operatorname{Vol}_d(P_{p,q})=\frac{p!q!}{d!}.
\]
Inside each chamber, the vector of gaps plus slack is exactly \(\operatorname{Dirichlet}(1,\ldots,1)\). This also proves that uniform volume is obtained by choosing two independent uniform orderings and then a uniform point of the standard \(d\)-simplex.

**2. Moments.** Let \(A=\max_i x_i\) and \(C=\max_j y_j\). Aggregating the Dirichlet gaps gives
\[
(A,C,1-A-C)\sim\operatorname{Dirichlet}(p,q,1).
\]
Conditioned on \(A,C\), the maximizer in each block is uniformly distributed over the block, one coordinate equals the maximum, and the remaining coordinates are independent uniform variables on the interval from zero to that maximum. The two blocks are conditionally independent. Therefore for distinct indices within the first block, and analogously within the second,
\[
\begin{aligned}
\mathbb E x_i&=\frac{p+1}{2(d+1)},
&\mathbb E x_i^2&=\frac{(p+1)(p+2)}{3(d+1)(d+2)},\\
\mathbb E x_ix_{i'}&=\frac{(p+1)(p+2)}{4(d+1)(d+2)},
&\mathbb E x_iy_j&=\frac{(p+1)(q+1)}{4(d+1)(d+2)}.
\end{aligned}
\]
The second-block mean is \((q+1)/(2(d+1))\). Subtracting products of means gives a common cross-block covariance of \(-h\). Within a block, the covariance matrix has a constant diagonal and a constant off-diagonal entry. It follows that the \((p-1)\)-dimensional first-block zero-sum subspace is a scalar eigenspace with eigenvalue \(t_p\); the analogous second-block zero-sum subspace has eigenvalue \(t_q\). In the remaining orthonormal basis \((\mathbf1_p/\sqrt p,0)\), \((0,\mathbf1_q/\sqrt q)\), the covariance restricts to \(B\), giving the full displayed spectrum.

**3. Strict smallest-eigenmode transition.** Direct simplification gives
\[
\begin{gathered}
u_p-t_p=\frac{pq(p+1)}{4D}>0,\qquad
u_q-t_q=\frac{pq(q+1)}{4D}>0,\\
\det B=\frac{(p+1)(q+1)(2pq+p+q+2)}{72(d+1)^2(d+2)^2}>0.
\end{gathered}
\]
Thus both longitudinal eigenvalues are positive; the larger eigenvalue \(\lambda_+\) exceeds \(u_p\) and \(u_q\), hence exceeds both transverse eigenvalues. By symmetry suppose \(p\ge q\), so the smallest transverse eigenvalue is \(t_q\). Both diagonals of \(B-t_qI_2\) are positive, while an exact factorization yields
\[
\boxed{\det(B-t_qI_2)=
\frac{pq(q+1)(p^2-q^2-3q-3)}{48(d+1)^3(d+2)^2}.}
\]
For \(p=q\), the final factor is \(-3q-3<0\); for \(p=q+1\), it is \(-q-2<0\). For \(p=q+2\), it is \(q+1>0\), and it increases strictly with \(p\). Therefore \(\lambda_-<t_q\) if and only if \(p-q\le1\), whereas \(\lambda_->t_q\) if and only if \(p-q\ge2\). No determinant vanishes for integers in the stated domain. This proves the complete eigenspace transition without a numerical eigenvalue comparison.

**4. Balanced rigidity.** When \(p=q=r\), the longitudinal eigenvectors are the symmetric and antisymmetric normalized block-constant directions. Substituting into the block matrix gives
\[
\lambda_+=u_r+rh=\frac1{12},\qquad
\lambda_-=u_r-rh=\frac{r^2+r+1}{12(2r+1)^2}.
\]
Since the balanced case lies on the \(\lambda_-\) side of the preceding strict comparison, the ratio of largest to smallest is exactly \((2r+1)^2/(r^2+r+1)\), tending to \(4\).

**5. Affine-invariant limit.** From the volume and spectral formulas,
\[
\det\Sigma=t_p^{p-1}t_q^{q-1}\,
\frac{(p+1)(q+1)(2pq+p+q+2)}{72(d+1)^2(d+2)^2}.
\]
Uniformly for integers \(p,q\ge2\),
\[
\log t_p=2\log(p/d)-\log12+O(1/p+1/d),
\]
and likewise for \(t_q\); also \(\log\det B=O(\log(d+1))\). A uniform factorial estimate \(\log(m!)=m\log m-m+O(\log(m+1))\) gives
\[
\log\frac{d!}{p!q!}
=-p\log(p/d)-q\log(q/d)+O(\log(d+1)).
\]
Insert these into \(\log L^2=\frac1d\log\det\Sigma+\frac2d\log(d!/(p!q!))\). The entropy terms cancel, leaving \(-\log12+O(\log(d+1)/d)\), proving the uniform convergence, even when one block remains of fixed size.

## Verification
The accompanying standalone `verify.py` independently integrates the centroid and every covariance-matrix entry over each of the \(p!q!\) explicit simplex chambers, using exact rational barycentric moments, for the nine pairs \(2\le p,q\le4\). Its separate exact-arithmetic checks test the two determinant identities, the strict sign transition for all pairs \(2\le p,q\le50\), and the balanced eigenvalue identity. The checker needs only the Python standard library. Run `python verify.py` in the directory containing this file. All-dimensional validity follows from the chamber argument and algebra above, **not** from the finite test range.

## Relationship to prior work
Aliniaeifard–Benedetti–Bergeron–Li–Saliola study the stable-set-polytope construction and its one-skeleton; Hamano–Hibi–Ohsugi study fractional stable-set polytopes and their Ehrhart series, observing the equality of integral and fractional stable-set polytopes for bipartite graphs. Ahmad–Fourier–Joswig develop the face structure of two-level order and chain polytopes. Earlier full classifications of the John ellipsoids for balanced and unbalanced complete two-level order polytopes concern **maximum-volume inscribed ellipsoids**, not the centroid or covariance of a uniform-volume distribution. A prior signed-chain-polytope volume calculation concerns a distinct signed object; this unsigned positive sector uses related elementary integration but is not a consequence of the signed object's reported full-body covariance. Neither the baseline volume, the general simplex-Dirichlet integration method, nor the known inscribed-ellipsoid formulas are claimed as new. The assessed result is the **exact finite covariance-mode transition at block imbalance two**, its balanced eigenvalue rigidity, and the **uniform** isotropic limit. Search did not uncover a stronger statement implying that combination; see bibliographic uncertainty below.

## Limitations
The theorem is for complete bipartite stable-set polytopes with \(p,q\ge2\), not general bipartite graphs or general graded posets. The existence of a combinatorial chamber triangulation does not imply the covariance mode transition without the moment and determinant computation. The asymptotic constant is shown uniformly but no higher-order expansion is claimed. Literature searches and inspected sources cannot establish worldwide priority; equivalent probability calculations may occur under two-level order-polytope, bipartite chain-polytope, or conditional order-statistics terminology. Independent verification by a distinct mathematical auditor has not been performed.

## References
1. F. Aliniaeifard, C. Benedetti, N. Bergeron, S. X. Li, F. Saliola, *Stable set polytopes and their 1-skeleta*, arXiv:1804.00360v1, first posted 2018-04-02, https://arxiv.org/abs/1804.00360.
2. G. Hamano, T. Hibi, H. Ohsugi, *Ehrhart series of fractional stable set polytopes of finite graphs*, arXiv:1603.09613v1, first posted 2016-03-31, https://arxiv.org/abs/1603.09613.
3. I. Ahmad, G. Fourier, M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626v1, first posted 2023-09-04, https://arxiv.org/abs/2309.01626.
4. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry 1 (1986), 9–23.
5. *Exact John ellipsoid of unbalanced two-layer chain and order polytopes*, published research record c200d8f4f023, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-john-ellipsoid-of-unbalanced-two-layer-chain-and-order-pol--c200d8f4f023.
6. *Exact John ellipsoid of balanced two-layer order polytopes*, published research record 8659155ecca7, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-john-ellipsoid-of-balanced-two-layer-order-polytopes--8659155ecca7.
