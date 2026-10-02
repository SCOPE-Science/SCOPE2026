# Exact labeled mutation-graph diameters of seven connected rank-five classes

## Finding

For the seven connected rank-five finite-mutation classes catalogued in the
Quiver Mutation Database (QMD), the labeled matrix-mutation graphs have
diameters \(7,8,9,11,11,11,11\), in increasing order of the class sizes
\(270,600,720,1440,1680,1980,2184\). The class list and sizes are prior
QMD data; the finding here is the exact graph-distance table.

| Archived representative ID | Number of labeled matrices | Diameter |
| --- | ---: | ---: |
| 31 | 270 | 7 |
| 13 | 600 | 8 |
| 0 | 720 | 9 |
| 15 | 1440 | 11 |
| 2 | 1680 | 11 |
| 415 | 1980 | 11 |
| 199 | 2184 | 11 |

The IDs are keys in `artifacts/representatives.csv`, which gives every
representative matrix explicitly. They do not assert publication priority.

## Assumptions and scope

The vertices of a graph are distinct skew-symmetric integer matrices
\(B\in\mathbb Z^{5\times5}\) in the labeled mutation orbit of its
specified representative. Simultaneous permutations are not identified.
For \(k\in\{0,1,2,3,4\}\), mutation is

\[
(\mu_k B)_{ij}=\begin{cases}
-B_{ij},&i=k\text{ or }j=k,\\
B_{ij}+\bigl(|B_{ik}|B_{kj}+B_{ik}|B_{kj}|\bigr)/2,&\text{otherwise}.
\end{cases}
\]

Two matrices are adjacent if one mutation relates them. This is an unweighted
undirected graph because mutation is an involution. Loops and coinciding
mutation neighbors do not affect distances. Its diameter is the maximum of
the shortest-path distances between all pairs of vertices.

This is a graph of exchange **matrices**, not the exchange graph of full
cluster seeds or cluster variables; those are different objects. The seven
matrices and their association with the prior catalogue are the domain of
the computation. No new classification theorem is claimed.

## Proof

Starting with each representative, compute all five mutations at every
discovered matrix, adding each previously unseen result to a queue. The
integer formula above is exact. The queue terminates with the respective
listed number of vertices, and every computed neighbor is in the same
finite set. Every discovered vertex is reachable from the representative;
closure under all generators conversely implies every matrix in that
mutation orbit has been discovered. Thus the finite graph is the whole
labeled mutation component, not a depth-truncated sample. All entries have
absolute value at most two, which is checked but is not imposed as a rule
for discarding unexplored neighbors.

On the resulting adjacency lists, run breadth-first search from **every**
vertex. In an unweighted graph, induction over successive queue layers
proves that the assigned distance is the shortest-path distance: every
length-one extension of a previous layer is explored before a later layer.
Taking the largest distance from every source therefore gives the exact
diameter, simultaneously an upper bound for all pairs and a realized lower
bound. The seven exhaustive runs give the table above.

## Verification

Run the standard-library-only checker from the package directory:

```text
python artifacts/verify_diameters.py artifacts/representatives.csv
```

It independently builds all seven matrix components, checks closure, entry
bounds, mutation involutivity and listed orders, and computes every source's
distance array. It asserts all listed diameters and finishes `DIAMETERS_OK`.
This checker does not rely on the saved adjacency or distance certificates.

The original `artifacts/recheck.py` remains available for its separate
checks of canonical representatives, disjoint canonical components, the
2,184-node finite witness, the finite initial growth log and the 78 triple
bridges. Those older checks alone do not compute the seven diameters.
All original artifacts remain preserved.

## Relationship to prior work

QMD's June 2026 catalogue already supplies these seven classes and all seven
labeled orders. Its rank-five finite-class API returns complete class data,
not graph diameters. The general finite-mutation classification of
Felikson–Shapiro–Tumarkin and Lawson's earlier enumeration software also
predate this record. Neither a class order nor a finite-mutation type
classification entails the exact labeled graph metric without an additional
distance computation. The precise distances are natural benchmarks for
mutation reachability searches and comparisons of search implementations.
The originality assessment is bounded by the inspected sources, not a
claim that no unindexed computation can exist.

## Limitations

The table is an exact finite computational result, not a symbolic formula
for other ranks. The new checker verifies each of the seven specified
components; it does not rerun the old exhaustive census of all bounded
rank-five matrices. Completeness of the seven-class catalogue is credited
to the existing catalogue and classification, not asserted as a new result.
The original intermediate filter counts, type guesses and separate
infinite-growth witness are not part of the surviving diameter claim.

## References

- B. Jackson, [Quiver Mutation Database](https://quivermutationdb.org/), June 2026 catalogue update; [rank-five finite classes](https://quivermutationdb.org/api/classes?rank=5&is_mutation_finite=true&limit=100).
- A. Felikson, M. Shapiro and P. Tumarkin, [Skew-symmetric cluster algebras of finite mutation type](https://arxiv.org/abs/0811.1703), JEMS 14 (2012), 1135–1180.
- J. Lawson, [qvfin](https://github.com/jwlawson/qvfin), finite-mutation enumeration software.
