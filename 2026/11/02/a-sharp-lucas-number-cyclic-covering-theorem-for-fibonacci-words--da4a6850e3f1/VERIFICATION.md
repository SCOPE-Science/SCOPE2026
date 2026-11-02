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

# Verification and scope

`python3 verify.py` (standard library) returned `VERIFY_OK`. It independently constructs Euler tours and checks exact window coverage, no forbidden cyclic `00`, balanced degrees, the source-to-sink pairing, and length identities for every integer \(2\le n\le12\). It also exhaustively rejects all shorter circular binary strings at \(2\le n\le5\).

`python3 flow_check.py` (NetworkX 3.6.1) returned `FLOW_VERIFY_OK`. Network simplex finds optimal extra traversal costs \(0,1,2,4,7,12,20,33,54,88,143\) for \(n=2,\ldots,12\) on the **unrestricted** binary de Bruijn graph; forbidden additional windows are permitted in that independent relaxation.

The full infinite proof uses degree imbalance, integral path decomposition, the forced initial-symbol shift distance, an exact source–sink bijection, connectivity, and a Fibonacci sum. Finite checks do not certify historical novelty, optimal-word uniqueness, or other forbidden languages. No external validation was performed.
