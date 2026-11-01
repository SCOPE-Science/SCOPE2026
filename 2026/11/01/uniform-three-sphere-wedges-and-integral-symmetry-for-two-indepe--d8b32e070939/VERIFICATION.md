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

# Reproducibility and verification
The all-parameter theorem is the combinatorial proof in `RESULT.md`. In particular, the contractible-cover argument and the exact integral connecting homomorphism are formal mathematical arguments, not extrapolation from finite tests.

Run `python3 verify_kneser2.py` with Python 3 standard library. The script requires no downloads or third-party packages. Its recorded output is embedded as `verification_output.txt`. It enumerates all faces for \(n=4,5,6,7,8\); for \(n=6\), an independent brute-force scan of every possible graph-vertex subset checks membership. It constructs explicit staged toggle matchings and verifies acyclicity against every Hasse arrow, checks the orientation and signed boundary of the octahedral cross-polytope, and checks all permutation characters for \(n=5\) and \(n=6\). The script fails by raising an exception if any assertion fails.

The sample computations verify finite cases only. They do not establish by exhaustion the universal quantifier over \(n\); that follows from the structural cover and exterior-algebra exact sequence. No independent audit or machine-formal proof is represented as having been performed.
