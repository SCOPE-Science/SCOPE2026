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
The proof is symbolic.

The packaged checker `artifacts/verify.py` models the cyclic subgroup
\[
C_{2^{m-1}}
\]
by character indices modulo
\[
2^{m-1}.
\]

For the dihedral and semidihedral split groups it computes conjugation orbits for exponents
\[
-1
\quad\text{and}\quad
2^{m-2}-1.
\]
For the generalized quaternion family it uses the same inversion action.

For the modular family it uses exponent
\[
2^{m-2}+1,
\]
checks that the invariant cyclic characters are exactly the even-index characters, and reconstructs the linear codegree distribution from
\[
C_{2^{m-2}}\times C_2.
\]

For every
\[
4\le m\le12,
\]
the checker verifies the exact pseudo-algebra formulas and the degree-squared identities.

It also prints the order-\(16\) boundary formulas.

The checker returns `VERIFY_OK`.

Finite computation is not used to prove the infinite family.
