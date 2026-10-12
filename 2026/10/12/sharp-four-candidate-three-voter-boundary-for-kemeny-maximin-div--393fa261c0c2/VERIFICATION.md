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
The embedded `verify_kemeny_maximin_first_layer.py` performs an exact finite replay using only the Python standard library.

For Kemeny, it independently:
1. maximizes total pairwise agreement over every candidate ranking;
2. minimizes total Kendall inversion distance to the voters' ballots.

It verifies the identity
\[
S_P(\pi)+D_P(\pi)=6|P|
\]
for every four-candidate ranking \(\pi\).

For maximin, it independently:
1. maximizes minimum pairwise support;
2. minimizes maximum opposing support.

It verifies
\[
m_P(x)+o_P(x)=|P|
\]
for every candidate.

The verifier exhausts:
- all \(24\) one-voter profiles;
- all \(576\) two-voter profiles;
- all \(13824\) three-voter profiles.

It confirms:
- equality for all one- and two-voter profiles;
- \(12768\) equal three-voter profiles;
- \(1056\) divergent profiles;
- exact incidence \(11/144\);
- \(K(P)\subsetneq M(P)\) in every divergence;
- divergent size counts \(144,576,336\);
- exactly eight divergent isomorphism classes;
- seven orbits of size \(144\) and one orbit of size \(48\);
- all displayed canonical winner sets.

Run:

`python3 verify_kemeny_maximin_first_layer.py`

The first output line must be:

`VERIFY_OK`

The universal equality for all three-candidate electorates is a cited published theorem and is not inferred from finite testing.
