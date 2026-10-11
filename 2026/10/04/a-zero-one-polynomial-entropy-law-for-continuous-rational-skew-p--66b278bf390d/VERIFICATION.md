---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The rational iterate is exactly \(f_{p/q,\phi}^q(x,y)=(x,y+\Phi_q(x))\), and polynomial entropy is unchanged by positive iterates. For a scalar twist \(G_\psi(u,v)=(u,v+\psi(u))\) with continuous \(\psi\) on compact \(K\), fix a finite small-diameter base cover and a fixed fiber net, then partition the bounded velocity interval into \(O(n)\) bins of width \(O(1/n)\). Points chosen in the same base patch and velocity bin remain uniformly close for all times up to \(n\), yielding an \(O(n)\) spanning set and \(h_{\mathrm{pol}}(G_\psi)\le1\) without any modulus-of-continuity assumption. If \(\psi\) is constant the twist is an isometry. If \(\psi:\mathbb T\to\mathbb R\) is nonconstant, its rotation set contains an interval and Corrêa's 2026 theorem gives the matching lower bound \(h_{\mathrm{pol}}\ge1\).

## originality

PASS

Corrêa computes the rational iterate and rotation set and proves the lower bound when \(\Phi_q\) is nonconstant, but his scalar upper bound assumes Lipschitz regularity. The assigned velocity-range covering removes that hypothesis by a genuinely different organization of spanning points and yields the exact continuous classification. The closest broader 2023 fibered-system result instead states a Hölder-dependent value \(1/\alpha\) for \(\omega(r)=|r|^\alpha\), which conflicts with the new universal scalar-twist upper bound rather than covering it. No implication-equivalent Resultary record was found beyond the assigned result.

## value

PASS

The theorem gives an exact classification for the full continuous rational-base family and removes a regularity condition from the best directly relevant upper bound. The velocity-range argument is independently reusable and also identifies a substantive issue with a published Hölder-dependent scalar example, making this more than a cosmetic sharpening.

The dated certificate retains the supplied scientific assessment, sources and limitations.
