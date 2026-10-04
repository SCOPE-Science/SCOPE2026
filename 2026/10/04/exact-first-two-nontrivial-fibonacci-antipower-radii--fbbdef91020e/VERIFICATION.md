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

Run `python3 verify.py` in the same directory as `certificate.json`.

The checker regenerates the Fibonacci fixed point from \(0\mapsto01\), \(1\mapsto0\). For \(k=3\), it reconstructs \(19\) distinct length-\(18\) factors; for \(k=4\), it reconstructs \(41\) distinct length-\(40\) factors. Since the Fibonacci word is Sturmian, these counts equal the known total numbers \(18+1\) and \(40+1\), so the finite lists are exhaustive.

For every certified factor the checker tests all relevant block lengths exactly and recomputes the minimum. It verifies the distributions
\[
2:8,\ 3:4,\ 4:1,\ 5:2,\ 6:4
\]
for \(k=3\), and
\[
3:4,\ 4:2,\ 5:4,\ 6:27,\ 7:2,\ 9:1,\ 10:1
\]
for \(k=4\). It also checks the sharp witnesses beginning at zero-based indices \(3\) and \(21\).

The computation does not independently prove that the Fibonacci word is Sturmian; that standard theorem is taken from the cited literature. Independent audit has not been performed.
