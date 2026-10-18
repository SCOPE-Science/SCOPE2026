---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For real ell_3^2 unit vectors, the increasing symmetric cubic difference Phi(u,v)=|u+v|^3-|u-v|^3 forces isosceles orthogonal pairs, modulo signed-coordinate isometries and interchange, to x=(a,b),y=(b,-a), a^3+b^3=1. Both ordered lambda branches were considered. The G branch has denominator minus numerator equal to concave quadratic expressions in the smaller parameter, nonnegative at the explicitly calculated endpoints, hence G<=1. For F(r,lambda)=(1+r^3)(1+lambda^3)/((r+lambda)^3+(1-r lambda)^3), I independently recomputed both symbolic gradients and their elimination in SymPy and recovered the q4(r)=r^4+6r^3+4r^2+2r-1 and q6 factors; the source's degree-six positive Bernstein certificate excludes roots of q6 on [0,1]. The unique q4 root t*=0.27799674994077759 gives the sole relevant interior stationary point (t*,t*), with boundary<=1 and value>1. Independent evaluation gives H3=1.0290679924451533. Source checker independently reconstructs the Sylvester identity by exact evaluation at 25 points and a degree bound. All real quantifiers and boundary values are covered analytically, not by the computed decimal.

## originality

PASS

The defining Baronti–Bertella 2024 paper computes H_p for Hilbert spaces and ell_infinity^2 and gives bounds but not H3 on the smooth real ell_3^2. Nearby published SCOPE records use H4 on a hexagonal norm or different Birkhoff/Dragomir/James functionals on ell_3^2, which are not mathematically interchangeable. Exact q4 parameter searches found no covering formula in inspected sources, subject to historical aliases and a failed Resultary request.

## value

PASS

The exponent-matched classical smooth non-Hilbert ell_3^2 plane is a canonical first computation for the new H_p family. Classification of isosceles unit pairs and an algebraic interior extremum, rather than the Hilbert/square endpoints or a routine bound, provide an exact benchmark for future H_p(ell_q^2) work. No new general p or dimension theorem is claimed or required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
