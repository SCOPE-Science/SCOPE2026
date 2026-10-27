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
# Verification record

The standalone `verify.py` exhaustively enumerates all labelled binary configurations of \(G_n=\overline{C_n}\) for each integer \(5\le n\le18\), applies simultaneous open-neighbour majority with tie retention using directly constructed neighbour lists, and checks that the candidate structural recurrent predicate agrees exactly with \(F_n^2(x)=x\). It separately checks counts of fixed configurations and primitive two-cycles against the closed formulas. The saved `verify_output.txt` ends with `VERIFY_OK`.

The infinite-family theorem is established by the run and weight-layer argument in `RESULT.md`; the computer checks are finite corroboration only. The known central no-zigzag sequence is not independently rediscovered or certified here, and no independent external audit is claimed.
