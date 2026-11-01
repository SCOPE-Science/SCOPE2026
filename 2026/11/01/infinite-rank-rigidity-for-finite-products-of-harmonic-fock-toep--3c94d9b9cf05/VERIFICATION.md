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

# Mathematical verification record

The kernel identity \((Pe^{w\cdot})(z)=e^{zw}V(z,w)\) with jointly exponential-type \(V\) was checked against the proof of Theorem 1.2 in Liu–Qin–Huang, especially recursion (4.2), identity (4.3), and the induction proving \(V\ne0\) when every symbol is nonzero.

The new Borel separation lemma was reconstructed independently from coefficient bounds: the Borel series converges absolutely outside a uniform radius, multiplication by \(e^{aw}\) translates its variable, the complement of disjoint disks is connected, and each shifted transform extends holomorphically across its disk if a linear relation holds. Decay at infinity then enforces the zero function via Liouville. This contradicts the nonzero evaluation rows of the kernel factor.

The proof establishes linear independence for arbitrarily many evaluation rows and converts this to infinite algebraic rank without invoking boundedness, numerical experiments, or finite-only enumeration.

No external independent audit or formal proof-assistant certification was performed. Publication novelty remains subject to further literature and expert checks.
