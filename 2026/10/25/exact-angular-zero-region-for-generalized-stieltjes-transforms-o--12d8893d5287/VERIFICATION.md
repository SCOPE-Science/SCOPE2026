---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For nonreal z, arg(z+t) is continuous strictly monotone with derivative -Im(z)/|z+t|^2; its range has length Theta<pi. If lambda*Theta<pi, a rotation of every integrand lies in a common strict open right half-plane, so a nonzero positive integral cannot vanish. If lambda*Theta>=pi, choose two support locations separated in argument by pi/lambda and masses |z+t_i|^lambda; their integrands are antipodal unit vectors and cancel. Real admissible z>-a gives positive transform. For lambda=2, the right-angle criterion simplifies exactly to |z+(a+b)/2|^2 <= (b-a)^2/4. Independent two-atom complex arithmetic yielded residual 3.5e-15 at z=-2.7+0.35i; the constructive proof is exact.

## originality

PASS

Best-of-knowledge comparison of the exact mathematical statement and hypotheses with accessible primary text and Resultary; no materially inspected prior statement logically supplies the complete final claim. Inaccessible relevant texts are identified as residual risks, not automatically classified noncovering.

## value

PASS

The first sharp order-uniform, support-sensitive geometric answer to where positive generalized Stieltjes transforms may vanish, with an attainable region and a two-point extremal construction. Despite its elementary convex-arc proof, this is a self-contained natural complex-zero classification for a broad transform family, not an arbitrary isolated integral or routine sign check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
