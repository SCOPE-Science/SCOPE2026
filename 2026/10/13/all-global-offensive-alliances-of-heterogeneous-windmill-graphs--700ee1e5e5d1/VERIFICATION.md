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

The proof was checked symbolically by separating whether the universal center belongs to the candidate set and computing the two relevant neighbor counts for an omitted blade vertex. The omitted-center inequality was then derived from the blade thresholds by the parity identity \(2\sum_i\lfloor m_i/2\rfloor=M-o\), where \(o\) is the number of odd blade sizes.

The standalone checker `verify_go_windmill.py` constructs each heterogeneous windmill directly and exhaustively tests all subsets for every ordered blade-size tuple with two through four blades, each blade size from one through four, subject to total graph order at most twelve. It verifies the theorem's criterion, the full coefficient vector of the factorized enumerator, the minimum size, and the number of minimum sets.

Replay output:

`VERIFY_OK tuples=269 subset_checks=365080 criterion_checks=365080 coefficient_checks=2798 minimum_checks=538 max_order=12`

The exhaustive computation is finite and does not establish the theorem for arbitrary blade sizes; that infinite scope is supplied by the symbolic neighborhood-count proof.
