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

The verified input is the type-\(A_n\) Cartan lattice \(C_n\mathbb Z^n\) intersected with the nonnegative orthant, over \(\mathbb C\), with \(n\ge2\). The proof is self-contained after standard finite-quotient smoothness and toric discrepancy criteria.

The attached standalone Python file `verify_lipman.py` uses exact rational and integer arithmetic, no third-party packages, and no external network access. Executing `python3 verify_lipman.py` returned `VERIFY_OK 45520`. It checks the proposed inverse Cartan matrix for ranks two through fourteen; deterministic exponent samples against lattice integrality; and for orders \(3\le N\le140\), every nonidentity cyclic element's fixed-axis count, age, absence of pseudoreflections, prime-stratum maximality, canonical-index congruence, terminal threshold, and torus-fixed interior minimum. It also verifies all generic prime transverse character multiplicities.

Finite replay is not a proof of all ranks. The infinite arguments are determinant/index equality, finite-subgroup fixed spaces, the character count by residue classes, the toric class-group sequence, and Ambro's minimum over strictly interior lattice points. No singular-scheme multiplicities, positive-characteristic extension, or independent audit is claimed.
