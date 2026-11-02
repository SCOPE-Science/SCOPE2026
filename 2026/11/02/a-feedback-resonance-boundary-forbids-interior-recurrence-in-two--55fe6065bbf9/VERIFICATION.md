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

Install Python 3.10 or newer, SymPy, NumPy and SciPy, then run `python verify.py` in the directory containing `verify.py` and `requirements.txt`. The script was executed against its own files, successfully verifying the exact total derivative, the algebraic feedback resonance, the all-parameter equilibrium family in the symbolic parameter \(u\), exact rational values for the two Fig. 8 feedback triples, and a numerical initial-value trajectory check of 101 time samples over \(0\le t\le10\).

The numerical maximum absolute error in the affine-log-odds identity was \(2.9574\times10^{-12}\). These numerical samples corroborate, but do not prove, the nonrecurrence statement. Its proof is the elementary differentiation, plus compactness and the quantitative one-sided log-odds estimate, reproduced in `RESULT.md`. The no-recurrence theorem makes no claim for compact sets on environmental boundaries. A resonant feedback ratio is necessary, not sufficient, for interior recurrence under arbitrary payoff games. No independent validation has been performed.
