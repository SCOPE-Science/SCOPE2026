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

The proof was checked from the normalized radial representation of a regular polygon. With \(p=\pi/n\), one period of the squared radial function integrates to \(2\cos^2p\tan p\). For odd \(n\), every central halfplane decomposes into complete periods plus one residual interval of length \(p\), and the residual integral evaluates exactly to the tangent difference in the stated formula.

Differentiating the residual term gives a strictly positive derivative on \((0,p/2)\). The endpoint \(\theta=p/2\) gives half of one radial period and therefore exactly half the polygon area. The endpoint \(\theta=0\) simplifies using \(1-2\tan(p/2)/\tan p=\tan^2(p/2)\), yielding the published maximal-depth value.

Direct polygon-clipping checks at sampled orientations for odd orders from \(3\) through \(31\) agreed with the closed formula to floating-point precision. These finite checks are sanity checks only and are not used to justify the all-orders conclusion.

The scientific limit is explicit: the theorem classifies central directions only. It does not assert a new value for maximal halfspace depth, because that endpoint value is already in Rousseeuw--Ruts.
