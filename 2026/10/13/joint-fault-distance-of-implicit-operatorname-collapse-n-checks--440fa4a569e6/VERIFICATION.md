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

The universal theorem is proved analytically in `RESULT.md`.

For each patch fault string \(x\), define the domain-wall string
\[
s_j=x_j\oplus x_{j+1}.
\]
The source's implicit check compares the reported root sign with the reported sign of \(LS_j\). Therefore acceptance is exactly
\[
e_j\oplus e_0=s_j.
\]

For wrong inferred root sign, \(e_0=1\), and an accepted pattern has total fault weight
\[
|x|+n-T(x),
\]
where \(T(x)\) is the number of domain walls. Since
\[
T(x)\le2|x|
\quad\text{and}\quad
T(x)\le n-1,
\]
one gets
\[
T(x)-|x|
\le
\left\lfloor\frac{n-1}{2}\right\rfloor.
\]
The alternating string attains equality, proving the exact distance
\[
\left\lfloor\frac n2\right\rfloor+1.
\]

The stochastic law is the exact transfer-matrix generating function
\[
G_n(r;q)
=
(1-q,q)
\begin{pmatrix}
1-q & qr\\
(1-q)r & q
\end{pmatrix}^{n-1}
\binom11.
\]

The bundled checker exhaustively replays finite cases only as a transcription check. It confirms the deterministic distances for \(2\le n\le10\), matches direct rational probability summation to the transfer matrix, and verifies the independent multi-patch parity formula. These finite checks are not used to infer the all-\(n\) proof.

Limits: this is an effective premeasurement \(X\)-fault plus readout-flip model, not a complete circuit-level noise analysis.
