# The two-generator degree-four resonance in free delta-mock-Novikov algebras

## Finding
Let \(K\) be any field of characteristic zero, let \(\delta\in K^\times\), and let \(F_\delta(x,y)\) be the free (nonunital, nonassociative) left \(\delta\)-mock-Novikov algebra on two generators. Its fourth homogeneous degree, with the fine grading recording occurrences of \(x\) and \(y\), has the following complete classification.

For \(\delta\ne -1\), its only nonzero fourth-degree bidegree is \((2,2)\), of dimension one, represented by \((y(xy))x\). For \(\delta=-1\), the fourth-degree bidegrees \((3,1),(2,2),(1,3)\) have dimensions \(1,2,1\), respectively. A basis at this exceptional value is
\[
(y(xx))x,\quad (y(xx))y,\quad (y(xy))x,\quad (y(xy))y.
\]
In particular,
\[
\dim_K F_\delta(x,y)_4=\begin{cases}1,&\delta\ne-1,\\4,&\delta=-1.\end{cases}
\]
The Hilbert-series prefix is \(2t+4t^2+4t^3+t^4\) away from \(\delta=-1\), but \(2t+4t^2+4t^3+4t^4\) at \(\delta=-1\). These equalities are **only statements through degree four**; no claim is made about higher degrees. The one-generator free algebra has zero third and fourth homogeneous degrees, so two generators are the smallest rank revealing this quartic resonance.

## Assumptions and scope
All products are bilinear and have degree equal to the sum of the degrees of their inputs, with no commutativity or associativity assumed. For every \(a,b,c\), the defining identities, in exactly the convention of Ruan--Normatov, are
\[
\delta\big((ab)c+(ba)c\big)+a(bc)+b(ac)=0,
\qquad (ab)c+(ac)b=0.
\]
They generate a homogeneous two-sided ideal in the free nonassociative algebra. We use left versions of the identities. The exception \(\delta=0\) is excluded from the definition and this theorem, even though some degree-four calculations may continue to hold there. The ground-field hypothesis is characteristic zero; no modular conclusion is asserted.

## Proof
**Completeness of the finite presentation.** Let \(W_4\) be the 80-dimensional free span of planar binary bracketings with four leaves labelled \(x\) or \(y\): five Catalan bracketings and 16 label assignments. A degree-four consequence of either defining cubic identity is a linear combination of (i) the identity multiplied on the left or right by a generator, or (ii) that identity with one of its three arguments replaced by a degree-two product of generators. This follows from degree considerations in the homogeneous ideal: a cubic relation can meet total degree four only by one binary multiplication or a single degree-two substitution. All occurrences are included, whether or not labels coincide.

Construct the \(160\)-row, \(80\)-column relation matrix \(M(\delta)\) by taking two cubic identities, all \(2^4\) assignments of four generators, and the five insertion choices just described. Repeated monomials within one relation are **added with multiplicity**, never overwritten. Define the column order: enumerate planar binary trees by splitting the first \(i\) leaves from the rest, with \(i=1,2,3\) in increasing order, recurse left then right, and label each tree using the lexicographic list of \((x,y)\)-words of length four with \(x=0\), \(y=1\). Number columns starting at zero; row order is the four-label lexicographic order, first identity followed by second, with right-multiplication, left-multiplication, and substitutions at arguments 1,2,3.

**Generic sharp rank.** Exact elimination over \(\mathbb Q(\delta)\) finds 79 pivot columns, all columns except 58. Selecting these pivot columns and the lexicographically determined pivot rows of the transpose of the same matrix produces a \(79\)-square minor of determinant
\[
-2^{41}\delta^{9}(\delta+1)^3.
\]
A polynomial nullvector with coordinate 58 equal to 1 proves the complementary upper rank bound. The nonzero coordinates, indexed from zero, are
\[
\begin{array}{r|rrrrrrrrr}
 i&3&5&6&9&10&12&21&22&25\\
 v_i&-\delta&\delta^2&-\delta(\delta-1)&-\delta(\delta-1)&\delta^2&-\delta&1-\delta&\delta-1&\delta-1\\
\hline
 i&26&35&38&41&44&53&54&57&58\\
 v_i&1-\delta&1&-1&-1&1&1&-1&-1&1
\end{array}
\]
with every unlisted coordinate zero. Direct substitution into each of the 160 rows yields zero as a polynomial in \(\delta\). In characteristic zero, for every \(\delta\notin\{0,-1\}\), the displayed minor is nonzero, so the rank is exactly 79. Because the free column is 58, the class of the corresponding monomial \((y(xy))x\) spans the quotient and is nonzero.

**Exceptional sharp rank.** Set \(\delta=-1\). Exact row reduction gives pivot columns all except 56, 57, 58, 59. The determinant of the square minor formed by these 76 pivot columns and the pivot rows of the transpose equals \(-2^{38}\), and thus its rank is at least 76. Four explicit kernel vectors, obtained by listing their nonzero \((\text{column},\text{coefficient})\) entries, are
\[
\begin{aligned}
&[(2,1),(4,-1),(34,1),(40,-1),(52,-1),(56,1)],\\
&[(5,-1),(6,1),(9,1),(12,-1),(21,-1),(22,1),(25,1),(26,-1),(38,1),(44,-1),(53,-1),(57,1)],\\
&[(3,1),(6,-1),(9,-1),(10,1),(21,1),(22,-1),(25,-1),(26,1),(35,1),(41,-1),(54,-1),(58,1)],\\
&[(11,1),(13,-1),(39,1),(45,-1),(55,-1),(59,1)].
\end{aligned}
\]
Their restriction to columns 56--59 is the identity matrix, so they are linearly independent; all four annihilate \(M(-1)\). Thus rank is at most 76 and hence exactly 76. The four free columns represent the four monomials in the stated basis. Their multidegrees are \((3,1),(2,2),(2,2),(1,3)\).

**Lower degrees and minimality.** Degrees one and two have dimensions two and four since the defining relations first appear in degree three. Degree three has four dimensions: for two generators, the second defining identity makes \((ab)c\) antisymmetric in the last two arguments, giving two independent left-associated classes. The first identity then determines the symmetric part of \(a(bc)\) in terms of those left-associated classes, leaving two independent antisymmetric right-associated classes. These four classes are independent because the defining cubic relation space has no relations mixing its two disjoint residual bases. For one generator, the right-anti-commutative identity with all arguments identical forces \((xx)x=0\), and then the first identity forces \(x(xx)=0\); all degree-three and degree-four products vanish, proving minimality of the two-generator witness.

## Verification
The accompanying standalone `code/verify.py` constructs every tree and identity from the defining equations, checks the polynomial nullvector and the four exceptional nullvectors, computes the two **exact** maximal-minor determinants, and checks the quartic bidegree profiles via exact rational row reduction at \(\delta=2\) and \(\delta=-1\). It prints `VERIFY_OK` upon success. The proof uses exact symbolic identities and nonzero integer-polynomial determinants; it does not infer an infinite-field theorem from sample computations. Reproduce using `python3 code/verify.py` with Python 3 and SymPy.

## Relationship to prior work
Ruan and Normatov (2026, arXiv:2609.06913v1), Definitions 2.1--2.2, introduce the identities; their Proposition 3.1 determines the arity-three operad size, while Lemma 3.3 determines **multilinear** arity-four dimensions 14 generally and 20 at \(\delta=-1\). Section 2 also computes a four-variable multidegree \((2,1,1)\) used for a Malcev identity. Those calculations are related but do not themselves specify the two-generator degree-four bidegree profile or an explicit rank-two quartic normal-form basis. The present statement is a non-multilinear quotient with coinciding generator labels, not a restatement of the total arity-four operad dimension. Prior classical Novikov, Ma-Novikov and Jacobi--Jordan results concern different defining operations/relations and do not supply this displayed rank-two basis directly.

## Limitations
This is the low-degree structural invariant of a newly introduced variety, not an all-degree Hilbert series, complete representation-theoretic description, or a claim that the full free algebra is finite-dimensional. The founding article contains closely related arity-four row reductions; an implicit consequence in its operadic computations or in earlier anti-Novikov literature remains a residual originality risk. The tests use a self-review only. No independent audit or external proof certification has been performed.

## References
1. J. Ruan and Z. Normatov, *\(\delta\)-Mock-Novikov Algebras: Structural Theory, Operad and Poisson-Type Constructions* (first posted 2026-09-07), arXiv:2609.06913v1, https://arxiv.org/abs/2609.06913.
2. I. Kaygorodov, A. Khudoyberdiyev and B. Sartayev, *A unified approach to the definition of anti-algebras* (2026), arXiv:2610.12479, https://arxiv.org/abs/2610.12479.
3. A. S. Dzhumadil'daev, *Codimension growth and non-Koszulity of Novikov operad*, Communications in Algebra 39 (2011), 2943--2952, https://doi.org/10.1080/00927870903386494.
