# Independent mathematical audit

## correctness

PASS

For p_n=(log n+t)/n with fixed real t, union-bound counting of reachable sets of sizes 2..floor(n/2), each with an out-arborescence and no outgoing edge, gives o(1) probability that any positive-outdegree vertex has at most half the graph reachable. The reversed statement holds for predecessor sets. Two sets exceeding n/2 intersect, yielding the exact all-pairs relation uRv iff u=v or outdeg(u)>0 and indeg(v)>0 a.a.s. Mixed factorial moments of zero indegrees/outdegrees tend to lambda^(a+b), lambda=e^-t; overlap patterns are lower order and hence independent Poisson limits follow. The resulting O_P(1) initial/final singleton layers and one large middle equivalence class give automorphism groups and a first-order convergence mixture by a quantifier-rank Ehrenfeucht–Fraïssé game with sufficiently large indistinguishable middle layers. The source finite verifier was inspected; it checks small directed-graph consequences, not asymptotic correctness.

## originality

PASS

Karp (1990) studies transitive closure of random digraphs with giant-component regime but the full paper was inaccessible and might have stronger threshold results. Pittel–Poole (2014) analyze the giant strong component at fixed np>1, rather than the near-connectivity logarithmic window. Bal et al. (2014) cover spanning-arborescence thresholds in a different random colored digraph setting. None of the materially inspected results gave the precise three-layer all-pairs preorder, independent Poisson layer decoration and full FO convergence law. Best-of-knowledge, with explicit historical Karp risk.

## value

PASS

The theorem gives an exact canonical random S4-frame structure with probabilistic exceptional layers and a complete first-order convergence law, bridging random directed-graph connectivity and finite-model theory. Its concrete limit mixture and automorphism description are natural and genuinely more informative than a single connectivity probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
