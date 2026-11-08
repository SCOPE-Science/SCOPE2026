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

At fixed strictly positive occupations and kinetic prefactors, continuity constrains currents to J_i=r_i+c with r=(−b_1,b_3,0). Each force F_i=2asinh(J_i/(2omega_i)); total entropy ΣJ_i F_i is strictly convex in c, and its unique minimizer satisfies Σ(x_i+tanh x_i)=0. For 3 terms, zero Σx_i and zero Σtanh x_i forces one x_i=0, and the other two are ±, equivalent to L_1(b)L_2(b)L_3(b)=0 where L is the weighted linear-response projection. These give exactly three distinct straight lines in b_1+b_2+b_3=0 and alternating sign sectors, with no positive-ray reversal by continuity. Taylor expansion yields epsilon³/8∏(L_i/omega_i)+O(epsilon^5). Under generic b_i≠0, order r_l<r_m<r_h and shift c=−epsilon r_m+z; strictly monotone limiting root u+tanh u=−log R yields affinity limit −2tanh u in (−2,2). Independent bisection and random positive weights tested 150 cases with cubic coefficient and strong-drive asymptotic. Numerical tests corroborate but do not prove all rays.

## originality

PASS

The Euler equation, nonconservative advantage, cubic ORDER and absolute affinity bound are previously known; evaluated contribution is exact three-line conservative locus, all-amplitude chirality sign, cubic coefficient and generic direction-dependent saturation.

## value

PASS

The smallest nonequilibrium cycle is a natural test case for whether entropy-minimizing control is conservative. Exact exceptional lines, non-reversing chirality, and asymptotically finite driving affinity describe the entire 2D velocity domain and enable scientifically motivated force-design predictions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
