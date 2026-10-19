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

The standalone `checker.py` enumerates the exact Jacobi sums over \(\mathbb F_{p^2}\) for twenty primes from \(5\) to \(79\). It independently chooses a nonsquare quadratic model, constructs a primitive element and discrete-log table, and reduces \(\zeta_{24}\)-powers in the integral basis using \(\Phi_{24}(X)=X^8-X^4+1\). For all eight exact-order-24 character extensions it checks that the Jacobi sum is \(\pm p\) exactly in residue classes \(\{13,17,19,23\}\). It also verifies the eight-class digit-sum criterion directly.

Running `python3 checker.py` from an extracted package produced `CHECK_PASS: exact Jacobi sums and digit-sum congruence for every listed field`. No third-party dependency or network service is needed.

The exhaustive computations are only for the finite list printed by the program. The uniform theorem rests on Stickelberger valuations, algebraic integrality, Kronecker's theorem, and the fixed-field argument in `RESULT.md`.
