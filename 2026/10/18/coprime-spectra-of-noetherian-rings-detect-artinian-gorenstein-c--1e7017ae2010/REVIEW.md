# Review: Coprime spectra of Noetherian rings

## Correctness — PASS

The theorem is proved for every nonzero commutative Noetherian unital ring. The definition gives the annihilator criterion directly. For a coprime ideal \(C\neq0\), support localization at a maximal ideal \(\mathfrak m\) combined with Nakayama forces \(C\subseteq\mathfrak m^n\) whenever its localized power is nonzero; Krull intersection then forces an Artinian localization. Noetherian minimal-prime finiteness makes that isolated maximal point a clopen local direct factor. Join-primality confines \(C\) to the factor; in an Artinian local ring the unique coprime ideal is its socle if and only if the socle dimension is one. Orthogonal socles realize all subsets as closed hulls. These are algebraic implications, not extrapolations from calculations.

A standalone verifier exhaustively tested the original coproduct coprimality definition on all ideals and ideal-pairs of 17 small Artinian local/product rings. All matched the classification, including zero, singleton, and multi-point spectra. Its finite checks do not certify the unrestricted theorem; the general proof supplies that part.

## Originality — PASS, with residual bibliographic risk

Murphy-Hernandez and Leon-Rodriguez introduced the coprime ideal definition, the annihilator formulation, and the dual-ring and domain special cases in *The Coproduct of Ideals and the Coprime Spectrum* (arXiv:2609.23351). These are prior facts, not new results here. The present statement handles all Noetherian rings, including positive-dimensional direct factors and non-Gorenstein Artinian factors, and identifies precisely which factors survive in the spectrum. The dual-ring theorem does not determine those missing cases. Searches for equivalent socle, Gorenstein and Artinian-component formulations found no covering result among inspected materials. This is a best-knowledge originality assessment, not proof that unindexed literature has no equivalent statement. The accessible source was inspected through its main definitions and relevant propositions, but some later passages were not completely re-accessible.

## Value — PASS

The finding gives an exact complete classification of the newly introduced coprime-spectrum invariant for an entire standard class, not an isolated example: it detects Artinian Gorenstein connected factors, gives an exact finite cardinality and proves discreteness for all Noetherian rings, sharply contrasting the known non-Noetherian nondiscrete example. In particular, it clarifies when the new spectrum is empty for broad mixed-dimensional and local families.

## Limits and citations

The conclusion requires Noetherianity and does not classify all non-Noetherian cases. Earlier arithmetic-geometry uses of the term coprime module have distinct definitions. The key nonstandard lemma from the motivating paper is rederived in RESULT.md, and the standard Krull intersection ingredient is identified precisely (Stacks Project, Tag 00IP). Earlier historical claim access was incomplete; current accessible claims were compared for deduplication. Independent auditing is still needed before relying on novelty as a publication claim.

Self-review: passed. Independent audit: not yet performed.
