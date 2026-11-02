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

# Verification notes

Run `python3 verify.py` from the directory containing the provided files. The completed run returned `VERIFY_OK 3477 finite assertions`.

The verifier enumerates all allowed length-two ordered pairs and computes a genuine infinite-word occurrence witness for each across \(2\le b\le10\), \(3\le m\le10\). It directly computes the first \(18{,}000\) symbols for \(2\le b\le7\), \(3\le m\le8\), independently constructs the corresponding substitution fixed point, compares their prefixes, and checks the absence of distinct factors related by plain reversal for lengths \(3\) through \(12\). It separately finds a binary-alphabet counterexample at \(b=2,m=2\).

The infinite assertion does not follow from bounded enumeration. Its proof is the carry-increment, triple, and four-factor argument in `RESULT.md`. The pair language is exhaustively proved by a constructive integer witness, not by the finite-prefix checks. No external independent audit has been carried out.
