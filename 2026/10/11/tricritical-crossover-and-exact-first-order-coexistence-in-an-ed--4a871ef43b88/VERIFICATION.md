---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For W_w with W(-1,0)=W(0,±1)=w, all other allowed edges weight one and forbidden (0,0), the positive Perron root of B_{w,y} is λ_k(y)=cosh y+√(sinh²y+k), k=1+2w²; the exhibited eigenvector is (1,2w/λ_k,1) and z=P_k'(y)=sinh y/√(sinh²y+k). Positive primitive matrix implies a unique linear equilibrium for each real y; the Legendre conditional entropy excludes endpoints for finite β. Differentiating R_k(y)=y/z_k(y) gives sign(N_k) for N=sinh y(sinh²y+k)-ky cosh y and N'=sinh y(3sinh y cosh y-ky). The increasing ratio 3sinh y cosh y/y rises from 3 to infinity, proving monotone R for 1<k<=3 and exactly one minimum for k>3. Along self-consistent stationary points the free-energy difference is C_k(y)=log(λ_k(y)/λ_k(0))-yz_k(y)/2, with derivative sign R'; its unique positive zero y_t>y_s yields exactly three global equilibrium pairs at coexistence and the strict β_s<β_t<√k order. The local series R/√k=1+(3-k)y²/(6k)+(7k²+30k-45)y⁴/(360k²)+O(y⁶) and sixth-order scaled free energy give β_s/√k=1-5(k-3)²/216+o((k-3)²), β_t/√k=1-5(k-3)²/288+o((k-3)²), y_s²/(k-3)→5/6, y_t²/(k-3)→5/4 and jump z/√(k-3)→√(5/12). Continuous-side k↑3 scaling gives z/√ε→√((√(25+1080b)-5)/18). Independently evaluated the scalar stationarity/coexistence equations for k=3.1,4,10, confirming the predicted ordering but using the analytic sign proof for all parameters; numerical roots never prove a continuum theorem.

## originality

PASS

The source fixed the unweighted k=3 critical point; the weighted family k=1+2w², its first-order region, unique coexistence and exact crossover constants are not stated or implied without new global analysis.

## value

PASS

PASS. A complete exact phase diagram for a natural one-parameter edge deformation resolves continuous versus discontinuous onset, the metastability interval and sharp tricritical crossovers. These are structural global phase facts not routine parameter substitution or a small numerical refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
