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

# Verification

The unrestricted claim is proved by occurrence-residue and interval arguments in `RESULT.md`, including short and long factors and both boundary regimes. No computer calculation is required in the general proof.

Run `python3 check.py` from the directory containing the supplied files to reproduce `check_output.txt`. The checker enumerates all distinct nonempty factors, unions their occurrence-position masks, and tests every one-per-letter set against these masks. It independently checks the classification and counts for all \(2\le q\le6\), \(1\le m\le4\), and \(0\le r<q\): 80 parameter cells, 71,426 position sets, and 4,400 cumulative distinct factors. This is finite corroboration, not an exhaustive check of infinitely many inputs.

Mathematical premises and normalization: zero-indexed positions; each period contains each symbol once; factors are contiguous and may occur at overlapping positions; every individual letter requires one selected position. The source's first public date is the first arXiv submission date, not its later revision date. No external independent review was performed.
