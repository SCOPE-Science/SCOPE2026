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

Run `python3 verify.py` in the directory containing `verify.py` and `classes.csv`. The program uses only the Python standard library.

The verifier reconstructs every one-row/one-column deletion ball for every binary \(3\times3\) array twice by independent routines and requires exact agreement. It then solves the induced set-packing problem over all 16 possible \(2\times2\) outputs, proving the maximum code size is \(4\). Separately, it enumerates every four-clique in the compatibility graph, obtaining exactly \(514\), and checks that the 16 order-preserving square/channel symmetries partition these optima into exactly \(46\) classes with orbit-size distribution \(2^1,4^4,8^{20},16^{21}\). Finally, it recomputes `classes.csv` byte-logically as parsed CSV and verifies the displayed witness.

The finite computation proves only the stated binary \(3\times3\) theorem. It is not evidence for a general formula in larger dimensions. A successful run ends with `VERIFY_OK`.
