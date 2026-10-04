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

The proof was checked in four independent steps.

First, for a closed interface the cross-section is disconnected, so the fiber Hamiltonian is an orthogonal direct sum. Its eigenvalues must therefore be the union of the two single-layer spectra
\[
B(2n+1)+\left(\frac{\pi m}{d_j}\right)^2.
\]

Second, for \(d_1=ps\) and \(d_2=qs\) with \(\gcd(p,q)=1\), the exact integer solutions of the source's matching relation \(m_1/m_2=d_1/d_2\) are \(m_1=pr\), \(m_2=qr\). The common transverse eigenvalue is consequently \((\pi r/s)^2\).

Third, the explicit transverse function
\[
\chi_r(z)=\sin\!\left(\frac{\pi r z}{s}\right)
\]
vanishes at \(z=-d_2\), \(z=0\), and \(z=d_1\), has a continuous derivative at the interface, and satisfies the one-dimensional eigenvalue equation with eigenvalue \((\pi r/s)^2\). This verifies the flat-band construction directly.

Fourth, the counting asymptotic is obtained from the exact finite sum
\[
N_{\mathrm{flat}}(E)
=
\sum_{r\le (s/\pi)\sqrt{E-B}}
\left\lfloor
\frac{E-(\pi r/s)^2+B}{2B}
\right\rfloor
\]
and the exact quadratic power sum. The error produced by the floor functions and endpoint replacement is smaller than the stated \(O(E)\) remainder.

The accompanying standard-library checker verifies representative coprime width ratios, common wave numbers, interface zeros, exact finite counts, and convergence to the leading constants. It is a reproducibility aid, not a substitute for the analytic proof.

No statement about distinct numerical-energy counting, absolutely continuous band widths, band crossings, open-gap counts, or disorder stability is verified here.
