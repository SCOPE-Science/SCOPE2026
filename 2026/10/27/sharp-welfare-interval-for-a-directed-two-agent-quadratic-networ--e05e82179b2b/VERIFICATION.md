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

# Reproducibility and verification

Run `python verify.py` in the same directory as the six scientific documents and the verifier. The program depends only on standard-library `fractions.Fraction` and has been executed successfully with `VERIFY_OK 945 exact rational parameter configurations`.

The 945 cases range over \(t\in\{1/7,1/3,2/5,3/5,4/5,9/10,99/100\}\), three positive square-root cost scales for each agent, and all nonzero pairs of nonnegative incentives from four rational choices per agent. For every case, the code directly computes unnormalized Nash and planner actions, evaluates both raw payoffs, checks both agents' best-response identities and the planner first-order equations, verifies strict positivity and all interval bounds, and checks the explicit endpoint factorizations as exact fractions. The separate unequal-cost case \((\gamma_1,\gamma_2,g,b_1,b_2)=(4,9,18/5,2,3)\) produces exact price of anarchy \(125/89\). Several additional rational strengths close to the threshold test that lower bounds exceed various prescribed magnitudes while the response matrix remains nilpotent.

The general proof uses no numerical estimates. Its essential critical steps are the normalization, the feasible positive-definite planner inverse, the two factored rational differences, and the diagonal-ray proof of unbounded welfare at and beyond the planner boundary. Finite checks provide reproducibility and could detect transcription errors but do not certify untested real parameters or historical originality. An independent audit has not been performed.
