# The square-orbit block-rank dichotomy for order-nine harmonic fusion frames

## Finding
Let \(F=\mathbb F_3[t]/(t^2+1)\), and let \(\mathcal Q\) be the family of eighteen distinct four-point sets
\[
Q_{a,b}=a+b\{1,t,-1,-t\},\qquad a\in F,\quad b\in F^\times.
\]
For each allowed nontrivial multiplicative character, consider the corresponding two-plane harmonic equi-isoclinic tight fusion frame constructed in Fickus--Iverson--Jasper--Mixon, Theorems 4.1 and 4.2, at field order nine. Denote the nine planes in dimensions eight and nine by \(U_a^-\subset\mathbb C^8\) and \(U_a^+\subset\mathbb C^9\), respectively, and write \(r_\pm(S)=\dim\bigl(\sum_{a\in S}U_a^\pm\bigr)\) for every \(S\subseteq F\).

For **every** odd multiplicative character in the eight-dimensional construction,
\[
r_-(S)=\min\{2|S|,8\}.
\]
For **every** nontrivial even multiplicative character in the nine-dimensional construction,
\[
r_+(S)=\begin{cases}
2|S|,&0\le |S|\le3,\\
7,&|S|=4,\ S\in\mathcal Q,\\
8,&|S|=4,\ S\notin\mathcal Q,\\
8,&|S|=5,\ F\setminus S\in\mathcal Q,\\
9,&|S|=5,\ F\setminus S\notin\mathcal Q,\\
9,&6\le |S|\le9.
\end{cases}
\]
Consequently every four of the nine eight-dimensional planes span the ambient space; for the nine-dimensional planes there are exactly eighteen deficient four-block choices and eighteen deficient five-block choices, all characterized by an affine four-point square or its complement. The respective rank histograms for four selected blocks are \((7:18,8:108)\) and for five selected blocks \((8:18,9:108)\) in the nine-dimensional family.

## Assumptions and scope
The field operations are taken in \(F\), with \(t^2=-1\), \(g=1+t\) a multiplicative generator of order eight, \(\omega=e^{2\pi i/3}\), \(\zeta=e^{2\pi i/8}\), and \(\psi(x)=\omega^{\mathrm{Tr}_{F/\mathbb F_3}(x)}\). For each character exponent \(e\), define \(\chi_e(g)=\zeta^e\). The four odd exponents are \(e\in\{1,3,5,7\}\), and the three nonzero even exponents are \(e\in\{2,4,6\}\). Oddness means \(\chi_e(-1)=-1\) and evenness means \(\chi_e(-1)=1\), precisely the respective equi-isoclinicity conditions in the cited constructions. Replacing \(\psi\) with any other nontrivial additive character only rescales the frequency labels by a nonzero element of \(F\), which preserves \(\mathcal Q\).

The result is a complete exact **dimension-of-span** classification for these two specific families over the field of nine elements. It does not claim a bound for their smallest positive singular value, for distinct constructions of the same fusion-frame parameters, or for other field orders.

## Proof
For every \(a\in F\), the two-column span of the first construction is represented, after harmless common nonzero row/column rescalings, by the matrix
\[
B^-_a(x,j)=\psi(ax)\chi_e(x)^{-j},\qquad x\in F^\times,\quad j\in\{0,1\}.
\]
For the second construction, the identical formula holds on its eight nonzero rows, together with a ninth row at \(x=0\), having entries \(B^+_a(0,0)=1\), \(B^+_a(0,1)=0\). The constant amplitudes appearing in Theorems 4.1--4.2 are independent of \(a\) and can be removed by invertible column scalings. These reductions preserve all ranks. The source constructs rank-two subspaces: the columns of each \(B^\pm_a\) span the corresponding plane.

Write \(g^j\) for the eight nonzero field elements, with \(j\in\{0,\ldots,7\}\). Every matrix entry lies in the cyclotomic integer ring \(\mathbb Z[\xi]\), where \(\xi=e^{2\pi i/24}\). Because \(4\in\mathbb F_{97}\) has exact order \(24\), substituting \(\xi\mapsto4\) defines a ring homomorphism \(\mathbb Z[\xi]\to\mathbb F_{97}\). Therefore, if a selected block matrix has rank \(r\) after this reduction, then its rank over \(\mathbb C\) is at least \(r\): a nonzero reduced minor lifts to a nonzero complex minor.

The accompanying pure-standard-library checker builds the two complete character families from field multiplication and trace, and computes the reduced rank of **all** relevant selected block matrices by exact modular elimination. For the eight-dimensional family it finds rank eight for each of the \(\binom94=126\) four-block choices and each of the four odd characters. For the nine-dimensional family it establishes the claimed rank lower bounds for all \(\binom9k\) subsets with \(1\le k\le6\), separately for all three nontrivial even characters.

It remains essential to prove the *upper* bounds for the exceptional strata: a rank drop modulo a prime alone would not do this. For the canonical square \(T=\{1,t,-1,-t\}\), the checker verifies, using exact integer arithmetic in \(\mathbb Z[i,\omega]\) and the relations \(i^2=-1\), \(\omega^2+\omega+1=0\), an explicit nonzero right-kernel vector of the four-block nine-dimensional matrix for each even character. It separately verifies a nonzero left-kernel vector of the five-block matrix indexed by \(F\setminus T\) for each even character. All six witness vectors are given literally in the checker, including their ordering; every row or column orthogonality equation is evaluated exactly, not approximately. Thus the complex ranks for these two canonical configurations are at most seven and eight, respectively.

For any \(c\in F\) and \(b\in F^\times\), translation \(a\mapsto a+c\) of block labels multiplies each nonzero row by \(\psi(cx)\), while dilation \(a\mapsto ba\) is implemented by the nonzero-row permutation \(x\mapsto b^{-1}x\) and invertible scalar changes to the two column types. In the augmented matrix the zero row is respected. Hence every affine copy \(T\mapsto c+bT\) has the same selected-block ranks. The set of such copies has cardinality exactly eighteen: the four-point multiplicative subgroup has two cosets in \(F^\times\), and its translates give two different four-point sets for each of the nine centers. The center is uniquely recovered as the sum of the four elements, since the field has characteristic three and the sum of the four elements of the subgroup is zero; thus distinct centers cannot coincide. The corresponding complements have the same count. This transports both upper-rank certificates to exactly the named exceptional configurations. Combining with the exhaustive certified lower ranks gives equality in every case through size six. For sizes seven to nine, every selected set contains a six-set, and each six-set spans \(\mathbb C^9\). For the eight-dimensional construction, four-block independence similarly determines all smaller and larger cardinalities.

## Verification
Run `python3 verify_q9_fusion.py` from the directory containing this document. The checker performs \(1899\) exact modular rank calculations and verifies six separate exact cyclotomic upper-rank witness identities. In the nine-dimensional family the checked histograms are \((2:9)\), \((4:36)\), \((6:84)\), \((7:18,8:108)\), \((8:18,9:108)\), and \((9:84)\) at the selected block sizes one through six, respectively, for each even character. The proof for all cardinalities is the finite exhaustive certificate plus the explicitly explained inclusion and affine-symmetry arguments; no numerical tolerance or sampling hypothesis is involved.

## Relationship to prior work
Fickus--Iverson--Jasper--Mixon establish the harmonic EITFF constructions and their pairwise isoclinicity, including their precise parity conditions on the multiplicative character; these are not new claims. Their Theorems 4.1 and 4.2 do not state the complete higher-order block-rank profile proved here. The general theory of fusion-frame restricted isometry and full-spark ordinary frames studies different implications. In particular, pairwise block coherence does not automatically force these four- and five-block ranks; the two canonical families exhibit sharply different failure behavior at order nine. The result concerns a specific finite-group model rather than a general EITFF classification.

## Limitations
This is an exact finite-field theorem for the particular order-nine constructions, not a field-uniform statement. The nonzero determinant arguments rely on a complete reproducible finite computation; the exceptional upper bounds rely additionally on explicit exact witnesses. The use of \(\mathbb F_{97}\) for *lower* rank bounds is logically one-way, as made explicit above. The claim of newness remains subject to unidentified equivalent descriptions in older block-spark or finite-geometry literature; independent audit has not been performed.

## References
1. M. Fickus, J. W. Iverson, J. Jasper, D. G. Mixon, *Harmonic Grassmannian codes*, arXiv:2112.14267v1 (publicly available December 28, 2021), especially Theorems 3.4, 4.1, 4.2 and their formulas: https://arxiv.org/html/2112.14267v1.
2. B. G. Bodmann, J. Cahill, P. G. Casazza, *Fusion Frames and the Restricted Isometry Property*, arXiv:1112.0158 (2011): https://arxiv.org/abs/1112.0158.
3. B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548 (2011): https://arxiv.org/abs/1110.3548.
