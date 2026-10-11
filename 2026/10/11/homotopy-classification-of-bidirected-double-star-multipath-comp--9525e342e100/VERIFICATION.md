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

# Reproduction and mathematical limits

Run `python3 verify.py` with a standard Python 3 interpreter. The script generates all faces of each bidirected double-star multipath complex for every unordered parameter pair \(1\leq a\leq b\leq6\), checks the two central-arrow links, and calculates boundary ranks with incidence signs over three prime fields. It prints a `VERIFY_OK` terminator after all assertions succeed.

The script directly evaluates 21 parameter pairs and three coefficient fields. It confirms finite Betti numbers, not homotopy equivalence or torsion-freeness over all integer parameters. The formal homotopy proof uses the crown graphs of bidirected stars, the join decomposition after deleting the two central arrows, null-homotopic cone attachments, and a separate homotopy-equivalent link inclusion at \((a,b)=(2,2)\).

The stated status records only an internal same-model review of the written proof and the reproduced finite checks; no independent mathematical audit or external certification has been performed.
