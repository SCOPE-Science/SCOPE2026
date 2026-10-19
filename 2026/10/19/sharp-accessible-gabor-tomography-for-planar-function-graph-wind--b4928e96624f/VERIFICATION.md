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

# Reproducible scientific checks

Use `python3 check_planar.py` and `python3 check_algebra.py`; both programs need only the Python 3 standard library. It enumerates all ambiguity coordinates on the quadratic planar graph over four fields and verifies both the uniform graph-indicator spectrum and the one-doubled-weight minimum. The \(9\)-element extension field is built explicitly as \(\mathbb F_3[t]/(t^2+1)\). It separately confirms that a nonplanar cubic graph over \(\mathbb F_5\) has additional missing horizontal Weyl rows.

The observed uniform multiplicities, ordered as eigenvalue \(q^2\), \(q\), \(1\), \(0\), were: for \(q=3\), \((1,6,54,20)\); for \(q=5\), \((1,20,500,104)\); for \(q=7\), \((1,42,2058,300)\); for \(q=9\), \((1,72,5832,656)\). The one-doubled graph window had accessible ambiguity minimum \(1/(q+1)\) in every test, with precisely \((q-1)q^2\) forced zero coordinates. Total direct ambiguity evaluations exceed \(19,000\). A separately constructed full matrix-projector Gram computation in dimension nine additionally confirmed the frame eigenvalue normalization \(q^2|A|^2\).

The standalone symbolic checker certifies in the polynomial ring \(\mathbb Z[q,z]\) the cubic deficit factorization and the quadratic-remainder identity, by exact integer coefficient arithmetic. The reported finite tests and algebra checks are reproducibility aids; the unrestricted proof is in `RESULT.md`. No exhaustive classification of all possible mass tuples was attempted or needed. No independent mathematical audit has been performed.
