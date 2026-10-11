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

Run `python3 verify.py` from the directory containing the standalone program. Only the Python 3 standard library is required.

The program constructs each grid's vertex permutations, induced connected three-vertex sets and unit squares directly. For all integer orders \(3\le n\le12\), it calculates the signed traces of invariant paths and squares under the five dihedral class representatives; it checks the resulting closed character values, multiplicity integrality, nonnegativity and dimension equality.

A separate verification for \(n=3\) and \(n=4\) constructs the ordinary three-cut complex from the defining disconnected triples, enumerates every face, computes the induced orientation sign on each fixed face, and sums reduced chain traces. Thus these checks do not rely on the general complement-face formula.

The run terminates with `VERIFY_OK` when all checks pass. Finite enumeration does not prove the infinite-family statement, prove the literature search exhaustive, or supply independent audit. The written proof uses the already published all-grid shellability theorem and symbolic counts valid for every \(n\ge3\).
