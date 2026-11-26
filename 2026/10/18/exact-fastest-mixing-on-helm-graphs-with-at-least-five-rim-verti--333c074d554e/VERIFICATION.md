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

Use the operator norm off constants, counting a second stationary eigenvalue for disconnected kernels. Dihedral averaging is a feasible convex norm contraction. In the first Fourier block the Laplacian is q E11 plus c times the matrix with diagonal 1 and off-diagonal -1, with q=a+2sb. Feasibility gives q+sc≤a+s(1−a)≤A, strictly unless both a=1/n and a+2b+c=1 since 0<s<1. The Rayleigh test at (1,1+√s) gives a nonstationary transition eigenvalue at least 1−A/D. Equality requires that vector to be an eigenvector, whose second equation fixes c=A(1+√s)/(√s D), even when zero weights are allowed. At the proposed triple it is indeed the top eigenvector of that block because both its entries and c are positive. For n≥10, 8/n²≤s≤20/n², and uD/(1+u)=2u+u³/(1+u)≤(2+1/5)/√5<1≤A/(1/n), giving c>1/n; c≤A/(2u)≤1/(4√2)+√20/20<1/2. For n=5 through 9 independent directed rational estimates on the explicit weight gave c in [380,382], [359,361], [339,341], [321,323], [305,307], respectively, in units of 1/1000. Thus the nonzero edge weights and holding probabilities are feasible. With α=1/n, the first block's top eigenvalue is ≥1−α: for c>α the determinant test reduces to s(1−α−c)(c−α)/c≤α; its left side is bounded by s(1−2√(α(1−α)))≤α using 20(n−2√(n−1))≤n². The latter follows from x⁴−18x²+40x−19≥5 for x=√(n−1)≥2 by differentiation. Other nonzero Fourier blocks have no larger upper eigenvalue; adding (1−α)I to each yields diagonal entries ≥c and off-diagonal c, so their lower eigenvalues are ≥−(1−α). The nonzero radial Laplacian roots have sum 1+α+2c and polynomial R(x)=x²−(1+α+2c)x+(2+α)c. R(α)=c(2−α)−α>0 and R(2−α)≥1−7α/2+2α²>0; the mean of the roots lies strictly between the endpoints, placing both roots in [α,2−α]. This establishes attainment, global minimum, and invariant-only uniqueness. Expanding s=2π²/n²+O(n⁻⁴) verifies both stated limits.

## originality

PASS

The closest inspected results share either the graph, objective, or an active weight constraint, but not their combination. No inspected result yields the coupled Fourier-block helm SLEM formula or the invariant allocation; symmetry reduction and saturated spokes on wheels are prior work.

## value

PASS

This is a complete exact optimization on a natural family built from a wheel and individual leaves. It resolves whether the competing radial and high-frequency modes prevent saturating both the hub and rim while pendant weights stay positive. The exact value, asymptote, and invariant optimizer give a reusable benchmark beyond the separate wheel and sunlet cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
