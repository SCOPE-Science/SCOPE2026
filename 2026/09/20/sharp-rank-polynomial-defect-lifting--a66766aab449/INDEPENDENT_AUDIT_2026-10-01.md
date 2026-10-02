# Independent mathematical audit — Sharp quantitative structure of polynomially finite-rank operators

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS** — The defect range is invariant because the polynomial defect commutes with the operator. Cayley–Hamilton on the restriction to this finite-dimensional range produces an annihilating polynomial of degree at most the polynomial degree plus defect rank. Complementing the range gives an upper-triangular block operator whose quotient block is already annihilated by the polynomial; replacing only the defect-range block by a scalar root gives a correction supported inside the defect range with no rank inflation. The noncommutative telescoping formula factors the polynomial difference through the perturbation in at most the polynomial degree many terms, yielding the lower rank-distance bound. The nilpotent, scalar and cyclic-shift examples give the stated sharpness.

## Originality

**PASS** — Barnes 1985 is a close qualitative antecedent: Corollary 11 gives some finite-rank perturbation that makes the polynomial vanish. The inspected source does not state localization of the perturbation inside the defect range, the no-rank-inflation bound, the minimal-polynomial degree bound, or the two-sided rank-distance estimate. No earlier exact quantitative theorem was located.

### Equivalent formulations

Searches/sources: Barnes 1985 Corollary 11, Algebraic elements of a Banach algebra modulo an ideal; Kramar 2012 finite-rank perturbation of algebraic operators; Resultary semantic query: polynomially finite-rank operator rank p(T) correction algebraic rank distance.

Evidence: Barnes proves existence of an unspecified finite-rank correction. Kramar's abstract concerns the reverse direction: finite-rank perturbations of algebraic operators remain algebraic. The exact quantitative Resultary search returned only the audited record.

The prior qualitative lifting is not equivalent to the localized and sharp quantitative structure theorem.

### Broader coverage

Searches/sources: Barnes 1985 full PDF; Giotopoulos–Roumeliotis 1991 algebraic ideals; operator-ideal perturbation literature surfaced by search.

Evidence: Barnes treats algebraic lifting modulo ideals in a broader Banach-algebra setting but without the rank controls. The 1991 source invokes Barnes for qualitative lifting modulo the socle.

No inspected broader theorem supplies the audited quantitative constants and localization.

### Exact database or table

Searches/sources: Resultary exact/semantic search for rank-polynomial defect lifting and rank distance.

Evidence: The audited record was the only exact quantitative hit.

There is no standard table; theorem-record search is the relevant exact comparison.

### Claim versus prior implication

Searches/sources: Does Barnes Corollary 11 imply rank at most rank p(T) or range localization?; Does finite-rank perturbation stability imply the lower rank-distance bound?.

Evidence: Barnes's conclusion supplies existence but no stated control connecting the correction rank or range to the original defect range. The lower bound requires the separate noncommutative telescoping rank estimate, while the degree bound uses the defect-range restriction.

The quantitative conclusions are not mechanically implied by the inspected prior theorem.

### Source inspections

- **Algebraic elements of a Banach algebra modulo an ideal** — QUALITATIVE_PRECURSOR.
  Identifier: https://doi.org/10.2140/pjm.1985.117.219
  Trigger: closest exact antecedent for polynomial finite-rank lifting
  Material read: complete Pacific Journal PDF, especially Corollary 11
  Method: lawful open-access full text
  Evidence: Corollary 11 gives a finite-rank correction but does not state the audited range localization or quantitative rank/degree bounds.
- **Some properties of algebraic operators on locally convex spaces** — REVERSE_DIRECTION_ACCESS_RISK.
  Identifier: https://acta.bibl.u-szeged.hu/16425/
  Trigger: plausible perturbative overlap
  Material read: abstract and bibliographic page; the accessible page says finite-rank perturbations of algebraic operators are algebraic
  Method: lawful public material
  Evidence: Complete theorem-level text was not inspected, so an equivalent quantitative formulation remains a residual risk.

Residual originality risks:
- Kramar's complete text and some older Olsen finite-rank perturbation papers were not inspected in full.
- Poorly indexed operator-ideal literature may contain an equivalent quantitative statement.

## Scientific value

**PASS** — The theorem converts one natural defect rank into a sharp degree bound, a correction supported exactly where the defect lives, and optimal universal rank-distance bounds. These are reusable quantitative structural facts, not a mere restatement of qualitative algebraicity.

## Final assessment

The final claim survives unchanged on correctness, originality and scientific value. No change to RESULT.md or SLOGAN.txt is proposed.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
