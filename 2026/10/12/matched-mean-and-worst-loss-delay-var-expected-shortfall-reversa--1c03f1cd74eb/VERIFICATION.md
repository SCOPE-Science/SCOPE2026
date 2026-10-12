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
Let
\[
p=1-\alpha.
\]

For an equal-weight empirical distribution on \(n\) losses, every order statistic occupies probability mass
\[
\frac1n.
\]

If
\[
np<1,
\]
both VaR and Expected Shortfall equal the maximum loss.

If
\[
1\le np<2,
\]
then
\[
\mathrm{VaR}_\alpha=L_{n-1:n}
\]
and
\[
\mathrm{ES}_\alpha
=
\frac{(np-1)L_{n-1:n}+L_{n:n}}{np}.
\]
At fixed maximum \(L_{n:n}\), this is strictly increasing in VaR, so reversal is impossible.

The first remaining integer is
\[
n_*=
\left\lceil\frac{2}{p}\right\rceil.
\]
Writing
\[
r=n_*p,
\]
one has
\[
2\le r<3.
\]

For
\[
A=(0,\ldots,0,1,3,4)
\]
and
\[
B=(0,\ldots,0,2,2,4),
\]
the means and maxima agree, while
\[
\mathrm{VaR}_\alpha(A)=1<2=\mathrm{VaR}_\alpha(B)
\]
and
\[
\mathrm{ES}_\alpha(A)-\mathrm{ES}_\alpha(B)
=
\frac{3-r}{r}>0.
\]

The embedded `verify_var_es_same_mean_max_threshold.py` evaluates the empirical quantile integral exactly with Python `Fraction` arithmetic. It checks ten rational confidence levels and \(2875\) finite order comparisons.

At \(95\%\),
\[
n_*=40,
\qquad
(\mathrm{VaR},\mathrm{ES})(A)=\left(1,\frac72\right),
\qquad
(\mathrm{VaR},\mathrm{ES})(B)=(2,3).
\]

At \(97.5\%\),
\[
n_*=80
\]
with the same risk values.

Run:

`python3 verify_var_es_same_mean_max_threshold.py`

The first output line must be:

`VERIFY_OK`

The general threshold is proved algebraically in `RESULT.md`; the script is a replay and boundary check.
