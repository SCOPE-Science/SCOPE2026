---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: Using the published eight-compartment equilibrium reconstruction, r1,r2 are affine in s; Δ=γ1γ2s²-σ1σ2v1v2r1r2 and Cramer numerators N1,N2 are quadratic or lower. Susceptible residual F_G=A-(v1sN1+v2sN2)/Δ+(θ12/(d12Δ))(γ1σ1r2N1+γ2σ2r1N2), where A affine. Therefore -ΔF_G=-ΔA+v1sN1+v2sN2-(θ12/d12)(γ1σ1r2N1+γ2σ2r1N2), each summand degree<=3. This is a universal algebraic proof rather than sample interpolation. Independently expanded the positive parameter example µ1,γ1=2,γ2=3,β1=3,β2=2,ηi=σi=θi=θ12=1,Λ=10, obtaining P_G(s)=s³+53s²-356s+260, so max degree exactly3. Singular Δ=0/feasibility interval are not part of asserted root classification.

## originality

PASS

PASS: The exact source Adenane--Avram--Halanay 2026 explicitly states P_G has degree four just before its Question 2, despite printed rational equations yielding a universal cubic cancellation/degree bound. Lawfully available full preprint section was read, confirming the incorrect source claim rather than guessing from summaries. Related withdrawn Gavish--Rabiu work's asymptotic quadratic is not the same exact scalar coexistence polynomial; a search of published findings gave no prior cubic correction.

## value

PASS

PASS: Correcting a concrete erroneous polynomial degree in a peer-reviewed paper's posed feasible-equilibrium root-count question changes maximal algebraic root count from four to three and simplifies prospective discriminant/resultant/Sturm analyses. It is a precise, substantive correction of mathematical claims, not an arbitrary computational check; it does not solve full feasible-multiplicity classification or stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
