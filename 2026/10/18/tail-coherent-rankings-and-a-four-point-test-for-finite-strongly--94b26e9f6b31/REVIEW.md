# Review of the finite strong-density classification

## Correctness — PASS

The theorem is proved by deriving contraction consistency from strong density and centering; this forces each world-indexed choice function to be the minimum operator for a unique strict total order, since a directed pairwise-choice triangle contradicts contraction consistency. Strong density then implies suffix coherence by testing two-element subsets of a tail. Conversely the four-point condition makes any two relevant suffix restrictions coincide and therefore yields the original strong-density equation. Both directions use the assumptions and quantifiers stated in `RESULT.md`. The polynomial-size test refers to an already-established ranking representation, not to arbitrary tables without normalization.

Two independent exhaustive programs support the small-frame data. `verify.py` tests each order profile through five worlds and checks the literal strong-density equation independently of the local test through four worlds. `verify_direct.c` examines all \(331776\) centered, total, functional four-world choice tables without a ranking assumption, finding \(138\) strongly dense tables. Finite code alone is not a proof for all worlds; the all-size statement is supplied by the structural proof.

## Originality — PASS with explicit uncertainty

The original strong-density notion, successful centered selection frames, and Boolean preconditional representation are in Holliday's 2024 *Preconditionals*, and are not claimed to be new. Relevant original source sections, a later version and similarly themed published records were compared. No equivalent four-point ranking and suffix-coherence classification, nor the exact small-frame labelled/unlabelled census, was identified. The closest found enumerations study preconditionals on *chains* rather than on finite Boolean powerset algebras, and do not imply these statements. Searches used choice-theoretic, Stalnaker, conditional-logic and numerical aliases, not solely matching titles.

An alternative earlier formulation could be present in unindexed rationalizable-choice literature or inaccessible Boylan–Mandelkern ESSLLI notes. This uncertainty is retained; non-retrieval is not a proof of publication uniqueness.

## Mathematical value — PASS

The object arises directly from finite conditional logic semantics. The normal form reduces exponentially indexed subset choices to finite ranking profiles and turns strong-density checking into an \(O(n^4)\) local forbidden-pattern condition once ranking representation is certified. The exact first nontrivial finite-frame and orbit census is an intrinsic, motivated classification, not an arbitrary finite slice. It produces finite examples of the total-functional centered subclass of Boolean preconditional semantics and identifies the first size at which strong density removes models.

## Boundaries

No closed-form count for arbitrary \(n\) is established, no unproved extension to partial/multivalued selection frames is asserted, and no claim of independent verification is made. Code and numerical output support the finite counts only; the general result relies on the proof. The associated Boolean-algebra claim relies on the source representation and does not claim to represent all preconditionals using total functional selections.

Self-review: passed. Independent audit: not yet performed.
