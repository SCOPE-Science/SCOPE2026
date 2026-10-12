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

`verify.py` reproduces the seven finite inequalities used in the proof with a standard-library sieve through \(30000000\) and integer interval arithmetic only.

For \(m=p-2\), it encloses
\[
\log\left(1+\frac1m\right)
\]
with a twelve-term alternating series plus the next-term remainder. Threshold logarithms are enclosed by the positive atanh series with a geometric tail bound. Every rational term is outward-rounded after scaling by \(10^{24}\), so strict interval separation is an exact integer certificate.

The replay checks the unrestricted \(1\pmod3\) product below \(5\); the even \(3\mid n\) product below \(7\); the unrestricted \(2\pmod3\) product below \(5\); both modulo-\(5\)-thinned \(2\pmod3\) products below \(3\); the odd \(3\mid n\), modulo-\(5\)-thinned product below \(5\); and the next-term crossing above \(5\).

A valid run ends with:
`VERIFY_OK lower_bound=617427 crossing_prime=26375269`

The computation does not enumerate Deaconescu numbers and does not prove existence.
