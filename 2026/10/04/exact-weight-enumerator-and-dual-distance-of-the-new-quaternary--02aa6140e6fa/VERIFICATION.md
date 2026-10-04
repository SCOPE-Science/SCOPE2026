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
`artifacts/verify.py` uses only the Python standard library and exact arithmetic in \(\mathbb F_4\).

The verifier reconstructs the \(10\times22\) matrix from the public source, checks row rank \(10\), and checks rank \(10\) of the Hermitian Gram matrix \(G\overline{G}^{\,T}\). It then enumerates all \(4^{10}=1{,}048{,}576\) messages and reproduces every coefficient of the stated Hamming weight enumerator.

For the dual-distance claim it tests all \(\binom{22}{6}=74{,}613\) six-column subsets and verifies that each has rank \(6\). It then exhausts all \(\binom{22}{7}=170{,}544\) seven-column subsets, finds exactly \(88\) of rank \(6\), and confirms the stored witness. Since every six-subset is independent, each dependent seven-set is a circuit and contributes exactly three scalar-multiple dual words. A separate MacWilliams calculation checks \(A_7(C'^\perp)=264\). The orthogonal-array strength follows from the verified surjectivity of every six-coordinate projection.
