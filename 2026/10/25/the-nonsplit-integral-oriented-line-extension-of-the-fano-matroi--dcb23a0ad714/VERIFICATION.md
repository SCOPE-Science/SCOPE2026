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
# Verification record

Running `python3 verify_fano.py` from a directory containing that embedded file regenerates all seven Fano lines from XOR, all \(28\) independent bases, and all \(168\) invertible binary maps. Integer signed-face traces are compared with the claimed complete character table, and the seven maps from tetrahedron boundaries to missing line coefficients are checked to be primitive.

For the line \([1,2,3]\) its stabilizer is reconstructed with \(24\) elements. All \(35\) triples are classified into five orbits and each candidate \(\eta\)-eigensum is tested against every stabilizer element. The only allowed orbit sums have sizes \(1,12,4\), with boundary multipliers \(1,4,0\). Their cycle condition forces the line coefficient to be a multiple of four; the explicit \(u_{12}-4u_1\) cycle realizes this bound and has no other line coefficients.

The mathematical proof in `RESULT.md` supplies the logical connection between these checked finite identities and the integral equivariant exact sequence. A successful log is a reproducibility artifact, not an independent certification. No separate external scientific audit is asserted.
