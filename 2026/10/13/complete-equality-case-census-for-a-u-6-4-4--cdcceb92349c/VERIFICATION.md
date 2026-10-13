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
# Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The program uses only the standard library.

The verifier performs the following checks from first principles: it enumerates all \(720\) permutations of six symbols; computes Ulam distance as six minus the longest common subsequence length; constructs the \(132\)-vertex normalized compatibility graph and its \(612\) edges; enumerates exactly \(298\) triangles; verifies that no triangle has a common neighbor, which rules out any normalized five-word code; generates all labeled maxima by all \(720\) symbol relabelings and deduplicates to \(53{,}640\); checks every maximum has six distances equal to \(4\); constructs the declared \(1440\)-element relabeling/reversal action and verifies the \(57\)-orbit distribution; and checks that none of the \(298\) normalized maxima is a subgroup.

The included `verification_output.txt` records the fresh replay used for this package. The computation is finite and exhaustive only for the stated \((n,d)=(6,4)\) parameter and does not certify any larger parameter.
