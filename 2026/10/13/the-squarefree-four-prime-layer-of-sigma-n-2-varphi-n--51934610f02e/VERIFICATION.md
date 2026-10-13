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

The proof in `RESULT.md` is an exact finite reduction from an unbounded prime domain.

The attached `verify.py` uses only integer and rational arithmetic. It reconstructs all ordered prime quadruples \(p<q<r<s\) satisfying
\[
\prod_{t\in\{p,q,r,s\}}\frac{t+1}{t-1}=2
\]
by applying the same monotonic branch bounds as the proof. It then evaluates
\[
s=\frac{2+A}{2-A},
\qquad
A=\frac{p+1}{p-1}\frac{q+1}{q-1}\frac{r+1}{r-1},
\]
checks integrality and primality, and verifies the defining \(\sigma\)-\(\varphi\) equality for every survivor.

The replay is expected to return exactly eight ordered prime quadruples:
\[
(5,11,23,109),
(5,13,17,127),
(5,13,19,71),
(5,13,23,43),
\]
\[
(5,13,29,31),
(5,17,19,31),
(7,11,13,29),
(7,11,17,19).
\]

The script also checks the exact finite candidate count of fifteen triples. No bounded search over \(n\) is used to infer the theorem.
