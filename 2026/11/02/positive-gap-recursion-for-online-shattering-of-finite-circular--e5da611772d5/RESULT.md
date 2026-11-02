# Positive-gap recursion for online shattering of finite circular intervals

## Finding

Let \(X_n=\mathbb Z/n\mathbb Z\), where \(n\ge1\). Let \(\mathcal A_n\) be the membership concept class consisting of the empty set, the whole set, and every nonempty proper cyclic interval (a sequence of consecutive vertices in the fixed cyclic order). Its concepts are subsets of vertices; a query asks whether one given vertex belongs to the target concept.

For a finite multiset \(G\) of positive integers, write its elements as a sorted tuple. Define \(F(G)\) recursively by
\[
F(G)=\max_{\substack{L\in G\\1\le a<L}}\left[1+\min\left\{F\big((G\setminus\{L\})\uplus\{a,L-a\}\big),\ \lfloor\log_2 a\rfloor+\lfloor\log_2(L-a)\rfloor\right\}\right],
\]
where the maximum of an empty set is zero. Repeated occurrences of \(L\) are removed one at a time. Every recursion replaces one positive integer by two strictly smaller positive integers, so termination is guaranteed. Then the **exact** Littlestone dimension, for every \(n\ge1\), is
\[
\boxed{\operatorname{Ldim}(\mathcal A_n)=1+F((n)).}
\]
There are at most \(p(n)\) distinct memoized states, where \(p(n)\) denotes the number of integer partitions of \(n\); thus the structural recursion requires \(p(n)\) times a polynomial in \(n\) operations, rather than enumerating all version spaces of the \(n(n-1)+2\) concepts.

The exact first-occurrence thresholds for Littlestone depths \(d=1,\ldots,10\), over all \(1\le n\le40\), are respectively
\[
\begin{array}{c|rrrrrrrrrr}
d&1&2&3&4&5&6&7&8&9&10\\\hline
\min\{n:\operatorname{Ldim}(\mathcal A_n)\ge d\}&1&2&3&5&7&10&14&20&28&40
\end{array}.
\]
These are certified through \(n=40\), not asserted to satisfy an unproved closed formula beyond that range. The first strict deficit from the elementary cardinality ceiling is
\[
\boxed{\operatorname{Ldim}(\mathcal A_6)=4<5=\lfloor\log_2|\mathcal A_6|\rfloor,\qquad |\mathcal A_6|=32.}
\]
For static shattering, \(\operatorname{VCdim}(\mathcal A_n)=\min\{n,3\}\). Moreover \(\operatorname{Ldim}(\mathcal A_n)=2\log_2 n+O(1)\) as \(n\) grows, while the VC dimension is fixed at three. The exact recursion, its finite initial classification, and the cyclic six-point obstruction are the findings; elementary VC and logarithmic growth observations supply context.

## Assumptions and scope

A cyclic interval is the set of vertices visited by a connected arc of a simple cycle, with any length between one and \(n-1\) inclusive. Empty and full concepts are explicitly included. Each concept corresponds to a different Boolean function on \(X_n\); all queries are individual vertex-membership predicates, not pair-separation queries. For \(n=1\), the class has exactly two concepts. For every \(n\ge1\), \(|\mathcal A_n|=n(n-1)+2\).

Littlestone dimension means the greatest depth of a complete binary tree of vertex queries such that every root-to-leaf Boolean answer sequence is realized by a concept. An empty version space has no shattered tree; a singleton nonempty version space has rank zero. All logarithms are base two. The recurrence applies to integer partitions represented by multisets; no geometric symmetry assumption beyond the fixed circular order is needed.

## Proof

**1. States after positive-only observations.** Suppose at least one vertex has been queried and every observed label was positive. Traverse the observed vertices in cyclic order, and record the numbers \(G=(g_1,\ldots,g_s)\) of cycle edges between successive observed vertices. These are positive integers summing to \(n\). A cyclic interval consistent with the observations is either the whole cycle or the complement of a nonempty consecutive block of unqueried vertices lying *inside one* gap. A gap of \(L\) edges has \(L-1\) interior vertices and \(L(L-1)/2\) possible nonempty excluded intervals. Hence the version space has
\[
1+\sum_{L\in G}\frac{L(L-1)}2
\]
concepts. Crucially, its future query behaviour depends only on the multiset of gap lengths, not on their cyclic permutation: query one of the interior vertices of a gap, and the two branches have the descriptions below. Induction on the number of unqueried vertices therefore establishes a well-defined rank \(F(G)\).

**2. The positive branch.** Query an interior vertex of a gap having \(L\) edges, at distance \(a\) edges from its preceding positive vertex and \(b=L-a\) edges from its following positive vertex. A positive answer inserts the queried vertex in the observed-positive list and replaces the gap \(L\) by gaps \(a,b\). Thus the positive-child rank is exactly \(F((G\setminus\{L\})\uplus\{a,b\})\).

**3. The negative branch.** A negative answer forces the excluded complementary interval to occur in this one gap and to contain the queried vertex. Its left and right endpoints can independently occupy \(a\) and \(b\) cut positions, respectively. All other gap vertices have fixed positive labels. Within the chosen gap, testing a vertex on the left tests one threshold coordinate; testing on the right tests the other. Therefore this child is exactly the product of independent threshold concept classes with \(a\) and \(b\) cut positions. A threshold class with \(m\) ordered possibilities has Littlestone rank \(\lfloor\log_2m\rfloor\), by midpoint-query construction and the \(m\)-hypothesis bound. The ranks of independent product classes on disjoint query domains add: concatenate optimal trees for the lower bound, and for the upper bound observe that a query in one factor must lower at least one child rank of that factor, then induct on product cardinality. Consequently the negative-child rank is \(\lfloor\log_2a\rfloor+\lfloor\log_2b\rfloor\).

**4. Minimax recursion and initial query.** For a finite nonempty class with children of ranks \(r_0,r_1\), a query offers a shattered tree of depth \(1+\min\{r_0,r_1\}\). Maximizing over the queries gives precisely the displayed recursion. When no interior vertex remains, there is one concept and the rank is zero. In the initially unqueried class, choose any vertex. Its positive branch is the positive-only state \((n)\). Its negative branch is isomorphic by complementing every concept and reversing all binary labels, since complements of cyclic intervals are again cyclic intervals. The two children therefore both have rank \(F((n))\), establishing \(\operatorname{Ldim}(\mathcal A_n)=1+F((n))\).

**5. Complexity and exact finite range.** Recursion replaces \(L\) by two summands and never changes their total \(n\). Sorting the gaps identifies states with integer partitions, so there are at most \(p(n)\) possible states, with at most quadratic-many split candidates and polynomial state processing per state. The included `verify_cyclic_arcs.py` computes the exact ranks through \(n=40\) using this recursion, and independently computes the same ranks from the definition of shattered trees using bitsets of explicit concepts. Both methods agree, and the first-occurrence thresholds are the displayed integers.

**6. Independent six-vertex obstruction.** For \(n=6\), there are exactly 32 concepts. A depth-five tree would need every node at every level to halve its version space perfectly. By rotation and complement symmetry, the first query may be taken as vertex 0 with positive answer, leaving 16 concepts. Among the other vertices, only vertices 2 and 4 split those 16 into eight and eight; reflection fixes vertex 2. On the child answering positive to vertex 2, only vertex 4 splits the eight into four and four. On its positive child, the four possible concepts are the full cycle and the three five-vertex cyclic intervals containing vertices \(0,2,4\). Each of the remaining vertices \(1,3,5\) belongs to exactly three of these four concepts, so no next query splits them two against two. This contradicts depth five. The explicit depth-four shattered tree is in `SIX_VERTEX_WITNESS.json` and independently checked by the verifier; thus the upper bound is attained.

**7. Static and asymptotic bounds.** Every three distinct vertices are shattered by circular intervals, while no four distinct vertices can realize the alternating cyclic labels \(1,0,1,0\). This gives the VC dimension. The class size is \(n(n-1)+2\), giving the upper online bound \(2\log_2 n+O(1)\). For any two marked vertices whose clockwise gaps have edge lengths \(a+b=n\), restricting to concepts containing one vertex and excluding the other yields the product of independent threshold classes with \(a,b\) options. Its rank is \(\lfloor\log_2a\rfloor+\lfloor\log_2b\rfloor\). Taking nearly equal \(a,b\) proves the matching lower asymptotic order.

## Verification

Execute `python3 verify_cyclic_arcs.py` beside `SIX_VERTEX_WITNESS.json` (Python 3.9 or later, standard library only). The program independently enumerates every cyclic interval as a bitmask and evaluates the full version-space shattering recurrence through 40 vertices. Separately, it memoizes the gap-partition formula and compares the resulting answers for every \(1\le n\le40\). It checks all cardinalities, the threshold table, and the exact six-vertex branching obstruction. The explicit six-vertex depth-four tree is checked along every root-to-leaf path, including distinct terminal witnesses. No other files, external services, sampled experiments, or cached result logs are required.

## Relationship to prior work

Alon, Livni, Malliaris and Moran (2018, arXiv:1806.00949) establish broad relations between Littlestone dimension, thresholds and learnability, but do not derive the finite cyclic-interval rank. Ghazi, Golowich, Kumar and Manurangsi (2020, arXiv:2007.03668) establish general bounds under Boolean aggregation; their Proposition 3 does not compute this particular all-length interval union or the gap-partition minimax recurrence. Earlier exact results for single-length circular windows are not interchangeable with this all-length union: adding possible lengths changes the class and its adaptive rank. Likewise a linear chain has endpoints and different positive-only gap states; its online ranks do not imply the circular thresholds. The principal mathematical comparison is therefore of **statements and reductions**, not of terminology. Searches under cyclic intervals, circular arcs, online mistake trees, thicket rank, unions of circular windows and finite chain intervals did not identify an already covering assertion; historical-priority uncertainty remains.

## Limitations

The threshold list is proved computationally only for \(1\le n\le40\), and no closed formula or extrapolation beyond that range is asserted. The all-size rank recursion and logarithmic asymptotic are proved independently of those finite computations. The work does not establish the minimum-time implementation of the recursion or classify optimal query trees, and its historical-priority search is not exhaustive. No independent scientific validation has been conducted.

## References

1. N. Alon, R. Livni, M. Malliaris, S. Moran, *Private PAC learning implies finite Littlestone dimension*, arXiv:1806.00949, first public version 4 June 2018, https://arxiv.org/abs/1806.00949.
2. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight closure bounds for the Littlestone and threshold dimensions*, arXiv:2007.03668, first public version 7 July 2020; Algorithmic Learning Theory 2021, https://arxiv.org/abs/2007.03668.
