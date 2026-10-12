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

# Verification notes

The proof is mathematical rather than experimental: the bidegree genus inequality establishes factorization of every candidate degree at most four, the nodal normalization ring gives the precise descent criterion, and quadratic-pencil algebra classifies all descended degree-four covers. The group identification uses evaluation in the quadratic residue field; the generalized-Jacobian torus follows from the normalization exact sequence.

`verify.py` is a standalone Python 3 program using only the standard library. Execute `python3 verify.py` in the directory containing this file. Successful execution prints `VERIFY_OK`. It tests finite fields \(\mathbb F_q\) for \(q\in\{3,5,7,11,13,17\}\), projective quadratic-extension unit classes, closure under multiplication and the displayed genus-four seed. Every assertion checks exact integers modulo prime characteristics; it does **not** prove the result for all odd prime powers or all source curves.

The source curve is required to be the one-node model of [1, Theorem 3.5], with smooth hyperelliptic normalization and \(\alpha\notin\mathbb F_q\) satisfying \(f(\alpha)\ne0\). The source's local ring was checked in its proof. The older Rosa–Stöhr (2002) full text was inaccessible, so implicit prior coverage remains a bibliographic risk. An independent scientific audit has not been performed.
