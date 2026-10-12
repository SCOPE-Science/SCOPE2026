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

Run `python3 verify.py`.

The program uses only the Python standard library. It performs the following complete finite checks:

1. Reconstruct all \(32\) binary words of length five.
2. Build compatibility independently from \(d_A(x,y)\ge2\) and from disjoint one-error Z-channel balls, then require the two graphs to agree exactly.
3. Enumerate every maximal clique by an exact Bron--Kerbosch search.
4. Require maximum clique size \(6\) and exactly \(120\) maximum cliques.
5. Apply all \(120\) coordinate permutations and optional global complementation, require that the action preserves the full maximum set, and recompute all equality orbits and stabilizers.

The expected terminal line is:

`VERIFY_OK maximum=6 labeled_maxima=120 orbits=3 orbit_sizes=30,30,60 stabilizers=4,8,8`

The computation is finite and exhaustive. It does not establish any claim for other blocklengths or error radii.
