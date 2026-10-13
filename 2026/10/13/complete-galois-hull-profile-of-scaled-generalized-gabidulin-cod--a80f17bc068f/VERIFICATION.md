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
The symbolic proof uses the scaled trace-self-dual correlation identity from Lemma 4.1 of arXiv:2605.20109v1 and the invertibility of \(s\) modulo \(N=2m\).

`artifacts/verify.py` independently checks the finite combinatorial consequences of that identity for every even \(N\le40\), every unit \(s\pmod N\), every \(1\le k\le N/2\), and every Galois twist \(e\). It verifies that the proposed \(N-k\) consecutive Moore indices are exactly the right and left orthogonal complements with shifts \(-t\) and \(t\), and that both hull sizes equal
\[
\min\{k,\min(t,N-t)\},\qquad t\equiv es^{-1}\pmod N.
\]

The same script implements \(\mathbb F_9=\mathbb F_3[w]/(w^2+1)\) and checks the explicit scaled trace-self-dual basis from the source example, including the zero correlation pattern and the Euclidean/Hermitian hull endpoints.

These finite checks do not certify arbitrary field sizes. The all-parameter claim is proved by the Moore-basis and cyclic-pairing argument in `RESULT.md`. Successful replay prints `VERIFY_OK`.
