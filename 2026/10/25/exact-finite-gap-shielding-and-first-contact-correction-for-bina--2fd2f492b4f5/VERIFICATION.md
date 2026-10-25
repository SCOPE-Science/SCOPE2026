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

Run `python3 verify.py` using an ordinary Python 3 interpreter. Its exact-rational two-state digit automaton computes all probabilities of at most \(r\) carries for 264 configurations of Hamming weights \(1\) through \(8\), including all gap profiles in selected finite grids. It checks each layer against the closed negative-binomial and first-contact formula. A logically distinct finite residue-class tally tests representative configurations directly from binary digit sums. Successful execution prints `VERIFY_OK`.

The complete infinite theorem is established by the coefficient-wise matrix decomposition in `RESULT.md`, not by the finite tests. No independent external certification has occurred. Probabilities beyond the stated low-carry range are not claimed.
