# A covariance sign transition for empirical fixed-point states in Ewens restaurant growth

## Finding
Fix \(\theta>0\) and run the Ewens Chinese restaurant permutation growth process. Let \(F_j\) be the number of singleton cycles (fixed points) after \(j\) insertions. For each nonnegative integer \(c\), write
\[
Q_{n,c}=\frac1n\sum_{j=1}^n{\bf1}\{F_j=c\}.
\]
For every fixed finite set of states, the associated empirical fractions converge jointly in distribution to
\[
W_c=\int_0^\infty e^{-t}{\bf1}\{X_\theta(t)=c\}\,dt,
\]
where \(X_\theta\) is a stationary immigration–death process with immigration rate \(\theta\), unit per-individual death rate, and Poisson\((\theta)\) stationary law. This weak convergence follows from the logarithmic-time process limit of Gnedin and Stark (2022); it is stated to identify the variables whose new covariance phase diagram is obtained below.

For each integer \(d\ge1\), the limiting covariance is exactly
\[
\lim_{n\to\infty}\operatorname{Cov}(Q_{n,0},Q_{n,d})
=\frac{e^{-2\theta}\theta^d}{d!}\left[\int_0^1 e^{\theta u}(1-u)^d\,du-1\right]. \tag{1}
\]
There is a *unique* positive \(\theta_d\) satisfying
\[
\int_0^1e^{\theta_d u}(1-u)^d\,du=1. \tag{2}
\]
The covariance in (1) is strictly negative for \(0<\theta<\theta_d\), zero for \(\theta=\theta_d\), and strictly positive for \(\theta>\theta_d\). The critical values strictly increase with \(d\) and satisfy the sharp first-order displacement law
\[
\boxed{\theta_d=d+(1+o(1))\sqrt{d\log d}},\qquad d\longrightarrow\infty. \tag{3}
\]
In particular, \(\theta_1=1.7932821329\ldots\), \(\theta_2=3.3836342829\ldots\). The initial-state exclusion of the two indicators therefore does not prevent *positive* covariance of their empirical occupation fractions.

## Assumptions and scope
At stage \(j\ge1\), a newly arriving element forms a singleton cycle with probability \(\theta/(\theta+j)\); otherwise it is inserted uniformly into one of the \(j\) existing cycle positions. Consequently, conditionally on \(F_j=k\), the next value is \(k+1\), \(k-1\), or \(k\), respectively, with probabilities \(\theta/(\theta+j)\), \(k/(\theta+j)\), and \((j-k)/(\theta+j)\). The initial state is \(F_1=1\). Fix \(\theta>0\) before taking \(n\to\infty\); fix \(d\) before taking that limit. The further limit \(d\to\infty\) is applied only to the mathematically defined critical parameters \(\theta_d\), not simultaneously to the original permutation process.

## Proof
**1. Weak occupation limit.** For any fixed \(\varepsilon\in(0,1)\), set \(Y_n(t)=F_{\lfloor ne^t\rfloor}\) on \([\log\varepsilon,0]\). The transition probabilities displayed above, viewed on the logarithmic clock, converge uniformly on compact state sets to those of the continuous-time birth–death generator
\[
\mathcal L f(k)=\theta[f(k+1)-f(k)]+k[f(k-1)-f(k)].
\]
The Ewens fixed-point marginal converges to Poisson\((\theta)\); compact-time tightness follows from bounded jump rates on a high-probability finite state set. Equivalently, the asserted finite-window Skorokhod convergence is the singleton specialization of Theorem 6 in Gnedin and Stark's *Random Permutations and Queues*. Its limit \(X_\theta\) is stationary on the logarithmic clock. Almost surely a sample path of this chain has finitely many jumps on a compact interval, so weighted integration of the state indicators is continuous at almost every limiting path. Therefore
\[
\frac1n\sum_{j=\lceil\varepsilon n\rceil}^{n}{\bf1}\{F_j=c\}
\ \Longrightarrow\ \int_{\varepsilon}^{1}{\bf1}\{X_\theta(\log u)=c\}\,du.
\]
Both the omitted discrete and continuous initial pieces have magnitude at most \(\varepsilon+1/n\). Let \(\varepsilon\downarrow0\) for joint convergence of any finite collection of states. Reversibility of the stationary immigration–death chain permits time reversal, and the substitution \(u=e^{-t}\) yields the displayed \(W_c\) representation. All empirical fractions and their limits lie in \([0,1]\), hence convergence of individual expectations and joint products accompanies weak convergence.

**2. Exact covariance.** The chain is reversible since its Poisson stationary masses \(\pi_k=e^{-\theta}\theta^k/k!\) satisfy \(\pi_k\theta=\pi_{k+1}(k+1)\). Given \(X_\theta(0)=0\), the population at time \(t\) consists of immigrants that arrived after zero and survived, hence is Poisson with mean \(\theta(1-e^{-t})\). Thus
\[
\Pr(X_\theta(0)=0,X_\theta(t)=d)
=\frac{e^{-2\theta+\theta e^{-t}}\theta^d(1-e^{-t})^d}{d!}.
\]
By stationarity and reversibility, symmetrizing the two integration times gives
\[
\mathbb E[W_0W_d]=\int_0^\infty e^{-t}\Pr(X_\theta(0)=0,X_\theta(t)=d)\,dt
=\frac{e^{-2\theta}\theta^d}{d!}\int_0^1e^{\theta u}(1-u)^d\,du.
\]
Since \(\mathbb EW_0=e^{-\theta}\) and \(\mathbb EW_d=e^{-\theta}\theta^d/d!\), subtracting their product proves (1). For completeness the time-ordering coefficient is exact: \(2\int_0^\infty e^{-2s}\,ds=1\), not \(2\).

**3. Unique ordered crossings.** Write \(I_d(\theta)=\int_0^1e^{\theta u}(1-u)^d\,du\). Differentiation under the integral gives \(I_d'(\theta)=\int_0^1u e^{\theta u}(1-u)^ddu>0\). Further \(I_d(0)=1/(d+1)<1\), and \(I_d(\theta)\to\infty\) by integrating over any closed subinterval of \((0,1)\). This proves the unique crossing and signs. Because \(I_{d+1}(\theta)<I_d(\theta)\) for each finite \(\theta\), the roots satisfy \(\theta_{d+1}>\theta_d\).

**4. Scale of the crossing.** Fix \(\eta\in(0,1)\), and put \(a_d^\pm=d+(1\pm\eta)\sqrt{d\log d}\). For \(u\in[0,1)\), \(\log(1-u)\le-u-u^2/2\). With \(\delta=(1-\eta)\sqrt{d\log d}\), completing the square gives
\[
I_d(a_d^-)\le\int_0^\infty e^{\delta u-du^2/2}\,du
\le\sqrt{2\pi/d}\,e^{\delta^2/(2d)}=O\bigl(d^{-\eta+\eta^2/2}\bigr)\longrightarrow0.
\]
For \(\delta=(1+\eta)\sqrt{d\log d}\), restrict the integral defining \(I_d(a_d^+)\) to the interval \(u\in[\delta/d-d^{-1/2},\delta/d+d^{-1/2}]\), which lies in \((0,1/2)\) for large \(d\). Uniformly there, \(\log(1-u)\ge-u-u^2/2-O(u^3)\), and
\[
(d+\delta)u+d\log(1-u)
\ge\frac{\delta^2}{2d}-O(1)-O(\delta^3/d^2).
\]
The cubic remainder tends to zero, so the integral is at least \(2d^{-1/2}\exp(\delta^2/(2d)-O(1))\to\infty\). Monotonicity forces \(a_d^-<\theta_d<a_d^+\) for all sufficiently large \(d\). Letting \(\eta\downarrow0\) proves (3).

## Verification
The accompanying self-contained `verify.py` uses exact rational recurrences for finite Ewens fixed-point occupation statistics, independent composite-Simpson integration for \(I_d\), and bisection for \(\theta_d\). It tests the phase signs, root ordering, benchmark roots and large-\(d\) scaling. It does not establish the unbounded-size limit by enumeration; the proof above supplies that argument. Run from the directory containing the file with `python verify.py`.

## Relationship to prior work
Gnedin and Stark, *Random Permutations and Queues* (arXiv:2209.12781v1, September 26, 2022), already define the same empirical state fractions in Section 3. Their Theorem 1 proves almost-sure liminf zero and limsup one, their mean calculation gives the limiting Poisson proportions, and their Theorem 6 provides the logarithmic-time process limit used in Step 1. Their Section 9 examines correlations of different *cycle-lifetime* counts, not covariance of empirical *fixed-point-state occupation fractions*. None of those statements supplies the sign-reversal thresholds or the \(d+\sqrt{d\log d}\) transition. These pre-existing results are essential inputs, not newly claimed discoveries.

Stark, *Markov chains generating random permutations and set partitions* (accepted 2024), constructs Markov chains for permutation generation including derangements, but its objectives differ from covariance comparisons of occupation times. General stationary infinite-server queue transition laws readily yield the integrand in (1); the scientifically proposed contribution is its threshold structure and quantified large-state boundary, not an original queueing transition kernel. Priority relative to all possible equivalent queueing calculations has not been independently established.

## Limitations
The process starts from the one-element permutation and has a fixed positive Ewens parameter. The empirical limit is weak, not almost-sure: the latter is ruled out by the earlier liminf/limsup theorem. Equation (1) is a limit at fixed \(d\), not a uniform finite-\(n\) estimate with \(d\) growing. The covariance-sign statement does not claim stochastic association or independence. Historical novelty relative to unpublished or differently formulated queueing results remains a limitation; independent mathematical audit has not been performed.

## References
1. A. Gnedin and D. Stark, *Random Permutations and Queues*, arXiv:2209.12781v1 (first public September 26, 2022), https://arxiv.org/abs/2209.12781; published in Advances in Applied Mathematics 2023.
2. D. Stark, *Markov chains generating random permutations and set partitions*, accepted manuscript 2024, QMUL repository https://qmro.qmul.ac.uk/xmlui/bitstream/handle/123456789/99650/Stark%20Markov%20chains%20generating%202024%20Accepted.pdf .
3. Standard stationary immigration–death queue theory (the exact Poisson stationary law and thinning transition), with background and detailed citations in Reference 1.
