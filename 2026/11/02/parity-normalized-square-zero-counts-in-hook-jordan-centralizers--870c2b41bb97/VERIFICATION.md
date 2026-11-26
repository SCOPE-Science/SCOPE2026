---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

As t-modules, R=F_q[t]/(t^n) and W=F_q^r with tW=0 give diagonal blocks f,D and off-diagonal maps t^(n−1)b and evaluation at zero times c. Their lower-right cross product vanishes since n≥2, while their upper-left cross product is t^(n−1)bc. The constant term forces f(0)=0; the remaining equations are D²=0, bD=Dc=0 and f²+t^(n−1)bc=0. The flag im D=U⊆K=ker D and the induced isomorphism W/K→U yield exactly G_{r,k}; b descends to (K/U)* on restriction and c to K/U, each with q^k lifts. The first nonzero coefficient of f², when present, is the square of the first nonzero coefficient of f at twice its degree. For n=2h this forces valuation at least h and bc=0; for n=2h+1 it leaves only the equation a_h²+bc=0. In both cases the higher free coefficients give q^h. On a quotient of dimension s>0, a nonzero form has q^(s−1) vectors in every pairing fiber, while the zero form gives q^s vectors and forces a_h=0 when relevant. This produces the stated H factors, both equal to 1 at s=0, and their difference is (q−1)q^(s−1)(q^s−1) for positive s. The k=0 term gives strictness for r≥1; no square-root count or characteristic assumption is used. Centralizer size follows from n+2r+r² free coordinates. Independent spot replay enumerated all d×d matrices over each listed prime field by base-q expansion and filtered by ordinary matrix products XB=BX and X²=0: for (n,r,q)=(2,1,3),(3,1,2),(2,2,2), the centralizer sizes and square-zero counts were (243,15),(64,8),(1024,44). The all-parameter decision rests on the proof; the frozen checker and recorded output were inspected but not executed.

## originality

PASS

The credited distinct content is the all-tail count and normalized parity separation for a long hook, especially the odd n≥3, r≥2 fiber. Resultary 0260ec1ac7b2 already gives (and rank-refines) n=2, and 50a5542dfb83 already gives the r=1 parity family and more rank information there. The even normalized generalization is effectively the n=2 count after extracting free coefficients; neither overlap evaluates the odd hook when the square-zero tail can have positive rank. Inspected primary frameworks encode the counting problem or classify possible types, but do not give a theorem that evaluates this mixed pairing and valuation fiber. Pass is best of available evidence for the general result, not originality of the subcases or of the flag factor.

## value

PASS

The natural finite-field fiber is determined for every rank of the square-zero tail block, and its size exhibits a strict residual parity gap after the free long-block coordinates are divided out. This separates parity from simple dimension growth and gives the probability of square-zero for a uniform commuting matrix. In the previously uncovered mixed regime it is an exact invariant of the hook centralizer, including characteristic two, rather than a tiny test instance or re-enumeration of the two known boundary slices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
