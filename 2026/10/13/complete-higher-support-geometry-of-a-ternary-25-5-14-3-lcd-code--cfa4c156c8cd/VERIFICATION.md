---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The standalone `verify.py` uses only Python 3 standard-library integer operations and modular arithmetic over \(\mathbb F_3\). From the published \(5\)-by-\(25\) generator it rebuilds all \(243\) codewords, checks the ordinary weight enumerator and the Euclidean LCD Gram criterion, and enumerates each of the \(121,1210,1210,121,1\) coefficient subspaces exactly once via unique reduced-row-echelon representatives. It checks all \(N_r(s)\) entries against their Gaussian-binomial totals, the six minimum-support two-spaces with their common-zero coordinate sets, and the four projective word weights in each.

A separate geometric census enumerates all \(1210\) vector three-spaces, tests membership of each of the \(25\) projective columns by rank, and checks the maximum-plane sextuples, their pairwise intersections, and their coordinate-incidence multiplicities. Run `python3 verify.py`; a successful run prints `VERIFY_OK`. This is an exhaustive finite computation for this one code and a transparent, replayable certificate, not an exhaustive search over all ternary LCD codes or an external/independent scientific audit.
