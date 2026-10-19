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
# Verification

The file `verify.py` enumerates every matching on \(2q\) labeled positions for \(1\le q\le7\). It converts each matching into a first-appearance-normalized double-occurrence word and directly compares the Parikh vectors of every pair of equal-length adjacent substrings. It checks the number of matchings, each half-length's exact expected number of Abelian-square occurrences, every binomial moment of the adjacent-equality statistic, and inclusion–exclusion for words without adjacent repetitions. The reference numbers of completely Abelian-square-free normalized words are \(0,0,1,15,195,2630,38519\).

Run `python3 verify.py` in the same directory. On a successful run it ends with `DOUBLE_OCCURRENCE_ABELIAN_POISSON_FINITE_PASS matchings= 146599`. The checker has only standard-library dependencies; its direct enumeration is finite. The proof of total-variation convergence for all \(q\), including the all-half-length tail bound, is mathematical and independent of extrapolation from these finite checks.

The scientific result is an analytical theorem with a finite supplementary checker. No external or independent audit has been performed.
