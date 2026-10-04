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
The embedded `verify_jefferson_quota_boundary.py` is an exact-rational replay of the finite checks supporting the analytic theorem.

It implements Jefferson/D'Hondt by direct highest-averages selection. For every strict allocation it independently verifies the equivalent divisor interval: there is a divisor \(d\) such that every allocation equals the floor of population divided by \(d\).

The replay checks:
- two-entity positive integer profiles through total population \(30\) and house sizes through \(10\), finding no upper-quota violation;
- three-entity, two-seat profiles through total population \(30\), again finding no violation;
- all three-entity, three-seat profiles through total \(30\), requiring exact agreement between actual violations and the chamber \(3/5<p_A\le2/3\) with both rivals below \(p_A/3\);
- all four-entity, two-seat profiles through total \(30\), requiring exact agreement with the chamber \(2/5<p_A\le1/2\) with all rivals below \(p_A/2\);
- unique least-total sorted integer witnesses \((4,1,1)\) and \((3,1,1,1)\);
- exact simplex probabilities \(1/45\) and \(1/40\) using `Fraction` arithmetic.

Run:

`python3 verify_jefferson_quota_boundary.py`

The first output line must be:

`VERIFY_OK`

The finite sweeps are consistency checks. The continuum minimality and chamber statements are proved analytically in `RESULT.md`; no infinite claim is inferred from bounded enumeration.
