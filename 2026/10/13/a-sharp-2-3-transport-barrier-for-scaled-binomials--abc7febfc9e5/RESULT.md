# A sharp \(2/3\) transport barrier for scaled binomials

## Finding

For every integer \(n\ge2\), let \(X_n\sim\operatorname{Bin}(3n,1/2)\). Let \(\mathcal B_{2n}\) be the Poisson-binomial probability laws on \(\{0,\ldots,2n\}\), including Bernoulli parameters at the endpoints. Then

\[
\inf_{Y:\,\mathcal L(Y)\in\mathcal B_{2n}}
W_\infty\!\left(\frac{2X_n}{3},Y\right)\ge\frac23.
\]

The constant is **sharp as a uniform lower bound**: for \(n=2\) a coupling with \(Y\sim\operatorname{Bin}(4,1/2)\) attains \(2/3\). The first size is genuinely exceptional: at \(n=1\) the optimum is \(1/3\).

A stronger obstruction underlies the lower bound. If \(R_n\) is nearest-integer rounding of \(2X_n/3\), its mass sequence fails ordinary log-concavity at index two for every \(n\ge2\), with an explicit strictly positive defect.

## Assumptions and scope

Here a Poisson-binomial variable is any finite sum of independent Bernoulli variables. Its probability-generating polynomial is a product of linear factors with nonnegative coefficients and hence its mass sequence is log-concave (indeed ultra-log-concave). We permit Bernoulli parameters zero or one. The support condition on \(Y\) is automatic in any coupling with maximal displacement below \(2/3\), but fixes the stated approximation class.

The infinity-Wasserstein distance is
\[
W_\infty(U,V)=\inf_{\pi\in\Pi(\mathcal L(U),\mathcal L(V))}
\operatorname*{ess\,sup}_{(u,v)\sim\pi}|u-v|.
\]
Every assertion concerns exact discrete probability laws, not asymptotic weak convergence.

## Proof

**Forced rounding.** For each integer \(k\), precisely one integer lies strictly nearer than \(2/3\) to \(2k/3\): it is
\[
r(k)=\left\lfloor\frac{2k}{3}+\frac12\right\rfloor
=\left\lfloor\frac{4k+3}{6}\right\rfloor.
\]
Indeed the fractional part of \(2k/3\) is zero, \(1/3\), or \(2/3\); the next-nearest integer is at distance at least \(2/3\). Therefore any coupling with essential maximal displacement strictly below \(2/3\) must satisfy \(Y=r(X_n)\) almost surely. It is thus enough to disprove the Poisson-binomial property of the rounded law.

**Four explicit masses.** Define \(a_j=2^{3n}\Pr(r(X_n)=j)\) and write \(N=3n\). Directly identifying the preimages of \(j=0,1,2,3\) gives
\[
\begin{aligned}
a_0&=1,\\
a_1&=\binom N1+\binom N2=\frac{3n(3n+1)}2,\\
a_2&=\binom N3=\frac{n(3n-1)(3n-2)}2,\\
a_3&=\binom N4+\binom N5
=\frac{3n(n-1)(3n-2)(3n-1)(3n+1)}{40}.
\end{aligned}
\]
These formulas are valid for every \(n\ge2\). Substituting and factoring gives the identity
\[
\boxed{\ a_1a_3-a_2^2=
\frac{n^2(3n-2)(3n-1)}{80}
\bigl[81(n-2)^3+279(n-2)^2+279(n-2)+41\bigr]>0.\ }
\]
The inequality holds for every integer \(n\ge2\) because every factor is positive. The usual log-concavity inequality \(a_2^2\ge a_1a_3\) is violated. Since every Poisson-binomial mass sequence is log-concave, \(r(X_n)\) cannot have a Poisson-binomial law. This contradicts any proposed coupling at cost below \(2/3\), proving the lower bound.

**Sharpness at six original trials.** At \(n=2\), the binomial numerator masses of \(X_2\) are \((1,6,15,20,15,6,1)\) out of 64, while those of \(Y\sim\operatorname{Bin}(4,1/2)\) are \((4,16,24,16,4)\) out of 64. The following nonzero transport masses, each divided by 64, give a coupling:

| \(k\) | \(j\) | Numerator mass |
|---:|---:|---:|
| 0 | 0 | 1 |
| 1 | 0 | 3 |
| 1 | 1 | 3 |
| 2 | 1 | 13 |
| 2 | 2 | 2 |
| 3 | 2 | 20 |
| 4 | 2 | 2 |
| 4 | 3 | 13 |
| 5 | 3 | 3 |
| 5 | 4 | 3 |
| 6 | 4 | 1 |

Row and column sums recover the two binomial distributions. For every listed pair, \(\lvert 2k-3j\rvert\le2\). Hence the essential displacement is at most \(2/3\), and the previous lower bound makes it exactly \(2/3\).

**First-size boundary.** For \(n=1\), the rounded variable has generating polynomial \((1+6z+z^2)/8\), which has two strictly negative real roots. Thus it is Poisson-binomial and can be coupled with \(2X_1/3\) within \(1/3\). A positive atom at \(2/3\) is at distance at least \(1/3\) from every integer, so the radius equals \(1/3\).

## Verification

The standalone standard-library checker is `verify.py`. Execute `python3 verify.py`. It checks the binomial preimage formulas and exact factored polynomial identity for all integer sizes \(2\le n\le350\), verifies the exceptional first size, and independently reconstructs the 64-unit coupling at \(n=2\). Expected message: `VERIFY_OK parameter_cases=349 coupling_maximum_thirds=2`. The proof of the all-size claim is symbolic and independent of the finite check range.

## Relationship to prior work

Tang and Tang, *The Poisson binomial distribution—Old & New*, initially available on 27 August 2019, formulate the \(W_\infty\) approximation of rationally scaled binomials. Their preprint's Section 4 and Appendix A give low-size examples and state an open general lower-bound question; they also discuss failure of real-rootedness for a **floor** transformation, which is not the forced **nearest-integer** transformation used here. Their six-trial example supplies a known attainable radius \(2/3\). The new part here is an explicit all-size obstruction for every \(n\ge2\), proved by a single uniform coefficient factorization, not the already known isolated attainment at six trials.

The later journal article (2023) places rational-fraction approximation discussion into separately published supplementary material. Its main text and the earlier complete preprint were examined; the later supplement could not be obtained, and an equivalent statement there or elsewhere remains a residual bibliographic risk.

## Limitations

The theorem gives the sharp **uniform lower constant** over integer \(n\ge2\), not the exact optimum for each \(n\). In particular it does not establish a uniform \(2/3\) upper bound for \(n>2\), nor any fixed upper bound independent of \(n\). It does not extend automatically to other rational scalings, nonfair Bernoulli parameters, or multivariate strong-Rayleigh laws. Finite exact checks are supporting evidence only. No independent audit has been conducted.

## References

1. W. Tang and F. Tang, *The Poisson binomial distribution—Old & New*, first arXiv version 27 August 2019, arXiv:1908.10024v1, Section 4 and Appendix A. https://arxiv.org/abs/1908.10024
2. W. Tang and F. Tang, *The Poisson Binomial Distribution—Old & New*, Statistical Science **38** (2023), 108–119, DOI:10.1214/22-STS852. https://www.columbia.edu/~wt2319/PB.pdf
3. W. Tang and F. Tang, *Rational Fractions of Poisson Binomial*, supplementary material to the 2023 article, DOI:10.1214/22-STS852SUPP (bibliographic record only; full text not inspected).
