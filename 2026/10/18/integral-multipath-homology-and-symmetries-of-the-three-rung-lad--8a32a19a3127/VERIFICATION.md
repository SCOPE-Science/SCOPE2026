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
# Reproducibility and limitations

In a single directory containing the supplied files, run `python3 verify_morse.py`, `python3 verify_symmetry.py`, and `python3 verify_independent.py`. No nonstandard Python package is used. Their expected complete standard output is included as `verify_morse.out.txt`, `verify_symmetry.out.txt`, and `verify_independent.out.txt` respectively.

`verify_morse.py` independently regenerates the face list from the directed-forest definition, regenerates the matched pairs from the fixed toggle order, and checks them against the explicit `matching_certificate.json`. It also verifies every directed face-poset cover against the topological order supplied in the certificate. Then it performs integer chain contractions and checks all pivot coefficients are units, all ten critical cells remain, and all Morse differentials vanish.

`verify_symmetry.py` uses the integral cancellation maps to construct cycles and project their signed graph-automorphism images to critical generators. It verifies the group multiplication identities and prints the rational characters and constituent multiplicities. `verify_independent.py` separately builds the entire complex, computes mod-two ranks without using the Morse matching, and computes reduced Lefschetz numbers directly as signed fixed-face counts.

These are finite, exhaustive checks of one fourteen-arc complex and its four automorphisms. A vanishing integral Morse differential establishes integral homology but **not** the higher attaching maps required for a wedge-of-spheres homotopy claim. The provided files do not establish a result for any other ladder length and have not undergone an independent external audit.
