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

The standalone file `verify.py` needs Python 3 and no third-party modules. Run `python verify.py`; the expected last output line is `VERIFY_OK`. The accompanying `VERIFY_OUTPUT.txt` records the enumerated size-by-size checks. The test checks original NEC voting against the derived four-symbol update independently for every labelled state with \(2\le n\le8\), then separately traces each orbit and compares first-periodic-entry times, fixed-state basins, primitive periods and exact cumulative counts with the formulas. There are exactly \(87{,}376\) tested initial states. All-size claims rest on the symbolic proof, not on extrapolation from enumeration. Literature searches do not certify novelty, and no independent audit has been conducted.
