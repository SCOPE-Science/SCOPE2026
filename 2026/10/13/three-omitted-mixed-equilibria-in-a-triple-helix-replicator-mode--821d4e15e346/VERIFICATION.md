---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The claim concerns exactly the three-affine-factor system Eq. (3.13), not a generic three-population game. Reconstructed all 3^3 boundary/interior status assignments over [0,1]^3 for the published calibration: precisely the eight corners and (34/37,40/41,0), (6/37,8/41,1), (517/1248,71/156,3329/4992) survive. Exact independent symbolic computation verifies det J*=-BE(A+D)x(1-x)y(1-y)z(1-z)<0 and tr J*=0 under B,E,A+D>0, proving one negative and two positive-real-part eigenvalues at any admissible fully mixed point. Face xy blocks have negative determinant, and exact transverse eigenvalues -46606/1517 and -23282/1517 establish one unstable direction each. This is exhaustive only at the stated baseline; general theorem covers interior point uniqueness and index, not every degenerate boundary case.

## originality

PASS

The 2026 primary Liu–Meng–Ji–Wang model explicitly lists eight corners as all its stationary points despite its own affine equations having three further baseline equilibria. Related Su et al. government-participation replicator equilibria are derived for a different payoff system, not this census. General tr/det saddle facts do not by themselves imply these source-specific omissions or rational coordinates. Published-record search found neighboring corrections but no equivalent computation; absolute novelty is not certified.

## value

PASS

A source-specific mathematical correction changes the exact equilibrium census from eight to eleven and classifies the omitted local saddle indices. In tripartite evolutionary-game interpretation the omitted saddles and their stable manifolds are substantive local phase-portrait structure, even without claiming global basins. This is a motivated error correction of a primary research model, not an arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
