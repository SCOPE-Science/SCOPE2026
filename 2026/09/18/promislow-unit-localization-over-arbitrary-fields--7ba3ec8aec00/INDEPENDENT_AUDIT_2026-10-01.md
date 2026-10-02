# Independent audit — Coefficient transport removes the characteristic-two restriction in Promislow unit localization

Audit date: 2026-10-01 (UTC) UTC

## Final claim assessed

The scientific claim in `RESULT.md` and `SLOGAN.txt` was assessed unchanged.

## Correctness — PASS

In \(\alpha\beta=1\), the identity product fiber has coefficient sum 1 and every other old fiber has sum 0. Tabei's compression preserves each old fiber as a monochromatic class and may only merge whole old fibers. Keeping the original coefficients therefore preserves every new product coefficient: nonidentity fibers sum zeros and the identity fiber is one plus zeros. The support realization is coefficient-independent and injective. Direct finiteness for the sofic Promislow group algebra upgrades the right inverse to a two-sided inverse. Over a finite field, bounded supports and finitely many coefficients make each fixed-support-size search finite; known positive-characteristic units make the minimum computable.

## Originality — PASS

The primary source explicitly isolates but does not solve the coefficient obstruction; coefficient transport through whole-fiber mergers supplies the missing bridge.

### Equivalent formulations
Both the field-independent theorem and weighted-fiber lemma were searched. Evidence: No matching arbitrary-field coefficient-transport result was found.

### Broader coverage
Neither broader framework supplies the same total-support-only radius over arbitrary fields. Evidence: Tabei proves the radius theorem over \(\mathbb F_2\) and explicitly leaves coefficients over other fields untreated; property (U) has a different support-dependent form.

### Exact database or table
The result is structural/algorithmic. Evidence: No table mechanically yields the theorem or all-finite-field computability.

### Claim versus prior implication
The whole-fiber coefficient-sum observation is the missing implication. Evidence: Direct finiteness and existence do not solve the coefficient obstruction in the compression.

### Source inspections
- **Localizing the Gardam unit: the support geometry of units in F2[P] and its non-unique-product relatives** — https://arxiv.org/abs/2609.17559. Trigger: Primary source for the localization theorem and stated characteristic-two limitation. Material read: Relevant full-text Section 7, Theorem 7.2, Remark 7.3, and support-realization discussion. Assessment: The source explicitly leaves the coefficient-bearing extension untreated while its geometry is coefficient-independent. Evidence: Remark 7.3 identifies the coefficient obstruction.

Checked sources: https://arxiv.org/abs/2609.17559; https://arxiv.org/abs/math/0305440; https://arxiv.org/abs/2106.02147; https://arxiv.org/abs/2303.02823; published scientific archive semantic search

Residual risks: An independent coefficient-based extension under other terminology may be unindexed.

## Scientific value — PASS

The theorem removes an explicit characteristic-two restriction without worsening the effective radius and extends finite-field minimum-support computability to every finite field.

## Reproducibility

The coefficient-sum coarsening and its application to the source compression were reconstructed algebraically; no finite experiment is needed.

## Disposition

**PASSED.** The unchanged final claim passes correctness, originality, and scientific value.
