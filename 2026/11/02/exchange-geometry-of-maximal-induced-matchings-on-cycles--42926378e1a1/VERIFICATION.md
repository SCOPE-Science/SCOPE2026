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

# Reproducibility and limitations

Run `python3 verify_primary.py` (Python 3 standard library) to directly enumerate the cycle-edge subsets through \(n=18\); success ends with `DIRECT_SUBSET_VERIFICATION_PASS 23`.

Compile `verify_alt.cpp` with `g++ -std=c++17 -O2 verify_alt.cpp -o verify_alt` and run `./verify_alt`; success ends with `INDEPENDENT_GAP_EXCHANGE_PASS 53`. This checker generates configurations from bounded cyclic compositions rather than enumerating all subsets, and reconstructs the one-edge exchange graph before testing its counts.

The primary and alternate executable sources were run as supplied. The algorithms independently verify finite instances but do not substitute for the proof for arbitrary \(n\). No external independent scholarly audit is represented or implied.
