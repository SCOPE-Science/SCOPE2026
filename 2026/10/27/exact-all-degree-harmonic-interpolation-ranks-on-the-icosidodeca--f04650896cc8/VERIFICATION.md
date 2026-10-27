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
# Reproducible checks

Run `python verify.py` with Python 3.10 or later. It requires no third-party packages. Its construction uses the exact icosahedral edge-midpoint coordinates in \(\mathbb Q(\sqrt5)\). The script calculates exact characteristic ranks in degrees \(0\)–\(14\), verifies an independent degree-six annihilating polynomial, and performs prime-field elimination at degrees \(15\)–\(199\). It checks primality of the modular prime and the square-root residue used for reduction. Its output must equal `verify_output.txt`. For degrees \(\ell\ge200\), the proof's explicit Bernstein inequality establishes strict diagonal dominance; code is not substituted for this infinite argument.

Optionally install `requirements.txt` and run `python crosscheck.py`: a separately constructed complex spherical-harmonic evaluation matrix has the same ranks in degrees \(0\)–\(16\). This is a finite numerical cross-check, not independent mathematical certification. No external specialist audit has been performed.
