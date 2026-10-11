---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Projective changes normalize the three centers and a standard affine chart puts the unique rank-one point at the origin. In six independent affine coordinates, the four source maximal minors transform so that three are exactly the \(2\times2\) minors of a generic \(3\times2\) matrix and the fourth is their linear combination. A fresh SymPy reconstruction verified all determinant identities and the invertible coordinate substitution. The rank-one cone has dimension four, tangent space all six ambient directions at its vertex, Hilbert series \((1+2t)/(1-t)^4\), and degree/multiplicity three; its projective Segre base is smooth, so the cone is singular only at the vertex.

## originality

PASS

Kileel's three-camera theorem gives the global maximal-minor ideal, and Breiding–Rydell–Shehu–Torres were materially reread in full around Theorem 3.1 and Corollary 3.2: for three noncollinear centers the line multiview variety has a unique singular point characterized by rank one. Those sources do not state the completed local ring, tangent dimension, multiplicity, or analytic identification of that singularity with the affine cone over the Segre \(\mathbb P^2\times\mathbb P^1\). Fresh Resultary and line-multiview-ideal searches found no distinct earlier exact local-normal-form statement.

## value

PASS

The prior literature locates the exceptional three-camera singularity but leaves its local geometry unnamed. Identifying it with a classical Segre determinantal cone immediately supplies tangent, multiplicity and singularity-theoretic information relevant to local conditioning and algebraic geometry. This is a natural local classification rather than a coordinate renaming alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
