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

# Reproduction and limitations

From this package, compile `verify_cpp.cpp` with a C++17 compiler, run it with `optimizers_cpp.txt` as the output file, and run `python3 verify_py.py optimizers_py.txt`. Both programs independently reconstruct the word set and compatibility graph, enumerate all maximal cliques and write lexicographically sorted optimum codes. Confirm both outputs match `optimizers.txt` byte-for-byte and have SHA-256 `63a11362c2775f93caebe0a2c00b94afddf3d4e2aab491055efdb9dabf18fdea`. The catalogue must be \(844{,}324\) bytes with \(4{,}996\) rows. The programs report \(272\) vertices, \(11{,}206\) edges, \(10{,}369{,}145\) recursion calls, \(4{,}887{,}344\) maximal cliques, and maximum clique size \(13\). Run `python3 verify_symmetry.py optimizers.txt` to independently verify all catalogued codewords, the symmetry orbits and the distance-four property.

These are exhaustive checks for a finite graph, not experiments supporting an extrapolation. The public preprint and article comparisons establish the documented context, but an independent literature audit remains unperformed.
