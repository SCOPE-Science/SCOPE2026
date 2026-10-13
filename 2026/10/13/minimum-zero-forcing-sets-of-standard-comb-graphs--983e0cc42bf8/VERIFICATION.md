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

The proof for arbitrary \(n\) is the forcing-chain/path-cover argument in `RESULT.md`. The executable check is deliberately finite and serves only to test boundary cases, parity, and the claimed classification.

`verify_comb.py` constructs the standard comb \(C_n=P_n\circ K_1\), implements ordinary zero forcing, and for every \(2\le n\le11\):

- exhaustively rejects every subset smaller than \(\lceil n/2\rceil\);
- exhaustively enumerates every subset of size \(\lceil n/2\rceil\);
- compares the brute-force minimum sets with the stated canonical family union; and
- checks the formulas \(2^m\) for \(n=2m\) and \((3m+4)2^{m-1}\) for \(n=2m+1\).

Replay output:

`VERIFY_OK n_range=2..11 subset_checks=148899 classification_checks=573 count_checks=10 max_order=22`

The computation does not establish novelty and does not extrapolate finite checks into the infinite theorem.
