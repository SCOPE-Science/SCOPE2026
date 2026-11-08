---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Reconstructed exact IF=(H+−H−)/2 and H±=(e^{it}/2)(1±e^{-it}I)²F; |H±|=(1±X)|F| with X=Re(e^{-it}I), so H^(1/2) quasi-norm ratios are (E_mu sqrt(1±X))². Let v(x)=(sqrt(1+x),sqrt(1−x)); ||v||²=2 and 1-P_t=(1/4) E||v(X)−v(X')||². Cauchy–Schwarz gives ||v(x)−v(y)||²>=(x−y)²/2, hence 1-P_t>=Var(X)/4. The maximum phase variance equals [1−|alpha|²+|beta−alpha²|]/2, proving the factor 1/8. For I=z and a symmetric two-atom boundary limit at ±delta, inf P_t=(1+cos(delta))/2, S=2sin²(delta), so ratio tends to 1/8; positive Poisson-kernel mixtures yield actual nonzero outer functions approximating those atoms, with phase-uniform convergence. Nonconstant inner has |alpha|<1 under strictly positive outer boundary density. Independently checked 22,680 finite randomized phase assertions and three small-delta ratios near 1/8. The coefficient is not certified sharp for the unrestricted dual-functional estimate.

## originality

PASS

Brevig–Søvik arXiv:2610.21788 gives the qualitative statement that extremals for H^p (p<1) are outer using the same decomposition and a strict Hölder inequality. In their accessible original mathematical proof no explicit optimized first-two-moment defect with coefficient 1/8 is given. Classical de Leeuw–Rudin introduced a qualitative decomposition in H¹. This theorem supplies a quantitative phase-optimized stability estimate and sharp envelope constant. General Hellinger variance inequalities are standard, and an equivalent earlier special inequality is a residual priority risk.

## value

PASS

Near-extremizer rigidity in nonlocally convex Hardy spaces motivates quantitative inner-factor penalties. The bound depends only on two explicitly computable moments, controls all bounded dual functionals without norm attainment, and includes a sharpness family for the natural decomposition envelope; this is more than a textbook statement that inner factors preclude exact extremizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
