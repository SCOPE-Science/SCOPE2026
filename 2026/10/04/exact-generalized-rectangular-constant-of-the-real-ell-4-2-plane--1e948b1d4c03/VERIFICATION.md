---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

For real unit vectors, differentiating the smooth fourth-power norm gives orthogonality x1^3 y1+x2^3 y2=0. Signed coordinate symmetries give x=(a,b) with a,b>=0 and a^4+b^4=1; every unit orthogonal direction is plus or minus (b^3,-a^3)/(a^12+b^12)^(1/4). The quartic expansion eliminates the linear term and gives 1+lambda^4+6A lambda^2+4B lambda^3. With u=a^2 b^2, A=u/sqrt(1-3u^2) ranges continuously over [0,1] and B^2=A(1-A^2); choose B negative. The normalized denominator F has boundary values at least one and tends to one uniformly in A as lambda tends to infinity; an interior test point is below one, so its global minimum is attained inside. The stationary equations are 3C=lambda(1-3A^2) and 3A(1-lambda^4)=C lambda(3-lambda^4). Substitution first gives lambda^4=1/A^2, then (1-3t)^4-81t^2(1-t)^2=(3t+1)(18t^2-15t+1)=0 for t=A^2. Only t=(5-sqrt(17))/12 has t<1/3. Substitution yields F=(5-sqrt(17))/2 and reciprocal (5+sqrt(17))/4. Uniform boundary control and unique feasible critical point establish the global optimum, not numerical enumeration. Independent 70-digit decimal arithmetic checks the stationary equations to residuals below 1e-68 and value 1.228911696999467; the proof is analytic.

## originality

PASS

Best-of-knowledge PASS for the original 2026-10-04 exponent-matched planar exact evaluation. The full same-invariant 2021/2022 paper gives bounds, not this value. The classical and quadratic constants use different numerators; their later exact evaluations cite this earlier record and do not establish prior coverage at its original publication. Two older/later subscription sources remain explicit bibliographic risks, not invented full-text noncoverage findings.

## value

PASS

The generalized rectangular constant is a established geometric invariant, and the same-invariant primary article explicitly identifies the gap between general estimates and exact values. Real ell_4^2 is the first non-Hilbert even-power planar case with a closed algebraic Birkhoff-orthogonality reduction. Its exact value and the coefficient relation B^2=A(1-A^2) form a natural sharp benchmark for general estimates; a researcher studying this invariant can need this exact fact without a general theorem. This is not classical-table recomputation or an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
