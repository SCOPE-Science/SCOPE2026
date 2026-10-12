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

The verifier constructs the lower-bound family for \(1\le k\le4\) and \(k\le n\le10\). It carries an explicit label on every output position identifying which copy of the root supplied that symbol, then checks that the two labeled subsequences are identical to the claimed root.

For every constructed word, the verifier computes the zero-run vector and applies the inverse formulas
\[
p_i=\frac{g_{2i}+g_{2i+1}}2,
\qquad
c_i=\frac{g_{2i}-g_{2i+1}}2,
\qquad
p_k=\frac{g_{2k}}2.
\]
It confirms exact parameter recovery, output injectivity, and the count \(\binom{n+k}{2k}\).

Independently, it brute-forces the shuffle-square property for every binary fixed-weight word through total length \(10\), reproducing the published rows
\[
(1,1),\ (1,4,1),\ (1,10,10,1),\ (1,19,42,19,1),\ (1,31,128,128,31,1).
\]

These finite checks validate the construction and implementation. The general lower bound, upper bound, and \(\Theta_k(n^{2k})\) conclusion follow symbolically from `RESULT.md`; no infinite claim is inferred from the finite tests.
