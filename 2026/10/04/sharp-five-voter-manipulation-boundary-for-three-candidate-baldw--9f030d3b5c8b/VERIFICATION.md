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
The embedded `verify_baldwin5_manipulation.py` provides an exact finite replay.

Route A enumerates every anonymous three-candidate profile for electorate sizes \(1\) through \(5\). For each unique truthful Baldwin outcome, every sincere ranking type present and every false report are tested. Two independent Baldwin implementations are required to agree on all truthful and deviating profiles.

Route B independently enumerates all \(6^5=7776\) ordered five-voter profiles, every distinguished voter, and every false report. Forgetting voter labels must give exactly the same six anonymous bad profiles as Route A, with the correct multinomial multiplicities.

The replay verifies:
- zero manipulable anonymous profiles for \(1\) through \(4\) voters;
- exactly \(6\) manipulable anonymous profiles at \(5\) voters;
- exactly \(180\) bad labeled profiles among \(7776\);
- exactly \(6636\) labeled profiles with unique truthful Baldwin outcome;
- exactly \(360\) vulnerable distinguished voter-profile pairs;
- one vulnerable ranking type per bad anonymous profile, of multiplicity two;
- one profitable false report per vulnerable voter;
- one candidate-relabeling class containing all six anonymous profiles;
- normalized truthful profile \((2,0,0,1,2,0)\), false report \(BCA\), and winner change \(C\to B\);
- direct first- and second-round Borda scores for the normalized representative.

Run:

`python3 verify_baldwin5_manipulation.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the finite tie-independent three-candidate statement above.
