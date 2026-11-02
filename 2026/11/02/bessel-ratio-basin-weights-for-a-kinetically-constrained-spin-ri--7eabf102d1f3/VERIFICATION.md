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

# Reproducibility and verification

The standalone program `VERIFY.py` uses only the Python standard library and can be run with `python VERIFY.py` from the same directory. It constructs the coefficient recurrence for the Bessel-ratio generating function independently of the full-state equations. A separate recursive finite Markov-chain first-step calculation evaluates each of the \(2^L\) initial configurations on labelled cycles and averages using the exact Bernoulli weights.

The program was run successfully, reporting `PASS 174 exact-rational/comparison checks`. Specifically, five choices of exact rational parameters were tested on eight cycle lengths each (40 equality tests), with 90 independent recurrence coefficient identities, 40 strict probability bounds and four numerical equal-rate exponent bounds. The exact finite-state tests use `fractions.Fraction` without Monte Carlo or floating-point tolerances. The four exponent bounds use Python floating point only to check the explicit tangent root lies in the physically expected interval.

The analytic singularity argument in `RESULT.md` establishes the existence and uniqueness of the dominant pole and the exponentially smaller remainder using standard Bessel-zero facts. No finite computation is represented as an infinite-size proof or as independent certification. Separate high-precision evaluations of the root equation were used for the illustrative values; no separate root-solving package is required to reproduce the finite exact checks.

Scope of scientific verification: labelled cycles of length at least three, independent occupied-site probability strictly between zero and one, positive isolated-death and facilitated-birth rates. Outside that scope no claim is made. Independent validation and a separate publication-priority audit are not yet performed.
