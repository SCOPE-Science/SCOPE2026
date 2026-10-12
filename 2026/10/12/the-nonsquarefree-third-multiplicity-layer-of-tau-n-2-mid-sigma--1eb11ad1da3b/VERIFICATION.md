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

The proof in `RESULT.md` is universal.

The attached `verify.py` performs two independent finite consistency checks.

For every prime
\[
p\le200000,
\]
it computes the exact prime-cube values of \(\tau\), \(\sigma\), and \(\varphi\), tests
\[
\tau(p^3)^2\mid\sigma(p^3)+\varphi(p^3),
\]
and compares the result with
\[
p\equiv5\pmod{16}.
\]

For every ordered pair of distinct primes
\[
p,q\le5000,
\]
it computes the exact values for \(p^2q\), tests the defining divisibility, and compares it with the union of the three residue families stated in the theorem.

The finite replay is corroborative only. The unrestricted result follows from the exact modulo-\(16\) and modulo-\(36\) proof.
