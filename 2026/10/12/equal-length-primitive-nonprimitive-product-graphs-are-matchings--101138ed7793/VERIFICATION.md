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

Run `python3 verify.py` beside `certificate.json`.

The checker exhaustively enumerates primitive words and the relation \(pq\) non-primitive for binary lengths through \(9\) and ternary lengths through \(6\). Every finite graph has maximum degree at most \(1\), and each ordered-pair count agrees with
\[
\sum_{\substack{d\mid\ell\\d\ge3,\ d\ {\rm odd}}}
\pi_n\!\left(\frac{2\ell}{d}\right),
\]
with \(\pi_n\) independently computed by Möbius inversion.

A separate finite window checks relation symmetry. The arithmetic inequality used by the Fine--Wilf proof is checked for every distinct odd exponent pair through \(999\).

These computations are consistency checks only; the infinite theorem is the symbolic argument in `RESULT.md`. Independent audit has not been performed.
