---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Reconstructed the Cayley group G of 2^(d-1) even-weight words, its character-dual quotient by the all-ones vector, adjacency energies ((d-2|a|)^2-d)/2 and complete energy coincidence criterion |a|=|b| or |a|+|b|=d. Godsil spectral-projector Schur squares diagonalize by Fourier characters; count equal energies for a,a+z by disjoint support one-counts t,u: 2t=|z| or 2u=d-|z|. Inclusion-exclusion gives the stated binomial fractions, positive precisely for even character parity and zero precisely for odd; even dimension makes parity invariant under quotient. Antipodal symmetry follows by character parity. For the gap, b_j=1-C(2j,j)/4^j is positive and discretely concave on j>0; its symmetric product maximizes at the center by log concavity. Recomputed Fourier equal-energy count exactly in d=6 and d=8, obtaining ranks 16,64 and gaps 11/16,39/64. Boundary d=4 is explicitly excluded from novelty; finite checks do not establish all even d.

## originality

PASS

Best-of-knowledge original: exact even-halved-cube Cesaro spectrum, positive antipodal sector and minimum nonzero mixing eigenvalue extend beyond existing instantaneous mixing, strong-cospectral nullspace inclusion and general Schur-square machinery. Directly compared graph, quotient normalizations, and implications; primitive distance-regular graph rank problems are not claimed solved. An unindexed association-scheme treatment remains possible.

## value

PASS

The even halved cube is a canonical distance-regular cubelike transport graph. Complete nullspace equality identifies every time-averaged lost mode, and exact gap measures mixing contraction on all surviving modes; these are structural family invariants absent from the cited general framework, not a selected toy sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
