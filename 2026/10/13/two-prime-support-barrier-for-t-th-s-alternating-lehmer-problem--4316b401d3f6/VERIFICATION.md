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

For β(p^a)=(p^{a+1}+(-1)^a)/(p+1), direct algebra gives 0<β<p^a and β>=p^{a-1}(p-1), equality only a=1. If β(p^a)|p^a−1, then β(p^a)|p+(-1)^a, forcing a=2,p=2 among composite prime powers (n=4). For distinct odd p<q, n/β(n)<= (p/(p−1))(q/(q−1))<=15/8<2 so quotient k=(n−1)/β(n)=1, contradicting β(n)<n−1. For 2^a q^b, denominator β(n) is odd (n−1 odd), and β(q^b) odd forces b even; strict q^b/β(q^b)<q/(q−1) gives n/β(n)<3, and k odd forces k=1, again impossible. No exponent upper bound was assumed. Independent exact factoring/enumeration of 40,115 composite integers of support <=2 through n=120000 returned only n=4, corroboration not universal proof.

## originality

PASS

Tóth primary survey poses β(n)|n−1 as Problem 4 with composite n=4 exception and reports finite search; it does not prove this uniform support <=2 exclusion in the inspected full paper. Classical Lehmer totient results bound squarefree candidates since β(n)=φ(n) there but do not cover nonsquarefree factors. Caragiu–Swieringa 2024 alternating divisor is nonmultiplicative under a different definition. Resultary matched unrelated divisor functions but no implication of this claim. Possible unindexed elementary argument remains a residual risk.

## value

PASS

Tóth’s explicit open analogue of Lehmer’s problem naturally asks for structural obstructions. Excluding every composite with at most two distinct prime factors, with arbitrary exponents rather than a numerical cutoff, is a substantive infinite reduction; the parity argument handles the nonsquarefree case omitted by the classical squarefree analogy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
