# Scientific review

## Correctness: PASS

The target is an indexed binary ring of length \(n\ge1\), and an enlargement is defined by repeating that target exactly \(m\) times. Inverse local determinism of each left-permutative rule produces four pair-state maps \(T_{G,0}\) and \(T_{G,1}\). A cyclic predecessor for the repeated target is equivalent to a fixed point of the \(m\)-th power of the composed map. The minimum permitted enlargement therefore equals its shortest cycle length. This establishes the universal fourfold bound without relying on experimental extrapolation. Direct closure of all sixteen finite transformation monoids, followed by exhaustive closure of the appropriate augmented word automata, proves the exceptional-word characterizations for arbitrarily long outputs. The independent forward-image check compares 5,120 target/replication pairs with the inverse criterion for cyclic lengths at most twelve. All scripted assertions pass with `VERIFY_OK`.

## Originality: PASS (historical-priority qualification)

Wolfram (1983) supplies the classical 256-rule taxonomy. Martin–Odlyzko–Wolfram (1984) studies linear-rule algebra, which substantially covers the linear constituents, but the inspected abstract does not state a simultaneous sixteen-rule classification. Mariot–Leporati–Dennunzio–Formenti (2017) gives a more general method for computing a particular periodic target's minimum predecessor period. The present finite inverse-pair mechanism is not novel. The specific new object checked is the simultaneous all-output classification for all sixteen rules with exact regular exceptional languages, including the uniform nonlinear triple-lift exceptions. The accessible 2017 full postprint was inspected for the main method and examples; none of the inspected material supplies this classification. Searches of research records and the primary literature found no stronger statement that directly implies the complete list. Risks remain from unindexed work and incomplete full-text access to the 1984 classical paper. A computational method's generality is distinguished from publication of this exact all-rule table.

## Value: PASS

One-step surjectivity on the bi-infinite lattice guarantees each periodic target can have a periodic preimage, but does not determine the smallest necessary ring enlargement. For finite-ring initial conditions that enlargement is an intrinsic reachability obstruction; this theorem sharply distinguishes the exceptional threefold nonlinear patterns from the fourfold parity obstruction of the linear rules, and proves that no larger factor is required in the entire natural sixteen-rule class. Every extremal value is witnessed by a short word. This simultaneous structural classification is more informative than a routine single-instance execution of the known period-computation algorithm.

## Sources and scientific limitations

- Stephen Wolfram, *Statistical mechanics of cellular automata*, Rev. Mod. Phys. 55 (1983), DOI: https://doi.org/10.1103/RevModPhys.55.601.
- O. Martin, A. M. Odlyzko and S. Wolfram, *Algebraic Properties of Cellular Automata*, Commun. Math. Phys. 93 (1984), DOI: https://doi.org/10.1007/BF01223745; bibliographic/abstract comparison only, full text not inspected.
- L. Mariot, A. Leporati, A. Dennunzio and E. Formenti, *Computing the Periods of Preimages in Surjective Cellular Automata*, Natural Computing 16 (2017), DOI: https://doi.org/10.1007/s11047-016-9586-x; author-hosted postprint: https://lucamariot.org/files/papers/mldf_naco_2017_postprint.pdf. Material inspected: abstract, introduction, inverse de Bruijn method, examples, linear case and concluding portions.

The result is not an assertion of novelty for the generic de Bruijn construction or the individual linear rules. It does not characterize the number of predecessors or multistep dynamics. No independent scientific validation has been performed.

Self-review: passed. Independent audit: not yet performed.
