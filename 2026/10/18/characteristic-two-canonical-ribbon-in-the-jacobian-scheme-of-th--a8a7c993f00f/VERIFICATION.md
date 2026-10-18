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

The proof computes the five partial derivatives over the integers, then works in characteristic two to obtain an exact three-quadric Jacobian ideal. Affine chart elimination shows that the singular scheme is locally \(k[t,u]/(u^2)\); the chart transition determines the conormal \(\mathcal O_{\mathbb P^1}(-6)\), and complete-intersection adjunction supplies the degree, arithmetic genus, and canonical embedding. In odd characteristic (including three), the intrinsic ideal includes the cubic equation and its two principal charts are reduced parameter lines.

`python verify.py` uses SymPy and checks derivative identities, reduction modulo two, nilpotent chart substitutions, the gluing transition, published balanced-ribbon quadrics, and the complete-intersection Hilbert polynomial for degrees \(2\) through \(10\). It also exhaustively enumerates projective prime-field points for \(p\in\{2,3,5,7\}\); it reports `VERIFY_OK` if all checks pass.

The enumeration does not establish any infinite statement or nonreduced scheme structure. The symbolic chart analysis is the proof. Existing work independently supplies the ribbon's abstract equations; the assessed contribution is specifically their occurrence as the intrinsic singular scheme of the chordal cubic, with a nonflat modular jump. No independent audit has been carried out.
