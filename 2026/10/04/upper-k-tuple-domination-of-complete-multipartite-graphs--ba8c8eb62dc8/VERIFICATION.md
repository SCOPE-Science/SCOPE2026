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

The theorem was checked in two independent ways within this package.

First, the proof derives the complete-multipartite closed-neighborhood counts directly and uses deletion minimality to obtain a tight witness. The two possible locations of that witness force the universal upper bound, while the largest-part construction supplies equality.

Second, `verify.py` builds every unordered complete-multipartite part profile through order \(10\), forms all closed neighborhoods explicitly, tests every subset against the literal \(k\)-tuple domination definition, tests inclusion-minimality by deletion, and compares the maximum with \(L+k-1\). It separately enumerates every choice of a largest part and every outside \((k-1)\)-set in the stated construction.

Replay with `python3 verify.py` gives:

`VERIFY_OK profiles=128 parameter_checks=697 subset_checks=403280 minimal_sets=24686 construction_checks=19604 max_order=10`

The exhaustive computation is finite and does not prove the infinite theorem by itself. It is a regression check for the general proof. No independent audit or independent validation has been performed.
