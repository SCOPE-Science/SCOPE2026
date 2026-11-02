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

# Exact-arithmetic verification

Run `python3 verify.py` with a Python 3 standard-library interpreter. No external scientific packages, databases, or precomputed files are needed.

The program independently counts the holomorphic-character set defined by the Kummer exponents and its complete doubling-cycle subset, and also counts the binary-itinerary rational points using exact integer inequalities. Tested parameters are \(1\leq h\leq8\), with \(M\) reaching \(65,537\). The resulting two-ranks are \(4,8,16,32,64,128,256,512\).

A separate check counts points on the genus-five member over \(\mathbf F_{2^r}\) for \(1\leq r\leq5\) by explicit binary-field multiplication, obtaining \((3,9,9,37,33)\). Newton's identities give zeta numerator coefficients through genus \((1,0,2,0,7,0)\), consistent with two-rank four. The expected terminal message is `VERIFY_OK`.

These are bounded consistency checks. The all-parameter result follows from the valuation, Cartier and inverse-branch contraction proofs, not from finite enumeration. No independent audit has been performed.
