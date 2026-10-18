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

Write p=max(0,m-1)+epsilon. For m in (1,2) each of k maximum observations contributes epsilon^{m-2+epsilon}, so L diverges; for m>2 it tends to zero; for m<1 prefactor gives L~p^n prod(1-x_i)^{-1}->0. For fixed xi and p->infinity, each density tends to e^{-xi}, making positive large-p alternative. Thus boundary cannot maximize in open parameter space for any m>1 and is not even a limiting maximum for m<1 or >2. Printed observations yield two reported boundary MLEs with lower reported log-likelihood than same likelihood at p=20 (-44.4075>-49.20; -104.3629>-126.50), as derived by the source checker. Independently rederived sample endpoint trichotomy and Pr(M20>2)=0.94122822985 in reported simulation regime. m=1 and m=2 deliberately outside displayed trichotomy (zero probability under continuous model).

## originality

PASS

PASS for source-specific 2026 likelihood contradiction and material numerical effect, not for generic nonregular endpoint-MLE theory. Bakouch et al present correct likelihood and assert incorrect closed-form sample-max MLE; Hirano-Porter treat general parameter-dependent-support asymptotics but do not deduce this specific three-regime boundary or contradict datasets. Resultary and targeted published correction searches did not reveal a subsequent source-specific erratum.

## value

PASS

PASS: The false universal MLE is used centrally throughout a published simulation design and two applied model-fit comparisons, which cannot be inferred correctly from an endpoint consistency result. Explicit interior p=20 beats both printed MLE likelihoods; the problematic region affects roughly 94.1% of n=20 samples in a published p=5.3245 setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
