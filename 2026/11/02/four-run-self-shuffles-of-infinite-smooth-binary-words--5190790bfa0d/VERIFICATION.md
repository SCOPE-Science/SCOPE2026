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

The certificate and checker are supplied as `four_run_witnesses.tsv`, `four_run_lower_bound.tsv`, and `verify_four_run.py`. Run `python3 verify_four_run.py` with Python 3.10 or later from the directory containing the files; only the standard library is needed. `verification_output.txt` gives the actual successful output.

The checker independently constructs the complete finite smooth language through length \(44\) by two mechanisms (finite-derivative inverse images and right extension with direct repeated differentiation). It verifies that the positive certificate contains every smooth even-Parikh word at lengths \(38\), \(40\), \(42\), and \(44\), with no duplicate or spurious word. It directly compares both induced subwords and maximum color-run lengths. It separately exhausts all shorter-run color assignments for twelve explicit obstruction words, checking the minimal four-length window and the existence of an obstruction to three-run coloring at length \(38\).

The infinite conclusion is justified by the written proof of parity atoms of length at most \(8\), the consequent allowed block-length window, and independent color swapping between consecutive finite self-shuffles. Verification of finite cases alone would not prove the infinite statement. External mathematical validation has not been performed.
