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

# Reproducible exact verification

Run `python artifacts/verify_radau_directed_cycles.py` after installing `artifacts/requirements.txt`. The included `artifacts/verification_output.txt` is the result of an actual execution of this standalone script against the actual packaged code.

The script checks the exact scalar Taylor coefficients, constructs rational matrix inverses for each directed unit-rate cycle of orders two through six, proves that all five denominators have positive coefficients, checks stochastic row sums exactly, and checks strictly nonnegative coefficient certificates for all numerator classes up to order five. For the six-cycle it verifies the displayed denominator factorization and exceptional polynomial \(h^5p(h)\), checks all four other off-diagonal numerator classes, verifies all eleven positive degree-ten Bernstein coefficients for the diagonal on \([0,1]\), and checks all eleven coefficients of the shifted diagonal on \([1,\infty)\). It also verifies \(p'\) has strictly positive coefficients and the exact witness at \(h=1/10\). Symbolic identities are exact, not floating-point residuals.

Analytical arguments, independently included in the proof, establish local nonnegativity for **all** finite CTMC generators with at most five states by shortest-path expansion, small-step sign loss on **every** longer unit-rate directed cycle, and eventual positivity on those cycles through Fourier spectral convergence. These quantifiers are not inferred from the finite order-two-through-six symbolic checks. The six-cycle's entire step classification uses polynomial positivity certificates rather than sampled signs.

The root \(\tau\) is specified exactly as the unique positive zero of \(p\); its decimal representation is illustrative only. The proof does not claim independent auditing, external theorem certification, floating-point safety or any nonlinear result.
