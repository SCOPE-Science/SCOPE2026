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

Normalized disk monomial moments are 1/(n+1). Taking the squared A² norm of P² gives the fourth moment; its sole phase-sensitive term comes from |b²+2ac|² and demands aligned phases at an interior optimum. When c=0 the quotient is 1+2v−5v²/3 for v=|b|²/(2||P||²_A²), attaining 8/5 at v=3/5. For c≠0 take u=|a|/|c| and q=3|b|²/(2|c|²). The q derivative has affine numerator with positive intercept and strictly negative slope for all u≥0, so it has a unique global maximum in q>0. After substitution the derivative of the remaining rational quotient has sign opposite to 30u³+35u²−5u−4; its unique positive root gives a strict maximum above both u=0 and the c=0 face. Independent exact differentiation and elimination reproduce q*=(3/2)u*(3u*+1) and the constant polynomial (the resultant multiplier is 2618387280). The quotient at u=1/3 is 2791/1042>13/5, and the constant polynomial is strictly increasing above 13/5, isolating the largest root. Magnitude and phase equality give exactly the stated scalar-and-rotation family; |a/c|=u*, whereas a/c=u* only in the aligned real representative. The invariant b²/(ac)=3u*+1>2 differs from 4/3 for every nonconstant K₂; K₂ at the origin is constant, and K₁ with |w|²=3/4 attains the degree-one maximum.

## originality

PASS

The supported distinct claim is the exact unweighted quadratic constant, the complete optimizer magnitudes and phases, and failure of truncated evaluation kernels at the first possible degree. Two close weighted records genuinely cover strict three-mode mixing and phase alignment at this weight; these structural statements alone are not distinct. The inspected weighted proofs give large-weight asymptotics rather than the finite-weight algebraic maximum or the kernel obstruction. The primary embedding literature has different measures, spaces or non-sharp bounds.

## value

PASS

Area A² normalization makes the fourth-moment quotient a natural exact measure of concentration among finite polynomial profiles, and reproducing kernels are the natural point-concentration candidates. Degree two is the first degree permitting a genuine relative phase in this moment problem. The exact optimizer family resolves whether the degree-one kernel prescription survives that new interaction, and gives a sharp benchmark for finite Bergman concentration rather than a numerical comparison at an arbitrary weight.

The dated certificate retains the supplied scientific assessment, sources and limitations.
