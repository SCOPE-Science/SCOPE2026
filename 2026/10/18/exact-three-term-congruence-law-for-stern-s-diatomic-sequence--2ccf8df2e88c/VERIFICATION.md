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

The accompanying `verify.py` requires Python 3.9 or newer and only the standard library. Run it from the directory containing the finding files with `python verify.py`.

The checker constructs Stern values directly from the defining recurrence, checks the three-term index-valuation identity at \(200000\) consecutive indices, checks exact rational mass normalization and primitive-pair marginals for every modulus \(2\le m\le12\), verifies graph reachability on those same finite residue-state spaces, and compares predicted and observed full-row triple frequencies at \(65536\) indices for moduli \(3,4,6,7\). It returns `VERIFY_OK` on success.

These finite checks do not establish a theorem for arbitrary indices or arbitrary moduli. The proof of existence and the formula for all \(m\) rests on the finite-state irreducible aperiodic Markov-chain argument, the suffix-conditioning decomposition, the exact index identity, and the linear-congruence calculation supplied in `RESULT.md`. An independent audit has not been performed.
