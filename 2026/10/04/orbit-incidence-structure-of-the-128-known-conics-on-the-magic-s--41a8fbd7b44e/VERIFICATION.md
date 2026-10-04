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

The replay script checks the finite identities used in the proof from exact integer and polynomial arithmetic.

For the automorphism action it verifies
\[
|S|=256,
\qquad
|\operatorname{Stab}_S(C_0)|=4,
\qquad
|S\cdot C_0|=64,
\]
and hence, after the published square reflection exchanges the two 64-families,
\[
|\operatorname{Stab}_{\operatorname{Aut}(V)}(C_0)|=2048/128=16.
\]

It enumerates the four projective sign classes solving
\[
a^2=b^2=c^2
\]
and checks an explicit polynomial parametrization of
\[
b^2+c^2=2a^2.
\]

It also verifies the unique nonzero term in the chosen Jacobian determinant and obtains
\[
-6^6a^2b^2c^2.
\]
The three coordinate-zero cuts of the conic have two projective points each, producing the \(4+2\) node split used in the proof.

Finally the script checks
\[
128\cdot4=256\cdot2,
\qquad
128\cdot4=128\cdot4,
\qquad
128\cdot2=64\cdot4.
\]

These finite checks do not verify the published automorphism theorem, the classification of the three singular orbits, or the fact that the 128 conics are exactly the components of \(Z_3\). Those geometric inputs are cited in `RESULT.md`.

The saved replay output ends in `VERIFY_OK`.
