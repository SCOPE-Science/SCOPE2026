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

The standard-library `checker.py` independently constructs the Cantor substitution prefixes, enumerates scattered-`01` factor profiles using a rolling update, and compares their sets with the arithmetic formula for each integer \(k\in[1,7]\). It also checks the closed collision witness construction at each integer \(k\in[3,7]\), comparing literal words and full multiplicity-determining profile pairs. Run `python3 checker.py` from this directory.

Observed output: `PASS: all ternary-length profiles k=1..7; exact overlap sum; linear nonidentical collision families k=3..7` and profile cardinalities `5,17,50,154,466,1402,4210`.

The checker does not certify infinitely many levels; that conclusion uses the explicit proof in `RESULT.md`. No other data, network service, compiler, or downloaded file is required.
