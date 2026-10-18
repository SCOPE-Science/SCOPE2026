---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The Montesinos double-branched-cover relation matrix [[p,0,0,3],[0,q,0,-8],[0,0,q,-8],[1,1,1,0]] has determinant q(16p-3q) with p=3b+5,q=8b+13. Thus det=(8b+13)(24b+41)>0. Symbolic first difference is 384b+832>0. The factors are coprime (difference of second minus triple first equals 2), while 24b+41=2 mod3 so cannot be square; hence product is nonsquare. Fox–Milnor forbids algebraic sliceness, and topological sliceness implies algebraic. Computation through b=150 only corroborates the symbolic all-b proof. Nakamura local-move construction is an explicitly cited external premise; its recent full text was unavailable in this run, so not independently re-proved. The frozen RESULT source contains literal control characters corrupting alpha/beta/fraction/right KaTeX, independently checked at its Git blob, hence an exact corrected full UTF-8 RESULT.md is supplied.

## originality

PASS

The exact family was introduced by Nakamura; the determinant factorization, strict separation and uniform Fox–Milnor nonsliceness obstruction were not found in matched statement searches or accessible source descriptions. The general determinant lemma and Fox–Milnor factorization are inputs, not the parametrized conclusion. Recent unavailable source full text leaves a substantive residual risk.

## value

PASS

It gives an all-parameter exact concordance obstruction on a naturally motivated two-site delta-unknotting family and certifies pairwise distinction by one invariant. Although the final modular obstruction is short, it answers a concrete topological question about every member of the family rather than an arbitrary numeric slice; no stronger general theorem is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
