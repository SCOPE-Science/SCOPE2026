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

The proof was reconstructed from the definition of the prime-power map. Its critical implications are:

1. For each fixed \(y\ge1\), the chosen CRT residue \(a_y\) is reduced modulo \(M_y\).
2. For every prime \(q\equiv a_y\pmod{M_y}\), each \(q+j\) with \(1\le j\le y\) has two distinct prescribed prime divisors and hence cannot be a prime power.
3. Since \(q\) is itself a prime power, it is the largest prime power not exceeding \(q+y\), giving \(P(q+y)=y\).
4. The prime number theorem in arithmetic progressions converts the constructed prime class into the displayed \(X/\log X\) lower bound.

`verify.py` performs finite regression checks for the first three targets by constructing the CRT class and locating an actual prime witness. These checks do not replace the infinite proof or the prime number theorem in arithmetic progressions.

Limits: no claim is made that the constructed subfamily exhausts any fiber, and no optimality is asserted for the auxiliary modulus or the lower-bound constant.
