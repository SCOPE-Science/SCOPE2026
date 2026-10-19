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

Run `python3 check_zimin.py` with Python 3.9 or later and no third-party packages. It constructs \(Z_k\), scans all substrings directly, assembles **all** absent two-sided extensions of occurring cores, and compares the resulting set to the classification for \(1\le k\le8\). It also compares each dyadic histogram and total to the symbolic formulas. Success ends with `ZIMIN_ANTIDICTIONARY_PASS k=1..8`.

The checker does not cover arbitrary \(k\). The unrestricted theorem is established by the border and right-extension lemmas and induction in `RESULT.md`, not by the finite enumeration. The algorithm operates on expanded words at each test size; its costs are not claimed to be a new compressed-string algorithm. The exact alphabet restriction is explicitly implemented by the enumeration over letters present in each finite word.

Self-review passed for the stated theorem. Independent audit remains unperformed.

