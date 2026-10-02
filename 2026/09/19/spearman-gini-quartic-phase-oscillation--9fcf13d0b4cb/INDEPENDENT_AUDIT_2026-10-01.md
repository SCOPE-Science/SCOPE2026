# Independent audit — Third-order universality and quartic phase oscillation at the Spearman-Gini boundary

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS** — Starting from the exact two-branch boundary parametrization, independent series reversion gives \(1-\rho=\frac32 y^2-\frac{5+3\sqrt3}{2}y^3+K(u)y^4+o(y^4)\), where \(y=1-\gamma\) and \(K(u)=39/2+45\sqrt3/4+16u^3-24u^4\). The cubic coefficient cancels identically on both branches. Since \(u\in[0,1/2]\), \(K\) has cluster interval \([K_0,K_0+1/2]\), so the fourth normalized remainder has no unique limit. Direct substitution into the exact formulas at large integer parameter agrees with the symbolic coefficients.

## Originality

**PASS** — Best-of-knowledge originality survives. The primary exact-region paper states only the quadratic endpoint law with an \(O((1-g)^3)\) remainder in the inspected main text. The universal cubic coefficient, explicit quartic phase law, cluster interval, and failure of fourth-order endpoint Taylor regularity were not located in the published archive or searched literature.

### Equivalent formulations

The current theorem refines an explicitly coarser source expansion.

Evidence: The semantic search returned the audited record as the direct higher-order hit. The primary paper's Remark 2.2 states \(\rho(g)=1-\frac32(1-g)^2+O((1-g)^3)\) near comonotonicity, without the cubic constant or quartic phase law.

### Broader coverage

The exact parametrization does not mechanically expose the phase law without a nontrivial uniform branch expansion and series reversion.

Evidence: The inspected primary paper gives the piecewise algebraic parametrization and its accumulating breakpoints; these are the necessary input for the calculation. No broader inspected theorem states the endpoint cubic/quartic regularity classification.

### Exact database or table

Search failure alone is not novelty proof; the positive assessment rests on the inspected source stopping one asymptotic order earlier and on the explicit new branch calculation.

Evidence: No earlier exact constant or cluster-law record was located.

### Claim versus prior implication

The final claim requires additional asymptotic analysis beyond the prior theorem.

Evidence: The two branch expansions have the same cubic coefficient but distinct phase-dependent quartic coefficients, which is stronger than the source's \(O(y^3)\) statement. The phase law varies with the fractional position between accumulating algebraic junctions and therefore is not implied by a single Taylor coefficient.

### Source inspections

- **The exact region determined by Spearman’s rho and Gini’s gamma** — PRIMARY_INPUT_NOT_COVERING_IN_INSPECTED_TEXT.
  Identifier: arXiv:2609.19890v1
  Material read: pages 1–12 of 16, including Theorem 1.1, equations (15)–(23), and the complete endpoint Remark 2.2 statement.
  Evidence: The inspected main text supplies the exact algebraic pieces and only the quadratic endpoint asymptotic with an \(O((1-g)^3)\) remainder; it does not state the cubic or quartic refinement.

### Residual risks

- The last four pages of the 16-page primary paper were not inspected after a later access/safety block; no whole-document noncoverage claim is made. An equivalent higher-order consequence could also be implicit in older rho–footrule calculations.

## Scientific value

**PASS** — The result identifies the first order at which the infinitely many exact-region pieces become asymptotically visible and gives the complete cluster interval. This is a natural regularity invariant of the newly solved exact boundary, not an arbitrary coefficient extraction.

## Final assessment

The claim survives unchanged on correctness, originality, and scientific value.

This assessment is mathematical review evidence, not formal proof-assistant verification or a guarantee against undiscovered prior art.
