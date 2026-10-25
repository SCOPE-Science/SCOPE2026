# Scientific assessment

## Correctness

**PASS.** A symmetric one-ball-per-color Pólya urn induces the uniform weak-composition distribution, because the probability of a count vector is independent of its component arrangement. Stars-and-bars counting supplies the two exact singleton probabilities, and subtraction factors into the displayed cubic. Three disjoint real sign changes of a monic cubic yield exactly three simple real roots, two positive. The elementary value at sample size two distinguishes small and large numbers of colors. Expanding around the occupancy-density-one point and using the nonzero derivative at the roots supplies the stated \(\pm\sqrt q-3/4\) locations and the \(q^{-2}\) critical-window limit. A standalone exact-arithmetic program independently enumerated 373,343 weak compositions covering 116 parameter instances. Scope: one initial ball per color, unit reinforcement, two distinct specified colors, sample size at least two.

## Originality

**PASS, with priority uncertainty.** The full text of Keener and Wu's *On Dirichlet Multinomial Distributions* covers the general occupancy law and central-limit/first-order joint-distribution approximation, but its \(O(q^{-2})\) joint approximation error does not resolve the sign of the critical covariance, which is itself of order \(q^{-2}\). The full arXiv text of Eaton, Godbole and Sinclair concerns independent occupancy and Poisson approximations rather than the reinforced critical window. Chen's 1981 *Limit theorems for general size distributions* has relevant urn-model limit theory; only its publisher abstract was accessible, so an older equivalent finite-sample sign classification remains a priority risk. Searches for equivalent formulations (Bose–Einstein cells, random weak compositions, Dirichlet–multinomial indicator covariances), parameter reductions, and more general coverage identified no stated two-reversal cubic with the critical shift or profile. The known exact Dirichlet–multinomial mass function is acknowledged as foundational rather than treated as new.

## Mathematical value

**PASS.** The contrast between positive reinforcement and independent allocation motivates the question: the color counts are constrained yet correlated through a common random directing probability. The two singleton *indicators*, unlike the underlying color *counts*, develop a positive covariance only in a narrow, analytically specified sample-size window. The exact roots show two sign reversals for every integer \(q\ge5\), and the critical scaling explains why an ordinary fixed-density asymptotic predicts negative dependence but misses a strictly positive island. The window width, displacement, and \(q^{-2}\) sign profile give a nontrivial finite-size refinement of established Dirichlet–multinomial asymptotics, not merely a known-table numerical value.

## Closest literature and limitations

- Keener and Wu (2006), DOI 10.1142/9789812772558_0008: full text, general Dirichlet–multinomial law, joint approximation and central limit theorem; not a direct critical-window sign theorem.
- Chen (1981), DOI 10.2307/3213174: abstract examined, original full text not accessed; residual historical comparison risk.
- Eaton, Godbole and Sinclair (2008), arXiv:0806.1007v1: full text, independent occupancy, different model and asymptotic regimes.

The exact theorem is limited to symmetric initial unit weights and unit reinforcement. No independent audit, historical-priority guarantee or extension to arbitrary concentrations is claimed.

Self-review: passed. Independent audit: not yet performed.
