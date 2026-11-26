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

The alternant quotient is e₂ at the five distinct complex nodes. Reduction in the basis 1,ω,…,ω^(N/2−1) pairs the ten products with their negatives, preserving multiplicity. If an antipodal node pair u,−u is present, its cross terms cancel and the four residual terms force another antipodal pair v,−v with v²=−u². In the other case opposite edge products come from disjoint edges. Each of the five vertices is omitted by one of the five edge matchings, so reducing each product relation modulo two forces equal parity of all five exponents. Dividing the shifted exponents by two descends to N/2 with five distinct nodes; a quartet at that order lifts to a quartet, and orders at most four are impossible. A quartet annuls both e₁ and e₂, proving sufficiency. The {0,1,2,4} minor on u,−u,iu and the outsider v is a nonzero Vandermonde times iu+v, so the singular rank is exactly four. Disjoint cosets give the claimed count without double counting. I inspected verify_dyadic_5minor.py and verification_output.txt: the reported exhaustive integer tests at 8,16,32 and four determinant evaluations corroborate the argument; I did not execute the frozen script and the proof is not predicated on these tests.

## originality

PASS

The distinct supported content is the exact converse to the quartet obstruction, together with the complete rank and multiplicity classification for this aperture. The rank-one block construction in the older full-spark proof already gives quartet sufficiency, not just a bare existential obstruction; the determinant and cancellation inputs are classical. No inspected source yields the necessity or exact-rank diagram.

## value

PASS

This is the natural next near-consecutive aperture after the missing-degree e₁ case, where simple full spark already fails. Knowing exactly which five-column selections lose rank, and that none loses more than one, determines the relevant erasure incidence rather than merely confirming a predicted failure. The necessity argument on product pairings across all dyadic dimensions is not a finite recalculation or a generic full-spark test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
