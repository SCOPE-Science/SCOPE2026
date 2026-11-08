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

For q>=2 an isomorphism class of a colour-partitioned bijection is exactly a multiset of directed q-colour necklaces, with Euler product ∏(1-z^d)^(-N_q(d)); Burnside gives N_q(d)=q^d/d+O(d q^(d/2)). Taking logarithms isolates H_q(z)/(1-qz), with H analytic and nonzero for |z|<q^(-1/2), so u_{n-s}/u_n=q^(-s)+exponentially small error. Marking finitely many specified necklaces gives independent geometric limits (1-q^(-d))q^(-jd) and rational capped-multiplicity event limits. For each local colour word v of radius R, necklaces deficient in T occurrences grow at exponential base beta<q by disjoint-block binomial bound; the multiset Euler product for deficient components converges beyond 1/q, proving exponential saturation of all long-cycle local types. Bounded-degree Hanf threshold locality then reduces any fixed first-order sentence (with function graph translated to binary relation) to finitely many capped short-necklace multiplicities, proving rational limit with exponential error. Excluding n=0 from sampling is harmless; q=1 is explicitly prior, with slower partition-ratio convergence. Independent Burnside counts for q=2 d<=7 and exact coefficient ratios were checked; not substituted for locality theorem.

## originality

PASS

The uncoloured-unlabelled zero-one law, necklace Burnside counts, and combinatorial transfer ideas are classical. Kuželka 2026 treats closely related unary functions, automorphisms and unlabelled counting, but accessible abstract alone does not resolve all conclusions; full text is an explicitly prioritized residual risk. No inspected source states the complete q>=2 rational first-order limit with exponential error under *uniform isomorphism-class* sampling and independent geometric necklace counts.

## value

PASS

The explicit all-sentence first-order limiting distribution and exponential convergence in a natural unlabelled model with named colours is a sharp transition from the known uncoloured zero-one law. Independent geometric necklace multiplicities give concrete nontrivial rational probabilities. This is a motivated logical/probabilistic classification, not a numerical sample or renaming of labelled Poisson laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
