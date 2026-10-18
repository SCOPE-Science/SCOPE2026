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
# Reproducing the finite checks

Run `python check.py 9` and `python twist_check.py` in the directory containing both scripts. SymPy and Python 3 are required. Their expected exact-rational summaries are `run.log` and `twist.log` respectively. No random sampling is used in these two computations.

The first script constructs the dicyclic group multiplication table and verifies each predicted nullity against the rank of the complete regular-convolution matrix for every three-element support in every group with \(2\leq m\leq9\). It also verifies the two class counts for singular supports.

The second script constructs both dihedral and dicyclic multiplication tables, and for all supports with \(m=3\) and \(m=6\) compares both exact regular-representation ranks with their respective formulas. For all supports with \(2\leq m\leq12\), it additionally checks the pairwise predicted nullities, the equality of singular-support indicators, the factor-of-two parity condition, and the integer counts of singular and strictly-halved supports.

The script output for \(m=3\) includes \(160\) singular supports and \(72\) strictly-halved supports, while the output for \(m=6\) has \(1280\) and \(288\). These computations are finite consistency checks, not exhaustive verification of the theorem over infinitely many \(m\). The general proof depends on the stated induced-character decomposition, its two-by-two matrix determinants and kernel dimensions, and elementary arithmetic counts.
