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

# Reproducible verification

Run `python3 verify.py` using Python 3 with no external libraries. It checks exact parameter counts for odd primes \(3,5,7,11\). For \(p=3\), it exhaustively evaluates all \(27^2\) group-element pairs for each of \(810\) parameterized group Rota–Baxter operators, and independently enumerates their image sets and the image sets of their duals. For \(p=3\) and \(p=5\), it enumerates all matrices \(A\), verifies the lift-fiber cardinalities, and computes the orbit decomposition under \(\mathrm{GL}_2(\mathbb F_p)\).

Expected printed checks include `VERIFY_OK` and `BRACE_VERIFY_OK`. The complete proof for every odd prime is in `RESULT.md`; finite enumeration is a consistency check rather than a proof of the unrestricted quantified claims.
