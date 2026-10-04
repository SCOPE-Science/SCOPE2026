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

The exact verifier uses the coordinate realization of \(A_4\) in the sum-zero sublattice of \(\mathbf Z^5\). It enumerates the \(240\) elements of
\[
S_5\times C_2
\]
as coordinate permutations followed optionally by global sign change.

The nine ray representatives are generated from the source formula for \(s_{I,J}\) together with \(v_1,v_2,v_3\). The script checks their orbit sizes to be
\[
20,60,40,10,30,20,40,60,120,
\]
checks that these nine orbits are pairwise disjoint, and verifies that the total number of rays is \(400\).

The eight maximal-cone representatives are encoded from the explicit subdivisions printed immediately before Proposition 7.6. For every representative the script checks all \(240\) group elements and finds stabilizer order \(1\). It also verifies that the eight cone orbits are distinct. Thus the number of maximal cones is exactly
\[
8\cdot240=1920.
\]

Finally, the script checks
\[
400-4=396
\]
and
\[
1920-(1+396+396+1)=1126.
\]
The saved output ends in `VERIFY_OK`.

Inputs not re-proved by the finite script are the source theorem that the displayed fan is smooth, projective, and complete, and the standard toric facts connecting rays and maximal cones to Picard rank and cohomology.
