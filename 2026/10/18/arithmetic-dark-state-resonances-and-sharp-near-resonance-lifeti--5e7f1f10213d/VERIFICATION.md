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

Run `python verify.py` in the directory containing `requirements.txt` after installing `numpy` and `scipy`. This verifier reconstructs complete quantum Hamiltonians on \(2^d\) sites, independently computes the permutation-symmetric energy-space evolution, and compares the survival norms. It also uses exact rational binomial arithmetic at the unit-strength resonances, solves stable Lyapunov equations at nonresonant strengths, compares a derived exact mean-time identity, tests sharp low-order detuning coefficients, and compares the size-dependent coefficient against its Gaussian limit.

Expected successful terminal line begins `VERIFY_OK`. The number of finite cases is printed by the executable, not used as a substitute for the analysis. Values extremely close to distant, very small-weight resonances are not numerically evaluated by a stiff Lyapunov solver; the all-resonance result follows from the exact symbolic Lyapunov expansion in `RESULT.md`. Finite checks do not establish infinite quantifiers, independent review, or publication priority. The claim concerns a precise continuous single-sink dynamics; no inference is drawn about other quantum hitting protocols.
