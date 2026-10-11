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
# Verification

The theorem is proved for every integer \(n\ge1\) by two exact inequalities.

1. With \(\theta=\pi/(4n)\), the regular polygon contains the Euclidean disk of radius \(\cos\theta\) and is contained in the Euclidean unit disk. Therefore \(\|z\|_2\le\|z\|_{X_{4n}}\le\sec\theta\,\|z\|_2\), so the published Banach–Mazur inequality gives \(C_{\mathrm{NJ}}[X_{4n}]\le\sec^2\theta\).
2. For adjacent symmetric vertices \(x=(\cos\theta,\sin\theta)\) and \(y=(\cos\theta,-\sin\theta)\), both the horizontal and vertical rays are facet-normal directions. Hence \(\|x+y\|=2\) and \(\|x-y\|=2\tan\theta\). The \(t=1\) value is therefore \(\sec^2\theta\), proving the reverse inequality.

The bundled script `verify.py` reconstructs the polygon norm from facet normals and checks these identities and the norm sandwich for \(1\le n\le64\). It is a regression check only. Finite numerical checks do not certify the infinite quantifier, and the proof above does not depend on them.

The literature check inspected the defining skew-constant paper and the two closest regular-octagon exact-constant papers. The octagon specialization is prior-covered; the claimed novelty is the uniform regular \(4n\)-gonal theorem. An unindexed equivalent older result remains the principal residual risk.
