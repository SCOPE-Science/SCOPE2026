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

# Exact reproduction

Run `python3 verify_translation.py` using Python 3 standard library. The verifier exhausts all \(2^{16}\) masks; checks face vectors \((16,72,96,16)\) for Shrikhande and \((16,72,96,24)\) for rook; checks the four translation subgroup coset families of maximal independent sets; constructs 88 and 96 Morse pairs respectively; checks acyclicity of the complete 496- and 528-incidence Hasse diagrams; checks mod-two boundary ranks; computes oriented simplex signs and complete fixed-face Lefschetz traces; performs Fourier inversion with exact integer pairs; and verifies all claimed matrices, nonnegative multiplicities and dimensions. A local execution ended with `VERIFY_OK`.

There is no independent external validation. The character concerns rational homology of only the 16-element translation group. The proof does not establish integral representation-lattice classification or full graph-automorphism representation.
