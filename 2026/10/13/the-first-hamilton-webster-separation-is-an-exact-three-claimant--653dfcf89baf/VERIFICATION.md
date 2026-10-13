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
The theorem is proved algebraically in `RESULT.md`.

For three strictly ordered claims \(0<p<q<r\) and two seats, Webster's second seat compares priorities
\[
q\quad\text{and}\quad \frac r3,
\]
so its threshold is \(r=3q\).

Hamilton's second seat, once the largest claimant has lower quota one, compares remainders
\[
\frac{2q}{S}\quad\text{and}\quad\frac{2r}{S}-1,
\]
where \(S=p+q+r\), so its threshold is \(r=p+3q\).

The embedded `verify_hamilton_webster_two_seat.py` independently implements both tie-aware correspondences with exact `Fraction` arithmetic. It verifies the cone on \(222680\) ordered integer triples, checks both boundary correspondences, replays two-claimant equality over a broad finite grid, and searches primitive positive integer triples for the minimum witness.

Run:

`python3 verify_hamilton_webster_two_seat.py`

The first output line must be:

`VERIFY_OK`

The finite replay is not used as an infinite proof. Its role is to check the symbolic derivation, tie handling, and the bounded search establishing the stated primitive minimum.
