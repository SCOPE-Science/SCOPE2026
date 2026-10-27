# Triangle–tangent metric bases and their exchange graph in the Heawood graph

## Finding

Let \(H\) be the incidence graph of the seven points and seven lines of \(\operatorname{PG}(2,2)\). A *metric basis* is a smallest vertex set \(S\) for which the vectors \((d(v,s))_{s\in S}\) distinguish every vertex \(v\) of \(H\). Let \(\mathcal B(H)\) have these bases as vertices, with \(S\sim T\) when \(|S\setminus T|=|T\setminus S|=1\).

**Theorem.** Every metric basis has five vertices and has exactly one of the following forms:

* three noncollinear points, together with two of the three lines each incident with exactly one of those points; or
* three nonconcurrent lines, together with two of the three points each incident with exactly one of those lines.

There are \(28\cdot 3=84\) bases of each type and \(168\) in total. The graph \(\mathcal B(H)\) is connected and \(5\)-regular, with \(168\) vertices and \(420\) edges. Its radius and diameter are both \(5\), and the distance-layer sizes from **every** vertex are

\[
(1,5,18,49,71,24).
\]

The bases form a canonical partition into \(56\) disjoint induced triangles: for each noncollinear point triple (or nonconcurrent line triple), its three choices of two tangents form one triangle. Each base has two neighbors inside its triangle and three outside. In particular, every pair of optimal landmark placements can be transformed into each other by at most five single-landmark replacements without ever losing the resolving property.

## Assumptions and scope

The graph is finite, simple, and unweighted. Let the points be the nonzero binary triples, identified with integers \(1,\ldots,7\) using bitwise exclusive-or. Its seven lines are exactly the three-element sets \(\{a,b,c\}\) satisfying \(a\oplus b\oplus c=0\). A point is adjacent to a line precisely when incident. No graph embedding or additional metric is used.

A *noncollinear point triple* is not one of the seven lines. A *nonconcurrent line triple* has no common point. Given a noncollinear point triple, each of its three members lies on a unique line containing none of the other two members; these are its three *single-incidence tangent lines*. The definition for lines is dual. Replacements may change either point or line vertices and need not follow edges of \(H\): this is token-jumping exchange, not token sliding.

## Proof

**Distance reduction.** Two distinct vertices in the same bipartition class of \(H\) have distance \(2\). A point and a line have distance \(1\) when incident and \(3\) otherwise; a vertex has distance \(0\) from itself. Thus all distance signatures can be calculated directly from the seven Fano incidence triples, without a shortest-path oracle.

**Exact five-set classification.** Consider all \(\binom{14}{5}=2002\) five-subsets. Program `verify_incidence.py` generates the seven lines algebraically, evaluates fourteen exact distance signatures for every five-subset, and checks, for **each** of the 2002 subsets, the equivalence between being resolving and belonging to the two triangle–tangent families above. This pointwise equality, not merely matching aggregate counts, is the finite classification certificate. It also checks all subsets of sizes \(0,1,2,3,4\), finding none resolving, establishing minimality independently of previously published metric-dimension calculations.

There are \(\binom{7}{3}-7=28\) noncollinear point triples. For any one, there are exactly three single-incidence tangent lines, and any choice of two yields one of three distinct bases. The same argument applies dually to line triples. The constructive verifier enumerates these \(84+84=168\) configurations without using the resolving-set test and verifies equality with the independently enumerated bases.

For clarity, one representative basis contains points \(1,2,4\) and lines \(\{1,6,7\}\), \(\{2,5,7\}\). The three point labels are not collinear, and the two selected lines are two of their three tangents.

**Exchange graph.** Enumerate every five-element metric basis, remove each of its five selected vertices, and adjoin each of the nine unselected vertices; connect the result when it is another enumerated basis. The resulting symmetric adjacency lists have exactly five entries per vertex, giving \(168\cdot5/2=420\) edges. The three bases sharing any majority triangle are pairwise adjacent, and all fifty-six such families are disjoint; the adjacency certificate finds no additional triangles. Every base has precisely three neighbors outside its majority-triangle family.

A complete breadth-first search in this \(168\)-vertex graph from **each** of its \(168\) vertices reaches all vertices and yields exactly the same distance-layer vector \((1,5,18,49,71,24)\). The maximum layer index is \(5\), hence both radius and diameter equal \(5\).

**Separate verification.** Program `verify_distance.py` instead constructs the incidence graph by the zero-dot-product equation in \(\mathbf F_2^3\), computes all fourteen graph distances by breadth-first search, tests all \(2^{14}\) vertex masks, constructs exchange edges via shared four-subsets, and verifies all source distance layers. It also enumerates the \(168\) invertible binary coordinate changes; they act on one \(84\)-element orbit of optimal bases, and point–line polarity exchanges that orbit with the other \(84\), establishing transitivity under these natural symmetries. Neither program reads the other's results.

## Verification

Run with a standard Python 3 interpreter and no third-party dependencies:

```
python3 verify_incidence.py
python3 verify_distance.py
```

Their independently obtained summaries are `incidence_output.txt` and `distance_output.txt`. Both scripts use assertions, cover all relevant finite configurations, and terminate with the recorded deterministic JSON summaries. The first has a pointwise test over all 2002 five-subsets; the second checks all 16384 subsets and breadth-first searches from every optimal basis. All claims are finite: no extrapolation to larger projective planes is made.

## Relationship to prior work

Héger and Takáts (2012, Remark 11 and Figure 1) already prove that the Fano incidence graph has metric dimension \(5\) and give a five-vertex example. Their Proposition 7 provides general incidence conditions characterizing resolving sets of finite projective planes; their all-optima classification theorem concerns projective planes of order at least \(23\), not the order-two exchange graph. Thus neither the metric-dimension value nor the existence of a five-set is claimed as new. The present theorem instead gives every order-two metric basis in a geometrically explicit form and determines their complete one-replacement graph.

Bailey (2013, Tables 1 and 3) independently lists metric dimension \(5\) for the Heawood graph; those tables give no basis-exchange adjacency, its diameter, or its distance layers. Work on reconfiguration of metric bases provides the natural operation, but it does not follow merely from having a known metric dimension that the optimal-solution exchange graph is connected. Targeted literature and mathematical-record comparisons did not identify the Heawood-specific exchange-graph classification reported here.

## Limitations

This is a finite classification for one graph, not a theorem for arbitrary projective planes or distance-regular graphs. The proof uses transparent exhaustive verification for the structural converse and distance distribution; it is not a purely hand-derived classification. Publication-priority uncertainty remains possible, particularly for unpublished research on metric-basis reconfiguration or equivalent incidence terminology. The exact finite calculations have not undergone independent external auditing.

## References

1. T. Héger and M. Takáts, *Resolving sets and semi-resolving sets in finite projective planes*, Electronic Journal of Combinatorics 19(4) (2012), P30, https://doi.org/10.37236/2582 ; first arXiv public submission 2012-07-23, https://arxiv.org/abs/1207.5469 . Relevant material: Definition 1, Proposition 7, Remark 11, Figure 1, Section 3.
2. R. F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, arXiv:1312.4973 (2013), https://arxiv.org/abs/1312.4973 . Relevant material: Section 3 and Tables 1 and 3; full text at https://www.math.mun.ca/rbailey00/papers/small.pdf .
3. Cal Poly Pomona mathematics research, *Metric Basis Reconfiguration*, https://www.cpp.edu/camp-reu/research_projects.shtml . General project description; no asserted Heawood-specific result.
