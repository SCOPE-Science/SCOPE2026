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
The proof in `RESULT.md` is symbolic and valid for every \(n\ge1\) and \(d\ge1\). The replay program checks consequences rather than extrapolating from finite cases.

For each \(1\le n\le7\) and \(1\le d\le6\), `verify.py` constructs the signed or unsigned action on pair-indexed top classes, verifies all Coxeter relations for adjacent transpositions, and then exhaustively evaluates every permutation in \(S_n\). The computed traces agree with
\[
\binom{X_1}{2}+X_2
\]
for the off-diagonal module when \(d\) is even and
\[
\binom{X_1}{2}-X_2
\]
when \(d\) is odd. It also checks the diagonal fixed-point contribution in even \(d\), the predicted torsion-degree pattern, and the reduced Euler characteristic.

The final replay line is:
```
VERIFY_OK cases=42 characters=all_permutations_n_le_7 coxeter=yes parity_sign=yes
```
The program does not attempt to certify Kallel--Sjerve's published finite-subset-space theorem; that theorem is used as literature input and the new equivariant deduction is reconstructed explicitly in `RESULT.md`.
