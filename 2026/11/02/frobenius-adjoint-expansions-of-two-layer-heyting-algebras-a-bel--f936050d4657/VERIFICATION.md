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

# Reproduction notes

Run `python3 checker.py` in a Python 3 environment using only the standard library. The program checks the upset-domain operations and Heyting implication directly, enumerates join/meet-closed candidate fixed-point images, constructs floor/ceiling operators, and tests every pair of inputs against all five defining conditions. It also independently enumerates every deflationary meet-homomorphic candidate \(f\), derives a possible adjoint \(g\), and tests the original conditions without relying on the image theorem. Expected terminal marker: `ALL_CHECKS_OK`.

The common-image enumeration tests \((a,b)=(1,1),(1,2),(2,1),(1,3),(3,1),(2,2),(2,3),(3,2),(3,3)\) with results \(2,3,3,6,6,5,11,11,26\). Direct-unary enumeration tests \((1,1),(1,2),(2,1),(2,2),(2,3)\) with valid counts \(2,3,3,5,11\). These are exact finite checks, not an exhaustive test of all positive \(a,b\); the mathematical proof in `RESULT.md` establishes the general statement.

The derived expression \(1+B_aB_b\) counts labelled carrier expansions; \(1+p(a)p(b)\) counts isomorphism classes under internal poset automorphisms. No result is asserted for other Heyting reducts. Independent audit status is unperformed.
