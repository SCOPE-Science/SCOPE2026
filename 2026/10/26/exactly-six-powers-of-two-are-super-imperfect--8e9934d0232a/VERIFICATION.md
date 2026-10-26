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

Run `python3 verify.py` with Python 3. No third-party modules or network access are needed.

This checker uses exact integer arithmetic. It evaluates the iterated arithmetic function for all \(1\le a\le24\), checks primality of \(F_0,\ldots,F_4\) by trial division, checks \(F_5=641\cdot6700417\), tests the required \(2\)-adic valuation identity on nine odd prime bases with sixteen geometric lengths, checks 113 first-omitted-bit instances, and confirms the modulo-sixteen obstruction for 99 even exponents.

The full theorem depends on the all-exponent proof in `RESULT.md`, not on experimental coverage. Finite tests cannot exclude all larger exponents and are not presented as independent mathematical audit or formal certification.
