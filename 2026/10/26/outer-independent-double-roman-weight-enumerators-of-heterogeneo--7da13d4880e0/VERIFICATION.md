---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS. On B=K_1∨(⊔_{i=1}^t K_{m_i}) for t≥2 and every m_i≥2, the four values of the unique hub exhaust all possible configurations. Independent zeros prohibit two zeros in one blade, and prohibit any blade zero when hub=0. The zero/one/defense conditions split independently by blade after fixing hub; local factors are T^m−z^m, T^m−z^m+m(T^{m−1}−z^{m−1}−(m−1)z^m), T^m+m(T^{m−1}−z^{m−1}), and T^m+mT^{m−1} for hub values 0,1,2,3, T=z+z²+z³. The hub-zero defense requires t≥2 (or a 3-valued vertex), and the proof handles it. Summing z^h∏_i A_{h,m_i} gives ALL labeling weights. Minimal term has weight 3+Σ_i(m_i−1) with count ∏m_i; comparing next terms gives the stated distinct t=2 correction. Independently built adjacency lists and enumerated all 4^N labelings for five heterogeneous vectors, obtaining exact total enumerators and next coefficients; examples (2,2) total 558,min5,next25, (2,3) total2121,min6,next50, (2,2,2) total7084,min6,next36. The actual verifier compares full histograms for ten test vectors. Finite cases are corroboration only; local-case proof establishes all t and sizes.

## originality

PASS

PASS on the complete four-label WEIGHT ENUMERATOR and its second coefficient, but not on the scalar minimum. Crucially, the clique bouquet is a one-vertex corona K1⊙(⊔ K_mi), and Mojdeh–Samadi–Shao–Yero (arXiv:1909.01775) Theorem 12 already covers its optimum by a general corona formula; treating the minimum as newly discovered would be false. Theorem 12 optimizes one scalar; it does not count the nonminimal admissible functions, their weights, or the t=2 next-weight correction. Original introductory Ahangar–Chellali–Sheikholeslami paper (AMC 364:124617) was found only in abstract; authorized Oxford full-text access returned VPN disconnected, so material priority risk is explicit rather than a verdict from lack of access. Published nearby weight enumerators on complete multipartite graphs concern distinct Roman variants/graphs. No inspected stronger implication covered the full stated polynomial.

## value

PASS

PASS. For a natural heterogeneous clique bouquet (connected block graph with a single common cut vertex), counting ALL defensive labelings by cost yields a complete combinatorial distribution that strictly refines the already-known scalar optimum. The second coefficient exhibits a genuine two-blade-only boundary term, and uniform sizes recover common friendship/generalized windmill families. The result is narrower than a general graph domination theory but a motivated exact natural invariant, not an unmotivated tiny gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
