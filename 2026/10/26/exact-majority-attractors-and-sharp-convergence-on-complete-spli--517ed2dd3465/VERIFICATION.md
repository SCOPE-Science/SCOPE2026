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

The self-contained `verification/verify_split.py` implements the synchronous majority update from the actual graph-neighbour masks. For each of 79 size pairs with \(1\le a,b\le10\) and \(a+b\le14\), it exhaustively checks all labelled initial configurations (253,956 total), counts fixed points and states satisfying \(F^2(x)=x\), confirms \(F^5(x)=F^3(x)\), and identifies the exact maximum entry depth. The recorded output is in `verification/verify_output.txt`.

A second, count-based update function checks every feasible pair of occupancy counts for each of 900 parameter pairs with \(1\le a,b\le30\). All assertions passed. These finite checks do not establish the infinite-parameter theorem; its proof is the coordinatewise case classification in `RESULT.md`. No proof-assistant or third-party audit is claimed.
