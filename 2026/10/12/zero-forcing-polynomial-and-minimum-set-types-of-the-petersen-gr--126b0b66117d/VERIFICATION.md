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

The claim is finite and exhaustively checkable. `verify_petersen_zero_forcing.py` reconstructs the standard Petersen graph as \(P(5,2)\), verifies ten vertices, cubic degree, and fifteen edges, and computes standard zero forcing closure for every one of the \(1024\) subsets. It checks the exact coefficient vector and the absence of any forcing set of size below \(5\).

For every one of the \(252\) five-vertex subsets, the script performs direct graph-isomorphism testing against six explicit five-vertex patterns and verifies both the full type census and the statement that precisely the \(C_5\), \(P_5\), and \(P_4\mathbin{\dot\cup}K_1\) types are zero forcing.

Run `python3 verify_petersen_zero_forcing.py`. Expected output:

`VERIFY_OK subsets=1024 zf_total=498 coefficients=5:132,6:190,7:120,8:45,9:10,10:1 min_types=C5:12,P5:60,P4+K1:60 nonforcing5=120`

The checker proves only this ten-vertex finite theorem. It does not certify any claim for other generalized Petersen graphs and it does not establish bibliographic novelty.
