---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed the structural proof from the assigned RESULT.md. Calderón–Walton H(Q)~k Qhat identifies the quiver whose vertices are ordered pairs and arrows synchronous pairs. Acyclicity of Q implies Qhat acyclic. Its path algebra has Dynkin finite, extended Dynkin tame, wild otherwise (Gabriel/Donovan-Freislich/Nazarova). Every vertex v contributes diagonal degree (deg^- v)^2+(deg^+ v)^2: parallel arrows yield a >=4-arrow Kronecker subquiver; branching >=3 or mixed (2,1) yields star >4 leaves, spectral radius >2. Exactly (2,0)/(0,2) creates an affine D4~ four-star; any further original connected arrow adds a diagonal edge, strictly enlarging a connected affine graph and forcing spectral radius >2. Thus nonwild components are directed paths or isolated 3-vertex forks. Ordered fork squares: same orientation one D4~, opposite orientation one A3~, remainder isolated; mixed fork/path yield A paths. For directed paths each indecomposable is an interval, counted by synchronous length-l path pairs, matching dim. Independently checked finite DAG/Cartan eigenvalues for 572 cases and explicit fork products, not an infinite substitute.

## originality

PASS

The face-algebra square isomorphism, small fork product examples and Dynkin/extended Dynkin classification are prior. Originality of completed result is the global input-quiver criterion including wild obstructions, affine factor multiplicity for any disconnected source, and finite-type count equality. Existing primary Table 1 covers a single fork and thus that example alone is NOT new.

## value

PASS

Finite/tame/wild representation type is a canonical central invariant of finite-dimensional face algebras; the result supplies an exact original-quiver recognition criterion, multiplicities of affine factors and a natural finite-type indecomposable-count invariant, all useful without recomputing a potentially large squared quiver.

The dated certificate retains the supplied scientific assessment, sources and limitations.
