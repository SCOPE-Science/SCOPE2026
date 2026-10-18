---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Expanding D=muY-2muX+A where A=int_a^b x p²/q, differentiating p=f/ΔF and q=g/ΔG under endpoint changes and using Leibniz gives dD/da=(2h1X-h1Y)D+2(h1X-h1Y)(muX-muY)-a(h1X-h1Y)²/h1Y; upper gives (h2Y-2h2X)D+2(h2Y-h2X)(muX-muY)+b(h2X-h2Y)²/h2Y. These have the correct equal-density zero-derivative limit unlike the published formulas. Symbolic cancellation and representative exponential numerical check corroborate, but the displayed unrestricted calculus proves the result.

## originality

PASS

Earlier unweighted Pearson and weighted KL truncation results concern different weighted integrals. The checked primary paper itself prints contradicting derivatives; no relevant correction was found, although basic Leibniz differentiation is known mathematics.

## value

PASS

Correctly computing both moving truncation-boundary derivatives is necessary for monotonicity and inequalities used in source Theorems 2.4–2.7 and 3.1; a simple exact equal-law stress test exposes the error. This is a useful source-specific analytic repair, not a claim that all theorems relying on the wrong formula are false.

The dated certificate retains the supplied scientific assessment, sources and limitations.
