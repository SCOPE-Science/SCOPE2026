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

# Reproducing the exact certificate

Run `python3 verify.py` using Python 3.8 or later. The expected deterministic output is `check_output.txt`. The checker visits all \(21\) two-column index pairs and all seven positive-frequency rows, in both prime fields of orders \(31\) and \(61\). Each field contains a verified primitive fifteenth root and is used only for the logically sound one-way implication from a complex zero determinant to a finite-field zero determinant.

For the \(21\) column pairs, the calculated upper bound on the number of zero positive-frequency rows has histogram \(\{1:8,2:12,4:1\}\). The only four-zero possibility uses columns \(\{3,6\}\); its zero row is \(5\) and its two nonzero row-direction classes are \(\{1,4,6\}\) and \(\{2,3,7\}\). The proof in `RESULT.md` explicitly constructs the two complex coefficient vectors realizing these classes and proves that all other candidates are excluded.

This finite proof certifies the fifteen-cycle statement only. The code does not infer nonvanishing of a complex minor from a finite-field zero, and it does not treat an unexecuted experiment as evidence. Independent audit and external validation have not been performed.
