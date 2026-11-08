---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For a 3D orthotope W(u)=Σa_i|u_i|. Haar U has each marginal uniform[-1,1], E W(U)=S/2. Given U, Haar V in U-perpendicular circle satisfies E(|V_j||U)=(2/π)sqrt(1-U_j²). The independent diagonal moment computes E|U_jV_j|=(2/π)∫_0^1 t sqrt(1−t²)dt=2/(3π), while for i≠j circle conditioning gives (4/π²)(1/2)∫_{−1}^1(1−t²)dt=8/(3π²). The mixed width moment follows by bilinearity. Subtract S²/4 to obtain A Q+B(S²−Q). A<0<B, A−B<0; solve root tau=−B/(A−B)=0.348201061933... . At fixed S, Q>=S²/3 uniquely for equal a,b,c and Q<S² for positive lengths with rod approach. The exact cube sign is >0 by π<22/7, while rod covariance tends A S²<0. Continuous positive lengths realize the whole interval. Independent SymPy checked both Haar integrals and tau expression.

## originality

PASS

Best-of-knowledge originality PASS after searches and real statement-level primary comparisons; no source found to imply the exact final claim. Explicit historical/inaccessible-source risks remain: Abas 2026 92-page primary full text not available despite OA and Oxford attempt; angular-pair covariance may be implicit in general cosine-transform results.; Only 3D orthotopes and orthonormal Haar pair, not full joint distribution or all convex bodies.

## value

PASS

Two orthogonal measurement directions in the same randomly rotated frame are a natural coupled stereological observable; the signed dependence changes sharply between cube-like and elongated boxes. The exact one-variable shape statistic and sharp nonattained lower bound are not recoverable from one-direction marginals and provide a complete natural three-dimensional classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
