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

# Verification of the Paley fourth-moment theorem

Run `python3 checker.py` (standard library only). The exact integer checks passed `EXACT_COMBINATORIAL_CERTIFICATE_PASS 335`, including all \(306\) nondegenerate triples of shift parameters for \(p=19\), all \(462\) for \(p=23\), the integer determinant \(11\) at \(p=11\), and difference-set counts for eight primes. The checker also tests weighted Fourier correlations using exact integer arithmetic. The general proof derives the inequality by finite Fourier orthogonality and Cauchy–Schwarz. Its large-prime equality classification uses the standard Weil character-sum bound; this analytical input is stated in the proof rather than inferred from tests. No computation purports to enumerate infinitely many primes. The verification does not constitute an independent mathematical audit.
