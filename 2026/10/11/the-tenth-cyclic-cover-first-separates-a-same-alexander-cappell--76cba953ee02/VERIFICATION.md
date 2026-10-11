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

The exact matrices are copied from the \(\ell=0\) specialization of the cited primary theorem. The complement-group formula is also stated in that source.

For each \(1\le d\le10\), `verify.py` computes \(M^d-I\), enumerates all minors of orders \(1,2,3,4\), takes their exact integer gcds, and reconstructs the Smith invariant factors from successive determinantal divisors. It then compares both matrices degree by degree, requires the first unequal Smith tuple to occur at \(d=10\), and checks that the two degree \(10\) torsion orders are nevertheless equal.

Replay command:

`python3 verify.py`

Observed output:

`VERIFY_OK first_difference=10 d1_9_match=true d10_A=(1,1,1,1309791722987654687) d10_B=(1,1,11,119071974817059517) equal_torsion_order=true`

The verification establishes only the stated range through degree \(10\). It does not infer behavior for higher cyclic covers or other members of the source family.
