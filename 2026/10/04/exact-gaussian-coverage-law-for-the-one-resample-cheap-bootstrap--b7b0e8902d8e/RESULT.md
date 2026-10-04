# Exact Gaussian coverage law for the one-resample Cheap Bootstrap
## Finding
For iid Gaussian data \(X_1,\ldots,X_n\sim N(\mu,\sigma^2)\), \(n\ge2\), the one-resample two-sided Cheap Bootstrap interval of Lam has an exact finite-sample coverage law governed only by the collision count of the bootstrap occupancy vector. Write
\[
I_n=\left[\bar X-a_\alpha|\bar X^*-\bar X|,\;\bar X+a_\alpha|\bar X^*-\bar X|\right],
\qquad
a_\alpha=t_{1,1-\alpha/2}=\cot(\pi\alpha/2),
\]
for \(0<\alpha<1\). If \((N_1,\ldots,N_n)\sim\operatorname{Multinomial}(n;1/n,\ldots,1/n)\) are the bootstrap counts and
\[
C_n=\sum_{i=1}^n\binom{N_i}{2},
\]
then
\[
\Pr_\mu(\mu\in I_n)
=\mathbb E\!\left[\frac{2}{\pi}\arctan\!\left(a_\alpha\sqrt{\frac{2C_n}{n}}\right)\right].
\]
The distribution of \(C_n\) is explicitly
\[
\Pr(C_n=c)=\frac{n!}{n^n}[z^n u^c]
\left(\sum_{k=0}^n\frac{z^k u^{\binom{k}{2}}}{k!}\right)^n.
\]
The coverage is strictly below \(1-\alpha\) for every finite \(n\ge2\), although it converges to \(1-\alpha\). More precisely,
\[
\Pr_\mu(\mu\in I_n)
=1-\alpha-
\frac{a_\alpha(3+5a_\alpha^2)}{2\pi(1+a_\alpha^2)^2}\frac{1}{n}
+O(n^{-3/2}).
\]
At nominal \(95\%\) coverage the exact values are \(0.475\) at \(n=2\), \(0.9429201071484832\) at \(n=10\), and \(0.9468018332436843\) at \(n=20\); the asymptotic deficit coefficient is \(0.0620900323007214\).

## Assumptions and scope
The result concerns the original Cheap Bootstrap interval with exactly one ordinary nonparametric bootstrap resample of the same size as the observed sample. The data are iid univariate Gaussian with unknown \(\mu\in\mathbb R\) and \(\sigma>0\). Probability is unconditional over both the observed data and the bootstrap resampling. The statement does not claim the same exact law for non-Gaussian data, for more than one resample, for studentized Cheap Bootstrap, or for other bootstrap confidence intervals.

## Proof
Condition on the multinomial count vector \(N=(N_1,\ldots,N_n)\), which is independent of the Gaussian observations. Put \(A_i=N_i-1\). Since \(\sum_i A_i=0\),
\[
\bar X^*-\bar X=\frac1n\sum_{i=1}^n A_i(X_i-\mu).
\]
The coefficient vector \((A_1,\ldots,A_n)\) is orthogonal to the all-ones vector. Gaussian orthogonality therefore makes \(\bar X-\mu\) independent of \(\bar X^*-\bar X\) conditional on \(N\), with
\[
\bar X-\mu\sim N\!\left(0,\frac{\sigma^2}{n}\right),
\qquad
\bar X^*-\bar X\mid N\sim N\!\left(0,\frac{\sigma^2}{n}Q_n\right),
\]
where
\[
Q_n=\frac1n\sum_i(N_i-1)^2.
\]
Because \(\sum_i N_i=n\),
\[
\sum_i(N_i-1)^2=\sum_i N_i^2-n=2\sum_i\binom{N_i}{2}=2C_n,
\]
so \(Q_n=2C_n/n\). The ratio of the two independent standardized normal variables is Cauchy. Since the \(t\)-distribution with one degree of freedom is Cauchy and \(a_\alpha=\cot(\pi\alpha/2)\),
\[
\Pr(\mu\in I_n\mid N)
=\Pr\!\left(|Z_0/Z_1|\le a_\alpha\sqrt{Q_n}\right)
=\frac{2}{\pi}\arctan(a_\alpha\sqrt{Q_n}).
\]
Averaging over \(N\) proves the exact coverage formula. The coefficient-extraction formula follows because an occupancy vector \((k_1,\ldots,k_n)\) has probability \(n!/(n^n\prod_i k_i!)\), and its collision count is \(\sum_i\binom{k_i}{2}\).

For strict undercoverage, define
\[
g(q)=\frac{2}{\pi}\arctan(a_\alpha\sqrt q),\qquad q\ge0.
\]
This function is increasing and strictly concave on \((0,\infty)\). Also
\[
\mathbb E C_n=\binom n2\frac1n=\frac{n-1}{2},
\qquad
\mathbb E Q_n=1-\frac1n.
\]
Hence Jensen's inequality gives
\[
\Pr(\mu\in I_n)=\mathbb E g(Q_n)\le g(1-1/n)<g(1)=1-\alpha.
\]

For the first-order expansion, represent \(C_n\) as the sum of indicators that two bootstrap draws choose the same original observation. Distinct pair indicators are pairwise independent. A direct equality-graph expansion gives
\[
\operatorname{Var}(C_n)=\frac{(n-1)^2}{2n},
\]
\[
\mathbb E(C_n-\mathbb EC_n)^3
=\frac{3(n-2)(n-1)^2}{2n^2},
\]
and
\[
\mathbb E(C_n-\mathbb EC_n)^4
=\frac{(n-1)^2(3n^3+32n^2-165n+180)}{4n^3}.
\]
For completeness, the fourth-moment identity follows by expanding centered edge indicators. The only nonzero edge-multiset types are one edge repeated four times, two edges each repeated twice, a triangle with one edge repeated, and a four-cycle; tree edge sets contribute zero because their equality indicators are jointly independent. Consequently \(\mathbb E|Q_n-1|^3=O(n^{-3/2})\), while the fourth moment makes the event \(Q_n<1/2\) contribute only \(O(n^{-2})\). Taylor expansion of \(g\) about \(1\) is therefore integrable through second order, with
\[
\mathbb E(Q_n-1)=-\frac1n,
\qquad
\mathbb E(Q_n-1)^2=\frac2n+O(n^{-2}),
\]
\[
g'(1)=\frac{a_\alpha}{\pi(1+a_\alpha^2)},
\qquad
g''(1)=-\frac{a_\alpha}{2\pi(1+a_\alpha^2)}-
\frac{a_\alpha^3}{\pi(1+a_\alpha^2)^2}.
\]
Thus
\[
\mathbb E g(Q_n)
=g(1)+\frac{-g'(1)+g''(1)}{n}+O(n^{-3/2}),
\]
and simplifying \(-g'(1)+g''(1)\) yields the stated coefficient.

## Verification
The accompanying `verify.py` implements the exact occupancy recurrence
\[
A_{m+1}(b,c)=\sum_{k=0}^b\binom bk A_m\!\left(b-k,c-\binom k2\right),
\]
where \(A_m(b,c)\) counts assignments of \(b\) labeled bootstrap draws to \(m\) labeled source observations with collision count \(c\). It exhaustively matches direct labeled resampling for \(n\le4\), checks that the occupancy counts sum to \(n^n\), verifies the displayed second through fourth central-moment identities for every \(2\le n\le30\), and recomputes the quoted \(95\%\) coverage values. Running the packaged script prints `VERIFY_OK`.

The computation is a reproducibility check for exact finite cases and formulas; it is not used as a substitute for the all-\(n\) proof above.

## Relationship to prior work
Lam introduced the Cheap Bootstrap interval and explicitly permits a single resample, proving asymptotically exact coverage for every fixed positive resample count. The same paper proves a two-sided \(O(n^{-1})\) coverage expansion for function-of-mean models but states that its general coefficient is a multidimensional integral not available in closed form. The Gaussian-mean calculation here specializes the one-resample method far enough to obtain an exact finite-sample occupancy mixture, a sign for the finite-sample error at every \(n\), and a closed-form coefficient.

Lam and Liu subsequently derived general finite-sample coverage-error bounds, including linear functions and Gaussian/sub-Gaussian settings. Those results bound the error through normal-approximation quantities rather than identify the exact Gaussian one-resample coverage distribution. Their linear-model theorem therefore does not imply the occupancy mixture, strict finite-\(n\) undercoverage, or the displayed coefficient.

The later Studentized Cheap Bootstrap modifies the procedure by adding an outer calibration layer to improve higher-order accuracy. It is a different interval and does not subsume the exact coverage law for the original one-resample interval stated here.

## Limitations
The exact law uses Gaussian orthogonality in an essential way. For non-Gaussian observations, the sample mean and centered bootstrap displacement are generally not independent conditional on the occupancy vector. The claim treats only one resample; with several resamples the bootstrap displacements are jointly conditionally Gaussian but share the same observed residual vector, so a different finite-sample analysis is required. The originality comparison cannot exclude an equivalent identity hidden in older bootstrap literature under different notation, although targeted searches of the focal and follow-up Cheap Bootstrap papers and exact-formula aliases did not locate one.

## References
1. H. Lam, “A Cheap Bootstrap Method for Fast Inference,” arXiv:2202.00090, first submitted January 31, 2022. Equations (1)–(3) define the interval; Theorems 1–2 give asymptotic exactness and higher-order coverage.
2. H. Lam and Z. Liu, “Bootstrap in High Dimension with Low Computation,” arXiv:2210.10974, first submitted October 20, 2022; Proceedings of Machine Learning Research 202 (2023), 18419–18453. Section 3 gives finite-sample coverage bounds and linear-function specializations.
3. S. He and H. Lam, “Higher-Order Coverage Errors of Batching Methods via Edgeworth Expansions on t-Statistics,” arXiv:2111.06859, first submitted November 12, 2021; Annals of Statistics 52 (2024), 1360–1383. This supplies nearby higher-order t-limit methodology rather than the exact one-resample bootstrap law.
4. S. He, H. Lam, and Y. Yan, “Studentized Cheap Bootstrap: Achieving Higher-Order Coverage Accuracy with Low Computation,” arXiv:2606.25968, first submitted June 24, 2026. This studies a calibrated extension rather than the original interval analyzed here.
