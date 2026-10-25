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

The local certificate comprises `verify.py` and `classification.csv`. Execute `python verify.py` with both files in one directory and Python 3.10 or newer. No external libraries or internet access are needed.

The program enumerates the complete four-vertex de Bruijn transitions of all 256 elementary rules, constructs reachable and co-reachable pair-of-subset states for minimal forbidden words, computes strongly connected components, and classifies path growth through exact finite graph structure. It verifies the CSV classification, its 176/28/52 counts, the absence of polynomial cases, and the sharp finite forbidden-length cutoff of ten exactly at Rules 57, 99, 156 and 198.

For bounded but infinite first-offender languages, integer path-count vectors are advanced to their first identical recurrence state. Equality of the entire vector, rather than merely observed output counts, proves eventual periodicity. Their exact preperiods and periods verify the four formulas for all lengths and the maximum of two offenders per length.

As a separate consistency check, complete finite preimage-block enumeration is performed for all 256 rules and output lengths one through nine, comprising 2304 independent comparisons with the first-offender product automaton.

These computations certify a finite classification. They do not establish historical priority, provide a complete classification of larger-radius rules, or constitute an independent external audit.
