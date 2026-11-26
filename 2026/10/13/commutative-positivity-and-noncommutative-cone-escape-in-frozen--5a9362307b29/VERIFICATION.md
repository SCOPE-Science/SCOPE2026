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

On the full real symmetric space, the linearization is I−L_Z⁻¹L_X. L_Z⁻¹L_X is similar to the self-adjoint L_Z⁻¹ᐟ² L_X L_Z⁻¹ᐟ², which lies strictly between 0 and 2I by the quadratic forms for X and 2Z−X. Thus the linearization has operator norm below one in the L_Z inner product, yielding local linear attraction by continuity of the derivative. Commuting data preserve the simultaneous diagonal subspace. In each scalar mode u=(y+x)/(2(z+x)) obeys g(u)=ru(1−u), r=1+x/z in (1,3), u₀=1/2 and u*=(r−1)/r. For r≤2, [u*,1/2] is invariant and the sequence decreases to u*. For 2<r<3 the two invariant alternating intervals are [1/2,u*] and [u*,r/4], using g(r/4)−1/2=(r−2)(−r²+2r+4)/16≥0. The second-iterate displacement −u(ru−r+1)[r²u²−r(r+1)u+r+1] is positive below u* in the even interval since the bracket has negative discriminant. This proves convergence and u>u*/2 at every step, hence y>0. Independent exact Kronecker-product solves on all four coordinates reproduced both matrices, with det(Z)=21/16, det(2Z−X)=11/16, det(Y₁)=13934861/4521216 and det(Y₂)=−89099634797531/107317319122944; both leading minors needed for positivity are positive and X,Z do not commute. Replay with python3 /workspace/branches/independent_algebra.py. The strict conditions persist by continuity. This establishes transient cone exit, not eventual divergence or a floating-point failure.

## originality

PASS

The distinct supported contribution is the sharp qualitative separation between global positive convergence for commuting seeds under the explicit order hypothesis and the failure of that same hypothesis to preserve the cone for noncommuting seeds, with local attraction established in the full symmetric space. The iteration is already in Gao–Kressner–Shao. An indexed November record independently covers the qualitative second-step obstruction (with a stronger family); neither the qualitative obstruction alone nor the classical scalar logistic mechanism is credited as a distinct result against the current corpus. The overlapping result does not cover the commuting guarantee. The different record dates are not taken as a priority determination.

## value

PASS

The order condition can be checked directly and has an exact interpretation: throughout-orbit positive convergence for commuting seeds but not a general positivity safeguard, despite a locally attracting fixed point. This is useful for refinements that require SPD intermediate factors. The two-dimensional strict witness is immune to roundoff interpretation and isolates the gap in the smallest possible noncommuting size; it is not evidence about the failure frequency of the small-error algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
