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

Run `python3 verify.py` from this directory. Only the Python standard library is needed.

The checker exhaustively compares all order-preserving and bounded maps on the six-point crown with the lazy-walk characterization. It then checks all bounded-morphism top-label tuples, counts Heyting-image cardinalities by actual inverse images of upper sets, and compares each multiplicity with the transfer-matrix expression for \(m=3,4,5,6,7\). For \(m=3,4\), it tests preservation of Heyting implication directly for every upper-set pair.

Expected final output: `VERIFY_OK`. Verified census rows are \(m=3\): \(\{2:3,5:18,18:6\}\); \(m=4\): \(\{2:4,5:56,13:16,47:8\}\); \(m=5\): \(\{2:5,5:150,13:100,123:10\}\); \(m=6\): \(\{2:6,5:372,13:432,34:36,322:12\}\); and \(m=7\): \(\{2:7,5:882,13:1568,34:294,843:14\}\).

The finite calculations check implementation and small cases only; the unrestricted theorem follows from the symbolic proof in RESULT.md. No independent audit or formal proof-assistant certification is claimed.
