---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For n=4r+2>=6 and m=n/2 odd, each translated length-5 cycle has an odd number of frustrated (equal-spin) edges; summing gives 2f-e_i>=n, and two odd inner m-cycles force e_i>=2, yielding f>=m+1 and minimum energy H/J=2f-3n>=-2(n-1). The 8-state transfer matrix T(z) with state (a_i,b_i,b_{i-1}) and edge cost [a=a’]+[c=b’]+[a=b] exactly enumerates labeled configurations by tr T(z)^n. Normalized determinant det(I-y z^{-1}T(z)^2) has E0=(1-3y²+y^4)^2, E1=-2y(y-1)^2(y^4+8y^3+15y²+8y+1); its logarithmic trace derivative has odd-y coefficient 2m² F_m at z^1, attaining the lower bound. Independently recomputed E0/E1 via 8x8 determinant symbolic arithmetic (both identities true), and independently verified the weighted determinant identity. A fugacity w^{a+b} yields odd-y first correction -2y^7+(2-w²-w^-2)y^5-2y, restricting magnetization to 0 and ±4 and giving coefficient A_m=m[t^((m-5)/2)](1-3t+t²)^(-2) for ±4. Independent transfer dynamic programming directly gave totals 36,250,1274,5508 and respective ±4 counts 0,5,42,225 for n=6,10,14,18. The determinant identity plus odd-cycle bound, not finite checks alone, supports all odd m.

## originality

PASS

Jacobsen–Salas 2013 supplies general Potts/Ising transfer methods for generalized Petersen GP(nk,k) graphs; the existence of a transfer matrix is prior. Strečka–Karlová–Madaras 2015 compute the n=10 dodecahedron including degeneracy 250 and ±4 multiplicity 5. Those are credited. Reviewed prior results did not state the unbounded n=4r+2 quadratic-Fibonacci count and magnetization coefficient A_m. Qualified originality PASS.

## value

PASS

The graph family GP(4r+2,2) is a standard sparse cubic graph with two frustrated odd inner cycles. Its exact all-size ground-state energy, degeneracy 2m²F_m and complete magnetization-resolved count are natural statistical-mechanical observables. These closed forms are substantially more informative than a generic transfer matrix or one isolated dodecahedral computation and can benchmark frustrated Ising calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
