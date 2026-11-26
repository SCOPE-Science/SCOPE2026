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

A prescribed two-symbol affine return has a unique fixed point since lambda^2 is not one; repeating a single branch cannot yield primitive period two. The two mixed itineraries give u=lambda/(1+lambda)=1/2+ih and -u, and their strict signs verify admissibility. At u+delta the entire positive-starting alternating itinerary is equivalent to h+Im((-lambda)^k delta)>0 at every k, by induction using the affine branches. These constraints repeat after q steps. Their intersection is open, convex and consists of points whose full orbits avoid the real axis; since the intersection is open, no point in it is in the closure of its preimages. On a regular component the sign of each iterate is locally constant, so no component containing this cell can extend beyond this complete itinerary class. The normals are the cyclic orbit of one normal under -lambda (up to inversion); its order is q/gcd(q,p+q/2). This gcd is 1 when 4 divides q and 2 when q=2 mod 4, because gcd(p,q/2)=1 and p is odd. All distinct normals are equally spaced, each at distance h, giving the stated regular polygons and areas. The two-step return is rotation by lambda^2 about the center; noncenters have least return period q/2, and a return under F must be even because F exchanges the cells. Thus the least period is q off the centers, and q=10 indeed gives pentagons.

## originality

PASS

Credit the general regular-set polygon and period framework, and the known square and triangle examples. The distinct supported increment is the exact even-denominator law for the period-two components outside the coprime-period regularity theorem, including the normal coincidence for q=2 mod 4 and the resulting metric profile. A distinct, broader catalogue record explicitly covers the same law and is listed later; this is genuine statement-level overlap, not evidence that the assigned finding was already known before its listed record.

## value

PASS

The unique primitive two-cycle is a natural distinguished part of the established map. The calculation resolves its maximal cells precisely in a noncoprime regime missed by the general regularity theorem, with infinite families attaining the general side bound or having only half as many sides. This makes the pentagons at q=10 an exact geometric example of the resonance, not a numerical pattern or a special-angle restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
