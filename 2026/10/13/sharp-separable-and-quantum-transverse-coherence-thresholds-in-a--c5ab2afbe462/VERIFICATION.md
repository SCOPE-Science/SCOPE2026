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
# Reproduction and limits

Run `python3 verification/verify.py` from the package root (Python 3 standard library only). The checker reconstitutes the six-dimensional computational ground manifold, constructs the compressed bit-flip adjacency exactly as integers, verifies degree two and connectivity, counts two edges per local spin flip, and establishes the rational \(2/3\) expectation for each site of the uniform ground vector. It checks the exact product energy and the twirled marginals over several rational values of \(c\in[0,1/3]\). All assertions are finite and deterministic.

The theorem for every real \(c\in[0,1]\) follows instead from the explicitly stated independent-sign identity, exact equality characterization, spectral radius bound for the six-cycle, and algebraic density-matrix convex constructions. The script is a reproducibility aid, not an infinite-domain certificate. The ground-energy finding does not assert full entanglement-spectrum classification, genuine multipartite entanglement, or uniqueness in historical literature.
