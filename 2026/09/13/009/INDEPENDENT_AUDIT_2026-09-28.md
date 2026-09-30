# Independent audit — SCOPE-20260913-009

Date: 2026-09-28 (UTC)  

## Disposition: REPAIRED

### Correctness
The Heegaard and tangent-complex core survives. The separating twist about c=[a1,b1] becomes trivial after the handlebody meridians are killed, giving π1(M)=F2 and Betti numbers (1,2,2,1). At the trivial SL2 local system, T Loc_G(M)≃C*(M;sl2)[1], hence tangent cohomology dimensions (3,6,6,3), virtual dimension 0, and shifted duality.

The filed “Tor Euler weight”, “Tor amplitude length”, and “loop-rotation secondary Euler” are not computed by these tangent dimensions. Tangent cohomology and local Tor groups are different derived invariants. The Behrend-sign sentence was also unsupported in the filed argument. Those claims are removed. The repository artifact paths are corrected from `output/artifacts/...` to the actual `artifacts/...` paths, and the verifier is narrowed to the claims it really checks.

### Originality
The mapping-stack, boundary-Lagrangian, and tangent formulas are direct applications of established shifted-symplectic local-system theory. The explicit genus-two example is a useful worked check but has limited standalone originality.

### Scientific value
Moderate as a transparent test case for derived Heegaard gluing and tangent duality once the unsupported local-invariant terminology is removed.

### Sources
- PTVV, arXiv:1111.3209.
- Calaque, *Lagrangian structures on mapping stacks and semi-classical TFTs*, arXiv:1306.3235.
