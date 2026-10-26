# Exact token-swapping distances on the eight-vertex Wagner graph

## Finding
Let \(W\) be the eight-vertex Wagner graph, also called the Möbius ladder \(M_8\). Let \(\Gamma(W)\) be the graph of permutations of eight different tokens on its vertices, where one move swaps the tokens at an edge. Its diameter is exactly
\[
\operatorname{diam}\Gamma(W)=10.
\]
The exact distance-shell counts from any configuration, listed for distances \(0\) through \(10\), are
\[
(1,12,90,500,2059,5960,11124,11986,6748,1702,138).
\]
In particular, exactly \(138\) token configurations require ten swaps. For each permutation \(p\) put \(L(p)=\left\lceil\sum_{i=0}^{7}d_W(i,p(i))/2\right\rceil\). The multiplicities of \(\operatorname{dist}_{\Gamma(W)}(\mathrm{id},p)-L(p)\), for gaps \(0,1,2,3\), are
\[
(16350,18574,5322,74).
\]
Among the \(138\) diametral permutations, \(48\) have total token transport distance \(15\) and \(90\) have total token transport distance \(16\).

## Assumptions and scope
The vertex set is \(\mathbb Z/8\mathbb Z\), represented by the integers \(0,\ldots,7\). Edges join each vertex \(i\) to \(i+1\) and \(i+4\), with indices reduced modulo eight. This yields twelve different undirected edges. All tokens are distinct; a configuration is a bijection \(p\) in which the token at vertex \(i\) has label \(p(i)\). The target is the identity configuration. The shortest-path distance is the minimum number of sequential (one-edge-at-a-time) swaps; parallel swapping rounds and indistinguishable or partly colored tokens are excluded. The statement concerns the single finite Wagner graph and does not assert a formula for all Möbius ladders.

## Proof
Each allowed move composes a token assignment with one transposition \((i\ j)\) indexed by an edge \(\{i,j\}\) of \(W\). Because \(W\) is connected, these transpositions generate the full symmetric group on eight tokens, so every state is reachable. Relabeling all tokens is an automorphism of the reconfiguration graph. It therefore suffices to determine every distance from the identity configuration.

The standalone Python verifier `verify_wagner.py` explicitly constructs all twelve permitted edges, and uses two separately encoded breadth-first traversals: a direct permutation-tuple dictionary, and a dense array whose keys are factorial-system (Lehmer) ranks. Each traverses all \(8!=40320\) distinct bijections. Every transition is one allowed edge swap, so the standard breadth-first queue invariant gives the exact minimum length for each reached configuration: upon first discovery, a state has a path of that length, and no shorter path can have been missed because all previous layers were processed earlier. Equality of total visited count with \(8!\) establishes exhaustive coverage. Both traversals agree pointwise at every permutation. The counted layers are exactly those displayed above; the last nonempty layer is ten and has \(138\) elements. These observations prove the diameter and its multiplicity.

For the transport statement, each swap can reduce the sum of graph distances from current tokens to their home vertices by at most two. Hence \(L(p)\) is a valid integer lower bound for every permutation. The verifier independently constructs all eight shortest-path vertex-distance rows in \(W\) and evaluates \(L(p)\) for every one of the \(40320\) states, comparing them with the exhaustive optimal swap distances. The complete gap counts and diametral total-transport breakdown are the results recorded in the finding.

## Verification
Run `python3 verify_wagner.py` with Python 3.10 or later and no external packages. Successful execution prints both distance and transport distributions and ends in `VERIFY_OK`. The verifier checks the factorial-rank unranking inverse, all states, the two complete distance arrays, the largest shell, and all bound-gap counts. A failed assertion means a claimed finite enumeration check did not pass. Both methods share the underlying graph definition and arithmetic, so they are independent encodings of the finite traversal rather than formal verification by a separate theorem prover.

## Relationship to prior work
The general token-swapping model, including individual labeled tokens and one-edge exchanges, appears in Yamanaka et al. (2014). That paper's primary results concern general bounds and algorithms on trees, graphs with tree spanners, and complete bipartite graphs, and give only an asymptotic hypercube discussion. An exact \(40320\)-permutation distance-shell profile for the **different** three-dimensional cube graph occurs in Zheng's 2009 reversible-circuit thesis, table 4.2; that cube profile is prior work, not claimed as new. In fact, the cube is bipartite while \(W\) contains odd cycles, so the twelve transposition generators represent different labeled base graphs, and the exact profiles differ beginning at distance three. The graph under study here is a canonical eight-vertex nonbipartite cubic graph. Earlier perfect-matching flip-graph results on Möbius ladders concern different states and moves and do not give the stated token-swap metric.

## Limitations
This is an exact finite state-space enumeration, not an asymptotic or infinite-family result. Breadth-first enumeration proves the displayed finite claim because all bijections are exhausted; partial experiments outside this eight-vertex graph imply nothing about larger ladders. A previously unindexed word-metric table could cover the same invariant; database searches are evidence rather than proof of novelty. Independent external validation has not been performed.

## References
1. K. Yamanaka et al., *Swapping Labeled Tokens on Graphs*, Fun with Algorithms, 2014. https://erikdemaine.org/papers/TokenReconfiguration_FUN2014/paper.pdf
2. Y. Zheng, *Circuit Design Methods with Emerging Nanotechnologies*, PhD dissertation, Virginia Tech, 2009, section 4.5.1 and Table 4.2. https://vtechworks.lib.vt.edu/bitstreams/30b5a77f-30e6-41c2-86b7-6880babd7a88/download
3. É. Bonnet, T. Miltzow, and P. Rzążewski, *Complexity of Token Swapping and its Variants*, arXiv:1607.07676, 2016. https://arxiv.org/abs/1607.07676
4. N. Alon, F. R. K. Chung, and R. L. Graham, *Routing Permutations on Graphs via Matchings*, 1994. https://epubs.siam.org/doi/abs/10.1137/S0895480192236628
