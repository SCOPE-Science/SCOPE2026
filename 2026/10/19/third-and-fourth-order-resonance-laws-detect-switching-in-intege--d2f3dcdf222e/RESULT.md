# Third- and fourth-order resonance laws detect switching in integer expanding circle maps

## Finding

Let \(n\ge1\), and choose any deterministic integers \(b_0,\ldots,b_{n-2}\ge2\). Starting at a Lebesgue-uniform \(X\in[0,1)\), successively apply the expanding circle maps \(T_b(x)=bx\pmod1\). Set \(a_0=1\), \(a_{j+1}=b_ja_j\), and observe the finite-time cosine sum
\[
S_n(X)=\sum_{j=0}^{n-1}\cos(2\pi a_jX).
\]
Write \(N_2=\#\{0\le j<n-1:b_j=2\}\), \(N_3=\#\{0\le j<n-1:b_j=3\}\), and \(N_{22}=\#\{0\le j<n-2:b_j=b_{j+1}=2\}\). The **exact conditional moments for every integer switching schedule** are
\[
\begin{aligned}
\mathbb E_X S_n&=0,\\
\mathbb E_X S_n^2&=\frac n2,\\
\mathbb E_X S_n^3&=\frac34N_2,\\
\mathbb E_X S_n^4&=\frac{3n^2}{4}-\frac{3n}{8}+\frac12N_3+\frac32N_{22}.
\end{aligned}
\]
Consequently the fourth cumulant is
\[
\kappa_4(S_n)=\mathbb E_XS_n^4-3(\mathbb E_XS_n^2)^2=-\frac{3n}{8}+\frac{N_3}{2}+\frac{3N_{22}}{2}.
\]

For the natural binary switch alphabet \(b_j\in\{2,3\}\), put \(L=n-1\), \(m=N_2\), \(A=N_{22}\). The pair consisting of the third moment and fourth cumulant recovers both statistics *exactly*:
\[
m=\frac43\mathbb E_XS_n^3,
\qquad
A=\frac23\left(\kappa_4(S_n)+\frac{3n}{8}-\frac{L-m}{2}\right).
\]
The **sharp complete attainable fourth-cumulant spectrum at fixed \(n,m\)** is the arithmetic grid
\[
\left\{-\frac{3n}{8}+\frac{L-m}{2}+\frac32A:\ A\in\mathbb Z,\ A_{\min}\le A\le A_{\max}\right\},
\]
where \(A_{\min}=A_{\max}=0\) if \(m=0\), and otherwise
\[
A_{\min}=\max\{0,2m-L-1\},\qquad A_{\max}=m-1.
\]
Every grid point is attained by a switching schedule, with no gaps. These low-order moments determine the **number and adjacent clustering of doubling choices**, not the full ordered schedule.

## Assumptions and scope

The expectation \(\mathbb E_X\) is exclusively over a Lebesgue-uniform initial point, with the whole schedule held fixed. All slopes are integers at least two; no distribution, independence, or stationarity is assumed for the schedule. The statement includes \(n=1\), with empty transition counts, and covers arbitrarily large integer slopes. The cumulative frequencies obey \(a_{j+1}\ge2a_j\).

For an additional annealed illustration, if the switches are independent, doubling occurs with probability \(p\in[0,1]\), and tripling otherwise, independently of \(X\), then
\[
\begin{aligned}
\mathbb E S_n^3&=\frac34(n-1)p,\\
\kappa_4(S_n)&=-\frac{3n}{8}+\frac{(n-1)(1-p)}2+\frac{3(n-2)_+p^2}{2},
\end{aligned}
\]
where \((n-2)_+=\max\{n-2,0\}\). Here the joint expectation is over \(X\) and the independent switches; the formula follows because the conditional first two moments are constant and \(\mathbb E N_{22}=(n-2)_+p^2\). It is not a claim about empirical estimation error or arbitrary observables.

## Proof

**Fourier reduction.** For any positive integer \(u\), write \(c_u(x)=\cos(2\pi ux)=(e^{2\pi iux}+e^{-2\pi iux})/2\). Thus the integral of a product of \(k\) such cosines equals \(2^{-k}\) times the number of sign choices for which the signed sum of its \(k\) positive frequencies vanishes. Frequencies \(a_0<\cdots<a_{n-1}\) are distinct. There is no first-order constant coefficient, and orthogonality gives the second moment \(n/2\).

**Three-factor resonances.** A zero signed sum with three selected frequencies must, up to permutation, be \(u+u=v\). Indeed a sum of three positive terms cannot cancel without the largest equaling the sum of two others; if the two smaller indices differ, their sum lies strictly between the larger small frequency and twice it, while the next allowable frequency is at least twice it. Hence the two small factors coincide. Since each frequency quotient along the orbit is a positive integer, \(v=2u\) occurs precisely at one transition with \(b_j=2\). At such a transition, \(\int c_u^2c_{2u}\,dx=1/4\). There are three permutations, contributing \(3/4\) per occurrence, proving the third-moment formula.

**Four-factor resonances.** Separate the possible equality patterns of four indices. A quadruple with one frequency has integral \(\int c_u^4\,dx=3/8\). Two different doubled frequencies have integral \(\int c_u^2c_v^2\,dx=1/4\), and six permutations. These give \(3n/8+6\binom n2/4=3n^2/4-3n/8\).

For a triple frequency and one distinct frequency, the only signed relation is \(u+u+u=v\): the distinct frequency must be larger, and its quotient must be three. Since consecutive integer multipliers are at least two, this means exactly one adjacent transition \(b_j=3\). Each such unordered quadruple has integral \(\int c_u^3c_{3u}\,dx=1/8\) and four permutations, contributing \(1/2\).

For exactly one doubled frequency and two distinct single frequencies, write their increasing distinct values as \(u<v<w\). A signed sum can vanish only when \(2u+v=w\). If \(v\) were the doubled frequency, the candidate equality \(u+2v=w\) would make \(w/v=2+u/v\) a noninteger, contrary to integer quotients; if \(w\) were doubled, it exceeds the sum of the smaller two. In the remaining case, \(w/v=1+2u/v\) is an integer with \(0<2u/v\le1\). Therefore \(v=2u\) and \(w=2v=4u\), i.e. two consecutive doubling transitions. The integral is \(\int c_u^2c_{2u}c_{4u}\,dx=1/8\), with twelve permutations, contributing \(3/2\).

Four distinct frequencies cannot balance: if \(w\) is largest and \(v\) second largest, the other two are at most \(v/2\) and \(v/4\), so their sum with \(v\) is at most \(7v/4<2v\le w\). These cases exhaust all fourth-order index patterns and yield the fourth-moment and cumulant identities.

**Sharp inverse range.** Now restrict switches to \(\{2,3\}\). Knowing \(n\) and the third moment determines \(m\); since \(N_3=L-m\), the fourth cumulant determines \(A\) by direct rearrangement. If \(m=0\), then \(A=0\). Otherwise let \(r\) be the number of nonempty contiguous runs of doubling switches. Every doubling run of length \(\ell\) contributes \(\ell-1\) adjacent pairs, whence \(A=m-r\). With \(L-m\) tripling symbols separating the runs, exactly
\[
1\le r\le\min\{m,L-m+1\}
\]
are possible. Conversely each integer \(r\) in this range is realizable by separating \(r\) positive-length doubling runs with tripling symbols, distributing surplus symbols freely. Substituting \(A=m-r\) gives exactly the stated contiguous integer interval and proves that every cumulant-grid point occurs.

## Verification

The included standalone `checks/verify_moments.py` expands the finite cosine polynomial into exact integer Fourier coefficients and computes its third and fourth moments as rational numbers, **without using the resonance classification to calculate the test expectations**. Running `python3 checks/verify_moments.py` produces 2,297 matching exact Fourier comparisons (all binary schedules of up to ten switches, plus 250 sampled integer schedules whose multipliers range over 2, 3, 4, 5, 7 and 11) and 66 exhaustive small-length inverse-spectrum comparisons. The proof above, not finite testing, establishes the theorem for all lengths and slopes.

## Relationship to prior work

Suzuki [1] analyzes random beta-transformations, including integer-slope instances, and establishes invariant/random density formulas and response properties. The current statement instead concerns **conditional, exact finite-time statistics for arbitrary prescribed switching strings**, and uses the same expanding-map object rather than Suzuki's density theorems.

Aistleitner, Berkes and Tichy [2, Section 3] explicitly explain the established general principle that higher moments of lacunary trigonometric sums count signed Diophantine relations. In particular they identify dyadic three-factor resonances; orthogonality and the moment-counting method are prior theory, not claimed as new. The contribution here is the complete low-order local resonance census for arbitrary integer-slope products, the exact two-statistic inverse, and the sharp *attainable* cumulant grid under switching between the two smallest slopes. These are not asserted in [2].

Prochno and Strzelecka [3] use cumulants and correlation graphs to establish moderate-deviation and mod-Gaussian results for lacunary sums. Their asymptotic theorems do not state this finite-schedule cumulant/inverse-spectrum classification. Aimino, Nicol and Vaienti [4, Example 7.3] establish quenched central limit theorems for random integer expanding maps; those results do not recover fixed-schedule local run statistics from raw finite moments. A published result on random integer maps' nondegenerate asymptotic variance [5] is also about a different, asymptotic observable and averaging regime. An equivalent low-order enumeration derived elsewhere remains a priority risk.

## Limitations

This is a finite-time, single-observable exact-moment theorem. It neither distinguishes all switching words nor asserts statistical identifiability from finitely many noisy trajectories. The full schedule is not reconstructible from these two moment statistics. The Fourier cancellation method is classical; the specific formulas and inverse extremal classification may have uncatalogued analogues. For noninteger slopes, initial measures other than Lebesgue, or observables other than the first cosine, the statements need not hold. There is no independent mathematical audit at this stage.

## References

1. Shintaro Suzuki, *Absolutely continuous invariant measures for random dynamical systems of beta-transformations*, arXiv:2303.17521 (first public posting 30 March 2023), https://arxiv.org/abs/2303.17521. Primary MSC2020 37E05.
2. Christoph Aistleitner, István Berkes and Robert F. Tichy, *Lacunary sequences in analysis, probability and number theory*, arXiv:2301.05561 (first public posting 13 January 2023), Section 3, https://arxiv.org/abs/2301.05561.
3. Joscha Prochno and Marta Strzelecka, *Moderate deviation principles and mod-Gaussian convergence for lacunary trigonometric sums*, arXiv:2312.09137 (first public posting 14 December 2023), https://arxiv.org/abs/2312.09137.
4. Romain Aimino, Matthew Nicol and Sandro Vaienti, *Annealed and quenched limit theorems for random expanding dynamical systems*, arXiv:1310.4359, Example 7.3, https://arxiv.org/abs/1310.4359.
5. *Distinct integer beta maps eliminate zero variance and give an exact noise-onset coefficient*, published published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-distinct-integer-beta-maps-eliminate-zero-variance-and-give-an-e--c097279b5a2a.
