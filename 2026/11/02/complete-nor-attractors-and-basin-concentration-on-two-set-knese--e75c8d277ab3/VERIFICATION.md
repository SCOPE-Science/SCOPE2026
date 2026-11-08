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

PASS. Define F(S) as the family of edges meeting every edge of S, with intersection including equality and open-neighborhood NOR on KG(n,2). Symmetric antitone polarity gives S⊆F²(S) and hence F³=F; every state enters a period <=2 orbit in one step. If F(S) nonempty, S has a size-two vertex cover; classifying its two spoke-end sets A,D and optional central edge gives all image shapes: n stars and C(n,3) triangle fixed points, and precisely 1+C(n,2)+3C(n,3)+9C(n,4) 2-cycles in five described classes. Explicit preimage enumeration yields g_n, h_n, e_n, 1, 2 and remaining B_n basin sizes; Bonferroni on size-two vertex-cover events yields exceptional tail asymptotic and majority threshold n=6. Independently enumerated ALL 2^10 and 2^15 configurations for n=5,6 with NOR transitions, F³=F, basin histograms, B_5=389 and B_6=27627.

## originality

PASS

Best-of-knowledge originality from explicit theorem-level source comparisons. The narrower final novelty is preserved; older established components are credited. Search absence does not prove priority.

## value

PASS

PASS. Exact attractor and basin census on a natural Kneser family is structurally richer than the general F³=F polarity fact: the large empty/full attractor basin undergoes a sharp majority threshold at n=6 and eventually captures 1-2^{-Theta(n²)} of states, while numerous small periodic orbits survive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
