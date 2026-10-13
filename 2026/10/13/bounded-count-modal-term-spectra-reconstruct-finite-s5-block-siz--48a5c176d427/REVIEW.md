# Scientific review

## Correctness — PASS
The exact domain and syntax are finite nonempty equivalence frames with Boolean term operations and fixed graded modalities \(D_1,\ldots,D_K\). A pointed input type is exactly its local propositional color and the vector of per-color multiplicities capped at \(K\). Explicit depth-one formulas isolate types. Uncapped histograms exist only at block sizes actually present; a capped histogram can be inflated in a largest block, giving the coefficient formula. For \(K\ge2\), the uncapped coefficient at size \(s\) is a polynomial of exact degree \(s-1\) in the alphabet size, while the capped contribution has degree at most \(M-K\). This separation proves recovery of the entire set of sizes after recovering their maximum. For \(K=1\), only the maximum remains in the expression. Full proof and reproducible finite cross-checks are provided. Computational enumeration is corroboration, not an infinite proof.

## Originality — PASS, with residual literature risk
General graded bisimulation and expressive completeness are established background, including Otto (arXiv:1910.00039) and Chen–van Ditmarsch–Greco–Tzimoulis (arXiv:2105.09202). The existing clipped-histogram result for a single universal S5 component is acknowledged; it does not settle how the entire arity-wise operation-count profile separates arbitrary sets of several component sizes. The new implication is the sharp \(K=1\) versus \(K\ge2\) recovery theorem, not the underlying counting modality or single-component type lemma. Searches for modal clones, truncated histograms, class-size spectra, and graded equivalence models disclosed no exact dominating theorem, but a historical equivalent in the broader literature cannot be ruled out.

## Mathematical value — PASS
The question is natural: which parts of a finite epistemic partition can be recovered from the algebra's intrinsic term-operation statistics? The theorem completely classifies the information content of these profiles under bounded counting and exposes a sharp expressiveness discontinuity at threshold two. It does not rely on arbitrary finite slices or parameter choices, and it separates recoverable distinct sizes from unrecoverable multiplicities. The concise exact formula supports direct computation of the invariants.

## Limitations and closest work
The theorem does not reconstruct multiplicities, does not concern isomorphism of the underlying powerset algebras, and uses the entire arity profile rather than one arity. It is restricted to finite S5 equivalence frames. The closest antecedents are the general graded-bisimulation theorems listed above and the known universal-cluster histogram census; possible earlier clone-classification literature remains the main originality risk.

Self-review: passed. Independent audit: not yet performed.
