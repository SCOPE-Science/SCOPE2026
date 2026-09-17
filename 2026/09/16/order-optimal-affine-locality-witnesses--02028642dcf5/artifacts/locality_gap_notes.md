# Pending Candidate: An Exact High-Girth Locality Gap

This is research material, not a RESULT or a completed same-model review.

## Exact Target

For all integers d>=3 and g>=6, find a connected finite simple bipartite d-regular
graph G of girth at least g and induced matchings M and F such that:

* no edge can be added to M;
* removing one edge of M cannot permit adding two distinct edges outside M;
* F is maximum;
* |F|/|M|=d^2/(2d-1).

The reference upper bound is Furst--Leichter--Rautenbach, arXiv:1708.02028,
Theorem 5 and Corollary 6(ii), PDF page 7. Local Search guarantees m/d^2 edges
on triangle- and 4-cycle-free graphs, while every induced matching of a
d-regular graph has at most m/(2d-1) edges. The latter follows by counting
the pairwise disjoint sets of edges incident with each matching edge.

## Two Certificates

Use two partitions of the vertices, A+B and C+D, satisfying:

* A induces a matching M. Every A vertex has d-1 neighbors in B.
* Every B vertex has one neighbor in A and d-1 in B.
* C induces a matching F. Every C vertex has d-1 neighbors in D.
* D is independent and every D vertex has d neighbors in C.

The first partition implies |M|=n/(2d). For the second, every edge intersects
exactly one member of F, so F is a dominating induced matching, also called an
efficient edge dominating set, and |F|=m/(2d-1). This attains the universal upper
bound and certifies maximum cardinality without an optimization oracle.

If girth is at least 5, M is 1-for-2 locally optimal. An A-B edge conflicts
with precisely its parent's matching edge. A B-B edge conflicts with exactly
the two distinct matching edges containing its endpoints' A-parents: equal
parents would form a triangle and partnered parents would form a 4-cycle.
Consequently the private conflict edges of an edge uv in M are exactly the
2d-1 edges incident with u or v. Every two of these conflict, via uv when
necessary. Every edge conflicts with M, so no addition or 1-for-2 exchange is
possible. These statements use the definition of conflict as distance at most
2 in the line graph, not mere edge intersection.

## A Finite Template

Let the six types have these sizes:

| Type | Partition memberships | Size |
| --- | --- | --- |
| A0 | A intersect C | 2 |
| A1 | A intersect C | 2(d-1) |
| AD | A intersect D | 2(d-1) |
| B0 | B intersect C | 2(d-1) |
| B1 | B intersect C | 2(d-1)^2 |
| BD | B intersect D | 2(d-1)^2 |

Pair the two A0 vertices, and pair A1 bijectively with AD. These edges form M.
Pair A1 bijectively with B0. Partition B1 into d-1 private neighbors for each
AD vertex. Pair all B1 vertices by an arbitrary perfect matching. The A0 edge,
A1-B0 edges and B1 matching form F.

Attach each BD vertex to one A vertex, using d-1 BD neighbors at each A0
vertex and d-2 at each A1 vertex. Both counts total 2(d-1)^2. Finally join
B0+B1 to BD so that each B0 vertex receives d-1 edges, each B1 vertex d-2,
and each BD vertex d-1. The stub totals agree:

    2(d-1)(d-1) + 2(d-1)^2(d-2) = 2(d-1)^3.

A bipartite multigraph with these degrees is obtained by arbitrary stub pairing.
The script instead uses a simple bipartite realization for its experiments.
All vertices now have degree d, and the two partitions satisfy their specified
adjacency conditions. Counts are n=2d(2d-1), m=d^2(2d-1), |M|=2d-1, |F|=d^2.

## Removing Short Cycles and Ensuring Connectedness

Take the bipartite double cover of the template. Each certificate is a local
adjacency condition and lifts unchanged. If the double cover is disconnected,
its components can be joined by switches of B-C to B-D edges (that is, edges
between B0+B1 and BD), preserving the six types and both certificates.
Each component contains such an edge. Every edge of a bipartite d-regular
graph with d>=2 lies on a cycle: decompose into perfect matchings and take the
union of its matching with a second one. Thus the chosen edges are not bridges.
Delete an edge from each of two components and reconnect crosswise, after
orienting their bipartitions consistently. This joins them, keeps d-regularity
and both certificates, and introduces no loops.

Now use the standard finite-cover fact: every finite connected graph has a
finite cover of arbitrarily large girth. It applies also to loopless
multigraphs, counting parallel-edge cycles as length 2. A self-contained route
is residual finiteness of free groups: select a spanning tree, enumerate the
finitely many nonbacktracking closed walks shorter than g, and separate all
their nontrivial fundamental-group words in a finite quotient. The associated
regular voltage cover has none of those closed lifts. A connected component
still covers the connected base. This step is standard, not claimed as new.

For completeness, a reduced word can be separated by making each generator a
partial permutation along the word's path on distinct states 0,...,length.
Reducedness prevents conflicts in the partial bijections; extend each to a
permutation. The word moves state 0 to its terminal state. Take the product
of these finite permutation images to separate finitely many words. In the
regular action of that finite group, a nonidentity element has no fixed point.

The finite cover inherits both partitions and is bipartite and d-regular.
Girth at least g>=6 makes it simple and certifies local optimality. Every
connected component has the same partition-count identities, independently of
the cover degree. Thus the prescribed ratio is exact, not asymptotic.

This construction is a candidate proof, subject to the unresolved originality
and substantive-value audit below.

## Actual Computational Check

Command: `python3 artifacts/locality_template_check.py`

The code constructs edges, not just type counts, and verifies all vertex
degrees; both induced-matching predicates; exact-one intersection domination
for F; component-wise count identities; and, for high-girth simple witnesses,
the full possible replacement pool for each deleted member of M. It tests all
pairs in that pool for conflict, which directly checks the exchange predicate.
BFS computes girth, and the bipartition is checked separately on every edge.

Observed output:

```text
base 3 vertices 30 edges 45 bad 5 good 9
base 4 vertices 56 edges 112 bad 7 good 16
base 5 vertices 90 edges 225 bad 9 good 25
base 6 vertices 132 edges 396 bad 11 good 36
base 7 vertices 182 edges 637 bad 13 good 49
base 8 vertices 240 edges 960 bad 15 good 64
verified cover trial 305 n 480 girth 6 components 1 bad 80 optimum 144 ratio 1.8
```

The last line attains the reference formulas exactly: m=720, m/3^2=80,
m/(2*3-1)=144, ratio=9/5. It is a certificate proof of the optimum, not a
claim that a numerical optimization solver independently found 144.

## Coverage Evidence and Unresolved Doubts

The claim was translated to a locality gap of independent-set local search in
L(G)^2, and to simultaneous existence of the first equitable partition and an
efficient edge dominating set. Searches included local search tightness,
worst-case examples, locality gap, dominating induced matchings, perfect codes,
and graph covers. No search failure is considered novelty evidence.

Primary material inspected:

* Furst--Leichter--Rautenbach, DOI 10.1016/j.tcs.2018.02.006,
  arXiv:1708.02028v1. Algorithm 1, Lemma 1, Theorems 4--5, Corollary 6,
  and the remaining theorems/conclusion were read. The closest exact upper
  guarantee is Theorem 5; its proof supplies the private-conflict and
  double-counting inequalities, not the simultaneous extremal template above.
* Duckworth--Manlove--Zito, DOI 10.1016/j.jda.2004.05.001, Section 3,
  Theorems 3.1--3.3 and the intervening construction, PDF pages 4--7 in the
  article numbering. Their tight examples concern MinGreedy and its different
  n-dependent lower bound. They do not, by the construction and theorem
  inspected, establish a 1-for-2 local optimum or the present exact ratio.
* Rautenbach, DOI 10.1016/j.tcs.2015.08.002, arXiv:1507.04145v1,
  introduction, Theorems 1--2 and local-search setup. Its stated approximation
  guarantee concerns triangle- and 5-cycle-free graphs and is larger than the
  present ratio; it was the starting point for the covered Candidate 2 proof.

Specific unresolved source: Gotthilf--Lewenstein, *Tighter Approximations for
Maximum Induced Matchings in Regular Graphs*, DOI 10.1007/11671411_21.
Known-paper acquisition by title, DOI, and the
containing volume DOI 10.1007/11671411 failed. Search found indexed Springer
and Academia copies but the full chapter could not be obtained.
Its possible extremal constructions have therefore NOT been excluded.

Further audit needed: assess whether standard common-cover results, especially
Leighton's theorem, together with already known extremal partitioned graphs make
this locality-gap statement a routine consequence. The bespoke template solves
the simultaneous degree constraints, but that alone does not establish
substantive originality. Do not issue originality/value PASS while these
concrete doubts remain unresolved.
