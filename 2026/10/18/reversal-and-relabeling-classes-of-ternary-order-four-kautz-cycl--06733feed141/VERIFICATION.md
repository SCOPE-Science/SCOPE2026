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

# Reproduction and boundaries

Execute `python3 verify.py` in a directory holding the extracted program. The program uses the standard library and has no required external data. It builds all allowed length-four words directly and independently enumerates (1) all 4096 two-way local vertex transition systems and (2) every distinguished-edge-rooted depth-first Euler circuit. It asserts identity of the resulting 384-word sets before computing reflection-fixed and relabeling classes.

The decisive exhaustive output is:

`VERIFY_OK q3_order4 cycles_384 reflection_fixed_24 bracelets_204 symbol_orbits_64 unoriented_symbol_orbits_34 achiral_symbol_orbits_4`

The proof in RESULT.md supplies the reduction from the infinite cyclic-word definitions to this finite search and independently proves the all-alphabet parity obstruction. No inference for higher-order census numbers is made from finite examples. No independent audit has been performed.
