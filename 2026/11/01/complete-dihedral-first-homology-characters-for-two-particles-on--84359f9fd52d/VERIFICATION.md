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
# Verification of the wheel configuration-space character

The check uses `verify.py` and Python 3's standard library only. Run `python3 verify.py` in the directory containing the verifier. The recorded execution output is in `verification_output.txt`.

For each integer rim length from four through forty, the program independently builds the wheel graph, all zero-cells, all oriented one-cells, and all oriented two-cell squares of its unordered two-particle cubical model. It computes the mod-two cellular boundary operators directly, checks that their composition vanishes, verifies full second-boundary rank and connectedness from first-boundary rank, and compares actual cell counts against the formulas. These checks use exact integer bit elimination and involve no floating-point tolerance.

It then enumerates every rotation and reflection, computes all three signed cellular Lefschetz traces by fixed-cell enumeration, and compares each trace to the corresponding symbolic parity case. All 1,628 group elements across the tested wheel sizes agree, and the character averages give two cyclic invariant lines and zero full-dihedral invariant lines. The recorded execution terminates with `WHEEL_CONFIG_CHAR_VERIFY_OK`.

Finite validation cannot prove the asserted formulas for all wheel lengths. That universal statement is supplied by the separate fixed-cell orbit classification and the integral path-based argument proving vanishing top homology. The script does not compute the full fundamental groups, integral representation lattices, or independent publication priority.
