---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The Weibull extreme level h_n=(log n)^(1/β), spacing b_n=h_n^(1−β)/β, and Gamma service fluctuation √h_n yield b_n/√h_n→∞,2,0 for β<1/2,=1/2,>1/2. Poisson extremal points with a Gaussian service mark give agreement probability 1 in the first regime and critical score x+g/2 in the middle. A Chernoff bound plus e^(Cs−c(s−K)^2) integrability excludes low-workload intruders when β≤1/2. At β>1/2 the expected number of rival jobs in [h_n−√h_n,h_n−√h_n/2] diverges, with independent Gaussian-tail chances to beat the workload winner. The Poisson winner void probability is 1/(1+A(g)); completing a square gives A(g)=exp(1/8−g/2)Φ̄(g−1/2)−Φ̄(g). Independent Simpson integration independently obtained p*=0.7444140829247499, matching the stated 0.744414083. Finite numerical integral is not proof of PPP convergence or intrusion cutoff; both were examined analytically.

## originality

PASS

The highly relevant Wu drawdown paper is about dependent random-walk excursions, not independent Weibull workload jobs with Gamma(ceil W,1) service clocks; Perfilev–Wachtel conditional excursion results are also distinct. Resultary search returned the submitted same-day record and tail/extremal results in other models, not an earlier statement of the same three-regime index-agreement probability or p*. Classical marked-Poisson concomitant theory is a plausible route to deriving the result, so exact historical priority remains bounded best-of-knowledge, not proven.

## value

PASS

A natural noisy-extreme ranking question: whether maximal workload and maximal realized Gamma-clock service duration occur at the same job. The explicit Weibull/Gamma model is mathematically motivated by excursion-length vs depth comparison; the shape-1/2 noise/spacing boundary with a nontrivial Gaussian-mark constant is a meaningful exact trichotomy, not a generic renaming or tiny computational observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
