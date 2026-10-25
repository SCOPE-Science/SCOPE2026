# Sharp drift threshold for optimal independent reset-to-record exploration

## Finding
Consider a nearest-neighbor walk on the integers, with a running record and an independent resetting clock that operates **even at the record itself**. A step goes right with probability \(p\in(0,1)\), left with probability \(q=1-p\), or resets the current position to the running maximum with probability \(r\in[0,1]\), as specified precisely below. If \(v_p(r)\) is the almost-sure long-time exploration speed of the running maximum, then the **unique** speed-maximizing resetting probability is
\[
r_*(p)=\begin{cases}
1-\dfrac{1}{2\sqrt{1-p}},&0<p<\tfrac34,\\[4pt]
0,&\tfrac34\le p<1.
\end{cases}
\]
The corresponding optimal speed is
\[
\max_{0\le r\le1}v_p(r)=
\begin{cases}
\dfrac{1-\sqrt{1-p}}{2\sqrt{1-p}},&0<p<\tfrac34,\\[5pt]
2p-1,&\tfrac34\le p<1.
\end{cases}
\]
In particular, positive resetting strictly improves exploration speed exactly when \(p<3/4\); for greater rightward bias, any resetting slows exploration. If \(\varepsilon=(1-p)-1/4\downarrow0\), then the optimal resetting probability and its gain over the no-reset speed vanish on different scales:
\[
r_*(p)=2\varepsilon+O(\varepsilon^2),\qquad
v_p(r_*)-v_p(0)=6\varepsilon^2+O(\varepsilon^3).
\]
This identifies a sharp drift boundary and a quadratic improvement onset for an unconditional reset-to-record clock, not for a clock suppressed at the frontier.

## Assumptions and scope
Let \((X_n,M_n)\) start at \((0,0)\), with \(M_n=\max_{0\le j\le n}X_j\). Fix \(p\in(0,1)\), \(q=1-p\), and \(r\in[0,1]\). At every integer time, independently draw one of three operations:

- With probability \(r\), set \(X_{n+1}=M_n\) and \(M_{n+1}=M_n\). **This consumes one time step even if \(X_n=M_n\)**, and is then a genuine no-op.
- With probability \((1-r)p\), set \(X_{n+1}=X_n+1\) and \(M_{n+1}=\max(M_n,X_{n+1})\).
- With probability \((1-r)q\), set \(X_{n+1}=X_n-1\) and \(M_{n+1}=M_n\).

Define \(v_p(r)=\lim_{n\to\infty}M_n/n\). This limit exists almost surely and in \(L^1\), as established below; the same limit holds for \(X_n/n\). No finite-time optimum, higher-order fluctuation law, or frontier-conditioned resetting protocol is asserted.

## Proof
**1. Gap reduction and stationarity.** Set \(G_n=M_n-X_n\ge0\), and \(t=1-r\). For \(0<r<1\), its transition law is
\[
G\ge1:\quad G\to0\ (r),\quad G\to G-1\ (tp),\quad G\to G+1\ (tq),
\]
\[
G=0:\quad 0\to0\ (r+tp),\qquad 0\to1\ (tq).
\]
Any positive gap resets to zero with probability \(r\) on the next step; the chain is irreducible, aperiodic, and positive recurrent. The unique invariant law is geometric:
\[
\pi_g=(1-\lambda)\lambda^g,\qquad
\lambda=\frac{2tq}{1+\sqrt{1-4t^2pq}},\qquad 0<\lambda<1.
\]
To verify this, substitute the geometric ansatz into every interior balance equation to obtain \(\lambda=t(q+p\lambda^2)\), whose admissible solution is the displayed smaller quadratic root. The state-zero balance also holds: from zero the chain stays with probability \(r+tp\), from state one it arrives at zero through resetting or a right step, and from every higher state through resetting; their sum is \(\pi_0\) by the same root identity. Irreducible positive recurrence gives uniqueness.

**2. Speed and endpoints.** The record increases exactly when \(G_n=0\) and the next operation is a right step. Ergodicity and the bounded martingale-difference strong law therefore give
\[
v_p(r)=(1-r)p\pi_0=tp(1-\lambda),\qquad 0<r<1.
\]
Since \(0\le M_n/n\le1\), almost-sure convergence also gives convergence of means. Moreover \(G_n/n\to0\) almost surely and in \(L^1\): for any fixed \(\eta>0\) and \(n\) large enough, \(G_n\ge\eta n\) requires at least \(\lceil\eta n\rceil\) consecutive steps without a reset, so its probability is bounded by \(t^{\lceil\eta n\rceil}\). Borel–Cantelli proves the almost-sure statement; the same exponential tail gives \(\mathbb E G_n/n\to0\). Thus \(X_n/n\) shares the record speed.

When \(r=1\), the walk never moves, hence \(v_p(1)=0\). When \(r=0\), the ordinary strong law for a biased walk and its running maximum yield \(v_p(0)=\max(2p-1,0)\), in both the almost-sure and mean senses. The formula for \(0<r<1\) has exactly these continuous endpoint limits (taking \(\lambda\to\min(1,q/p)\) at \(r\downarrow0\)), so the optimization below covers the full closed interval.

**3. Global maximization.** For \(0<r<1\), the quadratic-root identity rewrites as
\[
t=\frac{\lambda}{q+p\lambda^2},\qquad
v_p=\frac{p\lambda(1-\lambda)}{q+p\lambda^2}.
\]
The map \(\lambda\mapsto t\) is strictly increasing on the admissible interval, from zero to one, and \(\lambda\) runs from zero to \(\lambda_0=\min(1,q/p)\). Differentiation, with a strictly positive denominator, gives
\[
\operatorname{sgn}\frac{d v_p}{d\lambda}
=\operatorname{sgn}\bigl(q(1-2\lambda)-p\lambda^2\bigr).
\]
The expression decreases strictly on \([0,1]\) and has exactly one positive zero, \(\lambda_*=\sqrt q/(1+\sqrt q)\). It lies strictly within the accessible range precisely when \(\sqrt q>1/2\), equivalently \(p<3/4\). In that case it uniquely maximizes the speed; back-substitution gives \(t_*=1/(2\sqrt q)\), hence \(r_*=1-1/(2\sqrt q)\) and \(v_p(r_*)=(1-\sqrt q)/(2\sqrt q)\). For \(p\ge3/4\), the derivative never becomes negative before the no-reset endpoint, hence \(r=0\) uniquely maximizes speed, including equality at the critical parameter.

**4. Sharp onset.** For \(1/2<p<3/4\), put \(s=\sqrt q\); the exact speed gain is
\[
\frac{1-s}{2s}-(2p-1)=\frac{(s+1)(2s-1)^2}{2s}>0.
\]
For \(p\le1/2\), the no-reset speed is zero but the interior optimum has positive speed. The displayed exact gain expands to \(6\varepsilon^2+O(\varepsilon^3)\) at \(q=1/4+\varepsilon\). Expanding \(1-1/(2\sqrt q)\) gives \(2\varepsilon+O(\varepsilon^2)\). All endpoint claims follow.

## Verification
Run `python3 verify.py` from the directory containing the accompanying code. Only the Python standard library is used. The program independently propagates the full \((X,M)\) pair and the reduced gap for five exact-rational parameter pairs and six horizons, checking 30 finite-time identities. It separately verifies geometric stationary balance and speed for 841 interior parameter pairs, and compares the proposed optimum against 29,029 parameter-grid evaluations. These checks were run successfully. The proof above, rather than these finite tests, establishes the infinite-time statements and global uniqueness.

## Relationship to prior work
Majumdar, Sabhapandit, and Schehr [1] introduced random resetting to a running maximum and derived its speed and fluctuations for symmetric nearest-neighbor motion. **Their resetting is activated only while the walker lies strictly below its maximum**; at the frontier they always attempt a left/right step (their Section II, equations (2)–(3)). The present protocol instead draws the reset coin at every step, including an inert reset at the frontier, and allows biased steps \(p\ne1/2\). Their stated results do not imply this different protocol's optimized bias threshold.

Can, Doan, and Nguyen [2] prove strong laws and central limit theorems for the frontier-conditioned symmetric model, and extend it to time-decaying reset probabilities. Their Sections 1–2 retain equal left/right motion and the original frontier rule. Those statements do not classify the present fixed-clock biased optimum.

Bonomo and Pal [3] establish general discrete-time first-passage restart identities, including biased walks confined by two absorbing boundaries. Radice [4] derives analogous first-hitting-time optimization criteria for stochastic resetting, especially the Gillis walk. Their generic renewal methods can be adapted to obtain a particular record-increment mean time here; the general renewal principle and elementary optimization techniques are **not** claimed as new. The specific all-bias record-clock speed, sharp \(3/4\) no-reset transition, unique global optimizer, and quadratic gain onset are not established in the inspected treatments.

## Limitations
The statement is only for a one-dimensional nearest-neighbor discrete-time walk, independent Bernoulli resetting to its current rightmost record **including at the frontier**, constant step bias \(0<p<1\), and asymptotic speed. It does not apply to a conditioned-on-gap reset coin, to non-Markovian waiting times, to heavy-tailed jumps, or to finite-time search costs. The bibliographic comparison is not exhaustive: an unindexed biased restart specialization or a general result with an already evaluated optimizer could cover some statements.

## References
[1] S. N. Majumdar, S. Sabhapandit, G. Schehr, "Random walk with random resetting to the maximum," arXiv:1509.04516 (initial version 2015-09-15), later Physical Review E 92, 052126 (2015), https://arxiv.org/abs/1509.04516.

[2] V. H. Can, T. S. Doan, V. Q. Nguyen, "Limit Theorems for the One-Dimensional Random Walk with Random Resetting to the Maximum," Journal of Statistical Physics 183 (2021), DOI:10.1007/s10955-021-02754-w, accessible manuscript https://math.ac.vn/uploads/files/IMH20210205.pdf.

[3] O. L. Bonomo and A. Pal, "First passage under restart for discrete space and time: application to one dimensional confined lattice random walks," Physical Review E 103, 052129 (2021), arXiv:2102.00895, https://arxiv.org/html/2102.00895v1.

[4] M. Radice, "Non-homogeneous random walks with stochastic resetting: an application to the Gillis model," arXiv:2208.10220 (2022), https://arxiv.org/abs/2208.10220.
