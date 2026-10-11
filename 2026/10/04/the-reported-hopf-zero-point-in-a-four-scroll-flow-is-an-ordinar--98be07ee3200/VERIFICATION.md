---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

For the printed vector field the Jacobian characteristic polynomial is \((\lambda+c)[\lambda^3+(b-a)\lambda^2+(1-ab)\lambda+(b-a)]\). At \(a=0\) this factors as \((\lambda+c)(\lambda+b)(\lambda^2+1)\), giving \(\{-c,-b,i,-i\}\) and excluding a zero eigenvalue. Implicit differentiation of the critical root gives \(\operatorname{Re}\lambda'(0)=b^2/[2(1+b^2)]\), hence \(729/1460>0\) at \(b=27\). Reconstruction of the quadratic Hopf coefficient with the package normalization gives \(l_1=-58491/724744000<0\), so the crossing is an ordinary nondegenerate supercritical Hopf bifurcation and the stable small periodic branch lies for \(a>0\). The separate zero-Hopf spectral condition is \(a=b\in(0,1)\). A fresh exact rational replay independently reproduced the crossing derivative and Lyapunov coefficient.

## originality

PASS

The introducing article prints the same vector field and characteristic polynomial, states that a zero eigenvalue occurs when \(a=b\), but then at \(a=0\), \(b=27\) reports the incompatible spectrum \(\{\pm i,0,-27\}\) and calls it a codimension-two Hopf-zero point. The corrected spectrum is therefore directly checkable from the source, but the final audited claim goes further: it establishes transversality, computes the first Lyapunov coefficient, and classifies the actual local branch as stable and supercritical. Current Resultary and targeted web searches returned related corrections for other four-dimensional flows and later Vaidyanathan systems with different equations, but no prior correction or normal-form treatment of this system.

## value

PASS

The result repairs a published codimension-two bifurcation claim in a named system and determines the actual local branch and its stability, not merely one eigenvalue sign. Correct local bifurcation type is structurally relevant to how the reported parameter scan is interpreted, so the normal-form correction is a motivated mathematical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
