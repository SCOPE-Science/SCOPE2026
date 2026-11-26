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

Alternating biderivations are determined by h={x,y}; descent imposes 2xh=2yh=0. The Jacobiator is an alternating triderivation and vanishes on triples of algebra generators (only x,y), including in characteristic two. Every unital automorphism preserves the local maximal ideal and has an invertible linear part G; the square-zero constraints impose nothing further in characteristic two and require diagonal or anti-diagonal G in odd characteristic. In characteristic two, with Delta=det G, the Jacobian is J=Delta+alpha x+beta y, where alpha=af+cd and beta=bf+ce for the stated generator coordinates. Since (alpha x+beta y)^2=0, transport by J^(-1) times phi(h) gives cancellation of the extra xy terms: (va+wd)beta+(vb+we)alpha=Delta(vc+wf). Thus z is invariant even for unit h. At u=0, G↦G/det G is an involution of GL_2, so the nonzero linear parts form one orbit per z. At u≠0 the determinant freely changes the constant and the two quadratic shears prescribe the linear part. For odd characteristic h=zxy and the diagonal and anti-diagonal cases act by +1 and -1. Independent quotient-ring enumerations, not the uploaded script, found 16 brackets/24 automorphisms/6 orbits over F_2 and 256/2880/12 over F_4, with the three predicted sizes per z. Odd F_3 and F_5 runs gave sizes 1,2 and 1,2,2.

## originality

PASS

The supported advance is the characteristic-two orbit classification including both degenerate strata and orbits with a nonzero constant, not the elementary odd-characteristic sign calculation in isolation. The closest equivalent catalogue result is identified explicitly, and the original studies of homology and broader Poisson classification have different assumptions or outputs. The supplied later catalogue entry is not evidence of earlier coverage of this frozen record.

## value

PASS

This fixed algebra is a natural small modular group algebra. Characteristic two removes the descent obstruction and makes the constant and linear strata real possibilities. The invariant that survives every coordinate change and the uniform finite-field orbit sizes distinguish degenerate and symplectic brackets without enumeration, useful for selecting actual representatives for subsequent Poisson-invariant calculations. The odd comparison identifies the scope of the modular change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
