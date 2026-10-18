---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Determinant has only diagonal identity and full cycle permutations, giving chi_A(t)=prod_i(t-a_i)-B. Nilpotence iff prod_i(t-a_i)=t^n+B=(t^m+beta)^h with Frobenius bijective and m coprime p. Degree-m factor is separable and splits precisely when m|q-1 and -beta is mth power, giving each of m roots h times, n!/(h!)^m diagonal words for (q-1)/m allowed products B and (q-1)^(n-1) nonzero edge tuples per product. A Krylov triangular pivot along cycle e_n,Ae_n,...,A^(n-1)e_n proves minimal polynomial t^n, so index n. Diagonal conjugation transitive on edge-weight fibers with fixed B; rotations act on balanced root words, period d count F(d), Moebius inversion gives exact O_d and Burnside total. Independent finite-field word/rotation arithmetic recomputed (q,n)=(4,6) 21870 solutions in two 729-size and fourteen 1458-size orbits, along with q4,n3, q5,n4, q7,n3; finite checks corroborate but do not prove all n/q.

## originality

PASS

Best-of-knowledge originality of the final specific quantitative/mathematical statement after semantic published-finding search and primary source comparisons; precise coverage and residual risks are recorded. No literature search is represented as exhaustive or as independent priority certification.

## value

PASS

The same irreducible looped directed-cycle matrix support was previously treated only qualitatively for potential nilpotence. Complete labeled realization and symmetry-orbit multiplicities (including characteristic dividing size) answer the natural next counting/classification problem. Regular nilpotence and nontrivial necklace stabilizers sharpen existence, even though the component Möbius and diagonal similarity facts are classical.

The dated certificate retains the supplied scientific assessment, sources and limitations.
