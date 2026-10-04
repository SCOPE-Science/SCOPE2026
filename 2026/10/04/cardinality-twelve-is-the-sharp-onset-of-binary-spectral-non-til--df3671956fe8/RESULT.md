# Cardinality twelve is the sharp onset of binary spectral non-tiling
## Finding
Among all finite-dimensional binary vector spaces \(G=\mathbb F_2^d\), the minimum cardinality of a spectral subset that does not tile \(G\) by translations is exactly \(12\).

The new structural part is stronger: for every \(d\ge 1\), every spectral subset \(E\subset\mathbb F_2^d\) with \(|E|=8\) tiles with a linear-subspace tiling complement. Thus an eight-point spectral set is a full graph set in the terminology of Aten et al.

The bound is attained: a normalized Paley Hadamard matrix of order \(12\) has a dephased binary logarithm of rank \(10\), yielding a twelve-point spectral subset of \(\mathbb F_2^{10}\); it cannot tile because \(12\nmid 2^{10}\).

## Assumptions and scope
A nonempty set \(E\subset\mathbb F_2^d\) is spectral if there is a set \(\Lambda\subset\mathbb F_2^d\), with \(|\Lambda|=|E|\), such that the character matrix
\[
H_{x,\lambda}=(-1)^{x\cdot\lambda},\qquad x\in E,\ \lambda\in\Lambda,
\]
has pairwise orthogonal rows. A set tiles by translations if \(\mathbb F_2^d\) is a disjoint union of translates of it.

The lower-bound theorem is dimension-free. The upper-bound witness is in dimension \(10\). No assertion is made about the least dimension in which a binary spectral non-tile occurs; the cited literature leaves dimensions \(7,8,9\) unresolved.

## Proof
Translate \(E\) and its spectrum \(\Lambda\) independently so that \(0\in E\cap\Lambda\). This preserves spectrality and tiling. For \(|E|=8\), the character matrix \(H\) is then a normalized real Hadamard matrix: its first row and first column consist of \(+1\).

Consider a nonfirst row of \(H\). Orthogonality with the first row implies that it has four \(+1\) entries and four \(-1\) entries. Since its first entry is \(+1\), its \(+1\) positions among the remaining seven columns form a three-element subset \(C_i\). For two distinct nonfirst rows, let \(a=|C_i\cap C_j|\). Among the last seven columns the two rows agree in \(1+2a\) positions, and they also agree in the first column. Orthogonality therefore gives
\[
2+2a=4,
\]
so \(a=1\).

Hence the seven sets \(C_i\) are seven triples on seven points, any two meeting in exactly one point. No pair of points can lie in two triples, while the seven triples contain \(7\binom32=21=\binom72\) pairs in total. Thus they form the Steiner triple system on seven points, which is unique up to relabeling: the Fano plane.

Label the seven nonfirst columns by the nonzero vectors \(u\in\mathbb F_2^3\). The Fano lines are exactly
\[
C_v=\{u\ne0:v\cdot u=0\},\qquad 0\ne v\in\mathbb F_2^3.
\]
After relabeling rows, the normalized Hadamard matrix therefore has rows
\[
r_v(u)=(-1)^{v\cdot u},\qquad u,v\in\mathbb F_2^3.
\]
In particular its eight rows are closed under pointwise multiplication:
\[
r_vr_w=r_{v+w}.
\]

Return to the original character description of \(H\). Put
\[
K=\{g\in\mathbb F_2^d:g\cdot\lambda=0\text{ for every }\lambda\in\Lambda\}.
\]
For \(x,y\in E\), pointwise multiplication of the corresponding rows is the row \(\lambda\mapsto(-1)^{(x+y)\cdot\lambda}\). Row closure therefore gives a \(z\in E\) such that
\[
x+y+z\in K.
\]
Distinct points of \(E\) lie in distinct cosets of \(K\), because otherwise their rows in \(H\) would be identical. Consequently the image \(U\) of \(E\) in \(\mathbb F_2^d/K\) has eight elements, contains zero, and is closed under addition. It is therefore a three-dimensional subspace.

Let \(P\) be the inverse image of \(U\). Then \(P\) is a subspace, \(K\subset P\), and \(E\) is a complete set of representatives for the eight cosets of \(K\) in \(P\). Choose a linear complement \(L\) of \(P\) in \(\mathbb F_2^d\). Then
\[
T=K\oplus L
\]
is a subspace and every element of \(\mathbb F_2^d\) has a unique representation \(e+t\) with \(e\in E\) and \(t\in T\). Thus \(E\) tiles with the subspace complement \(T\).

It remains to exclude smaller cardinalities. The character matrix of any binary spectral set is a real Hadamard matrix. A real Hadamard matrix of order \(m>2\) has \(4\mid m\): normalize its first row; a second row has equally many signs, and orthogonality of a third row with the first two forces each half-size to be even. Therefore the only possible spectral cardinalities below \(12\) are \(1,2,4,8\). Sets of sizes \(1\) and \(2\) tile immediately. Every four-point set tiles: after translation it is \(\{0,a,b,c\}\); if its span has dimension two it is that subspace, while if \(a,b,c\) are independent then \(\{0,a+b+c\}\) is a tiling complement inside their three-dimensional span, and a complementary subspace extends the tiling to the ambient space. The eight-point case was proved above. Hence no binary spectral non-tile has fewer than twelve points.

For sharpness, take the Paley Hadamard matrix of order \(12\), built from the quadratic character of \(\mathbb F_{11}\). Its normalized binary logarithm \(M\), obtained by replacing \(+1\) by \(0\) and \(-1\) by \(1\), has rank \(10\) over \(\mathbb F_2\). A rank factorization \(M=AB^{\mathsf T}\) produces twelve distinct rows of \(A\) and twelve distinct rows of \(B\) in \(\mathbb F_2^{10}\), and
\[
(-1)^{A B^{\mathsf T}}
\]
is Hadamard. Thus the rows of \(A\) form a twelve-point spectral set with spectrum given by the rows of \(B\). Since a translational tile in a finite group must have cardinality dividing the group order and \(12\nmid2^{10}\), this spectral set does not tile.

## Verification
The accompanying `verify.py` performs two exact checks. First, it enumerates all labeled Steiner triple systems on seven points satisfying the pairwise-intersection condition arising from a normalized Hadamard matrix of order \(8\); it finds \(30\), and for every one verifies closure of the eight associated sign rows under pointwise multiplication. Second, it constructs the Paley Hadamard matrix of order \(12\), verifies \(HH^{\mathsf T}=12I\), verifies that its dephased binary logarithm has rank \(10\), computes an explicit rank factorization over \(\mathbb F_2\), and checks the resulting twelve-point spectral pair. The script prints `VERIFY_OK`.

These finite computations verify the two finite combinatorial cores. The dimension-free tiling statement itself follows from the quotient-and-transversal proof above, not from finite enumeration over ambient dimensions.

## Relationship to prior work
Aten et al. established the log-Hadamard formulation of finite-field spectral pairs and showed that a set with a subspace tiling partner is equivalently a full graph set. Their general theorem covers spectral sets of cardinality \(p\) or \(p^{d-1}\), which for eight-point binary sets only gives the four-dimensional case.

Ferguson and Sothanaphan proved the binary conjecture in dimension four, but explicitly noted that their simple proof does not extend to higher dimensions. They then used computation for dimensions five and six. Their addendum states that a set in \(\mathbb F_2^6\) of size \(8\) or \(16\) is spectral if and only if it tiles, and explains a finite search for the size-eight case. The theorem here replaces that dimension-bounded computation for size \(8\) by a dimension-free structural argument and gives a subspace tiling complement.

The same 2019 work dephased Tao's order-twelve Hadamard construction to rank \(10\), producing a twelve-point spectral non-tile in \(\mathbb F_2^{10}\). Combining that known upper witness with the new dimension-free eight-point theorem identifies twelve as the exact minimum cardinality of a binary spectral non-tile.

## Limitations
The theorem does not settle Fuglede's conjecture in \(\mathbb F_2^d\) for dimensions \(7,8,9\), nor does it classify spectral sets of cardinality \(16\) or larger. The originality search covered the primary 2019 paper and its addendum, the 2015 finite-field framework, targeted exact-claim searches, later finite-group Fuglede literature, and the current semantic database; an unindexed equivalent argument remains a residual risk.

## References
1. S. J. Ferguson and N. Sothanaphan, "Fuglede's conjecture fails in 4 dimensions over odd prime fields," arXiv:1901.08734; *Discrete Mathematics* 343 (2020), 111507. DOI: 10.1016/j.disc.2019.04.026.
2. S. J. Ferguson and N. Sothanaphan, "Addendum to 'Fuglede's conjecture fails in 4 dimensions over odd prime fields'," arXiv:1910.04212.
3. C. Aten et al., "Tiling sets and spectral sets over finite fields," *Journal of Functional Analysis* 273 (2017), 2547–2577. DOI: 10.1016/j.jfa.2016.10.018.
