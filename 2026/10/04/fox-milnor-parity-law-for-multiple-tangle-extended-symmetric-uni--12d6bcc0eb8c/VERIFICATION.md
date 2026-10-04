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

The primary recent theorem was checked in the construction source:
\[
\Delta_K(t)=\left(\prod_{i=1}^{n}\Delta_{N(T_i)}(t)\right)\bigl(\Delta_{\hat K}(t)\bigr)^2.
\]

The general proof uses unique factorization in \(\mathbb Z[t,t^{-1}]\). Under the reciprocal involution, a norm has even multiplicity on every self-reciprocal irreducible orbit and equal multiplicities on the two members of every non-self-reciprocal orbit. Since \(\Delta_{\hat K}\) is reciprocal, squaring it changes the first multiplicities by even amounts and the second in matched amounts. Hence it cannot alter norm status.

The earlier construction source was checked for the explicit admissible tangle with
\[
N(T)=5_2,\qquad \Delta_{5_2}(t)=2t^2-3t+2.
\]
Its discriminant is \(-7\), so the quadratic is irreducible, and its palindromic coefficients make it self-reciprocal. Thus its \(n\)-th power passes the orbit-parity criterion exactly when \(n\) is even.

The bundled regression program prints:

`VERIFY_OK orbit_parity_invariant=true delta_5_2_disc=-7 repeated_n_1_12=FPFPFPFPFPFP odd_fail_even_pass=true`

This computation checks the bookkeeping and the explicit specialization only. The arbitrary-number-of-regions theorem is the UFD proof above, not a finite enumeration.

No independent audit has been performed.
