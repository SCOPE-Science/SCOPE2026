---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The greedy occurrence time of each fixed subsequence has first-hit PGF I_t and successive equal/different target-symbol waiting PGFs S_t,F_t, independently by the strong Markov property. Binary palindromes are encoded by a first symbol and mirrored adjacency indicators: odd lengths give 2(S²+F²)^k, even lengths 2S(S²+F²)^k. Coefficientwise summation and division by (1-z) yield exactly 2I(1+S)/[(1-z)(1-H)]. For 0<t<1 the positive solution H(r)=1 is simple, inside the unit circle, and the z²/z³ support ensures it is the unique dominant pole. At fixed z, H=F²+[z-(1-z)F]² is convex in F and any first positive crossing of level one has positive F derivative; since F increases strictly in t, r decreases strictly, so growth base increases. At t=0 P_n=n; at t=1 the alternating chain has a second dominant pole and only growth base, not one-constant asymptotic, is claimed. Independent exhaustive binary words n<=8, three exact Markov parameters and coefficient comparison (24 cases) corroborated the rational PGF.

## originality

PASS

PASS, qualified: Biers-Ariel–Godbole–Kelley analyze all distinct binary subsequences including a Markov source, but do not restrict to the language of palindromes. Rubinchik–Shur analyze contiguous palindromic factors and iid sources, a different random variable. The genuinely correlated 0<t<1 exact palindrome series and strict optimization were not identified as previously covered; general weighted-language generating-function machinery is a plausible reduction risk.

## value

PASS

Distinct scattered-palindrome complexity is a natural nonlocal word invariant; an exact rational expected-count generating function plus correlation-dependent exponential rate and optimal alternating source gives mathematically informative behavior not supplied by unrestricted subsequence enumeration or contiguous factor counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
