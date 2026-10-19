# Brownian first-exit law for random-input Černý pair coalescence

## Finding
For an integer \(n\ge 3\), let the Černý automaton have state set \(\{0,\ldots,n-1\}\) and two letters \(a,b\), acting by
\[
a(i)=i+1\pmod n,\qquad b(n-1)=0,\quad b(i)=i\quad(0\le i<n-1).
\]
Independently at each time choose \(a\) with probability \(p\in(0,1)\) and \(b\) with probability \(q=1-p\). For any sequence of starting pairs \(0\le i_n<j_n<n\) with \((j_n-i_n)/n\to x\in(0,1)\), let \(T_n\) be the first time the two states become equal under the common random input. Then
\[
\frac{T_n}{n^3}\ \xrightarrow{\mathrm d}\ \tau_{p,x}:=\inf\{t\ge0:x+\sqrt{2p^2q}\,B_t\notin(0,1)\},
\]
where \(B\) is a standard Brownian motion. Equivalently, for every \(s\ge0\),
\[
\lim_{n\to\infty}\mathbb E\exp(-sT_n/n^3)
=\frac{\cosh\bigl((x-\tfrac12)\sqrt{s/(p^2q)}\bigr)}
{\cosh\bigl(\tfrac12\sqrt{s/(p^2q)}\bigr)}.
\]
In particular, the limit has mean \(x(1-x)/(2p^2q)\). The complete limiting distribution for any fixed macroscopic pair separation differs among input biases only by a deterministic time rescaling; its quantiles and tail probabilities are minimized simultaneously by the **unique** bias \(p=2/3\) (cycle-letter probability, with reset probability \(1/3\)). The limit variance is
\[
\operatorname{Var}(\tau_{p,x})
=\frac{x(1-x)(1-2x+2x^2)}{12p^4q^2}.
\]
For \(p=x=1/2\), the limiting mean is \(1\) and variance is \(2/3\).

## Assumptions and scope
The probability \(p\) is fixed strictly between zero and one as \(n\) grows; the initial normalized clockwise gap tends to a fixed interior point \(x\). The coalescence time concerns one specified pair of states driven by identical letters, not the simultaneous synchronization time of all states. Endpoints \(x=0,1\), varying biases \(p=p_n\), and finite-\(n\) stochastic optimality are not asserted.

## Proof
**1. Exact cycle decomposition.** Label the two moving states \(X,Y\) (the order of labels is fixed until coalescence), and put \(d=(Y-X)\bmod n\in\{1,\ldots,n-1\}\). Begin a complete cycle when \(X=0\). While \(X\) passes the phases \(0,1,\ldots,n-2\), a phase advances on the first occurrence of \(a\); at phase \(n-1\), either letter advances \(X\) to zero. Hence a hypothetical complete cycle takes
\[
C_n=1+G_1+\cdots+G_{n-1},\qquad
\mathbb EC_n=1+(n-1)/p,\qquad
\operatorname{Var}(C_n)=(n-1)q/p^2,
\]
with independent geometric \(G_i\) on \(\{1,2,\ldots\}\), having success probability \(p\). Independent fresh input blocks give independent copies of this whole-cycle duration, after coupling the final truncated cycle to a hypothetical completion.

For a cycle started at gap \(d\), \(Y\) reaches the exceptional state \(n-1\) while \(X=n-1-d\); this is a phase strictly before \(X=n-1\). If the first letter there is \(b\), the gap increases by one; otherwise it does not. Let \(U\) be that event's indicator. At \(X=n-1\), the first letter \(b\) decreases the gap by one, otherwise the gap does not change; let \(V\) be its indicator. The first letters are fresh and distinct, so for each complete cycle \(U,V\) are independent Bernoulli variables of parameter \(q\); the pairs are independent from cycle to cycle. Exactly one opportunity of each kind occurs in an unabsorbed cycle. The gap changes according to
\[
d\ \longmapsto\ d+U\ \longmapsto\ d+U-V,
\]
and coalescence occurs precisely if the intermediate value equals \(n\) or the final value equals zero. The former can happen only at \(d=n-1,U=1\), the latter only at \(d=1,U=0,V=1\). These statements also cover the degenerate gaps. The proposed cut-by-cut transition was exhaustively replayed against the original two-state automaton for \(3\le n\le30\) in the packaged verifier.

**2. Coupling to gambler's ruin.** Use the same independent \(U,V\) and define an unrestricted-in-the-interior lazy nearest-neighbor walk with macro-increments \(\Delta=U-V\), absorbed upon first reaching either \(0\) or \(n\). Let its absorption cycle count be \(H_n\), and the actual pair's count, with a partially completed terminal cycle counted once, be \(N_n\). They agree except that the actual process can die earlier when it is at gap \(n-1\) and \(U=V=1\); the ordinary walk then remains at \(n-1\). Thus \(N_n\le H_n\), and by the strong Markov property and the ruin formula,
\[
0\le\mathbb E(H_n-N_n)\le\frac{n-1}{2pq}.
\]
Indeed, the lazy walk has equal upward/downward probabilities \(pq\), zero drift and variance \(2pq\), so the exact expected absorption time from \(d\) is \(d(n-d)/(2pq)\). In particular \(H_n/n^2\) is tight, and \((H_n-N_n)/n^2\to0\) in probability.

**3. Diffusion limit and clock.** Donsker's invariance principle gives, at cycle-time scale \(n^2\),
\[
\frac{d_n+\sum_{j=1}^{\lfloor un^2\rfloor}\Delta_j}{n}
\ \Rightarrow\ x+\sqrt{2pq}\,B_u.
\]
The first-exit functional from \((0,1)\) is almost surely continuous at the limiting Brownian sample paths: the exit time is finite and Brownian motion crosses the hit endpoint arbitrarily soon thereafter. Therefore \(H_n/n^2\) converges to the corresponding Brownian exit time, and so does \(N_n/n^2\).

Writing \(\mu_n=\mathbb EC_n\) and \(m\le Kn^2\), Kolmogorov's maximal inequality yields
\[
\mathbb P\left(\max_{m\le Kn^2}\left|\sum_{j=1}^{m}(C_{n,j}-\mu_n)\right|>\varepsilon n^3\right)
\le\frac{Kn^2(n-1)q/p^2}{\varepsilon^2n^6}\longrightarrow0.
\]
Tightness of \(N_n/n^2\) permits replacement of the random number of cycles by its expectation clock. The terminal incomplete cycle is negligible: the maximum hypothetical cycle duration through \(Kn^2\) cycles, divided by \(n^3\), tends to zero in probability by the second moment bound and a union bound. Hence
\[
\frac{T_n}{n^3}-\frac{N_n}{pn^2}\ \xrightarrow{\mathbb P}\ 0.
\]
For arbitrary initial \(X=i_n\), the unfinished initial passage until \(X=0\) has expected length at most \(n/p+1\) and affects the gap by at most two. Because \(x\in(0,1)\), for sufficiently large \(n\) this passage cannot coalesce the pair. Its scaled duration and normalized gap change vanish. Consequently the physical-time limit is Brownian motion with diffusion generator \(p^2q\,\partial_{xx}\), as claimed.

**4. Distribution and optimal bias.** The Laplace transform of the exit time solves \(p^2q\,f''=sf\) on \((0,1)\), with \(f(0)=f(1)=1\), giving the displayed hyperbolic-cosine ratio. The first two moment boundary problems give \(\mathbb E\tau_{p,x}=x(1-x)/(2p^2q)\) and the variance above. Brownian scaling gives \(\tau_{p,x}\stackrel{\rm d}{=}\tau_{1,x}/(p^2q)\), where \(\tau_{1,x}\) is exit time for generator \(\partial_{xx}\). The strictly positive function \(p^2(1-p)\) is uniquely maximized at \(p=2/3\); this minimizes the entire limiting time distribution in stochastic order.

## Verification
Run `python verify.py` with Python 3, NumPy and SciPy (listed in `requirements.txt`). The code independently reproduces the actual automaton's two-letter transitions for all \(1736\) possible macro-branch cases with \(3\le n\le30\). Separately, it solves the full pair-state discounted linear equations—without using the macro-cycle reduction—for \(n\in\{20,40,80\}\), for \(p\in\{1/2,2/3\}\) and \(x\in\{1/4,1/2\}\). The resulting Laplace values converge toward the formula at \(s=3/4\). The packaged verifier's exact output is reported in `VERIFICATION.md`; this numerical evidence is not offered as a proof of weak convergence.

## Relationship to prior work
Gusev, *Synchronizing automata with random inputs* (arXiv:1404.6731, initially submitted April 27, 2014), derives pairwise expected synchronization times for Černý automata under biased Bernoulli input. Its Section 3 develops pair-state first-moment recurrences, not a limit law for the entire coalescence-time distribution. The present result uses a fresh two-opportunity cycle reduction and a diffusion-and-clock argument to identify the full limit for every macroscopic starting gap and every fixed input bias. Gonze and Jungers, *On the Synchronizing Probability Function and the Triple Rendezvous Time for Synchronizing Automata* (arXiv:1410.4034, initially submitted October 15, 2014), studies a game-theoretic optimal-word probability function and deterministic triple rendezvous thresholds, not an i.i.d.-input pair hitting-time law. Classical gambler's ruin and Donsker theorems are used as standard ingredients, but alone do not establish the reduction or time constant for this automaton.

## Limitations
The conclusion is a weak limit; it does not assert total-variation convergence of integer-valued scaled times, convergence rates, exact finite-\(n\) Laplace transforms, or optimal bias at finite \(n\). No independence from the common input is assumed between the two state trajectories. Earlier unpublished or unindexed equivalent distributional analyses are not ruled out by the literature searches. No independent scientific audit has been performed.

## References
1. V. V. Gusev, *Synchronizing automata with random inputs*, arXiv:1404.6731 (first submitted 2014-04-27), https://arxiv.org/abs/1404.6731.
2. F. Gonze and R. M. Jungers, *On the Synchronizing Probability Function and the Triple Rendezvous Time for Synchronizing Automata*, arXiv:1410.4034 (first submitted 2014-10-15), https://arxiv.org/abs/1410.4034.
3. Donsker's invariance principle and the elementary gambler's ruin hitting-time formula (standard probability results; precise uses and hypotheses are stated in the proof).
