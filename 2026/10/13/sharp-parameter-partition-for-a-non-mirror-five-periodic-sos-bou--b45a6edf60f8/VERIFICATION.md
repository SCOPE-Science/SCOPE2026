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

The proof uses exact polynomial identities and Sturm theory. For the degree-six polynomial \(\zeta_\tau\), the discriminant factors as
\[
4096(\tau^2-9\tau+19)(\tau^2+\tau-1)R((\tau-2)^2).
\]
The standalone verifier recomputes this identity by exact Sylvester determinants at enough distinct rational parameter values to exceed the rigorous degree bound. It also certifies
\[
\operatorname{Res}_x\!\left(\zeta_\tau,2-\tau x+\tau x^2-x^3\right)=64.
\]

An exact rational Sturm sequence proves that \(R\) has one positive root. Exact Sturm counts for \(\zeta_\tau\) at \(\tau=3,4,6,8\) are \(0,2,4,6\). Because the discriminant has no other physical zero and neither the constant nor leading coefficient vanishes for \(\tau>2\), these counts persist on the corresponding open cells.

At \(\tau_\pm\), direct derivatives show that \(x=1\) is exactly a double root of \(\zeta_\tau\). At \(\tau_*\), the discriminant has a simple zero away from \(x=1\), so exactly one nontrivial double root occurs. The verifier also isolates all six \(\tau=8\) roots in exact rational intervals and verifies positive \(\eta_8\) on each interval.

Running `python3 verify.py` prints a single `VERIFY_OK` line. The computation does not enumerate the full four-variable five-periodic system, and no such global claim is made.
