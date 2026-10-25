---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Subtracting consecutive partial sums of the original floor recurrence gives the exact divisor formula h_c(n)=-1-c sum_{1<d<n,d|n}h_c(d), valid including n=2. With g_c=epsilon+c(u-epsilon), convolution yields h_c*g_c=epsilon+(c-1)(u-epsilon). Modulo c-1 (c>=3), g_c≡u and Möbius inversion gives h_c≡mu mod(c-1), excluding nonsquarefree composites from h=-1. On squarefree r-prime support, Boolean subset convolution gives generating function H(z)=[(c-1)e^z-(c-2)]/[c e^z-(c-1)] =1-1/c+c^{-2}e^{-z}/(1-rho e^{-z}), rho=(c-1)/c. Its rth coefficient for r>=1 is (-1)^r c^{-2} sum_{m>=1}m^r rho^{m-1}, magnitude exactly 1 at r=1 and strictly >1 at r>=2. Thus all primes exactly -1 and no composite for every fixed c>=3. Sharp boundary c=0 at n4, c=1 at n30 via mu, c=2 at n8 by prime-power formula. Independently evaluated ORIGINAL floor recurrence versus the divisor recurrence for c=0..8, n<=180, all prime/composite classifications within cutoff; this bounded computation corroborates but does not replace the infinite argument.

## originality

PASS

Andrews–Kauffman–Sahoo arXiv:2609.25628 states a very broad claimed iff for arbitrary f, but fixed function f≡1 is a published counterexample, so that literal theorem cannot establish valid fixed-function primality across all choices. The proven affine positive/negative threshold c>=3, with exact squarefree layer formula and congruence, is a specific nontrivial surviving classification not stated in inspected abstract or closest published Resultary obstruction. Full original 2026 arXiv paper could not be read due access failure, so hidden sufficient conditions in its body could preempt the positive portion; this is explicitly retained.

## value

PASS

A new generalized Möbius recurrence purports to be a primality criterion but fixed-function quantifier matters. This result identifies an infinite sharp family of genuine *fixed* primality detectors and all failing nonnegative integer affine slopes, separating squarefree-support obstruction from nonsquarefree congruence obstruction. The complete threshold and coefficient formula give genuinely useful structural information beyond one cheap counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
