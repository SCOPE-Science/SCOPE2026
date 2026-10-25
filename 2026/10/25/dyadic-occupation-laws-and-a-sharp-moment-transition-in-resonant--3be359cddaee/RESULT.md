# Dyadic occupation laws and a sharp moment transition in resonant proportional-delay dynamics

## Finding
Fix any real parameter \(d\). Starting from \(x_0=1\), define the deterministic proportional-delay orbit
\[
 x_{n+1}=-x_n+d\,x_{\lfloor n/2\rfloor},\qquad n\ge0.
\]
The following assertions hold simultaneously for **every** \(d\in\mathbb R\), with no bound on the orbit imposed. This is an exact ergodic-average law for a singular observable of the \(2\)-adic adding machine, including its unbounded-observable moment boundary.

Put \(u_0=d-1\), \(u_{r+1}=d u_r-1\), and \(\nu_2(j)\) for the exponent of \(2\) in an integer \(j\ge1\). The exact solution is
\[
 x_{2k}=1,\qquad x_{2k+1}=u_{\nu_2(k+1)}\quad(k\ge0),
\]
where
\[
 u_r=\begin{cases}\displaystyle \frac{1+d^{r+1}(d-2)}{d-1},&d\ne1,\\ -r,&d=1.\end{cases}
\]
For \(N\ge1\) define the empirical probability measure \(\eta_N=N^{-1}\sum_{n=0}^{N-1}\delta_{x_n}\). Its **total-variation limit** is the explicit atomic probability measure
\[
 \eta_d=\frac12\delta_1+\sum_{r\ge0}\frac{1}{2^{r+2}}\delta_{u_r},\qquad
 \|\eta_N-\eta_d\|_{\mathrm{TV}}=O\!\left(\frac{1+\log N}{N}\right).
\]
The implied constant is universal (independent of \(d\)). Here \(\|\mu-\nu\|_{\mathrm{TV}}=\sup_B|\mu(B)-\nu(B)|\). In particular, even unbounded orbits have convergent occupation distributions in the strong total-variation topology.

The orbit is bounded precisely for \(d\in[-1,1)\cup\{2\}\). At \(d=1\) it is unbounded, but the limiting measure has moments of **every finite positive order**.

For \(|d|>1\) and \(d\ne2\), write
\[
 p_c=\frac{\log2}{\log|d|},\qquad C_d=\frac{d(d-2)}{d-1},\qquad M_p(N)=\frac1N\sum_{n=0}^{N-1}|x_n|^p\quad(p>0).
\]
Then the complete moment transition is
\[
 \begin{aligned}
 0<p<p_c&:\quad M_p(N)\longrightarrow\int|t|^p\,d\eta_d(t)<\infty,\\
 p=p_c&:\quad \lim_{N\to\infty}\frac{M_p(N)}{\log_2 N}=\frac{|C_d|^{p_c}}4,\\
 p>p_c&:\quad M_p(N)\longrightarrow+\infty.
 \end{aligned}
\]
The first convergence also holds for all \(p>0\) when \(d\in[-1,1]\cup\{2\}\). For \(|d|>1\), \(d\ne2\), the limiting atomic law therefore has a strict finite-moment threshold at \(p_c\), and a precise logarithmic divergence coefficient at equality. No infinite-time stochastic hypothesis is involved.

## Assumptions and scope
Let \(\mathbb Z_2\) be the compact additive group of \(2\)-adic integers, \(Tz=z+1\) its uniquely ergodic adding machine, and \(m_2\) its normalized Haar measure. The measurable observable \(g_d(z)=u_{\nu_2(z)}\) for \(z\ne0\) is assigned any value at the Haar-null exceptional point \(z=0\). Then \(x_{2k+1}=g_d(T^k1)\), and the limiting measure is exactly \(\eta_d=\tfrac12\delta_1+\tfrac12(g_d)_*m_2\). For parameters giving unbounded \(u_r\), \(g_d\) is an unbounded measurable observable, so ordinary bounded-continuous unique-ergodicity reasoning alone is insufficient for power moments.

The recurrence has real scalar data, dyadic floor delay, fixed instantaneous coefficient \(-1\), and normalized nonzero initial value \(x_0=1\). If \(x_0=a\), every value above is multiplied by \(a\); for \(a=0\) the orbit is identically zero. The only measure convergence asserted is that of empirical **state** distributions; no invariant measure for a time-homogeneous map is assumed. The total-variation rate is a bound, not an assertion of optimality.

## Proof
**1. Exact dyadic formula.** From the recurrence at adjacent indices,
\[
 x_{2k+1}=-x_{2k}+d x_k,\qquad x_{2k+2}=-x_{2k+1}+d x_k=x_{2k}.
\]
Induction gives \(x_{2k}=x_0=1\). With \(y_k=x_{2k+1}\), these identities give \(y_{2j}=d-1\) and \(y_{2j+1}=d y_j-1\). Since \(\nu_2(2j+2)=\nu_2(j+1)+1\), induction on the binary length of \(k+1\) shows \(y_k=u_{\nu_2(k+1)}\). Solving the first-order scalar recurrence for \(u_r\) gives the displayed formula, including its continuous parameter limit \(d=1\).

**2. Odometer representation and exact valuation counts.** Translation by one on \(\mathbb Z_2\) cycles through every residue modulo \(2^j\), proving unique ergodicity by cylinder approximation. Haar measure assigns mass \(2^{-(r+1)}\) to the clopen valuation stratum \(\{z:\nu_2(z)=r\}\). The odd orbit therefore samples \(g_d(T^k1)\), and the claimed Haar pushforward gives exactly its limiting atomic masses. The quantitative proof is an explicit arithmetic refinement, as follows.

**3. Exact total-variation estimate.** Let \(K=\lfloor N/2\rfloor\). Among \(k=0,\ldots,K-1\), the number for which \(\nu_2(k+1)=r\) is exactly
\[
 c_r(K)=\left\lfloor\frac K{2^r}\right\rfloor-\left\lfloor\frac K{2^{r+1}}\right\rfloor.
\]
Thus the exact empirical measure is
\[
 \eta_N=\frac{N-K}{N}\delta_1+\sum_{r\ge0}\frac{c_r(K)}N\delta_{u_r}.
\]
For fixed \(r\), \(c_r(K)/N\to2^{-(r+2)}\); the remaining limiting masses sum to \(1\). More quantitatively, \(|c_r(K)-K2^{-(r+1)}|\le1\). For \(r\le\lfloor\log_2 K\rfloor\) the total signed weight discrepancy is bounded by a constant times \((1+\log_2 N)/N\); beyond that level the empirical coefficients vanish and the geometric tail of the target measure is \(O(1/N)\). Summing absolute weights bounds total variation, even if distinct \(u_r\) happen to coincide. This proves the asserted uniform convergence rate.

**4. Boundedness.** For \(d\ne1\), write \(u_r=C_d d^r+(d-1)^{-1}\). If \(|d|\le1\) and \(d\ne1\), this is uniformly bounded. At \(d=2\), \(C_d=0\) and every \(u_r=1\). If \(|d|>1\) and \(d\ne2\), \(C_d\ne0\) and \(|u_r|\to\infty\). If \(d=1\), \(u_r=-r\) is unbounded. Every \(r\) occurs, for example at \(k=2^r-1\), so these are exactly the orbit-boundedness alternatives.

**5. Moment finiteness and empirical averages.** For \(|d|>1\), \(d\ne2\), the preceding closed form gives \(|u_r|\sim|C_d||d|^r\). Therefore
\[
 \int |t|^p\,d\eta_d(t)=\frac12+\sum_{r\ge0}2^{-(r+2)}|u_r|^p
\]
converges exactly when \(|d|^p<2\), equivalently \(p<p_c\). At \(d=1\) its summands are \(2^{-(r+2)}r^p\), which are summable for every \(p>0\). All other bounded-orbit cases also have finite moments.

To pass from limiting moments to empirical moments in the finite regime, substitute the exact \(c_r(K)\) formula. The coefficient error is at most \(O(1/N)\) at each \(r\le \lfloor\log_2 K\rfloor\); hence the total error is bounded by \(O(N^{-1}\sum_{r\le\log_2 N}|u_r|^p)\). This tends to zero if \(|d|^p<2\). At \(d=1\) it is \(O((\log N)^{p+1}/N)\); for bounded cases it is \(O(\log N/N)\). The limiting geometric tail tends to zero, proving convergence of finite moments. When \(p\ge p_c\), finite-level truncation and nonnegativity show \(\liminf M_p(N)\ge\frac12+\sum_{r=0}^R 2^{-(r+2)}|u_r|^p\) for every \(R\); the right side grows without bound with \(R\). Hence \(M_p(N)\to\infty\).

**6. Sharp critical coefficient.** Suppose \(|d|>1\), \(d\ne2\), and \(|d|^p=2\). Then \(2^{-r}|u_r|^p\to|C_d|^p\). The exact count formula and \(L=\lfloor\log_2 K\rfloor\) give
\[
 M_p(N)=\frac{N-K}{N}+\frac{K}{N}\sum_{r=0}^L 2^{-(r+1)}|u_r|^p+O(1),
\]
where the last \(O(1)\) follows from \(N^{-1}\sum_{r=0}^L|u_r|^p=O(2^L/N)=O(1)\). Cesàro averaging, \(K/N\to1/2\), and \(L/\log_2N\to1\) yield \(M_p(N)/\log_2N\to|C_d|^p/4\), as claimed.

## Verification
A standalone exact-arithmetic verifier checks the scalar recurrence against the valuation identity through 4,096 terms for nine rational parameters, including \(d=-3,-2,-1,0,1/2,1,3/2,2,3\). It also checks the exact valuation count formula, the special bounded cases and finite critical-moment slope samples. Computations illustrate the proof but do not replace its all-parameter argument. Execute with `python verify.py`.

## Relationship to prior work
Gade and Bhalekar (2026, arXiv:2610.21635v1, §§2.1–2.2 and Appendix) consider the same linear proportional-delay recurrence and study sufficient stability conditions and finite-horizon maximum/RMS tests. They do not state the dyadic resonant occupation measure, its total-variation convergence, or the parameter-dependent exact moment critical law. Their theorems do not imply these statistical conclusions: their delay-independent decay hypothesis is \(|\lambda|+|\delta|<1\), while the present instantaneous coefficient is \(\lambda=-1\). Their nonconvergence criteria also do not determine a time-sampling law.

Kundrát (2006, Theorem 3.1), a close earlier study of linear proportional-delay recurrences, assumes \(|1+A|<1\) in the scalar case. Under the identification \(\lambda=1+A\), this excludes the present resonant boundary. The historical homogeneous pantograph occupation-measure result concerns \(x_{n+1}=f(x_{\lfloor n/b\rfloor})\) with **no** instantaneous \(-x_n\) term and compact periodic underlying dynamics; it does not imply the unbounded resonant law here. Elementary density of dyadic valuations is classical and is not claimed as new.

## Limitations
This is an exact codimension-one parameter slice and a singular-observable result for one adding machine, not a classification of the full two-parameter stability diagram or of other delay ratios. The occupation measure need not describe growth of unbounded observables; its moment threshold is analyzed separately. The article's substantive novelty relative to earlier proportional-delay and arithmetic-sequence literature is assessed from inspected sources and targeted searches, not independently certified. No independent mathematical audit has been carried out.

## References
1. P. M. Gade and S. Bhalekar, *Pantograph Difference Equations: Stability, Multistability, and Chaos*, arXiv:2610.21635v1 (first public submission 2026-10-15), especially §§2.1–2.2 and the Appendix. https://arxiv.org/html/2610.21635v1
2. P. Kundrát, *On the asymptotics of the difference equation with a proportional delay*, Opuscula Math. **26** (2006), 499–506, especially Theorem 3.1. https://www.opuscula.agh.edu.pl/om-vol26iss3art11
3. H. Péics, *On the asymptotic behaviour of a pantograph-type difference equation*, J. Difference Equ. Appl. **6** (2000), 257–273, DOI:10.1080/10236190008808228 (bibliographic and abstract comparison only).
