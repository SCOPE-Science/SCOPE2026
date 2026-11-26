---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For monic characteristic polynomials p, q of degrees n, n−1, the shared algebraic multiplicity is deg gcd(p,q). The map (A,B) ↦ Ap+Bq on pairs of polynomials of degrees < n−1, < n has kernel dimension deg gcd(p,q), by dividing by the gcd and using coprimality. Consequently the lower bound on shared multiplicity is closed, and scalar multiplication of matrices preserves it. Diagonal conjugation preserves both spectra. With exponents 2^(j−1) the nonzero ordered weight differences are distinct (the sign and the 2-adic valuation recover the order and smaller index; the remaining odd factor recovers the larger index). The fixed locus in projective matrix space is the projective diagonal space and the n(n−1) off-diagonal matrix-unit points. The diagonal cutoff discards one spectral entry; an off-diagonal unit and its cutoff are nilpotent, with characteristic polynomials T^n and T^(n−1). Thus all fixed components lie in the deepest level, including for n=2. Euler localization on these invariant loci yields n+n(n−1)=n² in every closed level and zero in all lower exact levels, with compact supports on the latter. The argument is symbolic; the finite checks described in VERIFICATION.md were not rerun.

## originality

PASS

No equivalent or stronger covering theorem for this paired-cutoff Euler filtration was found in the inspected sources. The same-day one-matrix subdiscriminant record shares localization and the ambient endpoint, not the spectral condition or its Euler values. This is a bounded originality assessment, not a priority claim.

## value

PASS

The closed and exact coincidence levels are natural strata of an established matrix problem, with changing component structure. The simultaneous determination of their projective Euler invariants shows that every lower exact layer contributes zero in additive topological calculations, despite the filtration being geometrically nontrivial. The proof is short but requires identifying the full fixed locus in the deepest level, and the inspected component theorems do not tabulate or directly imply these invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
