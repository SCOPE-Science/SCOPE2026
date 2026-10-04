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
Run `python3 verify.py`.

The checker independently forms complementary divisor-pair sums and solves their subset-sum condition. It verifies the exact \(p^2q\) candidate list, checks the representations of \(6\), \(28\), and \(36\), and enumerates every integer through \(10000\) as a regression test.

The finite enumeration confirms that the only tested strongly pseudoperfect integers with \(\Omega(n)\le3\) are \(6\) and \(28\), and that \(36\) is a non-perfect witness at \(\Omega(n)=4\).

The all-integer theorem does not rely on this finite enumeration. Exhaustiveness follows from the symbolic factorization-shape proof in `RESULT.md`.

A successful replay prints `VERIFY_OK`.
