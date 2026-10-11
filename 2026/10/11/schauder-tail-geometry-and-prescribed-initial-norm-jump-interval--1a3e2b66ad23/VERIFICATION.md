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
# Verification of the mathematical statement

The main calculations are exact and analytic. First, Abel summation gives the operator-norm expansion of \(T(z)\) and the convex-combination expansion of \(I-T(t)\) over complementary projections. The weights in the latter expansion are nonnegative and sum to one. Second, the cutoffs \(t_n=(\lambda_n\lambda_{n+1})^{-1/2}\) satisfy \(\lambda_nt_n\to0\) and \(\lambda_{n+1}t_n\to\infty\), giving the displayed explicit convergence of \(T(t_n)\) to \(P_n\) in operator norm. Third, the change of basis in each \(\ell_\infty^2\) block gives the exact two-by-two positive matrix in the proof. Its row-sum norms yield \(\|T(t)\|=e^{-4t}\) and the exact defect formula. Fourth, odd and even spectral gaps give the respective limits \(c\) and \(1\), and norm continuity for \(t>0\) fills the interval.

A finite independent arithmetic sanity check on the exact block expression, using \(\alpha=0.65\), produced approximate odd-gap values \(1.610618305\) (index \(3\)), \(1.649990082\) (index \(5\)), and \(1.65\) (index \(7\)), and even-gap values \(1\) to nine displayed decimal places (indices \(4,6,8\)). This checks the implementation of the block formula, not the infinite-dimensional limit. Every infinite assertion has a separate proof in RESULT.md.

Limitations: no general law for non-superlacunary spectra is asserted; nor is the entire class of positive analytic semigroups classified. Independent review and certification were not performed.
