# Sharp mass-sensitive finite-atomic Gini–variance bound
## Finding
Let \(X\) be a nondegenerate real random variable supported on exactly \(N\ge2\) distinct atoms \(x_1<\cdots<x_N\), with masses \(p_i>0\) satisfying \(\sum_i p_i=1\). Let \(\sigma^2=\operatorname{Var}(X)\), let \(X'\) be an independent copy, define the Gini mean difference \(G=\mathbb E|X-X'|\), and write the second L-moment as \(\lambda_2=G/2\). Then
\[
\lambda_2^2\le \frac{\sigma^2}{3}\left(1-\sum_{i=1}^N p_i^3\right).
\]
This inequality is sharp for every fixed positive mass vector. If \(a_0=0\) and \(a_i=\sum_{j=1}^i p_j\), equality holds exactly when
\[
x_i=A+B\frac{a_{i-1}+a_i}{2},\qquad i=1,\ldots,N,
\]
for some \(A\in\mathbb R\) and \(B>0\).

Since \(\sum_i p_i^3\ge N^-2\), this gives the sharp atom-count envelope
\[
\frac{G}{\sigma}\le \frac{2}{\sqrt3}\sqrt{1-\frac1{N^2}},
\]
and equality here occurs exactly for the uniform distribution on an equally spaced \(N\)-point lattice.

## Assumptions and scope
The result is distributional, not asymptotic. It assumes finitely many distinct real atoms, all with positive mass, and finite positive variance. No sign restriction on the atoms is needed. The probability-sensitive inequality is stronger than the atom-count corollary and remains exact for every prescribed positive mass vector.

## Proof
Let \(U\sim\operatorname{Unif}(0,1)\), and let \(Q\) be the left-continuous quantile function of \(X\), so \(X\stackrel{d}=Q(U)\). Put \(I_i=(a_{i-1},a_i]\), where \(a_i=\sum_{j=1}^i p_j\), and let \(J=i\) when \(U\in I_i\). Then \(Q(U)=x_J\), while
\[
m_i:=\mathbb E[U\mid J=i]=\frac{a_{i-1}+a_i}{2}.
\]
The standard quantile representation of the second L-moment gives
\[
\lambda_2=\int_0^1 Q(u)(2u-1)\,du=2\operatorname{Cov}(Q(U),U).
\]
Because \(Q(U)=x_J\) is measurable with respect to \(J\) and \(\mathbb E[U-m_J\mid J]=0\),
\[
\operatorname{Cov}(Q(U),U)=\operatorname{Cov}(x_J,m_J).
\]
Cauchy--Schwarz therefore yields
\[
\lambda_2^2\le4\operatorname{Var}(X)\operatorname{Var}(m_J).
\]
Now apply total variance to the uniform variable. Conditional on \(J=i\), the variable \(U\) is uniform on an interval of length \(p_i\), so
\[
\operatorname{Var}(U\mid J=i)=\frac{p_i^2}{12}.
\]
Hence
\[
\frac1{12}=\operatorname{Var}(U)=\operatorname{Var}(m_J)+\frac1{12}\sum_{i=1}^N p_i^3,
\]
and thus
\[
\operatorname{Var}(m_J)=\frac1{12}\left(1-\sum_{i=1}^N p_i^3\right).
\]
Substitution proves the probability-sensitive inequality.

Equality in Cauchy--Schwarz holds exactly when \(x_i-\mathbb E X\) is a nonzero constant multiple of \(m_i-1/2\) for every \(i\). Since the \(m_i\) are strictly increasing with \(i\), the multiplier must be positive, giving precisely \(x_i=A+B m_i\) with \(B>0\). Conversely, this affine-midpoint geometry makes Cauchy--Schwarz an equality, so it attains the bound for every fixed mass vector.

Finally, convexity of \(t\mapsto t^3\) gives \(\sum_i p_i^3\ge N^-2\), with equality exactly when every \(p_i=1/N\). For equal masses, \(m_i=(2i-1)/(2N)\), so the affine-midpoint equality condition is exactly equal spacing of the atoms. This proves the atom-count envelope and its equality characterization.

## Verification
The proof uses only the quantile identity for \(\lambda_2\), conditional expectation, Cauchy--Schwarz, total variance, and strict convexity. As a numerical stress check, random finite atomic laws with between two and eight atoms were generated and the squared ratio of the two sides never exceeded one up to floating-point error; fixed-mass equality constructions using the quantile-bin midpoints attained equality to floating-point precision. These computations are checks only, not part of the proof.

## Relationship to prior work
Papadatos proves that, for a uniform law on an \(N\)-point population, the correlation of the sample minimum and maximum is maximized exactly by an equally spaced lattice, and explicitly raises the broader problem of optimizing order-statistic correlations after replacing uniform masses by a fixed probability vector. That theorem concerns a different functional and does not imply the Gini--variance inequality here.

La Haye and Zizler prove the classical distribution-free inequality \(\lambda_2\le\sigma/\sqrt3\). Their paper also discusses point-mass representations, but the inspected full text gives no mass-vector correction of the form above. Jones and Balakrishnan likewise recover \(\lambda_2\le\sigma/\sqrt3\) from a continuous-quantile argument and develop moment-based extensions; their inspected full text contains no discrete, atomic, or support-count refinement.

Cerone and Dragomir's 2006 paper is the closest older title on weighted empirical Gini mean differences. Its accessible abstract states that sharp empirical-distribution bounds are given. A later full-text paper by Miao, Ge and Peng summarizes the cited Cerone--Dragomir bounds as mean-absolute-deviation and support-range bounds, not a variance bound involving \(\sum_i p_i^3\). The original 2006 full text was not successfully recovered in this check, so it remains a specific residual literature risk rather than evidence of coverage.

## Limitations
The claim does not optimize other L-moments, higher-order Gini functionals, or order-statistic correlations. It does not assert that the same cubic-mass factor governs continuous-discrete mixtures or infinite countable support. The originality assessment remains exposed to the inaccessible full text of the 2006 empirical-Gini paper and to older inequality literature not indexed by the searches performed.

## References
1. N. Papadatos, "A discrete analogue of Terrell's characterization of rectangular distributions," arXiv:2205.14360v1, 28 May 2022.
2. R. La Haye and P. Zizler, "The Gini mean difference and variance," METRON 77 (2019), 43--52, DOI: 10.1007/s40300-019-00149-2.
3. M. C. Jones and N. Balakrishnan, "On absolute moment-based upper bounds for L-moments," Statistics & Probability Letters 216 (2025), 110249, DOI: 10.1016/j.spl.2024.110249.
4. Y. Miao, L. Ge and A. Peng, "Bounds for the weighted Gini mean difference of an empirical distribution," Journal of Mathematical Inequalities 7 (2013), 773--783, DOI: 10.7153/jmi-07-70.
5. P. Cerone and S. S. Dragomir, "Bounds for the Gini mean difference of an empirical distribution," Applied Mathematics Letters 19 (2006), 283--293, DOI: 10.1016/j.aml.2005.05.009.
