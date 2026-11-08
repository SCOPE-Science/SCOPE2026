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

# Reproduction and limits

On standard Hardy \(H^2(\mathbb D)\), compute the Berezin transform at \(z=re^{i\theta}\). Its image circles have center \(c=(1-r^2)/(1-r^{2m+2})\) and radius \(\rho=cr^{m+1}\). Define \(\alpha=c-\rho\). The exact inequality \((m+1)\rho\le1-\alpha\) is equivalent, after multiplication by strictly positive quantities, to \(\sum_{j=0}^{m-1}r^{2j}\ge m r^{m-1}\), which follows strictly from arithmetic–geometric mean for \(0<r<1\), \(m\ge2\). The circular limit as \(r\uparrow1\), together with the value \(1\) at the origin, determines the exact closed convex hull. Tangent lengths, a circular segment formula, and the maximum-of-support-functions identity determine the geometric invariants. The strict radial inequality yields nonattainment at every convex-hull boundary point other than \(1\).

Run `python checks.py` to reproduce the floating-point diagnostic samples in the delivered source. Its finite tests of radial inequality, support domination, tangent orthogonality, and area consistency are not proof for all degrees, nor are they external certification. The complete analytical argument is in `RESULT.md`.
