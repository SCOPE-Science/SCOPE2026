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

# Computational verification

Run `python3 verify.py` with Python 3 and only the standard library. Completed output:

`VERIFY_OK 1836 exact assertions; 82174 dual function tables; 32906 candidate subalgebras; 81210 direct algebra function tables; 35 dual-induced homomorphisms; m,n<=5 dual and m<=4 subalgebras`

The verifier builds the Heyting implication table independently from residuation on the finite ordered algebra. For every \(1\leq m,n\leq5\), it enumerates all functions between the dual rooted stars, screens for the cone-image p-morphism condition, checks the exact Stirling hom-set formula, and checks dual image ranks. For every \(1\leq m\leq4\), it screens all possible subsets containing the Heyting constants, tests closure under meet, join and implication, and compares the resulting sets and rank counts with independently enumerated set-partition normal forms. It also enumerates direct algebraic homomorphism tables for eight small ordered pairs and tests all defining operations; for \(m,n\leq3\) it independently reconstructs inverse-image homomorphisms from the duals. For the five self-pairs it independently tests idempotence and permutation counts.

These bounded checks cannot prove the all-parameter theorem or its bibliographic originality; the mathematical argument is in RESULT.md. The program performs no network access and needs no external data.
