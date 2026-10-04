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
The proof of the all-\(k\) theorem is symbolic and is contained in `RESULT.md`.

For regression against the published finite data, run
`python3 verify.py`.

The checker constructs the semigroup
\[
S_k=\langle n^k-1:n\ge2\rangle
\]
for every \(2\le k\le9\) far enough to certify a full conductor block after the published Frobenius number. It reproduces the published \(a_k\) and \(b_k\), constructs
\[
T_k=\left\langle2^k-1,\frac{u^k-1}{2}:u\ge3\text{ odd}\right\rangle,
\]
and verifies
\[
a_k=(2^k-1)+2F(T_k),
\qquad
b_k=2g(T_k)+2^{k-1}-1.
\]

A successful replay prints `VERIFY_OK`.

The finite replay is not used as evidence for arbitrary \(k\). The infinite quantifier is discharged only by the exact generator reduction, cofinite-semigroup argument, and complete parity classification of gaps in `RESULT.md`.
