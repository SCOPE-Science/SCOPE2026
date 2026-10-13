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
For sorted three-household incomes
\[
a\ge b\ge c>0
\]
with fixed total
\[
S=a+b+c,
\]
the relative Gini coefficient is
\[
G=\frac{2(a-c)}{3S}.
\]

Theil's \(T\) can be written as
\[
T
=
\frac1S\ln\!\left(\prod_i x_i^{x_i}\right)
+
\ln\!\left(\frac3S\right).
\]
Thus exact fixed-total ordering requires only an integer range and an integer product.

The embedded `verify_gini_theil_minimal_reversal.py` independently generates every positive three-part integer partition by:
- recursive partition construction;
- direct positive-triple enumeration followed by canonical sorting.

It verifies:
- no strict reversal for common totals \(3\) through \(12\);
- exactly one strict reversal at total \(13\);
- the unique pair \((8,3,2)\) and \((6,6,1)\);
- Gini values \(4/13\) and \(10/39\);
- Theil order keys \(1811939328\) and \(2176782336\);
- exact family inequalities for \(6\le x\le500\) as a consistency check.

The infinite family is proved analytically in `RESULT.md` by strict monotonicity of the logarithmic ratio, with the \(x=6\) case checked by an exact integer inequality.

Run:

`python3 verify_gini_theil_minimal_reversal.py`

The first output line must be:

`VERIFY_OK`
