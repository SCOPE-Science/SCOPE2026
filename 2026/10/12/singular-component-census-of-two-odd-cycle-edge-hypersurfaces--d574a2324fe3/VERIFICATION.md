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

The claim is a universal statement for all \(a,b\ge1\) and \(\ell\ge0\) over \(\mathbb C\). Its proof uses an exact primitive incidence-kernel relation, disjoint binomial supports, the Jacobian vanishing criterion, minimal support enumeration, analytic units, and Serre normality; finite testing is not substituted for proof.

Run `python3 checker.py` in the directory containing `checker.py` and `checker_results.json` using only Python's standard library. The script constructs actual edge-incidence relations from the two cycles and their joining path, checks the primitive signed relation, directly evaluates every partial derivative at each binary coordinate-zero support, and independently computes inclusion-minimal singular supports. Its predicted component sets and codimension counts are then compared to those direct evaluations.

Actual execution covered fifteen parameter triples with \((a,b)=(1,1)\), lengths \(0,1,2,3,4,5\); \((a,b)=(1,2)\), lengths \(0,1,2,3,4\); and \((a,b)=(2,2)\), lengths \(0,1,2,3\). In total it evaluated \(27{,}328\) binary coordinate support patterns; all checks passed. Representative codimension-one, -two, -three component counts are \((1,6,9)\) at \((1,1,2)\) and \((2,13,6)\) at \((1,1,3)\). The complete exact output is `checker_results.json`.

No all-parameter exhaustive enumeration was performed or needed. No independent audit, external certification, or conclusions about nongeneric component intersections or scheme-theoretic nilpotent structure are claimed.
