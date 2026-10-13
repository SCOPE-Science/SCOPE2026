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

The symbolic proof reduces the claim to three exact facts for the standard barbell \(B_n\): a dominating set meets both cliques; an induced isolate can occur only on a singleton clique-side; and a singleton bridge endpoint ceases to be isolated exactly when the opposite bridge endpoint is selected. The enumerator follows by subtracting the three disjoint non-isolate types from all dominating sets.

The packaged `verify.py` constructs the graph directly, tests domination and isolation from adjacency, and exhaustively checks every subset for \(2\le n\le7\). It compares the complete bivariate coefficient table with
\[
P_n(x)P_n(y)-Q_n(x)Q_n(y)-xy\big((1+x)^{n-1}+(1+y)^{n-1}-1\big),
\]
and compares the univariate coefficient table with
\[
2nz\big((1+z)^n-1\big)-2z^2(1+z)^{n-1}-(n^2-1)z^2.
\]
It also checks that there are exactly \(n^2-1\) minimal isolate dominating sets and that each is a two-vertex cross-clique pair other than the bridge pair.

Replay output:

`VERIFY_OK n_range=2..7 subset_checks=21840 isolate_sets=2633 minimal_sets=133 bivariate_checks=48 univariate_checks=27 max_order=14`

The finite replay is a consistency check only. It does not certify the infinite family; the all-\(n\) conclusion is supplied by the symbolic proof in `RESULT.md`.
