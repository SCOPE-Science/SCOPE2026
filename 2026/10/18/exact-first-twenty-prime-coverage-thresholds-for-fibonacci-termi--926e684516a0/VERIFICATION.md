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

# Exact finite reproducibility

Run `python3 verify.py` with Python 3 standard library. It generates every prime through \(1,803,947\) by integer Eratosthenes sieving, computes greedy Fibonacci coefficient expansions, parses the semi-proper blocks, and builds first-prime maps for each total digit length from \(1\) to \(20\). It verifies the full Fibonacci class count, each listed sharp maximum, and the last-attained word. The expected output begins `VERIFY_OK`; execution returned `VERIFY_OK prime_count= 135340 total_length_20_words= 10946 sharp_threshold= 1803947`.

No external file, downloaded paper, network connection, random seed, float approximation, third-party library or prior result record is needed to run this checker. Completeness rests on exhaustive enumeration through the witness prime and the Fibonacci word-count proof in RESULT.md. This finite certificate does not prove any asymptotic for larger terminal lengths. Independent audit has not been performed.
