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
# Verification

The mathematical proof is contained in `RESULT.md`; the checker is supplementary.

`verify.py` performs the following finite checks:

1. It confirms that the subcritical exponent gap \(\sqrt{2\beta}-\beta\) is positive for representative \(0<\beta<2\).
2. It evaluates the explicit supercritical choice \(q=1-\sqrt{(\beta-2)/(2\beta)}\) and \(\varepsilon=(\beta-2)/(8q)\), confirming that the Markov exponent is exactly \(- (\beta-2)/8\) up to floating-point roundoff.
3. At the exact critical scaling \(\delta=\sqrt{2\log n}\), it checks the closed-form truncated moments \(\mathbb E[W\mathbf 1\{W\le n\}]=1/2\) and \(\mathbb E[W^2\mathbf 1\{W\le n\}]=n^2\overline\Phi(\delta)\), and confirms numerically that the common bound \(n\overline\Phi(\delta)\) decreases toward zero over increasing \(n\).

The checker does not certify an infinite limit by finite enumeration. The asymptotic limits rely on the explicit inequalities and probability arguments in the proof. No second-order critical-window claim is verified or made.
