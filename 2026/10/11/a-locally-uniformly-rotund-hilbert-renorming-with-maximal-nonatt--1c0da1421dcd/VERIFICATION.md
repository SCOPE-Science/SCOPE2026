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
The support-functional identity in a real \(\ell_p^2\) block is
\[
j_p(u_p)(v_p)=0,
\]
while the reverse evaluation is exactly
\[
r_p=\frac{t_p-t_p^{(p-1)^2}}{(1+t_p^p)^{1/p}(1+t_p^{p(p-1)})^{(p-1)/p}}.
\]
For square exponents \(p\) the checker uses rational \(t_p=1-1/\sqrt p\), verifies the exact cancellation and the exact rational inequality \(0<r_p^p<1\), and then separately checks numerical normalization, dual support exchange and asymptotic behavior. It checks the coordinate \(\ell_p\)-to-Hilbert comparison at additional exponents.

The infinite-dimensional theorem does not follow from finite sampling. Its analytic verification is: (i) the \(\ell_2\)-sum is LUR because norms of coordinate magnitudes converge in \(\ell_2\), fixed-coordinate midpoint deficits vanish, and finite-dimensional strict convexity gives coordinate convergence; (ii) LUR forces the pointwise left and right approximate symmetry parameters below one, because reverse support values approaching one would force a Birkhoff-orthogonal pair to approach an antipodal or coincident pair; (iii) the explicit support pairing vanishes forward and approaches one in reverse at rate \(p^{-1/2}\); and (iv) strict convexity forbids attainment, while reflexive smooth duality transports the witnesses to the dual.

No independent audit or independent validation has been performed.

For the nonuniform-convexity boundary, the vectors \(2^{-1/p_n}(1,1)\) and \(2^{-1/p_n}(1,-1)\) in the \(n\)-th block have separation \(2^{1-1/p_n}\to2\) and midpoint norm \(2^{-1/p_n}\to1\). Hence the example is LUR but not uniformly convex.
