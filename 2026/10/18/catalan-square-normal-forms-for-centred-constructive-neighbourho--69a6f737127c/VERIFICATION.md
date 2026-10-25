---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For every intuitionistic formula, forcing is an upset by structural induction; this includes both modalities since each quantifies over all future worlds. For upset U_t=[t,n), a nonempty neighbourhood A is a subset iff min A>=t and intersects iff max A>=t. The source modal clauses reduce exactly to t<=B_i for Box and t<=D_i for Diamond where B_i=min_v>=i max_A min A and D_i=min_v>=i min_A max A. Centredness ensures B_i<=i<=D_i and monotonicity of suffix minima; both are realised by N*(i)={[B_i,D_i]}. All modalities therefore act identically on all upsets, and simultaneous formula induction establishes equivalence at arbitrarily nested depths. Distinct thresholds are separated by a principal upset valuation of Box p or Diamond p at depth one. Each monotone sequence on its respective side of i is enumerated by Catalan_n, independently, giving squared count. Fresh independent direct counts n1..6 =1,4,25,196,1764,17424; package verifier independently checks all 1/9/3375 raw frames for n1..3, not used to prove all n. Checked original Dalmonte–de Groot Definition 2.3 on accessible primary full text: actual Box/Diamond clauses are precisely those used here.

## originality

PASS

The published constructive neighbourhood semantics is explicit prior work (Dalmonte/de Groot Definition 2.3). The claim adds exact observational quotient and singleton-interval normal form on labelled finite chains, which differ substantially from arbitrary frame axiom characterisations and canonical segments. Published SCOPE KI and birelational finite-chain endpoint normal forms count relations under different conditions, not the quotient by modal behaviour of neighbourhood families.

## value

PASS

A canonical full-language semantic normal form drastically compresses potentially many raw neighbourhood families to exactly Catalan-square distinguishable behaviours. This is a natural finite-chain model-theoretic classification whose all-depth faithfulness and exact boundary conditions are useful for semantic enumeration and test model construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
