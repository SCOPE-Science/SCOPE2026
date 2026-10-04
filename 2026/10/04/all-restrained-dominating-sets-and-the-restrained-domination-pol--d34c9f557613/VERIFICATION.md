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

The proof is symbolic and does not depend on finite enumeration. A standalone standard-library checker nevertheless tests the two critical finite interfaces independently: the extremal-prefix/suffix characterization versus the definition of restrained domination, and the resulting coefficient formula versus brute-force subset counts.

The checked family consists of every canonical chain graph with \(1\le p\le4\), every twin-class size in \(\{1,2,3\}\), and total order at most \(11\). It contains 540 class-size profiles and 687,124 vertex subsets. The exact replay command is `python3 verify.py`.

Observed output:

`VERIFY_OK profiles=540 subsets=687124 classification_checks=687124 coefficient_checks=5836 max_order=11`

The computation is only a bounded stress test. It does not prove the infinite theorem, establish bibliographic originality, or assess cases outside the stated connected-chain-graph domain.
