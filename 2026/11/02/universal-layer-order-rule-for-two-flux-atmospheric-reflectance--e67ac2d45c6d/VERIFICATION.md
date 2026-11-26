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

The adding map f_i(x)=r_i+t_i^2 x/(1-r_i x) is strictly increasing on [0,1], with f_i(1)<=1 and equality only at r_i+t_i=1. Write its projective matrix as I+r_i[[-w_i,1],[-1,0]]. The commutator of two such matrices is h[[0,1],[1,0]], h=r_i r_j(w_j-w_i). If the reverse product acting on (x,1) gives (c,d), the difference between the two stack albedos is h(d-cx)/(d(d+hx)). Both denominators are positive by factoring them as the denominators of the two physical adding steps. For x<1 the factor 1-x(c/d) is positive. For x=1 it can vanish only if both sheets are lossless: a lossy outer sheet has f_i(1)<1, and a lossy inner sheet gives the strictly increasing outer sheet an argument below 1. Two lossless sheets have w_i=w_j=2, so unequal-index swaps remain strict even at white backing. Equal indices commute. The prefix is strictly increasing, so any adjacent inversion can be strictly improved, while equal-index swaps preserve the value; reversing the sign argument gives the minimum. Passivity gives w>=2 and the fixed-point equation p^2-wp+1=0 gives the indicated decreasing index p. Iterating the same sheet from a black backing converges to its unique fixed point in [0,1]. For Kubelka–Munk with a=1+K/S, b^2=a^2-1, s=sinh(theta), c=cosh(theta), and D=as+bc, the claimed reduction follows from D^2+s^2-b^2=2asD. The positive-thickness lossless limit gives r+t=1 and w=2. As an independent illustrative check, exact fraction composition of all six example orders yields BAC=204/437 and CAB=159/428 as the unique maximum and minimum. The frozen script was inspected, not run; universality follows from the swap proof.

## originality

PASS

The supported distinct claim is the arbitrary-stack, every-backing reflectance rearrangement with strict unequal-index swaps and complete equality cases, not the adding law or the optical index. No inspected stronger statement implies it: the related matrix-ordering theorem requires simultaneous triangularizability and optimizes a linear scalar objective, not these projective ratios. The strongest available optical comparison describes a composition framework; the unresolved full-text historical comparisons are stated limits, not evidence of noncoverage.

## value

PASS

A fixed collection of physical layers and an uncertain substrate give a natural ordering problem. A single scalar sort resolves both global extrema at every albedo, handles all ties, and reveals that raw sheet reflectance can choose the wrong order and that thickness drops out of the homogeneous-layer criterion. These properties are useful rather than a mere alternative matrix representation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
