---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The unique gcd factorization (AB,CD,AC,BD) with gcd(B,C)=1 and degrees deg A=deg D, deg B=deg C gives squarefree local memberships none, one of A/B/C/D or the A,D pair. Four-variable Euler product splits four simple poles at 1/q from a holomorphic H: local first-degree terms cancel and absolute convergence holds on polyradius R=q^-3/4 because sum_d(q^d/d)R^(2d)<infinity. Cauchy bounds give O_q(q^-min(a,b)/4) per a+b=n, totaling O_q(1) after n+1 slices. The exact unrestricted denominator comes from coprime B,C count. Independent exact squarefree product-energy counts reproduce S_2(4)=128 and lower-degree cases, and SymPy verifies the strict factor inequality (1-v²)^5-(1-v)^4(1+4v+v²)=(1-v)^4v²(v+2)(2-v-2v²-v³), positive for 0<v<=1/2. Local log Euler terms yield -9/q for log Cq and rho=1-8/q+... . No q-uniform degree-error claimed.

## originality

PASS

Best-of-knowledge: compared mathematical implication, equivalent aliases, broader frameworks and exact tables; not directly covered by sources actually inspected. Residual literature risks and incomplete full-text access are explicitly recorded.

## value

PASS

Conditioned multiplicative energy is a natural finer statistic of polynomial factorizations; exact density exposes a provable negative squarefree correlation that the unrestricted collision count cannot yield. Four-variable local multiplicities and strict comparison form a substantive arithmetic theorem beyond recomputing known energy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
