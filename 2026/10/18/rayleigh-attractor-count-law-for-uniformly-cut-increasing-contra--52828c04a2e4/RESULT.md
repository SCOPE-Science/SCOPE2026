# Rayleigh attractor-count law for uniformly cut increasing contractions

## Finding

A sharp deterministic upper bound of \(n\) attracting periodic orbits for an \(n\)-branch piecewise contraction contrasts with a much smaller typical count in a natural symmetric random-cut ensemble. Fix an integer \(n\ge2\), a slope \(\lambda\in(0,1)\), and the equally spaced branch fixed points \(u_i=i/(n+1)\), \(1\le i\le n\). Choose \(n-1\) independent uniform points of \((0,1)\) and order them into the partition \(0=c_0<c_1<\cdots<c_n=1\). On the branch \([c_{i-1},c_i)\), define

\[f(x)=\lambda x+(1-\lambda)u_i.\]

Let \(K_n\) be its number of distinct periodic orbits. With probability one, these are exactly its attracting fixed points and every orbit converges to one of them. Define the formal power series

\[G(z)=\sum_{a=1}^{\infty}\frac{a^a}{a!}z^a.\]

For every integer \(1\le k\le n\), the falling-factorial moment \((m)_k=m(m-1)\cdots(m-k+1)\) satisfies the **exact finite-size law**

\[\boxed{\mathbb E[(K_n)_k]=k!\frac{(n-1)!}{(n+1)^{n-1}}[z^{n+1}]G(z)^{k+1}.}\]

Let \(R\) have the standard Rayleigh density \(r\exp(-r^2/2)\) for \(r>0\). Then

\[\boxed{K_n/\sqrt n\Longrightarrow R,\quad \lim_{n\to\infty}\mathbb E[(K_n/\sqrt n)^k]=2^{k/2}\Gamma(1+k/2)}\]

for every fixed positive integer \(k\). In particular,

\[\boxed{\mathbb E K_n\sim\sqrt{\pi n/2},\qquad\operatorname{Var}(K_n)\sim(2-\pi/2)n.}\]

The largest possible count is exponentially rare:

\[\boxed{\Pr(K_n=n)=\frac{(n-1)!}{(n+1)^{n-1}}\sim\sqrt{2\pi n}\,e^{-n-1}.}\]

The law is **exactly independent of** \(\lambda\in(0,1)\).

## Assumptions and scope

The cuts are the increasing order statistics of \(n-1\) independent uniform random variables; the same distribution is uniform Lebesgue measure on the ordered-cut simplex. The maps act on \([0,1)\). Equalities between a cut and one of the finitely many branch fixed points are excluded from the almost-sure dynamical assertion; they have probability zero. The limit \(n\to\infty\) holds for an arbitrary fixed slope or for an arbitrary sequence of slopes \(\lambda_n\in(0,1)\), because the count distribution is slope-independent. No claim is made for arbitrary nonuniform fixed-point arrays or nonuniform cut distributions.

## Proof

**1. Dynamics reduce to fixed-point occupancy.** The map is strictly increasing on each branch, and at every cut the jump is positive, of size \((1-\lambda)/(n+1)\). Hence the whole discontinuous map is strictly increasing. If \(f(x)>x\), all later iterates increase; if \(f(x)<x\), all later iterates decrease. Iterates therefore have limits. An increasing map cannot possess a periodic orbit of least period greater than one. Off the finite zero-probability event that a cut equals a branch fixed point, a monotone orbit cannot converge to a cut: a limit from the left would require the left branch's limiting image to equal that cut, giving \(c_i=u_i\), while a limit from the right requires \(c_i=u_{i+1}\). Every limit is therefore an actual attracting fixed point.

The only candidate fixed point of the \(i\)-th branch is \(u_i\). It is a genuine attracting fixed point precisely if \(c_{i-1}<u_i<c_i\), apart from zero-probability endpoint coincidences. Let \(S_i\) count cuts strictly below \(i/(n+1)\). Then

\[K_n=\sum_{i=1}^{n}\mathbf1_{\{S_i=i-1\}}.\]

In particular \(K_n\ge1\): the integer path \(S_i-(i-1)\) starts nonnegative, ends nonpositive, and decreases by no more than one at a step, so it must visit zero.

**2. Exact joint occupancy and all factorial moments.** Write \(N=n+1\) and fix distinct indices \(1\le i_1<\cdots<i_k\le n\). Put \(a_0=i_1\), \(a_j=i_{j+1}-i_j\) for \(1\le j\le k-1\), and \(a_k=N-i_k\). All \(a_j\) are positive and sum to \(N\). The joint fixed-point event is exactly the event that the \(N-2=n-1\) independent cuts occupy these \(k+1\) consecutive blocks in amounts

\[a_0-1,\ a_1,\ldots,\ a_{k-1},\ a_k-1.\]

By the multinomial formula and the identity \(a^{a-1}/(a-1)!=a^a/a!\), its probability is

\[\boxed{\Pr(u_{i_1},\ldots,u_{i_k}\text{ all fixed})=\frac{(N-2)!}{N^{N-2}}\prod_{j=0}^{k}\frac{a_j^{a_j}}{a_j!}.}\]

There is a bijection between increasing index tuples and positive compositions \(a_0+\cdots+a_k=N\). Summing and multiplying by \(k!\) proves the coefficient formula for the falling-factorial moments. When \(k=n\), the only composition has all \(a_j=1\); this gives the exact maximum-count probability stated above, whose displayed asymptotic follows from Stirling's formula.

**3. Uniform simplex asymptotics.** Fix an arbitrary integer \(k\ge1\). For compositions \(\mathbf a\) with every \(a_j/N\) bounded away from zero, Stirling gives uniformly

\[\frac{(N-2)!}{N^{N-2}}\prod_{j=0}^k\frac{a_j^{a_j}}{a_j!}=\frac{N^{-k/2}}{(2\pi)^{k/2}}\prod_{j=0}^k(a_j/N)^{-1/2}\,(1+o(1)).\]

For all positive compositions, the elementary two-sided factorial bounds yield a constant \(C_k\), independent of \(N\), with

\[0\le \frac{(N-2)!}{N^{N-2}}\prod_{j=0}^k\frac{a_j^{a_j}}{a_j!}\le C_k\frac{\sqrt N}{\sqrt{a_0a_1\cdots a_k}}.\]

The singularities are integrable. Indeed, repeated use of \(\sum_{a=1}^{m-1}[a(m-a)]^{-1/2}\le C\) bounds the discrete Dirichlet convolution, while restricting any \(a_j\le\varepsilon N\) contributes only \(O_k(\sqrt\varepsilon)\) of the normalized sum. Thus the interior Riemann-sum limit extends to the full positive-composition simplex, and

\[\lim_{n\to\infty}\frac{\mathbb E[(K_n)_k]}{N^{k/2}}=\frac{k!}{(2\pi)^{k/2}}\int_{\substack{t_j>0\\\sum_{j=0}^k t_j=1}}\prod_{j=0}^k t_j^{-1/2}\,dt_0\cdots dt_{k-1}.\]

The Dirichlet beta integral evaluates to \(\Gamma(1/2)^{k+1}/\Gamma((k+1)/2)\), so by the gamma duplication identity

\[\lim_{n\to\infty}\frac{\mathbb E[(K_n)_k]}{N^{k/2}}=\frac{k!\sqrt\pi}{2^{k/2}\Gamma((k+1)/2)}=2^{k/2}\Gamma(1+k/2).\]

For fixed \(k\), expressing ordinary powers in falling factorials shows the same limits for ordinary moments. These are exactly the moments of the Rayleigh density. That distribution has a moment-generating function finite in a neighborhood of zero, so it is moment-determinate; moment convergence gives the claimed weak convergence and convergence of all fixed moments. Taking the first two limits yields the displayed mean and variance. Because \(N/n\to1\), the normalization can be stated using \(\sqrt n\).

## Verification

The standalone `verify.py` uses exact rational arithmetic. It enumerates every multinomial occupancy vector of the \(n-1\) cuts among \(n+1\) equal bins for all integers \(2\le n\le8\). For each vector, it independently counts fixed branches from the cumulative occupancies, weights the vector by its precise multinomial multiplicity, and compares every falling-factorial moment against the composition coefficient formula. It also checks the exact maximal-count probability. It prints `VERIFY_OK` when all checks pass. This exhaustive *finite-size* test is not the proof of the asymptotic statement; the uniform simplex argument above is its proof.

## Relationship to prior work

Nogueira and Pires (2012), Theorem 1.1 and Appendix A, establish the sharp deterministic \(n\)-orbit bound and discuss attractors of increasing piecewise contractions. Nogueira, Pires and Rosales (2013, 2014) establish generic asymptotic periodicity, in increasing generality, with at most \(n\) cycles. These are the qualitative starting points, and the deterministic bound is not claimed here as new. The new claim is the explicit random-partition ensemble, its full exact factorial-moment sequence, its Rayleigh attractor-count scaling, its nonvanishing normalized variance, and the exponentially small probability of saturating the bound.

Rayleigh distributions also arise classically from Brownian-bridge local time, as treated by Pitman (1998/1999). That continuum probabilistic connection is acknowledged, not claimed as original; the theorem is a direct finite combinatorial and dynamical derivation rather than a claimed discovery of the Rayleigh distribution itself.

## Limitations

The equally spaced fixed-point placement and uniform independent cuts are essential to the simple multinomial-composition law. For a nonuniform array, multinomial cells have unequal probabilities and this proof does not produce the stated Rayleigh constants. The theorem concerns the count of attracting fixed points, not the distribution of their basin sizes, their capture times, or fluctuations for random slopes with other branch orderings. A pre-existing general local-time invariance theorem might yield the limiting Rayleigh factor through an abstract reduction, though it does not by itself state the finite dynamical moment identities here. Historical priority is not asserted absolutely; independent assessment remains to be performed.

## References

1. A. Nogueira and B. Pires, *Dynamics of piecewise contractions of the interval*, arXiv:1206.5676v1 (first public 2012-06-25), especially Theorem 1.1 and Appendix A. https://arxiv.org/abs/1206.5676
2. A. Nogueira, B. Pires and R. A. Rosales, *Asymptotically periodic piecewise contractions of the interval*, arXiv:1310.5784v1 (first public 2013-10-22). https://arxiv.org/abs/1310.5784
3. A. Nogueira, B. Pires and R. A. Rosales, *Piecewise contractions defined by iterated function systems*, arXiv:1408.1663v1 (first public 2014-08-07), especially Theorems 1.1 and 5.1. https://arxiv.org/abs/1408.1663
4. J. Pitman, *The distribution of local times of a Brownian bridge*, Berkeley Technical Report 539 (1998-11-01), subsequently Séminaire de Probabilités XXXIII (1999). https://live-statistics.pantheon.berkeley.edu/tech-reports/539
