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
# Verification of the circular-ladder representation

Run `python3 verify.py` with Python 3 and no external dependencies. The script reconstructs the vertex set, edges, independent-set faces, group permutations, and reduced signed traces; it does not assume the theorem's traces in either finite enumeration. It compares those against the formulas for the group generators and all products.

Observed result: `VERIFY_OK: direct_signed_traces=208, orbit_signed_traces=1188, mod2_homology_widths=9, transfer_periods=80`.

Exact checks: 208 direct signed simplicial traces for every element of the natural group at widths 3 through 10; 1,188 independently calculated fixed-orbit-quotient traces at widths 3 through 24; reduced simplicial homology ranks over the field of two elements at widths 3 through 11; the transfer matrix's trace at 80 consecutive positive lengths. These are exact finite computations, but they are not an infinite proof or a verification of the prior published homotopy argument in full. The general claim relies on the explicit proof and the cited nonequivariant degree-concentration theorem.

Scientific scope: all integers \(n\ge3\) and rational representations of the natural \(D_n	imes C_2\) graph action; no assertion about integral representation lattices or exceptional extra graph automorphisms.
