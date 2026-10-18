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

For f(x)=sqrt(1+x²)−x cos x, independently differentiated f’=x/sqrt(1+x²)−cos x+x sin x and f’’’=−3x/(1+x²)^(5/2)+3 cos x−x sin x. Their sum is h(x)+2cos x, h=x(x⁴+2x²−2)/(1+x²)^(5/2). Putting y=x²≥0 yields exactly (1+y)^5−y(y²+2y−2)^2=1+y+18y²+10y³+y⁴>0, hence |h|<1 for every finite real x. Therefore |f’’’|−|f’|<=|f’’’+f’|<3; L0=3 valid at L1=1. At x=2πn tending to infinity, f’->0 and f’’’->3, making every L0<3 invalid. Symbolic independent differentiation and polynomial subtraction rerun exactly in SymPy; grid scripts are only consistency checks, not proof of global bound or asymptotic optimality.

## originality

PASS

For the 2026 Fang–Marumo–Takeda benchmark, the result claims to sharpen the exhibited admissible pair (L0,L1)=(6,1) to the exact fixed-slope optimum (3,1). Search for the same objective/formula, parameter-free cubic regularization and the fixed-slope intercept yielded no dominating published exact constant. The original 2026 paper primary full text was unavailable from lawful arXiv/OA attempts, and authorized institutional access returned vpn_disconnected, so the exact presentation of the old benchmark could not be independently re-read. This is a named residual originality risk, not automatic rejection; the calculation itself and what it adds to the claimed 6 certificate are explicit.

## value

PASS

The source deliberately uses a pointwise third-derivative smoothness model with constants entering cubic-Newton bounds. The exact minimum L0 at the natural fixed L1=1 is a coherent quantitative benchmark parameter and halves the cited sufficient intercept 6; it is a motivatable, reusable exact model constant, not a claim to optimize every parameter or show a new algorithmic convergence theorem. Though the proof is compact calculus, this benchmark-specific optimal input can matter when comparing instance-sensitive constants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
