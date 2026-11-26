---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The character m of the frequency torus is trivial on the full orbit closure exactly when sum m_l lambda_l=0, and on the line orbit closure exactly when that sum is orthogonal to v. Avoiding the countably many proper hyperplanes gives full measure and a dense G_delta, and equality of annihilators gives equality of the closed subgroups. Each of n phase vectors can therefore be approximated separately; the modulus-one quotient error is at most twice the individual error, and the normalized positive weights preserve that bound. The reverse inclusion follows by sampling the line in the original space. No intersection over sample sizes is needed. Adding a positive constant with renormalization, then multiplying by exp(-tau t^2), preserves positive definiteness. Reality plus positive definiteness implies evenness, bounded derivatives of the finite exponential sum give Schwartz decay, and each exponential gives a shifted Gaussian Fourier term with the stated normalization. The strict positivities are on the real axes, not on the complex planes. For the chosen finite sample diameter D the error is bounded by 2 delta + 2 alpha + tau D^2, so the scales can be chosen in that order, including D=0. This proves closure equality and finite-sample approximation, not exact equality or a single Schwartz kernel for every sample. Replay: RESULT.md lines 25–74 give the analytic certificate; VERIFY.py and VERIFICATION.md were read, not executed, and the bounded illustration is not needed for the theorem.

## originality

PASS

The closest primary work constructs a seven-variable witness and also shows that strict pointwise positivity alone is compatible with the defect; neither the witness theorem nor its positivity argument supplies a generic-line Gram closure or a one-dimensional regularization strictly positive in both domains. No matching statement was identified in the inspected Resultary material. Classical tools are credited rather than claimed as new.

## value

PASS

The nontrivial dimension question is posed by a concrete seven-dimensional counterexample. Equality of all fixed-size Gram closures for the same generic direction makes dimension irrelevant for any strict continuous finite-Gram obstruction in the stated class. The Schwartz refinement also removes both function and spectral zeros without losing a strict defect, which is stronger and more useful than merely finding another numerical counterexample or adding a constant to the known one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
