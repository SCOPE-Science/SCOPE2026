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

# Reproducibility and verification

The extracted standalone file `checker.py` requires Python 3 and only the standard library. Run `python3 checker.py`. It compares the exact combinatorial mass \(L(\sigma)=\prod_{j}\ell_j(\sigma)\), all rising adjacent swaps through \(n=8\), the factorization formula, sharp envelopes, and extremizing witnesses at every position. Exact normalization is checked by summing masses, not by floating-point approximations. A separate direct simulator enumerates all preference tuples for \(2\le n\le5\), performs the actual parking process, and checks the complete output-permutation preimage count. The observed result is `PASS: 475272 exact assertions; independent preference enumeration through n=5`.

General validity for all \(n\ge2\) comes from the proof in `RESULT.md`, not from testing finitely many values. No symbolic proof assistant or outside certification is claimed. The mathematical record has undergone self-review only. The literature evidence is substantive but not a proof of absolute historical priority.
