---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For independent Bernoulli(p) vectors X,Y and symmetric increasing threshold H_{n,k}, the exact disjoint witness criterion is S>=k,T>=k,U=|X∨Y|>=2k; hence product defect D=P(S>=k,T>=k,U<2k), and Δ=P(Bin(n,p)>=k)^2−P(Bin(n,p)>=2k). The sandwich P(U<2k)−2P(S<k)<=D<=P(U<2k), together with p<u=2p−p²<1, Chernoff and binomial CLTs, proves Gaussian windows at k=np/2+x√n and k=nu/2+x√n. Source Section 6 pivot identity with conditional X|occupied Bernoulli(1/(2−p)) gives exponentially negligible support failures and a local CLT √n π_i→φ(z)/σu and ||ρ||₂ same. Bivariate CLT for (J=sum XY,U) yields Gaussian truncation G_U<2x and conditional mean −p²(1−u)φ(z)/(σu Φ(z)); second moments give uniform integrability. Rare phase k/n→a∈(0,u/2) uses relative conditional Chernoff + binomial tail Stirling/geometric ratio with r_n=(2k−1)/n to retain lattice corrections. Independently enumerated all pairs of bit masks through n=6 at p=2/5, checking exact finite D, Δ and union-tail sandwich; asymptotics justified analytically, not finite samples.

## originality

PASS

Qualified best-of-knowledge PASS: Tesio (2026) already supplies exact disjoint-testimony threshold identity and pivot definitions plus general strengthened BK inequalities, and Cerf–Tesio supplies equality/background. This assessment does not count those facts as novel. The pair of different Gaussian transition windows, sharp pivotal norm, selected-overlap Gaussian truncation and rare-defect prefactor are more specific than the accessible primary abstract. Complete Tesio manuscript unavailable for confirmation; any equivalent worked-out Section 6 asymptotics remain a material originality risk.

## value

PASS

Natural threshold-event model reveals two separate macroscopic Gaussian transitions governed by p and u, identifies when the symmetric-pivot lower bound has correct order, and characterizes the configuration overlap selected by disjoint-testimony failure and precise rare tail. These answer meaningful quantitative questions in BK inequalities without pretending to improve the universal bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
