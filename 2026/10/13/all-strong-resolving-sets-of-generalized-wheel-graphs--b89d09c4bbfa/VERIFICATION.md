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

The proof is all-orders and is not inferred from computation. Its critical steps are: mutually-maximally-distant center pairs force at most one omitted center; for rim order at least four, nonadjacent rim pairs force the omitted rim set to be either empty, a singleton, or one cycle edge; and explicit shortest paths resolve every pair left by those omission patterns. The triangular rim is checked separately, including the complete graph \(W_{1,3}\cong K_4\).

The standalone checker computes graph distances and the definition of strong resolution directly. For every \(1\le m\le4\) and \(3\le n\le7\), it exhausts all vertex subsets, compares them with the structural criterion, compares all polynomial coefficients, and checks the minimum size and basis count. Its expected replay line is:

`VERIFY_OK pairs=20 subset_checks=7440 classification_checks=7440 coefficient_checks=170 minimum_checks=20 max_order=11`

The finite range is a stress test only. No statement beyond generalized wheels is certified, and no independent audit has been performed.
