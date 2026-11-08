---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The de Bruijn automaton after deleting the one forbidden edge is primitive via a zero padding path and all-zero loop. Its entropy eigenvalue lambda obeys phi<=lambda<2 because the golden-mean shift is contained. The weighted border generating function provides rho-1/2=E/(2Q^2*x0*F_x), with E=sum_b (2ones(b)-len(b))*lambda^{len(b)} and negative denominator. Short borders 1,11 contribute lambda+2lambda^2; each longer border is nonpositive. Every negative border beginning and ending 11 contains at least four ones and must have length>=9; thus E<=lambda+2lambda^2-lambda^9<0 for lambda>=phi. Direct independent KMP finite-state Perron calculations for (1100000011)^r, r=1,2,3 reproduced lambda~1.9980411457,1.9999980945,1.9999999981 and rho~.5009784186,.5000019044,.5000000027. The all-length sign theorem follows from the analytic argument, not finite tests.

## originality

PASS

The Bóna–Maga–Richey 2026 paper supplies the weighted border identity and addresses equal-frequency/balanced borders; it raises a mixed-sign issue. The candidate theorem gives a concrete sufficient sign criterion despite arbitrarily many zero-heavy overlaps, a different implication from balanced iff half. Resultary returned unrelated word statistics. Best-of-knowledge PASS, but complete primary text could not be inspected and another contemporaneous balanced-border characterization may contain a relevant proof ingredient.

## value

PASS

The exact sign of limiting symbol bias for one forbidden pattern is a natural symbolic-dynamics invariant. This theorem resolves a motivated infinite mixed-border region with no bound on number of competing borders; its entropy-floor domination is a nontrivial structural sufficient condition, albeit not a full conjecture solution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
