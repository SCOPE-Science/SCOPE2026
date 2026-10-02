# Independent mathematical audit — SCOPE-20260930-93ae1c88a87e
Audit date: 2026-10-01 (UTC) UTC.
Disposition: **passed**.

## Final claim
For every finite nonempty family of computable structures in disjoint renamed relational languages, the tagged disjoint union has relative categoricity spectrum equal to the intersection of the component spectra; when the component spectra have least degrees, the least degree of the union is their finite Turing join, and rigidity is preserved.

## Correctness
Status: **PASS**.

Both spectrum inclusions follow directly from the quantifiers. Tags make every component of an oracle-computable copy uniformly oracle-computable; component isomorphisms can therefore be combined. Conversely, replacing one component by an arbitrary oracle-computable copy and keeping the others computable forces any tagged-union isomorphism to restrict to the required component isomorphism. Upward closure then turns finite intersection of principal cones into the cone above the finite Turing join, and tag-preserving automorphisms are componentwise. An independent 65,536-case finite structural analogue reproduced product isomorphism counts and rigidity, but that finite check is only supporting evidence for the symbolic proof.

## Originality
Status: **PASS**.

Kalimullin defines and studies relative categoricity spectra and least relative categoricity degrees, but the inspected full text does not state a tagged-disjoint-union intersection theorem or finite-join closure. Semantic search of published findings returned the audited record and no earlier equivalent or stronger theorem. The construction is compatible with standard many-sorted/tagged-sum ideas, so an unlocated folklore formulation remains a residual priority risk, but no inspected source implies the stated spectrum identity.

### Equivalent formulations
- Search/source: I. Sh. Kalimullin, Notes on degrees of relative computable categoricity, arXiv:2207.08316v3
- Search/source: Published-record semantic query: relative computable categoricity spectra tagged disjoint union intersection finite Turing joins rigid witnesses
- Evidence: The inspected source defines relative categoricity spectra but contains no tagged-disjoint-union or finite-join spectrum theorem.
- Reasoning: No equivalent formulation was located; the theorem is reconstructed directly from the definitions.

### Broader coverage
- Search/source: arXiv:2207.08316v3
- Search/source: Published-record semantic corpus
- Evidence: The source supplies the framework and general realization results, not a theorem whose consequence is this exact finite tagged-sum identity.
- Reasoning: The inspected broader results do not mechanically imply the audited composition law.

### Exact database or table
- Search/source: Published-record semantic corpus
- Evidence: No exact theorem/database entry matching the spectrum-intersection law was located.
- Reasoning: This is not a finite invariant ordinarily tabulated; the relevant exact-source check is the published theorem corpus.

### Claim versus prior implication
- Search/source: arXiv:2207.08316v3
- Evidence: Definitions of relative categoricity and its spectra are prior; the two-direction tagged-sum argument is additional.
- Reasoning: The prior definitions do not by themselves state the theorem, and no stronger theorem was located that mechanically yields it.

### Source inspections
- **Notes on degrees of relative computable categoricity** (arXiv:2207.08316v3): trigger — primary source for the spectrum definition and surrounding theory; material read — full accessible text around the definitions, spectrum notation, least-degree framework, and relevant results; method — lawful arXiv full-text inspection; assessment — FRAMEWORK_NOT_COVERING; evidence — The paper defines the spectrum and least relative categoricity degree; searches within the full text did not locate disjoint-union or finite-join closure statements.

## Value
Status: **PASS**.

This is a natural compositional law for an established spectrum invariant: it gives exact finite intersection at the spectrum level, finite Turing-join closure for least degrees, and preservation of rigid witnesses. The tags and finite-uniformity hypotheses identify the exact mechanism and boundary, so the result is a motivated structural lemma rather than an arbitrary reformulation.

## Checked sources
- I. Sh. Kalimullin, Notes on degrees of relative computable categoricity, arXiv:2207.08316v3.
- Published-record semantic query: relative computable categoricity spectra tagged disjoint union intersection finite Turing joins rigid witnesses.

## Residual risks
- An equivalent tagged-sum closure observation may exist as folklore under many-sorted or disjoint-union terminology; no such source was located.
- Only finite tagged unions are proved; countable families require additional uniformity.

The audit distinguishes finite reproducibility checks from proofs of infinite statements and makes no claim beyond the final claim above.
