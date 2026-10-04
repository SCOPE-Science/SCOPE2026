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

The packaged verifier `verify.py` is deterministic and uses only the Python standard library. It exhaustively enumerates all \(6\times6\) binary incidence matrices with every row and column sum equal to three, quotients connected instances under all bipartition-preserving isomorphisms and exchange of the two sides, and checks minimum dominating-matching size exactly.

Recorded replay result: `ALL CHECKS PASSED` with \(550\) semilabeled matrices and exactly five connected isomorphism classes. The paired-domination values are \(4,4,4,4,6\). The unique value-six class is exactly the canonical form of the LCF graph \([5,-5]^6\), the Franklin graph.

The proof is finite; no conclusion about order greater than twelve is inferred from the enumeration. The external five-class census is corroborative rather than required for correctness.
