# Independent audit — Pro-star reversibility collapses on semiperfect rings

Audit date: 2026-10-01 (UTC) UTC

## Final claim assessed

The scientific claim in `RESULT.md` and `SLOGAN.txt` was assessed unchanged.

## Correctness — PASS

Applying the definition to \(u u^{-1}=1\) makes \((u^*)^{-1}u\) an invertible projection, hence 1, so every unit is self-adjoint. This makes the unit group abelian. The defining condition also forces idempotents self-adjoint; together with reversibility they are central. In a local ring, \(x\) or \(1-x\) is a unit, so the involution is the identity and the ring is commutative. A semiperfect ring then decomposes into central star-stable local factors. The domain criterion and the \(\mathbb F_4\) Frobenius example check directly.

## Originality — PASS

The primary source does not contain the unit obstruction or semiperfect collapse; later stronger records corroborate but do not predate the result.

### Equivalent formulations
The equivalent unit-fixation formulation was checked with chronology. Evidence: A 2026-09-19 archive record gives a stronger equivalent unit-group criterion but postdates this 2026-09-18 result.

### Broader coverage
Standard structure theory is an ingredient, not prior coverage of the new property. Evidence: The source proves reversibility/projection consequences but does not discuss units, local rings, semiperfect rings, or finite rings.

### Exact database or table
This is a structural classification. Evidence: No database or table mechanically supplies the theorem or the \(\mathbb F_4\) separation.

### Claim versus prior implication
No inspected prior statement mechanically implies the final theorem. Evidence: The source implications do not force units self-adjoint; that new step drives the classification.

### Source inspections
- **On star-Reversible and Generalized star-Reversible Rings** — https://arxiv.org/abs/2609.20076v1. Trigger: Primary paper introducing the property. Material read: Relevant full-text definition and section on pro-star-reversibility, with targeted checks for units/local/semiperfect/finite rings. Assessment: The primary paper does not state the unit-rigidity or semiperfect classification. Evidence: Its results stop at reversibility and projection consequences.

Checked sources: https://arxiv.org/abs/2609.20076v1; https://doi.org/10.1007/978-1-4419-8616-0_8; https://doi.org/10.1155/2013/650702; published scientific archive follow-up records dated 2026-09-19

Residual risks: The short unit argument could have an older equivalent formulation under different terminology.

## Scientific value — PASS

The result completely classifies the new property on semiperfect rings, covering finite, Artinian and finite-dimensional algebras, while the domain criterion and minimal \(\mathbb F_4\) example identify genuine boundaries.

## Reproducibility

The proof was reconstructed directly from the definition and standard semiperfect structure; no finite experiment is needed.

## Disposition

**PASSED.** The unchanged final claim passes correctness, originality, and scientific value.
