---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For k of characteristic other than two, reducing modulo the arrow ideal first kills the two constant diagonal terms. In the remaining path coordinates the diagonal equations are a²+zbc=d²+zbc=0 modulo z⁴ and the off-diagonal equations are b(a+d)=c(a+d)=0 modulo z³. Comparing coefficients verifies the stated equations, with a₃,d₃ free. For a₁≠0 one must have d₁=−a₁, d₂=−a₂ and exactly one of b₀,c₀ nonzero. At a₁=0, the cases a₂+d₂≠0 and a₂+d₂=0 give precisely the remaining branches in the stated union. The b₀≠0 chart of C₁ is G_m×A⁶; after the three eliminations C₁ is given by two equations in A⁹ and its complement has dimension at most six, so the height bound excludes hidden components there. Swapping b,c gives C₂; C₃,C₄ are distinct affine 7-spaces and meet the open where a₂+d₂≠0, which C₁,C₂ do not. These arguments hold over an algebraic closure. The three base-field strata give respectively 2(L−1)²L⁵, L⁵(L−1)(2L−1), and L⁵(4L−3); in the last stratum splitting the zero-product pairs by b's truncated valuation gives the indicated affine/torus pieces. The sum is L⁶(4L−3), giving 2,941,225 at q=7. In characteristic seven the displayed inversion-odd uniformizer generates k[C₇]; its off-diagonal corners relative to (1±s)/2 are opposite arrows and the alternating paths give the full basis. This verifies the algebra identification without assuming scheme-theoretic reducedness. An independent enumeration checked 729 constrained assignments out of 59,049 over F₃, with zero union discrepancies, hence 6,561 points including the two free coefficients. This is a finite consistency check only; the frozen script was inspected, not executed.

## originality

PASS

The supported distinct finding is the explicit four-component geometry and reduced motivic calculation for the internal square-zero locus. The same count and dihedral realization are present in related catalogue work and are not credited as independent novelty. No inspected work establishes the same geometric decomposition. Historical access limitations remain; this is not a priority certification.

## value

PASS

The square-zero locus is an intrinsic multiplication invariant of a natural truncated cyclic algebra and a modular group algebra. Giving the individual geometric components, their dimensions and an exact Grothendieck class extracts structural information not available from the finite count or from commutation alone. The proof handles all fields in scope without appealing to an exhaustive small-field census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
