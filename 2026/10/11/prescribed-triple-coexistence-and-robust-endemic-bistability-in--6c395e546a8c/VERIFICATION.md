---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Writing e1=s1+s2+s3, e2=Σsisj,e3=s1s2s3,P=Π(1+ωsi), choosing K>max(e1+1/ω+ωe3/s1,P/ω), r=aK, β=a(K−e1−1/ω), σ=aP/ω, μ large and α=aωe3/μ ensures all parameters and I(si)=βsi/μ−α positive. Direct nullcline elimination gives exact identity F(S)=−aωΠ(S−si)/(S(1+ωS)), an at-most cubic positive coexistence equation. At roots, g_I=−μτ_i<0 and det J=aμωτ_i Π_{j≠i}(si−sj)/(1+ωsi), giving +−+; f_S=H_i and μ>max H_i^+/τ_i forces traces negative at all roots, so outer sinks and intermediate saddle. r>σ makes disease-free Q(S) concave quadratic with positive constant and exactly one positive root. Nonzero det, strict inequalities, and the persistent cubic bound justify robust seven-parameter open realization by IFT. Independent exact rational arithmetic checked example (130,130,106,20/53,126,1,106), I coordinates 33/53,86/53,1040/53 and determinants 627,−516,11856/7 with traces −71/2,−60,−828/7. This exact example supports, but is not substituted for, arbitrary-triple algebraic proof.

## originality

PASS

The 2024 same-ODE source contains a coexistence cubic and conditional stability analysis, but not arbitrary prescribed triple inversion with simultaneous alternating hyperbolic sink/saddle/sink signs and one disease-free equilibrium. Its Theorem4 assumes r<σ, while the constructed open region has r>σ. Related forest/fire or ecological-bistability models differ in equations and do not imply this universal constructive realization.

## value

PASS

The universal constructive triple-realization theorem turns an algebraic upper bound of three coexistence equilibria into a robust simultaneous two-attractor endemic bistability mechanism in the exact ecological model. Requiring positive epidemiological parameters, exactly one disease-free positive root, and stability signs for every prescribed triple makes the result substantively stronger than numerical multistability examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
