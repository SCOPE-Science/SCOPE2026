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

# Verification

The proof was checked from the dual mutual-visibility definition and the explicit geodesics of \(G_n=K_1\vee(K_{n,n}-M_n)\). The critical steps are the forced split of every matched nonedge and the exact shore-count conditions.

The standalone verifier `verify_crown_cones.py` exhausts every hub-containing subset for \(2\le n\le8\), directly checks dual visibility, and verifies the chromatic witnesses. It produced:

`ALL CHECKS PASSED; n_range=2..8; hub_containing_subsets=87376; counts={2: 2, 3: 0, 4: 8, 5: 10, 6: 32, 7: 84, 8: 198}`

This finite computation is not used as the proof for arbitrary \(n\). The \(n=3\) wheel obstruction is prior literature; the all-parameter criterion and count are the reviewed new claim.
