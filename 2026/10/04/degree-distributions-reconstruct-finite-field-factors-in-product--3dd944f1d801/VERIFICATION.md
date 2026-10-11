---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For each nonzero component \(A_i\), the nondegenerate trace pairing makes \(B_i\mapsto\operatorname{tr}(A_iB_i)\) a nonzero linear functional with exactly \(q^{n_i^2-1}\) zeros; a zero component imposes no constraint. A support of size \(s\) therefore has exactly \(q^{T-s}\) orthogonal tuples before deleting the zero vertex and, precisely when \(X\) is self-orthogonal, deleting \(X\) itself. This gives \(q^{T-s}-1\) or \(q^{T-s}-2\). Both occur because \(E_{12}\) is self-orthogonal and \(E_{11}\) is not for every \(n_i\ge2\). Different support sizes give disjoint adjacent degree pairs, so there are exactly \(2k\) degrees. Summing both multiplicities over support sets of size \(s\) gives \(e_s(q^{n_1^2}-1,\ldots,q^{n_k^2}-1)\). Graph order and minimum degree give \(q^T\) and \(q^{T-k}\), hence \(q^k\); the degree count gives \(k\), and Viète's formulas recover the root multiset \(q^{n_i^2}-1\), hence every \(n_i\).

## originality

PASS

The 2024 survey explicitly poses unequal-size two-factor and arbitrary finite-product trace graphs as Problems 2 and 3, while its reproduced prior theorems treat a single common matrix size. The closest published SCOPE result handles a different semisimple direction—two field factors with one common matrix size—and does not dominate arbitrary \(k\) with unequal \(n_i\) over a common field. The audited support-stratum/elementary-symmetric reconstruction therefore supplies a genuine finite-field solution of the open direct-product problem rather than a special case of a stronger theorem.

## value

PASS

This solves a broad finite-field subcase of an explicit open direct-product problem and gives a rigidity theorem: the graph degree distribution alone reconstructs the common field and every matrix-factor size. The result works for arbitrary numbers of factors and is materially stronger than computing a few local degrees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
