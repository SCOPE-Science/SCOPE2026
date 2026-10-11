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
The primary source was checked for the precise degree-three inputs: four nonseparating and three separating vanishing cycles, pairwise intersection divisibility by \(3\), the Picard--Lefschetz first-homology action, the global product relation, and \(\pi_1(S(E,3))\cong\mathbf Z^2\).

The standard Lefschetz-handle quotient gives
\[
H_1(S(E,3);\mathbf Z)\cong H_1(\Sigma_2;\mathbf Z)/\langle[\delta_i]\rangle.
\]
The torsion-free rank-two quotient makes the vanishing lattice primitive of rank two. Reduction modulo \(3\) therefore gives a two-dimensional subspace, and the source's intersection divisibility makes it Lagrangian.

`artifacts/verify_mod3_monodromy.py` checks the remaining finite algebra over \(\mathbf F_3\). A successful replay prints exactly:

`VERIFY_OK projective_lines=4 unique_zero_sum_multiset=true span_dim=3 group_order=27`

The verifier is a check of the finite linear-algebra lemma, not a substitute for the source-dependent topology. The result does not verify the integral monodromy image or full mapping-class-group image.
