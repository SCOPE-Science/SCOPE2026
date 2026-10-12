# Seven vertices are the sharp unique-leader split for closeness and harmonic centrality
## Finding
Let \\(G=(V,E)\\) be a connected finite simple undirected graph. Define the classical closeness score by
\\[
C(v)=\\frac{1}{\\sum_{u\\ne v}d(u,v)},
\\]
and harmonic centrality by
\\[
H(v)=\\sum_{u\\ne v}\\frac{1}{d(u,v)}.
\\]
Positive normalizations do not change either maximizing set.

If both \\(C\\) and \\(H\\) have unique maximizing vertices and
\\[
|V|\\le 6,
\\]
then those two vertices are the same.

This is sharp. At order \\(7\\), exactly two connected unlabeled graph classes have distinct unique leaders. Representatives on vertices \\(0,\\ldots,6\\) have edge sets
\\[
E_1=\\{03,13,14,24,25,26\\},
\\]
and
\\[
E_2=\\{04,12,13,25,26,34,56\\}.
\\]
For \\(E_1\\), vertex \\(4\\) is the unique closeness leader and vertex \\(2\\) is the unique harmonic leader. For \\(E_2\\), vertex \\(1\\) is the unique closeness leader and vertex \\(2\\) is the unique harmonic leader.

Despite the two graphs being nonisomorphic, the competing leaders have exactly the same two distance profiles in both classes. The closeness leader has distance multiset
\\[
(1,1,2,2,2,3),
\\]
so its farness is \\(11\\) and its harmonic score is
\\[
2+\\frac32+\\frac13=\\frac{23}{6}.
\\]
The harmonic leader has distance multiset
\\[
(1,1,1,2,3,4),
\\]
so its farness is \\(12\\) but its harmonic score is
\\[
3+\\frac12+\\frac13+\\frac14=\\frac{49}{12}>\\frac{23}{6}.
\\]
Thus the first unambiguous split has a transparent cause: harmonic centrality rewards the extra immediate neighbor enough to offset one much more distant vertex, while closeness prefers the smaller total distance.

Each first-conflict graph has automorphism group of order \\(2\\), hence each has labeled orbit size
\\[
\\frac{7!}{2}=2520.
\\]
Together they yield exactly
\\[
5040
\\]
labeled first-conflict graphs, an incidence of
\\[
\\frac{5040}{1{,}866{,}256}=\\frac{45}{16663}
\\]
among connected labeled graphs on seven vertices.

There is a weaker tie-level separation one order earlier. At order \\(6\\), exactly three connected unlabeled graph classes have different closeness- and harmonic-maximizing sets. Their orbit sizes are \\(360,180,360\\), totaling \\(900\\) labeled graphs, but none has distinct unique leaders under both measures.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected.

Closeness is the reciprocal of the sum of shortest-path distances. Harmonic centrality is the sum of reciprocals of shortest-path distances. On connected graphs both are finite; multiplying either score by a positive order-dependent normalization leaves the maximizing set unchanged.

The sharp statement concerns distinct singleton maximizing sets. Set-valued disagreement already occurs at six vertices because one measure can refine a tie of the other.

The exhaustive classification ends at seven vertices. No larger-order frequency or structural classification is claimed.

## Proof
The proof is a complete finite classification over the connected portion of the Read--Wilson Graph Atlas through seven vertices.

The embedded table contains every connected unlabeled graph on \\(2\\) through \\(7\\) vertices, with counts
\\[
1,\\ 2,\\ 6,\\ 21,\\ 112,\\ 853.
\\]
For each graph, all-pairs shortest-path distances are reconstructed independently by breadth-first search from every source and by Floyd--Warshall; the two distance matrices agree exactly.

From each exact distance matrix, the verifier computes the farness
\\[
F(v)=\\sum_{u\\ne v}d(u,v)
\\]
and harmonic score
\\[
H(v)=\\sum_{u\\ne v}\\frac1{d(u,v)}
\\]
using exact rational arithmetic. Maximizing closeness is equivalent to minimizing \\(F(v)\\).

For graph orders \\(2,3,4,5\\), the maximizing sets always agree. At order \\(6\\), exactly three unlabeled classes have different maximizing sets, but in every such class at least one maximizing set has more than one vertex. At order \\(7\\), there are \\(22\\) unlabeled set-valued disagreements, of which exactly two have both maximizing sets singleton and distinct.

Direct evaluation of the two singleton-conflict representatives gives the leader distance profiles and exact scores displayed above. Full permutation checks show that each representative has exactly two automorphisms, hence orbit size \\(2520\\). Since the two classes are nonisomorphic, the total labeled count is \\(5040\\).

For the three six-vertex tie-level classes, the same permutation check gives orbit sizes \\(360,180,360\\), totaling \\(900\\).

## Verification
The embedded `verify_closeness_harmonic_boundary.py` uses only the Python standard library and the embedded `graph_atlas_connected_2to7.json` table.

It verifies:
- connected unlabeled graph counts \\(1,2,6,21,112,853\\);
- equality of independent BFS and Floyd--Warshall distance matrices;
- exact rational closeness and harmonic maximizing sets;
- set-disagreement class counts \\(0,0,0,0,3,22\\) for orders \\(2,\\ldots,7\\);
- distinct-unique disagreement counts \\(0,0,0,0,0,2\\);
- the two displayed seven-vertex representatives;
- identical competing-leader distance profiles in both representatives;
- exact scores \\(11,23/6\\) for each closeness leader and \\(12,49/12\\) for each harmonic leader;
- orbit sizes \\(2520,2520\\), hence total \\(5040\\);
- six-vertex tie-level orbit sizes \\(360,180,360\\), hence total \\(900\\).

Run:

`python3 verify_closeness_harmonic_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Marchiori and Latora replace arithmetic averaging of graph distances by a harmonic construction in their small-world efficiency framework; the public arXiv version dates to 24 August 2000. Boldi and Vigna later present harmonic centrality explicitly as a distance-based correction to classical closeness, motivated especially by disconnected networks and axiomatic behavior.

A highly relevant recent paper by Madaras and Paralič studies harmonic centers themselves. Its full text defines harmonic centrality and classical closeness side by side, states that local graph-theoretic properties of harmonic centrality have not been explored in detail, and develops realizability and localization results for harmonic centers. It does not state the smallest order at which harmonic and closeness centers choose different unique vertices, nor a complete small-order census.

The accepted contribution is therefore restricted to the sharp finite comparison of the two center notions: coincidence of unique leaders through six vertices, exactly two seven-vertex first-conflict classes, and the common pair of competing distance profiles that explains the split.

Targeted searches using `harmonic center`, `closeness center`, `unique maximizer`, `smallest graph`, `seven vertices`, the two distance profiles, and the exact labeled count did not locate an equivalent statement.

## Limitations
The Graph Atlas input is an externally curated complete list through seven vertices rather than a graph generator proved complete inside the package. Every scientific calculation on that input is independently replayed.

The result is restricted to connected simple undirected graphs and to the standard unweighted distance definitions.

The recent 2026 harmonic-center literature is close in topic and creates residual novelty risk even though its inspected full text does not state this boundary.

An unindexed graph atlas annotation, thesis appendix, software corpus, or teaching enumeration could contain the same finite observation.

## References
1. M. Marchiori and V. Latora, “Harmony in the Small-World,” arXiv:cond-mat/0008357, first submitted 24 August 2000; *Physica A* 285 (2000), 539–546. DOI: 10.1016/S0378-4371(00)00311-3.
2. P. Boldi and S. Vigna, “Axioms for Centrality,” arXiv:1308.2140, first submitted 9 August 2013; *Internet Mathematics* 10 (2014), 222–262. DOI: 10.1080/15427951.2013.865686.
3. T. Madaras and M. Paralič, “On harmonic centers of graphs,” arXiv:2609.31295, first submitted 25 September 2026.
4. R. C. Read and R. J. Wilson, *An Atlas of Graphs*, Oxford University Press, 1998.
