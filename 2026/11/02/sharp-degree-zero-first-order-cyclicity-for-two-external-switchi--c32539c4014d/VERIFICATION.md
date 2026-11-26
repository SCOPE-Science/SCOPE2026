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

Using angle as time, radial drift to order epsilon is Re(e^(-i theta)c_j); changes of entry/exit angles by O(epsilon) affect the return drift only at O(epsilon^2). On compact neighborhoods off all four grazing radii the switching events are transverse and their times and composed return map are smooth, so the expansion also holds in C1. The exterior constant integrates to zero around a circle, and the imaginary parts cancel on symmetric arcs. The law of cosines gives the two arc half-angle cosines (r^2+3)/(4r) and (r^2+2)/(4r), hence M=2(A f_-+B f_+) with f_± the respective sines on the common crossing interval. The two outer intervals have only 2B f_+, which either has no zeros or is identically zero there. On 1<r<3, with t=r^2, the square of the positive ratio f_-/f_+ is p/q for p=(t-1)(9-t), q=-t^2+12t-4>0. The derivative numerator -2(t^2+5t-34) changes sign at one simple interior root; the endpoint values are zero and the maximum is (47-sqrt(161))/64. Accordingly a positive level below the square-root maximum gives two simple zeros; equality gives a nondegenerate tangency and hence a double zero; above it gives none. No simple zero is added for AB>=0, even when an entire interval has M=0. At A=1, B=-1/2, the level equation factors as -(t-8)(3t-4)/4. At a root the derivative is (p'-q'/4)/(2 sqrt(p)), giving exactly the positive and negative slopes in the record. Dividing the smooth displacement by epsilon and using the simple-root implicit function theorem yields one hyperbolic cycle near each root for small positive epsilon, with the stated stability. This proof checks the three open transverse annuli only, not grazing, higher-order splitting of the double zero, or a global cycle maximum. RESULT.md lines 21–58 and the verification script were inspected; the script's recorded exact identities and sample quadratures were not rerun or used as the proof.

## originality

PASS

Credit only the parameter-uniform sharp first-order zero classification in the degree-zero stratum, including the transition at the double zero and an exact realizable stability pair. The model, disks, Melnikov method and even the two-term displacement up to a positive factor are already available by specialization of the closest paper. Its cycle lower bounds in a higher-degree family do not give the full sharp classification for constants.

## value

PASS

Degree zero is the lowest natural perturbation stratum in a previously studied two-interface geometry, not an arbitrary fitted slice. The result resolves how the two interfaces can create two crossings of the first-order return function although each alone has no simple zero for these perturbations. It gives a complete parameter threshold including degeneracy and an explicit stability pair; it does not claim an all-orders cycle bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
