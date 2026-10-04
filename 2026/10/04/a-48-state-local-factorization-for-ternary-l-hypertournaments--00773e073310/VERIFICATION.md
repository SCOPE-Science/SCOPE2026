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

The finite checker implements the two clauses of Huang--Pawliuk--Sabok--Wise Definition 7.2 directly for arity three. It does not use the parity characterization as its acceptance test.

For one unordered triple there are six injective ordered enumerations, so the checker tests all \(64\) possible truth sets. For every truth set it verifies: (i) every ordered enumeration can be coordinate-permuted to a true one; and (ii) for every coordinate permutation and every starting enumeration, the three cyclic rotations are not all true after applying that same coordinate permutation. The accepted truth sets are then independently compared with the parity-coset criterion.

The checker asserts that exactly \(48\) truth sets survive, with counts \(6,15,18,9\) according to relation size \(1,2,3,4\). It also expands \((1+3z+3z^2)^2-1\) directly and matches those coefficients.

For tuple orbits with repeated coordinates, the checker generates restricted-growth strings for set partitions through arity five, verifies the Stirling recurrence counts, and checks the formula \(b_n=\sum_k {n\brace k}48^{\binom k3}\). It prints the corresponding first values.

The script verifies only the finite combinatorial core. The free-amalgamation and homogeneous-orbit identifications are proved in `RESULT.md`; they are not inferred from finite experiments. The irreflexive convention is an explicit scope assumption.
