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

# Reproducible verification

Run `python3 verify.py` with any current Python 3 interpreter and its standard library. It uses `fractions.Fraction` and factorial/binomial arithmetic throughout. The checker evaluates exact winner events by constructing every strict ranking for sizes two through six, and does not rely on the proof's cyclic-block decomposition to evaluate those cases.

The first set of tests compares exhaustive exact probabilities in each of the zero-, one- and two-impartial strata to the all-size expressions. The second set directly weights every triple of rankings under the contaminated mixture for \(n=2,3,4\) and four rational values of \(\varepsilon\), then compares to the interpolation polynomial. The final set checks the strict positivity of the directional perturbation coefficient for sizes three through one hundred.

The script returned `PASS: 125 exact independent probability identities or inequalities`. This exact finite replay is supplementary to, not a proof of, the general all-size combinatorial identities. The asymptotic \(Q_n\sim\pi^{3/2}/(2\sqrt n)\) is a published theorem of May and Sauermann; the script does not independently certify this infinite limit. No independent external audit has been performed.
