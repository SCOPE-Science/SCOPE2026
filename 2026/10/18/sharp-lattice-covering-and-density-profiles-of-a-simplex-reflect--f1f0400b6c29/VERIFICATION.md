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

# Reproducibility and scope

After extracting every embedded file into one directory, run `python verify_covering.py` with Python 3. The script requires only the standard library and prints `PASS: 6728 exact rational grid-point checks, eight exact area and reciprocity tests, and exact endpoint/deep-hole identities.`

It verifies the stated polygon vertex representation and shoelace area, the reciprocal reflection law, deepest-hole certificates at rational parameters, and periodic gauge domination across eight finite rational grids. Every comparison uses `fractions.Fraction`, not floating-point rounding. The exact rational tests check the implementation and corroborate representative cases but do not exhaust the continuum. The exhaustive continuum proof is the covering partition and matching obstruction in `RESULT.md`, with its separately explained strict equality cases and analytic density derivative.

No independent audit has been performed. The source comparison is limited to publications and mathematical descriptions actually inspected; an earlier equivalent unlocated computation remains possible.
