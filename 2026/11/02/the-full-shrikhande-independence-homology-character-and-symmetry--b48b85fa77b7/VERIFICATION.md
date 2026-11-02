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

# Reproducibility and verification

Execute `python3 verify_shrikhande_symmetry.py`. It requires only the Python 3 standard library. Expected terminal marker: `SHRIKHANDE_INDEPENDENCE_FULL_192_EQUIVARIANT_CHARACTER_OK`.

Checks are performed from the defining six graph differences rather than external graph packages: 16 vertices, valency six, exactly two common neighbors for every distinct vertex pair, the complete independent-face count \((16,72,96,16)\), 88 discrete-Morse pairs with critical cells only in degrees zero and two, full topological sorting of 200 Hasse nodes and 496 cover relations, the complete set of 12 linear stabilizer maps and 192 affine symmetries, the signed trace for each automorphism, the frequency distribution, and integer Fourier multiplicities of the translation restriction.

The written group upper-bound argument requires the six-neighbor induced graph to be a cycle and the nine two-neighbor signatures to be distinct. Both finite conditions are tested by the checker. The rational quotient calculation additionally uses exactness of coinvariants for finite groups in characteristic zero after barycentric subdivision. The program does not compute integral homology of quotients and is not an external independent audit.
