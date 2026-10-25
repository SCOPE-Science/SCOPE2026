# Catalan-leading polynomial census of three-chain bounded morphisms from rectangular Kripke grids

## Finding

For integers \(a,b\ge1\), let \(P_{a,b}=[a]\times[b]\) be the reflexive coordinatewise-order Kripke frame, with \([a]=\{0,\ldots,a-1\}\), and let \(C_3=\{0<1<2\}\) be the reflexive three-world chain. Write \(F_a(b)\) for the number of **surjective, labelled bounded morphisms** \(f:P_{a,b}\to C_3\); each map must be order preserving and satisfy
\[
 f(\uparrow x)=\uparrow f(x)\qquad(x\in P_{a,b}).
\]
Source and target worlds are individually distinguished; the count is not modulo automorphisms.

**Exact positive-binomial theorem.** There are nonnegative integers \(c_{a,m}\), defined explicitly below by finite comparisons of \(2a\) ranks and independent of \(b\), for which
\[
 \boxed{F_a(b)=\sum_{m=0}^{2a}c_{a,m}\binom{b-1}{m}\qquad(a,b\ge1).}
\]
As usual, \(\binom{b-1}{m}=0\) for \(m>b-1\). The top coefficient is the Catalan number
\[
 \boxed{c_{a,2a}=\frac1{a+1}\binom{2a}{a}.}
\]
Thus \(F_a(b)\) is an integer-valued polynomial of **exact degree** \(2a\), with
\[
 \boxed{F_a(b)=\frac{b^{2a}}{a!(a+1)!}+O_a(b^{2a-1}).}
\]
In particular, for every fixed positive width \(a\), asymptotically almost every globally surjective order-preserving map \(P_{a,b}\to C_3\) is a bounded morphism as \(b\to\infty\). This fixed-width statement does not assert the same limit for \(a\) growing with \(b\).

**First branching-width exact evaluation.** For the two-row grid, the coefficient vector is \((c_{2,0},\ldots,c_{2,4})=(0,3,9,7,2)\), giving
\[
 \boxed{F_2(b)=3\binom{b-1}{1}+9\binom{b-1}{2}+7\binom{b-1}{3}+2\binom{b-1}{4}
 =\frac{(b-1)(b^3+5b^2+10b-12)}{12}.}
\]
For comparison, its **surjective order-preserving** maps that fail the bounded-morphism back condition number precisely \(b(b^2-1)/3\). The counts for \(b=1,2,3,4,5,6\) are \(0,3,15,43,96,185\). The two-row grid is the least rectangular family with branching upper cones, making its explicit obstruction count a natural boundary test of the bounded-morphism condition.

## Assumptions and scope

The order on \(P_{a,b}\) is reflexive and coordinatewise, with the first coordinate indexing rows and increasing downward. A map is *bounded* if it preserves order and has the **upward back property**: for any \(x\) and any target world \(y\ge f(x)\), there exists \(z\ge x\) with \(f(z)=y\). Equivalently \(f(\uparrow x)=\uparrow f(x)\). Both chains have positive length; \(C_3\) always has three individually distinguished target worlds.

For a map into \(C_3\), let \(\ell_i\) be the number of zeros in source row \(i\), and let \(u_i\) be the number of entries at most one there, for \(1\le i\le a\). An order-preserving map is equivalent to a pair of weakly decreasing integer sequences satisfying
\[
 0\le \ell_i\le u_i\le b,\qquad
 \ell_i\ge\ell_{i+1},\quad u_i\ge u_{i+1}\quad(1\le i<a).
\]
The row then consists of \(\ell_i\) zeros, followed by \(u_i-\ell_i\) ones, followed by \(b-u_i\) twos.

Here is the promised explicit coefficient definition. For \(0\le m\le 2a\), let \(c_{a,m}\) be the number of pairs of integer tuples \((\ell_1,\ldots,\ell_a)\), \((u_1,\ldots,u_a)\) with entries in \(\{0,1,\ldots,m+1\}\) such that:

1. \(\ell_1>0\) and \(u_a<m+1\); the displayed monotonicity and rowwise inequalities hold with \(b=m+1\).
2. Every *interior rank* \(1,\ldots,m\) occurs at least once among these \(2a\) entries.
3. For each row \(1\le i\le a\) with \(\ell_i>0\) and either \(i=a\) or \(\ell_{i+1}<\ell_i\), one has
\[
 u_i>\ell_i\quad\text{or}\quad
 (i<a\ \text{and}\ u_{i+1}\ge\ell_i).
\]

This definition involves at most \(2a\) interior ranks, not \(b\)-dependent unknown coefficients. It is also an exact finite algorithm for the coefficients. Alternatively, for fixed \(b\), a transfer on the \(\binom{b+2}{2}\) row states \((\ell,u)\) with \(0\le\ell\le u\le b\), using the adjacent-row test in the proof, counts \(F_a(b)\) in \(O(ab^4)\) arithmetic operations and \(O(b^2)\) stored integers.

## Proof

**1. Reduction to two Ferrers boundaries.** Since a monotone map into a chain is nondecreasing along each source row, each row is of the form \(0^{\ell_i}1^{u_i-\ell_i}2^{b-u_i}\). Columnwise monotonicity is precisely the pair of weak-decrease constraints in the previous section. Surjectivity requires the minimum label zero at the least source world, meaning \(\ell_1>0\), and the maximum label two at the greatest source world, meaning \(u_a<b\), together with at least one label one. We will see that the back property automatically supplies a one when the first two inequalities hold.

**2. Exact local characterization of the back property.** For any zero-labelled source world, the greatest source world above it is labelled two. Therefore the only nonautomatic target required by the upward back property is label one above each zero-labelled world. Every zero lies below a maximal zero. Such a maximal zero exists at the end of row \(i\), at column \(\ell_i-1\), precisely when \(\ell_i>0\) and either \(i=a\) or \(\ell_{i+1}<\ell_i\). If a one lies anywhere above a maximal zero, a saturated coordinatewise path to that one must begin with a one: no further zero is above this maximal zero, and a path passing through label two cannot later reach label one by monotonicity. Conversely, a one at an immediate upper cover plainly witnesses the back property. The right cover is a one precisely when \(u_i>\ell_i\). The lower cover is a one precisely when \(i<a\) and \(u_{i+1}\ge\ell_i\). Thus the displayed local disjunction is **necessary and sufficient** for the upward back condition for every source world. If \(\ell_1>0\) and \(u_a<b\), a maximal zero exists, and this condition forces some label one; surjectivity follows. This proves the complete row-length normal form, with no unstated connectivity or genericity assumptions.

**3. Positive binomial expansion.** Form the weak order of the \(2a\) numbers \(\ell_i,u_i\), retaining which entries are exactly \(0\) or \(b\). Suppose exactly \(m\) distinct values lie strictly between \(0\) and \(b\). Their relative order and assignments to coordinates form exactly one object counted by \(c_{a,m}\), after relabelling the distinct values in increasing order by \(1,\ldots,m\) and the two endpoints by \(0,m+1\). Because the normal-form conditions refer *only* to comparisons and endpoint equality, this order standardization preserves and reflects validity. Conversely, choosing any increasing \(m\)-subset of \(\{1,\ldots,b-1\}\) and replacing ranks by its members gives one valid source map. These operations are inverse. There are \(\binom{b-1}{m}\) choices, proving the formula. No pattern has more than \(2a\) distinct interior values, giving the finite upper limit and nonnegative coefficients.

**4. Catalan top coefficient.** When \(m=2a\), all \(2a\) row-boundary lengths are pairwise distinct and lie strictly between the endpoints. In particular \(u_i>\ell_i\), so the back condition holds automatically. The only remaining restrictions are two chains of inequalities \(\ell_1>\cdots>\ell_a\) and \(u_1>\cdots>u_a\), with \(\ell_i<u_i\). Their linear extensions are ballot interleavings of two chains of length \(a\), with each \(\ell_i\) preceding its corresponding \(u_i\) in increasing-value order (equivalently, the Young-tableau count for a \(2\)-by-\(a\) rectangle). By the reflection principle, their number is
\[
 \binom{2a}{a}-\binom{2a}{a-1}=\frac{1}{a+1}\binom{2a}{a}.
\]
This strictly positive top coefficient gives degree \(2a\) and the stated leading term since \(\binom{b-1}{2a}=b^{2a}/(2a)!+O_a(b^{2a-1})\).

**5. Comparison with all monotone maps and asymptotic density.** All order-preserving maps \(P_{a,b}\to C_3\), without the back condition, correspond to height-at-most-two plane partitions in an \(a\)-by-\(b\) box. MacMahon's product formula specializes to
\[
 T(a,b)=\prod_{i=1}^{a}\prod_{j=1}^{b}\frac{i+j+1}{i+j-1}
 =\frac{1}{a+1}\binom{a+b}{a}\binom{a+b+1}{a}.
\]
The maps omitting any particular one of the three labels are in bijection with order ideals of \(P_{a,b}\), numbering \(\binom{a+b}{a}\). Inclusion-exclusion yields exactly
\[
 S(a,b)=T(a,b)-3\binom{a+b}{a}+3
\]
surjective monotone maps. For fixed \(a\), \(T(a,b)=b^{2a}/(a!(a+1)!)+O_a(b^{2a-1})\), and the omitted-label correction is \(O_a(b^a)\). Part 4 gives the same leading coefficient for \(F_a(b)\). Consequently \(F_a(b)/S(a,b)\to1\) as \(b\to\infty\), wherever the denominator is nonzero. The statement is **fixed-width only**; no diagonal-aspect-ratio assertion follows.

**6. The two-row census.** In the coefficient definition with \(a=2\), only the four entries \(\ell_1,\ell_2,u_1,u_2\) vary. Their two weak-decrease conditions, the rowwise comparisons, the endpoint constraints and the two local disjunctions give, on taking exactly \(m\) distinct interior values for \(m=0,1,2,3,4\), respectively \(0,3,9,7,2\) admissible weak-order patterns. This is a *finite*, exhaustive comparison classification: to reproduce it, enumerate \(\{0,\ldots,m+1\}^4\), require every interior rank and apply the five inequalities and local tests. The embedded program `verify.py` implements precisely this certificate separately from direct Kripke-world enumeration. Substitution into Part 3 gives the positive binomial expansion, and elementary expansion gives the factored quartic. Subtracting from \(S(2,b)\), using the closed formula in Part 5, gives the exactly cubic failure count \(b(b^2-1)/3\). This is an identity of polynomials, not a numerical extrapolation.

## Verification

The accompanying standard-library program `verify.py` implements four independent encodings: direct enumeration of all three-colour functions on small grids with explicit comparison of upward cones; enumeration of admissible row-length pairs; dynamic transfer between row states; and exhaustive weak-order patterns with \(m\le2a\). It checks the whole class of maps for the tested finite dimensions, confirms the polynomial expansion for fixed widths \(a=1,2,3\), verifies the Catalan top coefficient and the two-row quartic, and cross-checks grid transposition. Run `python verify.py`. The exact recorded output is in `verification_output.txt`. Finite verification does not replace Parts 1–6, which prove the unrestricted statements for every \(a,b\ge1\).

## Relationship to prior work

Bounded morphisms and their upward back condition are standard in Kripke semantics. Bezhanishvili, Coumans, van Gool and de Jongh (arXiv:1403.0710, originally 2014) develop model-theoretic p-morphisms and universal models; that work is not presented as counting these labelled grid-to-three-chain maps. Vuletić (arXiv:0707.0532v1, 2007) treats plane partition generating functions, of which the MacMahon count of arbitrary monotone three-colour grids is a classical special case. Neither the box enumeration nor general p-morphism semantics is new here. The contribution is the particular **back-conditioned** positive binomial census, its Catalan leading term and fixed-width density theorem, and the first branching-width exact obstruction formula. The all-monotone map count alone does not determine these numbers.

Related enumerative statements for bounded morphisms from Boolean inclusion lattices to \(C_3\), or from rectangular grids to the four-element Boolean diamond, concern different source or target posets. A product of two nontrivial chains is not a Boolean lattice of arbitrary rank; the three-chain target is not the four-element diamond. Neither type of formula specializes to the claim here. General weak-order source results likewise do not subsume a rectangular product-order grid. The novelty comparison is a best-knowledge one, not a proof of uniqueness across unindexed literature.

## Limitations

The exact positive-binomial coefficients are given by a finite weak-order classification; a simple closed expression for \(c_{a,m}\) at arbitrary \(a,m\) is not established. The dense-limit statement fixes \(a\); it cannot be extended to a growing-width regime on this evidence. Maps are labelled, reflexive and globally surjective. No result is claimed for non-reflexive frames, different target height, or quotienting maps by source automorphisms. A broader unindexed work on order-preserving open maps or plane partition restrictions could imply portions of this result; independent scholarly review is needed before a publication-priority claim.

## References

- N. Bezhanishvili, D. Coumans, S. J. van Gool and D. de Jongh, *Duality and universal models for the meet-implication fragment of IPC*, arXiv:1403.0710v1 (first posted 4 March 2014), particularly the definitions of Kripke p-morphisms and the sections on universal models and frame formulas.
- M. Vuletić, *A generalization of MacMahon's formula*, arXiv:0707.0532v1 (first posted 4 July 2007), introduction and plane-partition generating-function framework.
- The classical MacMahon boxed plane-partition product formula, used only for the unrestricted monotone-map comparator.
