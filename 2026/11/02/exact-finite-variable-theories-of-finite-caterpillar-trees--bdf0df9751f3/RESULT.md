# Exact finite-variable theories of finite caterpillar trees

## Finding

Work in the counting-free first-order language of equality and one irreflexive symmetric adjacency relation. Let \(\mathcal C\) be the class of all nonempty finite caterpillar trees (trees whose vertices of degree at least two induce a path, possibly empty). Let \(\equiv_{\mathrm{FO}^{k}}\) denote agreement on every first-order sentence using at most \(k\) reusable variable names, without a bound on quantifier depth.

**Theorem.** All members of \(\mathcal C\) have the same \(\mathrm{FO}^{1}\)-theory. The \(\mathrm{FO}^{2}\)-theories are exactly four: the singleton tree, the two-vertex tree, the stars with at least three vertices, and the nonstar caterpillar trees.

For \(k\ge3\), singleton and two-vertex trees form separate classes. Every other tree \(T\in\mathcal C\) has a canonical nonleaf spine of length \(m\ge1\) and a vector \(\mathbf b=(b_1,\ldots,b_m)\) of pendant-leaf counts along that spine. For \(m=1\), necessarily \(b_1\ge2\). For \(m\ge2\), the endpoints satisfy \(b_1,b_m\ge1\), while internal entries may be zero. Two such trees \(T(\mathbf b)\) and \(T(\mathbf c)\) are \(\mathrm{FO}^{k}\)-equivalent precisely when their spine lengths are equal and their clipped words

\[
(\min\{b_i,k\})_{i=1}^{m}
\quad\text{and}\quad
(\min\{c_i,k\})_{i=1}^{m}
\]

agree either directly or after reversal. No other identifications occur.

At fixed spine length \(m\), the exact number of theories for \(k\ge3\) is

\[
N_k(1)=k-1,\qquad
N_k(m)=\frac{k^2(k+1)^{m-2}+k(k+1)^{\lfloor(m-1)/2\rfloor}}2
\quad(m\ge2).
\]

Every equivalence class has a unique smallest representative, obtained by replacing each pendant-leaf count with its value clipped at \(k\) (the singleton and two-vertex classes remain unchanged). Every caterpillar of order at least three has *relative logical defining width* \(\max\{3,1+\max_i b_i\}\), where relative width means the least variable count defining its isomorphism type **among members of** \(\mathcal C\). The variable hierarchy is strict for every width \(k\ge1\).

## Assumptions and scope

The graphs are finite, simple, undirected, nonempty, and connected. A tree is a caterpillar here if deleting all degree-one vertices leaves a path, including a singleton or empty path. The two smallest trees are treated separately. For every tree with at least three vertices, the induced subgraph on degree-at-least-two vertices is a nonempty path and gives the unique canonical spine. Every vertex outside that spine is a degree-one leaf with exactly one spine neighbor; each spine vertex has \(b_i\) such neighbors. A path with two or more spine vertices has at least one pendant leaf at each spine endpoint; a one-vertex spine has at least two pendant leaves. The reversal of the spine is its only possible nontrivial orientation change.

This theorem concerns ordinary \(\mathrm{FO}^{k}\), **not** first-order logic with counting quantifiers. Quantifier depth is unrestricted. The theory counts \(N_k(m)\) are for a specified spine length; there are infinitely many distinct theories as \(m\) varies for each \(k\ge3\).

## Proof

**1. Canonical spine and low widths.** Let \(L(x)\) mean that \(x\) has exactly one neighbor; this is a three-variable formula:

\[
L(x):=\exists y\bigl(E(x,y)\wedge \forall z(E(x,z)\to z=y)\bigr).
\]

The predicate \(S(x):=\exists y\exists z(E(x,y)\wedge E(x,z)\wedge y\ne z)\) uses three variables and selects precisely the spine vertices of every caterpillar of order at least three. In a nonstar caterpillar there are at least two spine vertices, every vertex has at least one neighbor and at least one **distinct nonneighbor**, and no vertex is universal. In a star of order at least three there is a universal center, while the leaves are not universal. The singleton and edge are separately \(\mathrm{FO}^{2}\)-definable within the class. All stars of order at least three are mutually \(\mathrm{FO}^{2}\)-equivalent: maintain the center/leaf types in the two-pebble game. All nonstar caterpillars are mutually \(\mathrm{FO}^{2}\)-equivalent: when one pebble is fixed, each vertex on the other side offers the three necessary options (equal, distinct adjacent, distinct nonadjacent). The four cases are distinguished using two-variable statements of singleton size and the existence/allness of universal vertices. With one variable the only adjacency atom available is the always-false loop atom, so all these nonempty loopless graphs are equivalent.

**2. Three-variable access to the spine geometry.** The binary predicate \(A(x,y):=S(x)\wedge S(y)\wedge E(x,y)\) is in \(\mathrm{FO}^{3}\). For every fixed nonnegative integer \(d\), a formula \(P_d(x,y)\in\mathrm{FO}^{3}\) asserts an \(A\)-walk of length \(d\): start with \(P_0(x,y):=(x=y)\) on spine vertices and \(P_1=A\); use \(P_{a+b}(x,y):=\exists z(P_a(x,z)\wedge P_b(z,y))\), with the bound variable name in the two subformulas hygienically reused. The exact spine distance predicate \(D_d(x,y)\) says there is a walk of length \(d\) and none of a smaller length, so is also in \(\mathrm{FO}^{3}\). The unary predicate asserting that a spine vertex has at most one spine neighbor is in \(\mathrm{FO}^{3}\) and singles out the two path endpoints (or its unique vertex at length one). Since the spine is a path, every position \(i\) is uniquely determined by its distance \(i-1\) from a chosen endpoint.

**3. A sharp local leaf-count test using variable recycling.** For every \(k\ge3\) and \(1\le r\le k\), there is a unary \(\mathrm{FO}^{k}\)-formula \(B_r(x)\) stating that \(x\) has at least \(r\) pendant-leaf neighbors. For \(r<k\), name \(r\) distinct leaf neighbors while holding \(x\); this uses at most \(r+1\le k\) names. To express \(B_k(x_0)\) with only \(k\) names \(x_0,x_1,\ldots,x_{k-1}\), first choose \(k-1\) distinct leaf neighbors \(x_1,\ldots,x_{k-1}\) of the free vertex \(x_0\). Then rebind \(x_0\) as another leaf, require it distinct from all stored leaves, and finally rebind \(x_{k-1}\) to a common neighbor of the new \(x_0\) and the stored \(x_1\). Since \(x_1\) is a leaf, that common neighbor must be the original spine vertex, so the new leaf is its \(k\)th distinct pendant neighbor. Every subformula \(L(x_i)\) uses at most three names and may locally shadow other names without changing their values outside its scope. Explicitly, the final nested part is

\[
\exists x_0\left(L(x_0)\wedge\bigwedge_{i=1}^{k-1}x_0\ne x_i
\wedge\exists x_{k-1}(E(x_{k-1},x_0)\wedge E(x_{k-1},x_1))\right).
\]

Conversely any satisfying assignment yields \(k\) distinct leaf neighbors of the original center. Thus the formulas \(B_j\wedge\neg B_{j+1}\) for \(0\le j<k\) (where \(B_0\) is tautological), and \(B_k\), recognize exactly the clipped count \(\min(b_i,k)\) at any spine vertex.

**4. Necessity.** For a given spine length \(m\) and clipped word \(\mathbf a\), existentially choose a spine endpoint \(x\). For each position \(i\), demand that the unique spine vertex at distance \(i-1\) from \(x\) have the unary clipped-count type \(a_i\); demand a spine vertex at distance \(m-1\) but none at distance \(m\). This is a sentence of \(\mathrm{FO}^{k}\): distance has at most two free variables and uses a third temporarily; the local count has one free variable and at most \(k\) names, and can shadow the endpoint name inside its own scope. It holds exactly when the clipped word is \(\mathbf a\) or its reversal. Hence differing spine lengths or clipped reversal classes are distinguished at width \(k\).

**5. Sufficiency.** Fix an isomorphism between two spines (identity or reversal) aligning equal clipped counts. In the unrestricted \(k\)-pebble game, match every pebbled spine vertex by this fixed isomorphism. In each pendant-leaf fiber, keep a bijection between currently pebbled distinct leaves. If the fiber sizes are below \(k\), they agree exactly. If both are at least \(k\), at most \(k-1\) other pebbles occupy that fiber before a new placement, so an unused corresponding leaf is always available. Maintain equality and adjacency on every move indefinitely. This wins all finite rounds and proves \(\mathrm{FO}^{k}\)-equivalence for unbounded quantifier depth.

**6. Counts, representatives and strictness.** For \(m=1\), the allowed clipped values are \(2,\ldots,k\), giving \(k-1\) theories. For \(m\ge2\), endpoints have \(k\) possible clipped values \(1,\ldots,k\), and each of \(m-2\) internal positions has \(k+1\) values \(0,\ldots,k\). The number of words is \(k^2(k+1)^{m-2}\). Reversal fixes exactly \(k(k+1)^{\lfloor(m-1)/2\rfloor}\) palindromes. Burnside's lemma gives the displayed count. Replacing each count by its clip minimizes total vertices independently at each spine position and is uniquely determined modulo reversal. Any \(k\ge3\) fails to distinguish a caterpillar from one in which a spine leaf count of \(k\) is raised to \(k+1\), while width \(k+1\) distinguishes them. For the first two boundaries, a singleton versus an edge witnesses width one versus two, and two nonisomorphic nonstar caterpillars, such as \(P_4\) and \(P_5\), witness width two versus three. The class-relative defining width is therefore \(\max\{3,1+\max_i b_i\}\) for any tree of order at least three.

## Verification

The package contains two standalone Python 3 programs requiring only the standard library. Run `python3 verification/verify_fo.py` to compute the stable atomic-type/extension-set partition of the full \(k\)-pebble game on a finite sample, without relying on the classification formula for refinement. It checks 70 small caterpillars at widths two and three (2,415 graph pairs at each width), and a 15-graph width-four sample (105 pairs): 4,935 pairwise predictions passed. The code starts from ordered \(k\)-tuple atomic types, repeatedly refines by the sets of colors obtainable by replacing each coordinate, and stops when no new classes split. For finite models this is an exact calculation of unrestricted-depth \(k\)-variable equivalence for the inspected models.

Run `python3 verification/verify_structure.py` to verify 3,203 canonical caterpillar examples, 45,180 local leaf-threshold configurations, and 15 independent orbit-enumeration comparisons. Both command outputs are embedded in `verification/fo_output.txt` and `verification/structure_output.txt`. Their exact replay is not evidence for all sizes or widths: the universal proof is the argument above. These scripts do not check publication priority.

## Relationship to prior work

Pikhurko and Verbitsky's *Logical complexity of graphs: a survey* (first public arXiv posting 2010-03-25, arXiv:1003.4865), Section 5.1.1, gives the general bound \(W(T)\le\Delta(T)+1\) for individual trees and the sharp example \(W(K_{1,m})=m+1\). It does not state the entire restricted \(\mathrm{FO}^{k}\)-equivalence spectrum of caterpillar trees, nor the exact orbit counts and minimum representatives. The 1987/1989 work of Immerman and Kozen studies bounded-variable properties of rooted tree **ancestry** structures, often at bounded degree, with different signatures and quantification over all models. Its finite-model results and sibling technique are relevant but do not imply the present pure adjacency classification with arbitrarily large leaf fibers.

Prior results for rooted homogeneous ancestry trees and leaf-covered **directed unicyclic** structures establish other clipped multiplicity classifications; the present statement covers **all** finite undirected caterpillars, including internal spine vertices with zero pendant neighbors and the reversal symmetry of an unoriented path. Neither source family includes these graphs under its specified signature and hypotheses. An unlocated general composition theorem for finite-variable logic on tree decompositions might imply the result; priority remains qualified.

## Limitations

Only the ordinary adjacency signature without counting quantifiers is covered. Theory counts are relative to the class of caterpillar trees, not counts over all finite graphs, and the defining width in the theorem is relative to that class. This does not classify arbitrary trees, forests, caterpillars with additional marks/orders, graphs with cycles, or counting logics. The computational examples are finite and not a proof of all cases. The literature comparison is not an exhaustive historical priority certificate, and independent mathematical auditing has not been performed.

## References

1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865, first posted 2010-03-25; especially Section 5.1.1. https://arxiv.org/abs/1003.4865
2. N. Immerman and D. Kozen, *Definability with Bounded Number of Bound Variables*, Logic in Computer Science 1987; expanded in *Information and Computation* 83 (1989), 121–139, DOI 10.1016/0890-5401(89)90055-2. Author-hosted full text: https://www.cs.cornell.edu/~kozen/Papers/bbv.pdf
3. R. E. Jamison, F. R. McMorris and H. M. Mulder, *Graphs with only caterpillars as spanning trees*, *Discrete Mathematics* 272 (2003), 81–95, DOI 10.1016/S0012-365X(03)00186-9. This is structural graph background, not a claimed logical-classification source.
