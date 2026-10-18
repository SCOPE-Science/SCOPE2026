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
# Reproducibility and limits

Run `python3 verify.py` with Python 3 and SymPy available. The included script is self-contained and uses exact rational `fractions.Fraction` arithmetic to enumerate permissible base digit words, reconstruct the periodic fiber points, and verify their returns on the concrete parameter choice. The base fixed-point counts for periods one through four are respectively \(0,2,3,6\); the full three-dimensional point counts are \(0,48,546,7200\). The script also checks forty rational cases of the sharp scalar fixed/period-two classification, thirty-nine primitive-period integer-base divisibility cases, and a symbolic logarithmic-derivative identity for the rational zeta. Its completed run printed `PASS`.

All-period factorization is proved in `RESULT.md` from the half-open integer-fiber lemma, not inferred from finite experiments. Branch boundaries are handled by explicit strict and non-strict inequalities. The code tests the quadratic case \(\gamma=2\), not every nonlinear exponent; the proof covers all positive integral exponents. It neither searches all parameter space numerically nor proves an independent literature-novelty certificate.
