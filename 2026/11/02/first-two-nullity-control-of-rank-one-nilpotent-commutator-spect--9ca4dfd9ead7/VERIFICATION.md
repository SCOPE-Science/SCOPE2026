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

Write X=uv^T, v^Tu=0, modulo q-1 rescalings. Stratify nonzero u by J²u nonzero, Ju nonzero but J²u zero, and Ju zero; each gives respectively 3,2,1 independent linear covector constraints. Subtract the zero covector in the zero-moment fiber to derive A,B,E. Rank([J,X])<2 iff u belongs to ker J or v to ker J^T; their intersection is governed by the pairing ker J^T x ker J of rank c=2b-d (singleton Jordan blocks), yielding Z and U by projective line counting, with V as the remainder. On span(u,Ju), C has matrix [[-t,-s],[0,t]], and C²=-sX at t=0: this forces every stated odd/even characteristic Jordan type. Independently enumerated actual matrix products, all moments and ranks for six small nilpotent partitions and fields, not as a substitute for proof. All nonnegative multiplicities and full partition of rank-one square-zero X follow.

## originality

PASS

Earlier work on nilpotent centralizer Jordan types describes matrices commuting with J, not the actual nonzero commutator distribution [J,X] with prescribed rank-one X and both traces. The special rank-one fixed-matrix count and centralizer component are not claimed as novel. Published rank-one commutator loci (Guralnick/Neubauer) are plausibly relevant but their complete texts were unavailable; no demonstrated implication of the complete moment-fiber counts was identified.

## value

PASS

The closed moment-refined similarity census for every finite field and every nilpotent J collapses complicated Jordan partitions to just their first two nullities, a structural universality phenomenon. The characteristic-two distinction and rank-two nilpotent fibers are genuinely new mathematical information beyond counting commuting rank-one matrices alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
