# Independent audit — 2026-10-01

## Finding

**Disposition: passed.** The final claim was reassessed on correctness, originality, and scientific value.

## Correctness — PASS

Fresh independent arithmetic reproduced all 28 pairs 4<=n<=10 and 3<=d<=n-1 from the displayed Li-Miao formulas: the v2 ratio has minimum 1.0402228914827727 at (4,3), maximum 1.1338599190158805 at (10,7), and the v1 ceiling is larger on every tested pair. Exact rational evaluation at (4,3) gives Psi(4)=-261/10, Psi(41/10)=7389/1000, and phi(7)=1971/4=492.75>486, so the published Corollary-2.5 ceiling cannot itself imply the proposed product bound there.

## Originality — PASS

Primary-source inspection confirms that Li-Miao supply the formulas and leave Question 4.20 open; no inspected source or published-record search states the 28-pair ceiling diagnostic or exact anchor certificate.

### Equivalent formulations

The claim is a quantitative diagnostic for the displayed published ceiling, not a reformulation of the open geometric conjecture.

### Broader coverage

The general theorems provide the input machinery, but do not state that these particular published v1/v2 ceilings miss the stratified target on all 28 tested pairs.

### Exact database or table

The exact finite table is not a known-source table reproduced under a new name.

### Claim versus prior implication

The diagnostic is a logically valid limitation of that displayed route and is not implied merely by knowing the formulas without doing the comparison.

### Sources inspected

- On the volume of K-semistable Fano manifolds — https://arxiv.org/abs/2506.17420: INPUT_NOT_COVERING. The paper supplies the ceiling framework and leaves the stratified product bound as an open question; it does not give the 28-pair failure table.
- The sharp volume gap for Kähler manifolds with positive Ricci curvature — https://arxiv.org/abs/2608.08193: NOT_COVERING. Its sharp global gap is not the stratified product-volume comparison diagnosed here.

## Scientific value — PASS

This is a motivated method-limit result tied directly to an explicit open question: it identifies that a published quantitative route, without sharper input, misses the target throughout the first 28 admissible parameter pairs. The exact (4,3) certificate makes the limitation rigorous independently of the floating-point census.

## Limitations and residual risks

The exact (4,3) certificate is symbolic; the remaining 27 table rows were independently recomputed numerically rather than interval-certified. The claim diagnoses only the displayed v1/v2 Corollary-2.5 ceilings and does not settle Question 4.20 or exclude sharper uses of those valuations.
