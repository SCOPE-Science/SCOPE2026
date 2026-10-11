---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Each binary parity pattern \(b\) has exactly \(2^{p-\operatorname{wt}(b)}\) ternary lifts. The syndrome parity identity \(\sigma(b)\equiv\operatorname{wt}(b)\pmod2\) is correct. Under cyclic right rotation, the syndrome changes modulo \(p\) by the cyclic transition count; for a nonconstant word this is a positive even integer below the odd prime \(p\), so every nonconstant orbit has size \(p\) and its syndromes modulo \(p\) are equidistributed. Summing ordinary and signed lift weights gives the stated \(T_r\) and \(D_r\), and the opposite parities of the two residues above each class modulo \(p\) give all four formulas. Independent exhaustive binary checks at \(p=3,5,7,11\) reproduced them and the minimizer set; finite covering checks are not used to prove the all-prime cardinality law. The covering property itself follows directly from the source theorem because \(\lfloor3/2\rfloor=1\).

## originality

PASS

Originality passes. The complete Xie--Sun--Ge source was read. Its Theorem VI.4 defines exactly the nonbinary parity-and-checksum lift and proves the two-burst covering property plus an averaging size bound. At alphabet size three the checksum moduli are one, so the audited classes are exactly that source specialization. The source does not compute their individual sizes. The cited exact q-ary differential-VT cardinalities concern a different direct q-ary syndrome family and do not imply the weighted parity-lift distribution.

## value

PASS

The source gives only an averaging guarantee inside a new explicit nonbinary two-burst covering construction. Exact syndrome sizes determine which parameter choices are genuinely smallest and by how much they improve the generic average at every odd prime length. That is a natural quantitative refinement of the construction, not an arbitrary code census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
