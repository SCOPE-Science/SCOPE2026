# Sharp failure of path maximality for bounded morphisms to two- and three-world chains

## Finding

Among all rooted trees on \(n\) vertices, the end-rooted path maximizes the number of bounded morphisms to the reflexive two-world chain exactly for \(n\le5\), and to the reflexive three-world chain exactly for \(n\le6\). Maps need not be globally onto. The first two-world failure, at \(n=6\), has a unique maximizing rooted shape: a root with path branches of orders 2 and 3 (7 maps versus 6 for the path). The first three-world failure, at \(n=7\), likewise has a unique maximizing shape: a root with two path branches of order 3 (25 maps versus 22 for the path).

The following explicit witnesses beat the path at every order past the corresponding cutoff. For the two-world target use \(k-r\) path branches of order 2 and \(r\) of order 3, with \(k\ge2\), \(r\in\{0,1\}\) and \(n=2k+1+r\ge6\); the count is \(1+2^{k-r}3^r\). For the three-world target use \(k-r\) path branches of order 3 and \(r\) of order 4, with \(k\ge2\), \(r\in\{0,1,2\}\) and \(n=3k+1+r\); the count is \(4^{k-r}7^r+3^{k-r}4^r\). Thus explicit branching families have exponential counts at every sufficiently large order, in contrast to the linear and quadratic path counts.

## Definitions and counting tools

Each source tree is nonempty with reflexive ancestor order, and the target \(C_j=\{0,\ldots,j-1\}\) has its usual reflexive order. A map is a bounded morphism if it is order-preserving and, for each source vertex \(x\), every \(a\ge f(x)\) is \(f(y)\) for some descendant \(y\) of \(x\) (possibly \(x\) itself). Different vertex functions are counted separately. Rooted shape means isomorphism class as an unordered rooted tree.

Write \(F_j(T)\) for the number of maps into \(C_j\). The earlier exact recurrence for surjective bounded morphisms between arbitrary finite rooted tree frames [1] already gives these numbers: the image is the unique suffix of \(C_j\) beginning at the root image, so \(F_j(T)=\sum_{a=1}^j N(T,C_a)\), where \(N\) counts the onto maps. The following chain specialization is recalled for use in the extremal argument, not asserted as a new counting theorem.

A leaf must map to the top, so \(F_2=F_3=1\) at order one. For a root with a nonempty family of child subtrees \(T_i\),
\[
 F_2(T)=1+\prod_iF_2(T_i),\qquad
 F_3(T)=\prod_iF_3(T_i)+\prod_iF_2(T_i).
\]
In the two-world case the top root image gives one map and the bottom one allows arbitrary child maps, since each already hits the top. In the three-world case the top root image gives one map, the middle image allows arbitrary child maps into the two-world suffix, and the bottom image allows arbitrary three-world child maps except when they are all constantly top: that is the only way they can collectively miss the middle. Indeed, a child image containing the bottom also contains the middle by back. This verifies the chain formulas directly and also explains the subtraction of one in the bottom-root case of the general recurrence.

The path counts are \(F_2(P_n)=n\) and \(F_3(P_n)=1+\binom n2\) by iterating the unary-root formula. For comparison, the unique minimum for either target at each order \(n\ge2\) is 2, attained by the rooted star. When some child is internal, its two counts are at least 2, forcing the respective counts at the root to be at least 3 and 4.

## Proof of the extremal cutoffs

For orders 1 through 7, the numbers of rooted shapes are \(1,1,2,4,9,20,48\) and the pairs of separate maxima are
\[
(1,1),(2,2),(3,4),(4,7),(5,11),(7,16),(10,25).
\]
For an exhaustive finite calculation one can give the root label 0 and each other vertex \(i\) a parent in \(\{0,\ldots,i-1\}\). Every rooted tree permits such a labelling by ordering vertices by distance from the root. The canonical string for a vertex is an open parenthesis, the sorted concatenation of its children's strings, and a closing parenthesis. This is an injective representation of rooted shapes: parsing the balanced string recovers the multiset of child strings, and induction recovers the shape. Deduplicating these strings therefore gives exactly the required set of shapes. Enumerating each vertex function to the target, checking that the labels in each inclusive descendant set consist exactly of the suffix beginning at the vertex's label, gives the displayed table. At order 6 the unique two-world winner has path branches of orders 2 and 3; at order 7 the unique three-world winner has two path branches of order 3. The supplied `check_cutoffs.py` implements this enumeration and checks both the table and these shapes directly. Comparing with the path values proves the sharp small-order statements.

For the first witness family the root formula multiplies the branch counts 2 and 3 and adds 1. With \(r=1\) the base case is \(7>6\); with \(r=0\) it is \(9>7\). Increasing \(k\) adds 2 vertices and replaces the count \(c\) by \(2c-1\). If the current count exceeds \(n\), the new count exceeds \(2n-1\ge n+2\) for these orders. This proves failure at every order starting at 6.

For the second family the branch counts for \((C_2,C_3)\) are \((3,4)\) and \((4,7)\). The two products in the root recurrence yield the stated formula. The three base comparisons are \(25>22,40>29,65>37\), for \(n=7,8,9\). Increasing \(k\) adds 3 vertices and at least triples the witness count. For \(p(n)=1+\binom n2\), \(3p(n)-p(n+3)=n^2-4n-1>0\) for \(n\ge7\), so the strict comparisons persist. The closed witness formulas imply exponential growth in both cases. They do not identify the globally maximizing shapes at later orders.

## Relationship to prior work and scope

The exact enumeration for a fixed source tree follows by specialization and summation from [1]. General enumeration can also produce the small finite table once the rooted shapes are supplied; the contribution here is the extremal cutoff with its first maximizing shapes and explicit exponential witnesses at every later order. The counts are not counts of all monotone maps, which lack the back condition, nor are they counts only of onto maps. A two-world map is equivalently an ancestor ideal avoiding all leaves. For three worlds, the two lower-level ideals are nested, and each vertex of the smaller ideal must have a descendant in the difference; this is an additional restriction beyond counting arbitrary nested ideals.

This result concerns only the two indicated chain targets and does not classify maximizers beyond the first failure for each. The original shape checker and the direct labelled-parent enumeration establish only the finite cases; the formulas and inequalities above establish the unbounded families.

## References

1. *Exact bounded-morphism counting between arbitrary finite rooted tree frames*, Resultary, 2026-10-18, [Finding and recurrence](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-exact-bounded-morphism-counting-between-arbitrary-finite-rooted--e532142d4dde/RESULT.md).
2. V. Goranko and M. Otto, *Model Theory of Modal Logic*, in *Handbook of Modal Logic* (2007), §2.2, for the forth/back definition.
