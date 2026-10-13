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

Run `python3 verify.py` with Python 3 (no third-party modules) in a directory containing the two supplied files. The verifier constructs all the integer normalized coefficient polynomials, confirms their degrees and leading coefficients, and then reduces pairwise mass differences modulo the prime \(1000003\) **after removing only exactly present integer-polynomial powers of the parameter**. Its output verifies exactly \(109943\) Euclidean gcds for the first eight orders and confirms the identities at the sole exceptional triple.

Expected orderwise triple counts are \(35,286,1330,4495,12341,29260,62196\). The exceptions are exactly \((1,3,4)\) with modular gcd \(t+6\), one for each order \(k=4,5,6,7,8\); their common positive real roots are absent because the exact characteristic-zero common root is \(-6\). All other modular gcds are \(1\).

The proof also uses two analytic facts not certified by a finite run: modal localization via the coefficient recurrence and the **published** strict compound-Poisson log-concavity theorem at \(\lambda>2\). These steps are reconstructed in RESULT.md. The assertion for every real positive parameter follows by the factor-lifting argument, not grid sampling. The theorem does not cover orders \(k\ge9\), unequal component rates, or exact modal transition thresholds.
