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

## Reproduction

Run `python3 verify.py` in the same directory as `class_character.json`; no third-party Python packages are required. This independently reconstructs all 12,960 proper four-colorings, 221,520 polyhedral Hom cells, the complete connected coloring graph, the classwise signed cellular Lefschetz table and the two representation projections.

The exact arithmetic checks yield \(\chi(X)=240\), \(\widetilde\chi(X)=239\), signed multiplicity \(+1\) for \(S^{(3,2)}\boxtimes\mathbf 1\) and \(-1\) for \(S^{(2,2,1)}\boxtimes\varepsilon_4\). The recorded output ends with `VERIFY_OK`.

## Limits

The enumeration establishes exact finite cellular data and the resulting virtual character. The existence of even- and odd-dimensional homology follows from character semisimplicity and the Hopf trace theorem. No integer boundary Smith normal form, grading-by-grading homology, full homotopy decomposition, or independent external assessment is provided.
