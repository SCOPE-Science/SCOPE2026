---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For d=h^infinity(0), h(0)=01 and h(1)=00, derive d[2j]=0 and d[2j+1]=1-d[j]. These force 11 and 0000 absent. Every even-length factor has exactly an aligned h(v) or a one-position rotation thereof; parity of 1 positions distinguishes the phases when v has length >=2, proving both directions and injectivity of the conjugacy-class bijection C_m -> C_2m. Handle m=1 directly. For odd n>=5, any cyclic class with >=2 ones contains a rotation with ones at opposite parities; with <=1 one, a rotation contains four zeros. The only odd base cases are n=1,3, each with two complete classes. Hence L(n)=2 iff odd part is 1 or 3, and 0 otherwise; class representatives follow by h. Independent exhaustive prefix factor/rotation tests n=1..90 and 45 even renormalizations are corroboration, not infinite proof.

## originality

PASS

PASS on statement-and-implication comparison: Bell–Shallit proves boundedness and automaticity of Lie complexity and supplies explicit examples for other automatic words, not the period-doubling table. Cassaigne et al. show period-doubling cyclic complexity c(2^a)=2 but their invariant counts any orbit with >=1 factor; that does not imply all rotations occur, the two 3*2^a classes, or absence elsewhere. Sturmian exact Lie formulas concern a different language. A fresh Resultary semantic query returned a period-doubling three-block lift but no equivalent exact Lie spectrum. This is best-of-knowledge, not exhaustive priority proof.

## value

PASS

The period-doubling word is a canonical nonperiodic automatic word and Lie complexity is an intrinsic language invariant. The complete two-progression support, exact orbit representatives, all other zeros and the structural doubling bijection are a natural infinite classification not supplied by general automaticity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
