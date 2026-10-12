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

For
\[
p_r(k)=\frac{1-r}{1+r}r^{|k|},
\]
the proof uses four exact identities:
\[
\mathbb E|X_r|=\frac{2r}{1-r^2},
\]
\[
d_{\mathrm{LP}}(\mu_r,\mu_s)=\frac{2(s-r)}{(1+r)(1+s)},
\]
\[
W_1(\mu_r,\mu_s)=2\left(\frac{s}{1-s^2}-\frac{r}{1-r^2}\right),
\]
and
\[
\frac{W_1}{d_{\mathrm{LP}}}=\frac{1+rs}{(1-r)(1-s)}.
\]
The first identity is a geometric-series calculation. The second follows from the single-crossing property and the Ky–Fan coupling representation on the integer lattice. The third follows by summing absolute CDF differences in one dimension. The last is algebra.

The standalone script `verify.py` independently checks these formulas against direct truncated probability sums on a deterministic grid for several moment budgets. It also checks that the observed ratios stay below the claimed sharp constant and approach it as the two parameters coalesce at the moment boundary.

Successful output ends with:
`VERIFY_OK B1_constant=3.414213562373095 max_formula_error<1e-12`.

The finite checks are regression tests only; they are not used to prove the uniform theorem or sharpness.
