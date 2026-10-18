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

The exact support identity is \(h(u)=\sum_{ij\in E}\sqrt{u_i^2+u_j^2}\). The lower and upper bounds follow from \(\sqrt{s}\ge s\) on \([0,1]\) and Cauchy–Schwarz, respectively. Equality cases were reconstructed using connectivity and parity of closed walks. The John bound is certified by coordinate supports and Hadamard's determinant inequality; the Löwner bound by averaging signed contact points and AM–GM on inverse shape eigenvalues. These steps prove the theorem for all connected regular graphs with at least three vertices.

The standalone `verify.py` checker (Python 3, standard library only) was run from its packaged source. It checked 16 connected regular graph examples, 16093 support evaluations, 4054 outer contacts and 601 exact signed covariance entries; all passed. The experiments do not constitute an exhaustive search over graphs, nor do they replace the universal argument. Source comparison was bibliographic and mathematical, not a claim of exhaustive novelty certification. Independent mathematical audit has not been performed.
