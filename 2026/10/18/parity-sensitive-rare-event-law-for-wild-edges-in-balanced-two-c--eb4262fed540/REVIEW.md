# Scientific review

## Correctness — PASS

The two-colour wild-number formula reduces the problem to monochromatic component counts. Exact fixed-size isolation probabilities are elementary binomial ratios, while a uniform cut union bound shows that configurations requiring two or more wild edges have probability \(O(n^2 4^{-n})\). The logarithmic expansion uses three explicit power sums; its \(n^{-1}\) terms cancel and the edge-balance parity yields the \(n^{-2}\) coefficient. Verification independently enumerated 359,423 balanced edge assignments for orders four through seven and checked multiple large-order asymptotic instances. No finite enumeration is used in lieu of proof.

## Originality — PASS, with residual risk

Dawkins et al. (arXiv:2610.22142, Section 3.2.1) establish the qualitative convergence of the expected wild number to zero, not a rare-event asymptotic, and Anders et al. (arXiv:2508.06711, Theorem 6.4(2)) give the underlying component identity. The second-order expansion explicitly distinguishes the parity of the complete graph's edge count. Searches for an equivalent wild-number formula, fixed-half-edge connectivity expansion, parity-corrected isolated-vertex distribution and existing mathematical research records did not identify this complete statement. Prior dense random-graph enumeration may imply the expansion after a further calculation; bibliographic priority is not independently guaranteed.

## Value — PASS

The October 2026 work makes the random-equitable wild number a natural question but leaves its failure probability and expected repair burden quantitatively unresolved. The result supplies an explicit exponentially small failure probability, identifies the unique-isolate mechanism with high relative accuracy, and detects a systematic parity effect invisible in the qualitative limit. The second-order coefficient requires a nontrivial cancellation of the first finite-size term, so the claim is more than a restatement of convergence to zero.

## Closest literature and limitations

The two named preprints are directly relevant and were compared at the statement level. The exact two-colour component identity and the qualitative convergence remain prior work. The large-graph expansion does not characterize higher-colour wild numbers or non-equitable colourings, and a general connected-labelled-graph asymptotic could overlap bibliographically.

Self-review: passed. Independent audit: not yet performed.
