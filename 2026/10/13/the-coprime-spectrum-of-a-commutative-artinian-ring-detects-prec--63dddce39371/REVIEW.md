# Scientific review: coprime spectrum of commutative Artinian rings

## Correctness — PASS
The proof reduces coprimality to a single simple socle ideal in the local case. For any nonsimple nonzero ideal \(C\), the explicit obstruction \(I=L\) (a simple ideal) and \(J=\mathfrak m C\) uses \(\operatorname{ann}(L)=\mathfrak m\), Nakayama's lemma, and \(C\subseteq[L:\mathfrak m C]\). When the socle has more than one simple direction, a second simple ideal obstructs the first. A unique simple socle lies in every nonzero ideal and satisfies the defining implication. Products are reduced coordinatewise, and support across two factors violates the coproduct condition. The topology is checked using separating ideals. The characteristic-two finite examples in `verify.py` support, but do not replace, these arguments.

## Originality — PASS, subject to stated residual risk
The closest identifiable primary source is arXiv:2609.23351v1. Its advertised general coverage defines the operation and topology and identifies the spectrum on dual rings, which cover Artinian Gorenstein rings, but does not establish the criterion for non-dual local rings or mixed Artinian products. The visible square-zero example gives a local non-Gorenstein boundary rather than the full theorem. Searches of the published research records and public mathematical sources found no theorem subsuming the full classification. The 2026 source could not be retrieved completely again in a later request, and historical ideal-lattice aliases remain possible; neither is a novelty certificate.

## Value — PASS
This is an exact classification, not a small numerical gain or an arbitrary slice. It calculates all points and the topology of a newly defined spectrum for an entire foundational class of commutative rings, and it shows precisely which ordinary prime-spectrum points disappear in mixed or non-Gorenstein cases. The Artinian Gorenstein locus provides a structural interpretation that is not obtainable merely from the dual-ring special case.

## Scientific limits
The theorem does not address general Noetherian rings. The finite verifier is exhaustive only for the nine named small rings. The source-comparison uncertainty concerns potential earlier equivalent formulations, not a missing step of the present proof.

Self-review: passed. Independent audit: not yet performed.
