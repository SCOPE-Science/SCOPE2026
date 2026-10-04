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
# Verification

For \(N_B=J_n+\varepsilon B\), direct expansion gives
\[
N_B^m=J_n^m+\varepsilon\sum_{i=0}^{m-1}J_n^iBJ_n^{m-1-i}.
\]
At \(m=n\), the dual coefficient is \(S(B)\). It commutes with \(J_n\), hence is an upper-triangular Toeplitz polynomial \(c_0I+\cdots+c_{n-1}J_n^{n-1}\). The matrix units \(E_{n,k+1}\) map to \(J_n^k\), so all \(n\) coefficients are independent linear coordinates and every coefficient vector has \(q^{n^2-n}\) preimages.

If all coefficients vanish, the index is \(n\). If \(c_d\) is the first nonzero coefficient, then \(S(B)J_n^j\) remains nonzero through \(j=n-1-d\) and vanishes at \(j=n-d\), giving index \(2n-d\). Counting coefficient vectors yields the stated distribution.

The standalone verifier independently multiplies dual matrices and exhaustively checks \((n,q)=(1,2),(2,2),(3,2),(2,3)\). It prints `VERIFY_OK`. These computations are finite sanity checks only; the proof above establishes the general theorem.
