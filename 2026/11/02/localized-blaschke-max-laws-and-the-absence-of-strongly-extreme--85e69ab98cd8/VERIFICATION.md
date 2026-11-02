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

# Verification of the analytical theorem

The complete argument is contained in `RESULT.md` and requires no external computations or unverifiable certificate. The essential equalities were checked directly:

1. For normalized Poisson harmonic measure, the centered quadratic form is \(\Phi_f(z)=\int|f-\mathcal P f(z)|^2d\omega_z\); hence its square root obeys the reverse and forward triangle inequalities.
2. At every simultaneous non-tangential Lebesgue point of \(f\) and \(|f|^2\), \(\Phi_f(z)\to0\). This is applicable because all \(\mathrm{BMO}\) boundary data under discussion are in \(L^2\).
3. For the disk automorphism \(b_a\), the exact expression \(\Phi_{b_a-a}(z)=1-|b_a(z)|^2\) follows from unimodular boundary values, and its value at \(z=a\) is exactly one.
4. Inverting \(w=b_r(z)\) yields \(z=(r-w)/(1-rw)\) and the exact identity for \(1-|z|^2\); the pseudohyperbolic disk \(|w|<t<1\) lies in a fixed Stolz cone and shrinks to the specified boundary point.
5. The peak disk and its complement yield, for every fixed \(t\in(0,1)\), a limsup bounded by \(\max\{|c|,\|f\|_G+|c|\sqrt{1-t^2}\}\). Sending \(t\to1\) and applying the two independent lower-bound tests proves the formula.
6. Each perturbation \(b_a-a\) is rational, holomorphic across the closed disk, vanishes at zero and belongs to \(\mathrm{VMOA}\), validating all four corollaries.

No use is made of numerical sampling as a substitute for an infinite-dimensional proof. The statement fixes the perturbation scalar before taking the limit. No independent scientific audit has been performed.
