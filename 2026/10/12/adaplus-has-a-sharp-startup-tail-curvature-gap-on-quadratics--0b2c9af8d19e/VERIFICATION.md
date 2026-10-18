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

The result explicitly defines the paper-form AdaPlus scalar recurrence with zero decay, h>0, 0<=beta1,beta2<1 and epsilon>0. Direct substitution at source state m0=s0=0 gives exact first-step correction (1+beta1)h*x0 and denominator sqrt(beta1^2*h^2*x0^2+epsilon/(1-beta2))+epsilon; small-x0 objective increase occurs iff a*h>2D/(1+beta1), D=sqrt(epsilon/(1-beta2))+epsilon, with equality not a strict spike. Along zero-gradient orbit second moment bias-corrected floor is epsilon/(1-beta2); linearize first-moment/state to matrix [[1-(a/D)(1-beta1^2)h,-(a/D)beta1^2],[(1-beta1)h,beta1]], plus stable second-moment eigenvalue beta2. Three exact Jury inequalities reduce to a*h<2(1+beta1)D/((1-beta1)(1+2beta1)), -1 root at equality. For beta1>0, nonempty gap and ratio (1+beta1)^2/((1-beta1)(1+2beta1)), independent defaults h_start=3.3287238528, h_tail=42.9167611023 and h=10 objective amplification 25.0831545759. Independently checked matrix determinant, eigenboundary, values and first-update formulas. The tail conclusion is only limiting local spectral stability, not global convergence. IMPORTANT: author official code AdaPlus.py lines 610-616 uses denom sqrt(s+epsilon)/sqrt(bias_correction2) WITHOUT a final +epsilon; thus exact numerical thresholds apply to the explicitly specified paper-form update, not that source implementation. Original full paper algorithm was not independently read, so a transcription mismatch remains a material model-provenance risk.

## originality

PASS

AdaPlus itself and its published empirical optimizer combination are prior. AdaBelief introduced the prediction-error squared moment; related stability analysis exists for AdaBelief (not AdaPlus), and general Nadam/AdamW momentum is prior. No equivalent two-threshold AdaPlus scalar startup-versus-asymptotic Jury phase diagram was located. Official source code is an important non-identical epsilon-placement implementation; do not claim exact source-code behavior or author implementation coverage.

## value

PASS

With the stated scalar recurrence the disagreement of startup objective descent and asymptotic Schur stability is an exact nontrivial optimizer safety frontier; the default gap ratio exceeds 12.89 and gives a motivated counterexample to trusting only local stable eigenvalues. A single scalar quadratic is the natural minimal diagnostic for a fixed optimizer, unlike arbitrary unmotivated parameter slices. It is explicitly not a theorem for the different official source-code epsilon placement, multidimensional curvature, stochastic gradients or nonlinear global convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
