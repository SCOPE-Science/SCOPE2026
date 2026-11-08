---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For n=2^k >=4 and s>=1, the actual symplectic two-block lattice matrix M=L^2 with C=P+P^-1 is invertible modulo 2^s. In F2[z]/(z^n-1), z^n-1=(z+1)^n and C=z^-1(z+1)^2 is nilpotent of exact index t=n/2. Writing M-I=CL and using invertibility of L gives M^(2^j)-I=C^(2^j)L^(2^j) mod2, proving exact binary matrix order t and kernel nullity 2min(2^(j+1),n). The crucial integral lift, checked algebraically for arbitrary k, has C^t congruent 2(I+P^t) mod4; E=(M^t-I)/2 mod2 equals J I + C^(t/2)L^(t/2), with E^2=0 and nonzero upper-right block C^(t-1). Therefore M^t has exact valuation one, M^(2t) exact valuation two, and subsequent squaring increases valuation by precisely one, yielding ord_(2^s)(M)=t*2^(s-1). Solving Cx=0 through x_(i+2)=-x_i gives precisely 2^(4s) fixed phases. Exact binary fixed counts f_j yield primitive cycle counts (f_j-f_(j-1))/2^j and maximal fraction 1-2^-n. Independently checked full modular matrix orders at n=4,8,16 and s=1..5 (15 cases), including strict half-order failure; the proof supplies arbitrary n and s rather than extrapolating finite runs.

## originality

PASS

PASS, qualified. Manolas–Floratos and Axenides–Floratos–Nicolis already developed the same coupled cat-map matrix family, Fibonacci-polynomial recurrences and sampled torus periods, including dyadic scaling. Their inspected relevant primary text did not give the exact power-of-two nearest-neighbor base order or binary full orbit census. Resultary all-to-all cat-map arithmetic uses a different coupling matrix and does not imply the cycle case. General finite-ring dynamical theory remains a possible antecedent.

## value

PASS

This gives a complete closed torus permutation-order law for all dyadic resolutions and an exact primitive binary orbit/zeta census for a canonical nearest-neighbor lattice cat-map family. It identifies the microscopic 2-adic order-lift mechanism behind a previously studied qualitative scaling and quantifies maximal-orbit prevalence; these natural invariants are not merely a numerical example or reparameterization of all-to-all coupling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
