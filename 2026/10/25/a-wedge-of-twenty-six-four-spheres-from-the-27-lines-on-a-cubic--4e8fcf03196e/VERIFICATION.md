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

# Reproduction and scope

Run `python3 verify.py` using the standard Python 3 interpreter with assertions enabled. No third-party modules or network access are required. The program builds the exact intersection-derived 27-vertex graph; verifies the graph parameters; enumerates every clique; enumerates each face-incidence relation; constructs the precise lowest-available-vertex acyclic matching; and topologically sorts the entire directed Hasse graph. The successful output recorded in `verify_output.txt` was produced by executing the included `verify.py` from this package.

The mathematical implication from the 27-line intersection classes to this graph is given in `RESULT.md`; it is not asserted solely on the basis of program logs. The independent mod-two boundary rank check returns \(26,190,530,550,72\). The complete finite face and Hasse enumeration is exhaustive for this fixed 27-vertex object. The acyclicity certificate proves the existence of a CW model with the stated cells and hence the homotopy type; it does not compute equivariant homology or claim a result for any larger untested family.

External independent audit has not been performed.
