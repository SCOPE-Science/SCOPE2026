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

# Reproduction and verification

Execute `python3 check_exact.py` with a standard Python 3 interpreter. The computation uses integer pairs representing elements of \(\mathbb Z[\varphi]\) and exact sign tests in \(\mathbb Q(\sqrt5)\), with no external libraries. It requires no network access and reads no input files.

Observed successful terminal line:

`VERIFY_OK 32 vertices, 30 rhombic facets, 39 exact levels, 20 isolated maximizers`

The checker verifies all \(64\) signed sums in the six-generator realization; the exact support inequalities from \(15\) generator pairs; all thirty supporting rhombi; the \(20+12\) vertex-valence split; zonotope volume \(20\); the full \(35\,960\)-quadruple histogram; \(2\,340\) degenerate cases; \(39\) distinct levels; unique top determinant \(6+8\varphi\) of multiplicity \(20\); all long equilateral triangle and antipodal apex relations; and absence of any two top quadruples sharing three vertices. The generated histogram matches the supplied `volume_spectrum.json` entry by entry.

Exactness is for this finite point-set calculation. The extension to arbitrary contained tetrahedra follows mathematically from the separate determinant-affinity argument in `RESULT.md`; finite tests alone do not prove that step. Independent validation and a definitive search of all historical tables remain unperformed.
