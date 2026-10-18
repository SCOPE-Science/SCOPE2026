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

Run `python3 verify.py` with Python 3. The program constructs Euler's totient by (a) prime-factor multiplicative depletion and (b) least-prime-factor recurrence, compares all results, independently computes the Nontotient iteration heights from each, and compares these as well. It then checks the complete dyadic maximum table and maximizer multiplicities, the earliest jump of at least three, and the full terminating orbit of the unique extremizer. It prints `VERIFIED` only after all assertions pass.

Coverage is **all positive integers up to 524288**, not a random trial or heuristic extrapolation. The proof includes why these recurrences compute exact arithmetic values. Python's integers and arrays suffice; no downloaded datasets or unbundled libraries are required. The code does not check any integers beyond 524288 and makes no assertion about later maxima. The scientific novelty comparison is literature-dependent; reproducible computation does not establish publication priority. No independent audit or third-party certificate has been performed.
