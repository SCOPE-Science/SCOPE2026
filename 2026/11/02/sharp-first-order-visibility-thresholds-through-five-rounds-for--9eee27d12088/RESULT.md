# Sharp first-order visibility thresholds through five rounds for complete-graph incidence graphs

## Finding
For each integer \(n\ge1\), let \(\mathcal I_n\) be the simple graph obtained by subdividing every edge of the complete graph \(K_n\) exactly once. It is also the unoriented incidence graph between the vertices and edges of \(K_n\). In first-order logic with equality and one undirected adjacency relation, write \(\equiv_q\) for equivalence on all sentences of quantifier rank at most \(q\).

**Theorem.** For every \(m,n\ge1\) and \(1\le q\le5\), set
\[
(c_1,c_2,c_3,c_4,c_5)=(1,3,4,5,7).
\]
Then
\[
\boxed{\mathcal I_m\equiv_q\mathcal I_n\quad\Longleftrightarrow\quad
\min(m,c_q)=\min(n,c_q).}
\]
Thus the numbers of theories at ranks one through five are respectively \(1,3,4,5,7\). At rank five, the seven smallest representatives contain \(1,3,6,10,15,21,28\) graph vertices. In particular, every graph in this family has a rank-five-equivalent representative on at most \(28\) vertices, and this bound is sharp *within the family*.

## Assumptions and scope
The vertex set of \(\mathcal I_n\) is the union of the singleton subsets and the two-element subsets of \([n]=\{1,\ldots,n\}\). Distinct graph vertices \(S,T\) are adjacent if and only if one is a singleton and the other is a two-element subset containing it. Thus \(|V(\mathcal I_n)|=n+\binom n2\); for \(n=1\), this is the one-vertex graph. There are no predicates naming the original points, the edge-subdivision vertices, or the underlying labels. Equality is available, but no counting quantifiers or parameters are allowed.

The quantifier rank of a first-order sentence is its maximum quantifier-nesting depth. Equivalence \(\equiv_q\) is ordinary Ehrenfeucht–Fraïssé equivalence for \(q\) rounds, without counting and without moving already placed pebbles.

## Proof
**1. Exact finite-type recursion.** For an ordered tuple \(\bar a\) of selected graph vertices, let \(A(\bar a)\) be its complete atomic diagram: for every ordered pair of selected positions, record both equality and adjacency. Define the finite, hereditarily set-valued type
\[
T_0^n(\bar a)=\bigl(A(\bar a),\varnothing\bigr),\qquad
T_{r+1}^n(\bar a)=\left(A(\bar a),
\left\{T_r^n(\bar a,b):b\in V(\mathcal I_n)\right\}\right).
\]
Set braces discard multiplicity, as appropriate for ordinary first-order logic without counting. Induction on \(r\) proves that two pointed graphs have the same displayed type if and only if Duplicator can win the corresponding \(r\)-round game from those pointed positions: at \(r=0\) the assertion is the atomic-diagram condition, and at the successor step equality of extension-type sets is precisely the two-way extension property when Spoiler may play in either structure. Consequently, \(T_q^n(())\) is a complete invariant of rank-\(q\) sentences for \(\mathcal I_n\).

**2. Exhaustive orbit representatives.** Let \(U\subseteq[n]\) be the union of the underlying index sets of the already selected vertices, and let \(F=[n]\setminus U\). Every permutation of \(F\) fixing \(U\) pointwise induces an automorphism of \(\mathcal I_n\) fixing the selected tuple. For the next move it is therefore enough to enumerate precisely these possibilities:

- every singleton \(\{u\}\) for \(u\in U\), and, if \(F\ne\varnothing\), the singleton containing the least element of \(F\);
- every two-element subset of \(U\);
- every pair containing one element of \(U\) and the least element of \(F\), when \(F\ne\varnothing\);
- the pair comprising the two least elements of \(F\), when \(|F|\ge2\).

Indeed, every possible move can be sent to one of these representatives by a permutation of unused indices, and the extension's remaining type is invariant under the resulting automorphism. Hence substitution of these representatives in the preceding recursion is *exact for every parameter*, not an approximation or sample.

**3. Finite classification.** Applying this exact recursion independently in the included C++17 and Python programs to \(1\le n\le10\) and \(1\le q\le5\) gives the following class numbers, where each row numbers new complete types in order of first appearance. These are equality comparisons of complete recursively interned or immutable-set objects; hash equality is not used as a correctness test.

| \(n\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(q=1\) | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| \(q=2\) | 1 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| \(q=3\) | 1 | 2 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| \(q=4\) | 1 | 2 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 |
| \(q=5\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 7 | 7 | 7 |

The implementations and their reproducible outputs are embedded in the accompanying package. A separate unquotiented enumeration checks that the orbit-reduced and all-vertex recursions return *identical complete types* for \(1\le n\le4\) at rank five. The finite computation therefore proves all the displayed distinctions and bridges, subject only to the correctness of the supplied finite code and its elementary recurrence.

**4. Infinite tail and conclusion.** More generally, for any positive integer \(q\), Duplicator wins the \(q\)-round game on \(\mathcal I_m,\mathcal I_n\) whenever \(m,n\ge2q\). Maintain a partial bijection between underlying indices that covers all indices occurring in already chosen graph vertices and matches each singleton or two-element vertex to the singleton or pair of images. Each round requires at most two new indices. Through \(q\) rounds there are at most \(2q\) distinct indices, so when \(m,n\ge2q\), the partial bijection can always be extended to the new labels, from either side. Adjacency and equality of chosen graph vertices are preserved because both depend only on the sizes and intersections of their underlying singleton/pair supports.

For \(q\le5\), the infinite lemma gives stabilization from parameter \(2q\). The finite row for each \(q\) shows that every parameter from \(c_q\) through \(2q\) already has the same complete type, while all smaller parameters have distinct complete types. The two conclusions combine to yield the asserted classification for **all** positive integers \(m,n\). Sharpness of each \(c_q\) follows from the distinct classes immediately below that threshold. The rank-five bound \(28=7+\binom72\) follows from the smallest parameter in the last class.

## Verification
The embedded verification materials contain `verify_incidence_types.cpp` (independently interned integer signatures), `verify_incidence_types.py` (immutable recursive type sets), and `verify_direct_small.py` (all-vertex enumeration, with no orbit reduction, for the first four parameters). `reproduce.sh` runs both main checks, compares their complete printed profiles, and runs the unquotiented check. The C++ program visited \(156276\) memoized states and interned \(2109\) distinct type signatures across all listed ranks and parameters; the Python orbit computation visited \(156276\) states. The separate direct check agrees with the orbit computation for all \(1\le n\le4\) at rank five. Both programs distinguish all parameter values below each listed cutoff and match the complete types above it through parameter ten.

The infinite part rests on the preceding support-preserving game proof, not on extrapolation from ten computed cases. All computations use finite integer or Boolean operations and exact set equality; no floating-point estimates or unproved convergence claims are involved.

## Relationship to prior work
Pippenger's publicly available technical report (2001) studies **the same family of incidence graphs** and enumerates matchings in them, including matching orbits under automorphisms. Its matching-orbit equivalence is not first-order rank equivalence, and its generating-function results do not imply this five-round type classification. Pikhurko and Verbitsky's 2010 survey develops graph logical depth and Ehrenfeucht games in the adjacency language; it does not state the numerical cutoffs here. Trotter and Wang's 2013 paper concerns order dimension and chromatic properties of incidence posets, including those of complete graphs, but studies a different invariant and signature. The present finite-type calculation and sharp cutoffs supplement these sources; no claim about universal priority beyond the checked literature is made.

## Limitations
The result is restricted to the undirected, unlabeled incidence **graph** (not the oriented incidence poset or the graph with named vertex/edge sorts), ordinary first-order logic with equality and adjacency, and quantifier ranks at most five. No higher-rank cutoff, classification of arbitrary graph subdivisions, or theorem about counting logic is asserted. The finite part depends on the exact algorithms supplied and remains subject to independent mathematical validation. Searches and available full-text inspections cannot exclude all unindexed historical priority.

## References
1. N. Pippenger, *Enumeration of Matchings in the Incidence Graphs of Complete and Complete Bipartite Graphs*, University of British Columbia Technical Report TR-2001-12, publicly posted 2001-09-10, https://www.cs.ubc.ca/tr/2001/tr-2001-12 (later SIAM Journal on Discrete Mathematics 16 (2002), 47–64).
2. O. Pikhurko and O. Verbitsky, *Logical Complexity of Graphs: A Survey*, first arXiv posting 2010-03-25, arXiv:1003.4865, https://arxiv.org/abs/1003.4865.
3. W. T. Trotter and R. Wang, *Incidence Posets and Cover Graphs*, first arXiv posting 2013-08-12, arXiv:1308.2471, https://arxiv.org/html/1308.2471v1.
