---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The proof reduces parking prefixes to iid parking marginals via a cited Lorentzian entropy contraction giving uniform o(1) TV error at k~lambda n/log n. An exact Borel ratio identity and uniform endpoint bias g(j)^2~2/(pi min(j,n+1-j)) yield optimal energy (4/pi)log M by rearrangement; exact censored chi-square and bounded third moments imply Gaussian log-likelihood N(-v/2,v) and TV=2Phi(sqrt(v)/2)-1. Fresh independent parking-function enumeration n=2..6 verified the Borel recurrence/reflection; n=1000 and 10000 energy diagnostics checked the constant. This is a conditional theorem using the published strengthened Lorentzian entropy lemma, not a finite proof of that lemma.

## originality

PASS

Best-of-knowledge original sharp budget-dependent profile; all cited generic and uncensored tools are treated as input, not new conclusions.

## value

PASS

Sharp and nonobvious statistical information budget law for random parking functions: boundary labels retain alpha fraction of critical testing signal, including full limiting power with o(n) observed labels. This is a motivated quantitative experiment-design boundary beyond uncensored TV thresholds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
