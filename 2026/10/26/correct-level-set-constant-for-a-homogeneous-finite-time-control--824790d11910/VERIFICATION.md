---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reconstructed the comparison. For nonzero x, dilate x by V(x)^(-1/(d+mu)) to the compact nonempty level set K (properness and homogeneity); on K the positive continuous F has minimum m>0. Rescaling gives F(x)>=m V(x)^(d/(d+mu)), with equality on the rays through the minimizers. The optimal HJB feedback gives dV/dt=-F-|u|^q/q. Integrate the inequality for V^(mu/(d+mu)) while V is positive; once V is zero, nonnegativity and monotonicity keep it zero. This includes x=0. For the example the weights (7/5,6/5) give degree 2 and satisfy the strict parameter constraint; the powers exceed 1. Constancy on K would imply V=C F^(11/10), whose last derivative vanishes at (s,0), s!=0. The drift there is also zero, contradicting HJB. Therefore max_K F is an upper, not lower, coefficient for F, in a genuinely admissible example. This does not refute a bound that could exploit the control-cost term. Bibliographic erratum: in the actual v1 PDF the target is Theorem 6.4, equation (6.1), followed by Remark 6.5; the frozen text misnumbers it but identifies the correct displayed argument. Replay: RESULT.md proof and example, lines 25–57; compare the cited PDF at pp. 13–14. VERIFICATION.md has narrative evidence only; no uploaded computation or formal certificate is required.

## originality

PASS

The general scalar comparison and homogeneous commensurability are known and are not the contribution. The distinct claim is the correction of the explicitly printed extremum in this particular theorem's F-only step, with an admissible control example separating the extrema. The inspected source uses max, not min; no distinct equivalent correction or example was identified in the bounded checks.

## value

PASS

This fixes a directional error in a quantitative finite-time guarantee for a standard chain of integrators. The example shows it is not a harmless choice of extreme values within the theorem's admissible cost class; using the correct extremum provides an applicable bound without asserting a trajectory-level counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
