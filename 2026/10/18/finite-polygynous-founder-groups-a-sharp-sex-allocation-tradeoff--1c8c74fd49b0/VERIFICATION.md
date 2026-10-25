---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Let F~Bin(n,p), g(k)=min(k,h(n−k)), n≥3,h≥2. Discrete slopes of g are nonincreasing with at least one strict decrease, so Bernstein second derivative R″=n(n−1)E Δ²g(Bin(n−2,p))<0 for all 0<p<1 and endpoint slopes have opposite signs. Reflection around p=1/2 shows R′(1/2)>0 exactly for n≥3,h≥2, so unique output optimum p*>1/2 whereas S=1−p^n−(1−p)^n maximizes uniquely at 1/2; boundaries n=2 or h=1 share optimum. Lipschitz binomial concentration gives uniform R/n→min(p,h(1−p)) and linear asymptotic gain. For n divisible h+1, slope jump at q=hn/(h+1) makes exact CDF quantile equation; binomial CLT and quantile inversion prove √n(p0−p*)→(√h/(h+1))Φ⁻¹(h/(h+1)). For h≥n−1, g(k)=k except g(n)=0, so R=np−np^n and p*=n⁻¹/(n−1), giving n(1−p*)~log n and no mating ~1/n. Representative exact n=3,h=2 and finite differences independently checked.

## originality

PASS

The binomial expected mating function itself is explicitly Eq. 9 in Bessa-Gomes–Legendre–Clobert (2004), and its sex-ratio effects were already studied; neither is claimed new. The survivor is universal finite-(n,h) strict optimization/feasibility tradeoff, exact binomial optimum quantile and different fixed-h versus h≥n−1 asymptotics. The 2010 directly relevant mating-function paper was inaccessible at full-text level after lawful arXiv/OA attempts and authorized Oxford access returned VPN disconnected; material priority risk retained, not automatic rejection.

## value

PASS

Two natural biological objective functions (expected realized reproductive females versus probability of any mating) provably have different optimum allocations throughout precisely identified finite-group regimes; quantified CLT male correction and logarithmic reserve explain otherwise unintuitive finite-group effects. Mathematically motivated constrained optimization result, not an unsupported evolutionary or persistence claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
