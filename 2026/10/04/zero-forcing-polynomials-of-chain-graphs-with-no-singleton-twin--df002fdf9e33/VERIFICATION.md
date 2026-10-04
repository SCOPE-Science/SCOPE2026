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
# Checks performed
The proof was reconstructed directly from the canonical twin-class representation. Necessity was checked from the false-twin invariant, and sufficiency was checked by the explicit forward pass through the \(B_i\) classes followed by the reverse pass through the \(A_i\) classes. The polynomial factorization was then recomputed class by class from the two allowed occupancy states.

The standalone script `artifacts/verify_chain_zf_poly.py` was executed from the package staging path. It builds every canonical weighted chain graph with \(p\le3\), all twin-class sizes in \(\{2,3,4\}\), and total order at most twelve. It exhaustively simulates zero forcing for every subset and compares both the set characterization and the entire coefficient vector with the theorem. The observed output was `VERIFY_OK graphs=60 subsets=128016 max_order=12 boundary=P4`. The script also confirms on \(P_4\) that dropping the non-singleton hypothesis invalidates the simple complement condition.

# Limits
The finite enumeration is corroborative and does not prove the infinite theorem. The proof supplies the general argument. Literature comparison was targeted across the principal chain/difference/Ferrers and zero-forcing aliases rather than logically exhaustive. One older foundational difference-graph source was not available in full text, so that access limitation remains recorded as an originality risk. No independent external audit has been performed.
