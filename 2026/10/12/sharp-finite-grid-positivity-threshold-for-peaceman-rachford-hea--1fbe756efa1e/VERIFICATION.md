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

The proof is symbolic. For \(I+sT_k\), leading principal determinants satisfy the stated second-order recurrence, and the inverse cofactor formula yields positive off-diagonal entries and diagonal entries \(D_{i-1}D_{k-i}/D_k\). The quotient recurrence for \(q_j=D_j/D_{j-1}\) proves endpoint minimality. Differentiating the endpoint resolvent entry proves the threshold is unique. The limiting quotient is the larger root of its scalar fixed-point equation, giving \(2-\sqrt2\).

The bundled `verify.py` uses only exact rational arithmetic for the \(2\times2\) witnesses. It verifies
\[
C_2(3/5)=\frac1{56}\begin{pmatrix}-1&15\\15&-1\end{pmatrix}
\]
and the negative tensor entry \(-15/3136\), together with the strictly positive factor at \(s=11/20\). It also checks determinant identities and representative numerical threshold monotonicity for several dimensions. These finite checks support implementation reproducibility; they are not substituted for the analytic proof of the all-dimension theorem or the limit.

No independent audit has been performed.
