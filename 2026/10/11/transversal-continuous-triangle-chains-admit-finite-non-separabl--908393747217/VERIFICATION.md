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
# Verification of the finite chain realization and strict bound

The exact finite product equations (5.20) in the cited primary source are solved by a pair \((c_m,s_m)\) satisfying
\[
c_m=v-\frac{(v-u)d}{v}\frac{(1-\kappa s_m/m)^m}{(1+Ds_m/m)^m},
\]
\[
d(\kappa+D)-\kappa c_m=\frac{dE_f}{v}(1-\kappa s_m/m)^m.
\]
The scalar zero is obtained by uniform convergence and strict opposite signs, not by an approximate numerical endpoint residual. The source's contact theorem ensures the non-separability and positivity of each resulting finite family. Uniform denominator control gives the limit of the exact finite sum as the continuous integral.

The enclosed script `verify_chain.py` uses only the Python standard library, exact rational objects and scaled integers. Run:

```text
python3 verify_chain.py
```

It verifies, using only outward-rounded operations and a proven exponential Taylor remainder, the root bracket
\[
\frac{1110182}{10^6}<s_*<\frac{1110185}{10^6}
\]
and derivative positivity, strict geometric signs, negativity of the recovery denominator, the upper rectangle sum with \(N=16384\), and the **integer comparison**
\[
S_\infty<0.940465236<\frac{10000}{10633}.
\]
The script concludes with `VERIFY_OK` only if every assertion holds. The integral bound applies to the entire root bracket; it is not merely quadrature at a guessed root.

The proof supplies finite examples for all sufficiently large \(m\) but gives no effective bound on the smallest such \(m\), nor any claim of a global optimum. Independent audit has not been performed.
