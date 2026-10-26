# Second-moment Markov mimicry in finite semi-Markov networks is exactly locally identifiable

## Finding

**Theorem (all-target second-order Markov mimicry).** Let a finite, irreducible, loop-free embedded Markov chain have transition probabilities \(P_{ij}\), and attach a strictly positive, destination-dependent semi-Markov holding time \(\tau_i\) to each departure from state \(i\). Assume finite positive means \(\mu_i=\mathbb E_i\tau_i\) and finite second moments. Compare this semi-Markov process to the continuous-time Markov chain with jump rates \(P_{ij}/\mu_i\). For every ordered pair of *distinct* initial and target states, the two processes always have the same mean first-hitting time. They have the same **second** first-hitting moments for *every* such pair if and only if, for every state \(i\) and every destination \(j\),

\[
\mathbb E_i[\tau_i^2]=2\mu_i^2,\qquad
\mathbb E_i[\tau_i\mathbf1_{\{J_1=j\}}]=\mu_iP_{ij}.
\]

The second condition says that the holding time and the next destination are uncorrelated at first order; it does **not** require them to be independent. Neither condition forces an exponential holding-time distribution. Hence an entire family of genuinely non-Markovian networks, including ones with destination-dependent conditional holding-time laws, has exactly the same all-pairs first and second passage-time moments as its rate-matched Markov chain.

## Assumptions and scope

There are \(n\ge2\) states. The row-stochastic matrix \(P\) is irreducible with \(P_{ii}=0\). Each visit to state \(i\) draws a fresh pair \((\tau_i,J_1)\), independently of prior history conditional on the current state; its joint law is stationary across visits and satisfies \(\tau_i>0\) almost surely, \(\mathbb P_i(J_1=j)=P_{ij}\), \(0<\mu_i<\infty\), and \(\mathbb E_i\tau_i^2<\infty\). The process is observed from a state-entry epoch. The hitting time \(T_{i\to t}\) stops on first *arrival* at a different target \(t\), without including a sojourn at \(t\). Its Markov comparator has the same jump matrix and independent exponential departure durations of mean \(\mu_i\). These assumptions ensure all displayed passage moments are finite, even if conditional holding time and destination are dependent.

## Proof

**1. First-step moments.** Set \(h_i^t=\mathbb E_i T_{i\to t}\), \(u_i^t=\mathbb E_i T_{i\to t}^2\), and \(h_t^t=u_t^t=0\). Write \(m_{2,i}=\mathbb E_i\tau_i^2\) and \(a_{ij}=\mathbb E_i[\tau_i\mathbf1_{\{J_1=j\}}]\). Independence of future visits conditional on the next state gives, for \(i\ne t\),

\[
h_i^t=\mu_i+\sum_jP_{ij}h_j^t,\qquad
u_i^t=m_{2,i}+2\sum_ja_{ij}h_j^t+\sum_jP_{ij}u_j^t.
\]

For the comparator, replace \(m_{2,i}\) by \(2\mu_i^2\) and \(a_{ij}\) by \(\mu_iP_{ij}\). Irreducibility makes the transition matrix killed at \(t\) transient, so these linear systems have unique finite solutions. Thus all first moments agree, and the two second-moment vectors agree for target \(t\) exactly when

\[
d_i+2\sum_j c_{ij}h_j^t=0 \quad\text{for each }i\ne t,
\]

where \(d_i=m_{2,i}-2\mu_i^2\) and \(c_{ij}=a_{ij}-\mu_iP_{ij}\). In particular, \(\sum_jc_{ij}=0\) and \(c_{ii}=0\). This proves sufficiency immediately. Necessity requires using *all* targets, not just one.

**2. The hitting-time inversion lemma.** Let \(\pi\) be the positive stationary row law of the embedded matrix \(P\), and put \(\bar\mu=\sum_k\pi_k\mu_k>0\). Define the invertible fundamental matrix \(Z=(I-P+\mathbf1\pi)^{-1}\), which obeys \(Z\mathbf1=\mathbf1\). The mean hitting-time column \(h^t\) satisfies, including the target row,

\[
(I-P)h^t=\mu-(\bar\mu/\pi_t)e_t.
\]

Indeed, the equation holds with right-hand side \(\mu\) away from \(t\), and stationarity of \(\pi\) forces the stated target-row correction. Since \(h_t^t=0\), this yields, for **any** row vector \(c\) with \(c\mathbf1=0\),

\[
c h^t=c Z\mu-\frac{\bar\mu}{\pi_t}(cZ)_t.
\]

Fix a departure state \(i\) and abbreviate \(c=(c_{ij})_j\), \(d=d_i\). The assumed second-moment agreement for every target \(t\ne i\) says \(d+2c h^t=0\). Therefore, with \(A=(cZ\mu+d/2)/\bar\mu\),

\[
(cZ)_t=A\pi_t\qquad(t\ne i).
\]

Because \(cZ\mathbf1=c\mathbf1=0\), the remaining coordinate is fixed and \(cZ=A(\pi-e_i)\). Multiplying by \(Z^{-1}=I-P+\mathbf1\pi\) gives

\[
c=A(P_{i\cdot}-e_i).
\]

But \(c_i=0\), while \(P_{ii}=0\); the \(i\)-th coordinate of this identity is \(-A\), hence \(A=0\). Consequently \(c=0\), and the original equality gives \(d=0\). As \(i\) was arbitrary, both stated local moment conditions follow for all states. This proves necessity.

**3. Explicit non-Markovian indistinguishability.** On three states take \(P_{ij}=1/2\) for \(i\ne j\). Choose any positive \(\mu_i\). Conditional on departure to one of the two destinations, choose a lognormal holding-time law with mean \(\mu_i\) and variance \(\mu_i^2/2\); for the other destination choose a lognormal law with the *same* mean and variance \(3\mu_i^2/2\). Such positive lognormal laws exist: a desired mean \(m>0\) and variance \(v>0\) correspond to log-variance \(\log(1+v/m^2)\) and log-mean \(\log m-\tfrac12\log(1+v/m^2)\). The conditional means are identical, but the conditional laws differ, so destination and holding time are not independent. Their unconditional second moment is \(\mu_i^2+\frac12(\mu_i^2/2+3\mu_i^2/2)=2\mu_i^2\). The theorem therefore gives exact agreement with the Markov comparator for all **six** ordered distinct initial-target pairs in both the first and the second passage moments. The holding-time laws are non-exponential, and the processes are not Markov in their visible state alone.

## Verification

The accompanying `verify.py` uses exact rational arithmetic to reconstruct the first-step first/second-moment equations for strongly connected matrices of sizes \(2\) through \(7\), tests the square all-target inversion for every starting state, and checks a perturbation that is detected by second moments. Its \(6{,}502\) checks passed. The lognormal witness's first two conditional moments are checked algebraically; the proof, not these finite tests, establishes the theorem for every finite \(n\).

## Relationship to prior work

Voits (2026), Theorem 15, establishes a general spanning-forest formula for semi-Markov hitting-time moments and notes that mean hitting times agree with those of the pseudo-rate Markov chain while higher moments contain semi-Markov information. Silvestrov and Manca (2017), particularly Section 2, give general semi-Markov first-step moment recursions and phase-space reduction algorithms. The present result uses those familiar recursions but asks a different inverse question: **if every target's first two hitting moments agree with the Markov comparator, precisely which local holding-time moment data remain invisible?** The all-target fundamental-matrix inversion proves the stated necessary-and-sufficient answer and the destination-dependent non-Markovian example witnesses non-identifiability beyond second order. Known stationary two-time-law aliasing for alternating renewal processes concerns a different set of observables and does not imply this all-target hitting-moment characterization.

## Limitations

This theorem characterizes only entry-epoch first/second *hitting-time moments*. It does not assert equality of whole hitting-time distributions, stationary two-time laws, transient probabilities, or third/higher moments; non-exponential lognormal clocks generally differ at higher orders. The necessity argument uses all distinct ordered initial-target pairs, a finite irreducible embedded chain, strictly positive finite-second-moment holds, and no self-loops. A single fixed target does not generally give the same identification. The previous general moment recursions are strong contextual prior work; an equivalent inverse characterization hidden in other semi-Markov literature cannot be categorically excluded without independent bibliographic review.

## References

1. Julian B. Voits, *Graph-theoretic framework for semi-Markov networks: transient and stationary occupation probabilities, hitting times and weak ergodicity breaking*, arXiv:2610.13505v1 (first posted 2026-10-09), especially Theorem 15 and Section 5. https://arxiv.org/abs/2610.13505
2. D. Silvestrov and R. Manca, *Reward Algorithms for Semi-Markov Processes*, Methodology and Computing in Applied Probability **19** (2017), 1191–1209, DOI: 10.1007/s11009-017-9559-2, especially Section 2. https://doi.org/10.1007/s11009-017-9559-2
