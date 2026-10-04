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
The embedded `verify_webster43_quota_boundary.py` replays the finite checks using only the Python standard library and exact integer or `Fraction` arithmetic.

It implements Webster in highest-averages form with priorities \(p_i/(2a_i+1)\). For every strict allocation it independently verifies that a nonempty Webster divisor interval exists for nearest-integer rounding.

The replay checks every positive integer profile through total population \(40\) in all coordinatewise predecessor cells of \((4,3)\), finding no quota violation. In the boundary cell it requires exact equivalence between an actual quota violation and the analytic chamber
\[
3p_A\le2P,
\qquad 5p_j<p_A\quad(j\ne A).
\]
It confirms that every such violation gives all three seats to the violating entity, verifies the unique least-total sorted witness \((6,1,1,1)\), and computes the fixed-label and total simplex probabilities as exact fractions \(1/5400\) and \(1/1350\).

Run:

`python3 verify_webster43_quota_boundary.py`

The first output line must be:

`VERIFY_OK`

The integer sweeps are consistency checks only. The continuum chamber and minimality statements are justified by the analytic proof in `RESULT.md`.
