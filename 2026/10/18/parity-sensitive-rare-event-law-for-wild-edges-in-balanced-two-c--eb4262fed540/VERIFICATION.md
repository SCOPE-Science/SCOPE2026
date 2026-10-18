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

# Reproducibility

Run `python3 verify.py` from the directory containing this document. This standalone standard-library script exhaustively enumerates all fixed-half-edge two-colour complete graphs on four to seven vertices, independently computes component counts in both colour classes, and checks the exact isolation formulas. It also compares the asymptotic coefficient, including the parity correction, at eight larger orders.

The recorded output is supplied as `verification_output.txt`; it was produced by executing the script. The exhaustive tests enumerate exactly \(20+252+6435+352716=359423\) edge assignments, not all possible sizes of complete graph.

The limiting formulas and all error estimates are proved in `RESULT.md`. Finite arithmetic checks cannot validate the full asymptotic quantifiers or settle bibliographic priority. Independent mathematical audit has not been performed.
