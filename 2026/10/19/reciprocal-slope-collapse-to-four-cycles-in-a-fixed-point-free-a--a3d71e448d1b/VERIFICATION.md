---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Set L=1 by scaling. Direct substitution gives [-r^2,-r) -> [1-r,0) -> [r,r^2) -> [0,r-1) -> [-r^2,-r), with slopes 1/r,r,1/r,r. The product is one and every composition is an affine bijection of its original bounded interval onto itself, hence the fourth iterate is the identity. Distinct intervals exclude any smaller period. Neutrality is in the return-map sense on the stated core; no ordinary differentiable multiplier at the discontinuity or Lyapunov stability of its endpoint orbit is needed. In the closed core, the omitted points are exactly r^2 -> r-1 -> -r -> 0, so eventual entry is established including all endpoints. The holes (-r,1-r),(r-1,r) map onto (0,r),(-r,0) respectively, each covering precisely the opposite hole among the two. Backward inversion on each allowed branch shrinks length by 1/r, giving two survivor intervals each of length L/r^n for survival at times 0 through n. The alternating pair +/- r^2 L/(r+1) belongs strictly to these intervals and has fourth-core-external period two and second-iterate multiplier r^2; the shrinking diameters exclude every other survivor. No other orbit outside Q can be periodic. Normalizing survivor length by 2r^2L yields P(N>n)=r^(-n-2); differencing gives the stated point masses, and summing gives 1/[r(r-1)]. This is formally a closed-core entry time. The half-open core has the same entry-time law for uniform starts since the union of all iterated preimages of the three omitted points is countable (the map is finite-to-one), though the two times need not agree pointwise. The uploaded exact-rational checker was read, not run; it tests a finite grid and finitely many survivor lengths, not the continuum classification.

## originality

PASS

The open 2023 primary article confirms the same four-branch map including the interval conventions, gives an existing no-fixed-point theorem, and reports period-four windows in a scan with m2 fixed at 5. That scan uses a single starting point and places the period-four window below, not on, the reciprocal point m1=1/5. The closest inspected indexed result in the same family is a sharp prime-three classification and excludes period three on this subcurve; that exclusion gives neither eventual period-four capture nor a transient law. The supported distinction is the global period-four census together with the exact exceptional orbit and geometric capture law on the full reciprocal curve. The oldest paper and related chapter were not inspected in full, so historical priority is not certified.

## value

PASS

The reciprocal curve is motivated by exact cancellation of expansion and compression, not a hand-picked numerical example. The classification replaces isolated trajectories or bifurcation plots with a full description, including the endpoint conventions and the unique exceptional cycle. The transient law quantifies how finite-time observations can hide the eventual exact period-four behavior near r=1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
