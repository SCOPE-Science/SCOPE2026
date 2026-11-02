# Rank-stratified commuting tuples and a sharp reducibility transition for three-block nilradicals

## Finding
Let \(k=\mathbb F_q\). Fix integers \(r\ge2\), \(c\ge1\), and \(m\ge0\). Let \(\mathfrak n_{1,r,c}\) be the Lie algebra of strictly upper three-block matrices with block sizes \((1,r,c)\). The number of ordered \(m\)-tuples whose members commute pairwise is
\[
C_{r,c}(m;q)=q^{cm}\sum_{d=0}^{\min(m,r)}
\left(\prod_{i=0}^{d-1}\frac{(q^m-q^i)(q^r-q^i)}{q^d-q^i}\right)
q^{c[m(r-d)+d(d+1)/2]}.
\]
Empty products are one. The sum is an integer, and \(C_{r,c}(0;q)=1\). The same count holds for ordered pairwise-commuting tuples in the three-block unipotent group \(1+\mathfrak n_{1,r,c}\).

There is also a geometric refinement over every field: the stratum on which the matrix of first-superdiagonal row blocks has rank \(d\) is a Zariski-locally trivial affine vector bundle over the irreducible variety of rank-\(d\) matrices of size \(m\times r\), with fiber dimension
\[cm+c\bigl[m(r-d)+d(d+1)/2\bigr].\]
Its dimension is
\[cm+d(m+r-d)+c\bigl[m(r-d)+d(d+1)/2\bigr].\]
Here and below geometric statements concern the underlying reduced commuting-tuple varieties, not their possibly nonreduced equation schemes.

**Sharp pair-variety transition.** Specialize to \(r=m=2\), allowing any \(c\ge1\). Then
\[C_{2,c}(2;q)=q^{6c}+(q^4-1)q^{5c}.\]
Over an algebraic closure, the reduced pairwise-commuting variety is irreducible if and only if \(c\le3\). If \(c\ge4\), it has exactly two irreducible components of dimensions \(6c\) and \(5c+4\); these components have equal dimension exactly for \(c=4\). Thus the leading-power asymptotics of finite-field counts change at \(c=4\): the dominant nonzero-first-block stratum has dimension \(5c+4\) for \(c\le3\), both dimensions tie at \(c=4\), and the first-block-zero component dominates for \(c\ge5\).

## Assumptions and scope
Every matrix in \(\mathfrak n_{1,r,c}\) has the form
\[X(a,B,z)=\begin{pmatrix}0&a&z\\0&0&B\\0&0&0\end{pmatrix},\]
where \(a\) is a \(1\times r\) row, \(B\) an \(r\times c\) matrix, and \(z\) a \(1\times c\) central row. The Lie bracket is \([X(a,B,z),X(a',B',z')]=X(0,0,aB'-a'B)\). No restriction on the characteristic is imposed. A commuting \(m\)-tuple means every two entries commute, and \(m=0\) denotes the unique empty tuple. The geometric statements hold after extension to an algebraic closure of any ground field.

## Proof
**1. Rank stratification.** For a tuple \((X_i)_{i=1}^m\), arrange its \(a_i\) into an \(m\times r\) matrix \(A\). For each column \(j\in\{1,\ldots,c\}\), form an \(m\times r\) matrix \(Y_j\) with row \(i\) equal to column \(j\) of \(B_i\), transposed. The commutativity equations are precisely
\[AY_j^{\mathsf T}=Y_j A^{\mathsf T}\qquad(1\le j\le c).\]
The \(cm\) central coordinates \(z_i\) are independent and unrestricted.

Fix \(A\) of rank \(d\), where \(0\le d\le\min(m,r)\). Row and column operations put it in the matrix normal form \(\begin{psmallmatrix}I_d&0\\0&0\end{psmallmatrix}\). The induced invertible operations on each \(Y_j\) preserve the property that \(AY_j^{\mathsf T}\) is symmetric. In this normal form, the upper-left \(d\times d\) block of \(Y_j\) is symmetric and the first \(d\) columns of its last \(m-d\) rows vanish. These are exactly \(\binom d2+d(m-d)\) independent linear equations. All other entries are free. Hence each \(Y_j\) has
\[mr-\binom d2-d(m-d)=m(r-d)+d(d+1)/2\]
free parameters. This proves the claimed fiber dimension, including \(d=0\).

The rank-\(d\) locus of \(m\times r\) matrices is irreducible of dimension \(d(m+r-d)\), and the displayed equations define a constant-rank kernel subbundle over it. Including free central coordinates, each commuting stratum is the claimed vector bundle and is irreducible. The number of rank-\(d\) matrices over \(\mathbb F_q\), by the standard full-rank factorization count, is
\[R_{m,r,d}(q)=\prod_{i=0}^{d-1}\frac{(q^m-q^i)(q^r-q^i)}{q^d-q^i}.\]
Multiplying by the fiber size and summing disjoint strata proves the all-arity formula. Because the group commutator of \(1+X\) and \(1+Y\) vanishes exactly when \(XY=YX\), the unipotent-group conclusion follows in every characteristic.

**2. Pair-variety transition.** Put \(m=r=2\). For each \(A\ne0\), the single symmetry equation in every \(Y_j\) is a nonzero linear functional on four entries. Thus all \(A\ne0\) points form an irreducible vector bundle over \(\mathbb A^4\setminus\{0\}\), of dimension \(4+5c\), with \((q^4-1)q^{5c}\) rational points. The closed stratum \(A=0\) is affine space of dimension \(6c\), with \(q^{6c}\) rational points. These give the pair formula.

If \(c\le3\), take any point with \(A=0\) and fixed \(Y_1,\ldots,Y_c\). Requiring a prospective \(A_0\) to commute with these \(Y_j\) gives at most \(c\) homogeneous linear equations in its four coordinates. A nonzero solution \(A_0\) exists over every field. The affine curve \(A=tA_0\), with all \(Y_j\) and all central coordinates fixed, consists of commuting points and specializes to the chosen \(A=0\) point. Hence the closed stratum belongs to the closure of the irreducible \(A\ne0\) stratum, proving irreducibility for \(c\le3\).

If \(c\ge4\), the closed \(A=0\) stratum has dimension \(6c\ge 5c+4\), whereas the closure of the irreducible \(A\ne0\) stratum has dimension \(5c+4\). These two closed irreducible sets are distinct, and neither contains the other: the first contains no nonzero \(A\), and the second cannot contain the first of at least equal dimension. Since their union is the entire reduced variety, they are its exactly two irreducible components. Equality of dimensions occurs only at \(c=4\). This establishes every geometric assertion.

## Verification
A standalone dependency-free program `verify_commuting.py` explicitly enumerates rows \(a_i\), blocks \(B_i\), and their matrix-product commutators, independently computing predicted rank-\(d\) matrix counts with the Gaussian product formula. The program exhaustively tests ten small configurations over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), including empty and singleton tuples, and prints `THREE_BLOCK_RANK_STRATIFIED_COMMUTING_OK 10` on success. Examples: \(C_{2,2}(2;2)=19456\), \(C_{2,1}(3;2)=5888\), and \(C_{2,1}(2;4)=265216\). This is finite corroboration, not a substitute for the general proof. Reproduce by running `python3 verify_commuting.py`.

## Relationship to prior work
Ghimire and Huang's 2016 preprint (arXiv:1603.08044v1), with the same strictly block-upper-triangular matrix algebras, studies **derivations**, not all-arity commuting point counts. Ghimire's 2016 thesis, especially Chapter 3, was inspected for this distinction. Goodwin and Röhrle's 2012 preprint on commuting varieties of Borel nilradicals gives geometric component results and notes related *parabolic* examples in Remark 3.1, notably block sizes \((1,1,c)\); it does not state the present \((1,2,c)\) threshold or the Gaussian all-tuple formula. Goddard and Goodwin's arXiv:1606.02262 considers commuting pairs in full parabolic Lie algebras, rather than this nilradical's finite-field tuples. The older special case with middle block size one and the general notions of rank strata, vector bundles, and Gaussian counts are prior knowledge; no novelty is claimed for them alone.

## Limitations
The full counting result requires one outer block of size one and three strict blocks. It is not a formula for arbitrary parabolic nilradicals or for conjugacy classes of tuples. The component statement concerns pairs with middle block dimension two, not all tuple lengths. It classifies reduced irreducible components, not nonreduced scheme structure. Historical priority remains subject to possible equivalent results under other geometric or quiver terminology. No independent mathematical audit has been performed.

## References
1. P. Ghimire and H. Huang, *Derivations of the Lie algebra of strictly block upper triangular matrices*, arXiv:1603.08044v1, first submitted 2016-03-25; published in *Journal of Lie Theory* 30 (2020), 1027–1046, DOI 10.5802/jolt.1149.
2. P. Ghimire, *Derivations of subalgebras of the Lie algebra of block upper triangular matrices*, Auburn University dissertation, 2016-08-06, especially Chapters 1 and 3, https://etd.auburn.edu/bitstream/handle/10415/5271/final%20version%20of%20dissertation.pdf?isAllowed=y&sequence=2.
3. S. Goodwin and G. Röhrle, *On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras*, Oberwolfach Preprints 2012-14, 2012-12-04, DOI 10.14760/OWP-2012-14, especially Section 3 and Remark 3.1.
4. R. Goddard and S. Goodwin, *On commuting varieties of parabolic subalgebras*, arXiv:1606.02262v1, 2016-06-07.
