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

The theorem is proved symbolically in `RESULT.md`. The accompanying `artifacts/verify.py` is a corroborative exact-arithmetic check, not an exhaustive proof of the infinite statement.

The checker enumerates every cut in the following families: complete graphs through eight vertices, cycles through eleven vertices, and the Petersen graph. For each graph it computes \(M=\operatorname{MAXCUT}(H)\), forms the coefficient \(c=1/(2M-|E|)\), checks all Fourier values \(1+c(|E|-2|C|)\ge0\), and checks that the objective equals \(2M/(2M-|E|)\). For each odd cycle it also checks the algebraic rigidity equations forcing every edge coefficient to \(1/(2k-1)\).

Limits: the script does not prove edge transitivity, does not search all graphs, and does not establish originality. Those are handled respectively by the mathematical hypotheses/proof and the literature comparison. No computation is used to infer an infinite theorem from finite data.
