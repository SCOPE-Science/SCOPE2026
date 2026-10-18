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

# Verification of the alternating complement-spectrum theorem

Run `python3 check.py` to enumerate independently the selected index sets in \((ab)^n\) and collect **distinct** residual words for every \(0\le k\le n\le10\). The program compares the complete sets, not only their cardinalities, to the proposed bounded-run characterization; it also compares their sizes to the closed binomial sum. The recorded result is in `check_output.txt`.

Run `python3 check_dp.py` to check individual membership by a separate dynamic program that tests whether the alternating source is an interleaving of the proposed deleted word and a candidate complement. This procedure does not enumerate deletion-position combinations. It covers \(n\le14\), \(r=n-k\le9\), and every domino encoding in the stated range, totaling 7,151 candidate decisions. The recorded result is in `check_dp_output.txt`.

Both programs use only Python's standard library. Their finite execution is a consistency check; the parity and phase-change proof in `RESULT.md` establishes the unrestricted theorem. The tests do not compare every possible unrelated literature source, and independent validation has not been performed.
