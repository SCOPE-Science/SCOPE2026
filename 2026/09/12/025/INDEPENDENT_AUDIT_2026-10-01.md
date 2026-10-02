# Independent audit — 2026-10-01

## Final claim

Hexagon-switch depth-two branching ball around the Netto STS(19): 57 classes (32 for second anti-Pasch cyclic type)

## Correctness — PASS

PASS. The certified roster was rechecked independently from the actual JSON data, rather than trusting the saved success log. For the Netto/5-sparse starter the recomputed invariant keys are (0,171,0) and (2,108,16), with 55 pairwise-new depth-two keys, giving 57 certified nonisomorphic classes. For the second anti-Pasch cyclic type the keys are (0,57,114) and (4,46,94), with 30 pairwise-new depth-two keys, giving 32. Every retained block system was revalidated as an STS(19), every recorded parent-to-child switch was replayed, and every Pasch/hexagon-record/mitre invariant was recomputed. Distinct invariant triples rigorously imply nonisomorphism, so the stated lower bounds follow.

## Originality — PASS

PASS. Erskine and Griggs compute the global connected-component structure of the length-six switching graph on STS(19), which is broader contextual coverage, but their published theorem does not determine the radius-two ball around the Netto system or the second anti-Pasch cyclic type. A component order alone does not imply a local radius-two count. Searches found no published exact 57/32 local-ball statement. The claim is therefore not a corollary of the inspected global component-size theorem.

## Scientific value — PASS

PASS. The Netto system is the unique 5-sparse STS(19) and a standard highly structured extremal design, while cycle switching is the natural local move studied in the primary literature. A certified local branching lower bound around this distinguished system is a motivated finite structural datum. The claim is deliberately only a lower bound and does not pretend to be a full distance census.

## Sources inspected

- Grahame Erskine and Terry S. Griggs, Cycle Switching in Steiner Triple Systems of Order 19 — https://arxiv.org/abs/2405.07750: BROADER_NOT_COVERING_LOCAL_BALL. The paper proves global disconnectedness and component orders for fixed cycle lengths, but does not state the radius-two ball sizes at the audited starters.

## Residual risks

- The 57 and 32 values are certified lower bounds, not exact full radius-two ball sizes.
- The historical verifier scripts contain environment-specific paths; the publication plan adds a portable verifier that reads the repository-local roster certificate.
- Absolute novelty remains best-knowledge because the full global switching computation may have generated unpublished local traversal data.

## Disposition

**repaired**
