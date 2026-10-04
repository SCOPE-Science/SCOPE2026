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
The infinite theorem is proved symbolically in `RESULT.md`.

The only finite auxiliary check is `verify.py`. It evaluates the alternating cofactor modulo \(8\) for every pair of odd residue classes and many exponents \(m=4k+1\), and verifies the closed residue formula
\[
B_m(u,v)\equiv1+2k(1-r)\pmod8,
\qquad
r\equiv uv^{-1}\pmod8.
\]
Every checked value is \(1\) or \(5\pmod8\), never \(7\).

This computation is not used to extrapolate an infinite claim. The proof that all \(k\ge1\) are covered is the parity count of even and odd powers of \(r\) in `RESULT.md`.
