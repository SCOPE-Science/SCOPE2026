---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For any n>=1 and any unrestricted relation R on the labelled n-chain, each row R[j] fails U_a->U_b exactly when nonempty and its minimum is in [a,b), because chain upset inclusion depends only on that minimum. The greatest violating j determines output U_{1+max ell_t}; adjacent-upset arguments recover each ell_t individually. Nonnegative ell_t are distinct as no row has two minima. Conversely singleton rows at ell_t realize every partial injection, so the operation census is sum_k binom(n,k)^2 k!. Every representing R must contain each edge (ell_t,t), hence the canonical singleton-row relation is the unique inclusion-minimum. At forced rows j=ell_t all choices are the w_t=2^(n-1-t) subsets with minimum t; optional rows are either empty or have minimum t with later last occurrence ell_t>j. Independence proves the stated exact product for all realization-fiber sizes. Independent direct semantic enumeration of relations for n<=3 verified counts 2,7,34 and fiber mechanism; inspected exhaustive package checker also implements n=4 but its previous pass was not substituted for proof.

## originality

PASS

The underlying flat Heyting-Lewis clause and successor-row upward closure are known in de Groot–Litak (2026). The new exact cross-row last-occurrence normal form, partial-injection operation quotient, unique least representative and complete fibers do not follow from mere rowwise closure and were not found in inspected primary results. The combinatorial sequence A002720 is already known; novelty is not its value but its semantic realization and exact fibers. Restricted S4-like Bell-number chain census and different birelational maxima are not dominating instances.

## value

PASS

Relational representation is highly nonunique: 2^(n²) relations collapse to far fewer induced connectives on the natural n-chain Heyting algebra. A complete invariant plus canonical minimal relation and each exact equivalence-class cardinality resolves a natural semantic classification, including all n and every unrestricted frame, not a small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
