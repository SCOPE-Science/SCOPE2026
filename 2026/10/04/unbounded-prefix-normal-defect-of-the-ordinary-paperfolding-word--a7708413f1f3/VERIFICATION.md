---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Separating even and odd indices in the odd-part definition gives \(S(2N)=S(N)+\lfloor N/2\rfloor\) and \(S(2N+1)=S(N)+\lfloor N/2\rfloor+(N\bmod2)\). Induction then yields \(S(2^m-1)=2^{m-1}-1\) and \(S(L_m)=\lfloor L_m/2\rfloor-\lfloor(m-1)/2\rfloor\). Since \(L_m+L_{m+1}=2^m-1\) and exactly one is odd, the two prefix sums add to \(2^{m-1}-m\), giving the witness excess exactly \(m-1\). For any fixed \(c\), choosing \(m\ge c+2\) makes this excess exceed the \(c\) prepended ones. A fresh independent recurrence computation verified every identity and exact gap for \(2\le m\le13\); the infinite conclusion rests on the induction.

## originality

PASS

The full open paper on infinite prefix-normal words materially inspected in this run treats finite prepending as a structural question: it records finite normalization for Sturmian and Thue–Morse words, impossibility for Champernowne, and separately derives prefix-normal forms for the ordinary paperfolding word. It does not state whether finite prepending can make the paperfolding word itself prefix normal. Madill–Rampersad give the ordinary paperfolding convention and unbounded/regular abelian complexity, but that factor-extremal result does not compare with the distinguished prefix. Fresh Resultary and web searches under finite-prepending and defect formulations found no covering theorem.

## value

PASS

Finite prepend-normalizability is a named structural distinction in the anchor prefix-normal literature, and that same paper treats paperfolding without deciding this behavior. The explicit logarithmically growing obstruction family places a classical automatic word definitively on the non-normalizable side and is stronger than a single counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
