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

All formulas concern the two symmetric endpoint maps on [0,1], 0<r<1/2, and the uniform target. Stationarity gives E[X]=p; conditioning on the digit places X on the appropriate side of 1/2 and gives E|X-1/2|=1/2-2rp(1-p), hence the dual quadratic bound including p=0 and p=1. Independently, the binary digit series for the fair quantile is increasing, and each Cantor coefficient divided by its binary coefficient is at most 2(1-r). On the lower half, the first digit is zero, and the sharper bound is Q(u)<=4r(1-r)u<=u. Reflection handles the other half. This coupling makes each displacement outward, realizing the dual difference and proving unique IID optimality. For the supported benchmark, every optimal coupling is concentrated on nearest points by the pointwise cost inequality. Ties are only countably many gap midpoints; existence of a minimizing coupling and uniqueness of the projection almost everywhere imply a unique minimizing law. The gaps of length g*r^k and multiplicity 2^k yield triangular costs and geometric sum g^2/[4(1-2r^2)]. The set itself has zero uniform mass and 1 has no projected mass, whereas r receives g/2. Since r can only be reached from 1 under these maps, no state-dependent stationary kernel on [0,1] can carry the optimizing law. Division gives the stated ratio, which diverges despite both costs vanishing. Independent finite quantile integrations with exact rational atoms checked four ratios including 127/256, with explicit coupling error r^10/2.

## originality

PASS

The prior work establishes inverse IID shaping as a general problem, and exact transport between stationary laws and other Cantor transport results. Nearest-point projection and monotone transport are standard. The distinct supported claim is the symmetric uniform-target IID optimum with a quantitative bias inequality, contrasted with the exact, nonstationary projection benchmark. The inspected passages do not give this combination or imply it by substitution.

## value

PASS

This is a benchmark for inverse invariant-measure shaping with fixed maps: the quadratic penalty distinguishes the optimizer quantitatively, while the projection comparison quantifies how much one would underestimate optimal IID cost by treating support as the only constraint. The policy-independent impossibility of attaining the unrestricted benchmark identifies a dynamical obstruction, and the divergent relative error shows it persists in a meaningful scale even when absolute costs vanish.

The dated certificate retains the supplied scientific assessment, sources and limitations.
