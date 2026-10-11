---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the two-marginal classification

The exact proof is the inverse-Jacobian calculation and the two Vieta identities in `RESULT.md`; those do not depend on numeric experiments. Both branches satisfy \(J(g_\pm(t))=-\varphi(t)\) and have weights \(\alpha_\pm(t)=1/J'(g_\pm(t))\). Differentiating gives \(|g_\pm'(t)|=\alpha_\pm(t)\varphi'(t)\). Summing inverse image densities therefore gives \(\pi\sum_{\varphi(t)=s}1/\varphi'(t)\) at \(s=-J(y)\).

For positive slope the finite-root Vieta sum is \(\sum \tau_j+(s-b)/a\), so its derivative is \(1/a\). For zero slope and \(s\ne b\), the sum is \(\sum \tau_j+\Gamma/(b-s)\), whose derivative is \(\Gamma/(b-s)^2\). This also demonstrates which cases require excluding a zero-slope exceptional value; no point mass is introduced by taking an almost-everywhere density.

Executed `python3 CHECK.py` with the included standalone script, using only Python's standard library. The outputs were: `PASS: 15 nonexceptional inverse-branch trace comparisons` and `PASS: 24 finite-difference graph-Jacobian comparisons`. The trace cases use two distinct poles, positive residues, slopes \(0\), \(0.3\), and \(2\), and five source values for each slope. The second probe independently finite-differences both supporting graphs at twelve parameter points and checks the predicted Jacobian cancellation. These tests do not constitute an infinite proof and cannot certify originality or independent validation.

The reference supporting the graph measure and its known extremality was inspected in full-text form: Fagrell--Luger, arXiv:2610.02476v1, Section 3.2. Distinctness of the two-marginal equivalence classes and singularity of different joint measures are proved algebraically from the rational-function hypotheses. No general statement about arbitrary nonrational Pick functions is verified.
