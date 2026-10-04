# Full-space conjugate phase retrieval from difference-plus-mean permutation orbits

## Finding

Let \(n\ge 4\), let \(\Gamma\le S_n\) be doubly transitive, choose distinct \(k_0,l_0\), and put \(\psi_1=\delta_{k_0}-\delta_{l_0}+n^{-1/2}\mathbf 1\). Then the permutation orbit \(\Pi(\Gamma)\psi_1\) does conjugate phase retrieval on all of \(\mathbb C^n\): if two vectors have equal magnitudes against every orbit vector, then one is a unimodular scalar multiple of the other or of its coordinatewise complex conjugate. The threshold is sharp for this generator in the sense that Bartusel--Führ--Oussa exhibit failure at \(n=3\).

## Assumptions and scope

Use the standard Hermitian inner product linear in its first argument. Let \(\mathbf e=n^{-1/2}\mathbf 1\). Write
\[
f=y+a\mathbf e,\qquad g=z+b\mathbf e,
\]
with \(y,z\perp\mathbf 1\). Double transitivity means that the orbit of the ordered pair \((k_0,l_0)\) contains every ordered pair \((i,j)\) with \(i\ne j\). Hence equality of all orbit magnitudes is equivalent to
\[
|y_i-y_j+a|=|z_i-z_j+b|\qquad(i\ne j).
\]
The result concerns this specific difference-plus-mean generator and arbitrary doubly transitive permutation groups. It does not assert ordinary phase retrieval, stability estimates, or a classification of other generators.

## Proof

Fix \(i\ne j\) and abbreviate \(u=y_i-y_j\), \(v=z_i-z_j\). Applying the measurement equality to both ordered pairs \((i,j)\) and \((j,i)\), then adding and subtracting the two squared equalities, gives
\[
|v|^2=|u|^2+c,\qquad c=|a|^2-|b|^2,
\]
and
\[
\operatorname{Re}(u\overline a)=\operatorname{Re}(v\overline b).
\]
Let \(D_y,D_z\) be the squared Euclidean distance matrices of the centered point configurations \((y_i)\) and \((z_i)\), regarded as points of \(\mathbb R^2\cong\mathbb C\). Let
\[
J=I-\frac1n\mathbf1\mathbf1^T.
\]
Classical double centering gives the real Gram matrices
\[
G_y=-\frac12 JD_yJ,\qquad G_z=-\frac12 JD_zJ.
\]
Since the preceding identity holds on every off-diagonal entry,
\[
D_z-D_y=c(\mathbf1\mathbf1^T-I),
\]
and therefore
\[
G_z-G_y=\frac c2J.
\]
Both Gram matrices are positive semidefinite of rank at most \(2\). If \(c>0\), then on \(\mathbf1^\perp\) the matrix \(G_z\) is bounded below by \((c/2)I\), so \(\operatorname{rank}G_z\ge n-1\ge3\), impossible. If \(c<0\), then because \(n-1\ge3\) while \(\operatorname{rank}G_y\le2\), there is a nonzero \(q\in\ker G_y\cap\mathbf1^\perp\); hence
\[
q^TG_zq=\frac c2\|q\|^2<0,
\]
contradicting positive semidefiniteness. Thus \(c=0\), so \(|a|=|b|\), \(D_y=D_z\), and \(G_y=G_z\).

Equality of the Gram matrices yields a real orthogonal map \(O\in O(2)\) taking every \(y_i\) to \(z_i\). Put
\[
W=\operatorname{span}_\mathbb R\{y_i-y_j:i,j\}.
\]
Because \(y\) is centered, \(W=\operatorname{span}_\mathbb R\{y_i:i\}\). The real-part identity above implies
\[
P_Wa=P_W(O^Tb).
\]
Together with \(|a|=|b|\), this lets the orthogonal extension be chosen so that \(Oa=b\): this is forced when \(\dim W=2\); when \(\dim W=1\), choose the sign on \(W^\perp\) matching the perpendicular components; when \(W=\{0\}\), choose any orthogonal map sending \(a\) to \(b\). Therefore \(g_i=O(f_i)\) for every coordinate.

Every real orthogonal map of \(\mathbb C\cong\mathbb R^2\) has one of the forms \(O(w)=\alpha w\) or \(O(w)=\alpha\overline w\), with \(|\alpha|=1\). Hence \(g=\alpha f\) or \(g=\alpha\overline f\), proving conjugate phase retrieval.

## Verification

The proof is finite-dimensional and analytic. The bundled `verify.py` supplies an independent exact finite stress test at the first new dimension \(n=4\). It enumerates all \(625\) vectors in \(\{0,1,-1,i,-i\}^4\), computes all ordered-pair measurements using Gaussian-integer arithmetic after clearing the factor \(\sqrt4\), and checks every collision against the two allowed ambiguities. It reports `VERIFY_OK n4_signals=625 signatures=99 max_collision_class=8 collision_pairs=1864`.

This computation is not used to infer the theorem for arbitrary \(n\); the universal step is the rank obstruction \(G_z-G_y=(c/2)J\) together with the orthogonal-congruence argument above.

## Relationship to prior work

Bartusel, Führ, and Oussa prove conjugate phase retrieval on the zero-sum subspace for a difference vector under a doubly transitive permutation group. Their Remark 5.3 then adds the normalized constant vector, gives a full-space counterexample in dimension \(3\), and explicitly states that it is unknown whether analogous counterexamples exist in dimensions greater than \(3\). Their following proposition proves only sign retrieval on \(\mathbb R^n\) for the same difference-plus-mean generator. The theorem here closes that stated gap: for every \(n\ge4\), no such complex counterexample exists.

Later general work on conjugate phase retrieval in Hilbert spaces develops abstract frame criteria, and later graph-based work develops different structured measurement schemes. Neither inspected statement gives the doubly transitive difference-plus-mean orbit theorem proved here.

## Limitations

The theorem is qualitative: it gives uniqueness only up to the unavoidable phase/conjugation ambiguity and no conditioning or noise-stability bound. It is specific to doubly transitive permutation actions and to the generator \(\delta_{k_0}-\delta_{l_0}+n^{-1/2}\mathbf1\). The finite verifier checks only a discrete test alphabet at \(n=4\); it is a consistency test rather than exhaustive verification over \(\mathbb C^4\).

## References

1. D. Bartusel, H. Führ, V. Oussa, *Phase retrieval for affine groups over prime fields*, arXiv:2109.07123, first submitted 2021-09-15; later Linear Algebra and its Applications 677 (2023), 161--193.
2. Y.-N. Li, Y.-Z. Li, *Conjugate phase retrieval on general Hilbert spaces*, Linear and Multilinear Algebra 72 (2024), 2845--2878, DOI 10.1080/03081087.2023.2300677.
3. *Conjugate phase retrieval on graphs and with applications in shift-invariant spaces*, arXiv:2507.22468.
