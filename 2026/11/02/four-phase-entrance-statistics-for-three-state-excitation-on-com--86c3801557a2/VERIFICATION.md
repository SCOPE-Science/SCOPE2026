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

# Reproducibility and verification limits

Extract `verify_split_gh.py` and `support_table.csv` into the same directory and run `python3 verify_split_gh.py`. No nonstandard Python package is required. The program rebuilds all 49 occupied-color support transitions from the three-color local rule, verifies their complete exact entrance-time/least-period partition and checks the nine polynomial coefficient identities, then prints its reconstructed 49-row certificate.

The program implements a separate microscopic synchronous graph-neighborhood update and tests 477,315 labelled initial configurations on the 39 graphs with \(1\le m,n\le7\) and \(m+n\le10\), checking the first periodic-entry time, least period and \(F^7=F^4\) identity for each. It also checks the exact extinction basin, primitive three-cycle population and sharp transient boundary for 49 parameter pairs. `verification_output.txt` contains the actual observed output of this run. The embedded `support_table.csv` is regenerated from those transitions; comparing it with the program output is a transparent table-replay step. The direct enumeration confirms the formula in a finite range; the proof for all positive integers depends on the exact 49-state quotient and its complete finite classification, not on extrapolation from enumerated graphs.

No independently conducted audit or external validation is asserted.
