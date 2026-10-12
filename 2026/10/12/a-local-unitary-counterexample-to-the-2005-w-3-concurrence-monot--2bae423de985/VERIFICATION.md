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

The proof is exact. The target functional is Eq. (23) of arXiv:quant-ph/0505109.

For the state
\[
|\psi_0\rangle=\frac{|000\rangle+|110\rangle}{\sqrt2},
\]
the only nonzero fixed-spectator pair-\(12\) determinant is \(1/2\), so
\[
C_{W^3}(\psi_0)^2/N^W_3=1.
\]

Applying \(iH\) to the third qubit produces, up to global phase,
\[
|\psi_+\rangle=\frac{|000\rangle+|001\rangle+|110\rangle+|111\rangle}{2}.
\]
There are now two nonzero pair-\(12\) determinants, each \(1/4\), so
\[
C_{W^3}(\psi_+)^2/N^W_3=1/2.
\]

The accompanying `verify.py` reconstructs these minors in exact arithmetic in \(\mathbb Q(\sqrt2)\), checks the local transformation, and checks \(\det(iH)=1\). It prints `VERIFY_OK` on success.

The executable replay is finite verification of the displayed counterexample; the conclusion about failure of invariance follows analytically from the exact unequal values. The result does not test or certify any later redefined concurrence.
