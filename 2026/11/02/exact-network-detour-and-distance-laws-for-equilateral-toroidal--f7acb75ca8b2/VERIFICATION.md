---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For distinct edges each shortest route enters and leaves via one of four endpoints; same-edge direct travel is included. Independently checked exceptional geometry: two aligned horizontal edges in different rows (or vertical analogue) force D=k+min(S+T,2-S-T) versus ambient k+|S-T|. The excess is 2min(min(S,T),1-max(S,T)), whose survival is (1-z)^2. Orientation and edge counts give exception mass (m+n-2)/(4mn). All other edge pairs have D=L. Conditioning on orientations yields two independent circle-distance uniforms in mixed case; same-direction baseline and exceptional replacements supply the full CDF, including the coefficients 1/(4m),1/(4n),1/(4mn). Cyclic vertex-distance mean correction -ε_k/(4k) establishes mean and elementary parity inequality yields full sign classification. Independently checked 10,000 exact rational endpoint-route comparisons. Finite samples do not prove the exhaustive route lemma.

## originality

PASS

Best-of-knowledge comparison of mathematical claims, implications, aliases and relevant primary texts; general tools are credited and historical priority is qualified. This is a continuous metric graph sampled by edge length, not the vertex-sampled toroidal distance matrix or the Euclidean flat-torus distance. Cheng–Qiu–Shen 2011 has vertex distances and their mean, not the edge-pair law or a Betalike routing excess.

## value

PASS

The full distance law of a periodic grid network under arclength sampling is a natural geometric-probability invariant for periodic streets; the universal Beta detour conditional law and a sharp comparison to area-sampled ambient tori quantify routing geometry versus sampling bias across an infinite family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
