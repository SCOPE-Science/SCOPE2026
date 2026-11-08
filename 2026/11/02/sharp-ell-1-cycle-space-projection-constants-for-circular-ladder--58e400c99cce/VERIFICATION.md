---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For unweighted real ℓ1 edge space of C_n □ K_2, n>=10, the n square circulations s_i and a global rim cycle t span the full n+1-dimensional kernel of the incidence map. Averaging an arbitrary projection under dihedral rotation/reflection and layer swap preserves the norm and projection property, allowing arrays b_i=-b_{-i-1}, 2a_i=1_{i=0}+b_i-b_{i-1}. Expanding all edge columns gives H=2Σ max(|a_i|,1/(2n))+Σ|a_i-a_{i-1}| and V=2Σ|b_i|+Σ|b_i-b_{i-1}|. The ten non-overlapping indices exist for n>=10 and produce 4H+V>=12-16/n, yielding the universal lower bound 12/5-16/(5n). Explicit b with u=(3n-9)/(10n), v=1/n attains H=V and fixes s_i,t. Independent exact-Fraction full 3n×3n projection checks for n=10,11,12,30 confirmed P²=P, divergence zero, and every column norm—256 individual matrix assertions.

## originality

PASS

Averaging projections and studying graph cycle subspaces are established. The explicit unrestricted prism-family minimum and its 10-index dual lower certificate were not supplied by the inspected general results on diamond/Laakso graphs or equal-factor cyclic tori; a distinct family-specific exact optimization is assessed original, with graph-terminology priority caveat.

## value

PASS

The minimum norm of a projection onto a natural graph circulation space is an intrinsic finite-dimensional Banach/graph quantity. The explicit closed expression for an infinite prism family, exact dual lower certificate, and limit 12/5 provide structural information not inferred from generic symmetry averaging.

The dated certificate retains the supplied scientific assessment, sources and limitations.
