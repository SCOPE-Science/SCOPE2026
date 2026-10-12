# Scientific review

## Correctness — PASS
The reduction to a \(272\)-vertex, \(11{,}206\)-edge compatibility graph is immediate from the explicit self-overlap and pair-compatibility constraints; no admissible code is excluded. Maximal-clique enumeration terminates with \(4{,}887{,}344\) maximal cliques and finds \(4{,}996\) of largest size \(13\), so the upper bound and completeness follow. Separate C++ and standard-library Python implementations, run from the actual included source code, agree on the full \(844{,}324\)-byte catalogue; all optimum codes satisfy their defining conditions. The completeness of the branching algorithm follows by induction, and the symmetry calculation checks every catalogue member. This certifies a finite result, not an all-length statement.

## Originality — PASS with residual bibliographic risk
The 2016 paper on weakly mutually uncorrelated codes introduces balanced error-correcting synchronization codes, but its constructions/bounds do not state or imply the full finite optimum and census at these parameters. The 2018 mutually uncorrelated code treatment addresses the balancing and error-detection conditions but does not give a complete length-twelve optimizer classification. The 2025 polarity-balanced non-overlap paper computes optima without the Hamming-distance constraint, a strictly broader feasible class whose reported sizes do not settle the combined problem. Searches for parameter aliases, the compatibility-graph reduction, code-size tables, and published mathematical results found no dominating claim. Negative search outcomes are not proof of worldwide novelty; unindexed finite catalogues remain possible.

## Value — PASS
This closes a natural finite simultaneous-constraint design instance: strict framing, exact binary composition, and one aligned substitution correction. The maximum size \(13\) is not supplied by the known balanced non-overlap maximum or the unconstrained coding bound; the complete \(4{,}996\)-code catalogue and symmetry reduction give all optimal designs, not just one example. The result supplies a reproducible benchmark for constructions satisfying multiple channel constraints without implying biochemical applicability or error-robust framing.

## Independent status
Self-review: passed. Independent audit: not yet performed.
