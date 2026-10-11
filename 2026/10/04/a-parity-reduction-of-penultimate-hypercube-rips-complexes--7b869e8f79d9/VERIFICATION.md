---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

At scale n-2, the forbidden differences are exactly the weight n-1 and n vectors, so the complex is the independence complex of Cay(F_2^n,{j,j+e_i}). For even n, {j+e_i} is a basis and maps j to the all-ones vector, giving FQ_{n+1}; for odd n, {j,j+e_1,...,j+e_{n-1}} is a basis and splits the generating set into one K2 direction plus the FQ_n directions. The actual verifier checks rank, generator images, bijectivity, and every adjacency for n=3,...,8, but the displayed basis argument proves all n.

## originality

PASS

The hypercube Rips literature determines small scales, the top scale n-1, homology lower bounds, and facet families, but the inspected sources do not identify the penultimate forbidden-pair graph with folded cubes by parity.

## value

PASS

The penultimate scale is a natural extremal filtration stage, and identifying the entire complex with familiar graph independence complexes converts a high-scale Rips problem into a standard graph-topology object. This is useful structural information even without a complete homotopy computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
