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

# Reproducible finite checks

Execute `python verify.py` with Python 3, NumPy and SciPy with HiGHS mixed-integer solver (observed SciPy 1.17.0). The provided `codewords.txt` gives all \(31\) selected base-three indices, from \(0\) to \(80\) inclusive. The script independently enumerates the \(243\) possible length-five inputs, forms their distinct four-symbol deletion outcomes, validates full coverage, and builds the exact \(243\) by \(81\) binary incidence matrix.

Two equivalent integer problems are solved to global optimality. The direct minimization selects at least one deletion outcome for every long word and yields \(31\), with a matching mixed-integer global bound and no gap (\(355\) branch-and-bound nodes in the observed replay). The complement maximization omits short words subject to leaving at least one outcome for each long word and yields \(50\), likewise with matching global bound (\(180\) nodes). Both statuses must be optimal before `VERIFY_OK` is printed. No enumeration of other parameter values is relied upon.

A separate machine-checkable branch proof or solver search-tree certificate is not provided. Thus the lower-bound evidence rests on exact discrete modeling and correctly completed commercial-free HiGHS mixed-integer optimization, not on verification of an independent low-level proof transcript. Independent audit has not been performed.
