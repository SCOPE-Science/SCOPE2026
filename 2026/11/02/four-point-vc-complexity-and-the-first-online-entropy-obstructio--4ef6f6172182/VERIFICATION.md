---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For a Dyck word with n-2 peaks, exactly four equal-letter adjacencies make its mismatch with the alternating word exactly two nonempty interval runs. A set of five ordered positions with alternating 1-0-1-0-1 cannot be shattered by two intervals; the 16 traces on positions 2,4,7,8 at n=6 and padding with (UD) tails prove VC=4 for every n>=6. The suffix interval-to-threshold embedding after the UUDD prefix proves unbounded online dimension with floor(log2(n-3)) lower bound. The exact boolean recurrence over all nonempty hypothesis subsets, using complete coordinate splits and exact 2^depth leaf cutoff, proves each finite Ldim n=3..11, rather than extrapolation. The independent finite solver enumerated all 3..11 layers including 825 hypotheses at n=11, 60,564 memoized states, and reproduced the listed dimensions and witness traces. Boundaries n=3,4,5 were separately enumerated. No formula is asserted for the full Ldim sequence past 11.

## originality

PASS

The Narayana layer and the VC theorem for unrestricted unions of two intervals are known; the new content is the natural fixed-peak-subclass lower bound, its exact online table, earliest entropy deficiency and qualitative VC/Ldim separation. Chase–Freitag identifies the online dimension and model-theoretic equivalence, not the Dyck count; Shigechi computes Catalan statistics such as major index and q-Narayana refinements, not shattering under step queries. No tested published Resultary result implies the exact restricted online depths. Older learning-theory classification under parity-adjusted interval embeddings remains a specified priority risk.

## value

PASS

Two fewer peaks defines a canonical Narayana stratum, not an arbitrary subset. The fixed VC=4 but growing adaptive dimension is a concrete structural separation, and the first failure of the generic floor(log2 class size) upper bound at semilength 9 is not given by the Narayana count. The exact initial table and the two-interval encoding can serve future lower/upper analyses of other peak-deficit strata, while not claiming an all-n Ldim formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
