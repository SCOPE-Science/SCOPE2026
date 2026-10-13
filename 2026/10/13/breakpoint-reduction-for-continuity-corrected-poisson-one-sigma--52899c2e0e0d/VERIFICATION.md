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

The universal proof is analytic. For fixed rounded endpoints \(\ell\) and \(u\), direct differentiation of the Poisson mass sum gives
\[
J'(\lambda)=p_{\ell-1}(\lambda)-p_u(\lambda).
\]
When \(\ell\ge1\), the ratio of the two terms is a strictly decreasing monomial in \(\lambda^{-1}\); hence any interior zero of the derivative is a strict maximum. When \(\ell=0\), the derivative is strictly negative.

The endpoint-change equations were solved exactly as \(A_m\) and \(B_n\). For integer squares \(s^2\), direct one-sided endpoint accounting adds one strictly positive Poisson atom on either side of the value at the square, proving strict local minimality for every \(s\ge2\).

The included checker numerically replays the derivative identity away from breakpoints and square local-minimum behavior for \(2\le s\le100\). These finite checks do not certify the quantified theorem; they are regression tests against transcription or implementation errors.

The unresolved limit is explicit: this package does not prove that every finite breakpoint value exceeds \(2\Phi(1)-1\). It proves only the exact localization and reduction stated in the finding.
