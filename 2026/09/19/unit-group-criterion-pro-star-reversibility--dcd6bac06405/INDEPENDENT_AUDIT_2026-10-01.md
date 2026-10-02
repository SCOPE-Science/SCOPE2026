# Independent mathematical audit — 2026-10-01

**Record:** SCOPE-20260919-dcd6bac06405 — Unit groups exactly detect pro-star-reversibility
**Disposition:** PASSED

## Final claim assessed

For every unital ring with involution, pro-\(*\)-reversibility is equivalent to \(*\)-reversibility together with pointwise fixation of every unit; under these conditions \(ab=p\in P(R)\) forces \(b^*a=p\), with the stated clean, semiperfect, radical, local, and division-ring consequences.

## Correctness — PASS

Necessity is immediate from \(u u^{-1}=1\): the resulting projection \((u^*)^{-1}u\) is a unit and hence equals \(1\). For sufficiency, \(*\)-reversibility implies reversibility, so the projection \(p=ab\) is central and \(ba=p\). The lifted corner elements \(pa+(1-p)\) and \(pb+(1-p)\) are inverse units and therefore self-adjoint. This gives the \(p\)-corner of \(b^*a\) equal to \(p\); applying \(*\)-reversibility to \(((1-p)a)b=0\) kills the complementary corner. Thus \(b^*a=p\). The unit-group, radical, clean/semiperfect, and division consequences then follow by direct standard arguments.

## Originality — PASS

An earlier 2026-09-18 published SCOPE record proves the necessary unit rigidity and local/semiperfect/domain consequences, but not the global converse for an arbitrary \(*\)-reversible ring. Resultary returns the audited exact criterion as the first full equivalence and a later same-day record explicitly marked as an alternate proof. The Chen--Wang--Zou accessible primary abstract introduces the notion and basic characterizations but does not expose the unit criterion. The source full HTML was unavailable, so an unadvertised equivalent statement there remains a residual risk rather than evidence of coverage.

## Scientific value — PASS

The theorem gives an exact structural boundary between two recently distinguished ring-theoretic notions and immediately organizes several natural classes (clean, semiperfect, local, division) and the Jacobson radical. The general converse is not a mere renaming of the earlier semiperfect/domain special cases.

## Originality comparison details

### Equivalent formulations

Equivalent formulations through projection products and pointwise self-adjoint units were compared, not merely titles.

Searches:
- Resultary semantic search: pro-star-reversible rings unit group fixed by involution exact criterion star-reversible
- web/arXiv search for arXiv:2609.20076 with unit/invertible terminology

Evidence:
- Resultary returned the audited criterion, the later duplicate, and the prior semiperfect-rigidity result; no earlier full arbitrary-ring equivalence appeared.

### Broader coverage

The prior SCOPE theorem covers major consequences and one direction but does not dominate the global iff theorem.

Searches:
- 2026/09/18/pro-star-reversible-semiperfect-rigidity--8cd8850c47f1 full RESULT.md
- Chen--Wang--Zou arXiv:2609.20076

Evidence:
- The 2026-09-18 record gives unit rigidity, semiperfect/local collapse, and a domain criterion, but does not prove that every \(*\)-reversible ring with all units fixed is pro-\(*\)-reversible.
- The accessible primary abstract describes introduction and study of pro-\(*\)-reversibility but no unit-group equivalence.

### Exact database or table

No finite database/table determines this structural theorem; the index check was used to locate exact and stronger published SCOPE statements.

Searches:
- Resultary query listed above

Evidence:
- Top matches were the audited criterion, the later alternate-proof record, and the earlier semiperfect-rigidity record.

### Claim versus prior implication

The audited corner argument supplies a genuinely missing implication at the level of the general class.

Searches:
- direct comparison with the 2026-09-18 semiperfect/domain theorem

Evidence:
- Unit rigidity alone is only the necessary direction. Local/semiperfect and domain converses do not imply the converse on arbitrary \(*\)-reversible rings.

## Source inspections

### Pro-star reversibility collapses on semiperfect rings

- Identifier: 2026/09/18/pro-star-reversible-semiperfect-rigidity--8cd8850c47f1
- Trigger: Closest earlier SCOPE theorem
- Material read: Full RESULT.md
- Method: Read-only repository inspection at the frozen commit
- Assessment: PARTIAL_COVERAGE
- Evidence: Contains necessity and several class-specific converses, not the arbitrary-ring converse.

### On *-Reversible and Generalized *-Reversible Rings

- Identifier: arXiv:2609.20076
- Trigger: Originating primary source for the notion
- Material read: Primary abstract and accessible metadata; full HTML fetch failed
- Method: Open arXiv/web inspection
- Assessment: UNRESOLVED_FULLTEXT_RISK but no accessible covering statement
- Evidence: Abstract says the notions and basic properties/characterizations are studied; it does not state the unit criterion.

## Limitations and residual risks

- The full current Chen--Wang--Zou text could not be inspected through the available open route; originality is best-of-knowledge with this source risk recorded.
