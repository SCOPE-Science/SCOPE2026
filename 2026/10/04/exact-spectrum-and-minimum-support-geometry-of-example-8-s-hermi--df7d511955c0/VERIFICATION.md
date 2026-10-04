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
with the encoding \(0,1,\omega,\omega^2\mapsto0,1,2,3\). It reconstructs the three Example 8 generators in
\[
(\mathbb F_4[x]/(x^7-1))^3
\]
and all seven simultaneous cyclic shifts, obtaining rank \(14\).

It computes an ordinary nullspace and conjugates it coordinatewise to obtain the Hermitian dual, verifying the Hermitian orthogonality equations and rank \(7\). All \(4^7=16384\) dual codewords are enumerated, and every coefficient of the packaged weight distribution is checked.

The Hermitian Gram matrix of the dual basis has rank \(6\). The verifier checks the explicit hull generator and hull dimension \(1\).

Finally, all weight-\(11\) supports are canonicalized. The replay checks exactly \(357\) minimum words, \(119\) distinct supports, exactly \(17\) simultaneous-shift orbits of size \(7\), and the complete three-block support-pattern histogram. Successful replay prints `VERIFY_OK`.
