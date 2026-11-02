---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For alternating equal-duration directed layers A1=[[0,a],[b,0]], A2=[[0,b],[a,0]], let κ=sqrt(ab), Γ=(a+b)/(2κ). Since Aj²=κ² I, their exact half-period exponentials multiply to a positive determinant-one 2×2 matrix with half-trace 1+2Γ² sinh²(βκT/2); its Perron eigenvalue is exp(2 asinh(Γ sinh(βκT/2))). Thus Λ=−μ+2/T asinh(Γ sinh(βκT/2)). With Γ>1, f(z)=asinh(Γ sinh z) has f(0)=0 and f(z)=Γ(1−Γ²)sinh z/(1+Γ² sinh² z)^(3/2)<0 for z>0, so f(z)/z decreases strictly from Γ to 1, yielding a unique cutoff iff βκ<μ<β(a+b)/2 and correct equality/degenerate a=b cases. Expanding f(z) at 0 gives C2=β³κ³Γ(Γ²−1)/24>0 and Tc~sqrt((βm−μ)/C2); large-z gives βκ−μ+2logΓ/T. Independent symbolic matrix trace/determinant and f checks and a numeric bracket around Tc=0.947213258 for a=9,b=1,β=1,μ=4 passed. These are only the disease-free Floquet exponent of the deterministic approximation, not stochastic persistence or global endemic convergence.

## originality

PASS

Best-of-knowledge exact statement and implication comparison: closest accessible primary papers and ranked published findings do not establish this precise claim under the stated parameters. This is not a historical-priority certificate; see source inspections and risks.

## value

PASS

Rapid switching of individually subcritical directed contact layers is previously known qualitatively, but the precise critical half-period is an important natural missing invariant. This two-group family admits an exact all-period monotone phase diagram with strict necessary-and-sufficient parameter window, unique switching cutoff and quantified square-root emergence, making the directional effect mathematically interpretable rather than merely exhibiting one example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
