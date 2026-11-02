---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The proof derives the exact pair-swap gain identity, the two prefix-by-prefix quadratic optimum conditions, feasibility of their rounded prefix-count sequences, and the separate star inequalities. The stated \(K_{2,5}\) gap is checked by seven possible pairs of type values, with multiplicities among the four zero-type agents.

`python check_biclique.py` (Python 3, standard library) was executed. It passed all exact-integer assertions on 2,674 type/part-size families, 64,548 allocations, and 803,860 cross-swaps, plus both rounded algorithms, the exact seven-agent counterexample, and 48 star sharpness instances. The solver does not rely on floating-point tolerance. The finite checks cannot certify arbitrary sizes or arbitrary real types; those quantifiers are established only by the written proof.

No independent audit or external formal certification has been performed.
