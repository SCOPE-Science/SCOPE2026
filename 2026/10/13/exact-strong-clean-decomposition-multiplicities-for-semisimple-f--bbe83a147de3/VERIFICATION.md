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

PASS: For a semisimple F_q[t]-module V=⊕_f K_f^{m_f}, every E commuting with A is a tuple of endomorphisms E_f in M_{m_f}(K_f). The unit A-E requires E_f=I on the f=t summand and E_f=0 on f=t−1; for other f, A and A−I are invertible, so any idempotent is allowed. Image/kernel complementary decompositions of K_f^{m_f} give exactly [m_f choose k]_{q^deg f}(q^deg f)^{k(m_f−k)} idempotents of rank k. Multiplication gives the claimed formula. Each nonspecial factor contributes at least 2, yielding unique strong-clean decomposition iff A²=A; regular semisimple case gives 2^s. Independent finite matrix enumeration for scalar 2I in M2(F3), M2(F5), M2(F7) returned 14,32,58; no finite enumeration used as proof of all n/q.

## originality

PASS

PASS (best of knowledge): The inspected Borooah–Diesl–Dorsey and Chen–Yang–Zhou sources provide invariant-submodule/existence criteria for strong cleanness, but no exact fixed-matrix multiplicity formula. The quantitative extension-field idempotent product and exact uniqueness restriction are the final claim. This deduction uses classical semisimple centralizer and idempotent counts, so equivalent older centralizer-enumeration formulas could imply it and remain a nontrivial priority risk; it is not asserted as a new structural decomposition theorem.

## value

PASS

PASS: Counting all decompositions of a fixed matrix is a natural quantitative refinement of strong-cleanness, and the formula uniformly handles arbitrary semisimple multiplicities and nonsplit primary components and gives a sharp unique-decomposition criterion. This all-strata invariant can be used to distinguish multiplicity profiles even when existence is automatic. The argument is short and relies on classical counting; its modest breadth is explicitly recognized.

The dated certificate retains the supplied scientific assessment, sources and limitations.
