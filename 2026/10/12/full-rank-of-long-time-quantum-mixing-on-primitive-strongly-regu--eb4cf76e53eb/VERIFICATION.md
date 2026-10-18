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

Expanding U(t)=sum exp(i theta t)E_theta and Cesàro-averaging gives Mhat=sum E_theta∘E_theta. Primitive SRG projector entries are constant on diagonal, edges and nonedges; independently simplified m=(-k-(n-1)s)/(r-s), n=(k-r)(k-s)/(k+rs), and resulting d-f+(e-f)r to the displayed rational expression Λ_r=[r²+s(s+2)]/(r-s)²−2r(s+1)/[(k−r)(r−s)] exactly (SymPy difference zero). For primitive SRG restricted r>0 and s<-1; integer case gives r>=1,s<=-2. In the nonintegral Galois-conjugate case m=p implies r+s=-1, k=(n-1)/2 and conference parameters; n>=9 again r>=1,s<=-2, with n=5=C_5 direct. Both terms of Λ_r are nonnegative with strict positive second term; complement swaps restricted eigenspaces without changing projector Schur squares, implying Λ_s>0 too. Principal eigenvalue=1 and C_5 Λ_r=Λ_s=1/5. This is a proof for all feasible primitive SRG, not extrapolated from example scripts.

## originality

PASS

Best-of-knowledge acceptance follows the actual statement-versus-implication comparisons above; the strongest inspected primary sources establish a general framework, different problem, or strictly narrower subcase, not this final full claim. The explicitly listed plausible full-text access/implicit-coverage risks remain open; lack of search hits alone is not novelty evidence.

## value

PASS

Resolves the diameter-two primitive strongly regular subclass of an explicit open full-rank question for primitive distance-regular graph quantum mixing; strict positivity means no vertex-distribution mode is lost under long-time averaging. The result addresses a natural unknown spectral property, not an arbitrary graph sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
