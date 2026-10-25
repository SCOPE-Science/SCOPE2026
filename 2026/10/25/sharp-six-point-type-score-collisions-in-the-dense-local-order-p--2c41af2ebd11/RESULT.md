# Sharp six-point type-score collisions in the dense local order, persisting at every order

## Finding
Let \(D\) be the countable homogeneous dense local order, whose finite induced tournaments are precisely the locally transitive tournaments. A tournament is **locally transitive** if, at every vertex, the out-neighborhood and in-neighborhood induce transitive tournaments. For a finite individually named induced tournament \(T\) on \(n\ge1\) vertices, let \(E_T(z)\) be the polynomial summing \(z^k\) over complete nonalgebraic one-types whose realizations beat exactly \(k\) vertices of \(T\). Write \(s_T(v)\) for the outdegree of \(v\) in \(T\).

The established type-score identity is
\[
E_T(z)=(1+z)\sum_{v\in T}z^{s_T(v)}.
\]
Thus equality of type-score polynomials is equivalent to equality of score multisets. The new conclusions are: **(i)** for \(n\le5\) this polynomial distinguishes isomorphism classes; **(ii)** at \(n=6\), there are six locally transitive isomorphism classes and exactly four score-polynomial fibers. Precisely two size-two fibers have sorted scores \((1,2,2,3,3,4)\) and \((2,2,2,3,3,3)\), and the other two fibers are singletons; **(iii)** at every \(n\ge6\), nonisomorphic locally transitive tournaments share the entire polynomial. An explicit pair at order \(n\) is distinguished by having respectively \(2(n-5)\) and zero induced regular five-vertex subtournaments.

## Assumptions and scope
All tournaments are finite, loopless, complete directed graphs with exactly one arc on each unordered vertex pair; isomorphism preserves arcs. Every parameter vertex is named individually. A nonalgebraic one-type is the orbit of one fresh point under the pointwise stabilizer, not an arbitrary formal arc pattern. A regular five-vertex subtournament is an induced five-vertex tournament in which each vertex has outdegree two. The claimed six-point threshold is restricted to the locally transitive age; it is not a classification of arbitrary finite tournaments.

## Proof
**Known one-type reduction.** The circular antipodal representation of a locally transitive tournament places \(n\) points and their antipodes in circular order. The \(2n\) open gaps encode the distinct nonalgebraic one-types in the homogeneous dense local order; the new point's number of outgoing arcs is a gap statistic. At the original-point boundaries these statistics are the existing outdegrees; at antipodal boundaries they are their complements. The locally transitive score symmetry \(s_i+s_{n+1-i}=n-1\) converts the complementary multiset into a shift by one, yielding the displayed type-score identity (see Brouwer and Belkillani). In particular, computing the score multiset suffices to compare the polynomials.

**Exact six-point threshold.** Enumerate every labeled tournament on \(n\) vertices by its \(\binom n2\) arc-direction bits, for each \(1\le n\le6\). For each vertex test transitivity of the induced in- and out-neighborhoods by checking that their internal sorted outdegrees are exactly \(0,1,\ldots,k-1\): a tournament has these scores exactly when it is transitive, by the usual induction on the unique zero-score vertex. Group locally transitive tournaments by sorted global outdegrees, then identify isomorphism classes within each group by all degree-preserving permutations of vertex labels. These finite exhaustive loops are included in `verify_dense_local.py`, which has no randomized or oracle steps. For \(n=1,2,3,4,5,6\), the respective numbers of isomorphism classes are \(1,1,2,2,4,6\), and the numbers of distinct score multisets are \(1,1,2,2,4,4\). At six vertices the complete list of sorted scores and class multiplicities is
\[
(0,1,2,3,4,5):1;\quad (1,1,2,3,4,4):1;\quad (1,2,2,3,3,4):2;\quad (2,2,2,3,3,3):2.
\]
This is an exhaustive finite classification: the loops cover all \(2^{\binom n2}\) labeled arc assignments, and all possible vertex relabelings are tested when forming isomorphism classes.

**Explicit six-point witnesses.** Index vertices by \(0,1,\ldots,5\) and encode each out-neighborhood by a bitmask, with bit \(j\) set when the row vertex beats vertex \(j\). Define
\[
A=(14,28,56,48,33,3),\qquad B=(14,12,56,48,35,3).
\]
Both have sorted scores \((2,2,2,3,3,3)\); direct neighborhood checks establish local transitivity. In \(A\), precisely the five-sets \(\{0,1,2,4,5\}\) and \(\{0,1,3,4,5\}\) induce regular tournaments; in \(B\) none does. They are therefore nonisomorphic. Both have the identical type-score polynomial
\[
E_A(z)=E_B(z)=3z^2+6z^3+3z^4.
\]

**Infinite family by transitive substitution.** Fix \(h\ge1\). Replace vertex \(1\) of \(A\) by a transitive \(h\)-vertex chain, and replace vertex \(0\) of \(B\) by a transitive \(h\)-vertex chain. Orient all arcs between each chain and an original outside vertex uniformly according to the old arc. Call these new tournaments \(A_h\) and \(B_h\); both have \(h+5\) vertices. Transitive substitution preserves local transitivity: for any old vertex its in- and out-neighborhoods were transitive and substituting a chain for one member of an induced transitive neighborhood remains transitive; for a new chain vertex its in- and out-neighborhoods are a chain segment joined to a fixed transitive outside neighborhood in a single coherent order.

Each replaced vertex has score three and has exactly two outside in-neighbors with scores \(2\) and \(3\) in its respective original tournament. Hence the other three outside vertices have unchanged scores \(2,2,3\), the two in-neighbors' scores become \(h+1,h+2\), and the chain's scores are \(3,4,\ldots,h+2\). Both resulting tournaments therefore have the same sorted score multiset
\[
\{2,2,3,h+1,h+2\}\uplus\{3,4,\ldots,h+2\}.
\]
By the type-score identity their complete weighted nonalgebraic one-type polynomials agree.

A regular five-vertex subtournament cannot contain two points from one substituted transitive chain: those two vertices see every outside vertex in the selected set identically, while their internal chain outdegrees differ, contradicting their equal required degree two. Therefore each regular-five subtournament in \(A_h\) or \(B_h\) selects at most one replacement vertex and projects to a regular-five subtournament of the corresponding six-vertex source. Both such five-sets of \(A\) contain vertex \(1\), giving exactly \(2h\) lifts. Since \(B\) has none, \(B_h\) has none. Thus \(A_h\) and \(B_h\) are nonisomorphic for every \(h\ge1\), proving the asserted all-order collision.

## Verification
Run `python3 verify_dense_local.py` in a Python 3.10+ environment without third-party packages. The checker enumerates every labeled tournament for orders one through six; verifies local transitivity, degree-fiber classifications and pairwise isomorphism; separately enumerates all one-point extensions of the concrete witnesses; and verifies the transitive-substitution families through replacement-chain size twelve. Its preserved output is `verify_dense_local.out`, ending in `ALL_CHECKS_PASS`. The finite enumeration is the exhaustive proof of the sharp small-order claim; the infinite statement rests on the substitution and five-subtournament arguments above, not on finite experiments.

## Relationship to prior work
Brouwer established enumeration and circular representations for locally transitive tournaments. Belkillani characterized possible score sequences, their symmetry, and methods to construct tournaments realizing them. Coregliano develops structural descriptions of locally transitive tournaments. The type-score transform itself was known previously. The asserted new contribution is the sharp first failure of recovery, the complete order-six numerical fibers, and the explicit nonisomorphic collisions at **every** larger order with an independent regular-five separator. A general recipe for realizing score lists does not, without a further fiber analysis, specify this six-vertex boundary or the uniform infinite witnesses.

## Limitations
This is a self-reviewed mathematical claim, not independently audited or published. Belkillani's realization theorems are a material potential source of implicit overlap; the full primary article was inspected, but unlocated earlier exact score-fiber results remain possible. The type-score polynomial is strictly weaker than the complete isomorphism type. Explicit finite verification of the infinite family covers only stated finite values; unrestricted validity uses the proof. No claim is made about higher-arity type distributions or the uniqueness of score fibers above six vertices.

## References
- A. E. Brouwer, *The Enumeration of Locally Transitive Tournaments*, Mathematisch Centrum report ZW 138/80 (1980), https://ir.cwi.nl/pub/6805/6805D.pdf.
- A. Belkillani, *Scores des Tournois Localement Transitifs*, Ars Combinatoria **117** (2014), 75–83, https://combinatorialpress.com/article/ars/Volume%20117/volume-117-paper-6.pdf.
- L. Coregliano, *Quasi-Carousel Tournaments*, arXiv:1503.04124 (2015), https://arxiv.org/abs/1503.04124.
