---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

With fixed denominator M>=2 and coprime numerators, Carvalho's exact order-class recurrence gives (M-z phi(M))F_M=1+z sum_{1<d<M, d|M}phi(d)F_d. For M=p^s m with p largest prime, the only divisors whose phi(d)/d equals rho=(p-1)/p are powers p^j. By induction on divisors, modulo functions holomorphic at z0=p/(p-1), F_{p^j e} is congruent to F_{p^j}, and the totient identity sum_{e|m}phi(e)=m collapses all pole principal parts to the prime-power F_{p^s}=p^{-s}(1-rho z)^{-s}. The multiplier M-z phi(M) is nonzero at z0 for m>1; all other possible poles have modulus >=1/eta_M>1/rho. This justifies the coefficient error O_M(n^{tau(M)} eta_M^n), leading polynomial-binomial term, and tail factor 1/(1-rho)=p; density of infinite orders zero is cited rather than assumed pointwise. Independently rebuilt the rational-function recurrence using SymPy and checked cancellation for all M=2..90, and directly iterated T using exact rational arithmetic over one modulus period for M=3,4,6,10,12 and orders 1..3. The infinite proof is divisor induction, not finite experiment.

## originality

PASS

Best-of-knowledge new analytic dominant-pole cancellation and composite-denominator sharp large-order tail; the exact recurrence and p-power density are acknowledged prior work. The other map has the same recurrence, so a differently phrased earlier asymptotic remains a real risk.

## value

PASS

Fixed-denominator stopping statistics for a natural rational map are motivated by the open individual finite-order question. The theorem gives a sharp general asymptotic with both leading constant and polynomial factor, and proves a nonobvious dominance/cancellation by the largest prime-power component. It is not a routine restatement of density one or a small computational improvement; all lower prime factors contribute only exponentially smaller terms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
