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

The proof in `RESULT.md` is unrestricted.

The attached `verify.py` checks every integer
\[
2\le n\le2{,}000{,}000.
\]
It computes \(\sigma(n)\), \(\varphi(n+2)\), and primality by exact integer sieves.

For each input it compares direct evaluation of
\[
\sigma(n)-\varphi(n+2)<5
\]
with the theorem's predicate:
either \(n\) and \(n+2\) are both prime, or
\[
n\in\{2,7,9,23\}.
\]

It also checks the exact exceptional values
\[
1,\ 2,\ 3,\ 4
\]
at those four inputs and the sharp boundary value \(5\) at \(n=4\).

The finite replay is corroborative only. Exhaustiveness follows from the divisor-excess and cototient bounds in the proof.
