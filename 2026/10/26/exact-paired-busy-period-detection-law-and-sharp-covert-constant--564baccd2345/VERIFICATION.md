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

Each busy trajectory with N=j has j-1 arrivals, j departures, and 2j-1 exponential waiting times of rate lambda+mu. Its Catalan path density is theta^(j-1)mu^j t^(2j-2)e^-(theta+mu)t/[j!(j-1)!]. Therefore T|N=j is Gamma(2j-1,theta+mu); conditional jump ordering and waiting-time simplex given the pair are parameter independent, giving Blackwell equivalence to full unmarked within-busy paths. Log likelihood is S log((lambda+eta)/lambda)-eta U, so exact gamma/ballot weights and the Gamma CDF at q S give both NP errors. Conditional likelihood changes sign under either marginal observation, making paired TV strictly larger. E[S]=lambda/(mu-lambda), E[U]=1/(mu-lambda) give exact KL pair and positive count-only information gap; score variance is 1/[lambda(mu-lambda)], giving LAN Gaussian total error. Small-eta expansion plus the pooled-Poisson initiating-customer source mark yields Kpair=mu sqrt(2/[lambda(mu-lambda)]). Fresh independently generated ballot-Gamma sums at (lambda,mu,eta,k)=(1,3,0.25,2) give alpha 0.286581758460309, beta 0.632887806741184, plus KL and Fisher comparisons. Analytic arguments justify infinite sums, strict inequalities and limits.

## originality

PASS

Qualified PASS: The 2026 Sahithi–Yardi–Ravi primary article presents alternative count-only and duration-only monitors, not their paired simultaneous observation theorem. Classical count/duration joint busy-period laws (Takács/Prabhu) and M/M/1 stopped-path sufficiency (Clarke, surveyed by Asanjarani et al.) are prior and explicitly not claimed new. The target contribution is the paired Gamma–ballot NP risk, strict simultaneous-report detection superiority, information gain and local covert coefficient. Full historical Takács and earlier covert queue paper not verified, so priority risk remains.

## value

PASS

PASS: A paired count-duration release is the natural information-larger observation model in a specific 2026 covert monitoring problem. It yields quantitative finite optimal detection and sharp square-ROOT insertion constant not available by treating marginals separately. Correct Gamma conditional dependence also exposes a scientifically important distinction from a parameter-free conditional-duration assertion in the source; generic exponential-family sufficiency alone is not assigned value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
