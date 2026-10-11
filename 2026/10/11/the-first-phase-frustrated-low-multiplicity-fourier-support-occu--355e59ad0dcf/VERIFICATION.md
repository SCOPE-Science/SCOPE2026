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

The analytic proof has four independently checkable steps.

1. Parseval converts the fourth moment into the squared \(\ell^2\)-norm of the ordered pair-sum convolution.
2. The progression-free and multiplicity-two hypotheses reduce every nontrivial repeated pair sum to a term \(8+8\cos\phi\).
3. On at most five support points, two collision quadruples would share three points; two distinct completions of the same triple force a three-term arithmetic progression.
4. For \(\{0,1,3,4,9,10\}\), the three collisions have one phase relation \(\phi_1-\phi_2+\phi_3=0\). The exact trigonometric minimum is \(-3/2\), so the fourth-moment minimum is \(66-12=54\).

`artifacts/verify.py` reconstructs the pair-sum fibers, checks the integer row dependency, evaluates the displayed cubic-root phase witness, and confirms the fourth moment from convolution.

The script is corroborative. It does not replace the universal proof for supports of size at most five and does not establish claims outside the stated hypotheses.
