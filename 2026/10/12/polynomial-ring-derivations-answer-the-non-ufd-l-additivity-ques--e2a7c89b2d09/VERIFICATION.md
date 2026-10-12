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
Run `python3 verify.py`.

The checker uses the explicit coefficient ring
\[
\mathbb Z[\sqrt{-5}]
\]
represented exactly by integer pairs. It verifies the identity
\[
6=2\cdot3=(1+\sqrt{-5})(1-\sqrt{-5}),
\]
the norms of the four irreducible factors, the absence of elements of norm \(2\) and \(3\), and the unit calculation at norm \(1\).

It then checks the formal product rule over a deterministic finite family of low-degree polynomials with coefficients in that ring.

These checks are regression evidence. The universal theorem is proved in `RESULT.md` from Hilbert's basis theorem, Noetherian atomicity, the degree formula in a polynomial ring over a domain, and the formal product rule. No finite enumeration is used to infer the infinite statement.

A successful replay prints `VERIFY_OK`.
