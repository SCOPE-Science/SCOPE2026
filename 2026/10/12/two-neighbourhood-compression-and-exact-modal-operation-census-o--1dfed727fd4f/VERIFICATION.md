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

# Reproduction

Run `python3 verify.py` with Python 3 and no external dependencies. The standalone program checks all local neighbourhood families for chains of one, two and three worlds against their canonical representatives and local box/diamond truth tables for every upset. It then exhaustively enumerates the possible local threshold words on chains of one through four worlds, restricting to continual words, and checks the number of distinct global operator signatures against the independent dynamic-programming recurrence.

A deterministic sequence of 4,800 random nested modal formulas is evaluated against original and compressed neighbourhood models with arbitrary persistent propositional valuations. Lastly, the closed binomial formula is checked against the dynamic-programming recurrence for one through eight worlds. Expected terminal marker: `VERIFY_OK`.

These are finite sanity checks. The all-size compression and enumeration depend on the local-signature proof, continual-prefix decomposition and the Vandermonde/hockey-stick counting argument in `RESULT.md`. The scripts do not certify an infinite quantifier by sampling, do not test arbitrary non-chain posets, and do not constitute independent validation.
