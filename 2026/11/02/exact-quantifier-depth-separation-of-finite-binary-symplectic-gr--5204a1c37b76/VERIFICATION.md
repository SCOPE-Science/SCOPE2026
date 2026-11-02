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

# Reproducibility and limits

Execute `python3 verify.py` with Python 3.10 or later. The script reconstructs graphs of orders 3, 15, 63 directly from the standard alternating-form coordinates; it does not use precomputed graph tables. It computes canonical root Ehrenfeucht–Fraïssé types through rank four using finite extension supports, and checks the presence or absence of an induced claw.

The program's results are in `verify_output.txt`. The assertions require rank-two and rank-three equivalence for dimensions two and three and rank-four distinction, and distinguish dimension one at rank two. A finite check cannot certify equivalence for arbitrary dimensions or arbitrarily large quantifier ranks: these claims depend on the extension lemma, the linear span isometry strategy, and the isotropic-dimension lower bound proved in `RESULT.md`.

No independent audit has been performed.
