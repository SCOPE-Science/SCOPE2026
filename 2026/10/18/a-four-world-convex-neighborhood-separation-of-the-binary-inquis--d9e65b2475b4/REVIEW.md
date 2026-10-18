# Scientific review

## Correctness — PASS

The statement concerns the exact inhabited neighborhood semantics of Ciardelli, with nonempty neighborhoods and unbounded unary nesting. Both four-world neighborhood families are convex: the only strict inclusion in the larger family is a covering pair. The proof's type-support induction uses actual state profiles, not a bounded-depth approximation; implication respects those profiles because every subset of a realized profile is realized by a substate. Since universal and existential neighborhood quantification in both models reduce to the same maximal and minimal type profiles, every unary-fragment formula has the same support at all information states. The binary conditional has opposite values by direct evaluation. The standalone checker confirms the finite premises and all 19 downward-closed profile predicates, without purporting to replace the induction.

## Originality — PASS, subject to literature risk

The closest primary source, Ciardelli's *Inquisitive Neighborhood Logic* (arXiv:2411.04031, Section 4, Open Problem 4.6), poses the precise convex-frame definability question. Its unrestricted-model expressivity separation does not logically imply nondefinability on convex models. The earlier existential-only/upward-monotone counterexample answers a different half of that problem. Searches for equivalent convex-frame separations did not identify an answer. Related works on convex team semantics (arXiv:2503.21850) and classical bundled modalities (arXiv:2603.26268) use different operators and class restrictions; their statements do not imply this counterexample. Unknown equivalent work remains a priority risk; a search failure is not uniqueness proof.

## Value — PASS

The result settles a specifically published expressivity question, not an arbitrary small invariant. It exhibits why preserving extremal observable neighborhood profiles does not preserve the binary conditional, even when each raw neighborhood family is itself convex. The countermodel and structural induction provide a reusable obstruction method for comparing inquisitive modal fragments.

## Closest literature and limits

Primary comparison: Ciardelli, *Inquisitive Neighborhood Logic*, Proposition 4.3, Corollary 4.4, Proposition 4.5 and Open Problem 4.6; Anttila–Brinck Knudstorp, *Convex Team Logics*, Sections 1–3; Ding–Yang, *A General Theory of Propositional Modal Bundled Modalities*, Section 4.1. The theorem makes no minimality claim about four worlds and does not decide the separate convex-invariance completeness conjecture. It has not undergone an independent audit.

Self-review: passed. Independent audit: not yet performed.
