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

The proof was checked case by case at the structural level.

For \(|A|\ge5\), the half-group intersection argument gives \(A-A=G\). For \(|A|=3\), translation gives \(A=\{0,a,b\}\), the difference set is the plane \(S=\langle a,b\rangle\), and the nontrivial character with kernel \(S\) gives the exact obstruction
\[
\widehat h(\chi)=-\frac23.
\]
For \(|A|=2\) and \(|A|=4\), explicit complementary subspaces or the translate by \(a+b+c\) produce proper tilings. The autocorrelation witness of a tiling complement verifies the positive-definite weak-tiling direction directly.

The accompanying `verify.py` was executed successfully. It exhaustively enumerates every nonempty subset of the eight-element group, checks all translational tilings exactly, verifies the full-difference-set cases, and checks the three-point Fourier obstruction using rational arithmetic. It prints `VERIFY_OK`.

Because the ambient group is finite and all \(255\) nonempty subsets are enumerated, the computation is exhaustive rather than a sampled experiment. The analytic proof remains the primary explanation of the classification.
