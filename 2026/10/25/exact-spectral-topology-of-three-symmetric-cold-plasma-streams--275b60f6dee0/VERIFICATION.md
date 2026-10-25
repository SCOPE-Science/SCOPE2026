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

# Reproduction and boundaries

`python check.py` requires Python 3 with NumPy and SymPy. The program checks twelve exact polynomial identities, root classifications over 2,500 sampled positive density ratios and wavenumbers, and both asymptotic expansions. The full all-parameter classification follows from the discriminant and sign argument in `RESULT.md`; numerical sampling is not an exhaustive search and is not used as the proof.

The idealized assumptions (three cold electron delta distributions, two equal opposite streams, stationary third stream, fixed neutralizing ions) are essential. At positive cutoff wavenumber the frequency roots are repeated and algebraic time dependence is possible despite absence of positive imaginary frequencies. Independent audit has not been performed.
