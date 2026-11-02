# A sharp quadratic-memory resonance in the twisted baker map

## Finding

For the two-dimensional twisted baker map of Saiki, Takahasi and Yorke, normalized area measure gives an exact stationary correlation and central limit theorem for the centered squared radius. In square coordinates \(u=x\) and \(v=2y-1\), let
\[
q(u,v)=u^2+v^2-\frac23.
\]
For **every integer** \(k\geq0\),
\[
\operatorname{Cov}_m(q,q\circ F^k)=\frac8{45}\left(\frac58\right)^k.
\]
For **every integer** \(n\geq1\), the finite-time variance is
\[
\operatorname{Var}_m\!\left(\sum_{j=0}^{n-1}q\circ F^j\right)
=\frac{104}{135}n-\frac{128}{81}\left[1-\left(\frac58\right)^n\right].
\]
Furthermore,
\[
\frac1{\sqrt n}\sum_{j=0}^{n-1}q\circ F^j
\ \Longrightarrow\ \mathcal N\!\left(0,\frac{104}{135}\right).
\]
The rate \(5/8\) is the **sharp slowest exponential correlation rate on centered polynomials of total degree at most two**, while all centered affine observables have correlations bounded at the strictly faster rate \((1/2)^k\). In particular a natural quadratic energy remembers the past longer than any affine measurement in this system.

## Assumptions and scope

The phase space is \(X=[-1,1]\times[0,1]\), endowed with normalized Lebesgue probability \(m\) (density \(1/2\) with respect to area). The fixed, nonrandom, two-branch map is
\[
F(x,y)=\begin{cases}
(1+2x,y),&x<0,\\
(1-2y,x),&x\geq0.
\end{cases}
\]
The horizontal divider and all of its inverse images are null and therefore do not affect stationary assertions. In centered square coordinates \((u,v)=(x,2y-1)\), the same map is
\[
F(u,v)=\begin{cases}
(1+2u,v),&u<0,\\
(-v,2u-1),&u\geq0.
\end{cases}
\]
Here \((u,v)\) are independent uniforms on \([-1,1]\). The correlation bound on degree-two polynomials is for each fixed pair of centered real polynomials, with its own finite multiplicative constant, under the same invariant probability. No claim is made about rates for general observables or about higher-dimensional maps.

## Proof

**1. Transfer operator and its quadratic eigenfunction.** Every point of the centered square has two inverse branch images, each with Jacobian magnitude \(2\). The Perron--Frobenius operator on integrable functions is therefore
\[
(\mathcal P f)(u,v)=\tfrac12f\!\left(\tfrac{u-1}2,v\right)
+\tfrac12f\!\left(\tfrac{v+1}2,-u\right).
\]
It satisfies \(\mathcal P1=1\), proving stationarity. Its action on the centered coordinate functions and squared radius is
\[
\mathcal Pu=\tfrac14(u+v),\qquad
\mathcal Pv=\tfrac12(v-u),\qquad
\mathcal Pq=\tfrac58q-\tfrac14u+\tfrac14v.
\]
Consequently
\[
e=q-\tfrac{10}{11}u+\tfrac2{11}v
\quad\text{satisfies}\quad
\mathcal Pe=\tfrac58e.
\]
Because uniform area on the centered square makes \(q\) orthogonal to both \(u\) and \(v\),
\[
\int q^2\,dm=\tfrac8{45},\qquad
\int qu\,dm=\int qv\,dm=0.
\]
Writing \(q=e+10u/11-2v/11\), invariance of the affine subspace under \(\mathcal P\) gives, for all \(k\geq0\),
\[
\int q\,(q\circ F^k)\,dm
=\int q\,\mathcal P^kq\,dm
=\left(\tfrac58\right)^k\!\int qe\,dm
=\tfrac8{45}\left(\tfrac58\right)^k.
\]
These are covariances since \(\int q\,dm=0\).

**2. Sharp contrast with linear observables.** On \(\operatorname{span}\{u,v\}\), the transfer operator has characteristic polynomial \(\lambda^2-\tfrac34\lambda+\tfrac14\), whose roots are \((3\pm i\sqrt7)/8\), both of modulus \(1/2\). On the entire real polynomial space of total degree at most two, the transfer characteristic polynomial is
\[
(\lambda-1)\lambda^2(\lambda-\tfrac58)
\left(\lambda^2-\tfrac34\lambda+\tfrac14\right).
\]
Thus every centered pair of degree-two polynomial observables has correlation \(O((5/8)^k)\); the exhibited \(q\) makes this exponent optimal. Every pair of centered affine observables has correlation \(O((1/2)^k)\), proving the strict two-scale distinction.

**3. Exact finite-time fluctuations.** Stationarity and the correlation formula yield
\[
\operatorname{Var}\left(\sum_{j=0}^{n-1}q\circ F^j\right)
=\frac8{45}\left[n+2\sum_{k=1}^{n-1}(n-k)\left(\frac58\right)^k\right].
\]
Summing the finite geometric series yields the stated identity, including the constant \(-128/81\) and exponential remainder. The limiting variance per iterate is \(104/135\), strictly positive.

**4. Central limit theorem without an unproved spectral assumption.** Define the bounded polynomial
\[
h=\frac53q-\frac43u+\frac23v.
\]
Direct substitution into the explicit transfer operator gives
\[
(I-\mathcal P)h=\mathcal Pq.
\]
Therefore \(d=q+h-h\circ F\) obeys \(\mathcal Pd=0\). On the left and right half-squares respectively, its explicit formulas are
\[
d_L=-\frac{12u^2+16u-3v^2+3}{3},\qquad
 d_R=-\frac{12u^2-12u-3v^2+2v+5}{3}.
\]
Integration over the two half-squares with uniform probability density \(1/4\) gives
\[
\int d^2\,dm=\frac{104}{135}.
\]
The original map with \(m\) is Bernoulli, hence ergodic, by the measure-theoretic isomorphism established in Saiki--Takahasi--Yorke, Section 3.3. The identity \(\mathcal Pd=0\) makes \(d\circ F^j\) a stationary reverse martingale-difference sequence for the decreasing image filtration. The bounded stationary ergodic martingale central limit theorem applies, with variance \(\int d^2dm\). Finally
\[
\sum_{j=0}^{n-1}q\circ F^j
=\sum_{j=0}^{n-1}d\circ F^j+h\circ F^n-h,
\]
and the last two terms are uniformly bounded in \(n\). Slutsky's lemma gives the asserted Gaussian limit.

## Verification

The standalone program `verification/check_energy.py` uses SymPy exact rational arithmetic. It reconstructs \(\mathcal P\) from the two inverse branches, checks its complete degree-two characteristic polynomial and the eigenfunction, verifies 25 consecutive exact correlations, 29 exact finite variances, the bounded martingale-coboundary equation, and the exact \(L^2\)-norm of \(d\). It executes without simulated or probabilistic certificates. These finite checks confirm algebraic identities; the preceding argument establishes the quantified infinite conclusions.

Run with `python verification/check_energy.py` in an environment with Python 3 and SymPy.

## Relationship to prior work

Saiki, Takahasi and Yorke introduced this twisted baker map and established its Lebesgue invariance, Bernoulli coding, periodic-point spectral properties, mixing, and equidistribution. Those results supply the dynamical setting and ergodicity, but do not state this polynomial transfer spectrum, exact squared-radius autocovariance, finite-time fluctuation formula, or Gaussian variance. Existing calculations of autocorrelations of **linear coordinates** for this map do not imply the new quadratic eigenvalue \(5/8\): the affine transfer subspace has spectral radius only \(1/2\). Existing periodic-Jacobian spectral calculations concern a different linear operator. The martingale-coboundary principle is classical (Gordin), and no general central limit theorem is claimed as novel; the contribution is the exact energy-specific computation and strict quadratic-versus-affine memory contrast.

## Limitations

Only the two-dimensional version and its normalized stationary area measure are treated. The exact rate \(5/8\) is sharp on the bounded-degree polynomial subspace, not a claimed global mixing rate for arbitrary observables. A Gaussian central limit theorem does not imply finite-sample Gaussianity, independence of observations, or a Berry--Esseen bound. Prior publication of the same exact quadratic computation in an unindexed source is a residual priority risk. Independent external validation has not been performed.

## References

1. Y. Saiki, H. Takahasi and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304 (first submitted February 9, 2022), especially definition in Section 1 and Bernoulli proof in Section 3.3; DOI: 10.1088/1361-6544/acb4d3. https://arxiv.org/abs/2202.04304
2. M. I. Gordin, *The central limit theorem for stationary processes*, Doklady Akademii Nauk SSSR **188** (1969), 739–741; classical martingale-approximation principle. See also G. K. Eagleson, *On Gordin's central limit theorem for stationary processes*, Journal of Applied Probability **12** (1975), 176–179, DOI: 10.2307/3212425.
