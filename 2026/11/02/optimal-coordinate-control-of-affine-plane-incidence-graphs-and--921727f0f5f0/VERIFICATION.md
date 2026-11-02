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

Run `python3 verify.py` in the directory containing this file and the standalone `verify.py`. No third-party package, network access or external data file is needed.

The executed script prints `VERIFY_OK 3514`. It checks the exact point–line incidence Gram identity for prime-field affine planes of orders 2, 3, 5 and 7 and the explicit minimum placement for each. It exhaustively compares all 120 three-input placements at order 2 against the PBH rank condition using rational Gaussian elimination; 56 pass both the direct and geometric tests. Fixed concurrent line sets yield exactly 4 and 48 optimal omitted-point sets at orders 2 and 3, respectively. It additionally compares 128 seeded order-three placements against full modular Kalman ranks and checks the order-five optimal construction by modular Kalman rank.

Modular computations certify full rational rank whenever they return full rank, but the cross-order proof is analytic and does not depend on these finite-field tests. The script does not enumerate all finite affine planes or analyze non-Desarguesian planes computationally. All such planes are covered by the mathematical proof because it uses only the affine incidence axioms.

The sharpness, determinant characterization, and exact pencil count are proved in `RESULT.md`. No independent third-party mathematical verification has occurred.
