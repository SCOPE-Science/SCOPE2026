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
# Mathematical verification

Execute `python3 verify_semi_narayana.py`. It uses the Python standard library and checks integer matrices, exact determinant values, all seven primitive parity triples, all fourteen three-word binary lifting bases, explicit primitive orbits modulo \(2,4,8,16,32\), and the underlying binary-partition generating function and recurrence through index \(8191\).

The verifier's expected terminal line is `VERIFY_OK`. These computations certify the finitely many nonstandard identities used in the written lifting proof. Complete orbit coverage at all moduli follows by induction from the base orbit and the fourteen lifting bases, not from the finite orbit census. Natural densities additionally require the irreducible, aperiodic, doubly stochastic finite-chain argument and the arbitrary-cutoff binary cylinder estimate.

No independent mathematical audit has been performed. The literature comparisons do not establish exhaustive priority.
