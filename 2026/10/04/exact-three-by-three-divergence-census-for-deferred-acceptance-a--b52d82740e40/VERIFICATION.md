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
The embedded `verify_ttc_da3_census.py` is a standard-library-only exact replay.

It enumerates every strict preference-priority profile for market sizes \(n=1,2,3\). At \(n=3\), it checks all \(46{,}656\) labeled profiles.

For each profile it computes DA twice, once with a free-student stack and once by simultaneous proposal rounds. It computes TTC twice, once by detecting all cycles in each round and once by repeatedly tracing and executing a single cycle in the residual problem. The paired implementations must agree profile by profile.

The replay verifies the exact partition
\[
42{,}336\text{ equal},\quad 1{,}080\text{ TTC-dominance},\quad 3{,}240\text{ incomparable},\quad 0\text{ DA-dominance}.
\]
It independently tests DA Pareto efficiency against all six perfect matchings and verifies exactly \(1{,}296\) inefficient DA profiles, of which \(216\) are TTC-incomparable.

For every divergent profile, all \(36\) independent relabelings of students and schools are generated. Canonicalization gives \(120\) classes with refinement \(30+84+6\), every class of orbit size \(36\). A separate Burnside fixed-point sum reproduces the same class counts.

The replay also reconstructs the three-student, three-school Abdulkadiroğlu--Sönmez example, obtaining the diagonal DA matching and the TTC matching that swaps the first two assignments and Pareto-improves DA.

Run:

`python3 verify_ttc_da3_census.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the finite claims stated here; it does not extrapolate the frequencies to larger markets.
