# Same-model review

## Correctness

PASS. The proof uses the exact decision characterization of SCoRE-MDR. For \(\gamma\le\alpha\), the paper already gives \(\psi_\gamma=\mathbf{1}\{Q\le\gamma\}\), which is immediately dominated by \(\psi_\alpha\). For \(\gamma>\alpha\), the paper requires both \(Q\le\gamma\) and exclusion of every candidate empirical-risk value from \((\alpha,\gamma]\). Substituting the admissible pair \(t=s(X_{n+1})\), \(\ell=1\) makes that candidate exactly \(Q\), forcing \(Q\le\alpha\). The weighted proof has the same structure with \(Q_w\). The strict-witness constructions respect \([0,1]\)-bounded calibration risks and finite score sets.

## Originality

PASS. Bai and Jin explicitly state one-sided dominance for \(\gamma<\alpha\) and asymptotic power optimality of \(\gamma=\alpha\), but do not state the all-\(\gamma\) pointwise finite-sample dominance or its reward-uniform corollary. The latter follows from a specific implication hidden in the \(\gamma>\alpha\) extra condition. The adjacent conformal-risk-control and selective-conformal-risk-control sources use different procedures and do not supply this tuning result. Targeted database searches returned no close SCoRE/\(\gamma\)-dominance record.

## Value

PASS. The result resolves a concrete tuning question left partly asymptotic in the motivating paper. It removes any finite-sample reason to search over \(\gamma\) for MDR power within this family: \(\gamma=\alpha\) dominates every alternative realization-by-realization, and therefore for every nonnegative reward objective. The weighted extension shows the same conclusion survives the paper's known covariate-shift construction. This is an exact methodological simplification rather than a numerical increment.

## Closest literature and limitations

The closest source is Bai and Jin, arXiv:2603.24704, especially Proposition 4.4, Remark 4.5, Theorem 4.6, and the weighted analogue in Appendix A/C. Angelopoulos et al., arXiv:2208.02814, supplies the broader conformal risk-control framework but not this risk-adjusted e-value tuning family. Xu, Guo, and Wei, arXiv:2512.12844, studies a different two-stage selective conformal risk-control construction. The theorem does not extend automatically to SDR/e-BH tuning or to changes in the score function.

Same-model review: passed. Independent audit: not yet performed.
