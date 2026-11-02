---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The moment-free reverse inclusion is obtained by symmetrizing X-X′ and applying the cited symmetric-randomization transfer lemma. Independently checked its probabilistic core: Bernoulli thinning yields E B_N=pi A_N and E B_N^2<=pi A_N^2, hence Paley–Zygmund P(B_N>=pi A_N/2)>=pi/4. Integrating a positive power yields a uniform P(V_N>=c U_N/2)>=c/2; monotone divergence and Kolmogorov 0-1 show a.s. divergence of the thinned quadratic norm. For q<2, infinite L2 gives block sample averages diverging in probability; the dyadic construction has deterministic mass sum 2^-j and randomized lower contributions 2^j eventually a.s. (Borel–Cantelli). Sufficiency and some necessity/strict embedding invoke precisely numbered published supporting lemmas, whose full text could not be independently retrieved; this is a stated external dependency, not a formal certificate.

## originality

PASS

Chen–He–Wang 2026 explicitly describes only partial q<4 necessity/sufficiency and L4-assumed reverse inclusion, whereas the new claim asserts a complete 0<q<4 threshold and removes all reverse moment hypotheses. Its exact published theorem text was not accessible (authorized institutional request blocked), leaving a nontrivial implication/priority risk.

## value

PASS

Completing a partially characterized parameter regime and removing a fourth-moment hypothesis are mathematically motivated functional-space randomization results; the unbounded-moment counterexample mechanism and exact centering boundary are substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
