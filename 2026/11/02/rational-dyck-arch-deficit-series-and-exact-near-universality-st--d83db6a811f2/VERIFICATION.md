---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The arch factorization for scattered-subsequence universality equals the greedy count of completed 0/1 arches. Pairing consecutive symbols turns Dyck words into coloured Motzkin excursions (paired height h), tracking R/Z/O arch states; each two-symbol block completes at most one arch. On first reaching a new paired height, the 00 block cannot be good because good 00 needs state O and creating that state at height h requires an earlier 11 from height h+1, impossible at the first visit. Thus max h<=d bad blocks and all fixed-deficit Dyck paths are in a finite 3(d+1)-state transfer system. G_d=e(I-zP)^(-1)[zQ(I-zP)^(-1)]^d f proves rationality for every fixed d, not joint bivariate rationality. Checked boundaries n=0 and d=0, transition table and first four displayed rational functions. Independent fresh direct enumeration of 23,714 Dyck paths for n<=10 corroborates height bound and first deficiency distributions; all-n argument is the first-height lemma plus formal matrix identity, not finite extrapolation.

## originality

PASS

Known arch decomposition, regular-language universality counting and the known numerical sequence A001793 are carefully separated from the claimed structural Dyck fixed-deficit rationality and explicit d=3. The exact d=2 count is not presented as discovery of a new sequence; it is a differently defined Dyck statistic. No stronger result inspected mechanically gives the bounded-height arch-deficit transfer.

## value

PASS

A structural bounded-height characterization and rational generating function for every fixed universality deficit in the canonical nonregular Dyck class is an independently useful exact enumeration theorem. It unifies arbitrary fixed deficit and explains exponential sparsity, rather than reporting only the already-known d=2 sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
