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
The embedded `verify_nanson_baldwin_first_unique_divergence.py` uses exact finite enumeration with only the Python standard library.

It enumerates every anonymous four-candidate profile with one through five voters as a weak composition into the \(24\) strict ballot types.

Baldwin is treated as a correspondence over all legal eliminations among tied lowest-Borda candidates. A singleton winner set therefore means the winner is independent of every such tie-breaking choice.

Nanson simultaneously eliminates every candidate whose current Borda score is strictly below the average. If no candidate is below average while more than one survives, the surviving set is returned as non-unique rather than imposing an artificial tie-break.

Two implementations are compared on every anonymous profile:
1. a multiplicity engine using precomputed score contributions for each surviving-candidate set;
2. an explicit-ballot engine that expands the profile and recomputes restricted-ballot Borda scores directly.

The verifier confirms:
- anonymous domain sizes \(24,300,2600,17550,98280\);
- zero tie-independent unique divergences for one through four voters;
- \(7232544\) labeled five-voter profiles with unique outcomes under both rules;
- exactly \(384\) anonymous and \(24480\) labeled five-voter divergences;
- incidences \(85/27648\), \(85/25113\), and \(16/4095\);
- exactly \(16\) candidate-relabeling classes, each of orbit size \(24\);
- \(2040\) labeled profiles for each ordered pair of distinct winners;
- the displayed witness and all intermediate scores.

Run:

`python3 verify_nanson_baldwin_first_unique_divergence.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated four-candidate boundary through five voters.
