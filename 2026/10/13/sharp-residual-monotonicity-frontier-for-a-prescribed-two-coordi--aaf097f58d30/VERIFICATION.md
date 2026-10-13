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
The universal proof is analytic. This file records the finite replay checks.

For the prescribed order \(1\to2\), the squared worst residual amplification at condition number \(\kappa\) and orientation parameter \(u\ge0\) is
\[
\Phi_\kappa(u)
=
\frac{(\kappa-1)^2u}{(\kappa+u)^2}
\left(
1+\frac{(\kappa-1)^2u}{(1+\kappa u)^2}
\right).
\]

The frontier polynomial is
\[
P(\kappa)
=
32\kappa^6
-131\kappa^5
-144\kappa^4
-362\kappa^3
-144\kappa^2
-131\kappa
+32.
\]
Its unique root above one is
\[
\kappa_*=5.36076789614546\ldots.
\]
The reciprocal reduction uses
\[
x=\kappa+\kappa^{-1}
\]
and
\[
Q(x)=32x^3-131x^2-240x-100.
\]

The embedded `verify.py` uses only the Python standard library to:

1. isolate the unique root of \(Q\) above \(2\);
2. recover \(\kappa_*\) from that root and check \(P(\kappa_*)\);
3. numerically maximize \(\Phi_\kappa\) at values just below and above the frontier;
4. replay exactly the \(\kappa=6\) witness
\[
A=
\begin{pmatrix}
5&2\\
2&2
\end{pmatrix},
\qquad
r^-=(2,-5)^{\mathsf T},
\qquad
r^+=(29/5,0)^{\mathsf T}.
\]

The resultant factorization and one-positive-stationary-point argument are part of the analytic proof in `RESULT.md`; the numerical maximization here is corroborative, not exhaustive.

Unproved limits include best-order selection, dimensions above two, randomized or symmetric variants, SOR, asynchronous updates, and finite precision.
