---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The normal form F=P_X A(Y)+P_Y B(X), with one syzygy gauge, has 9 ternary parameters and (3^9-1)/2=9841 projective equations. Direct enumeration found 3504 rationally nonsingular equations. An independently implemented GL2 generator action and four-chart characteristic-three Groebner singularity tests gave 56 factor-preserving rationally smooth orbits and precisely seven geometrically smooth orbits of sizes 18,18,24,24,36,72,72, totaling 264. Factor swap gives four full orbits of sizes 36,36,48,144. Independently computed nine-by-nine Cartier/Hasse-Witt coefficient matrices [x^(3i-k)y^(3j-l)] f^2 for seven representatives (6898,6904,6919,7858,7876,8344,8356); ranks and ninth-power stable ranks respectively (8,8,8,8,9,8,9). Thus exactly 216 cases have p-rank8/a=1, and the 48 ordinary ones form one full orbit; genus nine from adjunction. The independent orbit implementation required correction of an accidental projective normalization of generator columns, then produced the exact results; no failed interim computation was concealed.

## originality

PASS

Best-of-knowledge mathematical implication assessment, comparing identical objects/parameters and stronger results rather than title similarity; known preliminary counts, matrix formulas and examples are credited, not treated as new.

## value

PASS

This is a complete, naturally delimited embedded genus-nine family over F3 with a sharp two-valued p-rank/a-number stratification and a unique ordinary ambient orbit. These are useful arithmetic moduli data not implied by the known 264-equation count and help distinguish ordinary versus nonordinary minimal space-filling curves.

The dated certificate retains the supplied scientific assessment, sources and limitations.
