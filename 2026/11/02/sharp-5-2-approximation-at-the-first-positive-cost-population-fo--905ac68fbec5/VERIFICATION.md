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

For four ordered distinct reports with gaps x,y,z>0, each three-facility triple omits one agent. Its four Product-Gap weights are yz,(x+y)z,x(y+z),xy summing 2(xy+xz+yz), and corresponding nearest-facility costs are x,min(x,y),min(y,z),z. Hence E=[2xyz+z(x+y)min(x,y)+x(y+z)min(y,z)]/[2(xy+xz+yz)]; OPT_3=min(x,y,z) because some facility must serve a pair and selecting all but one member of a minimum gap attains the bound. For m=x, N/x≤5yz+xz<5(xy+xz+yz); m=y gives N/y=4xz+xy+yz<5H; m=z is mirror. Thus E/OPT<5/2 strictly for all distinct profiles. The family (ε,1,1) yields (5+ε)/(2(1+2ε))→5/2, establishing sharp but nonattained supremum. Independently enumerated the four selected triples and verified exact formulas for all 30³=27000 integer gap triples and four rational epsilon values, but the algebraic case split is the infinite proof.

## originality

PASS

The identical Product-Gap / Gap-Product sampling rule and the population-uniform factor six for k=3 are known from Jia 2026 and Chan–Lin–Wang 2026. Both primary papers were read in available full text; their general bounds and tightness examples do not determine the exact four-distinct-agent population optimum 5/2 and its nonattainment. The finite-n result is a motivated sharp boundary rather than a new mechanism. An unindexed fixed-small-population optimization could still cover it.

## value

PASS

Four distinct agents are the first population with positive three-facility social optimum; this makes the exact n=4 factor mathematically canonical rather than an arbitrary numerical slice. The sharp improvement from globally valid 6 to 5/2, and the explicit degenerating near-extremal gap geometry, describe a practically meaningful finite-population limitation/strength of the known randomized strategyproof mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
