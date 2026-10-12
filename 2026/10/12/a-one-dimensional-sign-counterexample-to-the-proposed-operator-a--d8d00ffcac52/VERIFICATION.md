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

The counterexample is symbolic. The source alignment condition holds because \(-2x^2\le0\) for every \(x\in[-1,1]\), while the augmented direction equals \(-x\).

`artifacts/verify_alignment_sign.py` uses exact rational arithmetic to replay the source diminishing-step schedule and checks that \(x_0=\tfrac12\) reaches \(1\) after one step and stays there. It also checks an explicit late-iterate violation of the source one-step recursion using the sharp bound \(G=1\).

The finite script is supporting evidence only. The quantified failure and the corrected implication follow from the displayed algebra. The verification does not assess later source extensions beyond those depending on the same disputed sign step.
