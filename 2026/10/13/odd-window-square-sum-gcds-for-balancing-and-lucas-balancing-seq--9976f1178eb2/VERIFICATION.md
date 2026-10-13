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

The infinite theorem is established by the proof in `RESULT.md`. The finite program `verify.py` is a regression check only.

It regenerates Pell, associated Pell, balancing, and Lucas-balancing numbers from their recurrences. For every odd \(k\) with \(1\le k\le199\), and a range of starting indices, it verifies the two explicit block identities
\[
\sum_{i=1}^k B_{n+i}^2=\frac{B_kQ_{4n+2k+2}-k}{16},
\qquad
\sum_{i=1}^k C_{n+i}^2=\frac{B_kQ_{4n+2k+2}+k}{2},
\]
and checks that direct finite GCDs stabilize at \(\gcd(B_k,k)\).

The computation does not certify the infinite quantifier. The symbolic proof uses exact Pell identities, the Pell strong-divisibility property on the relevant arithmetic progression, and explicit parity congruences.
