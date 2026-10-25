---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS: Every nonnegative representation n=a+3b with a,b having base-4 digits 0/1 is counted by a two-state carry automaton; on output digits d=0,1,2,3 its (carry0,carry1) counts update respectively (u,u+v),(u+v,v),(v,0),(u,0), initially (1,0). Final valid carry0 count equals R(n), including leading-zero conventions. The nonempty supports {0} and {0,1} have transition counting matrix [[2,2],[1,2]], hence H0=1,H1=3,H_(k+2)=4H_(k+1)-2H_k and the radical closed form. Component max<=F_(k+1), min<=F_k is invariant under all four digit transformations; explicit least-significant-first words (01)^m for even k and 001(01)^(m-1) for odd k>=3 attain F_(k+1), while k=1 is direct. Comparing X between consecutive fourth powers yields the two Theta growth exponents and density zero. Independent exact enumeration through k=8 gave supports 1,3,10,34,116,396,1352,4616,15760 and maxima 1,1,2,3,5,8,13,21,34, corroborating but not proving the induction.

## originality

PASS

PASS, qualified: the numeric recurrence itself is already OEIS A007052, so only the identification with M+3M and the Fibonacci maximum of representation multiplicity are assessed as potentially original.

## value

PASS

PASS: The original Moser–de Bruijn set with a perturbed coefficient 3 has an inherently natural carry-language representation problem. The exact support growth exponent and sharp maximum multiplicity (Fibonacci) distinguish sparsity from unbounded local ambiguity; the contribution is the arithmetic identification and extremal representation law, not the already-known raw integer recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
