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

The exact checker is `artifacts/verify_target.py` and uses only Python's standard library.

It verifies:

1. the polynomial identity
\[
9\mu^{3}(\mu^{2}+\mu+1)-(\mu+2)^{3}
=
(\mu-1)(3\mu^{2}+2\mu+4)(3\mu^{2}+4\mu+2);
\]

2. the exact reduction of
\[
27\mu^{3}(\mu^{3}+8)^{3}
\]
against
\[
(\mu^{3}-1)^{3}
\]
modulo each quadratic factor, giving \(j=-32768\) and \(j=8000\);

3. the negative discriminants \(-44\) and \(-8\), and nonvanishing denominator remainders, which ensure that the four quadratic roots are distinct allowed nonsingular parameters.

A successful replay ends with:

`VERIFY_OK fixed_parameters=4 j_values=8000,-32768`

The checker does not re-prove Otsubo's general isogeny theorem and does not derive the CM classification of the two \(j\)-values from first principles. Those two inputs remain explicitly cited literature premises.
