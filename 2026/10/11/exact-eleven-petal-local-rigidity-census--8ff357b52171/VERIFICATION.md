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

The bundled file `artifacts/petal11_verify.cpp` is a standalone C++17 verifier.

It represents each cyclic position class by its unique word beginning with \(0\), so the enumeration has exactly
\[
10!=3{,}628{,}800
\]
cases. For each word it implements the source definitions directly:

- \(\mathsf T^-\): some cyclically adjacent letters are consecutive integers;
- \(\mathsf X\): all eleven basepoints are tested, the remaining positions are paired as in the source, every admissible \(m,w\) is checked, and the exact interval nesting condition is enforced;
- \(\mathsf R\): add \(1\) to every height modulo \(11\);
- \(\mathsf S\): reverse the word and complement heights by \(h\mapsto10-h\).

The verifier checks the source's explicit seven-petal crossing-exchange example and confirms that each of the three named nine-petal hard representatives has neither local move. It then enumerates the full eleven-petal space and the complete \(\langle\mathsf R,\mathsf S\rangle\)-orbit of every locally rigid candidate.

Compile and run:

`g++ -O3 -std=c++17 artifacts/petal11_verify.cpp -o petal11_verify && ./petal11_verify`

Expected output:

`VERIFY_OK total=3628800 no_Tminus=393410 no_X=1971006 local_rigid=325398 dihedrally_local_rigid_words=270630 dihedral_orbits=12786 orbit_sizes=1:8,11:954,22:11824`

The enumeration proves only the finite combinatorial claim. It does not certify knot types and does not turn local rigidity into a hardness theorem.

No independent audit has been performed.
