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

The program evaluates the ternary \(2\)-shifted digit product using repeated integer division by \(3\). It then checks every start
\[
1\le n<4096
\]
until the orbit repeats, reconstructs the repeated cycle, and records precisely which starting values are periodic.

The expected complete set is
\[
\{36,64,72,144,288,1152\}.
\]
The program also checks the exact ternary strings and transitions for those points and for
\[
4096\to10368\to4608\to4096.
\]

The finite exhaustion is the proof of the two least-value assertions; it is not being extrapolated to any infinite classification. A successful replay prints `VERIFY_OK`.
