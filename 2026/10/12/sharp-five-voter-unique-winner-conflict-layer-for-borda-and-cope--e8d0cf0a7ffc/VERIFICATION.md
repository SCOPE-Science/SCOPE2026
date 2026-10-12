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
The embedded `verify_borda_copeland_unique_conflict.py` performs an exact finite replay using only the Python standard library.

Borda is independently computed from \(2,1,0\) positional scores and from pairwise-support totals. Copeland is independently computed from \(1,1/2,0\) contest scores and from pairwise-margin signs.

The verifier exhausts every labeled three-candidate profile with one through five voters. It confirms no different unique winners through four voters, exactly \(60\) conflicts at five voters, incidence \(5/648\), an independent anonymous count of \(6\) among \(252\), incidence \(1/42\), one candidate-relabeling class, and one combined candidate/voter orbit containing all \(60\) labeled conflicts.

It also checks the representative `3 BCA + 2 CAB`, Borda scores \((2,6,7)\), pairwise margins \((-1,-5,1)\), unique Borda winner \(C\), and unique Copeland/Condorcet winner \(B\).

Run:

`python3 verify_borda_copeland_unique_conflict.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated three-candidate finite boundary through five voters.
