---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Length-one observations give zero and one totals; lengths two determine the two run counts; length-three counts refine them to zero/one singleton-run counts plus endpoint correction. The exact formulas N000=z-2r0+a0 and N111=p-2r1+a1, and mixed triples from boundary terms, also give the converse: the finite run signature determines every composition multiplicity. The enumeration separates endpoint cases with r0-r1 in {-1,0,1} and performs an inclusion-exclusion correction on their single overlap. For each feasible signature, the diagonal generating series for run excesses is geometric, so the eleven-term finite rational sum is exhaustive. Its common-denominator integer-polynomial equality proves the displayed rational generating function for all n, and partial fractions give the period-four quartic. Constant words and n=1 are separate. Independent direct enumeration of all words n=1..12 reproduces the counts (2,3,6,10,20,35,62,101,160,241,354,502). It does not establish the infinite identity; the run bijection and rational algebra do.

## originality

PASS

Ye–Elishco define precisely the r-limited contiguous-composition model but do not calculate the fixed r=3 profile quotient. The published r=2 study proves a quadratic enumeration and run-count class sizes, whereas r=3 requires singleton-run and endpoint distinctions and has a quartic period-four profile. Full-spectrum reconstruction and ordered substring spectra are nonequivalent observations and do not imply the coarser quotient cardinality. Best-of-knowledge original, with unindexed fixed-cutoff equivalences still possible.

## value

PASS

The maximal number of codewords distinguishable by a fixed small composition window is a natural exact reconstruction invariant; the shift from quadratic r=2 growth to a quartic, period-four r=3 law precisely identifies the information unlocked by one additional substring length. The all-n generating function is a substantive enumeration, not a sampled code table or trivial substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
