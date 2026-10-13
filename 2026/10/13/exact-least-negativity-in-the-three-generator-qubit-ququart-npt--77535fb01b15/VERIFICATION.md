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

The proof is analytic. Partial transposition gives two positive singleton entries and three explicit \(2\times2\) Hermitian blocks. Their exact negative eigenvalues yield the closed formula used in the proof. Strict convexity first reduces every possible minimizer to \(x=z\), and the remaining scalar function is proved monotone on the two sides of \(y=1/3\).

`verify_min_negativity.py` reconstructs the \(8\times8\) matrices symbolically, verifies the block spectrum at the uniform point, checks
\[
\mathcal N\!\left(\rho_{1/3,1/3,1/3}\right)=\frac{\sqrt5-1}{6},
\]
and confirms inertia \((5,1,2)\). The script is a replay check; it does not replace the global analytic proof.

Unproved limits: arbitrary coherent states supported on the same three-dimensional subspace and higher-dimensional diagonal simplices are outside the claim.
