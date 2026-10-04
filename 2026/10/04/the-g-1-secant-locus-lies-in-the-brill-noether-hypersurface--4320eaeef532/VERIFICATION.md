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

The scientific proof was checked in the following order.

1. For an effective \(D\) of degree \(g-1\), the source's secant-span description identifies \(\overline D\) with the projectivized kernel of \(H^1(L^{-1})\to H^1(L^{-1}(D))\).
2. Functoriality of extensions under \(L(-D)\hookrightarrow L\) turns kernel membership into a split pullback and hence a lift \(L(-D)\to E\).
3. Riemann--Roch at \(\deg L(-D)=g\) gives \(h^0(L(-D))\ge1\).
4. The lifted section has nonzero image in \(L\), while the canonical \(\mathcal O_X\)-section has zero image; therefore they are independent and \(h^0(E)\ge2\).
5. The exact cohomology dimensions are \(h^1(L^{-1})=3g-2\) and \(h^1(L^{-1}(D))=2g-1\), so the projective kernel is \(\mathbf P^{g-2}\).
6. At \(g=5\), this is \(\mathbf P^3\subset\mathcal H\subset\mathbf P^{12}\).

`artifacts/verify_dimensions.py` replays the numerical Riemann--Roch identities for \(2\le g\le100\) and prints `VERIFY_OK`. This script is only a numerical consistency check; the Ext functoriality and section-independence argument above is the proof.
