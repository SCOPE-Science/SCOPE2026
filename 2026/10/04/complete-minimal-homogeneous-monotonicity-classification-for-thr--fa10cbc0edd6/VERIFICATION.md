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
The embedded `verify_irv17_homogeneous_monotonicity.py` is an exact finite replay.

Route A enumerates every anonymous three-candidate profile for electorate sizes \(1\) through \(17\). At each uniquely resolved profile it tests every nonempty group of voters sharing one ballot and every identical ranking change that raises the current winner while preserving the relative order of the other two candidates. It verifies zero harmful events through \(16\) voters and exactly \(252\) at \(17\).

Route B independently generates the two symbolic normal-form families
\[
(x,6-x,y,5-y,2,4)
\]
and
\[
(x,6-x,y,5-y,0,6),
\]
with \(0\le x\le6\) and \(3\le y\le5\), and requires exact set equality with the candidate-normalized exhaustive output.

The replay additionally verifies:
- every minimal harmful group has size \(2\);
- every bad profile has exactly one harmful homogeneous change;
- exactly \(126\) profiles raise the winner by one position and \(126\) by two positions;
- there are exactly \(42\) candidate-relabeling classes, each with orbit size \(6\);
- all six ordered old-winner/new-winner transitions occur \(42\) times;
- the all-profile incidence is exactly \(2/209\).

Run:

`python3 verify_irv17_homogeneous_monotonicity.py`

The first output line must be:

`VERIFY_OK`

The exhaustive checks are finite. The lower bound \(n\ge17\) and the equality-case normal forms are also proved symbolically in `RESULT.md`.
