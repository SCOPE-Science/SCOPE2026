# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The argument is a finite-state construction specialized to the explicit q-decimal semantics of Qiao et al.

The hidden-vector universe is finite because every scalar arithmetic result lies on the q-decimal grid in the bounded precision interval or is one of the finitely many special values. Qiao et al. prove that their recursively reduced finite-precision RoPE has a finite period \(C\). Thus, for a fixed current query, a previous position's contribution to an attention head is determined by its hidden-vector type and its position modulo \(C\).

The only nontrivial issue is whether finitely capped multiplicities preserve the exact softmax result. They do under the cited semantics. A positive rounded exponential is at least \(10^{-q}\); \(10^{2q}+1\) copies already force the rounded denominator above the allowed magnitude and hence to `Inf`, making every head weight zero by the rule \(c/\mathrm{Inf}=0\). If no positive type reaches that threshold, all positive multiplicities are stored exactly, so the denominator and weighted value sums are exactly reconstructible. Joint overflow from several unsaturated types is also detected because those counts are exact.

Causality keeps all previous-position hidden vectors fixed when a token is appended. The current position can therefore be propagated block by block from the capped histograms, and the histograms can be updated deterministically. The final-position hidden vector determines the output logits. With fixed argmax tie-breaking, the prefix summary is a finite deterministic state.

The bounded-halting and ultimate-periodicity conclusions then follow from the pigeonhole principle for deterministic finite-state orbits. The finite-range and regular-total-decider corollaries are standard consequences.

The proof does not rely on empirical evidence. No computation artifact is needed for the general claim.

## Originality

**PASS, qualified to the best of our knowledge.**

The motivating paper, Qiao et al. arXiv:2609.20335, proves finite-precision incompleteness only through the class of "non-converging" Turing machines and a repeated-block collision argument. The inspected full text does not state a finite sufficient state for all prefixes, a uniform bound on every halting autoregressive generation, or ultimate periodicity of every non-halting generation.

The closest identified prior work is Jerad, Svete, Li and Cotterell, arXiv:2608.11909. For a related fully uniform finite-precision soft-attention model with component-periodic RoPE they prove the exact single-pass recognition class \(\mathrm{LTL}[P,\mathrm{MOD}]\). That result already places periodic-RoPE recognition inside the regular languages, so **regularity of single-pass periodic-RoPE recognition is not claimed as novel here**. Their model also treats the realization of conventional RoPE differently from Qiao et al.'s recursively rounded phase rule.

The novelty claim is restricted to the explicit capped phase-by-hidden-state summary for Qiao et al.'s q-decimal arithmetic and its iterative-autoregressive consequences: a model-dependent uniform bound on every halting generation and ultimate periodicity of every non-halting continuation. Targeted searches for these formulations, including synonymous finite-state, bounded-generation, finite-range, periodic-generation, and chain-of-thought terms, did not locate a prior statement.

Merrill and Sabharwal's chain-of-thought expressivity results concern a different arithmetic/model regime and do not supply this finite q-decimal collapse.

Residual originality risk is non-negligible. Qiao et al.'s preprint is extremely recent, and a near-simultaneous observation or later revision may not yet be indexed. The inspected full text was arXiv:2609.20335v1 dated 17 September 2026. More abstract automata-theoretic literature may also contain a general finite-state transducer lemma that subsumes the final dynamical step; no novelty is claimed for that elementary finite-state lemma itself.

## Value

**PASS.**

The result materially sharpens the interpretation of the motivating finite-precision theorem. In the exact q-decimal model, chain-of-thought is not merely insufficient for a selected infinite-output family of Turing machines: if it halts, its length is bounded by a constant depending only on the fixed transformer, and if it does not halt, its generated continuation must eventually cycle.

This gives a direct structural boundary for the model and separates two sources of transformer expressivity that can otherwise be conflated: iterative token generation does not create unbounded computational state when the prefix itself admits the stated finite sufficient summary. The explicit state bound also makes the obstruction quantitative, albeit very loose.

## Limitations

The theorem does not cover infinite precision, precision growing with input length, external memory/tools, nonperiodic realized positional mechanisms, or stochastic decoding. The displayed state bound is not claimed to be tight. The result is tied to Qiao et al.'s particular overflow convention; replacing that arithmetic may invalidate the capped-count proof.

No independent validation is asserted.
