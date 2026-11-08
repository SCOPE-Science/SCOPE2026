---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Rebuilt the edge-bubble/nodal basis h=t(1-t), phi=1-t-(5/2)h, psi=t-(5/2)h. Symbolic integration independently yielded Gram entries 1/30,0,0,1/8,1/8,-1/24; inverse of H=((3n-2)I-J)/24 was independently checked at n=3,4,5,6,8,20. Vertex reproducing kernels on incident/nonincident edges are beta*(5nt^2+(2-7n)t+2n-1) and beta*(1-5t(1-t)); their exact signed intervals give displayed absolute-integral formula. Symbolic differentiation matched the claimed strictly positive derivative for all real n>=3; N5≈2.48558, N6≈2.52508, with displayed limit. For the full norm, |bubble coefficient|<=5 and |phi|+|psi|+2h<=1 strictly for 0<t<1, so n>=6 and N_n>5/2 transfer vertex control to every interior point. Sign of vertex kernel attains N_n; P1=1 yields exact positivity defect. Does not claim full-norm formula for n=3,4,5.

## originality

PASS

Known L2 projection stability and interval spline theory supply techniques and broad bounds, not the closed junction-coupled K_n operator norm or extremizers; related published exact simplex affine projection computes a different space/geometry. Best-of-knowledge exact-graph specialization with explicit risk of prior equivalent kernel computation.

## value

PASS

Provides exact stability and positivity-loss constants for a natural globally vertex-coupled finite-element projector on K_n, including sharp location of norming points, critical graph size and first asymptotic correction, not just generic boundedness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
