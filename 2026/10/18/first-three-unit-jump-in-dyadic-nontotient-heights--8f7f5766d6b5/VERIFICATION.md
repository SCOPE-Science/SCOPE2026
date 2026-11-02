---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of cototient-height maximizer fibers

Execute `python3 verify.py` in the directory containing `MAXIMIZERS.json`. The program computes exact Euler totient arrays through \(2^{19}\) by prime-factor depletion and smallest-prime-factor recurrence, then computes all cototient iteration heights by induction in increasing argument order. Each result is compared against the other method. The complete sets of maximizing arguments in each dyadic interval are compared with every entry in `MAXIMIZERS.json`. All 123 listed arguments are thus checked, including all 44 attaining height 30 at scale 18 and the sole height-33 argument 462210 at scale 19. The resulting height maxima and the length-33 witness orbit are also asserted.

This is a finite exhaustive certificate, not a formal proof in Lean, an external expert attestation, a verification of any higher dyadic scale, or proof of novelty. The recurrence identities and finite coverage are given in `RESULT.md`. The earlier OEIS first-hit table already determines the maximum-height threshold and is credited explicitly; the new certificate concerns complete extremal-position fibers. Verification-status channels are managed separately from the mathematical computation.
