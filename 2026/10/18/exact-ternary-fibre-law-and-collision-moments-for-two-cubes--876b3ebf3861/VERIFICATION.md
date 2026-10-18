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

# Reproduction and limits

Execute `python3 verify.py` in the directory containing the standalone `verify.py` file. It uses only the Python standard library and exact integer/rational arithmetic. It constructs each cube-residue multiplicity table, performs independent circular convolution for every target modulo \(3^n\) for \(0\le n\le8\), and compares the resulting raw ordered counts with the rationally normalized formula. It checks \(9841\) target residues in total and independently evaluates their exact collision moments. The recursive formula is then checked at depths \(0\) through \(11\), including the small bases \(M_0=M_1=1\), \(M_2=19/9\).

The last numerical check does not prove the infinite recurrence. The general theorem follows from the unit-cube change of variables, the exhaustive unit/nonunit parity-of-sign decomposition, exact mass preservation, and the valuation-annulus argument given in `RESULT.md`. The code does not establish publication originality or independent certification, and no attempt is made to derive global integer solvability from the local statement.
