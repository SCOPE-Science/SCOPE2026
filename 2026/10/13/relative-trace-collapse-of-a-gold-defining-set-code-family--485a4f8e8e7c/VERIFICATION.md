---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For m=2e and F/K quadratic, x^(2^e+1)=N(x) in K; trace transitivity reduces both binary trace constraints to Tr_K(c_i N(x))=0 with c_i=a_i+a_i^(2^e), hence D=N^(-1)(C^perp\{0}). Surjective norm has fibers size 2^e+1, giving |D|=(2^(e-r)-1)(2^e+1). If C′=sC then C′^perp=s^(-1) C^perp, choose t with N(t)=s^(-1); multiplication by t bijects defining sets and reparameterizes b in the trace code, proving permutation equivalence. The cyclic norm-one kernel of order 2^e+1 acts freely on D. The three source Theorem 3.5 regimes have rank r=1. Independently checked GF64 trace transitivity for all 64*8 input pairs and all 7 nonzero relative-trace scalar normalizations with norm-one invariance; infinite conclusion follows from algebra.

## originality

PASS

Xiang–Song provide Gold construction and identical two-weight distributions for the three rank-one regimes, but source Theorem 3.5 does not assert code permutation equivalence or norm-one coordinate automorphisms. Same weight enumerator alone never implies permutation equivalence; extra norm/scalar action yields a genuinely stronger classification. No directly covering prior theorem was identified in searches.

## value

PASS

Identifies redundant parameterizations of a published natural binary code family at code-equivalence level, not just equality of enumerators; gives exact orbit decomposition and nontrivial automorphism subgroup, useful for classification, avoiding duplicate constructions, and further code automorphism analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
