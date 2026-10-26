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

The file `verify.py` is standalone Python 3 and requires only the standard library. Run `python3 verify.py` from the directory containing this file. Its full-subsequence construction iteratively extends a set by both omitting and retaining each input position; it does not use the proposed four-run basis. Every candidate with an observed proper prefix and an absent full word is independently checked against all its one-letter deletions. This gives an exhaustive minimal-absent-subsequence comparison for \(1\le a,b,c,d\le4\), namely 256 quadruples.

Separately, the code checks absence and all immediate-deletion witnesses of the proposed basis for 625 quadruples drawn from run lengths \(\{1,2,3,7,11\}\), and it verifies the exact numbers of five-, six-, and eight-element bases at each total length \(4\le n\le40\) by enumerating all positive compositions of the length.

Expected stdout: `VERIFY_OK exhaustive_quadruples=256 long_witness_checks=625 composition_lengths=4..40`.

The checks are finite. They neither prove the universal four-parameter theorem nor independently establish originality. The paper-style exhaustive run-case proof in `RESULT.md` is the infinite proof. No external audit was performed.
