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

# Reproducibility and limits

Run `python3 verify_drt_path_h1.py` using Python 3.8+ standard library; compare with `verify_drt_path_h1.log`. The verifier checks Paley digraph arc orientations for \(7,11,19,23,31\) vertices, verifies tournament and pairwise-degree identities and enumerates every triple, including all common source/sink apexes and integral triangle boundaries. A separate procedure constructs finite regular degree-two boundary generators and performs exact modular elimination for Paley \(7\), Paley \(11\), and the cyclic seven-vertex tournament at primes \(2,3,5,101\).

The expected final line is `VERIFY_OK_DRT_INTEGRAL_PATH_H1`. These tests do not give an infinite proof, do not establish integral homology by modular ranks alone, and make no claims about degree-two or higher homology. The full integral and uniform argument is written in `RESULT.md`.

Independent audit has not been performed.
