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

# Verification of the involution comparison theorem

The standalone `adaptive_certificates.json` gives complete binary trees for every order from two through ten. The generator enumerates involutions via a least-remaining-element recursion and tests all possible query splits of hypothesis-bitsets. This search finds a witnessing tree; no failed search is needed for any claimed upper bound because concept cardinalities give all upper bounds.

The independent verifier reconstructs involutions by adding the largest element as a fixed point or as one endpoint of a transposition. For each certificate it checks the involution count, the number of tree nodes and leaf witnesses, distinctness of the witnesses, all path comparisons, and \(2^d\le I_n<2^{d+1}\). It also verifies all adjacent-descent patterns by the reverse-block construction for every order through ten.

Reproduction: execute `python3 verify_certificates.py` beside `adaptive_certificates.json`. The verifier uses only the Python standard library. The recorded final result is `ALL_INDEPENDENT_CHECKS_PASS`.

The all-order VC and block-amplification arguments are mathematical deductions stated in `RESULT.md`; running finite software does not by itself prove the unbounded assertion. No independent scientific audit is claimed.
