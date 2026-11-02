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

Run `python3 verify_open_cubic.py --write-table open_cubic_spectra.csv` with Python 3 (standard library). The executed script reported `W(E6): 51840 elements; 25 conjugacy classes; 15 first-field polynomials; 25 formal zeta signatures`, checked its computed class sizes, element orders, and Picard traces against the published 25-class table, and ended in `VERIFY_OK`.

The construction includes 27 geometric lines, 135 unordered meeting pairs and 270 line–pair flags. For each Frobenius class the script compares point counts from orbit lengths with those obtained from fixed points of Frobenius powers for extension degrees 1 through 24. It checks each explicit six-point blowup in \(\mathbb P^2(\mathbb F_{17})\) has no collinear triple or common conic; its two direct point counts are 57 and 55, with 1 and 3 Eckardt points.

The uniform formula is proved symbolically from normalization of a reduced line union and the \(S_3\) character identity at Eckardt points. No finite-field sample alone establishes its infinite scope. The table provides formal possible Weyl actions and cannot independently prove their realization over a given field. Review is not independent validation.
