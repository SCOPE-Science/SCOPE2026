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

# Reproducibility
Run `python3 verify.py` from the directory containing the files. The checker constructs two complete parent-child incidence representations for every permutation length from three through eight: one by deleting each entry of each full permutation, another by inserting all possible new values into each child. It creates the sorted multiset of parent-pair keys appearing together in each distinct child, and uses exact integer run lengths to count common children.

For each length the checker verifies that the two complete positive-intersection histograms and the actual maximizer key sets coincide. It also generates every pair in the proposed local \(2413\)/\(3142\) construction and checks exact set equality with the extremizers. The supplied `check_output.txt` records the successful replay and exact histograms. No third-party packages, cached tables, third-party downloads, random sampling, or approximate floating-point arithmetic are used.

The exhaustive range is exactly \(3\le n\le8\). Exhaustion of this finite range does not prove analogous upper bounds for arbitrarily long permutations. The proof of the four-block lower-bound construction holds for all lengths, but the classification outside the tested range is left open. No independent validation has been performed.
