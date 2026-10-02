# Independent scientific audit — SCOPE-20260918-f0490e7ec2cc

Audited at: 2026-10-01T08:23:38.851470Z

Disposition: **passed**

## Correctness — PASS

The exact degree-4 and degree-5 formulas for the squared largest zero give positive real upper-boundary values on the extra intervals beyond the first degree-loss point. At the next pole they behave as \(3/(\lambda+3)\) and \(5/(\lambda+4)\), so the continued positive square-root branch acquires negative imaginary boundary values immediately to the left; this excludes d>3 and d>4 by the Pick characterization. For d at or below those endpoints, the source right-half-plane theorem, the extra explicit boundary intervals, sublinear singular growth, and the boundary minimum principle give the upper-half-plane Pick property.

## Originality — PASS

Full-text inspection of version 1 shows that Appendix A.3 proves only the sufficient largest-zero range d<=ceil(n/2) for n>=4 and explicitly says its upper endpoint is not claimed optimal; exact largest-zero classifications are given there only for degrees two and three. The audited d<=3 and d<=4 thresholds therefore are not contained in the inspected version.

### Equivalent formulations

No equivalent formulation was found in the inspected primary version; the inaccessible later revision is recorded as a concrete residual risk rather than treated as novelty proof.

### Broader coverage

The source's broader analytic continuation framework supplies tools, but its largest-zero theorem does not imply the degree-4 and degree-5 optimal endpoints.

### Exact database or table

The decisive evidence is the inspected source theorem scope, not the absence of a table.

### Claim versus prior implication

The sharp endpoints require the explicit low-degree branch formulas and next-pole analysis; they are not corollaries of the published sufficient bound.

## Value — PASS

The first two largest-zero degrees not exactly classified by the source are a natural finite boundary problem. Determining both sharp endpoints, identifying the next pole as the obstruction, and extending the low-degree pattern through n=5 are meaningful exact structural results.

## Sources inspected

- Complete Bernstein functions and scaled ultraspherical zeros — https://arxiv.org/abs/2609.19186v1. NOT_COVERING: The source explicitly labels the largest-zero range in Proposition A.4 as sufficient only and gives exact largest-zero classifications only for n=2,3.
- Later revision of Complete Bernstein functions and scaled ultraspherical zeros — https://arxiv.org/abs/2609.19186. INACCESSIBLE_PLAUSIBLE_SOURCE: Because the later full text was not verified, it remains a specific originality risk but does not by itself defeat the version-1 comparison.

## Checked sources

- https://arxiv.org/abs/2609.19186v1
- https://arxiv.org/abs/2609.19186
- https://doi.org/10.1515/9783110269338

## Residual risks

- A later revision of the same very recent preprint may contain the degree-4/5 thresholds; that full text was not verified in this audit.
- No claim is made for n>=6.

## Limitations

- The exact classification is only for the largest zero in degrees four and five.
- Failure above the stated d endpoints concerns the complete-Bernstein/Pick property, not necessarily the weaker Bernstein property.
- The all-degree optimal largest-zero threshold remains open.
- A later revision of the motivating preprint remains an explicit originality risk because its updated full text was not verified.
