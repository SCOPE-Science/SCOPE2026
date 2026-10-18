---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Normalized Bloch and rotation axes have dot product zero and cross n × r=(-3,2,-1)/sqrt(14). Consequently J=(2,-1)^T/sqrt(14), v=(0,-1)^T, J^T J=5/14, J^T v=1/sqrt(14), c^T J=1/sqrt(14), and s_E=1/(5+14 lambda)>0. Independently reconstructed these exact identities symbolically; H^2=2I, E^2=3/2 gives -2 Var(H)=-1. For any one-term H=cO, s_E=||j||^2/(||j||^2+lambda)*v_H<=0 for lambda>0; zero-row and lambda=0 least-squares degeneracies also cannot ascend. The source checker was inspected and is ancillary. Claim is a local directional, not an accepted step, result.

## originality

PASS

Best-of-knowledge PASS: the motivating VIME paper expressly warns that the projected velocity may violate an energy descent test and uses Armijo safeguards, even reporting numerical increases if unchecked. That qualitative statement and algorithm do not state an exact noise-free one-qubit direction uniformly positive for all lambda nor the minimal Hamiltonian term count. Earlier OVQITE methods and weak Gauss–Newton obstructions have different quantifiers.

## value

PASS

The exact obstruction isolates projected-vector geometry from sampling, truncation and solver error, and proves that two nonconstant Hamiltonian terms are the smallest possible setting. This mathematically explains why a descent safeguard can be necessary even with exact observables; no typicality or source algorithm failure is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
