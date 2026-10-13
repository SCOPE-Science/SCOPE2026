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

The proof uses the fixed choice
\[
\alpha=\frac7{20}.
\]
The two strict numerical conditions are exact:
\[
\frac13<\frac7{20}
\]
and
\[
3^{7/20}<\frac32
\quad\Longleftrightarrow\quad
2^{20}<3^{13}.
\]

The many-zero class is controlled by the binomial tail for zero probability \(1/3\). Because \(7/20>1/3\), its exponential rate is strictly below \(3^n\).

For the remaining strings, the recurrence comparison and asymptotic inspected in the primary source give
\[
2^{m-n}n\asymp3^n.
\]
After fixing the recurrence index and a prefix of length \((1-\alpha)n+O(1)\), any two coordinatewise comparable suffixes would produce a difference simultaneously smaller than \(3^{\alpha n+O(1)}\) and larger than a constant multiple of \((3/2)^n\), which is impossible because \(3^\alpha<3/2\).

The packaged checker confirms the exact alpha inequalities, evaluates finite binomial tails, and exhaustively enumerates ternary Keith numbers through ten ternary digits. Those computations are corroborative only and are not used to justify the infinite bound.
