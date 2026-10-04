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

It reconstructs the six Example 6.1 polynomials over \(\mathbb F_5\), takes all cyclic shifts modulo \(x^8-1\), and row-reduces the resulting length-\(16\) vectors. It verifies
\[
\dim C=\dim D=8
\]
and
\[
\dim(C+D)=16.
\]

The exact modular nullspace of the generator matrix of \(D\) gives a basis of \(D^\perp\). The verifier exhausts all \(5^8=390625\) words in \(C\) and all \(5^8\) words in \(D^\perp\), computes both Hamming histograms, and checks byte-for-byte equality with the embedded certificate.

It separately counts ordered symbol compositions. At minimum weight it verifies \(704\) words on each side, \(48\) distinct composition types for \(C\), \(20\) for \(D^\perp\), and specifically
\[
N_C(9,0,0,1,6)=8,\qquad N_{D^\perp}(9,0,0,1,6)=0.
\]
It also verifies membership of the displayed witness word in \(C\).

Successful replay prints `VERIFY_OK`.
