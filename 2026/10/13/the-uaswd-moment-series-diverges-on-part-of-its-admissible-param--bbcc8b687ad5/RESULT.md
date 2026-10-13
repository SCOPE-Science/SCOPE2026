# The UASWD moment series diverges on part of its admissible parameter space
## Finding
Let \(Y\) have the unit arcsine–Weibull distribution with parameters
\[
k>0,
\qquad
\lambda>0.
\]
After the source's change of variable, its raw moment is represented first by the convergent integral
\[
\mu_r
=
\frac1\pi
\int_0^\infty
\frac{e^{-r\lambda u^{1/k}}e^{-u/2}}
{\sqrt{1-e^{-u}}}
\,du,
\qquad r>0.
\]
The paper then expands both factors and states Eq. (3.8):
\[
\mu_r
=
\frac1\pi
\sum_{n=0}^{\infty}
\frac{(-1)^n(r\lambda)^n}{n!}
\sum_{m=0}^{\infty}
\frac{\binom{2m}{m}}{4^m}
\frac{\Gamma(n/k+1)}{(m+1/2)^{n/k+1}}.
\]

This series representation is not valid throughout the stated parameter space.

Because every term in the inner \(m\)-sum is positive apart from the common sign \((-1)^n\), the magnitude of the \(n\)-th outer block is at least its \(m=0\) contribution
\[
A_n
=
\frac{2}{\pi}
\frac{(r\lambda)^n}{n!}
2^{n/k}
\Gamma(n/k+1).
\]
The consecutive ratio obeys
\[
\frac{A_{n+1}}{A_n}
=
\frac{r\lambda\,2^{1/k}}{n+1}
\frac{\Gamma((n+1)/k+1)}{\Gamma(n/k+1)}
\sim
r\lambda
\left(\frac2k\right)^{1/k}
n^{1/k-1}.
\]
Therefore:
\[
\boxed{
0<k<1
\quad\Longrightarrow\quad
A_n\not\to0
\text{ for every }r\lambda>0,
}
\]
and at the boundary
\[
\boxed{
k=1:\quad A_{n+1}/A_n=2r\lambda.}
\]
Hence Eq. (3.8) diverges for
\[
0<k<1
\]
for every positive moment order and scale, and it also diverges for
\[
k=1,
\qquad
2r\lambda\ge1.
\]

The failure is in the termwise integration, not in existence of the moment. Since
\[
0<Y<1,
\]
every positive raw moment is finite.

A particularly transparent admissible point is
\[
k=1,
\qquad
\lambda=1,
\qquad
r=1.
\]
The true mean is
\[
\boxed{
\mu_1
=
\frac{\Gamma(3/2)}{\sqrt\pi\,\Gamma(2)}
=
\frac12.
}
\]
But the \(m=0\) terms of the source's outer series are
\[
\boxed{
\frac{2}{\pi}(-2)^n,
}
\]
so they grow in magnitude rather than tend to zero.

A valid replacement is obtained by expanding only
\[
(1-e^{-u})^{-1/2}
=
\sum_{m=0}^{\infty}
\frac{\binom{2m}{m}}{4^m}e^{-mu}.
\]
All terms are nonnegative, so Tonelli's theorem gives
\[
\boxed{
\mu_r
=
\frac1\pi
\sum_{m=0}^{\infty}
\frac{\binom{2m}{m}}{4^m}
\int_0^\infty
 e^{-r\lambda u^{1/k}}
 e^{-(m+1/2)u}
\,du.
}
\]
This representation is valid for every
\[
k>0,
\quad
\lambda>0,
\quad
r>0.
\]

At \(k=1\), the integral can be evaluated explicitly:
\[
\boxed{
\mu_r
=
\frac{\Gamma(r\lambda+1/2)}
{\sqrt\pi\,\Gamma(r\lambda+1)}.
}
\]

The same invalid interchange appears inside the source's moment-generating-function series Eq. (3.12). For \(0<k<1\), the coefficient row corresponding to the first positive outer power already has nonvanishing integrated Taylor terms. For \(k=1\), any \(\lambda>0\) admits an outer power index \(n\) with
\[
2n\lambda\ge1,
\]
so the corresponding nested coefficient series diverges. Thus Eq. (3.12), interpreted as the printed ordinary nested series, is not valid there for nonzero \(t\), even though the actual MGF is entire because the random variable is bounded.

The source's empirical maximum-likelihood fit is
\[
k=0.9952,
\qquad
\lambda=0.9716.
\]
Since the fitted shape satisfies \(k<1\), the printed Eq. (3.8) diverges for every positive raw moment at the fitted parameter pair.

## Assumptions and scope
The model parameter domain is exactly the source's stated
\[
k>0,
\qquad
\lambda>0,
\]
and the random variable lies in
\[
0<Y<1.
\]
The claim concerns the infinite series in Eqs. (3.8) and (3.12), not the defining CDF, PDF, quantile, or the integral moment formula Eq. (3.4).

The result does not assert that Eq. (3.8) diverges for every \(k>1\). It identifies a rigorous admissible region where the source's unrestricted equality fails. No alternative summability convention is assumed; the source presents ordinary infinite sums and uses the formulas as ordinary moments and an MGF.

The actual MGF exists for every real and complex argument because \(Y\) is bounded. The issue is solely the source's integrated Taylor representation.

## Proof
The source writes
\[
e^{-r\lambda u^{1/k}}
=
\sum_{n=0}^{\infty}
\frac{(-1)^n(r\lambda)^n}{n!}u^{n/k}
\]
and
\[
(1-e^{-u})^{-1/2}
=
\sum_{m=0}^{\infty}
\frac{\binom{2m}{m}}{4^m}e^{-mu}.
\]
Formally integrating the product term by term gives Eq. (3.8).

For fixed \(n\), the inner \(m\)-sum is positive. Its \(m=0\) term gives the lower bound \(A_n\) displayed above. The gamma-ratio asymptotic
\[
\frac{\Gamma(z+a)}{\Gamma(z)}
\sim z^a
\]
with
\[
z=n/k+1,
\qquad
a=1/k
\]
yields
\[
\frac{A_{n+1}}{A_n}
\sim
r\lambda
\left(\frac2k\right)^{1/k}
n^{1/k-1}.
\]
If \(k<1\), the exponent \(1/k-1\) is positive, so the ratio tends to infinity. In particular, the outer terms of Eq. (3.8) cannot tend to zero.

If \(k=1\), gamma recurrence gives the exact ratio
\[
A_{n+1}/A_n=2r\lambda.
\]
When \(2r\lambda\ge1\), the terms again fail the necessary term test.

For the valid replacement, expand only the reciprocal square root. Since every term of that expansion and every remaining factor in the integral is nonnegative, Tonelli's theorem justifies interchange of the \(m\)-sum and the integral without any cancellation argument.

When \(k=1\), substitute
\[
z=e^{-u}
\]
into the original moment integral. This gives
\[
\mu_r
=
\frac1\pi
\int_0^1
z^{r\lambda-1/2}(1-z)^{-1/2}
\,dz
=
\frac1\pi
B(r\lambda+1/2,1/2),
\]
which simplifies to the stated gamma ratio.

The MGF series uses these same integrated moment coefficients. For \(0<k<1\), the first positive power already inherits the divergence. At \(k=1\), for any \(\lambda>0\), choose a positive integer \(n\) such that \(2n\lambda\ge1\); that coefficient row fails the same term test.

## Verification
The accompanying checker evaluates the original integral at
\[
k=\lambda=r=1
\]
and obtains
\[
0.5
\]
to high precision. It independently evaluates the beta-function closed form and obtains the same value.

The checker also evaluates the \(m=0\) integrated Taylor terms. At \(k=1\), their magnitudes are
\[
\frac2\pi,
\frac4\pi,
\frac8\pi,
\frac{16}\pi,
\ldots,
\]
confirming the exact ratio two. At \(k=1/2\), the growth is substantially faster.

Finally, the checker evaluates the positive one-sum replacement for the \(k=1\) example and confirms agreement with the exact beta-function value.

The finite computations are consistency checks. The divergence statement itself follows from the analytic term-ratio proof.

## Relationship to prior work
Alghufily et al. derive Eq. (3.8) by expanding both the transformed Weibull factor and the reciprocal square-root factor and then integrating the resulting double series. The paper gives the parameter space as \(k,\lambda>0\) and does not state convergence restrictions for Eq. (3.8). The same integrated coefficients are then reused in its MGF series Eq. (3.12).

The source's reported real-data maximum-likelihood estimate is \(k=0.9952\), \(\lambda=0.9716\), which lies in the divergence region proved here. Thus the issue is not confined to a remote boundary of the model.

A related 2026 unit arcsine–exponential model gives a closed gamma-ratio moment formula in the exponential special case. After accounting for reciprocal rate-versus-scale parameterization, that special-case formula is consistent with the \(k=1\) identity above. It does not identify the convergence failure of the UASWD double series.

Focused searches using the exact DOI, the UASWD name, moment-series terminology, gamma-series convergence, and termwise-integration aliases did not locate a corrigendum or another source already stating this UASWD-specific obstruction.

## Limitations
The exact convergence region of the full double series for \(k>1\) is not classified here.

The result concerns ordinary convergence of the printed series. It does not study generalized summation procedures, which the source neither states nor uses.

The current finding does not reassess the source's separate Rényi-entropy formula or its likelihood computations.

A very recent unindexed author correction could exist outside the sources examined.

## References
1. N. Alghufily, K. S. Sultan, M. M. M. Mansour, and N. M. Mohamed, “Statistical properties and inference for a new bounded lifetime model with application,” AIMS Mathematics 11 (2026), 14121–14140. DOI: 10.3934/math.2026580.
2. A. S. Al-Moisheer, K. S. Sultan, M. N. Mousa, and M. M. M. Mansour, “The Unit Arcsine–Exponential Distribution and Its Statistical Properties with Inference and Application to Reliability Data,” Axioms 15 (2026), 218. DOI: 10.3390/axioms15030218.
