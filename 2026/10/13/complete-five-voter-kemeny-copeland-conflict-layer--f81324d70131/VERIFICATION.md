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
The embedded `verify_kemeny_copeland_odd_first_layer.py` performs two exact finite replays.

The labeled engine exhausts all complete strict profiles with \(1\), \(3\), and \(5\) voters over three candidates.

Kemeny is computed independently by:
1. maximizing pairwise agreement over all six candidate rankings;
2. minimizing total Kendall inversion distance.

For every candidate ranking \(\pi\) it verifies
\[
S_P(\pi)+D_P(\pi)=3|P|.
\]

Throughout these finite domains, it also checks Kemeny against maximin, matching the published three-candidate equivalence.

The anonymous engine independently enumerates all
\[
252
\]
five-voter ballot-multiplicity vectors. It confirms exactly \(6\) divergent anonymous profiles and weights each by its multinomial number of labeled realizations.

The verifier confirms:
- equality for every one-voter profile;
- equality for every three-voter profile;
- \(7236\) five-voter profiles with the same unique winner;
- \(360\) five-voter profiles where both rules return all three candidates;
- \(180\) five-voter profiles with \(K(P)\subsetneq C(P)\);
- exact labeled incidence \(5/216\);
- exactly \(6\) divergent anonymous profiles among \(252\);
- exact anonymous incidence \(1/42\);
- one candidate-relabeling orbit of anonymous divergences;
- multiplicity pattern \(2,2,1\) and labeled weight \(30\) for every divergent anonymous profile;
- absolute cyclic margin multiset \((3,1,1)\);
- the displayed representative with \(K(P)=\{A,B\}\) and \(C(P)=\{A,B,C\}\).

Run:

`python3 verify_kemeny_copeland_odd_first_layer.py`

The first output line must be:

`VERIFY_OK`

The five-voter minimality and margin-level \((3,1,1)\) boundary are treated as prior; the finite replay establishes the complete preference-profile realization layer.
