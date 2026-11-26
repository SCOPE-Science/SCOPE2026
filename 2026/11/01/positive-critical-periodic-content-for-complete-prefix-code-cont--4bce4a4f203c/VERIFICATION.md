---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The ratios are exactly b^(-|c_i|/s), with positive code lengths because the maps are contractions. Kraft equality and strong separation give dimension s. A de Bruijn digit cycle has b^k distinct length-k blocks. Parsing at every residue defines a finite self-map; on any directed cycle its positive total digit length is a multiple of b^k, and individual advances are at most L. A shorter symbol period would induce a digit period divisible by b^k and thus an earlier return to the same parser residue. At distinct parser residues a common symbol prefix encodes at most k-1 digits. Applying its similarity to distinct first-level pieces gives the stated gap. The resulting cardinalities tend to infinity, exactly as required by the critical-content definition, and the normalized gap is at least (b/L)δ^s. The unequal-ratio example has separated invariant interval images, with minimum interval gap 3/16.

## originality

PASS

The supported distinct claim is quantitative critical positivity for every strongly separated system with finite complete-prefix-code ratios. It extends the known homogeneous construction to unequal ratios through a block-boundary cycle argument. The closest distinct Resultary record uses a related coding construction for an unequal two-map pair, not the complete-code family. This is a bounded best-of-knowledge decision, not a priority determination.

## value

PASS

At the critical exponent, dimension equality permits every large-period normalized gap to shrink to zero. This result rules that out quantitatively for a structurally defined, genuinely inhomogeneous class. The bound gives explicit data for constructing large separated orbits, and the parser-cycle argument works for arbitrarily many length levels. Its value is as a constructive partial answer, not as a solution for all uneven ratios.

The dated certificate retains the supplied scientific assessment, sources and limitations.
