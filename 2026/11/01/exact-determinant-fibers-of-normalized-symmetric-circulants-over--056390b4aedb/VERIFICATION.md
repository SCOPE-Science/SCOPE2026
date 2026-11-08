---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

A symmetric circulant is an inversion-fixed polynomial in R=F_q[X]/(X^n-1), normalized by f(1)=1. In odd field characteristic ℓ, reduction to S=F_q[X]/(X^m-1), n=ℓ^s m, is surjective on involution invariants by averaging and has q^((n-m)/2) uniform normalized lifts. Reconstructed the decomposition of nonfixed roots under Frobenius and negation into factors F_(q^e), with fixed root 1 and an extra -1 factor iff m even. The determinant is (product of norms)^(2ℓ^s) for m odd, and v^(ℓ^s)(product of norms)^(2ℓ^s) for m even; nilpotents do not affect the determinant. Surjective finite-field norms give the exact even uniform fibers, odd square-only fibers, and pure-ℓ-power determinant-one exception, including n1. Independently enumerated symmetric first rows and evaluated determinants by finite-field Gaussian elimination at q3 n2..6 and q5 n3,4; all individual fibers matched formulas. Finite checks were corroboration of the general finite-field algebra proof.

## originality

PASS

Unrestricted finite-field circulant determinant counts are known (Appel), but involution-fixed row-sum-one matrices have a genuinely different distribution (square support at odd nonexceptional order, uniform even order, determinant-one pure characteristic powers). No inspected exact source subsumes all three cases. These are derived with standard field-norm algebra; an equivalent older self-reciprocal group-algebra formula remains a material priority risk.

## value

PASS

Complete determinant-fiber distribution for every symmetric circulant row-sum-normalized matrix over odd finite fields is a natural algebraic invariant. The even/odd/special-characteristic trichotomy explains exact arithmetic obstructions and supplies zero, square and every nonzero determinant counts, going beyond mere invertibility tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
