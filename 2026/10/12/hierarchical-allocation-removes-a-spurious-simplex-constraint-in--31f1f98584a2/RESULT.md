# Hierarchical allocation removes a spurious simplex constraint in a respiratory-resource model
## Finding
The resource-allocation definition in Zhuang, Zhu, Lu, Cheng and Tan assigns the four non-hospitalized infected classes the fractions
\[
p_1=\sigma\alpha_1,\qquad p_2=\sigma(1-\alpha_1),\qquad p_3=(1-\sigma)\alpha_2,\qquad p_4=(1-\sigma)(1-\alpha_2).
\]
For fixed \(0\le\sigma\le1\), every \(\alpha_1,\alpha_2\in[0,1]\) gives a valid allocation because \(p_j\ge0\) and
\[
p_1+p_2+p_3+p_4=\sigma+(1-\sigma)=1.
\]
Hence \(\alpha_1\) and \(\alpha_2\) are conditional within-group splits. The later condition \(\alpha_1+\alpha_2\le1\) is not a resource-conservation condition for the printed allocation formula.

For the paper's instantaneous objective
\[
R_0(\alpha_1,\alpha_2)=\max\{R_0^1(\alpha_1),R_0^2(\alpha_2)\},
\]
assume the two displayed functions are finite and continuous on \([0,1]\), and put
\[
m_i=\min_{a\in[0,1]}R_0^i(a),\qquad M=\max\{m_1,m_2\}.
\]
Then
\[
\min_{(\alpha_1,\alpha_2)\in[0,1]^2}R_0(\alpha_1,\alpha_2)=M.
\]
In particular, any pair of individual minimizers attains the corrected optimum. The complete minimizing set is
\[
\{(a_1,a_2)\in[0,1]^2:R_0^1(a_1)\le M,\ R_0^2(a_2)\le M\}.
\]
The one-dimensional restriction \(\alpha_2=1-\alpha_1\) used in Eq. (20) has optimal value at least \(M\), with equality exactly when that boundary intersects the minimizing set above.

The practical-data section independently exposes the mismatch. It reports the within-unvaccinated moderate/severe split \(0.6242:0.3758\) and the within-vaccine-failure split \(0.8157:0.1843\). Thus its two conditional first coordinates satisfy \(0.6242+0.8157=1.4399>1\), contradicting the stated simplex while remaining perfectly admissible under the four-fraction definition.

## Assumptions and scope
The claim concerns the instantaneous allocation algebra printed in Section 4, conditional on a fixed between-group share \(\sigma\) and fixed state-dependent efficiencies \(g_1,\ldots,g_4\) at the instant of optimization. It assumes \(0\le\sigma\le1\), \(0\le\alpha_1,\alpha_2\le1\), and that the rational reproduction-number functions in Eq. (17) are finite and continuous on \([0,1]\). The endpoint cases \(\sigma=0\) or \(\sigma=1\) merely make one conditional split operationally irrelevant; the normalization identity still holds.

This finding does not solve the paper's full time-dependent control problem, does not optimize \(\sigma\) itself, and does not assert that every numerical allocation reported by the paper is otherwise optimal. It corrects the feasible set and the resulting separable instantaneous minimax problem induced by the paper's own four allocation fractions.

## Proof
First, the four fractions are nonnegative on the stated ranges. Their sum is
\[
\sigma\alpha_1+\sigma(1-\alpha_1)+(1-\sigma)\alpha_2+(1-\sigma)(1-\alpha_2)
=\sigma+(1-\sigma)=1.
\]
No term involving \(\alpha_1+\alpha_2\) remains. Therefore resource conservation imposes no coupling between the two conditional splits.

Second, continuity on the compact interval gives minimizers \(a_i^*\in\operatorname{{argmin}}R_0^i\). For every \((a_1,a_2)\in[0,1]^2\),
\[
\max\{R_0^1(a_1),R_0^2(a_2)\}\ge\max\{m_1,m_2\}=M.
\]
Choosing \((a_1^*,a_2^*)\) gives equality, proving the optimum. A point attains \(M\) exactly when both component values are at most \(M\), which proves the formula for the full minimizing set.

Third, the boundary \(\{(a,1-a):0\le a\le1\}\) is a subset of the square. Minimizing over a subset cannot lower the square optimum, and equality holds precisely when the subset contains a square minimizer.

Finally, the reported Wuhan conditional ratios give the exact decimal identity
\[
0.6242+0.8157=1.4399>1.
\]
Nevertheless, for any between-group share \(\sigma\), the four corresponding top-level shares are \(\sigma(0.6242)\), \(\sigma(0.3758)\), \((1-\sigma)(0.8157)\), and \((1-\sigma)(0.1843)\), whose sum is exactly one.

## Verification
The accompanying `verify.py` uses exact rational arithmetic to check the Wuhan-ratio arithmetic and the four-share normalization for the reported decimal splits at two nontrivial rational values of \(\sigma\), including \(0.5521\). The universal normalization and minimax statements are proved algebraically above and do not rely on finite sampling.

## Relationship to prior work
The motivating article first defines the four hierarchical shares above, then later declares \(\alpha_1+\alpha_2\le1\) to be the total-resource constraint and restricts the minimax problem to \(\alpha_2=1-\alpha_1\). Its Appendix B.2 analyzes the two component functions separately, and its practical section reports two independent within-group ratios whose first coordinates sum to more than one. These passages jointly support the interpretation that \(\alpha_1\) and \(\alpha_2\) are conditional splits under an outer group share \(\sigma\).

Related epidemic-allocation literature inspected uses genuine top-level budget shares, for example a single treatment fraction between two locations or a single vaccine-budget split between groups. Those formulations do not imply the extra simplex constraint for two already-normalized conditional splits, nor do they state the source-specific corrected minimax identity above.

## Limitations
The source uses inconsistent prose around \(\alpha_1\), \(\alpha_2\), and \(\sigma\). This result follows the literal four-fraction allocation formula, Eq. (16), Eq. (17), and the reported conditional ratios; an alternative intended model with different decision variables would require re-derivation. The correction is instantaneous and conditional on \(\sigma\); it does not establish an optimal dynamic policy over a control horizon. No independent audit has been performed.

## References
1. M. Zhuang, J. Zhu, X. Lu, D. Cheng, X. Tan, “Dynamic Allocation of Emergency Medical Resources in Respiratory Infectious Disease Models Considering Vaccine Failure,” *Mathematics* 14(3), 425 (2026), DOI: 10.3390/math14030425.
2. C. Forsberg White et al., “Model-informed optimal allocation of limited resources to mitigate infectious disease outbreaks in societies at war,” *Journal of the Royal Society Interface* (2024/2025), DOI: 10.1098/rsif.2024.0575.
3. “Optimal allocation of limited vaccine to minimize the effective reproduction number,” PubMed PMID: 34216636 (2021).
