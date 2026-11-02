# Scientific review: random-edge matching on complete split graphs

## Correctness (PASS)

The exact state space is \((x,y)\) with \(\binom{x}{2}\) internal and \(xy\) cross edges. The finite recursion covers the boundary \(x=1,y>0\), where a cross edge remains mandatory. It was independently checked against all full labeled-edge permutations in small test graphs. The deterministic ODE has invariant \(x/y-\log(y/\beta)\), giving the residual \(\beta e^{-\alpha/\beta}\). The proof carries the central limit theorem to actual termination, including its vanishing remaining quadratic-variation bound, and evaluates variance explicitly. Independent seeded simulations corroborate, but are not used to prove, the infinite-size results. The benchmark maximum matching size is \(\min\{a,\lfloor(a+b)/2\rfloor\}\); its ratio has a unique minimum at equal part sizes.

## Originality (PASS, historically qualified)

The closest fully inspected primary work is Arnosti (2021), DOI 10.1287/stsy.2021.0082, a comparison of algorithms for random bipartite graphs. Its full open-access PDF and proofs do not analyze the deterministic complete split graph, which has clique edges and is nonbipartite. Dyer and Frieze (1991), DOI 10.1002/rsa.3240020104, study general randomized matching and worst-case bounds, and Dyer, Frieze and Pittel (1993), DOI 10.1214/aoap/1177005436, study sparse random graphs and random trees. Their accessible abstracts do not imply the displayed dense-split-graph central limit theorem or sharp \(1-1/(2e)\) family bound; their complete text was not accessible, leaving an expressly unresolved historical-priority risk. Published semantic comparisons and earlier related claims were checked for matching objects, asymptotic parameters, equivalence through line graphs, and stronger general statements; no covering statement was identified. This is evidence of noncoverage within the inspected material, not proof of unique historical priority.

## Value (PASS)

Complete split graphs are a canonical class interpolating between cliques and complete bipartite graphs. The random-edge heuristic may leave a positive *linear* number of peripheral vertices unmatched even when a perfect matching exists. The unique sharp performance threshold quantifies its worst loss on this natural graph family; the explicit Gaussian variance additionally quantifies finite-sample uncertainty. The result is not a simple relabeling of the bipartite matching process, because clique-clique matches permanently squander potential partners for the independent vertices.

## Closest sources and limitations

Arnosti (2021), https://doi.org/10.1287/stsy.2021.0082 ; Dyer and Frieze (1991), https://doi.org/10.1002/rsa.3240020104 ; Dyer, Frieze and Pittel (1993), https://doi.org/10.1214/aoap/1177005436 ; Krivelevich et al. (2020), https://doi.org/10.4230/LIPIcs.AofA.2020.20 . General bounded-degree/local-limit matching arguments do not directly provide a dense complete-split fluctuation law. The result assumes positive limiting part densities and uniform admissible-edge selection. Unbounded aspect ratios, adversarial edge order, and all noncomplete split graphs remain outside the theorem. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
