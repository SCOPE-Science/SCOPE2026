# Maximal skew-line systems of the Fermat quartic: geometric and arithmetic orbit classification

## Finding
Let \(X\subset\mathbb P^3_{\mathbb Q}\) be the smooth quartic
\[
x_0^4+x_1^4+x_2^4+x_3^4=0.
\]
Among its \(48\) geometric lines, there are exactly \(128\) unordered sets of \(12\) pairwise skew lines, and no skew-line set has more than \(12\) members. The full geometric projective automorphism group of order \(1536\) has exactly two orbits of these systems, of cardinalities \(32\) and \(96\), whose stabilizers have orders \(48\) and \(16\), respectively.

Every individual geometric line requires the cyclotomic field \(K=\mathbb Q(\zeta_8)\) for its definition, yet every **unordered configuration** of twelve lines is defined over \(\mathbb Q(i)\). Precisely \(16\) configurations descend further to \(\mathbb Q\); each of the other \(112\) has minimal configuration field \(\mathbb Q(i)\). The Galois orbit profile on the \(128\) sets is therefore \(1^{16}2^{56}\). Here defining a set means defining its reduced union or its unordered collection, not defining each line separately.

## Assumptions and scope
Everything is over characteristic zero. Choose \(\zeta_8\) with \(\zeta_8^4=-1\), and write the three partitions of coordinate indices into pairs as
\[
((0,1),(2,3)),\quad ((0,2),(1,3)),\quad ((0,3),(1,2)).
\]
For each partition, each of the sixteen ordered pairs \((r,s)\in\{1,3,5,7\}^2\) gives a line whose two equations are \(x_a=\zeta_8^r x_b\) and \(x_c=\zeta_8^s x_d\), for the listed coordinate pairs \((a,b),(c,d)\). These comprise all \(48\) geometric lines by the cited Fermat-line classification. A *system* means an unordered subset of maximum cardinality twelve consisting of pairwise disjoint lines.

The source article typically uses a different sign model of the Fermat quartic. Its **geometric** assertions transfer after base extension, but its arithmetic Galois action must not be identified with that of the all-plus \(\mathbb Q\)-model without computation; the arithmetic claims here refer only to the displayed all-plus model.

## Proof
**Maximum and finite reduction.** Fix one of the three coordinate-pair families. Two lines with the same first exponent \(r\) intersect, since both lie in one coordinate-ratio plane. Thus a skew family contains at most four lines of each family, and a complete skew set has at most \(3\cdot4=12\) lines. Within one family, four pairwise skew lines must use all four first exponents and all four second exponents exactly once. There are precisely \(4!=24\) possible four-line sets in each of three families.

**Exact skewness predicate.** Encode each line by its two homogeneous linear equations in four variables. Two lines are skew exactly if the corresponding four-by-four coefficient matrix has nonzero determinant in \(\mathbb Q(\zeta_8)\). The provided verifier evaluates these determinants, without floating-point approximation, in \(\mathbb Z[t]/(t^4+1)\) for every one of the \(\binom{48}{2}=1128\) distinct line pairs. An independent reduction \(t\mapsto2\) in \(\mathbb F_{17}\), followed by row reduction, agrees for every pair. The exact predicate exhaustively tests the \(24^3=13824\) triples of four-line candidates; the complete set of compatible triples has cardinality \(128\). It explicitly lists representatives, so twelve is attained. Each of the \(48\) lines belongs to exactly \(32\) systems, giving the independent count \(128\cdot12=48\cdot32\).

**Complete projective symmetry.** The projective Hessian discriminant of the quartic is a nonzero scalar times \(x_0^2x_1^2x_2^2x_3^2\). Every projective automorphism therefore permutes the four coordinate hyperplanes and is monomial. Preserving the quartic forces its diagonal entries to have equal fourth powers. After quotienting common projective scalars, its full group is \((\mu_4^4/\mu_4)\rtimes S_4\), with order \(4^3\cdot24=1536\). Three independent coordinate multiplications by \(i\) and three adjacent coordinate transpositions generate this group. The verifier applies all six generators to the \(128\) systems and computes **exactly two complete orbits**, of sizes \(32\) and \(96\); orbit–stabilizer yields the claimed stabilizer orders.

**Arithmetic descent.** Every line equation includes a primitive eighth-root coordinate ratio, so every individual line has minimal field \(K=\mathbb Q(\zeta_8)\). The four Galois automorphisms of \(K/\mathbb Q\) act by \(\zeta_8\mapsto\zeta_8^k\) for \(k\in\{1,3,5,7\}\). The verifier evaluates their permutations on all \(48\) lines and \(128\) unordered twelve-line systems. Their respective system fixed-point counts are \(128,16,128,16\). Consequently the involution with \(k=5\) fixes *every* system, and its fixed field is \(\mathbb Q(i)\). The \(16\) systems fixed by the entire Galois group descend to \(\mathbb Q\); the other \(112\) have stabilizer precisely \(\{1,5\}\), so their minimal configuration field is exactly \(\mathbb Q(i)\). The orbit profile follows.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. It uses only the standard library and no external data files. It deterministically recomputes the line list, all exact determinants, the independent modular rank cross-check, the \(24^3\) candidate census, both projective orbits, all four Galois actions, and field-descent counts. A successful execution prints `VERIFY_OK` along with the numerical assertions. The source directly encodes every determinant, loop bound, and group generator; no previously generated logs or tables are required. It also checks that pairwise intersections between distinct systems have histogram \(\{0:4160,2:384,4:960,6:1280,8:960,10:384\}\).

## Relationship to prior work
Andria, Rojas and Mangueira classify the Fermat-line families and prove that the maximum number of mutually skew lines on the degree-four Fermat surface is \(12\). Their cited theorem establishes the **maximum size** and witnesses, not the enumeration of all maximum sets, its complete projective orbit decomposition, or the arithmetic descent of unordered systems in this \(\mathbb Q\)-model. The \(48\)-line construction and the degree-four skew bound are credited, not claimed as new. Schütt, Shioda and van Luijk study Fermat-surface lines and their Néron–Severi generation rather than this enumeration. Brosowsky and collaborators classify maximal skew sets on a **Hermitian quartic in characteristic three**, with \(112\) lines, so their different-incidence census does not imply the present characteristic-zero \(48\)-line count.

## Limitations
This result concerns the specified all-plus quartic and its complete maximum-cardinality twelve-line systems, not arbitrary maximal-by-inclusion subsets or all Fermat quartics over number fields. Field descent applies to each unordered reduced union, not to an individual constituent line. Exact symbolic enumeration establishes the finite assertions; it does not classify skew systems on other quartics or assert a uniform family theorem. Independent external audit has not been performed. Potential unindexed historical enumerations remain a bibliographic residual risk.

## References
- S. Andria, J. Rojas and W. Mangueira, *Maximal number of skew lines on Fermat surfaces*, arXiv:2403.15666, first submitted 2024-03-23; *Portugaliae Mathematica* 83, DOI:10.4171/PM/2150.
- M. Schütt, T. Shioda and R. van Luijk, *Lines on Fermat surfaces*, arXiv:0812.2377.
- L. Brosowsky and collaborators, *Maximal skew sets of lines on a Hermitian surface and a modified Bron–Kerbosch algorithm*, arXiv:2211.16580.
