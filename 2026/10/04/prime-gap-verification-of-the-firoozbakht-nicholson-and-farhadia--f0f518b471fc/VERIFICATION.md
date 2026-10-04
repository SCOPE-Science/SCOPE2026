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
The replay script `verify.py` uses exact integer record data and 80-digit decimal logarithms.

For the four new intervals it checks
\[
g_i^*<F_F(n_i^*)<F_N(n_i^*)
\]
for \(i=81,82,83,84\). The smallest numerical margin is still large: at \(i=83\),
\[
1676<1924.231497579769\ldots.
\]

The script also checks the ordering of the relevant maximal-gap starts through
\[
p_{85}^*=101412319996363309069.
\]

The computation does not enumerate all primes in the covered range. Coverage of every intervening prime follows from the maximal-gap interval argument and monotonicity proved in `RESULT.md`.
