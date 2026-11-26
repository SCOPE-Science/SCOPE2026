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

Solving the two triangular stages gives the stated rational multiplier. Its derivative is s^3(2x-1)/(1+sx)^3, and the endpoints locate the two sign boundaries at 2 and 1+√3. The two third-order expressions reduce to x²−x+1/2 and x−x², so both target expectations impose the same mean m=1/12 on U=(x−1/2)^2. In the mixed range the negative set is U<a_s. Thus m≥a_s Pr(U≥a_s), with equality for the proposed atoms at 0 and a_s; the atom at the boundary is zero-amplifying, not strictly positive. At a_s=m only δ_m in U avoids negatives, and above the upper step endpoint all draws are negative. The positive-side attainment follows by choosing parameters on both sides of the mean-matching parameter in the open positive region. The finite-step uniform laws follow by iid parity and the geometric waiting time, with no zero atom. For the more general endpoint-tail limit, an atom at the moving boundary is allowed: writing F(u)=Pr(ξ−1/2<u), its mass is at most F((1+ε)u)−F(u), hence o(F(u)) by regular variation and ε↓0. The chance that a zero absorbs the process before a negative is therefore o(1), preserving the stated exponential limit for the first negative iterate. For A-stability, writing C=x²−2x+1/2, the squared denominator minus squared numerator on z=iω is (x⁴−C²)ω⁴≥0 on the stated x interval. There are no left-half-plane poles and the limit at infinity has modulus at most one. The real endpoint bounds give strict fixed-s contraction. An independent evaluation of the displayed quadratic gives s*=2.2458294939508745 at double precision; the analytic proof, not this evaluation or the finite grids, establishes the result.

## originality

PASS

Credit is for the sharp frontier, strict-positivity feasibility boundary and optimal redesign over the expected-order moment class. The originating paper supplies the tableau, uniform sampler, rational stability function and A-stability. The November 2 catalogue record materially overlaps the uniform sign-risk, square-root onset and iid count results, which are not credited as distinct from that record. Its statements do not settle the optimization over general admissible sampling laws. The catalogue date is not used to decide priority.

## value

PASS

Changing the sampler while preserving the source method's formal expected-order conditions is a natural design question. Its exact step threshold 2.24582949… is strictly above the uniform sampler's sign onset at 2, and distinguishes strict safety, inevitable zero amplification at the frontier for negative-free draws, and unavoidable negative risk above it. The optimizer and upper-endpoint jump clarify why zero multipliers cannot be ignored in the design problem; A-stability alone offers no such guidance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
