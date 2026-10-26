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

# Reproduction and limits

The executable `verify.py` contains no imported project-specific libraries. Run `python3 verify.py` using the Python standard library. It sieves every prime at most \(2000\), checks all \(45{,}753\) distinct pairs \(p<q\) for the necessary prime-support condition, and checks the three concrete excluded pairs and the congruence forcing \(p\mid13\).

The expected result is a `VERIFY_OK` line. The enumerated cases do **not** prove universal nonexistence. That conclusion is established by the exact argument in `RESULT.md`, including the three-adic valuation lemma, the multiplicative-order lemma, the comparison \(\Phi_3(p)/3<q^2\), and the final prime-support contradictions. No independent audit or external proof certification has been performed.
