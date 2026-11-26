---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Gaussian cross-entropy at fixed positive variance is uniquely minimized at the true mean, after which optimizing the variance gives the true variance; both moments and differential entropy are finite for a>0. Strict positivity of forward KL follows from unequal laws (bounded beta support). Beta logarithmic moments, derivative of log B(a,a), and trigamma duplication give J'=-1/(2a+1)+(a-1)Delta(a), with Delta(a)=psi_1(a)-psi_1(a+1/2)>0. This is negative for 0<a<=1. For a>1, the trigamma difference integral is the Laplace transform of t/(1+exp(-t/2)). Strict AM–GM bounds Delta by 1/[2(a-1/4)^2]=2/(2a-1/2)^2; (2a-1/2)^2-2(a-1)(2a+1)=9/4, proving strict negativity. Independently, the kernel factor 1/(1+exp(-t/2))=1/2+t/8+O(t^3) near zero, giving Delta=1/(2a^2)+1/(4a^3)+O(a^(-5)) by Laplace integration, with exponentially small tails away from zero. Then J'=-3/(8a^3)+O(a^(-4)). To see J(infinity)=0, use Y=2X-1: its entropy is log B(1/2,a)-(a-1)[psi(a)-psi(a+1/2)]=(1/2)log(pi e/a)+O(1/a), by the gamma ratio and digamma expansions. The moment-matched Gaussian for Y has variance 1/(2a+1) and the same leading entropy. Integrating J' from infinity gives a^2 J(a) -> 3/16. The odd Uniform sample median has shape a=(n+1)/2, so the variance is 1/[4(n+2)], strict decrease holds for successive odd sizes including n=1 to 3, and n^2 K_n -> 3/4. Inspected requirements.txt, verify.py and VERIFICATION.md; the mpmath tests are diagnostics, not universal evidence, and the uploaded code was not run.

## originality

PASS

The supported distinct core is the global strict derivative sign over the continuous symmetric-beta shape family for the optimal forward Gaussian KL projection. Exact beta entropy, Gaussian optimization, and the order-statistic entropy expansion are prior ingredients. The leading constant is a sharp consequence of known special-function asymptotic tools, not the main novelty. The published Cardone–Dytso–Rush discussion is a material remaining access risk, not evidence of equivalence or noncoverage.

## value

PASS

This settles a natural strict-order question for a canonical bounded family under an optimal information-theoretic approximation, across all positive shape parameters, not just the asymptotically normal regime. The global sign requires a uniform special-function inequality, and its exact sharp rate and consequence for the best Gaussian at every odd median sample size are independently interpretable. No reverse-KL, asymmetric-beta, or general order-statistic monotonicity is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
