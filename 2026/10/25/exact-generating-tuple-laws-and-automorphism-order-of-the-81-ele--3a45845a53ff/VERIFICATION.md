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
# Verification record

Run `python verify_generating_tuples.py` with Python 3 and no third-party packages. The embedded checker evaluates the original finite operation on all 81 elements. It exhausts every \(81^3\) right-self-distributivity instance, every \(81^2\) elementary condition, and the determinant medial-defect identity for every \(27^4\) projected quadruple. It computes the generated closure of one affine-basis quadruple and one dependent quadruple, confirms that the number of ordered independent triples in the projection is 11232, and independently checks 24564384 generating quadruples and generation probability 416/729. Successful execution prints `VERIFY_OK`.

These checks are exhaustive over the fixed finite 81-element algebra and the fixed polynomial identity's finite field; the universal formula over all positive integers k additionally relies on the rank-counting proof in RESULT.md. Identification with the four-generated free kei uses the published 2006 cardinality theorem, not a regenerated enumeration of every free-quandle relation. No independent audit or validation is claimed.
