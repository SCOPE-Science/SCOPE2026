# Strict concavity of the Chvátal negative-binomial local-minimum sequence
## Finding
For every \(r>0\), define
\[
a_r(n)=I_{r/(n+r+1)}(r,n+1),\qquad n=0,1,2,\ldots,
\]
where \(I_x(a,b)\) denotes the regularized incomplete beta function. Equivalently, by the negative-binomial identity used by Guo, Tao, and Hu,
\[
a_r(n)=\left(\frac{r}{n+r+1}\right)^r\sum_{k=0}^n\binom{k+r-1}{k}\left(1-\frac{r}{n+r+1}\right)^k.
\]
Then \(a_r\) is strictly concave on the nonnegative integers:
\[
a_r(n+2)-a_r(n+1)<a_r(n+1)-a_r(n)\qquad\text{for every }n\ge0.
\]

Writing \(\Delta_N=a_r(N)-a_r(N-1)\) for \(N\ge1\), there is the exact factorization
\[
\Delta_N=P_{r,N}H_{r,N},
\]
with
\[
P_{r,N}=\frac{\Gamma(N+r+1)}{\Gamma(r)\Gamma(N+1)}\frac{r^rN^N}{(N+r)^{N+r+1}},
\]
and
\[
H_{r,N}=1-\int_0^1\frac{(1+t/N)^N}{(1+t/(N+r))^{N+r+1}}\,dt.
\]
Both factors are positive and strictly decreasing in \(N\). The published source proves \(\Delta_N>0\); the new statement identifies the stronger strict diminishing-returns structure \(\Delta_{N+1}<\Delta_N\).

## Assumptions and scope
The shape parameter is any real \(r>0\), with no integrality assumption. The index \(n\) is any nonnegative integer. The result concerns exactly the local-minimum sequence introduced in the proof of the negative-binomial mean-tail infimum theorem. It does not assert continuous concavity in a real interpolation of \(n\), nor does it claim analogous concavity for arbitrary moving beta cutoffs.

Equivalently, \(a_r(N-1)\) is the probability that a central \(F\) random variable with numerator and denominator degrees of freedom \(2r\) and \(2N\), respectively, is at most \(1\). Thus the theorem also gives strict discrete concavity, along even denominator degrees of freedom, of this normalized \(F\)-CDF value.

## Proof
The source gives
\[
a_r(n)=\frac1{\mathrm B(n+1,r)}\int_0^{r/(n+r+1)}x^{r-1}(1-x)^n\,dx.
\]
Fix \(N\ge1\). Repeating the source's change of variables for the difference between consecutive terms, and using its Lemma 2.2, gives
\[
\Delta_N=\frac1{\mathrm B(N+1,r)}\bigl(c_{r,N}-J_{r,N}\bigr),
\]
where
\[
c_{r,N}=\frac{r^rN^N}{(N+r)^{N+r+1}}
\]
and
\[
J_{r,N}=\int_{(N+r)/r}^{(N+r+1)/r}(u-1)^Nu^{-N-r-1}\,du.
\]
Put \(u=(N+r+t)/r\). Direct cancellation yields
\[
J_{r,N}=c_{r,N}\int_0^1R_{r,N}(t)\,dt,
\qquad
R_{r,N}(t)=\frac{(1+t/N)^N}{(1+t/(N+r))^{N+r+1}}.
\]
This proves the displayed factorization \(\Delta_N=P_{r,N}H_{r,N}\).

First, \(P_{r,N}>0\), and
\[
\frac{P_{r,N+1}}{P_{r,N}}
=\left(1+\frac1N\right)^N
\left(\frac{N+r}{N+r+1}\right)^{N+r+1}<1.
\]
Indeed, \(N\log(1+1/N)<1\), whereas \((N+r+1)\log(1+1/(N+r))>1\). Thus \(P_{r,N}\) is strictly decreasing.

Second, for \(0<t\le1\),
\[
N\log(1+t/N)<t
\]
and
\[
(N+r+1)\log(1+t/(N+r))>t.
\]
For the second inequality, use \(\log(1+x)>x/(1+x)\) and \((N+r+1)/(N+r+t)\ge1\). Hence \(0<R_{r,N}(t)<1\), so \(H_{r,N}>0\).

It remains to compare \(H_{r,N}\) across \(N\). For fixed \(t>0\), set
\[
\phi_t(x)=x\log(1+t/x).
\]
Then
\[
\log R_{r,N}(t)=\phi_t(N)-\phi_t(N+r)-\log(1+t/(N+r)),
\]
and
\[
\phi_t''(x)=-\frac{t^2}{x(x+t)^2}<0.
\]
Therefore \(\phi_t'\) is strictly decreasing, and differentiation with respect to the continuous variable \(N\) gives
\[
\frac\partial{\partial N}\log R_{r,N}(t)
=\phi_t'(N)-\phi_t'(N+r)+\frac{t}{(N+r)(N+r+t)}>0.
\]
Thus \(R_{r,N+1}(t)>R_{r,N}(t)\) for every \(t>0\), so \(H_{r,N+1}<H_{r,N}\). Since \(P_{r,N}\) and \(H_{r,N}\) are both positive and strictly decreasing,
\[
\Delta_{N+1}<\Delta_N.
\]
This is exactly the stated strict discrete concavity.

## Verification
The proof is analytic and does not depend on numerical enumeration. A standalone checker, `verify.py`, independently evaluates the incomplete-beta definition and the factorization on a broad deterministic grid of positive shape parameters and indices, then checks strict decrease of consecutive increments on that grid. Its finite checks are only a consistency test; the inequalities in the proof establish the theorem for all \(r>0\) and all integers \(n\ge0\).

The critical nonstandard input from the source is its exact beta-integral representation and Lemma 2.2. Both were inspected in the full arXiv text. All subsequent inequalities are elementary and are reproduced above.

## Relationship to prior work
Guo, Tao, and Hu introduced this exact sequence while proving the sharp negative-binomial mean-tail infimum. Their stronger intermediate statement is strict monotonicity,
\[
a_r(n+1)-a_r(n)>0,
\]
for every \(r>0\). The present result compares successive positive increments and proves they themselves decrease strictly.

Finner and Roters established extensive parameter log-concavity results for chi-square, \(F\), and beta distribution functions. Karp later gave analytic proofs and refinements for normalized incomplete beta functions. The relevant results in those works hold with the distribution-function argument fixed. Here the beta cutoff \(r/(r+N)\) moves with the second shape parameter; in the equivalent normalized \(F\) formulation, the threshold is fixed at \(1\) precisely because the normalization itself depends on \(N\). The inspected fixed-argument log-concavity statements therefore do not imply the ordinary discrete concavity proved here.

## Limitations
The theorem is a one-parameter curvature statement for the canonical local-minimum sequence and does not characterize all curvature properties of incomplete beta functions. No claim is made about higher finite differences, complete monotonicity, continuous interpolation in \(N\), or arbitrary negative-binomial tail thresholds. A residual literature risk is that an equivalent diminishing-increment statement may appear under older normalized-\(F\) power-function terminology; targeted searches did not locate one.

## References
1. Z.-Y. Guo, Z.-Y. Tao, and Z.-C. Hu, *A study on the negative binomial distribution motivated by Chvátal's theorem*, arXiv:2311.06877v1, 2023.
2. H. Finner and M. Roters, *Log-concavity and inequalities for Chi-square, F and Beta distributions with applications in multiple comparisons*, Statistica Sinica 7 (1997), 771-787.
3. D. Karp, *Normalized incomplete beta function: log-concavity in parameters and other properties*, arXiv:1509.05120, 2015.
