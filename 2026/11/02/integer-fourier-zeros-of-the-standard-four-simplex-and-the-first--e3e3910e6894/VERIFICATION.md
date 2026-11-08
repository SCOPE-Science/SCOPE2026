---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For integer nodes a_0=0,a_j=k_j, the Hermite–Genocchi identity gives t^4 FT=[a_0,…,a_4]e^{tz} at t=-2πi. Contour partial fractions and integer-node e^{ta}=1 reduce this to a rational-coefficient polynomial in transcendental t, with its constant coefficient zero since denominator is O(z^-5). If one node uniquely maximizes multiplicity at M≥2, c_{a,M}=∏_{b≠a}(a-b)^-m_b is nonzero; only tied maximal partition of 5 with repeated nodes is (2,2,1), whose t-term coefficient is (a+b-2c)/[(a-b)^2(a-c)(b-c)]. Thus midpoint iff resonance and all-distinct zeros exhaust every partition. For d≤3 only tied case (2,2) produces 2/(a-b)^2≠0. Independent symbolic partial-fraction computations recovered zeros for nodes [0,0,1,2,2] and [0,1,1,-1,-1], and nonzero -t/6 for [0,0,1,2,3]. Normalization uses unnormalized Lebesgue measure on simplex (vol 1/24), negative exponential, and integer lattice only.

## originality

PASS

de Boor's full divided-differences account proves the integration/contour inputs; Diaz–Le–Robins derive general Fourier transforms of polytopes. Neither compared source explicitly supplies the sharp complete integer-frequency zero iff for the 4-simplex or its first-dimension (2,2,1) midpoint resonance. The proof is an explicit algebraic application of known general formulas, but the exhaustive zero classification is not simply a reformulation of those inputs without new multiplicity cancellation analysis. Resultary nearby finite-field/group signal Fourier zeros concern different harmonic objects. Equivalent historical divided-difference identities remain a residual risk.

## value

PASS

The full integer Fourier zero set of a canonical Euclidean simplex is a natural invariant for periodization, harmonic analysis and Poisson summation. The exceptional repeated-vertex-phase midpoint relation and proof of minimal dimension four are substantive structural information; the work does not pretend to generalize to arbitrary simplices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
