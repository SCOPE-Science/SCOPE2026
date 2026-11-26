---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

PASS applies to repairs/4/RESULT.md, not to the frozen definition. Frozen RESULT.md line 26 uses (x_i,x_5,x_6) with x_6=x_0. With that definition the distance is six iff the two words differ in their (x_0,x_5) pair: otherwise two windows certainly agree. Thus its true maximum is four, with 16^4=65536 labeled maxima, and the full dihedral action need not preserve admissibility. The replacement uses consecutive cyclic triples (x_i,x_{i+1},x_{i+2}), as in the frozen proof and programs, and specifies pair-distance five in the comparison. Every window projection must then be injective; the eight words abcabc attain the bound. The independent replay (branches/b14a181c-550e-434d-8163-b4e6fcc9fe43/record4_independent_check.py and .out) checked all 4096 ordered word pairs by two definitions, enumerated all eight-cliques, and reproduced 776 maxima, 232 affine and 544 nonaffine, with all ten stated orbits and stabilizers. In the two size-96 orbits, one is affine and one is not. Translating by a codeword reduces the affine test to closure under addition, and translations and dihedral window permutations preserve compatibility. The difference from d_pair>=5 consists exactly of the three cyclic masks 001001, with 32 unordered pairs per mask. The other package files already concern consecutive triples and did not require replacement; the frozen verifier was inspected, not executed.

## originality

PASS

For the repaired consecutive-window claim, the bound and linear attainment are prior. The scientifically distinct claim is the complete census of arbitrary codes at binary n=6 and d_3=6, with affine split and translation-dihedral classification. No covering census was established by the bounded comparison.

## value

PASS

This is the shortest length on which six three-symbol disagreements are possible. The equality layer describes every eight-word set with simultaneous bijective cyclic three-window projections. It measures the abundance and orbit complexity of nonaffine equality cases beyond known linear attainment, and it provides an exact contrast with the closely related affine-rigid pair-read problem. These features motivate the precise finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
