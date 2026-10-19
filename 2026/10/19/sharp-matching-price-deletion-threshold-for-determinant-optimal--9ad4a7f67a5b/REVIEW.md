# Review of the determinant-optimal bipartite conductance theorem

## Correctness — PASS
A positive tree-count candidate exists for every \(n\ge3\); strict log-determinant concavity and an injective grounded-Laplacian parametrization force a unique global optimum over independently controlled weights. The matching-preserving graph automorphism group reduces that optimum to two edge orbits without assuming the answer. Direct eigenspace decomposition gives \(0\), \(2[a+(n-1)b]\), \(nb\) with multiplicity \(n-1\), and \(2a+(n-2)b\) with multiplicity \(n-1\). Applying weighted matrix-tree and the exact price budget yields a scalar objective whose logarithmic derivative has sign opposite to a specified quadratic. The quadratic has a single positive zero below the critical price and is positive for every positive ratio at and above it. The proof includes the equality boundary, \(a=0\), \(b=0\), and the limit of infinite conductance ratio. Exact rational determinant, tree-enumeration and derivative checks have been run from the packaged script; they support rather than replace the all-size proof.

## Originality — PASS, with residual historical risk
Khosoussi et al. [1] formulate weighted spanning-tree design, determinant identities, and edge-selection relaxations, but the inspected main text and appendix do not state this exact all-price continuous cost allocation for a matching-distinguished complete bipartite graph. Prior published results about unweighted crown graphs or different graph spectral objectives do not logically imply the present global determinant-optimal threshold. Semantic published-record searches for the same objective, graph, matching prices, and aliases returned no identical conclusion. Earlier log-determinant design or weighted spanning-tree enumerator literature could still contain an equivalent solution, so priority remains unverified externally. Generic logdet concavity and the eigenvalue-product formula are credited as established tools, not claimed as new.

## Value — PASS
Weighted spanning-tree count is a natural D-optimal network connectivity criterion, and unequal edge prices are a concrete design constraint. The theorem gives a full, unique optimizer for arbitrary individual edge decisions, an exact price at which an entire perfect matching is rationally omitted, a compact algebraic design formula below that price, and explicit asymptotic budget-allocation behavior. Unlike rephrasing a known table, it resolves a continuous global network design problem with a non-obvious structural deletion transition.

## Limits
The claim is restricted to equal-sided complete bipartite graphs and one distinguished perfect matching cost class. No finite validation is treated as an infinite proof. The exact historic priority comparison is not exhaustive. Independent review has not been performed.

Self-review: passed. Independent audit: not yet performed.

## Source
[1] Khosoussi et al., arXiv:1604.01116 (initial public version 2016-04-05).
