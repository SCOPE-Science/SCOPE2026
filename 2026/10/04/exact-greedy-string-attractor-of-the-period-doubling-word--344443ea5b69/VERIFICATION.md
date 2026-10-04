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

Run `python3 verify.py`.

The checker independently reconstructs the period-doubling word from \(\mu(1)=10\) and \(\mu(0)=11\). For each prefix length through \(128\), it enumerates all distinct factors together with the union of positions covered by all their occurrences and directly executes the greedy definition. The selected endpoints are exactly \(0,1,3,7,15,31,63,127\).

It also reconstructs \(P_k=\mu^k(1)\) and \(Q_k=\mu^k(0)\) for thirteen levels, checks that the two blocks agree except in the last bit, and checks by direct occurrence enumeration that \(Q_k\) appears exactly once in \(P_kQ_k\), at the suffix position used in the proof.

These finite checks support but do not replace the all-length induction. No assertion for arbitrarily long prefixes is inferred solely from the finite replay.
