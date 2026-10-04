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

The universal proof is analytic. The critical identities checked in the derivation are
\[
R^2=1-\gamma+\gamma^2n(1-n)
\]
and
\[
(R-\gamma\sqrt{n(1-n)})(R+\gamma\sqrt{n(1-n)})=1-\gamma.
\]
They force the longitudinal Bloch multiplier of the unital representative to equal the square of its transverse multiplier. The established unital entanglement-annihilation inequality therefore reduces exactly to
\[
2(1+\sqrt2)n(1-n)\gamma^2+\gamma-1\geq0.
\]

An independent singlet calculation gives a partial-transpose determinant proportional to
\[
\left(n(1-n)\gamma^2+\frac{\sqrt2-1}{2}(\gamma-1)\right)
\left(n(1-n)\gamma^2-\frac{\sqrt2+1}{2}\gamma+\frac{\sqrt2+1}{2}\right).
\]
The second factor is nonnegative on the full parameter square, so the singlet PPT threshold is the same inequality. For two qubits, PPT is equivalent to separability.

Boundary checks: \(n=0\) and \(n=1\) give the complete-damping threshold \(\gamma=1\); \(n=1/2\) gives \(\gamma=2-\sqrt2\); \(\gamma=0\) is the identity channel; and \(\gamma=1\) is constant-output. These are consistency checks, not the basis of the proof.

Independent audit has not been performed.
