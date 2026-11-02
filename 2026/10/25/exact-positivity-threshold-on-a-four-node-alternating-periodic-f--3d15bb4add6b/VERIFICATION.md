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

Reassembled periodic M and K from edges, then independently computed exact 4×4 symbolic inverse product. Every denominator factor in D_τ=(ab+12τ)(a²+3ab+12τ)(3ab+b²+12τ) is >0. Diagonals and edge classes are >0 for τ>0, while opposite-node entries equal 6τq(τ)/D_τ with q=72τ²+12abτ−ab(a+b)². Since q(0)<0 and q′>0 for τ>=0, a unique positive root determines positivity. τ=0 gives I. Uniform a=b=h recovers h²/6. Exact symbolic matrix algebra verifies all positive real a,b,τ in the domain; spot checks are supplementary.

## originality

PASS

Four-node alternating periodic exact contrast-dependent threshold was not located in searched primary literature. The uniform threshold and general positivity/M-matrix results are previously known and explicitly excluded as novelty. Very relevant 2015 heat-FEM paper remains inaccessible after authorized access reported disconnected VPN; best-of-knowledge PASS retains meaningful priority risk.

## value

PASS

Exact positivity preservation under consistent mass is a natural and practically meaningful mesh-dependent invariant. The simplest truly nonuniform periodic stencil shows a nontrivial contrast-sensitive sharp threshold, quantifying conservatism of the standard max-cell sufficient bound and its singular high-contrast limit. This motivates the precise four-node case rather than an arbitrary tiny computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
