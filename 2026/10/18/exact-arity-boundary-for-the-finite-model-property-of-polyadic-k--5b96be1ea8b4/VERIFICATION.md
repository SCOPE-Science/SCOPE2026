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

# Verification and reproducibility

Run `python verify.py` using Python 3.10 or later. The program prints `INFINITE_ARITY_FMP_VERIFY_OK` if all assertions pass. It evaluates explicit finite modal formulas and frames at argument arities \(1\) through \(9\), checking disjoint height types and finite truncations of the countable construction.

**Deductive checks (not replaced by computation):** Every finite-arity well-founded formula has a finite subformula set by König's lemma; filtration by this set preserves the modal satisfaction clause in both directions. If \(E^{n+1}\top\) holds then \(E^n\top\) holds, so the exact-height formulas \(\chi_n\) are pairwise incompatible. An infinite-arity root tuple assigning all these formulas to distinct coordinates therefore requires infinitely many worlds. The explicit \(\mathbb N\cup\{r\}\) structure supplies a matching countable model.

**Limits:** The code checks finite instances, not arbitrary signatures, infinite formulas, or infinitely many worlds. The theorem is a self-review, not an independent verification or machine-formalized proof. Historical novelty against all possible prior literature cannot be certified by bounded searches.
