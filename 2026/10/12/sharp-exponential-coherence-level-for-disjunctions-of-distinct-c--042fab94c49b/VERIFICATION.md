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

# Verification procedure and scope

Run `python verify.py` in the extracted package directory; Python standard library suffices. The script exhaustively tests all subsets of binary tuple carriers for \(r=1,2,3,4\) and ternary carriers for \(r=1,2\), for 66,332 team masks total. It computes selector covers directly, enumerates inclusion-minimal counterexample sizes, checks every binary-cube sharpness witness, and independently computes multilinear coefficient-matrix ranks over the rational field. It also tests 12,000 reproducible randomly generated ternary three-coordinate teams by greedy minimization and checks their residual minimality and size.

Expected closing line: `VERIFY_OK exhaustive_team_masks 66332`.

The exhaustive computations concern only the listed finite carriers and the sampled ternary case. The theorem for arbitrary values of \(r\), arbitrary domains, and infinite teams is certified solely by the fully explicit induction and polynomial-independence proof in `RESULT.md`, not by finite test extrapolation. No external independent mathematical review has taken place.
