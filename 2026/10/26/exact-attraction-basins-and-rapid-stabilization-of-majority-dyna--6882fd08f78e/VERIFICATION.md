---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For synchronous open-neighborhood binary majority with ties retained, each outer triangle pair has three types relative to its initial hub: both same, both opposite, mixed. One update makes every pair monochromatic (a mixed pair aligns with the initial hub); every monochromatic pair is thereafter frozen. The hub first reacts to a vs b pair counts and then to b vs m/2, so the second update is fixed. A fixed coloring must have no mixed pairs and at most m/2 opposing pairs. Conditioning on the initial hub gives individual fixed-state basin counts B_m(j)=3^(m−j)+3^j for 2j<m and 3^j at 2j=m; correct handling of a hub tie is essential. Summing basins produces the displayed terminal-blue polynomial, consensus probability (3^m+1)/4^m, and the formula for exactly two rounds; binomial large-number asymptotics yield hub persistence and a 1/2 two-round fraction. A newly implemented synchronous update iterator exhaustively checked all 174760 labelled initial configurations for m=1..8; e.g. m=8 has 326 fixed and 37888 two-round starts. Uniform pair-case proof, not finite extrapolation, covers every integer m>=1.

## originality

PASS

Prior synchronous-majority research supplies model and possible period-2 stabilization on arbitrary graphs and cycle-specific counts. This result classifies every individually labelled attraction basin on the friendship graph family and a sharp two-update stabilization; it is not equivalent to general period bounds or static counts of friendship graph substructures.

## value

PASS

The all-size individual attraction-basin census, terminal population generating function, two-round sharp stabilization and rare-consensus law are natural exact network-dynamics observables not entailed by a generic eventual-stability theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
