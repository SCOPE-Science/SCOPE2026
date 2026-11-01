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

Run `python3 verify_multipath_k34.py` from the folder containing the checker. It uses only the Python standard library. Its last line is `K34_BIDIRECTED_MULTIPATH_MIXED_WEDGE_EXACT_OK` if all assertions pass.

The completed checks are: two independent exhaustive face enumerations; the face counts \((1,24,204,768,1296,864,144)\) in degrees minus one through five; all \(144\) maximal six-arc paths; \(1608\) augmented matching pairs, or \(1607\) ordinary pairs; critical ordinary cells in dimensions zero, three and four with multiplicities \((1,37,48)\); all \(13104\) Hasse cover incidences and global matching acyclicity; zero entries in the exact \(37\times48\) integral Morse boundary; independent direct mod-two boundary ranks \((1,23,181,587,672,144)\).

The mod-two calculation is independent corroboration. The infinite mathematical principles invoked after finite verification are the standard discrete-Morse CW theorem and the Hurewicz isomorphism for a wedge of three-spheres. No external or independent audit has been performed. The proof asserts only the specified seven-vertex digraph.
