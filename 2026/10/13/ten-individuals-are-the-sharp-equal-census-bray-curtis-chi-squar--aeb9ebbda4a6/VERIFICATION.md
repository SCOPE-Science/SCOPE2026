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
For equal row total \(N\),
\[
B(x,y)=\frac{1}{2N}\sum_i|x_i-y_i|,
\]
and, using column masses from the same two-row table,
\[
X(x,y)^2=\frac2N\sum_i\frac{(x_i-y_i)^2}{x_i+y_i}.
\]

The embedded `verify_bray_chi_square_boundary.py` generates every positive composition for every \(3\le N\le10\) and every admissible richness. It verifies the composition and pair counts combinatorially and compares every unordered two-community table with exact rational arithmetic.

It verifies no strict reversal for \(N\le9\). At \(N=10\), reversals occur exactly for richness \(3,4,5,6\), with labeled counts \(288,8256,30100,17100\).

It separately checks the stated witness and the exact values \(1/5\), \(3/10\), \(2/5\), and \(4/11\).

Run:

`python3 verify_bray_chi_square_boundary.py`

The first output line must be:

`VERIFY_OK`
