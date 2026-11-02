---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The integer s→∞ limit of the product of two scalar factors gives (1-U)(1-V)≤UV a.s. on the countable intersection of all integer-step events. With U,V∈(0,1) uniform, U+V≥1 and expectation exactly 1 force U+V=1 a.s.; no independence is assumed. Direct multiplication at V=1-U yields P_z=(1+z+c z²)/(1-z+c z²), c=U(1-U). For B=hA dissipative, D=I-B+cB² and N=I+B+cB² satisfy ||Dy||²-||Ny||²=-4[Re<y,By>+c Re<By,B(By)>]≥0, so N D^{-1} is nonexpansive even when B is nonnormal; D is invertible since its two dissipative resolvents are. For s>0, integration of 4s/D_s-4s²/D_s² with D_s=1+s+s²u(1-u) gives δ(s)=8(s²+2s+4)log(1+s)/(s+2)^3-8s²/((s+2)²(s+1)), with sδ(s)-8log(s)→-8. An independently implemented SymPy derivation checked the transfer and gap algebra; this is only supporting computation, while the all-couplings/all-matrices quantifiers follow analytically.

## originality

PASS

The novel part is uniqueness among all couplings with uniform marginals and the exact logarithmic damping law, not the single-step randomized method or adjoint-composition order cancellation. The primary Bochacik–Przybyłowicz article imposes independently drawn stages and analyzes a different sampling rule. The reviewed Blanes–Casas–Murua composition discussion explains deterministic adjoints and order cancellation but does not imply probabilistic coupling rigidity, its full copula quantifier or this mean-square stiff law. No indexed equivalent was identified; historical literature on correlated stages remains a risk.

## value

PASS

A two-step random method can share the same one-step stage marginals while changing samplewise A-stability radically. Characterizing the only permissible coupling, proving matrix stability even for nonnormal dissipative operators, and determining a sharp logarithmically weak stiff-damping rate are natural structural integrator questions; not merely a second-order expansion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
