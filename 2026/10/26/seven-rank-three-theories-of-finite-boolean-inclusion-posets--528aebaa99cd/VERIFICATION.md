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

The attached `verify.py` is self-contained and uses only Python's standard library. `verification_output.txt` records its completed run, with exact rank-three Venn types through nine atoms and independent raw-subset enumeration through seven atoms. It records 25,090 memoized Venn states, an independent agreement of pairwise type equivalences on the common finite domain, and 4,404 local splitting checks. The infinite equivalence above eight atoms is established by the symbolic Ehrenfeucht–Fraïssé proof in `RESULT.md`, not by experiment. The finite recursion supplies exhaustive exact existence/nonexistence checks for the seven classes and is reproducible on a normal Python installation.
