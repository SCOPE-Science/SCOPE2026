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

Run `python3 rb_squarezero_checker.py` with the Python standard library. The script enumerates all linear operators (not just presumed normal forms), verifies the weight-zero Rota–Baxter identity on each pair of basis vectors, tests the predicted necessary-and-sufficient normal form independently, and enumerates the actual action of all invertible linear changes of radical basis.

The script passed for \((q,n)=(2,1),(3,1),(2,2),(3,2),(2,3)\): respective operator totals \(2,3,16,33,176\); the last three orbit-size profiles are \((1,3,3,3,6)\), \((1,8,8,16)\), and \((1,7,21,21,42,84)\). Only the binary cases verify instances of the new characteristic-two theorem; the ternary controls verify how the constraint \(T(u)=0\) reappears for odd characteristic.

For arbitrary even prime powers, the proof must be read: a finite enumeration does not certify infinitely many fields and dimensions. The derivations of the count and orbit sizes invoke standard Gaussian counting and the explicitly displayed centralizer blocks; the nilpotency index uses the exact identity \(P^2(a+v)=aT(u)\). No external validation or independent mathematical audit has been performed.
