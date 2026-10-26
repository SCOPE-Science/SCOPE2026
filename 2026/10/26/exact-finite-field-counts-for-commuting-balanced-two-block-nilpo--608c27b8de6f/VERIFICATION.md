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

The standalone source `check_two_block_commuters.py` uses exact finite-field modular operations and is run using `python3 check_two_block_commuters.py`. Its expected completion marker is `TWO_BLOCK_COUNT_OK`.

Checks actually executed: 40 exhaustive invertible two-by-two matrix enumeration cases over the prime fields of orders \(2,3,5,7,11\), each with exponents \(3,4,5,6,7,8,12,15\). Every computed number of matrices with \((H^n)_{11}=0\) agrees with the closed two-by-two formula. Independently, direct exhaustive enumeration of full nilpotent commuting endomorphisms with exact matrix-rank and power tests gave \((n,q,\mathrm{total},\mathrm{matching})=(3,2,256,16),(3,3,6561,648),(4,2,4096,256)\), agreeing with the main formula.

The general theorem is proved symbolically from the module decomposition and the two-by-two similarity-class classification. The tests do not constitute exhaustive proof for all prime powers or all dimensions. No independent audit has been performed.
