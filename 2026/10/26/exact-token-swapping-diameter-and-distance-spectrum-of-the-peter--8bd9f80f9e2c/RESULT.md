# Exact token-swapping diameter and distance spectrum of the Petersen graph

## Finding

Let \(P\) be the Petersen graph on ten vertices and let \(\Gamma(P)\) be the graph on the \(10!\) permutations of distinct tokens, where two configurations are adjacent if one is obtained from the other by swapping the tokens at the endpoints of an edge of \(P\). Then

\[\operatorname{diam}(\Gamma(P))=13.\]

Write \(h_k=|\{\pi\in S_{10}:d_{\Gamma(P)}(e,\pi)=k\}|\). The complete distance-shell vector is

\[(h_0,\ldots,h_{13})=(1,15,135,955,5504,26096,99739,297535,655169,984833,923838,493350,130014,11616).\]

The final shell has \(11616\) permutations, partitioned by permutation cycle type as follows:

| Cycle lengths | Count |
| --- | ---: |
| \((10)\) | 5832 |
| \((2,2,2,2,2)\) | 24 |
| \((4,3,3)\) | 960 |
| \((4,4,2)\) | 960 |
| \((5,3,2)\) | 2280 |
| \((6,2,2)\) | 1320 |
| \((6,3,1)\) | 240 |

For the natural transport lower bound
\[L(\pi)=\left\lceil\frac12\sum_{v\in V(P)}d_P(v,\pi(v))\right\rceil,\]
where \(\pi(v)\) is the label of the token at vertex \(v\), the exact gap \(d_{\Gamma(P)}(e,\pi)-L(\pi)\) has values \(0,1,2,3,4\) with respective multiplicities
\[(431532,1509516,1382012,299060,6680).\]
Thus the largest excess over the transport lower bound is exactly \(4\).

## Assumptions and scope

All graphs are undirected, simple, and unweighted. Explicitly use vertices \(\{0,\ldots,9\}\). For \(i\in\{0,\ldots,4\}\) with subscripts reduced modulo \(5\), put in the outer edge \(\{i,i+1\}\), spoke \(\{i,i+5\}\), and inner edge \(\{i+5,5+(i+2)\}\). These \(15\) edges define \(P=GP(5,2)\).

A token placement is a bijection \(\pi:V(P)\to V(P)\). Vertex \(v\) contains token \(\pi(v)\), whose destination is vertex \(\pi(v)\); the target placement is the identity \(e\). One move exchanges \(\pi(u)\) and \(\pi(v)\) for exactly one \(\{u,v\}\in E(P)\). Every pair of placements has the same relative-word metric as identity-to-a-permutation in the Cayley graph, by left translation in the group. Hence the radius from \(e\) equals the full graph diameter.

The Kneser realization \(P\cong KG(5,2)\) is the disjointness graph on the ten two-subsets of a five-element set. The independent implementation builds this model afresh rather than reusing the generalized-Petersen edge generator.

## Proof

**Permutation coding.** Fix the order \(0,1,\ldots,9\). The standard factorial-radix ranking is a bijection from permutations to integers \(0\) through \(10!-1\): the digit for position \(i\) is the number of as-yet-unused labels smaller than \(\pi(i)\), multiplied by \((9-i)!\). Its inverse successively selects the indicated unused label. This is an exact enumeration, not a random sample.

**Transition.** Given any ranked permutation, decode it and, for each of the exactly \(15\) edges \(\{u,v\}\), exchange the two coordinates, re-rank the resulting placement, and add the corresponding undirected adjacency. Every permitted one-step move arises exactly this way, and no forbidden move is added.

**Distances.** Start a FIFO breadth-first search at the identity. Mark a state with its queue depth at first discovery. By induction on depth, a discovered state has a path of that length and no path of a smaller length: all lower-depth states are dequeued before any higher-depth state is first reached. The recorded queue visits all \(3{,}628{,}800=10!\) states, so there are no omitted placements or disconnected components. Exact layer counters, checked against the hard-coded values by `verify_gp.cpp`, give the stated shell vector; its largest nonempty index is \(13\). Left translation makes the Cayley graph vertex transitive, so \(13\) is the diameter, not merely the eccentricity of one arbitrarily chosen state.

**Extremal types and transport gap.** For every state in layer \(13\), follow the cycles of the permutation and sort the cycle lengths. Exact counters yield the seven stated types, summing to \(11616\). For each permutation, compute shortest-path distances in the fixed ten-vertex graph by the all-pairs Floyd--Warshall recurrence. Each edge swap moves only two tokens, changing each token's distance from its target by at most one, hence at most two units of total transport distance can be saved per swap. This proves \(d_{\Gamma(P)}(e,\pi)\geq L(\pi)\). Subtracting this bound from the enumerated exact distances gives the five gap counts above. One explicit diametral placement, in vertex order, is \((0,3,8,6,5,1,7,4,9,2)\): its sum of individual target distances equals \(18\), its transport lower bound is \(9\), and its exact swapping distance is \(13\).

## Verification

Two independently implemented, standalone C++17 programs are included. Run `g++ -O3 -std=c++17 verify_gp.cpp -o check_gp && ./check_gp` and separately `g++ -O3 -std=c++17 verify_kg.cpp -o check_kg && ./check_kg`. Each must terminate successfully with `VERIFY_OK`. The first uses ten-vertex generalized-Petersen edges, the Lehmer rank of token-at-vertex permutations, and direct exchange of coordinates. The second constructs the Kneser graph from all two-subsets of a five-element set, ranks inverse permutations (positions of tokens), and effects swaps by exchanging **values**, not array positions. The latter independently reproduces all shells, all extremal cycle-type counts, and all transport-gap multiplicities.

The first implementation also validates rank/unrank on all \(10!\) indices. The two state encodings, distinct graph constructions and move implementations provide cross-checks against a single accidental adjacency convention. A valid explicit isomorphism from the generalized-Petersen vertex order to the lexicographically ordered Kneser two-subsets is \((0,7,3,4,9,8,6,5,2,1)\).

## Relationship to prior work

Yamanaka et al., *Swapping Labeled Tokens on Graphs* (FUN 2014), define the adjacent-swap task and provide general and special-class algorithms, including the complete-bipartite case. The primary PDF's sections on the model, tree approximation, tree-spanner approximation and complete bipartite graphs do not state Petersen-specific exact distances. The work *Diameter of Cayley graphs of permutation groups generated by transposition trees* (arXiv:1111.3114) addresses generating **trees**, while the Petersen generating graph has \(15\) edges on \(10\) vertices and contains cycles. Bonnet, Miltzow and Rzążewski, arXiv:1607.07676, give general complexity and search algorithms rather than the exact Petersen spectrum. Kim's 2016 review describes paths, stars, cliques and rings, rather than this graph; its complete readable manuscript was not available during this comparison. These general results are credited and not relabelled as new.

## Limitations

This is a finite exact computation for the Petersen graph only. It does not give a uniform theorem for arbitrary cubic graphs or larger generalized Petersen graphs, nor a closed-form distance formula for each permutation beyond the reproducible BFS. Searching records and accessible literature cannot exclude an older unindexed numeric census or computation in inaccessible material. The verification is computational and independently reproducible, but has not undergone independent external audit.

## References

1. Katsuhisa Yamanaka et al., *Swapping Labeled Tokens on Graphs*, FUN 2014, pp. 364–375, DOI: 10.1007/978-3-319-07890-8_31. Public conference July 1–3, 2014. Primary PDF: https://erikdemaine.org/papers/TokenReconfiguration_FUN2014/paper.pdf
2. *Diameter of Cayley graphs of permutation groups generated by transposition trees*, arXiv:1111.3114, https://arxiv.org/abs/1111.3114
3. Édouard Bonnet, Tillmann Miltzow and Paweł Rzążewski, *Complexity of Token Swapping and its Variants*, arXiv:1607.07676, https://arxiv.org/abs/1607.07676
4. Dohan Kim, *Sorting on graphs by adjacent swaps using permutation groups*, Computer Science Review 22 (2016), pp. 89–105, DOI: 10.1016/j.cosrev.2016.09.003.
