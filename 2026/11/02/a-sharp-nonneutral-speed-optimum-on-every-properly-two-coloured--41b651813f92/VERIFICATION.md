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

# Reproduction and verification

Run the included file using `python3 verify.py`; only Python's standard library is required. The program uses exact `fractions.Fraction` arithmetic, not floating-point simulations.

The first method constructs all \(2^{\ell+1}\) labelled red/blue configurations of the original parent-selection/neighbor-replacement chain for each \(2\le\ell\le5\), retaining self-transitions. It solves the full transient linear equations for the probability of reaching all-red fixation and for the truncated first time moment \(\mathbb E[\tau\mathbf1_{\mathrm{fix}}]\). For each size it tests six exact fitness values \(1/2,1,6/5,3/2,2,3\) against the analytical fixation probability and conditional duration.

The second method independently verifies the absorbing embedded-chain harmonic probabilities, conditional occupation balance and exact three-coefficient holding-time sums for \(2\le\ell\le6\). The combined run completed **128 exact assertions**. These bounded calculations are consistency checks only; the proof in `RESULT.md` supplies the quantified all-size/all-real-parameter theorem.

The public data contain no experimental measurements. Mathematical limitations, matching assumptions and distinctions between full updates and genuine state-changing jumps are specified in `RESULT.md`. No independent audit has been performed.
