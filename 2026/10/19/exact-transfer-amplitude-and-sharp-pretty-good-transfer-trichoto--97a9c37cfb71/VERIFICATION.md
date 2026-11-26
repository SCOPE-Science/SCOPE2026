---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The tail bipartition alternates under U=SC, so even overlap vanishes. For m≥1 permutation symmetry leaves the eight grouped arcs invariant. In the vertex-layer swap sector ε=±1, take the four combinations a+εb,c+εe,d+εf,g+εh from the frozen basis. The characteristic polynomial of this sector is (z−εα)(z³+εα)−β²=(z²−1)(z²−εαz+1), using α²+β²=1. Layer swap also interchanges source and target and commutes with the real orthogonal U; hence a(−t)=a(t). For m≥2 this makes the odd-time spectral expression constant plus a cosine, without a sine term. The first and third amplitudes are −1/(m+1) and −(α²+m)/(m+1) by direct arc evolution, determining the two coefficients in the frozen formula. For m=1 the squared walk has eigenvalues ±1, and the first and third amplitudes agree, so every odd overlap is −1/2; for m=0 the walk is −S on the single edge. For m≥2 the rational noninteger 2cos(theta) cannot be the sum of a root of unity and its inverse. Therefore the odd angles are dense and never hit pi exactly; the upper endpoint of the amplitude range is strictly below +1. This proves the pretty-good but not perfect case. The odd-time means of cosine and cosine squared are 0 and 1/2, by the two geometric sums, giving the stated Cesàro average after the even zeros are included. The incoming convention follows from the target's −1 coin eigenvalue. Exact evaluation at m=3,t=31 gives amplitude −4294404829/4294967296 and the frozen fidelity fraction.

## originality

PASS

Credit the all-m analytic amplitude, the m≥2 distinction between pretty-good and exact transfer for every finite time, and the Cesàro law. Rani et al. already give the same walk construction and the m=0,1 behavior; their m=3 near-unity numerical example is antecedent, not part of the distinct contribution except for its exact correction under their explicitly listed outgoing vectors.

## value

PASS

The result settles an exact-versus-approximate transfer question for a motivated scalable network where finite plots can be misleading. It identifies the entire m≥2 regime with arbitrarily high fidelity but no finite perfect time and gives an exact baseline average for that regime. The m=3 fraction alone or the prior low-m cases would not carry the same value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
