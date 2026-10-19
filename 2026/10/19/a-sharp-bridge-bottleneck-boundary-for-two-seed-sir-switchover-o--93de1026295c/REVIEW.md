# Scientific review

## Correctness

**PASS.** The full SIR(1) model, seed sampling, graph definition, parameter ranges, and endpoint cases are explicit. In a percolated graph, a component of size \(k\) is hit by two uniformly sampled distinct vertices with probability \(1-(N-k)(N-k-1)/(N(N-1))\). This gives the cubic component contribution. The bridge-closed versus bridge-open split exhausts all possibilities, so first-through-third binomial moments yield the exact difference. The sign analysis gives three mutually exclusive cases, and its large-\(n\) limit is a direct leading-coefficient calculation. A separate graph enumeration checked the full symbolic identity for six sizes and \(907{,}792\) graph/seed-pair combinations. The theorem relies on the general proof, not on extrapolating the finite check.

## Originality

**PASS with residual risk.** Ódor et al. [1] establish and motivate epidemic-seeding switchover for heterogeneous geometric/random networks. The 2022 overview [2] treats broader qualitative seeding effects. Keliger et al. [3] prove general sufficient conditions, with a strong-switchover conclusion under graph-expansion and seed-size assumptions that the pendant-leaf, fixed-two-seed family here does not satisfy. The exact double-star polynomial, sole six-vertex reversal, and macroscopic dominance gap are neither stated by nor consequences of those inspected claims. Searches for double-star, bistar, two-hub, tree-percolation, and fixed-two-seed aliases found no covering result, but previously unindexed influence-spread computations on trees remain a genuine priority risk. Search absence alone is not evidence of uniqueness.

## Value

**PASS.** The two-hub bridge network is a minimal deterministic model of two highly connected local communities linked by one bottleneck. The exact classification answers a natural question posed by the prior seeding-switchover literature: how a sparse intercommunity cut and only two initial cases affect whether dispersed seeding can eventually overtake hub seeding. The result does not merely approximate a known inequality: it shows that reversal occurs for exactly one branching size, locates its exact probability, excludes reversal uniformly for every larger size, and quantifies a nonvanishing population-scale discrepancy. These are testable structural benchmarks for epidemiological seeding comparisons, not an assertion of relevance to every real network.

## Literature and limitations

References [1]–[3] are listed with accessible links in `RESULT.md`. The SIR/independent-bond equivalence and concept of switchover are prior knowledge. Conclusions apply to the specific double-star SIR(1) family with exactly two seeds and equal edge transmissibilities; they do not transfer automatically to multi-step infectious periods or stochastic contact networks. The closed-form formula is an analytical proof, whereas the standalone exhaustive checker samples only finitely many graph sizes. Independent scientific audit remains outstanding.

Self-review: passed. Independent audit: not yet performed.
