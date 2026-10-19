# Automorphism-order strata of full-support three-dimensional evolution algebras over finite fields

## Finding

For every prime power \(q\), all full-support three-dimensional perfect evolution algebras over \(\mathbb F_q\) have automorphism groups isomorphic to one of \(1,C_2,C_3,S_3\). The exact number of isomorphism classes with each group is given by the following explicit formulas, including the exceptional characteristics \(2\) and \(3\).

Set
\[
\begin{aligned}
D&=3(q-1)^3(q-2)^2+(q-1)^2(q-2)(q-3)(q^2-3q+3),\\
T&=\begin{cases}(q-2)(q-1)^2,&\operatorname{char}\mathbb F_q=2,\\
(q-1)(q^2-4q+5),&\operatorname{char}\mathbb F_q\ne2,
\end{cases}\\
E&=\begin{cases}q^2-3q+3,&\operatorname{char}\mathbb F_q=3,\\
q^2-5q+10,&q\equiv1\pmod3,\\
(q-1)(q-2),&q\equiv2\pmod3,
\end{cases}\\
S&=\begin{cases}q-2,&\operatorname{char}\mathbb F_q\in\{2,3\},\\
q-3,&\operatorname{char}\mathbb F_q\notin\{2,3\}.
\end{cases}
\end{aligned}
\]
(The three cases defining \(E\) are disjoint because powers of \(3\) have residue \(0\) modulo \(3\).)

If \(c_H(q)\) denotes the number of isomorphism classes of such algebras whose ordinary \(\mathbb F_q\)-linear automorphism group is isomorphic to \(H\), then
\[
\boxed{\begin{aligned}
c_1(q)&=\frac{D-3T-E+3S}{6},\\
c_{C_2}(q)&=T-S,\\
c_{C_3}(q)&=\frac{E-S}{2},\\
c_{S_3}(q)&=S.
\end{aligned}}
\]
These are nonnegative integers for every prime power. In particular, there are no such algebras over \(\mathbb F_2\). Over \(\mathbb F_3\), the four respective counts are \(2,3,1,1\); over \(\mathbb F_4\) they are \(66,16,2,2\). All the algebras counted here are absolutely simple.

## Assumptions and scope

An evolution algebra \(A\) over \(\mathbb F_q\) has a natural basis \(e_1,e_2,e_3\) satisfying \(e_ie_j=0\) for \(i\ne j\), with \(e_j^2=\sum_i a_{ij}e_i\). Its structure matrix is \(M=(a_{ij})\). We call \(A\) *perfect* when \(A^2=A\), equivalently \(\det M\ne0\), and *full-support* when each of the nine entries of some (equivalently every) natural-basis structure matrix is nonzero. Isomorphisms and automorphisms are linear over \(\mathbb F_q\), not semilinear. The counts are counts of algebra isomorphism classes, not labeled natural bases.

For perfect evolution algebras, any algebra isomorphism takes a natural basis to a monomial transformation of a natural basis. Monomial scaling and permutation preserve the nonzero-entry support condition. In the full-support locus, the three diagonal entries are nonzero, so uniquely rescaling the natural basis makes all diagonal entries of \(M\) equal to \(1\). Two such *normalized* matrices define isomorphic algebras exactly when they are simultaneously permuted in rows and columns by \(S_3\). Their automorphism groups are precisely their stabilizers under this \(S_3\)-action.

Let \(\mathcal X_q\) be the set of invertible normalized matrices
\[
\begin{pmatrix}1&a&b\\ c&1&d\\e&f&1\end{pmatrix},\qquad
(a,b,c,d,e,f)\in(\mathbb F_q^\times)^6.
\]
The theorem is an exact stabilizer-type orbit census of \(\mathcal X_q\).

## Proof

**1. Normalization and simplicity.** The monomial property can be proved directly: if \(\phi(e_i)=\sum_k p_{ki}e_k\) is an isomorphism between perfect evolution algebras, then for \(i\ne j\) the identity \(0=\phi(e_i)\phi(e_j)=\sum_k p_{ki}p_{kj}e_k^2\) and linear independence of the squares imply \(p_{ki}p_{kj}=0\) for every \(k\). Thus the invertible matrix \(P=(p_{ki})\) has disjoint column supports and must be monomial. Its structure matrix action is \(M\mapsto P^{-1}MP^{(2)}\). For a diagonal \(P=\operatorname{diag}(t_i)\), the new diagonal entries are \(t_i a_{ii}\). Hence \(t_i=a_{ii}^{-1}\) is the unique diagonal normalization. If two matrices already have unit diagonal, any monomial isomorphism between them has diagonal factor equal to the identity after its permutation; their residual equivalence is just \(S_3\). Consequently the full algebra automorphism group of a normalized member is the subgroup of \(S_3\) fixing its matrix under simultaneous index permutation.

Every full-support perfect algebra is absolutely simple. Indeed, for any nonzero ideal \(I\), choose a nonzero \(x=\sum_i x_ie_i\in I\) and \(j\) with \(x_j\ne0\). Then \(e_j^2=x_j^{-1}xe_j\in I\). Each coefficient of \(e_j^2\) in the natural basis is nonzero, so \(e_i e_j^2\) is a nonzero multiple of \(e_i^2\) lying in \(I\) for all \(i\). Since \(M\) is invertible, these three squares span \(A\); thus \(I=A\). The same argument holds over every field extension.

**2. Counting all normalized matrices.** To count \(D=|\mathcal X_q|\), first count invertible \(3\)-by-\(3\) matrices all of whose entries are nonzero, and divide by \((q-1)^3\), the number of ways to choose their nonzero diagonal entries. Choose the first row freely in \((\mathbb F_q^\times)^3\), then describe the second row by coordinatewise ratios \((t_1,t_2,t_3)\). Linear independence means these ratios are not all equal. Exactly one of the three coordinates of the normal vector to their row span vanishes when exactly two ratios agree; this occurs in \(3(q-1)(q-2)\) ways. None vanishes when the ratios are pairwise distinct; this occurs in \((q-1)(q-2)(q-3)\) ways. For these two types, the plane contains respectively \((q-1)^2\) and \((q-1)(q-2)\) vectors with all entries nonzero. Subtracting from \((q-1)^3\) gives the choices for an independent third row. Thus
\[
\begin{split}
D={}&3(q-1)(q-2)\bigl((q-1)^3-(q-1)^2\bigr)\\
&+(q-1)(q-2)(q-3)\bigl((q-1)^3-(q-1)(q-2)\bigr),
\end{split}
\]
which expands to the stated expression.

**3. One transposition.** The normalized matrices fixed by the transposition \((12)\) are precisely
\[
M=\begin{pmatrix}1&x&y\\x&1&y\\z&z&1\end{pmatrix},
\qquad x,y,z\ne0,
\]
with determinant \((1-x)(1+x-2yz)\). In characteristic \(2\), nonsingularity is equivalent to \(x\ne1\), so their number is \(T=(q-2)(q-1)^2\). In odd characteristic, exclude \(x=1\), and for each of the \(q-3\) remaining values other than \(x=-1\), exactly \(q-1\) nonzero ordered pairs \((y,z)\) make the second factor vanish. Hence \(T=(q-1)(q^2-4q+5)\).

**4. A three-cycle.** The normalized matrices fixed by \((123)\) are the circulant matrices
\[
M=\begin{pmatrix}1&u&v\\v&1&u\\u&v&1\end{pmatrix},
\qquad u,v\in\mathbb F_q^\times,
\]
with determinant \(1+u^3+v^3-3uv\). In characteristic \(3\), this is \((1+u+v)^3\), yielding \(E=(q-1)^2-(q-2)=q^2-3q+3\). If \(q\equiv1\pmod3\), the determinant factors into the three distinct linear factors \(1+u+v\), \(1+\zeta u+\zeta^2v\), and \(1+\zeta^2u+\zeta v\) for a primitive cube root \(\zeta\in\mathbb F_q\). Each factor vanishes at \(q-2\) points of the nonzero torus, and the three pairwise intersections lie in the torus, are distinct, and have no triple intersection. Inclusion–exclusion gives \(E=(q-1)^2-[3(q-2)-3]=q^2-5q+10\). If \(q\equiv2\pmod3\), the two nontrivial factors are Galois conjugate over \(\mathbb F_{q^2}\) and have a common \(\mathbb F_q\)-zero only at \(u=v=1\); this point does not lie on \(1+u+v=0\). The total number of zeros in the torus is \(q-2+1=q-1\), giving \(E=(q-1)(q-2)\).

**5. Full symmetric invariance and stabilizer inversion.** All six off-diagonal entries of an \(S_3\)-fixed normalized matrix are equal to some \(t\ne0\). Its determinant is \((1-t)^2(1+2t)\). The number of permissible \(t\)'s is therefore \(S=q-2\) in characteristic \(2\) or \(3\), and \(S=q-3\) otherwise.

The subgroups of \(S_3\) are the trivial group, three groups of order \(2\), one group of order \(3\), and \(S_3\) itself. Their fixed-point sets intersect in the \(S_3\)-fixed set whenever distinct proper nontrivial subgroups are involved. The counts of normalized matrices with *exact* stabilizers of respective orders \(1,2,3,6\) are consequently
\[
D-3T-E+3S,\qquad3(T-S),\qquad E-S,\qquad S.
\]
An orbit whose stabilizer has size \(h\) has \(6/h\) matrices. Dividing the corresponding labeled counts by \(6/h\) proves all four isomorphism-class formulas.

## Verification

The standalone program `artifacts/check_automorphism_profile.py` constructs \(\mathbb F_q\), independently enumerates all \((q-1)^6\) normalized candidate matrices, computes their exact determinants and stabilizers under all six permutations, and compares the resulting four exact counts with the theorem. Tests were executed for \(q=2,3,4,5,7,8,9\), including three extension fields and all characteristic/residue cases. Every test passed and printed `ALL_EXACT_CHECKS_PASSED 7 finite fields`. The finite enumerations check the formulas but do not replace the all-prime-power proof.

## Relationship to prior work

Wei and Zou's *Isomorphism Classes of Idempotent Evolution Algebras* (2023) establishes the general monomial orbit action and gives exact total numbers of perfect evolution-algebra isomorphism classes in dimensions \(2,3,4\) over finite fields. Its proof counts fixed points in the *entire* invertible-matrix space, including circulant matrices. It does not give the four individual stabilizer-order multiplicities on the invariant full-support open locus in dimension \(3\). The present result uses its monomial equivalence premise, but recovers the finer automorphism-group distribution using a new full-support determinant census and subgroup inversion; knowing only the total orbit count does not determine that distribution.

Costoya, Muñoz, Tocino and Viruel (2023) realize finite groups as automorphism groups of absolutely simple Cayley evolution algebras. Their construction establishes existence of prescribed symmetry groups, not counts within the full-support three-dimensional locus. The related finite-dimensional graph-automorphism framework supplies qualitative background, but not these exact finite-field strata.

## Limitations

The result covers only the natural dense full-support locus of perfect three-dimensional evolution algebras. It does not count algebras with zero structure constants or classify automorphism group schemes or semilinear automorphisms. The calculation refines established monomial orbit theory rather than claiming that theory itself is new. Related subgroup-refined orbit calculations under another terminology may exist; indexed and inspected sources do not establish absolute publication priority. Independent mathematical audit has not been performed.

## References

1. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, Linear Algebra and Its Applications **675** (2023), 142–178, preprint arXiv:2310.12368, first posted 2023-10-18. https://arxiv.org/abs/2310.12368
2. C. Costoya, V. Muñoz, A. Tocino, and A. Viruel, *Automorphism groups of Cayley evolution algebras*, RACSAM **117** (2023), article 82. https://doi.org/10.1007/s13398-023-01414-w
3. A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, Linear and Multilinear Algebra **69** (2021), 331–342. https://arxiv.org/abs/1902.02191
4. S. Sriwongsa and Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, Linear Algebra and Its Applications **641** (2022), 143–155. https://arxiv.org/abs/2202.01333
