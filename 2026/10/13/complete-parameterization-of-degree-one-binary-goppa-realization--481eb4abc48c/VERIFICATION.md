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

It implements \(\mathbb F_{2^M}\) for \(M=2,3,4\), including inversion. Three parity-check systems are tested: the binary \([3,1,3]\) repetition code, the \([7,4,3]\) Hamming code, and a \([6,3,3]\) shortened Hamming code.

For each fully replayed extension degree, every ordered independent image of a syndrome-space basis and every field anchor are enumerated. The verifier constructs
\[
\alpha_i=\beta+\psi(e_i+C)^{-1}
\]
and checks directly that all support points are distinct, avoid the anchor, and define exactly the same binary kernel as the original parity-check matrix.

The exact census is compared with
\[
2^M\prod_{j=0}^{s-1}(2^M-2^j).
\]
The two distinct redundancy-three codes each have exactly
\[
8\cdot7\cdot6\cdot4=1344
\]
anchored ordered realizations over \(\mathbb F_8\).

Successful replay prints `VERIFY_OK`.
