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

The exact identity \(D\nu(e_z)=(\beta^2/r_i)e_z\) follows from the Hessian and unit normal of the stated obstacle equation at each equatorial collision. The source and its spherical predecessor supply the block Poincaré representation and the identification of logarithmic growth with the normal exponent. No external proof assistant, numerical census, or simulated trajectory is needed.

Write \(Q=\beta^2\) and \(h=Q^{-1}\). Starting at \(U_0=V_0=1\), check the exact recurrence
\[
U_i=U_{i-1}+d_i V_{i-1},\qquad V_i=V_{i-1}+Qa_i U_i.
\]
Elementary division and subtraction give \(0<u_i\le h/a_i\) and \(0\le h/a_i-u_i\le h^2/(a_*^2d_*)\). Next expand the exact log increment and apply \(|\log(1+z)-z|\le z^2/2\) for \(z\ge0\) to obtain the termwise \(3h^2/(a_*^2d_*^2)\) bound. This bound is independent of \(i\) and \(\mu\), so ergodic averaging retains it; the finite initial increment disappears.

An independent constant-coefficient algebraic boundary check: for \(a_i=a\) and \(d_i=d\), the one-step matrix is symplectic with trace \(2+Qad\). Its expanding eigenvalue is \(\frac12(2+Qad+\sqrt{(2+Qad)^2-4})\). Its logarithmic expansion is \(\log(Qad)+2/(Qad)+O(Q^{-2})\), matching the integral expression \(C_1=2/(ad)\). This check tests the first correction; the general proof does not depend on periodicity.

Limits: no numerical data are presented as proof; no independent audit has been performed. The controlled remainder is not claimed optimal; the flattening cutoff is qualitative and depends on a uniform bound for the \(\beta\)-independent planar block. The theorem concerns exponents per reflection, not per unit flow time.
