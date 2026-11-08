---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Eliminating x^q=y-x² yields quartic X^4−2yX²+X+y²−y^q so all fibers have <=4 distinct roots. For each nonzero h=x-z the equal-image pair relation x+z=−h^(q−1) determines exactly one ordered pair, giving sum r(r-1)N_r=q²−1. Distinct triple preimages biject with ordered distinct norm-one αβγ=1 in cyclic U of order m=q+1, count m²−3m+2g. A triple fails to extend to fourth point precisely for an opposite α,β; there are 3(m−2g) such triples. Thus N3=(m−2g)/2, N4=(m²−6m+8g)/24; pair, mass and target identities yield all remaining N_r. The argument uses 2 invertible, valid for odd q including characteristic3. Independent exhaustive quadratic-coordinate evaluation verified every target multiplicity for 10 odd primes. Unrestricted proof is algebraic, not extrapolated from tests.

## originality

PASS

General finite-field polynomial value-set bounds of Mullen–Wan–Wang and polynomial permutation constructions of Qin–Hong are different: an upper bound or bijectivity criterion does not give the five multiplicity classes of this non-permutation map. Exact map and affine-coordinate aliases were searched with no dominating indexed formula established. Claimed originality is qualified by incomplete specialist priority survey.

## value

PASS

The full fiber distribution is a natural invariant of a simple Frobenius-perturbed polynomial across the entire odd-prime-power family; it separates cubic residue behavior in N1-N4 while image size is uniform, a structural arithmetic distinction not mechanically implied by a value-set bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
