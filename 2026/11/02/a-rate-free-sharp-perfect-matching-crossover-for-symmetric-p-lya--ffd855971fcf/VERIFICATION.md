---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Inspected the exact threshold matching–ballot equivalence and reflection count, then independently implemented graph perfect-matching recursion and the symmetric Beta urn exact probability: 697 exact assertions verify the two characterizations and equal finite probabilities for even n=2..10 and three rational Beta parameters. Analytically, the reversed (n−1)-bit path has symmetric endpoint K, ballot probability E[2(K+1)/(n+K+1)*1_{K>0}], variance σ²=L+L(L−1)/(κ+1), and difference from E|K|/n bounded by O(n^{-1}+σ²/n²). The Beta mixing CLT and conditional centered-binomial CLT are asymptotically independent; every coefficient subsequence converges to a unit Gaussian combination, proving K/σ→N(0,1) for every κ_n→∞. Uniform integrability from exact second moment gives E|K|/σ→sqrt(2/π), and σ/n∼sqrt(1/n+1/κ). Finite enumeration corroborates, but the rate-free asymptotic comes from this analytic proof.

## originality

PASS

Reilly–Scheinerman already proved deterministic threshold-graph ballot matching and the independent-bit perfect-matching asymptotic; Yu–Alajaji–Gharesifard supplied the Pólya threshold graph law. Those results are credited rather than presented as new. Neither inspected source states the coupled n,κ→∞ rate-free Gaussian crossover; a general exchangeable ballot theorem might implicitly imply it, retained as a risk.

## value

PASS

The quantity is a natural random-graph feasibility probability. The exact effective size (n^{-1}+κ^{-1})^{-1} connects weak reinforcement, crossover κ∼n and independent-bit regimes in one sharp formula with no hidden growth-rate restriction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
