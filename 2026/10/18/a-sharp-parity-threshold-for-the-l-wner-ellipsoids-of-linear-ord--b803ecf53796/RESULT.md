# A sharp parity threshold for the Löwner ellipsoids of linear-ordering polytopes

## Finding
For every integer \(n\ge4\), let \(d=\binom n2\), and index \(\mathbb R^d\) by ordered pairs \((i,j)\) with \(1\le i<j\le n\). For each permutation \(\pi\) of \([n]\), define its pairwise-ranking sign vector by
\[
(v_\pi)_{ij}=\begin{cases}1,&\pi(i)<\pi(j),\\-1,&\pi(i)>\pi(j).\end{cases}
\]
Let \(P_n=\operatorname{conv}\{v_\pi:\pi\in S_n\}\) be the full linear-ordering polytope in sign coordinates, and \(Q_n=\operatorname{conv}\{v_\pi:\pi\in A_n\}\) the convex hull restricted to even permutations. Both have full dimension \(d\). The unique minimum-volume containing ellipsoids are, respectively,
\[
\mathcal L(P_n)=\{x:x^\mathsf T T_n^{-1}x\le d\},\qquad
\mathcal L(Q_n)=\{x:x^\mathsf T C_n^{-1}x\le d\},
\]
where the explicit positive-definite matrices \(T_n,C_n\) are defined below. Every generating vertex, and no other polytope point, lies on the corresponding ellipsoid boundary.

Define the oriented vertex-edge incidence matrix \(B\in\mathbb R^{n\times d}\) by putting \(e_i-e_j\) in column \((i,j)\). Then
\[
T_n=\frac{I+B^\mathsf TB}{3},\qquad
C_n=\begin{cases}T_n+\frac13 H_4,&n=4,\\T_n+\frac1{15}H_5,&n=5,\\T_n,&n\ge6.\end{cases}
\]
The symmetric matrices \(H_4,H_5\), indexed by pairs of edges \(e=(i,j),f=(k,\ell)\) with \(i<j\), \(k<\ell\), have zero entry if the edges share a vertex. For four distinct endpoints, let \(\epsilon(e,f)\in\{\pm1\}\) be the sign of the four-term sequence \((i,j,k,\ell)\) relative to the increasing ordering of those four labels. Then \((H_4)_{e,f}=\epsilon(e,f)\); for \(n=5\), if \(h\) is the unique omitted label in \([5]\), put \((H_5)_{e,f}=(-1)^{h-1}\epsilon(e,f)\). These formulas specify all matrix entries.

The squared-semiaxis spectra of \(\mathcal L(Q_n)\), namely \(d\) times the eigenvalues of \(C_n\), are obtained from the following complete eigenvalue lists for \(C_n\):

* \(n=4\): \(1+\sqrt5/3\) and \(1-\sqrt5/3\), each of multiplicity \(3\).
* \(n=5\): \(2\) of multiplicity \(4\), and \((5+\sqrt5)/15\), \((5-\sqrt5)/15\), each of multiplicity \(3\).
* \(n\ge6\): \((n+1)/3\) of multiplicity \(n-1\), and \(1/3\) of multiplicity \((n-1)(n-2)/2\).

Consequently, the **exact ratio of minimum enclosing ellipsoid volumes** is
\[
\boxed{\frac{\operatorname{Vol}_d\mathcal L(Q_n)}{\operatorname{Vol}_d\mathcal L(P_n)}=
\begin{cases}\displaystyle\frac8{5\sqrt5},&n=4,5,\\1,&n\ge6.\end{cases}}
\]
In particular, removing half the ordering vertices changes the optimal ellipsoid by the same nontrivial constant volume factor in dimensions \(6\) and \(10\), but leaves the ellipsoid exactly unchanged from \(n=6\) onward, despite \(Q_n\subsetneq P_n\). The **Euclidean smallest enclosing ball**, by contrast, is already identical for both polytopes for every \(n\ge4\): it is the ball of radius \(\sqrt d\) centered at the origin. For \(n=4\), the ratio of longest to shortest semiaxis of \(\mathcal L(Q_n)\) is \((3+\sqrt5)/2\).

## Assumptions and scope
All volumes and ellipsoids use the ordinary Euclidean metric on the \(d\) pairwise-comparison coordinates. The permutation \(\pi(i)\) represents the rank of label \(i\); its parity is the parity of the rank-assignment permutation. The result concerns **even linear-ordering polytopes in pairwise-comparison coordinates**, not polytopes of even permutation matrices. The sign-coordinate embedding is an isometric dilation by factor two of the customary zero-one linear-ordering embedding \(y=(x+\mathbf1)/2\). In zero-one coordinates the centers are \(\mathbf1/2\) and the ellipsoid shape matrices are \(dT_n/4\) and \(dC_n/4\); the volume ratio is unchanged.

The theorem intentionally begins at \(n=4\). For \(n=3\), the even-permutation hull has affine dimension \(2\), not the full ambient dimension \(3\), and does not have the stated full-dimensional ellipsoid. All formulas for \(n=4,5\) are exact finite identities; the \(n\ge6\) formulas hold for every integer in that range.

## Proof
**1. Uniform permutation covariance.** Let \(V=v_\pi\) for a uniformly random permutation in \(S_n\). Each coordinate has mean zero and variance one. For two distinct edges sharing a label, the covariance of their signs equals \(\frac13\) or \(-\frac13\), according to the agreement of the oriented incidence signs: this is the direct enumeration of the six relative orders of three labels. For disjoint edges the two comparison signs are independent, and their covariance is zero. Since \((B^\mathsf TB)_{e,e}=2\), and for distinct edges its entry is the corresponding incidence inner product, \(\mathbb E(VV^\mathsf T)=T_n=(I+B^\mathsf TB)/3\). The complete-graph incidence identity \(BB^\mathsf T=nI-\mathbf1\mathbf1^\mathsf T\) shows that the eigenvalues of \(T_n\) are \((n+1)/3\) on the \((n-1)\)-dimensional gradient subspace \(\operatorname{im}B^\mathsf T\), and \(1/3\) on the \((n-1)(n-2)/2\)-dimensional circulation subspace \(\ker B\).

**2. Parity eliminates all effects involving at most four labels once \(n\ge6\).** For any statistic \(F\) depending only on the relative order of at most four specified labels, exchange two of the remaining labels. This preserves \(F\) and reverses the permutation parity. Thus its mean under uniform even permutations equals its unrestricted mean. In particular, all first and second moments of the pairwise comparison signs coincide when \(n\ge6\), so \(C_n=T_n\). For \(n=4,5\), two unused labels suffice to cancel the parity correction for one comparison, so the even-permutation mean is also zero.

**3. Exact low-dimensional parity corrections.** Let \(\chi(\pi)\in\{\pm1\}\) be its permutation sign. For any \(F\),
\[
\mathbb E_{\pi\in A_n}F=\mathbb E_{\pi\in S_n}F+\mathbb E_{\pi\in S_n}(\chi(\pi)F).
\]
For \(n=4\), direct enumeration of the relative four-label orders gives the parity correction \(\epsilon(e,f)/3\) for disjoint comparison pairs and zero for overlapping comparison pairs. For \(n=5\), insertion of the fifth label into the four-label order gives the factor \((-1)^{h-1}/5\) relative to the four-label correction, where \(h\) is the omitted label. The resulting covariances are exactly \(T_4+H_4/3\) and \(T_5+H_5/15\). These are finite calculations over \(12\) and \(60\) permutations, respectively; the standalone exact checker constructs both covariances directly and verifies every entry.

**4. Spectra of the parity corrections.** Write \(P=B^\mathsf TB/n\), the orthogonal projection onto the gradient space, and \(Q=I-P\). For \(n=4\), the displayed signed-disjoint-edge matrix satisfies \(H_4^2=I\), \(PH_4P=0\), and \(QH_4Q=0\). Hence \(H_4\) exchanges the three-dimensional gradient and circulation spaces by an isometry. In mutually paired orthonormal bases, \(C_4\) is three copies of the matrix
\[
\begin{pmatrix}5/3&1/3\\1/3&1/3\end{pmatrix},
\]
whose eigenvalues are \(1\pm\sqrt5/3\). For \(n=5\), direct matrix multiplication yields \(H_5P=PH_5=0\), \(H_5^2=5Q\), and \(\operatorname{tr}H_5=0\). The operator \(H_5\) therefore has eigenvalue zero four times and \(\pm\sqrt5\) each three times on the six-dimensional circulation space. Since \(T_5=2P+Q/3\), the stated spectrum follows. The checker verifies all these rational matrix identities independently from the entry formulas. Every listed eigenvalue is positive. This proves full-dimensionality of the even hulls and establishes the asserted spectra.

**5. Covariance ellipsoids are exactly optimal.** The alternating group \(A_n\) acts transitively on the even rank permutations by relabeling. Its action on the comparison vectors is by orthogonal signed coordinate permutations. Consequently \(C_n\), their uniform covariance, is invariant under this action, and every \(v_\pi\) in the orbit has the same value of \(v_\pi^\mathsf T C_n^{-1}v_\pi\). Averaging and using \(\operatorname{tr}(C_n^{-1}C_n)=d\) gives the common value \(d\). Thus the stated ellipsoid contains \(Q_n\), with every generating vertex tangent. For any other ellipsoid \(E=\{x:(x-a)^\mathsf TR^{-1}(x-a)\le1\}\) containing \(Q_n\), averaging over even vertices implies
\[
\operatorname{tr}(R^{-1}C_n)+a^\mathsf TR^{-1}a\le1.
\]
The arithmetic-geometric mean inequality on the eigenvalues of \(R^{-1/2}C_nR^{-1/2}\) gives \(\operatorname{tr}(R^{-1}C_n)\ge d(\det C_n/\det R)^{1/d}\). Thus \(\det R\ge d^d\det C_n\), with equality only for \(a=0\) and \(R=dC_n\). This proves unique minimum volume without restricting competing ellipsoid orientations or centers. Replacing \(A_n\) with \(S_n\) gives the full ordering-polytope ellipsoid based on \(T_n\). Since ellipsoids are strictly convex and all generating vertices touch their boundaries, no nonvertex convex combination can be a contact point.

**6. Sharp volume ratio.** The ratio is \(\sqrt{\det C_n/\det T_n}\). For \(n=4\), the determinant quotient is \((4/9)^3/((5/3)^3(1/3)^3)=64/125\). For \(n=5\), the quotient is \(2^4(4/45)^3/[2^4(1/3)^6]=64/125\). For \(n\ge6\) it is one. The minimum enclosing ball claim follows because every sign vector has squared Euclidean norm \(d\), while the even or full vertex mean is zero; any containing ball has radius at least \(\sqrt d\), with equality uniquely at the origin. For the four-label case, the semiaxis ratio simplifies to \(\sqrt{(1+\sqrt5/3)/(1-\sqrt5/3)}=(3+\sqrt5)/2\).

## Verification
Run `python3 CHECKER.py` with Python and SymPy. The program exhaustively enumerates the full and even permutations for \(n=4,5,6\), constructs every covariance entry over exact rational arithmetic, verifies the parity-correction matrices and their projection identities, checks positive determinants, proves the expected Mahalanobis boundary equality at every even permutation vertex, and verifies the exact squared volume ratios \(64/125,64/125,1\). The observed output is:

```
n=4: even_vertices=12 full_vertices=24 dim=6; covariance determinant ratio=64/125; contact equality on all vertices
n=5: even_vertices=60 full_vertices=120 dim=10; covariance determinant ratio=64/125; contact equality on all vertices
n=6: even_vertices=360 full_vertices=720 dim=15; covariance determinant ratio=1; contact equality on all vertices
PASS: all exact covariance, spectrum, normalization, and volume-ratio checks
```

The exact finite calculations verify the exceptional dimensions. For all \(n\ge6\), the parity-pairing and covariance/AM–GM arguments provide the proof; enumeration is not extrapolated into an infinite theorem.

## Relationship to prior work
The 2023 first-public preprint by Gartsman and Linial determines the extremal ellipsoids of the **metric polytope** and develops contact-certificate methods for its cut-metric vertices. The present pairwise-ordering and parity-restricted polytopes are different convex bodies and are not reduced to metric polytopes by the cited theorem. Katthän's *The Linear Ordering Polytope via Representations* establishes the decomposition of the full linear-ordering polytope into potential and circulation components and its projection structure; those known components are used in the covariance calculation, not claimed as novel. The earlier Cunningham–Wang paper entitled *On the even permutation polytope* concerns the convex hull of **even permutation matrices** in matrix coordinates, not the convex hull of pairwise-ranking comparison vectors in this theorem. The cited results provide no Euclidean isometry or covariance theorem transferring their conclusions to the pairwise-comparison embedding used here.

The new statement is the exact ellipsoid and volume classification of the **even-rank-restricted pairwise-ordering hull**, including the four-label parity cancellation threshold and the identical exceptional volume deficit in two dimensions. Search results and inspected primary material did not disclose a statement implying this classification. This is a qualified comparison, not a proof that no earlier formulation exists.

## Limitations
The result gives containing ellipsoids, not maximum-volume inscribed John ellipsoids, facet descriptions, or intrinsic uniform sampling laws. The full-volume ratio depends on the stated pairwise-comparison embedding, not on the distinct permutation-matrix embedding. The first motivating public source was arXiv:2305.02113, submitted 2023-04-19; earlier sources are acknowledged as background. The covariance identities for \(n=4,5\) are finite exact certificates, with an independent human audit of the complete argument not yet performed. An unindexed equivalence under rank-data covariance or alternating-group orbitope terminology remains a bibliographic risk.

## References
1. R. Gartsman and N. Linial, *On the Löwner-John Ellipsoids of the Metric Polytope*, arXiv:2305.02113, first posted 2023-04-19; Theorem 1.2 and Sect. 2 (different polytope and contact method). https://arxiv.org/abs/2305.02113
2. L. Katthän, *The Linear Ordering Polytope via Representations*, arXiv:1109.5040, 2011; Theorem 1 and Sect. 3 (potential/circulation decomposition, full polytope). https://arxiv.org/abs/1109.5040
3. W. H. Cunningham and Y. Wang, *On the even permutation polytope*, Linear Algebra and its Applications 389 (2004), 269–281; DOI 10.1016/j.laa.2004.03.016 (distinct permutation-matrix polytope).
4. F. John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant on His 60th Birthday* (1948); standard extremal-ellipsoid optimality criterion.
