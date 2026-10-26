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

# Verification instructions

The standalone `verify_prufer.py` program generates every labeled tree up to seven vertices by Prüfer sequences, canonicalizes to graph-isomorphism classes, enumerates all induced-four-path-free selected vertex sets, then tests all target-colour assignments and all proper three-colourings. The independent `verify_dp.py` uses NetworkX's unlabeled-tree enumeration, and decides every binary pattern's realizability with a bottom-up three-colour list-constraint recurrence. Their outputs are included and agree at every order.

`witness_5.json` holds \(32\) concrete proper three-colourings covering all patterns of the claimed five-query shattered set. Run `python3 verify_witness.py` to replay it. These are actual complete certificates of the finite claims. The infinite restriction lemma is proved in the manuscript; no finite search is offered as proof of it.

Commands:

```bash
python3 verify_prufer.py
python3 verify_dp.py
python3 verify_witness.py
```

Dependencies: Python 3.10 or later; `verify_dp.py` additionally uses the NetworkX package. All files are relative to this directory. No random seeds or external inputs are required.
