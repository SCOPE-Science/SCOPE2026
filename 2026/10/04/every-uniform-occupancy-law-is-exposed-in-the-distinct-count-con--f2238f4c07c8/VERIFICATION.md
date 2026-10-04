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

The proof uses the exact occupancy identity
\[
\Pr\{K_{n,m}=k\}=\frac{S(n,k)(m)_{k\downarrow}}{m^n}
\]
and the reciprocal parameter \(x=1/m\). This produces the polynomial coordinates
\[
p_{n,k}(x)=S(n,k)x^{n-k}\prod_{j=1}^{k-1}(1-jx).
\]
Their lowest nonzero powers are distinct: \(p_{n,k}\) starts with \(S(n,k)x^{n-k}\). Therefore they form a basis of all polynomials of degree at most \(n-1\).

For every finite \(m_0\), the exposing polynomial is
\[
-\left(x-\frac1{m_0}\right)^2.
\]
It is available exactly when \(n\ge3\), and it has a unique maximum at \(x=1/m_0\) on the full set \(\{0,1,1/2,1/3,\ldots\}\). The limiting point \(x=0\) is exposed by \(-x\). This verifies the universal claim without a limiting or finite-enumeration step.

The accompanying exact-arithmetic checker reconstructs Stirling numbers and coordinate polynomials, verifies the triangular basis structure and the identity \(\sum_k p_{n,k}(x)=1\), solves for the linear functionals representing the exposing polynomials for multiple values of \(n\) and \(m_0\), and checks strict separation on sample parameter grids. These computations are consistency checks only; the symbolic basis argument is the proof for all \(n\ge3\).

The verification does not address Zhu's stronger characterization of all exchangeable distinct-count laws and does not assess any independent audit channel.
