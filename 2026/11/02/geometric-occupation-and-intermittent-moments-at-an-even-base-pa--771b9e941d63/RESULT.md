# Geometric occupation and intermittent moments at an even-base pantograph flip resonance

## Finding

Fix an even integer \(m\geq2\), a starting value \(c\in\mathbb R\), and a continuous map \(G:\mathbb R\to\mathbb R\). Define the discrete proportional-delay orbit by
\[
x_0=c,\qquad x_{n+1}=-x_n+G\!\left(x_{\lfloor n/m\rfloor}\right),\qquad n\geq0.
\]
Write \(t_m(n)\) for the number of consecutive **odd** base-\(m\) digits at the least-significant end of the nonnegative integer \(n\), with implicit leading zero digits, and let \(Q_c(u)=G(u)-c\). Then, for every \(n\geq0\),
\[
\boxed{x_n=Q_c^{\,t_m(n)}(c).}
\]
The empirical probability measures \(\nu_N=N^{-1}\sum_{n=0}^{N-1}\delta_{x_n}\) converge **in total variation**, even if the orbit of \(Q_c\) is unbounded, to the geometric orbit law
\[
\boxed{\nu_N\xrightarrow[N\to\infty]{\rm TV}\mu_c:=\sum_{r=0}^{\infty}2^{-r-1}\delta_{Q_c^r(c)}.}
\]
For every integer \(K\geq1\), the finite-sample identity is exact:
\[
\boxed{\nu_{m^K}=\sum_{r=0}^{K-1}2^{-r-1}\delta_{Q_c^r(c)}+2^{-K}\delta_{Q_c^K(c)},\qquad
\|\nu_{m^K}-\mu_c\|_{\rm TV}\leq2^{-K-1}.}
\]
Here \(\|\nu-\mu\|_{\rm TV}=\sup_B|\nu(B)-\mu(B)|\).

In the linear specialization \(G(u)=\delta u\), with \(\delta\in\mathbb R\) and \(c\ne0\), the entire orbit is bounded **if and only if** \(\delta\in[-1,1)\cup\{2\}\); in no case does it converge to zero because \(x_{mk}=c\) for all \(k\geq0\). For each \(p>0\), the time-averaged absolute \(p\)-moment
\[
M_p(N)=\frac1N\sum_{n=0}^{N-1}|x_n|^p
\]
converges to a finite number **if and only if** \(|\delta|^p<2\) or \(\delta=2\); otherwise \(M_p(N)\to+\infty\). More sharply, for \(\delta\ne1,2\) define
\[
\rho=\frac{|\delta|^p}{2},\qquad B=\left|c\frac{\delta-2}{\delta-1}\right|^p.
\]
At \(\rho=1\), \(M_p(m^K)\sim BK/2\); at \(\rho>1\),
\[
\boxed{M_p(m^K)\sim B\left(1+\frac1{2(\rho-1)}\right)\rho^K.}
\]
Thus unbounded pointwise excursions can coexist with a total-variation limit of the unweighted empirical measures; a precise geometric-tail threshold governs which time moments survive.

## Assumptions and scope

The delay is the integer-valued rule \(h(n)=\lfloor n/m\rfloor\) with **even** integer \(m\geq2\). The instantaneous coefficient is exactly \(-1\). The starting value \(c\) is arbitrary in the nonlinear part. The function \(G\) is real-valued on the whole line, ensuring all iterates exist; continuity is natural for discrete dynamics but is not needed by the combinatorial proof. The moment and boundedness classifications concern scalar linear feedback \(G(u)=\delta u\), nonzero \(c\), and arbitrary real \(\delta\). Powers of a real absolute value use \(p>0\).

## Proof

**Block cancellation.** For any block index \(k\geq0\), the delay index is constant, \(\lfloor (mk+j)/m\rfloor=k\), for \(j=0,\ldots,m-1\). If \(x_{mk}=c\), the recurrence alternates exactly between \(c\) at even internal positions and \(G(x_k)-c\) at odd internal positions. Because \(m\) is even, the end of the block is again \(c\). Starting with \(x_0=c\), induction gives \(x_{mk}=c\) for every \(k\), and
\[
x_{mk+j}=\begin{cases}c,&j\text{ even},\\Q_c(x_k),&j\text{ odd}.\end{cases}
\]
Applying this identity recursively to base-\(m\) digits removes one least-significant odd digit at each step, stopping at the first even digit. This proves the exact digit representation for every integer index.

**Exact digit frequencies.** Among the integers in \([0,m^K)\), the number with exactly \(r<K\) trailing odd digits is
\[
(m/2)^r(m/2)m^{K-r-1}=m^K/2^{r+1}.
\]
There are exactly \((m/2)^K=m^K/2^K\) integers with at least \(K\) such digits; their implicit next digit is zero, so their tail length is exactly \(K\). Pushing forward this histogram under \(r\mapsto Q_c^r(c)\) yields the asserted finite-sample formula. Its difference from the infinite geometric measure is an excess mass \(2^{-K-1}\) at \(Q_c^K(c)\), compensated by the entire tail beyond \(K\), giving the total-variation bound.

For arbitrary \(N\to\infty\), the residue classes specifying \(t_m(n)=r\) are periodic modulo \(m^{r+1}\), with density \(2^{-r-1}\). Similarly \(t_m(n)\geq R\) is periodic modulo \(m^R\), with density \(2^{-R}\). Fixing \(R\), the first \(R\) frequencies converge and the combined omitted probability mass has limsup at most \(2^{-R}\). Letting \(R\to\infty\) proves convergence in \(\ell^1\) of the digit-tail distributions, hence in total variation of their pushforwards, regardless of how rapidly \(Q_c^r(c)\) grows.

**Linear orbit and boundedness.** When \(G(u)=\delta u\), the internal orbit is \(a_0=c\), \(a_{r+1}=-c+\delta a_r\), so
\[
a_r=\begin{cases}c(1-r),&\delta=1,\\c\dfrac{(\delta-2)\delta^r+1}{\delta-1},&\delta\ne1.\end{cases}
\]
All nonnegative tail lengths occur (at indices whose first \(r\) base-\(m\) digits are odd). If \(|\delta|\leq1\), the orbit \((a_r)\) is bounded except at \(\delta=1\), where it grows linearly in \(r\). If \(|\delta|>1\), it is unbounded except at \(\delta=2\), where \(a_r=c\) for all \(r\). This proves the exact boundedness set. Each subsequence \((x_{mk})\) remains \(c\ne0\).

**Moment transition.** Exact digit counting gives
\[
M_p(m^K)=\sum_{r=0}^{K-1}2^{-r-1}|a_r|^p+2^{-K}|a_K|^p.
\]
For \(\delta\ne1,2\) and \(|\delta|>1\), \(|a_r|^p\sim B|\delta|^{pr}\), with \(B>0\). Comparison with the geometric series of ratio \(\rho=|\delta|^p/2\) proves finite moments for \(\rho<1\), linear divergence with coefficient \(B/2\) when \(\rho=1\), and the stated exponential-in-\(K\) asymptotic when \(\rho>1\); the final term contributes \(B\rho^K\), while the partial geometric sum contributes \(B\rho^K/[2(\rho-1)]\). At \(\delta=1\), \(|a_r|^p=|c|^p|1-r|^p\) is geometrically summable; at \(\delta=2\), \(a_r=c\), so all moments are finite. Cases \(|\delta|\leq1\) are covered by these statements.

For general \(N\), choose \(K\) with \(m^K\leq N<m^{K+1}\). Every nonnegative summand gives \(M_p(N)\geq m^{-1}M_p(m^K)\), proving full-time divergence in the supercritical and critical cases. In the subcritical case, the tail of the weighted moment beyond digit depth \(R\), divided by \(N\), is bounded by \(m\) times the corresponding tail of the explicit \(m^{K+1}\)-block formula, uniformly as \(N\to\infty\). Since the infinite geometric moment series converges, these tails vanish as \(R\to\infty\). Truncating at fixed depth and passing to the limit yields \(M_p(N)\to\sum_{r\geq0}2^{-r-1}|a_r|^p\). All asserted cases follow.

## Verification

The standalone standard-library checker `verify_digit_flip.py` directly iterates the defining recurrence for even bases \(2,4,6\), compares every position to the digit formula for a nonlinear polynomial feedback, checks exact digit counts, and checks rational affine orbit formulas and second moments for eight distinct rational values of \(\delta\). It prints `ALL_EXACT_FINITE_CHECKS_PASS` if all checks succeed. These finite checks corroborate, but do not replace, the all-index combinatorial proof or infinite moment argument.

## Relationship to prior work

Gade and Bhalekar (arXiv:2610.21635v1, publicly posted October 15, 2026) study \(x_{n+1}=\lambda x_n+\delta x_{\lfloor an\rfloor}\), give stability/instability regions, explicitly leave parameter-dependent regions unresolved, and discuss nonlinear purely delayed composition plateaus. The present result concerns their previously unclassified critical coefficient \(\lambda=-1\) at reciprocal even-integer delays, and proves exact physical-time frequencies and moment thresholds rather than finite-horizon classifications. The digit-sampling law applies to nonlinear feedback \(G\), where the undelayed current-state term does not vanish.

Kundrát's 2006 proportional-delay bounds assume that the instantaneous multiplier has modulus strictly less than one, hence do not apply at \(\lambda=-1\). Péics (2000) treats asymptotic bounds for pantograph-type differences; its publicly accessible abstract does not resolve the present exact flip-resonant digit and moment law. Known geometric weighting in purely delayed recurrences has no direct implication for the current-state flip equation: the exact even-block cancellation is an additional mechanism.

## Limitations

No conclusion is claimed for non-even integer reciprocal delays, nonreciprocal delays, instantaneous coefficients other than \(-1\), or arbitrary multi-component equations. The limiting occupation measure need not be invariant under \(G\) or \(Q_c\); it is a physical-time sampling law. Convergence of bounded test-function averages does not imply convergence of unbounded moments. Historical priority remains subject to comparison with the broader literature on digital sequences and pantograph dynamics. No independent mathematical audit has been performed.

## References

- P. M. Gade and S. Bhalekar, *Pantograph Difference Equations: Stability, Multistability, and Chaos*, arXiv:2610.21635v1, October 15, 2026, https://arxiv.org/html/2610.21635.
- P. Kundrát, *On the asymptotics of the difference equation with a proportional delay*, Opuscula Mathematica 26(3) (2006), 499–506, https://www.opuscula.agh.edu.pl/om-vol26iss3art11.
- H. Péics, *On the asymptotic behaviour of a pantograph-type difference equation*, Journal of Difference Equations and Applications 6(3) (2000), 257–273, DOI:10.1080/10236190008808228.
