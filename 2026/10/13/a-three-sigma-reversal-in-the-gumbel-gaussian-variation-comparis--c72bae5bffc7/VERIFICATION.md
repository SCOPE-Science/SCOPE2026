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

For the standardized Gumbel law, the exact central probability used in the proof is
\[
C_G(c)=\exp\!\left(-e^{-\gamma-ac}\right)-\exp\!\left(-e^{-\gamma+ac}\right),
\qquad a=\frac{\pi}{\sqrt6}.
\]
The analytic certificate for every \(c\ge3\) is the comparison
\[
T_G(c)>\frac{x_c}{1+x_c},
\qquad
T_N(c)<\frac{2\varphi(c)}{c},
\qquad
x_c=e^{-\gamma-ac},
\]
together with strict monotonicity of
\[
R(c)=\frac{c x_c}{2(1+x_c)\varphi(c)}.
\]
The proof certifies \(R(3)>1\) by elementary rational/exponential bounds and then proves \((\log R)'(c)>0\) for all \(c\ge3\).

The standalone script `verify_gumbel_radius_reversal.py` independently evaluates the original exact CDF formulas and the comparison ratio. It checks the published radius-one sign, the reversed sign at several radii at least three, deterministic-mesh monotonicity of the analytic lower-bound ratio, and a non-theorem numerical crossover locator. Its output is:
`VERIFY_OK root_locator=2.055935618225228 R3=4.005361355853`.

The numerical mesh and locator do not prove the infinite-radius statement, uniqueness of a crossover, or the tail equivalent. Those conclusions used in the accepted claim come from the analytic argument only.
