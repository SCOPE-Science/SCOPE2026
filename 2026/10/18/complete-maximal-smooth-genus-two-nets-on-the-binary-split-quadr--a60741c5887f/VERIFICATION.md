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

# Exact reproduction

From the extracted package directory, execute `sh verify_all.sh`. The first stage uses four affine charts and exact Gröbner bases to produce 1116 geometrically smooth masks. The second stage counts 44070 pencils, 250992 pencil-extension incidences, 8964 distinct nets, no possible all-smooth four-space extension, 249 polarized automorphism orbits each of size 36, and 14 rational-point spectra. Output terminates with `VERIFY_OK`.

The complete computation was executed successfully using SymPy and g++ with the scripts attached. The checked output is `verification_output.txt`. Smoothness over the algebraic closure follows algebraically from unit Jacobian ideals; mere sampling over finite extensions would not suffice. Counts apply only to the fixed bidegree-\((2,3)\) coefficient space over the two-element field. Independent external audit has not been performed.
