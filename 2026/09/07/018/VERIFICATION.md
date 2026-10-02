---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-02.md",
      "INDEPENDENT_AUDIT_2026-10-02.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The frozen artifacts/kasteleyn_census.py was rerun in an isolated output directory. For the five claimed 6-by-n boards it reproduces pure dimer counts 6728,31529,167089,817991,4213133; 45,123,156,198,240 two-hole symmetry orbits (762 total); and unique adjacent-corner maxima 3364,16926,85659,431819,2182406. Pfaffian and independent transfer-DP values agree on every one of the 762 orbits. The orientation-control case gives the claimed failure at two interior holes, while boundary/Temperley checks pass. These finite exact comparisons support the stated ranges only.

## originality

PASS

The closest monomer-dimer Pfaffian formula is a broad computational formula, but the inspected papers do not assert the exact symmetry-orbit tables and location of maxima for these five boards. A formula capable of producing an answer after 762 computations does not itself mechanically state or imply the extremal classifications; the exact data are independently useful.

## value

PASS

The fixed-height rectangular dimer model and monomer-position dependence are canonical; a full symmetry-reduced two-hole census, exact maxima and Pfaffian-vs-DP cross-check form a reusable finite statistical-mechanics benchmark. The placement optimization is not an arbitrary small negative check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
