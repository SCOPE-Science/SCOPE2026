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

The proof is analytic for the full parameter interval \(0\le\lambda\le1\). The decisive reduction is
\[
Q_\lambda\longmapsto[-a_\lambda,a_\lambda]\times[-b_\lambda,b_\lambda],
\qquad
a_\lambda=\frac{2-\lambda}{4},\quad b_\lambda=\frac{1+\lambda}{2},
\]
with the lattice
\[
L=\{(m/2,n):m,n\in\mathbb Z,\ m\equiv n\pmod2\}.
\]
For a rectangle \([-a,a]\times[-b,b]\), the row geometry gives exactly
\[
\mu=
\min\left\{
\max\left(\frac1{2a},\frac1{2b}\right),
\max\left(\frac1{4a},\frac1b\right)
\right\}.
\]
Substitution gives the two branches \(2/(2-\lambda)\) and \(2/(1+\lambda)\), whose crossover is exactly \(\lambda=1/2\).

`verify_profile.py` checks the matrix inverse, the exact branch comparisons, symmetry, endpoint values, midpoint value, and representative rational parameters using `fractions.Fraction`. Running it produces `VERIFY_OK`, stored in `verification_output.txt`.

The script is a reproducibility check only. The all-real-parameter claim rests on the analytic row-covering proof, not on finite sampling.
