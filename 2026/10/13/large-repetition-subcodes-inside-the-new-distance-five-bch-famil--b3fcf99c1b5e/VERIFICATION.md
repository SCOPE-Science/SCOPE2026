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

It independently constructs \(\mathbb F_{16}\) with modulus \(X^4+X+1\) and \(\mathbb F_{256}\) with modulus \(X^8+X^4+X^3+X+1\). Every nonzero field element is checked to satisfy the expected multiplicative group order.

For the first source pattern, all exact order-five elements are found and the sums
\[
1+\omega+\omega^2+\omega^3+\omega^4
\]
and
\[
1+\omega^3+\omega^6+\omega^9+\omega^{12}
\]
are checked directly.

For the second pattern, every element of exact order \(51\) is tested against
\[
E=\{0,3,21,33,44\}.
\]
The replay finds exactly eight elements satisfying both
\[
\sum_{e\in E}\theta^e=0
\]
and
\[
\sum_{e\in E}\theta^{3e}=0.
\]
This independently certifies existence of the finite-field pattern used in the proof.

The script then verifies the divisibility cases and disjoint-support construction for every integer \(2\le s\le200\), and checks the direct-sum weight enumerator exactly for representative cases. The finite range is a stress test only; the all-\(s\) argument is the algebraic proof in `RESULT.md`.

Successful replay prints `VERIFY_OK`.
