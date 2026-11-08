---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The four-field linearization at (1,1,h,h), projected onto Neumann eigenvalue κ, has characteristic quartic (z+t)^4+(5/2)(z+t)^2−(11/2)g(z+t)+g² with t=1+κ, g=hκ. Independent SymPy calculation verified the 4×4 determinant, Δ2=20t³+5t+(11/2)g>0 and Δ3=4t²(5/2+4t²)²−((11/2)^2+16t²)g². For first nonzero disk eigenvalue κ=1, a4=h²−11h+26 and Δ3=5476−377h²/4 give the three exact boundaries h± and hosc. Higher disk modes κ>5/4 have a4=(g−11t/4)^2+t²(t²−81/16)>0; the positive derivative polynomial makes their oscillatory thresholds larger than first-mode hosc. Constant mode remains stable, high modes decay. Thus the two strict stability intervals and the two stationary plus one oscillatory crossings follow with duplicated disk angular eigenvalues; at critical parameters no exponential stability is asserted.

## originality

PASS

Best-of-knowledge original as exact three-threshold reentrant local stability for this fixed positive specialization on a Neumann disk, with global-in-mode analytic exclusion. The four-field model, general quartic dispersion, Routh–Hurwitz theory and Turing/Hopf mechanisms are known.

## value

PASS

The recovered narrow stability interval is a meaningful model-specific counterexample to naive one-way-instability expectations. Exact thresholds plus rigorous suppression of all other spatial modes provide a reproducible dynamical benchmark, without claiming global bifurcations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
