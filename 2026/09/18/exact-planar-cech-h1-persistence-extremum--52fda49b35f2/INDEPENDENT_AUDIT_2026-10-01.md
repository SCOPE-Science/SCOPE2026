# Independent mathematical audit — SCOPE-20260918-52fda49b35f2

Final disposition: **PASS**.

## Correctness
**PASS.** The proof was reconstructed from the persistent class itself. At any b<t<d a planar alpha representative decomposes into simple cycles, one of which must survive to at least d. Its q<=m edges have perimeter at most 2qt. If its inradius were below sqrt(d^2-t^2), the polygonal interior would already lie in the offset of its vertices at a radius below its death, a contradiction. Convexification and the sharp tangent-polygon perimeter inequality give the opposite bound r<=t cot(pi/q), hence d/t<=csc(pi/q)<=csc(pi/m) and t down to b gives the claim. Perturbation stability removes general position. The regular m-gon has birth sin(pi/m) and death 1, so equality and the inverse threshold follow.

## Originality
**PASS.** The primary 2026 Bobrowski–Skraba abstract describes an asymptotic minimum-point law governed by sphere covering and a persistent isoperimetric mechanism, not an exact finite planar formula. Targeted searches did not locate the csc(pi/m) extremum in Čech persistence. Full text of the most relevant preprint could not be obtained through the available lawful routes, so the originality conclusion is explicitly best-of-knowledge.

### Equivalent formulations
Equivalent alpha/offset formulations were checked; no alternate formulation found that turns the theorem into an existing exact result.

### Broader coverage
The inspected broader results do not imply the exact finite m-point Čech extremum.

### Exact database or table
Absence of a table is only supporting context; novelty rests on comparison with the asymptotic primary statement.

### Claim versus prior implication
The final statement is not a corollary of the inspected asymptotic theorem.

## Value
**PASS.** This exactly solves the finite k=1,d=2 instance of a motivated extremal persistence problem for every m and every target ratio, with a sharp geometric extremizer. The finite formula is a natural classification rather than an arbitrary computation.

## Source inspections
- **A Universal Law of Large Numbers for Extreme Cycles in Random Čech Complexes** (arXiv:2609.19474): primary abstract; full text attempted through arXiv/OA and authorized retrieval, which returned no verified PDF Assessment: ABSTRACT_ONLY; supports asymptotic prior context but cannot justify a whole-document noncoverage claim. Evidence: The abstract states a sharp asymptotic minimum-point law governed by covering density.

## Residual risks
- The most relevant 2026 preprint was not available in full text during this audit; exact finite material hidden outside the abstract therefore remains a residual originality risk.
- The general-position removal uses standard barcode stability; no coefficient-field extension beyond the stated Z2 case was assessed.

The JSON companion records the structured four-part originality comparison and the same limitations.
