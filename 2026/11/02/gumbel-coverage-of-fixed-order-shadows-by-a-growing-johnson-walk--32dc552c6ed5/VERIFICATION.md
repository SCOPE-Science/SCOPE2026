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

# Reproduction of finite checks

Execute `python3 verify.py` with Python 3. The code uses only the standard library, exact integer binomial coefficients, and `fractions.Fraction`. It constructs (i) the full uniform single-swap walk on all \(r\)-element sets and (ii) the reduced chain on the intersection with the union of prescribed \(s\)-subset targets. For 22 specified finite cases, it checks the exact projected initial law, the full and reduced surviving distributions at eight consecutive times, the survival probabilities, and stationary entrance flux. The replay printed `PASS 396 exact-rational comparisons across 22 small-volume target families`.

# Analytic checks and limitations

The complete proof in `RESULT.md` independently derives the bounded projection, explicit pure-death diagonalization, uniform eigenprojector control, regenerative rare entrance rate, fixed-order factorial-moment limit, and mean tail bound. Its nonstandard rate estimate is \(1-\rho_F=d\binom{r_n-1}{s-1}/\binom ns\,[1+O_{s,d}(r_n/n)]\) for every fixed family of \(d\) distinct targets. This is a mathematical assertion proved by the excursion and return-transform argument, not an empirical estimate inferred from the checker. The checker tests exact finite identities, not the uniform matrix-resolvent bounds or the infinite-dimensional limit of missing targets. No growing-target-order or positive-density-block extension has been verified.
