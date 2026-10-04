---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof was checked directly from the definitions of Bowen spanning sets and rotation sets.

For the scalar twist \(G_\psi(u,v)=(u,v+\psi(u))\), fix \(\varepsilon\). A finite base cover of diameter below \(\varepsilon/4\) and a fixed fiber net are independent of the horizon \(n\). Partitioning the bounded real velocity range into intervals of width below \(\varepsilon/(4n)\) produces at most linearly many velocity bins. Points sharing a base-cover element and a velocity bin remain within \(\varepsilon\) for every time \(0\le k\le n\). This proves the required \(O(n)\) spanning bound without any modulus-of-continuity estimate.

For rational base rotation, direct iteration gives \(f_{p/q,\phi}^q=G_{\Phi_q}\). Positive-iterate invariance of polynomial entropy then transfers the scalar result. When \(\Phi_q\) is nonconstant, the rotation set contains the nondegenerate set \(\{p/q\}\times q^{-1}\Phi_q(\mathbb T)\), so the published 2026 rotation-set theorem supplies the matching lower bound. When \(\Phi_q\) is constant, the \(q\)-th iterate is an isometry.

A cancellation check was included: nonconstant \(\phi\) can have constant \(\Phi_q\), so the theorem correctly uses the periodic sum rather than \(\phi\) itself. No computation, finite enumeration, or unproved limiting heuristic is used.

A prior 2023 scalar angle-action proposition asserts a value above \(1\) for certain non-Lipschitz velocities. The explicit spanning cover above applies to the displayed compact scalar model and therefore supplies a direct incompatible upper bound. The present verification does not attempt to assess unrelated results from that paper.
