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

Using the specified group law and [x,y]=x⁻¹y⁻¹xy, the first rotation is u⁻ⁱ⁻ʲ[(1−uʲ)a+(uⁱ−1)b]; each further step multiplies it by u⁻ʲ−1. The fixed-(i,j) image is the ideal of the two coefficients, with gcd d_{i,j,k} and kernel size m d_{i,j,k}. All coefficients are multiples of (u−1)^k and i=0,j=1 realizes this ideal if h>1; the h=1 case is trivial. At p^a∥m, a j not divisible by t=ord_p(u) leaves the first coefficient a unit. For t∣j valuation grows by at least s each iteration; when t=1 both coefficients already have valuation ≥s at the first step. This gives the stated ceilings. The bounds are attained prime-locally by i=j=1 when t=1 and s<a; by i=1,j=t when t>1 and s<a (then h>t); and by i=1,j=0 at depth one when t>1 and s=a. The divisors increase by divisibility, so a deficient divisor keeps the identity fiber strictly below its terminal count, proving leastness for the distribution, not just for a sufficient local bound. The terminal divisors give the subset/lcm identity normalization by averaging j modulo h, since all t_p divide h. A primitive unit modulo an odd prime power has t=p−1 and s=1 for exponent a≥2; exponent one is already sharp for the nontrivial action of C₂ on C₃.

## originality

PASS

Credit the distinct contribution in arbitrary, potentially noncoprime cyclic-by-cyclic actions: the sharp valuation-sensitive least plateau and explicit all-depth distribution beyond coprime-action and identity-locus results. Prior cosetwise homomorphism counting, the fixed-point-free depth-two identity locus, and the coprime terminal law are already covered ingredients or cases. The closest inspected sources do not yield the mixed/lift-dependent sharp cutoff. This is a best-of-knowledge scoped pass, not a priority certification.

## value

PASS

Repeated commutation may keep the same eventual law while changing how long it takes to get there. The exact cutoff identifies which prime-power lift delays stabilization and detects a full extra step from a nontrivial residue action, instead of supplying only qualitative eventual behavior or an upper bound. For example, the two C₂₇ actions with complement C₁₈ have the same terminal law but cutoffs 4 and 3. The formula is an independently useful exact invariant of a broad natural family, with the noncoprime regime providing the value beyond the coprime cases already covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
