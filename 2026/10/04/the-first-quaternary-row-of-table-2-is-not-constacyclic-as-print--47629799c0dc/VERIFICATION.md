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
`artifacts/verify.py` uses only the Python standard library.

The verifier realizes
\[
\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1)
\]
and performs exact polynomial long division in \(\mathbb F_4[x]\). It checks that neither
\[
1+\omega x+x^2+x^3+x^4
\]
nor its reverse-coefficient reading divides
\[
x^{10}-\omega.
\]

For the natural constant-to-leading reading it also forms the six ordinary unwrapped shifts in length \(10\), checks rank \(6\), and exhausts all \(4096\) linear combinations. The exact minimum distance is \(3\), with weight distribution
\[
1+12z^3+57z^4+246z^5+645z^6+960z^7+1158z^8+798z^9+219z^{10}.
\]
The Hermitian Gram matrix has rank \(6\), so this auxiliary span has hull dimension \(0\).

Successful replay prints `VERIFY_OK`.
