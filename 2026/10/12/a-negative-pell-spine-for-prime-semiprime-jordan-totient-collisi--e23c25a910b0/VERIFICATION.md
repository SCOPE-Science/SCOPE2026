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

The infinite proof is contained in `RESULT.md`. The finite checker is corroborative.

It constructs
\[
P_t+Q_t\sqrt3=(1+\sqrt3)(2+\sqrt3)^t
\]
by the exact recurrences
\[
P_{t+1}=2P_t+3Q_t,
\qquad
Q_{t+1}=P_t+2Q_t,
\]
and verifies
\[
P_t^2-3Q_t^2=-2.
\]

For every tested index at which both coordinates are prime, it independently evaluates the Jordan totient from integer factorization and checks
\[
J_2(P_t)=J_2(2Q_t).
\]

For the first one hundred indices it also checks
\[
t\equiv1\pmod3,
\quad t>1
\Longrightarrow
5\mid P_t,
\quad3\mid Q_t.
\]

Finally, it enumerates every pair of primes
\[
p,q\le5000
\]
and verifies that a collision
\[
J_2(p)=J_2(2q)
\]
occurs exactly when \((p,q)\) is one of the Pell-coordinate pairs in that window.

No bounded computation is used to infer that all positive solutions of the negative Pell equation lie on the displayed orbit; that statement is proved by descent in `RESULT.md`.
