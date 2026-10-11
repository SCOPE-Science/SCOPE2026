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

Seigal–Sukarto's published primary decomposition gives four fixed rank-two points plus three quadratic components; at \(9\rho^2-14\rho+9=0\), each quadratic has a double root, so the rank-at-most-two scheme has length \(10\) and support \(7\). For a rank-three symmetric Hessian matrix, singularity of its determinant forces \(T(k,k,v)=0\) for every \(v\), hence the kernel point \(k\) is singular on the cubic. The three source-listed cubic nodes yield unique projective kernel-incidence points, exhausting rank-three singularities. The inspected exact symbolic checker verifies all \(3\times3\) minors at the seven rank-drop points, the three corank-one splitting calculations with nonzero fourth-order coefficient, and nondegenerate quadratic germs at the four remaining rank-drop points and three cubic nodes. This gives exactly \(3A_3+7A_1\).

## originality

PASS

The primary Seigal–Sukarto source identifies the same \(3A_1\) family, the four fixed points and three quadratic pieces, and the exceptional condition \(9\rho^2-14\rho+9=0\) where the ten generic rank-drop points cease to be distinct. It does not determine the resulting curvilinear double structure, the \(A_3\) local types, or the three additional rank-three \(A_1\) singularities of the Hessian quartic. Current Resultary searches for the exact exceptional basket found no covering theorem.

## value

PASS

The exceptional divisor is already singled out in the primary Hessian-rank analysis, so determining what the three pair-collisions become is a motivated local-geometry question. The exact \(7A_1+3A_3\) basket, including the previously hidden rank-three nodes, is a structural classification of that natural degeneration rather than an arbitrary computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
