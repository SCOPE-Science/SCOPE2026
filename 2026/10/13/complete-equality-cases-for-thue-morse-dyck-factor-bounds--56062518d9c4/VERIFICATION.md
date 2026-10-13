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

Run `python3 verify.py` beside `certificate.json`.

The verifier encodes the published rank-\(7\) linear representation over exact rational arithmetic and reproduces the paper's displayed values through \(n=20\).

It checks all four recurrences of Lemma 5.1 for every recurrence parameter from \(3\) through \(5000\), and checks the DFA consequence
\[
q(2^a)=2
\]
for \(1\le a\le39\).

The complete induction base \(1\le n<29\) is then evaluated from the linear representation. The verifier obtains exactly
\[
1,2,3,6,12,24
\]
for upper equality,
\[
4,8,16
\]
for global lower equality, and
\[
3,5
\]
for equality in the stronger odd lower bound.

As a separate regression, the verifier directly enumerates Dyck factors in two long Thue–Morse prefixes and reproduces the same base values. It also checks the final three equality classifications for every \(n<200000\).

The finite replay confirms the arithmetic and base cases. The proof for all \(n\) is the symbolic recurrence argument in `RESULT.md`.
