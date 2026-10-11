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
# Verification

`verify.py` embeds the two complete \(66\)-facet presentations and uses only the Python standard library.

For each complex it reconstructs
\[
f=(12,57,148,165,66).
\]
Unimodular reduction of the integral triangle-to-edge boundary map yields rank \(46\), leaving a rank-\(102\) integral \(2\)-cycle lattice. Expressing tetrahedral boundaries in that lattice and reducing again gives a primitive rank-\(100\) sublattice, so
\[
H_2\cong\mathbb Z^2.
\]

Every four-vertex subset is then exhausted. Exactly \(72\) induced tetrahedral boundaries are missing three-simplices in each complex, and all \(144\) boundaries across the pair have nonzero primitive integral coordinates.

Up to sign, the exact integral spectra are
\[
33,33,3,3
\]
for \(\mathbb{CP}^{2}\#\mathbb{CP}^{2}\), and
\[
33,33,6
\]
for \(\mathbb{CP}^{2}\#-\mathbb{CP}^{2}\).

Reducing the same exact coordinate vectors modulo two yields
\[
33,33,6
\]
for both complexes.

Exact successful output:

`VERIFY_OK f_both=12,57,148,165,66 H2_Z=Z^2 min_vertex_support=4 carriers=72_each all_primitive=yes integral_spectra=33,33,3,3|33,33,6 mod2_spectra=33,33,6|33,33,6 reps_pp=1236|1359|1239|56710 reps_pm=1234|12310|12410`
