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
# Verification details

Run `python verify_three_block_commutator.py` using Python 3, without third-party packages. The verifier enumerates group elements as triples of block coordinates and implements multiplication, inversion, and actual group commutators without using the theoretical commutator shortcut in the group-enumeration routine. For each of seven groups over fields of orders \(2\), \(3\), and \(4\), it checks all target central matrices against the fiber formula at lengths one and two. Independent explicit matrix-products enumerate five additional parameter sets, including rank-deficient targets. The marker on successful completion is `VERIFY_OK_THREE_BLOCK_COMMUTATOR_FIBERS 7 5`.

Verified finite cases are exhaustive only in the printed dimensions and fields. The general proof uses a bijection with matrix products, image stratification, and full-rank conditioning; it is not inferred from test coverage. The claims make no assertion of independently performed review.
