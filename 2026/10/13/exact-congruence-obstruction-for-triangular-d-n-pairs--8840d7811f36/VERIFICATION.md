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

Run `python3 verify.py`.

The verifier checks:
- bijectivity of \(j\mapsto T_j\pmod{2^k}\) for \(1\le k\le8\);
- the complete bad-parameter set modulo \(3^k\) for \(1\le k\le5\), verifying that it is exactly the lift of \(2,5\pmod9\);
- the identity \(T_{1+3u}=1+9T_u\) on a symmetric finite range;
- existence of a nonsingular finite-field seed for every residue parameter for primes \(5,7,11,13,17,19\).

These are finite consistency checks. They do not replace the universal proof in `RESULT.md`, whose infinite steps are Hensel lifting and the Chinese remainder theorem.
