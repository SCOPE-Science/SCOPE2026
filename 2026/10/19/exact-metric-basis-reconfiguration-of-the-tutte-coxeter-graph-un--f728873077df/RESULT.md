# Exact metric-basis reconfiguration of the Tutte–Coxeter graph under token jumping and sliding

## Finding

**Theorem (complete minimum-resolving-set relocation classification).** Let \(T\) be the Tutte–Coxeter graph, the thirty-vertex cubic incidence graph of the fifteen duads and fifteen synthemes on a six-element set. It has exactly \(32{,}460\) unordered metric bases, each with six vertices. When a move replaces one selected vertex and retains the metric-basis property, the resulting token-jump and token-slide graphs have the following exact invariants:

| Invariant | Token jumping | Token sliding |
| --- | ---: | ---: |
| Vertices | 32,460 | 32,460 |
| Undirected edges | 403,020 | 55,440 |
| Connected components | 1 | 1 |
| Radius | 7 | 17 |
| Diameter | 8 | 20 |

For jumping, precisely \(31{,}740\) bases have eccentricity \(7\), and precisely \(720\) have eccentricity \(8\). Those \(720\) bases form exactly one orbit under the natural permutation action of \(S_6\) on duads and synthemes. The sliding eccentricity distribution is \(3780,11040,10440,7200\) at eccentricities \(17,18,19,20\), respectively.

The bases contain, respectively, \(2\), \(3\), or \(4\) duad vertices in exactly \(7470\), \(17520\), or \(7470\) cases. Under the natural \(S_6\)-action, all \(32{,}460\) bases form \(62\) orbits, of sizes \(720\) (\(32\) orbits), \(360\) (\(24\)), \(180\) (\(2\)), \(120\) (\(2\)), and \(90\) (\(2\)).

## Assumptions and scope

Let \(U=\{0,1,2,3,4,5\}\). A *duad* is a two-element subset of \(U\); a *syntheme* is a partition of \(U\) into three duads. The vertex set \(V(T)\) consists of the fifteen duads and fifteen synthemes, with an edge precisely when a duad belongs to a syntheme. This bipartite graph is the Tutte–Coxeter eight-cage. All distances \(d_T\) below are ordinary, unweighted graph distances.

A set \(B\subseteq V(T)\) is *resolving* when the vectors \((d_T(v,b))_{b\in B}\) distinguish every two distinct vertices \(v\). A *metric basis* is a resolving set of minimum possible cardinality; here that cardinality is \(6\) (also previously known, as noted below).

The token-jump graph \(R_{\mathrm{TJ}}\) has as vertices all such unordered six-element bases, with \(B\sim B'\) precisely when \(|B\triangle B'|=2\). The token-slide graph \(R_{\mathrm{TS}}\) retains only those jump edges for which the unique outgoing vertex \(u\in B\setminus B'\) and incoming vertex \(v\in B'\setminus B\) satisfy \(uv\in E(T)\). No intermediate non-resolving configurations and no seventh landmark are allowed. Radius, diameter and eccentricity refer to these two reconfiguration graphs, not to \(T\).

## Proof

This finite classification has a complete, exhaustive computational proof by the two included standard-library Python certificates. The exhaustive domains and reductions are as follows.

1. Construct all \(15\) duads, all \(15\) partitions into three duads, and all \(45\) incidences. Breadth-first search supplies all \(30\times30\) distances. For each of the \(\binom{30}{2}=435\) unordered vertex pairs, a selected landmark separates it if its distances to the two vertices differ. A subset resolves \(T\) if and only if the union of its separation sets equals the set of all \(435\) pairs. Exhausting **all** \(\binom{30}{k}\) vertex subsets at each \(1\le k\le6\) yields zero resolving sets for \(1\le k\le5\) and exactly \(32{,}460\) at \(k=6\). Thus the minimum cardinality and full basis set, not merely a sample, are certified. The duad-count distribution is accumulated directly over this exhaustive list.
2. Enumerate each unordered pair of bases that differs in one element. This produces exactly \(403{,}020\) edges of \(R_{\mathrm{TJ}}\). Filtering such an edge by incidence of the outgoing and incoming cage vertices produces exactly \(55{,}440\) edges of \(R_{\mathrm{TS}}\). Standard full breadth-first search from a base verifies that each graph reaches all \(32{,}460\) states, hence is connected.
3. Permuting the six symbols maps duads to duads and synthemes to synthemes and preserves their incidence, hence is an automorphism of \(T\), and therefore of both relocation graphs. The five adjacent transpositions generate \(S_6\); their explicit permutations of all thirty vertices are checked edge by edge. Orbit closure under these generators partitions **all** bases into the \(62\) listed orbits. Since a graph automorphism preserves distances and eccentricity, a breadth-first search from one representative of each orbit, testing reachability of all states, suffices to determine every state's eccentricity. Those \(62\) complete searches give the stated distributions, radii and diameters for both relocation rules. Exactly one jump orbit has eccentricity \(8\) and it has size \(720\).
4. An independently constructed representation uses the fifteen nonzero vectors of the symplectic space \(\mathbb F_2^4\) and its fifteen totally isotropic two-dimensional subspaces; the associated point–line incidence graph is an alternative model of the same generalized quadrangle of order \((2,2)\). In that implementation, resolution is checked from distinct distance **signatures** rather than pair-separation masks. Jump edges are constructed by grouping bases according to their common five-element subsets, and slide edges by direct replacement along incident cage edges. Symplectic transvections replace the six-symbol generators for the orbit argument. This second program independently reproduces all counts, orbits, connectedness assertions and both eccentricity distributions.

A printed log alone is not the proof: the two fully provided programs enumerate the finite quantifiers, assert the critical invariants, and terminate only after their tests pass.

## Verification

Run `python3 verify_metric_A.py` and `python3 verify_metric_B.py` in a Python 3 environment using only its standard library. They require no input files or external packages. Their complete captured outputs are `verify_metric_A.out` and `verify_metric_B.out`. All exact assertions were successfully replayed from these same source files; the final markers are `VERIFY_OK` and `INDEPENDENT_VERIFY_OK` (the latter denotes a second computational method, **not** an external audit).

The labels of the two constructions need not coincide: all reported graph invariants are isomorphism invariant. The six-symbol construction provides an explicit representative \((0,1,12,15,21,22)\) of the unique maximal-eccentricity jump orbit in the vertex ordering induced by lexicographic duads followed by generated synthemes; the tuple is not asserted to be canonical independently of this enumeration.

## Relationship to prior work

Bailey's 2013 paper [1], especially its distance-regular-graph tables and orbit-reduced metric-dimension method, already gives the Tutte eight-cage's **metric dimension of six**. That value and the notion of a resolving set are not new claims. Bartoli and collaborators [2] study metric dimensions and bounds for generalized quadrangles, again without the enumerated pair of relocation graphs above. General work and presentations on metric-basis reconfiguration [3,4] motivate the token-jump and token-slide questions but do not, in the material inspected, provide the cage's counts, connectedness or distance spectra. The theorem adds the full count of minimum bases, their natural-orbit decomposition, and exact relocation graph statistics, not a restatement of those general results.

A published-record similarity search located works on Tutte–Coxeter homology, independence complexes and topological invariants, and other works on resolving sets of different graph families; none of those scientific statements covers the explicit minimum-basis relocation classification. A failed retrieval or missing search hit alone is not proof of originality.

## Limitations

The result concerns one precisely defined thirty-vertex graph and two moves preserving **minimum** resolving-set cardinality, not all generalized quadrangles, all resolving-set sizes, or arbitrary simultaneous moves. The exhaustive algorithms are finite proofs for this graph and do not establish an infinite-family theorem. The known minimum cardinality of six is acknowledged as prior literature. A 2026 thesis on metric-basis reconfiguration [4] was listed but its complete text was not available for detailed comparison; unpublished or unindexed overlapping computations remain a residual originality risk. No external independent scientific audit has been performed.

## References

[1] R. F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, arXiv:1312.4973v1, originally posted 2013-12-17. https://arxiv.org/abs/1312.4973

[2] D. Bartoli et al., *On the metric dimension of affine planes, biaffine planes and generalized quadrangles*, arXiv:1706.06583v1, originally posted 2017-06-20. https://arxiv.org/abs/1706.06583

[3] *Metric Basis Reconfiguration*, California State Polytechnic University, Pomona, project description. https://www.cpp.edu/camp-reu/research_projects.shtml

[4] B. A. Foster-Greenwood, *Student Research*, listing J. Morentin, *Reconfigurations of Metric Bases* (2026 thesis). https://www.cpp.edu/faculty/brianaf/student-research.shtml
