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
# Verification record

The full source-code reproduction was executed from the bundled files. Python 3 with SymPy generated \(279\) quartic projective orbits, with \(78\) geometrically smooth representatives weighted to \(10{,}920\) equations. Two independent C++17 programs each checked rational even-contact lines over fields \(\mathbf F_{2^k}\) for every \(k=1,2,3,4,5,6,7\), covering \(546\) representative-extension pairs. They used different coefficient computations and distinct irreducible field polynomials for degrees three to seven. Both returned identical vectors of fixed-line counts; the final Python program compared each entry, reconstructed Frobenius cycles using divisor inversion, and verified the whole ten-stratum table, orbit weights, and stable Hasse--Witt rank predictions.

The encoded representative `2566` yielded exactly seven lines over \(\mathbf F_{128}\), one Frobenius orbit of length seven and none over extensions of degree at most six. Its seven coefficient pairs and equation appear in RESULT.md and the generated data tables.

Finite extension checking through degree seven proves all cycle partitions here **only because** the separate geometric theorem bounds the total number of geometric bitangents by seven. The computation does not prove that theorem for arbitrary characteristic-two quartics; it invokes and independently cross-checks the known result. These are same-project checks, not independent external audit.

Run from the directory containing the packaged sources with the commands in RESULT.md. The generated `quartic_orbits.json`, `smooth_orbits.txt`, `splittings.tsv`, `independent_fixed_counts.txt`, `splitting_distribution.csv`, and `splitting_orbits.csv` are included as separate inspectable evidence.
