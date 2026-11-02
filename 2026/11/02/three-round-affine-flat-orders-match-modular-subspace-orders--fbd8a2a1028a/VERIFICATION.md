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

# Verification record

The extension lemma and its ten-case table give a mathematical proof for every positive finite affine dimension and every field. The programs are **computational checks only**. The certificate enumerates all ten truncated-rank/corank pointed spectra as explicit relation/mask pairs. Equality of those complete spectra, rather than merely their sizes, is the invariant needed for the three-round back-and-forth argument.

To reproduce in an extracted package directory, run `python3 symbolic_profiles.py` and `python3 geometric_enumeration.py` using Python 3 standard libraries only. The symbolic program writes `symbolic_certificate.json` and tests its finite threshold classification through lattice rank sixty. The geometric program independently constructs subspace bit sets over prime fields, uses direct incidence to determine third-move patterns, and tests binary affine dimensions one through six, further prime-field cases, and corresponding linear-subspace lattices.

Both programs returned their `PASS` checks in the supplied execution. The direct program's exact output is provided in `geometric_enumeration.out`; `symbolic_profiles.out` records the other output. This check does not constitute a proof for arbitrary dimensions, arbitrary fields, or a claim of external mathematical certification.
