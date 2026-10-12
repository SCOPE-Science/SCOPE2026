# Exact posterior-error and false-stop law for sign-probed XTrace on a rank-two identity
## Finding

For every integer \(k\ge3\) and every \(\lambda>0\), take
\[
A=\lambda I_2,\qquad \operatorname{tr}(A)=2\lambda.
\]
In the *unnormalized Rademacher* versions of the published naïve XTrace and XNysTrace definitions, draw independent test vectors
\[
\omega_i\in\{-1,+1\}^{2},\qquad i=1,\dots,k,
\]
each uniformly distributed. XTrace uses \(2k\) matrix-vector products for these \(k\) probes; XNysTrace uses \(k\) such products. Both methods have the same basic estimators \(B_i\) on this instance.

Form the published exchangeable trace estimate and its posterior error proxy:
\[
\widehat T=\frac1k\sum_{i=1}^{k}B_i,
\qquad
\widehat e^2=\frac1{k(k-1)}\sum_{i=1}^{k}(B_i-\widehat T)^2.
\]
Their **complete joint distribution** is
\[
\boxed{
\begin{array}{c|c|c}
\widehat T & \widehat e & \Pr \\
\hline
\lambda &0&2^{1-k}\\
\lambda(2+1/k)&\lambda/k&k2^{1-k}\\
2\lambda&0&1-(k+1)2^{1-k}
\end{array}}
\]
(the third probability is zero when \(k=3\)). Consequently,
\[
\mathbb E\widehat T=2\lambda,
\qquad
\mathbb E(\widehat T-2\lambda)^2
=\lambda^2 2^{1-k}\left(1+\frac1k\right),
\qquad
\mathbb E\widehat e^2=\frac{\lambda^2 2^{1-k}}k,
\]
so the exact mean-squared calibration factor is
\[
\boxed{\frac{\mathbb E(\widehat T-2\lambda)^2}
{\mathbb E\widehat e^2}=k+1.}
\]
Every pair of distinct basic estimators \(B_i,B_j\) has correlation exactly \(1/2\).

The paper's adaptive test stops at a probe count when \(\widehat e\le\delta|\widehat T|\). If a stop is called **false** when
\[
|\widehat T-2\lambda|>\delta(2\lambda),
\]
then, at this inspected probe count and for every \(0<\delta<1/2\), its false-stop probability is exactly
\[
\boxed{
2^{1-k}\left[
1+k\,\mathbf{1}_{\{1/(2k+1)\le\delta<1/(2k)\}}
\right].
}
\]
In particular, with probability \(2^{1-k}\), the reported error is exactly zero although the trace estimate has **50% true relative error**. With \(k=4\), for instance, this happens with probability \(1/8\). This is a precise one-stage false acceptance event; it makes no claim about later continuation conditional on failing the test.

## Assumptions and scope

The matrix is a real positive definite scalar multiple of the \(2\)-by-\(2\) identity. The sign probes are independent and unnormalized, so each has squared Euclidean norm \(2\).

The mathematical definitions used are the *naïve* XTrace Algorithm 1.2 and *naïve* XNysTrace Algorithm 1.3 in the first arXiv version of the defining paper. Orthogonalization returns an orthonormal basis for the **actual** span even when sampled columns are linearly dependent, and the Nyström definition uses a Moore–Penrose pseudoinverse. Thus the expression is well-defined on rank-deficient sketches. The efficient full-column-rank update formulas are not asserted to produce the same output in finite precision.

The paper separately recommends sampling from a spherically symmetric distribution and normalizing residual directions. That is a distinct algorithmic choice **excluded** here. The input and test distribution here are among the sign-probe settings explicitly treated in the paper's definitions and experiments.

The result concerns a fixed positive number \(k\ge3\) of test probes and the stated one-stage tolerance test; it does not claim a general guarantee or a general counterexample for every input or probe distribution.

## Proof

For the sign vector \(\omega=(u,v)\), put \(\xi=uv\in\{-1,+1\}\). Two sign vectors lie on the same one-dimensional *unoriented* line precisely when their \(\xi\) values agree. The two lines are perpendicular, and \(\xi_1,\ldots,\xi_k\) are independent fair signs.

Let \(P_{-i}\) be the orthogonal projector onto the span of the other \(k-1\) probes. For \(A=\lambda I_2\), the range of \(A\Omega_{-i}\) equals this span, and the Nyström approximation obeys
\[
A\Omega_{-i}(\Omega_{-i}^{\mathsf T}A\Omega_{-i})^\dagger
(A\Omega_{-i})^{\mathsf T}=\lambda P_{-i}.
\]
The latter identity follows from the singular-value decomposition of \(\Omega_{-i}\): the product \(\Omega_{-i}(\Omega_{-i}^{\mathsf T}\Omega_{-i})^\dagger\Omega_{-i}^{\mathsf T}\) is exactly its range projector, including on rank-deficient samples.

Hence both published naïve basic estimators reduce to
\[
B_i=\lambda\operatorname{rank}(P_{-i})
+\lambda\|(I-P_{-i})\omega_i\|_2^2.
\]
If all the other signs \(\xi_j\), \(j\ne i\), are equal, then \(P_{-i}\) has rank one. The held-out vector is either on the same line (giving \(B_i=\lambda\)) or on the perpendicular line (giving \(B_i=3\lambda\)). If both signs occur among the other probes, the projector is the identity and \(B_i=2\lambda\).

There are only three mutually exclusive patterns, for \(k\ge3\):

* All \(\xi_i\) agree. Every \(B_i=\lambda\); there are \(2\) such sign patterns out of \(2^k\).
* Exactly one \(\xi_i\) differs from all the others. Its basic estimator is \(3\lambda\); all others are \(2\lambda\). There are \(2k\) such patterns. The mean equals \(\lambda(2+1/k)\) and the scaled spread is \(\widehat e^2=\lambda^2/k^2\).
* Both sign categories have multiplicity at least two. Every other-probe span is the whole plane, so all \(B_i=2\lambda\). The remaining \(2^k-2-2k\) patterns yield this case.

Each pattern is equally likely after forgetting the orientation within a line. Dividing the counts by \(2^k\) proves the complete joint law.

Direct averaging gives
\[
\mathbb E(\widehat T-2\lambda)
=2^{1-k}(-\lambda)+k2^{1-k}(\lambda/k)=0,
\]
\[
\mathbb E(\widehat T-2\lambda)^2
=2^{1-k}\lambda^2+k2^{1-k}(\lambda/k)^2,
\]
and
\[
\mathbb E\widehat e^2=k2^{1-k}(\lambda/k)^2.
\]
The stated factor \(k+1\) follows.

More directly, for each \(i\), the centered basic estimator \(B_i-2\lambda\) equals \(-\lambda\) on the all-equal event and \(+\lambda\) exactly when the \(i\)-th sign is the unique minority. Both have probability \(2^{1-k}\), and otherwise it is zero. Thus
\[
\operatorname{Var}(B_i)=\lambda^2 2^{2-k},
\qquad
\operatorname{Cov}(B_i,B_j)=\lambda^2 2^{1-k}\quad(i\ne j),
\]
which proves correlation \(1/2\) and is compatible with Proposition 3.1 in the defining source.

For the stopping claim, the all-equal outcome always passes \(\widehat e\le\delta|\widehat T|\), while its actual relative error is \(1/2\). The singleton outcome passes the posterior test exactly when
\[
\frac{\lambda/k}{\lambda(2+1/k)}=\frac1{2k+1}\le\delta,
\]
but its true relative error is \(1/(2k)\). It is therefore a false stop precisely when
\[
\frac1{2k+1}\le\delta<\frac1{2k}.
\]
All remaining outcomes have zero true error. Summing the corresponding disjoint probabilities proves the exact expression.

## Verification

The accompanying standalone `verify.py` computes the projector for each leave-one-out sketch directly from its sign vectors, without relying on the three-case distribution. It enumerates all \(4^k\) ordered sign-vector families for \(3\le k\le8\), uses exact rational arithmetic, and verifies the joint frequencies, mean squared error, reported posterior squared error, correlations, and stopping probabilities at tolerance boundaries. It also checks the Nyström projector identity independently on full-rank and rank-deficient rational sketches.

This exhaustive finite enumeration protects against transcription mistakes for the tested probe counts. The proof above establishes the formulas for *all* integers \(k\ge3\), without extrapolating from computation.

## Relationship to prior work

Epperly, Tropp, and Webber's XTrace paper supplies the two exchangeable trace estimators, their posterior error proxy, and the adaptive tolerance rule. It already proves the *general* correlation identity relating expected posterior error to true mean-squared error (Proposition 3.1, section 3.1) and discusses mild positive correlations in examples. No novelty is claimed for the basic estimator definitions, the fact that correlations can bias the proxy, or the adaptive rule itself.

The new result is an **exact joint law** for both estimators with a discrete, explicitly included sign-probe distribution on the smallest nontrivial scalar-identity test matrix. It identifies the previously unstated correlation \(1/2\), the resulting exact \(k+1\) squared-calibration factor, and the complete tolerance-dependent false-stop probability. The general correlation identity does not by itself determine any of these finite-instance values.

Epperly and Tropp's earlier work on posterior matrix error and jackknife variance develops **different resampling estimators** for matrix approximations and establishes averaged variance inequalities. It does not imply the joint distribution of the XTrace/XNysTrace residual-probe basic estimates. Classical Hutchinson is in fact exact on this diagonal input with Rademacher probes; this sharpens the interpretive contrast but does not constitute the new claim.

The earlier Hutch++ construction can be specialized to an identity matrix; that elementary one-sketch marginal calculation does not determine the joint law here. The present statement does **not** claim that the marginal law of a single deflated Rademacher probe is new; it concerns \(k\) coupled leave-one-out estimates, their posterior statistic, and the stopping-decision law.

The source's normalization option and optimized full-rank update formulas have different operating assumptions. The finding concerns only the mathematically explicit unnormalized, possibly rank-deficient naïve algorithms.

## Limitations

* The input is two-dimensional and proportional to the identity; the output law is not asserted for arbitrary spectra or dimensions.
* Test probes are independent unnormalized Rademacher signs. Continuous Gaussian probes and the source's spherical normalization proposal need separate analysis and are not covered by the theorem.
* Degenerate test spans are legitimate for the naïve formulas but may be outside the scope of optimized full-rank inverse-based implementations.
* The event calculated is a false decision at **one** probe count, not the probability of final failure of every multi-stage adaptive procedure.
* A vanishing posterior proxy is not asserted to be a mathematical certificate, and the source did not claim a rigorous per-instance confidence guarantee for that heuristic.
* Despite the mean-squared calibration ratio \(k+1\), both the true mean-squared error and false-stop probability decay exponentially in \(k\) for this fixed two-dimensional test case.

## References

1. E. N. Epperly, J. A. Tropp and R. J. Webber, *XTrace: Making the most of every sample in stochastic trace estimation*, arXiv:2301.07825v1 (first public version 2023-01-19), Algorithms 1.2–1.3, §§2.3, 3.1–3.2, and Proposition 3.1. Later published in SIAM Journal on Matrix Analysis and Applications 45 (2024).
2. E. N. Epperly and J. A. Tropp, *Efficient error and variance estimation for randomized matrix computations*, arXiv:2207.06342 (initial release 2022-07-13), §3.1 on Tukey jackknife variance; SIAM Journal on Scientific Computing 46 (2024).
3. R. A. Meyer, C. Musco, C. Musco and D. P. Woodruff, *Hutch++: Optimal stochastic trace estimation*, arXiv:2010.09649 (2020), for earlier variance reduction by randomized deflation.
