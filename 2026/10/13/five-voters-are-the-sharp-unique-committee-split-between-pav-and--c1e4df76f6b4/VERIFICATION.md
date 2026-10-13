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
The embedded `verify_pav_cc_unique_boundary.py` performs two exact finite replays using only the Python standard library.

The first replay enumerates all labeled approval profiles for one through five voters. Each voter independently chooses one of all eight subsets of the three-candidate set. PAV is scored ballot by ballot with exact rational arithmetic, and approval CC is scored by direct voter coverage.

The second replay independently enumerates anonymous eight-type count vectors. PAV is scored in integer half-units and CC by aggregate coverage. Exact multinomial weights reconstruct the labeled profile counts.

The two representations agree on every aggregate count. The verifier confirms:
- no different unique PAV/CC committees for \(1,2,3,4\) voters;
- exactly \(120\) labeled five-voter conflicts;
- exactly \(6\) anonymous five-voter conflicts;
- one candidate-relabeling class;
- canonical counts \(3\times\{A,B\}+\{A\}+\{C\}\);
- canonical PAV scores \((11/2,5,4)\);
- canonical CC coverage scores \((4,5,4)\);
- unconditional labeled incidence \(15/4096\);
- exactly \(11970\) labeled five-voter profiles with both rules unique;
- conditional incidence \(4/399\).

The verifier also checks the integer inequalities used by the analytic proof on every boundary profile after normalization by candidate relabeling.

Run:

`python3 verify_pav_cc_unique_boundary.py`

The first output line must be:

`VERIFY_OK`

The finite replay does not make claims for more than three candidates or committee sizes other than two.
