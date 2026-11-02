# Scientific review

## Correctness — PASS

Exact Cholesky of a symmetric positive-definite \(M\)-matrix corresponds to neighbor-clique completion without cancellation. A first elimination fills all absent pairs in other multipartite parts. Fill is quiescent during the first-part run; the first outsider fills all still-absent pairs in the original part and completes the remaining graph. The falling-factorial initial-run probabilities, linearity-of-expectation pair argument, extrema, and geometric limit follow without asymptotic gaps. The fixed-size rational verifier's 2,231 grouped checks agree, but do not substitute for the proof.

## Originality — PASS, qualified

The classical graph-elimination rule in [1] and [2] is assumed as prior, and the deterministic best ordering is not presented as a discovery. The new claim is the all-part-size fill probability-generating law and the balanced near-maximal-fill limit. The inspected technical text of [1] studies sparse randomized *incomplete* clique replacements and reordered matrix experiments, not the uniform **exact** fill law. The inspected [2] studies min-degree rather than the random permutation distribution. Direct searches for complete multipartite/bipartite random fill, geometric initial-run, exact expected sparse-Cholesky fill, and equivalences did not locate the proposed formula. Bibliographic access to [3] alone is insufficient to rule out an earlier version; publication priority remains qualified.

## Mathematical value — PASS

Complete multipartite supports are natural dense-cross-part sparse-matrix stress tests. The joint law resolves every fill-count probability, not just an average, and quantifies a strong practical asymmetry: balanced bipartite random order has asymptotically one-half probability of achieving maximal fill whereas the minimum is exponentially unlikely. The result supplies precise baselines for fill-reducing elimination orders, with explicit restrictions on the numerical algorithm.

## Limitations and closest literature

[1] Chen, Liang and Biros (2020), arXiv:2011.07769; [2] Fahrbach et al. (2017), arXiv:1711.08446; [3] Kloks (1993), minimum fill-in for chordal bipartite graphs (full material unavailable). No independent publication-priority certification and no claims for arbitrary graphs or incomplete factorization.

Self-review: passed. Independent audit: not yet performed.
