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

# Verification and limits
The self-contained `check_anticircle.py` uses Python's built-in exact integers and `fractions.Fraction` only. Successful execution was observed from the actual embedded source: `CHECK_OK: 256 complete cut inequalities; 5,6,7 exact embeddings; n=5..34 graph distances`. Its first two independent loops exhaust all binary cut masks \(0,\ldots,127\) for the two universal seven-point inequalities. It then evaluates every unordered vertex pair for the three explicit upper embeddings, without numerical tolerances. The sample graph-distance checks are supplementary; the all-\(n\) distance formula has an elementary proof in `RESULT.md`. Complete finite enumeration is a proof of the two seven-point lemmas; it is not a proof by extrapolating finite graph sizes.

The standalone file contains the entirety of the computations used in the accepted argument. No external datasets, packages or network access are needed. The claimed lower bound for all \(n\ge8\) follows from a seven-point restriction and the cut representation of \(\ell_1\) metrics. The exact optimum for \(n\ge8\) is unproved. Priority remains subject to older unavailable literature. No independent audit has been performed.
