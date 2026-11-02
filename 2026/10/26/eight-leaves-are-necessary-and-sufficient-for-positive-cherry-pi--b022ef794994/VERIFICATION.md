---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Conditioned on the four Ford alpha attachment-edge categories, rederived the five raw moment recurrences for cherry C_n, pitchfork A_n, C_n^2, A_n C_n and A_n^2 with denominator n-alpha. Starting at the unique n=3 state, independent SymPy recurrences give the exact n<=7 covariance formulas and reproduce the two degree-4 and degree-6 numerator polynomials for n=6 and n=7. After substituting alpha=t/(1+t), the relevant numerator polynomials have strictly positive coefficients for t>=0, establishing covariance<0 on 0<=alpha<1 for 4<=n<=7; n=3 covariance=0. Differentiating the moment recurrences at the deterministic comb boundary alpha=1 yields linear-response coefficient r_n=(n-3)/2-H_{n-3}. Since r_{n+1}-r_n=1/2-1/(n-2)>0 for n>=5 and r_7<0<r_8, r_n>0 for every n>=8. Fixed-n rational analyticity gives positive covariance for alpha<1 sufficiently close to 1. The exact symbolic checks independently corroborate n<=7 signs and the universal harmonic threshold; they do not replace the recurrence induction.

## originality

PASS

Qualified PASS: Kaur–Choi–Wu 2023 contains the full joint distribution recurrence, means, second moments and eventual sign change at alpha=1/2 for sufficiently large n. It does not state the exact smallest leaf count for positive covariance or the near-comb harmonic first-order coefficient. Wu–Choi 2015 treats only the Yule and PDA endpoints, which do not capture near-alpha=1 positivity. Derivation from a preexisting exact recurrence is mathematically valid new implication when the nontrivial all-n sign inequality and natural sharp n=8 cutoff were not stated; potential independently published finite-size consequences remain a priority risk.

## value

PASS

The first leaf count permitting positive cherry/pitchfork covariance is a canonical finite-size threshold for a standard phylogenetic random tree model. The closed-form harmonic first derivative supplies an explanatory all-n mechanism, and exact small-n sign exclusion completes the natural classification; not mere tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
