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

# Finite proof and reproducibility record
Run `python3 verify.py`, using only Python 3 standard-library modules, on the accompanying source file. Its expected terminal output is embedded as `verification_output.txt`. It enumerates exactly thirty vertices, forty-five edges, thirty neighborhood facets, 27,535 simplices, 13,495 valid elementary simplicial collapses, and a connected two-complex with face vector \((30,200,315)\). Its exact binary triangle boundary rank is 171. Since the connected edge cycle space also has dimension 171, the rational rank must equal 171, giving \(\dim\widetilde H_2=144\) and vanishing other reduced rational homology. A field-rank computation is not being misused as an integral torsion certificate.

The group-action verification checks all 720 label permutations preserve the radius-two ball collection. For every permutation it exactly evaluates the signed Lefschetz trace by enumeration of admissible vertex-orbit unions. For all eleven conjugacy classes it separately enumerates every stabilized nonempty simplex and computes its orientation sign; these independent calculations agree with the group-wide trace table. An exact Young-tabloid alternating formula constructs all eleven irreducible symmetric-group characters and confirms their orthogonality and the displayed Specht decomposition. The induced character calculation follows directly from the usual finite-group induction formula and its special centralizer counts. No probabilistic sampling, assumed certificate, external proof checker or infinite-case extrapolation is used.

The previously published sphere-wedge homotopy type is acknowledged as prior work. The current result concerns rational homology and natural label symmetries only; no integral equivariant statement, full outer-automorphism action or independent external audit is asserted.
