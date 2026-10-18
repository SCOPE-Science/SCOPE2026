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

For one Bell-pair block a selected subsystem retains 0/1/2 endpoints and contributes purity 1,1/2,1; selecting one endpoint has combinatorial multiplicity 2. Hence the contribution after weighting by purity has local polynomial 1+x+x², proving mean m-subsystem purity [x^m](1+x+x²)^K/binom(2K,m). For m=K, the coefficient is the central trinomial T_K∼sqrt(3)3^K/(2sqrt(pi K)), while binom(2K,K)∼4^K/sqrt(pi K), yielding sqrt(3)/2(3/4)^K. The ratio to 2^-K grows as (3/2)^K and Scott Q_K tends to 1; K≥2 states factor into entangled two-qubit blocks and have depth 2. Independently enumerated K≤8 subsets; the asymptotic follows analytically, not from finite enumeration.

## originality

PASS

Facchi et al. define the balanced purity potential and universal lower bound; Scott defines normalized average-subsystem purity. Prior de Oliveira–Rigolin work already points out that Bell-pair products can lack genuine multipartite entanglement despite high global-entanglement values, so that qualitative point is not counted as new. Exact all-m coefficient profile and central-trinomial asymptotic are distinct from a four-qubit generalized average under a different convention. No equivalent profile was located in targeted searches.

## value

PASS

This gives a closed benchmark for a natural structured multipartite state family at every subsystem size, with a sharp exponential separation from the balanced minimum and a precise warning about interpreting normalized purity saturation as high entanglement depth. The full exact object-specific invariant and scale law survive despite the previously known qualitative example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
