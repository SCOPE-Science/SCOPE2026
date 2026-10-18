---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Sigma(2^a p^2)=(2^(a+1)-1)(p^2+p+1), and its excess above 2^(a+1)p^2 has sign equal to p<2^(a+1) for odd prime p; equality is impossible by parity. Splitting the exact prime-count formula at 2^(3a+2)=X gives a geometric sum of cutoffs 2^(a+1) and one of sqrt(X/2^a). PNT with geometric-tail uniformity yields A_2(X)=(X^(1/3)/log X)(F(s)+o(1)), F(s)=3*2^(1/3)*s^(-1/3)[2+(1+sqrt(2))*sqrt(s)], s in [1,8). Differentiation gives the stated min/max; a separate direct 200000-bound divisor-excess enumeration matched the cutoff and found 89 abundant members. Finite enumeration does not establish the asymptotic.

## originality

PASS

Dean et al. analyze excedent values of structured prime-square integers but do not provide this exact sparse abundant-input phase count. The Resultary two-prime practical-number phase result is for a different predicate, and the primitive-abundant two-prime layer does not include squared odd-prime factors. The full cited Dean et al. PDF mathematical sections were inspected, and no equivalent phase law appeared in material read. An unindexed number-theoretic enumeration could preempt it.

## value

PASS

This is the natural first repeated-odd-prime layer within the established 2^a p^b family. The exact dyadic oscillatory main term and distinct limsup and liminf quantify sparsity not recoverable from the overall abundant-number density or leading first-prime-power stratum, so the exact invariant has self-contained value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
