# The house graph is the unique first high-degree seeding failure under strict-majority diffusion
## Finding
Let \(G=(V,E)\) be a connected finite simple undirected graph. Give every vertex the strict-majority threshold
\[
\tau(v)=\left\lceil\frac{\deg(v)+1}{2}\right\rceil.
\]
Starting from a seed set \(S\), activation is progressive and irreversible: an inactive vertex becomes active as soon as at least \(\tau(v)\) of its neighbors are active, and active vertices remain active. Let
\[
\sigma_G(S)
\]
be the number of active vertices when the process stops.

For a seed budget of exactly two vertices, call the **high-degree pair** unambiguous when there is a unique pair maximizing
\[
\deg(u)+\deg(v).
\]
Equivalently, after ordering the degrees nonincreasingly, the second-largest degree is strictly larger than the third-largest degree.

For every connected graph on at most \(4\) vertices whose high-degree pair is unambiguous, that pair maximizes \(\sigma_G(S)\) over all two-vertex seed sets.

The statement is sharp at \(5\) vertices. Among the
\[
728
\]
labeled connected graphs on \(5\) vertices, exactly
\[
290
\]
have an unambiguous high-degree pair. In exactly
\[
60
\]
of those graphs, the high-degree pair is strictly suboptimal. Hence the unconditional incidence is
\[
\frac{60}{728}=\frac{15}{182},
\]
and the incidence conditional on an unambiguous high-degree pair is
\[
\frac{60}{290}=\frac6{29}.
\]

All \(60\) failures form one isomorphism class: the house graph. Its orbit has size
\[
60=\frac{5!}{2},
\]
so its automorphism group has order \(2\).

A representative on vertices \(0,1,2,3,4\) has
\[
E=\{01,03,04,12,14,23\}.
\]
This is a \(4\)-cycle \(0-3-2-1-0\) with the roof vertex \(4\) adjacent to \(0\) and \(1\). Its degree vector is
\[
(3,3,2,2,2),
\]
so every vertex has strict-majority threshold \(2\), and the unique high-degree pair is
\[
H=\{0,1\}.
\]

Seeding \(H\) activates vertex \(4\), but neither \(2\) nor \(3\) ever receives two active neighbors. Thus
\[
\sigma_G(\{0,1\})=3.
\]
By contrast,
\[
\sigma_G(\{0,2\})=
\sigma_G(\{1,3\})=
\sigma_G(\{2,4\})=
\sigma_G(\{3,4\})=5.
\]
Therefore the unique high-degree choice reaches only three fifths of the graph while an optimal two-seed set activates every vertex.

The two-seed budget is the first nondegenerate budget for strict-majority interaction: from one seed, no vertex of degree at least \(2\) can activate. The house obstruction therefore identifies the first graph order at which a genuinely social-reinforcement cascade makes the standard unambiguous high-degree heuristic fail.

## Assumptions and scope
Graphs are finite, simple, undirected, connected, and labeled when labeled counts are stated.

The process is progressive and irreversible. All vertices use the strict-majority threshold
\[
\tau(v)=\left\lceil\frac{\deg(v)+1}{2}\right\rceil.
\]

The seed budget is exactly two. The high-degree heuristic chooses vertices in decreasing degree order; the theorem restricts to graphs for which its two-vertex choice is unambiguous.

The objective is final cascade cardinality, not activation time.

The theorem does not claim that high-degree seeding is optimal for larger graphs, different thresholds, different seed budgets, directed or weighted networks, or nonprogressive dynamics.

## Proof
For \(2\) vertices, the only connected graph is \(K_2\), and the unique two-seed set is trivially optimal.

For \(3\) vertices, neither connected isomorphism type has an unambiguous high-degree pair. In \(P_3\), the second seed is tied between the two leaves; in \(K_3\), all vertices tie.

For \(4\) vertices, there are six connected unlabeled graphs. Exactly two have an unambiguous high-degree pair:
- \(P_4\), whose two internal vertices are the unique high-degree pair;
- \(K_4\) with one edge deleted, whose two degree-\(3\) vertices are the unique high-degree pair.

Under strict-majority activation, the high-degree pair activates all four vertices in each case. Hence no smaller connected graph can be a counterexample.

For \(5\) vertices, the verifier exhausts all
\[
2^{\binom52}=1024
\]
labeled simple graphs and retains the
\[
728
\]
connected ones. Exactly \(290\) have an unambiguous high-degree pair. Their high-degree-pair spread versus optimal two-seed spread is distributed as
\[
(5,5):230,\qquad (3,5):60.
\]
Thus every first failure is as strong as possible at this order: the heuristic stalls at \(3\), while another pair activates all \(5\) vertices.

Canonicalization under all \(5!\) vertex permutations maps all \(60\) failures to the same canonical graph
\[
\{01,03,04,12,14,23\}.
\]
Its relabeling orbit has size \(60\), so the entire failure set is exactly the orbit of the house graph.

On this representative, the high-degree pair \(\{0,1\}\) has both degree-\(3\) vertices. Because all strict-majority thresholds equal \(2\), vertex \(4\) activates from those two seeds, after which the process stops at \(\{0,1,4\}\).

For the pair \(\{0,2\}\), vertices \(1\) and \(3\) each have two active neighbors and activate; then vertex \(4\) has two active neighbors and activates. Hence all five vertices become active. The other three optimal pairs listed in the Finding are verified identically by exact closure computation.

## Verification
The embedded `verify_strict_majority_high_degree_boundary.py` uses only the Python standard library.

It independently verifies connectivity by breadth-first search and transitive-closure computation.

It computes every strict-majority cascade in two independent ways:
1. synchronous round-by-round activation;
2. a queue-based incremental active-neighbor-count algorithm.

The two closures agree for every two-seed set in every connected labeled graph through \(5\) vertices.

It verifies:
- connected labeled graph counts \(1,4,38,728\) for orders \(2,3,4,5\);
- unambiguous high-degree-pair counts \(1,0,18,290\);
- suboptimal high-degree-pair counts \(0,0,0,60\);
- the five-vertex distribution \((5,5):230\) and \((3,5):60\);
- exactly seven five-vertex isomorphism classes with an unambiguous high-degree pair;
- exactly one failing class;
- the house edge set \(\{01,03,04,12,14,23\}\);
- house orbit size \(60\) and automorphism-group order \(2\);
- high-degree-pair spread \(3\);
- optimal spread \(5\);
- the four optimal seed pairs listed above.

Run:

`python3 verify_strict_majority_high_degree_boundary.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Kempe, Kleinberg, and Tardos formulate influence maximization as choosing a fixed-size seed set to maximize eventual spread. They explicitly describe the high-degree heuristic as choosing vertices in decreasing degree order and report that it can be outperformed because network effects are not accurately reflected by degree alone. Their classical linear-threshold formulation uses random thresholds, while also noting work with thresholds hard-wired near one half.

Khoshkhah, Soltani, and Zaker study the progressive irreversible threshold process on finite simple graphs with the exact strict-majority threshold
\[
\tau(v)=\left\lceil\frac{\deg(v)+1}{2}\right\rceil,
\]
and identify the model with irreversible influence spread in social networks. Their results concern the size and existence of dynamic monopolies, not the performance of the degree-ordered two-seed heuristic.

The checked literature therefore already establishes both ingredients of the comparison: high-degree seeding is a standard influence heuristic, and strict-majority progressive diffusion is a standard threshold model. The contribution here is restricted to the sharp finite boundary and complete first obstruction layer: no unambiguous high-degree failure through four vertices, exactly \(60\) labeled failures at five vertices, and one isomorphism type, the house graph.

Targeted searches using high-degree, degree-centrality, strict-majority, dynamic-monopoly, influence-maximization, two-seed, five-vertex, and house-graph formulations did not locate this exact boundary or census.

## Limitations
The result is restricted to connected simple undirected graphs and the strict-majority threshold.

The seed budget is fixed at two. This is mathematically motivated as the first budget at which a seed set can jointly satisfy the threshold of a degree-\(2\) vertex, but no statement is made for other budgets.

The exact census stops at five vertices. No density, asymptotic, or approximation-ratio claim is made for larger networks.

The result concerns final spread only; it does not compare activation times among optimal seed sets.

An unindexed small-graph table, software corpus, thesis appendix, or teaching example could contain the same house-graph obstruction.

## References
1. D. Kempe, J. Kleinberg, and É. Tardos, “Maximizing the Spread of Influence through a Social Network,” *Proceedings of KDD 2003*, 137–146, 2003. DOI: 10.1145/956750.956769.
2. K. Khoshkhah, H. Soltani, and M. Zaker, “On dynamic monopolies of graphs: the average and strict majority thresholds,” arXiv:1202.1146, first submitted 6 February 2012; *Discrete Optimization* 9 (2012), 77–83. DOI: 10.1016/j.disopt.2012.02.001.
