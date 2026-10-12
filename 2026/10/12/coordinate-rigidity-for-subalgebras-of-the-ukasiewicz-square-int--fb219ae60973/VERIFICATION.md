---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The bundled `verify_coordinate_rigidity.py` is a standalone Python 3 standard-library script. It verifies the exact dyadic ramp formula on every dyadic point with denominator \(256\), for every \(0\le k\le8\) and \(0\le j<2^k\); it separately tests the definable-zero term on the same grid. It enumerates every endpoint-preserving nondecreasing mapping between the standard full grids of denominators \(1\) through \(9\), then checks preservation of negation, square and join. It also enumerates every pair of subalgebras of standard grids through denominator \(7\), screens all endpoint-preserving nondecreasing maps, and operation-checks survivors against the inclusion criterion. On a chain, preservation of join implies nondecreasingness, so the restricted candidate generation is exhaustive after endpoint preservation.

The replay returned:

```
VERIFY_OK 131994 exact structural assertions; 131327 exact ramp evaluations; 92368 full-chain monotone candidate maps screened; 23 actual full-chain homomorphisms; 324 subalgebra pairs; 10364 subalgebra monotone maps screened; 162 actual subalgebra homomorphisms
```

A final boundary test exhibits a nonidentity homomorphism in the join-and-negation reduct of the five-element grid that fails to preserve square; another test shows that negation and square alone permit endpoint interchange on the Boolean two-element subalgebra, which fails to preserve join.

The program exhausts only the indicated finite ranges. The general theorem, including arbitrary infinite domains, is established by the dyadic squeezing argument in `RESULT.md`; no independent audit has been performed.
