# Sharp ten-vertex period cutoff for sequential bi-threshold dynamics on trees

## Finding
For a finite simple tree \(T\), write \(L(T)\) for the largest primitive period of its asynchronous bi-threshold dynamical system with uniform thresholds \((k^{\uparrow},k^{\downarrow})=(1,3)\), where each vertex is updated once in a fixed permutation each round. Then the exact maxima
\[
M(n)=\max_{|V(T)|=n}L(T),\qquad 1\le n\le10,
\]
are
\[
(M(1),\ldots,M(10))=(1,1,1,1,2,3,6,10,14,22).
\]
The numbers of unlabelled trees realizing these maxima are
\[
(1,1,1,2,1,1,2,1,1,1).
\]
In particular, the ten-vertex extremizer is unique up to graph isomorphism and carries exactly **two distinct primitive cycles of length \(22\)**. Thus ten is the smallest vertex count in the proved range for which \(M(n)>2n\).

One labelled representative of the extremal tree has vertex set \(\{0,1,\ldots,9\}\) and edge set
\[
\{(0,1),(0,2),(0,7),(1,3),(1,8),(2,4),(2,6),(3,5),(4,9)\}.
\]
For increasing-label updates, a period-\(22\) orbit is encoded by the successive state bitmasks
\[
(2,725,319,207,791,255,271,131,597,20,495,543,471,47,395,599,149,367,671,343,175,267).
\]
Here mask bit \(i\) is the state at vertex \(i\); the next mask after \(267\) is \(2\).

## Assumptions and scope
Every tree is finite, simple, connected and unlabelled for enumeration. The local rule at vertex \(v\) uses the states in its **closed** neighborhood immediately before its update. When the old state is zero, it becomes one if at least one vertex in that closed neighborhood is one. When the old state is one, it remains one only if at least three vertices in that closed neighborhood are one. Equivalently, for \(s_v=\sum_{u\sim v}x_u\), the new state is one exactly when \(s_v\ge x_v+1\). All vertices share these thresholds. A round is one full, fixed permutation sweep; the primitive period is measured in such rounds, not individual vertex updates.

## Proof
**Reduction to one update order.** For any fixed tree and any collection of fixed vertex local functions, all permutation sweeps are cycle-equivalent: their periodic phase spaces are in bijection preserving the orbit periods. This is the tree case of the update-order cycle-equivalence result quoted in [1, Section 4.2] and explicitly used in [2, Results]. Hence it suffices to evaluate the increasing-label sweep for each unlabelled tree. This reduction is about periodic orbit structure only; transient trajectories and labelled states need not agree.

**Exhaustive list of tree shapes.** The supplied `verify.py` begins at the one-vertex tree. For each order \(n\ge2\), it adds a leaf to every vertex of each representative from order \(n-1\). Every unlabelled tree has a leaf, so deleting one yields an order-\(n-1\) tree and the construction is surjective on isomorphism classes. Duplicates are removed by a canonical string: recursively parenthesize a rooted tree with the child strings sorted, then take the lexicographically least rooted string over its one or two centers. The center(s) are isomorphism-invariant; the sorted recursive string distinguishes rooted trees by induction on their size. Thus this string is a complete invariant for unrooted trees. The generated class counts are \(1,1,1,2,3,6,11,23,47,106\) for orders one through ten.

**Complete dynamics.** For each tree on \(n\) vertices, the script evaluates the single-sweep transition on **every** one of its \(2^n\) Boolean states. Every finite functional digraph is partitioned into disjoint cycles and directed in-trees; tracing every previously unvisited state until reaching an old state or repeating inside the current path lists each cycle exactly once. The algorithm records the primitive length of every cycle and takes its maximum for each tree. Consequently the maximum over the complete list of unlabelled trees is a rigorous finite exhaustion, not a sampling inference. The resulting full table is:

| \(n\) | Unlabelled trees | \(M(n)\) | Trees attaining \(M(n)\) |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 1 |
| 3 | 1 | 1 | 1 |
| 4 | 2 | 1 | 2 |
| 5 | 3 | 2 | 1 |
| 6 | 6 | 3 | 1 |
| 7 | 11 | 6 | 2 |
| 8 | 23 | 10 | 1 |
| 9 | 47 | 14 | 1 |
| 10 | 106 | 22 | 1 |

**Extremal witness and uniqueness.** The program's order-ten output identifies exactly one canonical tree class with a period-\(22\) orbit, counts two cycles with that period, and re-evaluates all transitions in the explicit witness above including the last-to-first return. Every smaller order has maximal period at most \(14\), while \(22>20\). The exhaustiveness argument simultaneously establishes uniqueness and the sharp cutoff.

## Verification
Run `python3 verify.py` with Python's standard library. The script prints one line for each size and a detailed cycle-length census, followed by the extremal edge set, a \(22\)-state cycle and `VERIFY_OK`. The script asserts all ten tree counts, all ten maximal-period values, uniqueness of the ten-vertex extremizer, the two distinct extremal cycles, and each of the \(22\) witness transitions. Separately implemented tree generation and cycle enumeration agreed on all ten orders; that cross-check is corroborative, while completeness follows from the argument and the supplied script.

## Relationship to prior work
Kuhlman, Mortveit, Murrugarra and Kumar [1] proved that sequential bi-threshold systems at threshold difference two can exhibit arbitrarily long cycles and constructed specific families of trees. Their Section 5.2 expressly leaves open the *minimal tree order* supporting a specified period. Elmeligy Abdelhamid and collaborators [2] evaluate the previously selected H-, Y-, and X-tree families rather than all tree isomorphism classes. The present finite classification addresses a distinct sharp-extremality question through ten vertices and exposes a period \(22\) on ten vertices, not entailed by a general existence theorem or the three-family plots. A bounded literature search did not identify a previous full census; absence from searches is not proof of global novelty.

## Limitations
This is an **exact finite cutoff** through ten vertices only. It proves no formula for \(M(n)\) when \(n>10\), no unrestricted asymptotic, and no minimum order for periods other than the one consequences explicitly deducible from the table. The schedule-independence assertion uses an established published equivalence theorem; the exhaustive computations themselves are fully specified in `verify.py`. Related literature not accessible in full, or not indexed, may still contain equivalent finite data.

## References
[1] Chris J. Kuhlman, Henning S. Mortveit, David Murrugarra, V. S. Anil Kumar, *Bifurcations in Boolean Networks*, first publicly posted 2011-08-15, arXiv:1108.2974 (especially Sections 4.2 and 5.2), https://arxiv.org/html/1108.2974v2 .

[2] S. H. Elmeligy Abdelhamid, C. J. Kuhlman, M. V. Marathe, H. S. Mortveit, S. S. Ravi, *GDSCalc: A Web-Based Application for Evaluating Discrete Graph Dynamical Systems*, PLOS ONE 10(8), e0133660 (2015), doi:10.1371/journal.pone.0133660, https://pmc.ncbi.nlm.nih.gov/articles/PMC4532456/ .
