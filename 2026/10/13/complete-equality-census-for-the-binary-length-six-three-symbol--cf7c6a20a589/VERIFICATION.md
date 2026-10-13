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

The verifier uses only the Python standard library and performs the following complete checks:

1. Generate all \(64\) binary words of length six.
2. Compute every cyclic \(3\)-symbol distance twice: by direct comparison of the six length-three read windows and independently from the cyclic coverage of the support of the difference word.
3. Require the two complete distance matrices to agree.
4. Build the minimum-distance-\(6\) compatibility graph.
5. Enumerate every maximal clique by exact Bron--Kerbosch search and obtain maximum size \(8\) with exactly \(776\) maxima.
6. Independently enumerate all eight-cliques by an increasing-vertex intersection recursion and require exact agreement with the \(776\)-code set.
7. Independently enumerate nine-cliques and require that none exist.
8. Test every maximum for affine closure after translation to zero, obtaining exactly \(232\) affine and \(544\) nonlinear maxima.
9. Apply all \(64\) translations and all \(12\) dihedral coordinate symmetries, then reproduce the ten orbit sizes and stabilizers.

The expected terminal line is:

`VERIFY_OK maximum=8 labeled_maxima=776 affine=232 nonlinear=544 orbits=10 orbit_sizes=8,24,24,32,48,64,96,96,192,192 stabilizers=96,32,32,24,16,12,8,8,4,4`

The computation is finite and exhaustive for the stated parameter only.
