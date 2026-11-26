---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In characteristic dividing 2m the Gauss-map ideal is (x,y), so the actual x-chart is the subring adjoining y/x in the fraction field, with domain presentation x²t=z^(2m), not an unsaturated chart. Adjoining w=z^m/x is finite (w²=t), birational, and normal by the hypersurface S2 property and the Jacobian R1 check, including when the z derivative vanishes identically. The y-chart is symmetric and ww'=1 on the overlap. To check the conductor independently, use x=u^m, z=uv, w=v^m, t=v^(2m). The normalized monoid consists of (a,b)≥0 with a≡b mod m. The raw monoid contains all such pairs with a≥m, and for a<m it contains exactly those with b−a a nonnegative even multiple of m. Thus adding (0,m) to a raw monomial of a<m moves it outside, while the pairs with a≥m are precisely x times the normalized monoid. Linear independence of monomials gives the same criterion for sums. The two conductor quotients are k[z,t]/(z^m) and k[z,w]/(z^m), giving thickness m and including the reduced case m=1. Reducing gives t=w², with degree two, separable and ramified only at zero/infinity in odd characteristic, and radicial and purely inseparable in characteristic two. The normalized chart origins are distinct, are smooth for m=1, and have the stated A_(m−1) equations otherwise.

## originality

PASS

The ordinary Nash ideal and methods for the normalized fan are known. The supported distinction is the unnormalized conductor on the full exceptional curve together with its exact thickness and characteristic-dependent reduced normalization map. No inspected source already gives or subsumes that calculation for the even-exponent family; this does not establish historical priority.

## value

PASS

The exact conductor is a natural scheme invariant for a standard family and measures what is lost when the Nash blowup is normalized. The result identifies a codimension-one defect globally, determines its variable thickness and shows that the reduced normalization map changes separability. The normalized chart computation alone would not explain these distinctions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
