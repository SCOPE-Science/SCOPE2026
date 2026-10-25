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

# Reproducibility

Run `python check_direct.py` and `python check_structure.py` with Python 3 and NetworkX. The expected exact output is recorded in `direct_output.txt` and `structure_output.txt`, respectively. The first script derives feasibility by testing all open neighborhoods on the labeled board; the second constructs the bounded-fiber function graph directly. Both independently verify the Desargues graph isomorphism using NetworkX's reference graph constructor.

The direct exhaustive check covers only the six boards specified in the finding, whereas the structural test covers support graphs with three through eight columns. The proof of the general statement is combinatorial and does not rely on those finite cutoffs. No external independent audit has been performed.
