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

# Verification and reproducibility

Execute `python3 verify.py` using Python 3 with only standard-library modules. The verifier reconstructs the Lucas pairs for \(1\le P\le20\), all primes \(p\le43\), and indices \(1\le n\le200\). It independently calculates prime valuations, compares their closed forms, performs Möbius inversion from the actual terms, checks all repaired Dold congruences in range, checks exact Dold criterion predicted by the quadratic character and parity, and tests nonnegativity or negativity of the computed transforms. A successful run yields:

`VERIFY_OK parameter_prime_cases=280 max_index=200 U_and_V_exact_valuations=PASS repair=PASS signs=PASS`

These checks were actually executed. Their finite search range cannot establish assertions for all parameters, primes, and indices. The proof in `RESULT.md` supplies the infinite valuation reductions, Möbius-support calculations, minimality witnesses, and prime-density argument; the verifier is a reproducible error check rather than an infinite proof or independent validation. The minimum-multiplier computation is proved symbolically, not exhaustively sought over multipliers of unbounded size. No independent audit has been performed.
