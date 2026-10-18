# A sharp one-line obstruction for covering finite-field elliptic cubics with one rational involution

## Finding

Let \(E\subset\mathbb P^2_{\mathbb F_q}\) be a smooth plane cubic with an \(\mathbb F_q\)-rational flex \(O\), and let \(N=\#E(\mathbb F_q)\) be divisible by \(3\). Define \(\operatorname{cov}(E)\) as the least number of projective \(\mathbb F_q\)-lines whose union contains all rational points of \(E\). Then

\[
\operatorname{cov}(E)=\frac N3 +\begin{cases}1,&\#E(\mathbb F_q)[2]=2,\\0,&\#E(\mathbb F_q)[2]\ne2.\end{cases}
\]

Thus the presence of **exactly one nonidentity rational point of order two** gives a sharp, uniform, one-line covering defect. For every other two-torsion type the elementary Bézout bound is attained. The zero-defect case is already implied by Cichacz's general zero-sum partition theorem; the excess-one conclusion is the specific contribution emphasized here.

## Assumptions and scope

The field \(\mathbb F_q\) is any finite field, including characteristics \(2\) and \(3\); the cubic is smooth and geometrically integral, and its given plane embedding has a rational flex \(O\). Equip \(G=E(\mathbb F_q)\) with the elliptic group law based at \(O\). We assume \(3\mid N=|G|\), and write \(m=N/3\). Finite elliptic groups have at most three nonzero elements of order two. The notation \(G[2]\) includes the identity, so \(|G[2]|\in\{1,2,4\}\). A secant joining two rational points is a rational line; three **distinct** rational points lie on one such line if and only if their group sum is \(O\).

## Proof

**1. The basic obstruction.** Bézout gives \(\operatorname{cov}(E)\ge m\), since a line meets a smooth cubic in at most three distinct points. Suppose \(|G[2]|=2\), with unique nonzero involution \(\iota\). Pairing \(g\) with \(-g\) gives
\[
\sum_{g\in G}g=\iota\ne O.
\]
If \(m\) lines covered all \(3m\) points, each would have to contain exactly three distinct rational points and the resulting triples would be pairwise disjoint. Every such triple has group sum \(O\), so summing all \(m\) triples would give \(\sum_{g\in G}g=O\), a contradiction. Therefore \(\operatorname{cov}(E)\ge m+1\) in the unique-involution case.

**2. An index-three embedding of transversals.** Choose a surjective homomorphism \(\chi:G\to\mathbb Z/3\mathbb Z\), which exists because \(G\) is finite abelian and \(3\mid|G|\). Set \(H=\ker\chi\), so \(|H|=m\), and choose \(u\in G\) with \(\chi(u)=1\). The three disjoint cosets are \(H\), \(u+H\), and \(2u+H\), with \(3u\in H\).

A partial transversal in the addition table of \(H\) is a family of pairs \((h_i,k_i)\) in which all first coordinates, all second coordinates, and all sums \(h_i+k_i\) are separately distinct. Associate to each pair the three points
\[
T_i=\big\{h_i,\;u+k_i,\;2u-3u-h_i-k_i\big\}.
\]
They lie in three different cosets and sum to \(O\). Thus each \(T_i\) consists of three distinct rational collinear points; the transversal condition ensures that the \(T_i\)'s are disjoint. Consequently, a transversal of order \(m\) gives an \(m\)-line cover. A near transversal of order \(m-1\) gives \(m-1\) disjoint trisecants, leaving exactly three rational points, which are covered by at most two further rational lines. (For the last three points, join any two; a rational line through the remaining point always exists.) Hence
\[
\operatorname{cov}(E)\le m+1
\]
for every such cubic, using Goddyn--Halasz's theorem that every finite-group Cayley table admits a near transversal. Combined with Step 1, this proves the exact \(m+1\) formula for unique rational involution.

**3. The zero-defect case and complete classification.** Because \(H\) has odd index in \(G\), its Sylow-two subgroup equals that of \(G\). If \(|G[2]|\ne2\), that subgroup is trivial or noncyclic. The complete-mapping theorem quoted as Theorem 4 by Goddyn--Halasz then gives a full transversal of the addition table of \(H\), and Step 2 gives an \(m\)-line cover. Equivalently, Cichacz's 3-zero-sum partition theorem directly supplies a partition of \(G\) into zero-sum triples whenever \(G\) has odd order or more than one involution. Bézout makes this optimum. Both arguments identify the same zero-defect regime, which is **not independently new**.

**4. Explicit witnesses for cyclic groups.** Suppose \(G\cong\mathbb Z/(3m)\mathbb Z\) and index elements by integers modulo \(3m\). If \(m\) is odd, for every \(0\le a<m\) set \(b=a\) and \(c\equiv-2a-1\pmod m\). Then \(\{3a,\,3b+1,\,3c+2\}\) are \(m\) disjoint zero-sum triples. If \(m=2k\) is even, let \(0\le a\le2k-2\), put \(b=a\) for \(a<k\), \(b=a+1\) for \(a\ge k\), and let \(c\equiv-a-b-1\pmod{2k}\). The first coordinates omit \(2k-1\), the second omit \(k\), and the third omit \(0\): the third coordinates run through odd residues and the nonzero even residues exactly once. These \(2k-1\) disjoint trisecants leave precisely the group elements \(6k-3\), \(3k+1\), and \(2\). Two additional rational lines cover them, realizing the sharp \(2k+1\) bound. This is an elementary constructive illustration of the general existence argument, not a claim of novelty for group near-transversals.

## Verification

The standalone exact-arithmetic script `verify.py` tests the explicit cyclic triples for every \(1\le m\le200\), their completeness and missing points, and the predicted group sum obstruction; it also enumerates rational points of specific smooth Weierstrass cubics in odd characteristic, checks their cardinalities, torsion counts, and the presence of the expected lines on the cubic. It is a finite consistency check only. The unbounded existence claim follows from the published Cayley-table near-transversal theorem and the group-theoretic proof above; the finite script does not replace either.

## Relationship to prior work

Asgarli--Dassarma--Ghioca--MacLean--Stokdyk (2026), in their introduction to the plane-curve line-covering problem, already discuss the elliptic chord--tangent reduction and cite Tannenbaum's \(N/3+O(1)\) bound for odd \(N\). Their main result is a large-field asymptotic upper bound, not the exact one-involution classification. Cichacz (2017 preprint) proves the 3-zero-sum-partition property for all finite abelian groups of order divisible by three except those with exactly one involution; this **already implies the zero-defect half** of the displayed formula. Goddyn--Halasz (2019 preprint; 2020 publication), Theorems 2 and 4, prove group near-transversal existence and characterize full transversals. Their statements concern Cayley tables, not minimum rational line covers of smooth plane cubics. The excess-one geometric deduction uses an index-three coset construction and a matching obstruction, and is the contribution asserted here.

## Limitations

This result applies only when \(3\mid\#E(\mathbb F_q)\) and the plane embedding has an \(\mathbb F_q\)-rational flex. It neither describes optimal covers up to projective equivalence nor determines the count of optimal covers, and it does not cover singular cubics or higher-degree plane curves. The deduction rests on Goddyn--Halasz's nontrivial theorem and is not an independent proof of that combinatorial result. A previously unpublished or unindexed application of group near-transversals to elliptic line covering is a residual priority risk; the result should not be interpreted as priority certification.

## References

1. S. Asgarli, S. Dassarma, D. Ghioca, S. MacLean, and E. Stokdyk, *Covering plane curves over finite fields with lines*, arXiv:2610.13042v1 (2026), especially Question 1.1, Theorem 1.2 and Introduction, page 3.
2. L. Goddyn and K. Halasz, *All group-based latin squares possess near transversals*, arXiv:1905.07071v2 (2019), Theorems 2 and 4; *Journal of Combinatorial Designs* 28 (2020), 358--365, doi:10.1002/jcd.21701.
3. S. Cichacz, *Zero sum partition into sets of the same order and its applications*, arXiv:1702.07859v1 (2017), Section 3, Lemma 11 and the 3-zero-sum partition theorem.
4. P. Tannenbaum, *Partitions of abelian groups into sets with zero sums*, *Congressus Numerantium* 33 (1981), 341--348, as cited in [1].
