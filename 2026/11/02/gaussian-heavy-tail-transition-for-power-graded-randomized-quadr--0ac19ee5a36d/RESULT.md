# Gaussian–heavy-tail transition for power-graded randomized quadrature

## Finding

Let \(0<\alpha<1/2\), \(p>0\), and \(q=p(1-\alpha)\). Estimate the improper integral \(I=\int_0^1 t^{-\alpha}\,dt=1/(1-\alpha)\) by taking **one independent uniform point per cell** of the power mesh \(t_{j,n}=(j/n)^p\), and weighting each value by its cell length. Denote this unbiased estimator by \(Q_n\). Set \(c=\alpha^2p^4/12\). The following three alternatives are exact:

1. If \(q<3/2\), then \(n^q(Q_n-I)\) converges in distribution to a non-Gaussian variable \(S\) with \(\mathbb P(S>x)\sim x^{-1/\alpha}\) as \(x\to\infty\), and \(n^{2q}\operatorname{Var}(Q_n)\to V\in(0,\infty)\).
2. If \(q=3/2\), then \(n^3\operatorname{Var}(Q_n)/\log n\to c\) and \(n^{3/2}(Q_n-I)/\sqrt{\log n}\Rightarrow N(0,c)\).
3. If \(q>3/2\), then \(n^3\operatorname{Var}(Q_n)\to c/(2q-3)\) and \(n^{3/2}(Q_n-I)\Rightarrow N(0,c/(2q-3))\).

Among **fixed power meshes**, the unique minimizer of the asymptotic \(n^3\)-scaled variance is \(p_*=2/(1-\alpha)\), with sharp value \(4\alpha^2/[3(1-\alpha)^4]\). As an exact finite-sample instance, \(\alpha=1/3\), \(p=3\) gives \(\operatorname{Var}(Q_n)=3/(4n^3)\) **for every positive integer** \(n\), and every cell contributes exactly the same variance. This result does not claim optimality among unrestricted partitions or other randomized quadrature algorithms.

## Assumptions and scope

The integrand is \(f(t)=t^{-\alpha}\) on \((0,1]\). For each integer \(n\ge1\), partition \([0,1]\) at \(t_{j,n}=(j/n)^p\). Independently sample \(X_{j,n}\sim\operatorname{Unif}(t_{j-1,n},t_{j,n})\), and put

\[
Q_n=\sum_{j=1}^n (t_{j,n}-t_{j-1,n})X_{j,n}^{-\alpha}.
\]

Every sample is strictly positive almost surely. The estimator is unbiased. All convergence-in-law statements concern fixed positive \(\alpha,p\) and \(n\to\infty\), not parameters changing with \(n\). For \(1/2\le\alpha<1\), the estimator remains unbiased but has infinite variance for every \(n,p\); thus finite-variance claims require \(\alpha<1/2\).

## Proof

**1. Independent exact triangular-array representation.** Take independent \(U_j\sim\operatorname{Unif}(0,1)\), define \(a_j=j^p-(j-1)^p\) and \(q=p(1-\alpha)\), and let

\[
Z_j=a_j\bigl((j-1)^p+a_jU_j\bigr)^{-\alpha}-\frac{j^q-(j-1)^q}{1-\alpha}.
\]

The \(Z_j\) are independent and centered. The distribution of the estimator's error equals

\[
Q_n-I\;\stackrel{\mathrm d}=\;n^{-q}\sum_{j=1}^n Z_j.
\]

Here the common coupling is useful for almost-sure convergence of the rescaled error; equality in distribution suffices for the original independently generated rules. Explicit integration on each cell yields the exact variance formula

\[
v_j:=\operatorname{Var}(Z_j)=\frac{a_j\bigl(j^{p(1-2\alpha)}-(j-1)^{p(1-2\alpha)}\bigr)}{1-2\alpha}-\left(\frac{j^q-(j-1)^q}{1-\alpha}\right)^2,
\quad \operatorname{Var}(Q_n)=n^{-2q}\sum_{j=1}^n v_j.
\]

In particular \(v_1=(1-2\alpha)^{-1}-(1-\alpha)^{-2}>0\).

**2. Local variance and uniform bounds.** On \([(j-1)^p,j^p]\), with \(j\to\infty\), the cell width satisfies \(a_j=pj^{p-1}(1+O(j^{-1}))\); its relative width is \(O(j^{-1})\). Taylor's theorem for the smooth function \(t\mapsto t^{-\alpha}\), on this cell away from zero, gives

\[
v_j=\frac{\alpha^2p^4}{12}j^{2q-4}\bigl(1+O(j^{-1})\bigr)=c\,j^{2q-4}\bigl(1+O(j^{-1})\bigr).
\]

Indeed the leading fluctuation is the local derivative times the uniform-point displacement, so its variance is the derivative squared times the fourth power of the cell width, divided by 12. The Taylor remainder contributes one smaller relative power of \(j\). The mean-value theorem, independently of this asymptotic expansion, also gives \(|Z_j|\le C_{\alpha,p}j^{q-2}\) for every \(j\ge2\) after increasing the constant. The first variable is unbounded but has finite second moment because \(\alpha<1/2\).

**3. Subcritical law and right tail.** When \(q<3/2\), the series \(\sum_{j\ge1}v_j\) converges and is positive. Independence and Kolmogorov's convergence theorem give \(S:=\sum_{j\ge1}Z_j\) almost surely and in \(L^2\). The first term is \(Z_1=U_1^{-\alpha}-1/(1-\alpha)\), with \(\mathbb P(Z_1>x)=(x+1/(1-\alpha))^{-1/\alpha}\) for all sufficiently large \(x\). The remainder \(W=\sum_{j\ge2}Z_j\) is independent of \(Z_1\) and sub-Gaussian: Hoeffding's lemma and \(\sum_{j\ge2}j^{2q-4}<\infty\) control its moment-generating function. Conditioning on \(|W|\le x^{1/2}\), together with the exponentially small complement, proves \(\mathbb P(S>x)\sim x^{-1/\alpha}\). Hence \(S\) cannot be Gaussian.

**4. Critical and supercritical laws.** The variance asymptotic in Step 2 gives \(\sum_{j\le n}v_j\sim c\log n\) at \(q=3/2\), and \(\sum_{j\le n}v_j\sim c n^{2q-3}/(2q-3)\) at \(q>3/2\). The bounded variables \(j\ge2\) satisfy Lindeberg's condition, because their largest absolute magnitude divided by the total standard deviation tends to zero: at \(q=3/2\), \(\sup_{j\ge2}j^{-1/2}/\sqrt{\log n}\to0\); at \(q>3/2\), \(\max_{2\le j\le n}j^{q-2}/n^{q-3/2}=O(n^{-\min\{q-3/2,1/2\}})\). The fixed finite-variance term \(Z_1\) is negligible. Lindeberg–Feller and Slutsky prove both Gaussian limits. Multiplying the variance sum by \(n^{-2q}\) proves both variance constants.

**5. Optimal power grading.** For \(q\le3/2\), \(n^3\operatorname{Var}(Q_n)\to\infty\). In the supercritical regime it tends to

\[
C(p)=\frac{\alpha^2p^4}{12[2p(1-\alpha)-3]}.
\]

Its logarithmic derivative has the sign of \(6p(1-\alpha)-12\). It tends to infinity at both boundaries of the interval \(p>3/[2(1-\alpha)]\), hence \(p_*=2/(1-\alpha)\) is the unique minimizer with value \(C(p_*)=4\alpha^2/[3(1-\alpha)^4]\).

**6. Exact equal-variance example.** For \(\alpha=1/3\), \(p=3\), \(q=2\), the formula in Step 1 simplifies to

\[
v_j=3\bigl(j^3-(j-1)^3\bigr)-\frac94\bigl(j^2-(j-1)^2\bigr)^2=\frac34\quad(j\ge1).
\]

Thus \(\operatorname{Var}(Q_n)=n^{-4}\times(3n/4)=3/(4n^3)\) exactly, not just asymptotically. In addition, direct polynomial expansion gives, for \(\alpha=1/4\), \(p=4\), \(v_j=2(6j^2-6j+1)/9\), hence \(\operatorname{Var}(Q_n)=4/(9n^3)-2/(9n^5)\). These identities cross-check the general calculation.

## Verification

Run `python3 verify.py` using the standard Python library. The verifier reconstructs rational exact cell variances for two independent choices of \(\alpha,p\), proves the equal-variance polynomial identity at each tested integer, checks the exact finite-sample variance at several \(n\), tests the rational closed form for the second example, and compares the analytical supercritical optimization constant at selected rational parameter values. The proof, not finite tests, certifies all \(n\), limits, and tails. The code has no network requirements.

## Relationship to prior work

Chopin and Gerber, *Higher-order stochastic integration through cubic stratification* (arXiv:2210.01554; first submitted 2022-10-04), discuss smooth \(C^r\) function classes, cubic stratification, and convergence/central limit theory. The present integrand has an endpoint singularity and is outside those smooth hypotheses; the new analysis is for the elementary independent one-sample-per-power-cell estimator, not their derivative-control-variates method.

Carpentier and Munos, *Adaptive Stratified Sampling for Monte-Carlo integration of Differentiable functions* (arXiv:1210.5345, 2012), develop differentiable-function adaptive stratification and an oracle variance constant. Their smooth-case formula motivates the power grading and is credited. In particular, the formal oracle-density calculation resembles the minimizer \(p_*\), so this finding does **not** claim discovery of general optimal allocation. The distinguishing results are the exact finite-grid decomposition, the non-Gaussian/critical/Gaussian fluctuation transition for the improper power integrand, its sharp variance constants, and exact equal-variance instances. Relevant probabilistic tools (Lindeberg–Feller, Kolmogorov, and Hoeffding bounds) are classical and not claimed as new.

## Limitations

The result is restricted to a one-dimensional pure power singularity, independent uniforms in deterministic power cells, and fixed grading exponent. The source differentiability-based oracle theorem cannot simply be extended by a formal substitution; the results here follow from a separate exact decomposition. Gaussian/variance statements fail when \(\alpha\ge1/2\) because the first cell has infinite second moment. There is no claim of optimality over arbitrary meshes or sophisticated randomized estimators. Searches of available mathematics records and literature do not establish definitive global priority; independent expert checking has not occurred.

## References

- Nicolas Chopin and Mathieu Gerber, *Higher-order stochastic integration through cubic stratification*, arXiv:2210.01554v1 (2022-10-04), revised 2023-06-09, https://arxiv.org/abs/2210.01554. Primary MSC classifications include 65D32 and 65C05.
- Alexandra Carpentier and Rémi Munos, *Adaptive Stratified Sampling for Monte-Carlo integration of Differentiable functions*, arXiv:1210.5345v1 (2012-10-19), https://arxiv.org/abs/1210.5345.
- S. Haber, foundational randomized integration constructions, as cited and discussed in the introductory literature review of Chopin and Gerber (1966–1969). No new priority claim is made concerning the basic one-sample-per-stratum rule.
