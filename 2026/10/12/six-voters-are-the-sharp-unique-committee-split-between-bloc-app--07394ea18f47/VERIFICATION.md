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
The embedded `verify_av_sav_six_voter_boundary.py` performs an exact finite replay using only the Python standard library.

The ballot domain is the seven nonempty subsets of three candidates.

The verifier exhausts every labeled profile through six voters and computes:
- ordinary AV candidate scores with integers;
- SAV candidate scores with exact `Fraction` arithmetic;
- unique two-member committees by identifying a unique lowest-scoring candidate.

The numbers of labeled profiles where both rules are unique are
\[
3,\ 27,\ 201,\ 1467,\ 10398,\ 75051
\]
for one through six voters.

The corresponding numbers with distinct unique committees are
\[
0,\ 0,\ 0,\ 0,\ 0,\ 360.
\]

An independent anonymous enumeration over weak compositions of six voters into the seven ballot types finds exactly six conflict profiles. Candidate relabeling puts all six in one orbit represented by
\[
(0,1,2,3,0,0,0)
\]
for ballot types
\[
A,B,C,AB,AC,BC,ABC.
\]

That representative has AV scores
\[
(3,4,2)
\]
and SAV scores
\[
\left(\frac32,\frac52,2\right).
\]

Its voter-labeling multiplicity is \(60\), so the six candidate relabelings give \(360\) labeled profiles.

Run:

`python3 verify_av_sav_six_voter_boundary.py`

The first output line must be:

`VERIFY_OK`
