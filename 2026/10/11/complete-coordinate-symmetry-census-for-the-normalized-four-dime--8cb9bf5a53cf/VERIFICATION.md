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

The verification reconstructs the finite group calculation from first principles.

It enumerates all \(24\) permutations in \(S_4\), generates all \(30\) subgroups, forms their orbits on
\[
U_4=\{0,1\}^4\setminus\{(1,1,1,1)\},
\]
and for each orbit representative counts the permutations having the required homochiral parity and centralizing its point stabilizer.

The resulting fixed-family values are checked against the complete expected conjugacy-type table. In particular the source's structured-family values
\[
32,\qquad768,\qquad6912
\]
are recovered.

Burnside's formula is evaluated directly from element fixed sets and checked to equal
\[
53{,}496{,}608{,}995{,}008.
\]

The verifier then performs descending subgroup-lattice subtraction
\[
E(H)=F(H)-\sum_{K>H}E(K)
\]
for every concrete subgroup \(H\), aggregates exact stabilizers by conjugacy type, and checks the assignment and orbit counts in the finding.

It separately asserts that every subgroup containing a three-cycle has fixed count zero.

The finite calculation is exhaustive for this normalized \(S_4\)-action. It does not test coarsening closure or any later geometric certificate condition, and no conclusion about those conditions is inferred from the symmetry census.
