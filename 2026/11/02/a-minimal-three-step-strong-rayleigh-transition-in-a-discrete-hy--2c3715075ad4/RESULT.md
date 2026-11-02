# A minimal three-step strong-Rayleigh transition in a discrete hyperbolic staircase

## Finding

Let \(0<p\leq1\). Consider the descending Markov chain started at \(X_0=1\): from \(X_{j-1}=x\), with probability \(px\) replace \(x\) by a uniform point of \((0,x)\), and otherwise keep \(x\). Write \(I_j=\mathbf 1\{X_j<X_{j-1}\}\) and \(N_n=\sum_{j=1}^n I_j\). The following jointly characterize an unusual separation between count-level and time-indexed negative dependence.

**Theorem.** For every \(0<p<1\), all distinct jump indicators are strictly negatively correlated. For every \(n\geq1\), the law of \(N_n\) is that of a sum of \(n\) independent, generally nonidentical Bernoulli variables, despite the dependence of the actual indicators. The latter count-level fact follows by a Meixner-polynomial transformation of an earlier generating-function formula and is not asserted as independently new.

For the *ordered three-time indicator vector* \((I_1,I_2,I_3)\), the exact strong-Rayleigh classification is

\[
\boxed{\text{strongly Rayleigh}\ \Longleftrightarrow\ 0<p\leq 2\sqrt6-4\quad\text{or}\quad p=1.}
\]

Here strongly Rayleigh means that the multiaffine probability-generating polynomial has no zero when all three variables lie in the open upper complex half-plane. The threshold is \(2\sqrt6-4=0.898979485566\ldots\). Thus there is a sharp interior breakdown of strong Rayleigh despite strict pairwise negative correlations and a Poisson-binomial total, followed by restoration of independence at \(p=1\). A vector of only two Bernoulli indicators cannot exhibit this discrepancy, making three time steps the minimum horizon.

## Assumptions and scope

All uniform draws, activation coins, and transitions are independent conditional on the current state as specified. The parameter satisfies \(0<p\leq1\), the initial condition is \(X_0=1\), and all statements concern discrete times. The exact strong-Rayleigh classification is only for the first three jump indicators; no assertion about full higher-dimensional real stability is made. The count-level statement holds for every finite \(n\geq1\); strict pairwise covariance holds for every \(1\leq i<j\) and \(0<p<1\). At \(p=1\) the record indicators are independent, with the first indicator identically one.

For a polynomial \(F\), set \(\Delta_{ij}F=(\partial_iF)(\partial_jF)-F\partial_i\partial_jF\). We use the standard characterization: a real multiaffine polynomial is stable precisely when \(\Delta_{ij}F\geq0\) for every pair and every real evaluation of its variables [2,3].

## Proof

**1. Exact record-minimum coupling.** Let \(B_j\) be independent Bernoulli variables of success probability \(p\), and \(U_j\) independent uniform variables on \((0,1)\). Set \(W_j=U_j\) if \(B_j=1\), and \(W_j=1\) otherwise. Then

\[
X_j=\min(1,W_1,\ldots,W_j),\qquad
I_j=\mathbf 1\{W_j<X_{j-1}\}.
\]

Indeed, conditional on \(X_{j-1}=x\), the chance that \(B_j=1\) and \(U_j<x\) is \(px\); conditional on that event, \(U_j\) is uniform on \((0,x)\). This constructs exactly the specified Markov kernel. Conditional on the indices \(a_1<\cdots<a_k\) for which \(B_j=1\), the relative ranks of the \(k\) uniforms are uniform; their strict lower-record indicators are independent Bernoulli variables with success probabilities \(1,1/2,\ldots,1/k\) [classical record-ranking argument]. Hence their conditional joint generating polynomial is

\[
\prod_{r=1}^k\frac{z_{a_r}+r-1}{r}.
\]

**2. Strict covariance sign.** For \(0<t<1\), the coupling gives \(\Pr(X_i>t)=(1-pt)^i\). In addition,

\[
\Pr(I_i=1,X_i>t)=p\int_t^1(1-pu)^{i-1}\,du
=\frac{(1-pt)^i-(1-p)^i}{i}.
\]

Thus \(\Pr(I_i=1)=[1-(1-p)^i]/i\), and for \(0<p<1\) the conditional tail \(\Pr(X_i>t\mid I_i=1)\) is strictly below \(\Pr(X_i>t)\) for every \(0<t<1\). For \(j>i\), conditional on \(X_i=x\), the probability of a jump at \(j\) is

\[
h_{i,j}(x)=p\int_0^x(1-pu)^{j-i-1}\,du,
\]

which is strictly increasing in \(x\). Strict stochastic comparison therefore yields \(\Pr(I_j=1\mid I_i=1)<\Pr(I_j=1)\), proving \(\operatorname{Cov}(I_i,I_j)<0\). At \(p=1\), the conditional tails coincide and the standard continuous-record rank indicators are independent.

**3. The total count has a Poisson-binomial distribution.** The count generating polynomial computed in [1, Theorem 3] is

\[
P_n(z)=\mathbb E[z^{N_n}]
=\sum_{j=0}^n\binom nj\binom{z-1}{j}p^j.
\]

Put \(c=1-p\in(0,1)\), and define

\[
M_n(x;c)=\sum_{j=0}^n\binom nj\binom xj(1-c^{-1})^j.
\]

The generating functions satisfy

\[
\sum_{n\geq0}P_n(z)t^n=(1-t)^{-z}(1-ct)^{z-1},
\qquad
\sum_{n\geq0}M_n(x;c)t^n=\frac{(1-t/c)^x}{(1-t)^{x+1}}.
\]

Consequently \(P_n(z)=c^n M_n(-z;c)\). For completeness, a direct multiplication and summation of the second generating function against the positive geometric weight \((1-c)c^x\), \(x=0,1,\ldots\), gives

\[
\sum_{x=0}^\infty (1-c)c^x
\left(\sum_{m\geq0}M_m(x;c)s^m\right)
\left(\sum_{n\geq0}M_n(x;c)t^n\right)
=\frac1{1-st/c}.
\]

Coefficient comparison yields orthogonality
\(\sum_x(1-c)c^xM_m(x;c)M_n(x;c)=c^{-n}\mathbf1\{m=n\}\). Because this is a strictly positive measure with infinite support on the nonnegative integers, the degree-\(n\) orthogonal polynomial has \(n\) simple roots in \((0,\infty)\). Accordingly all roots of \(P_n\) are strictly negative. Since \(P_n(1)=1\), its factorization is

\[
P_n(z)=\prod_{r=1}^n\left(1-q_r+q_rz\right),
\qquad 0<q_r<1,
\]

which is a sum-of-independent-Bernoullis law. At \(p=1\), the well-known record formula gives \(P_n(z)=\prod_{r=1}^n(z+r-1)/r\). The classical Meixner orthogonality itself is also recorded in [4].

**4. Exact three-step stability threshold.** The record-minimum coupling gives the multivariate polynomial

\[
F_p(z_1,z_2,z_3)=\sum_{A=\{a_1<\cdots<a_k\}\subseteq\{1,2,3\}}
 p^k(1-p)^{3-k}\prod_{r=1}^k\frac{z_{a_r}+r-1}{r}.
\]

For \(0<p<1\), direct differentiation and completion of squares give, for the three distinct pairs,

\[
\Delta_{ij}F_p
=\frac{p^2(1-p)}{12}\left[p^2(z_k-b_{ij})^2+
\frac{8-8p-p^2}{4}\right],
\]

where \(\{i,j,k\}=\{1,2,3\}\) and

\[
b_{12}=\frac12-\frac2p,
\qquad b_{13}=\frac32-\frac2p,
\qquad b_{23}=\frac52-\frac2p.
\]

The three Rayleigh differences are nonnegative for every real evaluation if and only if \(8-8p-p^2\geq0\). In the open parameter interval this is precisely \(p\leq2\sqrt6-4\). If \(2\sqrt6-4<p<1\), choosing the unused variable to equal its displayed \(b_{ij}\) makes a Rayleigh difference strictly negative, and stability fails. At \(p=1\), the indicators are independent and their polynomial \(z_1(1+z_2)(2+z_3)/6\) is stable. Two-time Bernoulli laws are stable whenever their covariance is nonpositive, proving horizon minimality.

## Verification

The standalone file `check.py` reconstructs \(F_p\) independently by conditioning on activation sets; symbolically verifies all three completed-square identities; evaluates both sides of the phase boundary using exact rational parameters; compares the count-generating polynomial with both its activation representation and its Meixner transformation for dimensions one through nine; verifies the algebraic orthogonality generating kernel; and checks strict rational pairwise covariances for 75 index/parameter configurations. It completed 120 checks, recorded in `check_output.txt`. These are finite symbolic and numerical consistency checks; the preceding analytical argument proves the statements for all claimed indices and parameters.

To replay with SymPy installed: `python check.py`.

## Relationship to prior work

Yoshida [1] established the underlying chain's marginal laws, joint survival probabilities, and the univariate jump-count generating function. The present count factorization is a classical Meixner consequence of that earlier formula and is used as a *contrast*, not as the core priority claim. Meixner orthogonality is classical [4]. Strong Rayleigh and the all-real Rayleigh-difference criterion originate in [2,3]. The assessed model-specific contribution is the sharp minimal-horizon failure/restoration interval and its coexistence with strict pairwise negative correlation and Poisson-binomial count statistics.

The inspected material in [1] (the complete publicly available HTML text, including its probability, count, and martingale sections) does not state this three-indicator phase transition. The cited general theory [2–4] does not by itself give its model-specific threshold without an additional exact generating-polynomial computation. This is a best-knowledge comparison, not a guarantee of historical priority; earlier results on record processes with atoms could contain an equivalent implicit formulation.

## Limitations

The exact phase boundary concerns only the first three jump indicators; no claim is made about multivariate stability at times four or later. Poisson-binomial representation concerns the marginal distribution of \(N_n\), not independence of the original indicators. The proof uses a previously established general stability criterion and classical orthogonal-polynomial theory, with a separate direct orthogonality calculation included. Potential priority overlap with general atom-bearing record-process theory remains unresolved without a more exhaustive specialist review. No independent external mathematical audit has been performed.

## References

1. Naohiro Yoshida, *Poisson Hyperbolic Staircase in Discrete Time*, arXiv:2604.22637, first posted 2026-04-24. https://arxiv.org/abs/2604.22637
2. Petter Brändén, *Polynomials with the half-plane property and matroid theory*, Advances in Mathematics 216 (2007), 302–320; arXiv:math/0605678. https://arxiv.org/abs/math/0605678
3. Julius Borcea, Petter Brändén and Thomas M. Liggett, *Negative dependence and the geometry of polynomials*, Journal of the American Mathematical Society 22 (2009), 521–567; arXiv:0707.2340. https://arxiv.org/abs/0707.2340
4. Mourad E. H. Ismail and Walter Van Assche (eds.), *Encyclopedia of Special Functions: The Askey–Bateman Project*, Chapter 6, *Discrete Orthogonal Polynomials* (2020). https://doi.org/10.1017/9780511979156.007
