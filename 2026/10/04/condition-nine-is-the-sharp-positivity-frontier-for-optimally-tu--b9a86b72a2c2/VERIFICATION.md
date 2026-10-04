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
The verification artifact uses exact rational arithmetic and the Python standard library.

It verifies the first-two-iterate identity for rational Stieltjes examples and checks the optimal heavy-ball threshold at square condition numbers below, at, and above \(9\). The explicit system
\[
A=\operatorname{diag}(1,16),
\qquad
b=(1,1)^{\mathsf T}
\]
is replayed exactly, including the negative second component at iteration two and the positive exact solution.

For diagonal modes the checker verifies the recurrence
\[
e_{k+1}=2qc\,e_k-q^2e_{k-1}
\]
and the closed form
\[
e_k=q^k[U_k(c)-qU_{k-1}(c)]
\]
for many rational values. It checks the high-curvature endpoint formula
\[
e_2=q^2(3+2q)
\]
and its equality value at \(q=1/2\).

The infinite all-iterate positivity statement is proved analytically in RESULT.md from the Chebyshev bound and is not inferred from enumeration.
