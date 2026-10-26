# Review of the macroscopic inversion law

## Correctness — PASS

The direct/skew-sum recursion of the ordered binary-tree group gives exactly one independent fair swap for each internal vertex. An inversion pair is assigned to its unique lowest common ancestor. Consequently the inversion count is a sum of independent Bernoulli contributions weighted by the square of the relevant half-block size; this proves the finite generating law. Geometric series give the stated moments and a deterministic coupling tail of \(2^{-n-1}\). The support argument uses the explicitly checked tail-dominance property of the decreasing weights. The Fourier argument selects a level for every frequency \(|t|\ge4\), giving a bound of \(e^{-c\sqrt{|t|}}\) and hence all derivatives of the density. Small-size direct exhaustive checks and exact rational identities agree with the analytic derivation. Risks: the probability-space coupling is not an explicit coupling of matrix instances at different dimensions, and the result does not apply to nonuniform-angle models.

## Originality — PASS, qualified by priority risk

The relevant butterfly articles establish the ordered 2-Sylow subgroup and its uniform law, and analyze longest increasing subsequences, cycles, and pivot structure; the full relevant sections were inspected and no inversion-limit or density theorem appeared. Cai and collaborators' inversion problem labels tree vertices independently and counts ancestor inversions: their independent summands are uniform on integer intervals rather than Bernoulli contributions from subtree swaps. The accessible Mendes–Remmel abstract treats standard wreath and Weyl-group statistics rather than the iterated binary-tree action at issue. The exact group uniformity is prior work, not a new conclusion. The recorded external literature searches and comparisons revealed no direct or stronger coverage of this specific smooth macroscopic inversion law; search absence alone does not prove novelty. Risk: an unlocated general Fourier-smoothing or iterated-wreath result might specialize to this case; independent historical review remains necessary.

## Mathematical value — PASS

The inversion number is a canonical global statistic of permutations and directly measures the amount of discordant row reordering in a Gaussian-elimination pivot permutation. The nondegenerate \(N^2\)-scale limit contrasts qualitatively with the deterministic inversion fraction of a uniform symmetric-group permutation. The full support and smoothness conclusions describe a substantive limiting law rather than just a small finite example or a routine moment computation. The exact convergent law and explicit Fourier rate provide a reproducible starting point for quantitative work on random butterfly permutation geometry.

Self-review: passed. Independent audit: not yet performed.
