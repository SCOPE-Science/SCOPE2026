# A sharp probe-depth mean-square crossover for Gaussian inverse-trace Lanczos quadrature

## Finding

Consider a real symmetric positive-definite \(2\times2\) matrix \(A\) with two **distinct** eigenvalues \(a>b>0\), and fix an even matrix–vector-product budget \(B\ge2\). Let \(\kappa=a/b\), \(u=\sqrt\kappa>1\), and \(\tau=\operatorname{tr}(A^{-1})\). Compare two precisely specified Gaussian stochastic Lanczos quadrature (SLQ) estimators of \(\tau\):

- **Shallow:** average \(B\) independent one-node SLQ estimates, each using one product with \(A\).
- **Deep:** average \(B/2\) independent two-node SLQ estimates, each using two products with \(A\).

The exact mean-squared errors are

\[
\begin{aligned}
\operatorname{MSE}_{\mathrm{shallow}}
 &=\frac1{b^2}\left[\frac{(u-1)^4}{u^4}+\frac{4(u^2-u+1)}{Bu^3}\right],\\
\operatorname{MSE}_{\mathrm{deep}}
 &=\frac{4}{Bb^2}\left(1+u^{-4}\right).
\end{aligned}
\]

Define the **critical product budget**

\[
B_*(u)=\frac{4(u^4-u^3+u^2-u+1)}{(u-1)^4}.
\]

Then \(\operatorname{MSE}_{\mathrm{shallow}}<\operatorname{MSE}_{\mathrm{deep}}\) **if and only if** \(B<B_*(u)\); the comparison reverses when \(B>B_*(u)\), with equality precisely at \(B=B_*(u)\). The threshold decreases strictly from \(+\infty\) as \(u\downarrow1\) to \(4\) as \(u\to\infty\). Thus **every** distinct-spectrum matrix favors shallow SLQ at \(B=2\) and \(B=4\), while for **each** even \(B\ge6\) there is exactly one spectrum condition number \(\kappa_B>1\) at which the preferred allocation switches. At \(B=8\), this threshold is \(\kappa_B\approx26.0810875046554\).

In particular, the two-product benchmark satisfies the stronger uniform comparison

\[
\operatorname{MSE}_{\mathrm{shallow}}
 <\tfrac12\operatorname{MSE}_{\mathrm{deep}}
 \qquad (B=2,\;a>b>0).
\]

The result compares **two named SLQ allocations**, not all methods available to a two-dimensional matrix-vector-product oracle.

## Assumptions and scope

The matrix \(A\in\mathbb R^{2\times2}\) is symmetric positive definite and has eigenvalues \(a>b>0\). Each stochastic probe \(g\sim N(0,I_2)\) has two independent standard normal coordinates, and all probes are independent between and within the two estimators. Lanczos arithmetic is exact. The matrix-vector-product budget \(B\in\{2,4,6,\ldots\}\) counts applications of \(A\) to a vector, not scalar arithmetic or probe generation.

For a nonzero probe \(g\), one-node Gaussian SLQ for \(f(t)=1/t\) produces

\[
Q(g)=\|g\|_2^2\left(\frac{g^\top Ag}{\|g\|_2^2}\right)^{-1}
=\frac{\|g\|_2^4}{g^\top Ag}.
\]

Two-node Gaussian SLQ produces \(D(g)=\|g\|_2^2 e_1^\top T_2^{-1}e_1\), where \(T_2\) is its two-step Lanczos tridiagonal matrix. Since \(A\) has two distinct eigenvalues and both spectral projections of a Gaussian probe are nonzero almost surely, the two Lanczos vectors form an orthonormal basis of \(\mathbb R^2\). Therefore

\[
D(g)=g^\top A^{-1}g\quad\text{almost surely}.
\]

Write \(Q_1,\ldots,Q_B\) and \(D_1,\ldots,D_{B/2}\) for independent copies. The estimators are \(\widehat\tau_1=B^{-1}\sum_{i=1}^B Q_i\) and \(\widehat\tau_2=(B/2)^{-1}\sum_{i=1}^{B/2} D_i\). Mean-squared error means \(\mathbb E[(\widehat\tau_j-\tau)^2]\), including squared bias.

## Proof

**1. Spectral and radial reduction.** Rotational invariance permits \(A=\operatorname{diag}(a,b)\). Write \(g=R(\cos\theta,\sin\theta)\), with \(R^2\sim\chi^2_2\) independent of \(\theta\), uniform on \([0,2\pi)\). Set \(h(\theta)=a\cos^2\theta+b\sin^2\theta\). Then \(Q=R^2/h(\theta)\). The Gaussian radial moments are \(\mathbb E R^2=2\) and \(\mathbb E R^4=8\).

**2. Two exact angular integrals.** Using a tangent substitution on the quadrants, one obtains

\[
I_1(a,b)=\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{h(\theta)}
=\frac1{\sqrt{ab}}.
\]

Replacing \((a,b)\) by \((a+s,b+s)\) and differentiating at \(s=0\) under the integral sign gives

\[
I_2(a,b)=\frac1{2\pi}\int_0^{2\pi}\frac{d\theta}{h(\theta)^2}
=\frac{a+b}{2(ab)^{3/2}}.
\]

The derivatives are legitimate for \(a,b>0\). Hence

\[
\mathbb EQ=\frac2{\sqrt{ab}},\qquad
\mathbb EQ^2=\frac{4(a+b)}{(ab)^{3/2}},\qquad
\operatorname{Var}(Q)=\frac{4(a+b)}{(ab)^{3/2}}-\frac4{ab}.
\]

The exact target is \(\tau=1/a+1/b=(a+b)/(ab)\), so the one-node bias is

\[
\mathbb EQ-\tau=-\frac{(\sqrt a-\sqrt b)^2}{ab},
\]

strictly negative for distinct eigenvalues. Independently averaging \(B\) probes divides the variance by \(B\), but preserves this bias.

**3. Deep quadrature moments.** As noted above, two-step Lanczos produces \(D(g)=g^\top A^{-1}g\). Standard independent Gaussian-square moments yield \(\mathbb ED=\tau\) and

\[
\operatorname{Var}(D)=2\operatorname{tr}(A^{-2})
=2(a^{-2}+b^{-2}).
\]

The average of \(B/2\) copies is unbiased and has variance \(4(a^{-2}+b^{-2})/B\).

**4. Exact comparison.** Substitute \(a=u^2b\), with \(u>1\), into the squared-bias-plus-variance identity from step 2 and the variance from step 3. This gives exactly the displayed MSE expressions. Their difference factors as

\[
\operatorname{MSE}_{\mathrm{deep}}-\operatorname{MSE}_{\mathrm{shallow}}
=\frac{4(u^4-u^3+u^2-u+1)-B(u-1)^4}{Bb^2u^4}.
\]

Its denominator is positive. Thus its sign equals that of \(B_*(u)-B\). Direct differentiation gives

\[
B_*'(u)=-\frac{4(u+1)(3u^2-4u+3)}{(u-1)^5}<0\quad(u>1),
\]

since \(3u^2-4u+3=3(u-2/3)^2+5/3>0\). The limits at \(u=1\) and \(u=+\infty\) are \(+\infty\) and \(4\), respectively. Therefore for even \(B=2,4\) the shallow MSE is always strictly smaller, and each even \(B\ge6\) has exactly one crossing. For \(B=2\), direct simplification also gives

\[
\tfrac12\operatorname{MSE}_{\mathrm{deep}}-
\operatorname{MSE}_{\mathrm{shallow}}
=\frac{2(u-1)^2}{b^2u^3}>0.
\]

All inequalities and identities hold for every admissible spectrum, with no asymptotic passage. This completes the proof.

## Verification

Run `python verify.py` after installing dependencies listed in `requirements.txt`. The standalone verifier checks the MSE identities, difference factorization, sign derivative, special budgets, and three rational two-node Lanczos calculations using symbolic arithmetic. It independently approximates both angular integrals for four spectra by periodic quadrature, brackets six crossing roots, and runs seeded Gaussian diagnostics on two distinct spectra. It reports `VERIFY_OK` if all assertions hold. Numerical integration and simulations are **diagnostics only**; the infinite-family comparison is proved in the preceding algebraic argument. In particular, the random checks do not certify universal coverage or absence of earlier literature.

For \(B=8\), the crossing in \(u\) is approximately \(5.10696460773475\), yielding \(\kappa_8\approx26.0810875046554\). At \((a,b)=(4,1)\), the shallow estimator has MSE \(1/4\) versus deep \(17/32\); at \((a,b)=(36,1)\), the shallow MSE exceeds the deep MSE, illustrating both sides with the same budget.

## Relationship to prior work

Stochastic Lanczos quadrature, including inverse traces, was established by Ubaru, Chen, and Saad (2017). Cortinovis and Kressner (2020) developed Gaussian trace-estimation tails and their interaction with Lanczos; the preprint has the verified primary MSC class \(65C05\). Chen, Trogdon, and Ubaru (2022) give unified matrix-free quadrature error bounds. Li, Huang, and Zhu (2023) study optimized depth-versus-probe resource allocation for log-determinants and associated bounds. Those analyses motivate this calculation but do not state, in the inspected material, the exact inverse-trace two-eigenvalue mean-square allocation boundary above.

This theorem is distinct from two-dimensional antithetic **log-determinant** direction coupling: the target here is the inverse trace, the probes are independent unnormalized Gaussian vectors, and the competing decisions are one versus two Lanczos nodes at fixed product budget, not the dependence between same-depth probes. Nor is it the rank-two Hutch++ variance comparison, which uses a different trace estimator.

## Limitations

The result uses independent unnormalized Gaussian probes, exact arithmetic, a fixed real \(2\times2\) SPD matrix with distinct eigenvalues, two pure depth allocations, and the specific inverse function. It does not apply verbatim to Rademacher probes, normalized-Haar probes scaled to dimension, arbitrary two-eigenvalue matrices with higher multiplicity, finite precision, or different allocation mixtures. Equal eigenvalues have one-step Lanczos breakdown and hence a different actual matvec-cost accounting; the limit \(\kappa\downarrow1\) is not an included endpoint.

A two-dimensional matrix can be recovered with two carefully chosen deterministic matrix-vector products. Consequently this comparison **does not** assert minimax oracle complexity or universal optimality among all trace estimators, nor that Gaussian SLQ must be deployed in dimension two. Its value is as a sharp, reproducible bias–variance counterbenchmark for the familiar depth-versus-probe design decision. Possible equivalent specialized calculations in less searchable literature remain a priority risk.

## References

1. S. Ubaru, J. Chen, and Y. Saad, *Fast estimation of tr(f(A)) via stochastic Lanczos quadrature*, SIAM J. Matrix Anal. Appl. 38 (2017), 1075–1099. DOI: `10.1137/16M1104974`. Primary text: `https://www.cs.cornell.edu/courses/cs6241/2020sp/readings/Ubaru-2017-fast.pdf`.
2. A. Cortinovis and D. Kressner, *On randomized trace estimates for indefinite matrices with an application to determinants*, original public arXiv version 20 May 2020, `arxiv:2005.10009v1`; `https://arxiv.org/abs/2005.10009`. Primary MSC \(65C05\).
3. T. Chen, T. Trogdon, and S. Ubaru, *Randomized matrix-free quadrature: Unified and uniform bounds for stochastic Lanczos quadrature and the kernel polynomial method*, original public arXiv version 5 April 2022, `arxiv:2204.01941v1`; `https://arxiv.org/abs/2204.01941`.
4. W. Li, Y. Huang, and S. Zhu, *An analysis on stochastic Lanczos quadrature with asymmetric quadrature nodes*, original public arXiv version 3 July 2023, `arxiv:2307.00847v1`; `https://arxiv.org/abs/2307.00847`.
