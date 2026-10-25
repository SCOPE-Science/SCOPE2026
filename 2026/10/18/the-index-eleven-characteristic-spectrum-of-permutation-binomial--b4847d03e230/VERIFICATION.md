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

Let Q=p^m arbitrary, gcd(s,Q−1)=11, t=(Q−1)/11, u=s/11. Fiber quotient and gcd(u,t)=1 imply a permutation of μ_t by ψ(y)=y^b(y+a)^11 with bu≡r (mod t), gcd(r,11)=1. Root exclusion ζ=(-a)^t∈μ11\{1} and product of all nonzero permutation values forces (ζ−1)^11=(-1)^{r−1}; ζ or ζ⁻¹ is common root of X^11−1 and (X+1)^11−1 modulo p. Independently reconstructed W11=101832157445630503=23^5·67²·89·199². For p67,89,199, all μ11 lie in prime field and 11j<p for j=1,2; differentiated rational partial fractions justify necessary P11(−11⁻¹,U1,ζ)=0 and P22(−11⁻¹,U2,ζ)=0 with U2≡2U1+(1−c)/11. Independently computed all ζ and first-moment roots (6,2,4 for p67,89,199) and verified both second-moment cases nonzero, uniformly excluding EVERY extension field. For p23 f=x^12+2x permutes F23 as 3-times nonzero squares/fixes nonsquares. Finite residue certificates are exhaustive BECAUSE of the all-extension reduction, not a substitute for it.

## originality

PASS

Tang–Fan 2026 proves precisely p=23 when Q=p PRIME and g=11; their theorem is not the all-extension quantifier. Their general finiteness/Wendt restriction leaves 67,89,199 as candidates; the submitted second reciprocal moment excludes these over p^m of unbounded m. Ni/Pang/Yu/Yuan and Fan fixed structured exponents gcd(q−1) are different. Best-of-knowledge extension spectrum survives prior implication test.

## value

PASS

Classifying exactly which prime characteristics can support a prescribed natural gcd index over ANY extension degree is a meaningful strengthening of a known prime-field result; exact universal finite obstruction and an explicit realizing witness may guide permutation-polynomial classification at other indices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
