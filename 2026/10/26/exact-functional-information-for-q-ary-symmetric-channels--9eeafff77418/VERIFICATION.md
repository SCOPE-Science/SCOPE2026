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

The proof was checked from the published width-function definition. For each output, the width is \(1\), then the prior mass of the high-likelihood set, then \(0\); the middle interval has length \((a_y-b_y)/P_Y(y)\). Multiplying the resulting divergence by \(P_Y(y)\) yields the stated formula.

The q-ary symmetric specialization uses the singleton high-likelihood set when \(1-\epsilon\ge\epsilon/(q-1)\) and its complement otherwise. The uniform extremizer follows from strict concavity of Shannon entropy or of \(u\mapsto-(1-u)\log_2(1-u)\). The maximum-gap result follows from \(H(cP_X+(1-c)u)\ge cH(P_X)+(1-c)\log_2q\).

Boundary checks: at \(\epsilon=0\), \(I_F=H(P_X)\); at \(\epsilon=(q-1)/q\), \(I_F=0\); at \(\epsilon=1\), the complement-entropy branch applies. For \(q=2\), the expression reduces to \(I_F=|1-2\epsilon|H(P_X)\). These checks follow from the analytic formula, not as a substitute for the proof.

No external computation is required for the theorem. The result does not claim an independent audit or independent validation. The cited coding-rate interval requires the bounded-likelihood-ratio assumption from the source theorem; the formula for functional information itself does not.
