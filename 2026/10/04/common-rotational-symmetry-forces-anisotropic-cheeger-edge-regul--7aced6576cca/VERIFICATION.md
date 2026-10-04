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

The critical external premise is the planar anisotropic Cheeger representation
\[
C_W(\Omega)=(\Omega\ominus\rho W)\oplus\rho W,
\qquad
|\Omega\ominus\rho W|=\rho^2|W|,
\]
with uniqueness. This is the content of Kawohl--Novaga's planar theorem inspected in the open full text.

For a common orthogonal symmetry \(Q\), the set identity is checked directly:
\[
x\in\Omega\ominus\rho W
\iff
x+\rho W\subseteq\Omega
\iff
Qx+\rho W\subseteq\Omega
\iff
Qx\in\Omega\ominus\rho W.
\]
Thus the erosion is \(Q\)-invariant, and equivariance of Minkowski addition yields \(QC_W(\Omega)=C_W(\Omega)\).

For rotational orders \(k\) and \(\widetilde k\), the two generated cyclic rotation groups contain the subgroup of order \(\gcd(k,\widetilde k)\). If \(k\mid\widetilde k\), rotation by \(2\pi/k\) preserves both sets.

For contact, let \(A=\Omega\ominus\rho W\). The area equation gives \(|A|>0\). If \(z\in\partial A\) and \(z+\rho W\) had positive clearance from \(\partial\Omega\), then all sufficiently small translates of \(z\) would remain in \(A\), contradicting \(z\in\partial A\). Hence \(z+\rho W\) touches \(\partial\Omega\), and that contact lies on \(\partial C_W(\Omega)\). Under full common \(k\)-symmetry its orbit meets every Cañete edge.

No numerical enumeration or finite experiment is used. The verification is an exact reconstruction of the set identities, group inclusion, and compactness argument.
