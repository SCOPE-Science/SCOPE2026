---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For a balanced connected three-vertex directed multigraph the BEST/Whittle rooted-word formula T(M)=n*tau*product_i(d_i-1)!/product_ij(m_ij)! correctly accounts for indistinguishable parallel arcs. The source handles nonprimitive pure repeated 2- and 3-cycles separately; for all other unique cases a unit-multiplicity edge forces primitivity and F=T/n=1. Loop multiplier binomial(r_i+a_i-1,a_i) and exact bowtie/theta F formulas classify <=4 cross-arcs; five-cross-arc lower bound >=2 and six-cross-arc arborescence lower bound >=3 exclude others. Sum of five disjoint support GFs gives the claimed rational function and leading n² term. Independent brute force grouped all 88,572 ternary words of lengths 1..10 by digram profile and necklace, reproducing coefficients 3,6,11,24,45,64,93,114,139,168; symbolic summation confirmed the rational identity. Enumeration is only corroboration: the support and primitivity arguments are the all-length proof.

## originality

PASS

Classical BEST/Whittle counts Euler circuits and all Markov transition matrices, but the five-support singleton-necklace fiber classification and generating series require an additional ambiguity criterion. The published Resultary binary two-spectrum singleton table is a proper alphabet restriction and cannot imply the labeled ternary classification without new case analysis. The full-result theorem remains best-of-knowledge original, with possible unindexed assembly results.

## value

PASS

Unique reconstruction from cyclic adjacent-pair statistics is a natural question in sequence assembly and Markov-type inversion. An exact labeled ternary all-length five-support classification, GF and quadratic growth degree give nontrivial structural information, not routine reparameterization of BEST or known binary tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
