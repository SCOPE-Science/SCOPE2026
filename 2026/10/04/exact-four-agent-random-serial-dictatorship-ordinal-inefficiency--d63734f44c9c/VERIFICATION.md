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
The embedded `verify_rsd4_ordinal_efficiency.py` is a standard-library-only exact replay.

It checks every labeled strict profile for \(n=1,2,3\) and finds no ordinally inefficient RSD outcome. For \(n=4\), it uses two exhaustive routes.

Route A enumerates all \(17{,}550\) anonymous multisets of four rankings, computes exact RSD support over all \(24\) priorities, restores the exact number of agent labelings, and canonicalizes under all \(24\) object relabelings. It verifies:
- \(762\) total symmetry classes;
- \(153\) inefficient symmetry classes;
- \(3{,}270\) inefficient anonymous multisets;
- labeled inefficient weight \(68{,}976\);
- inefficient orbit-size histogram \(72:4,\ 144:3,\ 288:55,\ 576:91\);
- inefficient preference-multiplicity histogram \(2+2:4,\ 2+1+1:30,\ 1+1+1+1:119\).

Route B independently enumerates all \(24^4=331{,}776\) labeled profiles directly and again obtains \(68{,}976\) inefficient profiles. On every labeled profile it verifies that cyclicity of the Bogomolnaia--Moulin ordinal relation is equivalent to the presence of a reciprocal pair.

The replay also reconstructs the standard four-agent \(2+2\) witness exactly, including its RSD matrix.

Run:

`python3 verify_rsd4_ordinal_efficiency.py`

The first output line must be:

`VERIFY_OK`

The finite computations prove only the finite claims stated above. No inference to arbitrary \(n\) is made.
