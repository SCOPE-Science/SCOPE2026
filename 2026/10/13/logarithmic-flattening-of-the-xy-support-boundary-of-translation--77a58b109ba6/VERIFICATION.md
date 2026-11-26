---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Analytic verification

**Observable normalization.** At zero anisotropy the hopping amplitude is 2, so the occupied negative half of the Fourier spectrum yields
\[
\epsilon(0)=\frac1{2\pi}\int_{\pi/2}^{3\pi/2}4\cos q\,dq=-4/\pi.
\]
Even without using the exact spectrum, averaging the two shifts of a product of nearest-neighbor singlets gives a translation-invariant state with bond marginal \(\tfrac12|\mathrm{singlet}\rangle\langle\mathrm{singlet}|+\tfrac12 I/4\). This gives \(a=0\) and \(b=-1\), excluding the larger value \(-1/(4\pi)\) for the minimum in the stated coordinates.

**Leading singularity without series differentiation.** For nonzero \(\gamma\), differentiate the integral for the support value to write
\[
\epsilon''(\gamma)=-\frac4\pi\int_0^{\pi/2}\frac{\cos^2 q\,\sin^2 q}{(\cos^2q+\gamma^2\sin^2q)^{3/2}}\,dq.
\]
Near \(q=\pi/2\), put \(t=\pi/2-q\). On \(0\le t\le c\) for fixed small \(c>0\), the integrand without its prefactor equals \(t^2/(t^2+\gamma^2)^{3/2}\) times \(1+O(t^2)\) uniformly. The integral of the error and the integral away from that endpoint are bounded. The leading integral equals \(\operatorname{arsinh}(c/|\gamma|)-c/\sqrt{c^2+\gamma^2}=\log(1/|\gamma|)+O(1)\). Thus the coefficient of the divergent support second derivative is \(-4/\pi\). Taking the reciprocal with the minus sign from convex duality and converting from \(\gamma\) to \(a=\epsilon'(\gamma)\) gives the coefficient \(\pi/4\) on the lower graph. The higher-order expansion follows separately from DLMF 19.12.2.
