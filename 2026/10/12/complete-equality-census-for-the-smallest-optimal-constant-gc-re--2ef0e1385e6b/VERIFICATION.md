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

The verifier uses only the Python standard library and performs complete finite checks:

1. Generate all \(96\) length-four DNA words of GC-content \(2\).
2. Retain the \(72\) words whose self reverse-complement distance is at least \(3\).
3. Build constrained compatibility in two independent formulations and require exact equality.
4. Enumerate all maximal cliques and obtain maximum size \(6\) with exactly \(512\) maxima.
5. Independently enumerate all six-cliques and require exact agreement with the \(512\)-code set; independently require that no seven-clique exists.
6. Build the ordinary constant-GC Hamming graph on all \(96\) words and enumerate its \(128\) maximum twelve-word codes.
7. Identify exactly \(16\) reverse-complement-invariant ordinary maxima, exactly \(8\) without self-reverse-complement words, and verify that these \(8\) are exactly the parents of all constrained maxima.
8. Enumerate all \(64\) transversals of each viable parent and require their union to equal the direct \(512\)-code census.
9. Generate all \(256\) stated symmetries, verify graph preservation, and reproduce the four \(128\)-element orbits and stabilizer order \(2\).

The expected terminal line is:

`VERIFY_OK maximum=6 labeled_maxima=512 parents=8 children_per_parent=64 orbits=4 orbit_sizes=128,128,128,128 stabilizers=2,2,2,2`

The computation is exhaustive only for the stated finite parameter.
