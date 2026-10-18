# Exact maximum-depth excursions and two critical crossovers in the Pelikan random map

## Finding

For the Pelikan random map and the finite excursion from the upper dyadic half-interval back to itself, the **entire maximum-depth distribution** is explicit. Let \(p\in[1/2,1]\), \(q=1-p\), and \(m\ge1\) an integer. With the precise random experiment below, write \(H_m(p)=\Pr(M\ge m)\). For \(1/2<p<1\), \(p\ne2/3\), set \(r=p/q\). Then

\[
H_m(p)=\frac{r-1}{2-r}\,\frac{2q-p(r/2)^m}{r^m-1}.
\]

The three excluded cases have exact limiting expressions

\[
H_m(1/2)=\frac{1-2^{-(m+1)}}m,\quad
H_m(2/3)=\frac{m+1}{3(2^m-1)},\quad
H_m(1)=2^{-m}.
\]

The full fixed-parameter asymptotic phase diagram as \(m\to\infty\) is

\[
H_m(p)\sim
\begin{cases}
1/m, &p=1/2,\\
\displaystyle\frac{2(1-p)(2p-1)}{2-3p}\left(\frac{1-p}{p}\right)^m,&1/2<p<2/3,\\
\displaystyle \frac m3\,2^{-m},&p=2/3,\\
\displaystyle\frac{p(2p-1)}{3p-2}\,2^{-m},&2/3<p\le1.
\end{cases}
\]

There are two **parameter–depth crossover profiles**. If \(p_m\ge1/2\), \(m(2p_m-1)\to a\in[0,\infty)\), then

\[
mH_m(p_m)\longrightarrow\frac{2a}{e^{2a}-1},
\]

with continuous value \(1\) at \(a=0\). If \(p_m\to2/3\) and \(m\log(p_m/[2(1-p_m)])\to t\in\mathbb R\), then

\[
\frac{3\,2^m}{m}H_m(p_m)\longrightarrow\frac{1-e^{-t}}{t},
\]

with continuous value \(1\) at \(t=0\). These results jointly determine how the closest approach to the neutral fixed point during a completed return excursion changes across the recurrence threshold and the geometric-reinjection resonance.

## Assumptions and scope

At each integer time, independently apply \(x\mapsto2x\pmod1\) with probability \(p\) or \(x\mapsto x/2\) with probability \(q\). Sample \(X_0\) **uniformly on \([1/2,1)\)**, independently of future map choices; this is not the system's stationary distribution. Define the first return \(\tau=\inf\{n\ge1:X_n\in[1/2,1)\}\). Define shell depth \(L(x)=j\) for \(x\in[2^{-(j+1)},2^{-j})\), \(j\in\mathbb Z_{\ge0}\); the boundary \(x=0\) is an event of probability zero in this experiment. Set \(M=\max_{0\le j\le\tau}L(X_j)\). Thus \(M\ge m\) is the event that the trajectory visits \((0,2^{-m})\) **before returning** to the upper half. All probabilities average over both \(X_0\) and the independent map choices. For every \(p\ge1/2\), \(\tau<\infty\) almost surely. The exact formulas concern integer depths \(m\ge1\), not first-return durations or statistics under the invariant measure.

## Proof

**1. Exact shell process and launch distribution.** From shell \(j\ge1\), doubling takes the position into shell \(j-1\); halving takes it into shell \(j+1\), independently of the within-shell location. After the first step out of shell zero, halving has probability \(q\) and sends the state to shell one. Doubling maps the uniform upper-half starting point uniformly onto \([0,1)\), so its subsequent shell is \(j\ge0\) with probability \(2^{-(j+1)}\). Therefore the one-step launch distribution is \(\Pr(L(X_1)=1,\text{halve})=q\) and \(\Pr(L(X_1)=j,\text{double})=p2^{-(j+1)}\) for \(j\ge0\). The depth-zero doubling event terminates the excursion. This is the only use of uniform initial position; the transition probabilities thereafter are position-independent. For \(p\ge1/2\), the nearest-neighbor walk on positive depths with decreasing-step probability \(p\) almost surely visits depth zero, hence the first return is finite.

**2. Finite two-sided hitting problem.** For \(1\le j\le m\), define \(h_j=\Pr_j(T_m<T_0)\) for the nearest-neighbor depth process, with \(h_0=0\) and \(h_m=1\). On \(1\le j<m\), the Markov property yields \(h_j=p h_{j-1}+q h_{j+1}\). Solving the second-order Dirichlet equation gives, for \(p\ne1/2\) and \(q>0\),

\[
h_j=\frac{r^j-1}{r^m-1},\qquad r=\frac pq.
\]

For \(p=1/2\), \(h_j=j/m\); for \(p=1\), \(h_j=0\) when \(j<m\). Any starting shell \(j\ge m\) already meets the target event.

**3. Average over the launch.** The launch probabilities yield the exact finite formula

\[
H_m(p)=q h_1+p\sum_{j=1}^{m-1}2^{-(j+1)}h_j+p2^{-m}.
\tag{1}
\]

The last term is the entire geometric tail of launches to shell \(j\ge m\), and for \(m=1\) the empty sum is zero. Substitute the solution from step 2 into (1). Summing the geometric progressions in \(r/2\) and \(1/2\) gives the stated quotient when \(r\ne1,2\). At \(r=1\), evaluate \(\sum_{j=1}^{m-1}j2^{-(j+1)}\) to obtain \((1-2^{-(m+1)})/m\). At \(r=2\), the progression in \(r/2\) has \(m-1\) constant terms, yielding \((m+1)/[3(2^m-1)]\). At \(p=1\), all departures from depth zero arise from a single doubling image, yielding \(2^{-m}\). The degenerate case \(m=1\) also follows from (1): \(H_1(p)=q+p/2=1-p/2\).

**4. Fixed-parameter asymptotics.** For \(1/2<p<2/3\), \(1<r<2\); the bracket \(2q-p(r/2)^m\) tends to \(2q\), while \(r^m-1\sim r^m\). For \(2/3<p<1\), \(r>2\); the term \(-p(r/2)^m\) dominates the bracket. Simplifying \((r-1)/(2-r)=(2p-1)/(2-3p)\) gives the two exponential constants. At the exceptional parameters use the exact expressions. The \(p=1\) limiting constant equals one.

**5. Double scaling near \(p=1/2\).** Let \(\delta_m=2p_m-1\ge0\) and \(m\delta_m\to a\). Then \(r_m=(1+\delta_m)/(1-\delta_m)\), so \(m\log r_m\to2a\); moreover \(2q_m-p_m(r_m/2)^m\to1\) and \(2-r_m\to1\). For \(a>0\), \(m(r_m-1)\to2a\) proves the stated limit. For \(a=0\), use \((r_m^m-1)/(m(r_m-1))\to1\) (valid also at \(r_m=1\) by continuity), giving limit one.

**6. Double scaling near \(p=2/3\).** Put \(s_m=\log(r_m/2)\), so \(ms_m\to t\). Rewrite the quotient as

\[
\frac{3\,2^m}{m}H_m(p_m)
=\frac{3(r_m-1)}m\,\frac{2q_m e^{-ms_m}-p_m}{(2-r_m)(1-r_m^{-m})}.
\]

When \(t\ne0\), use \(m(2-r_m)\to-2t\), \(2q_m e^{-ms_m}-p_m\to\frac23(e^{-t}-1)\), and \(r_m^{-m}\to0\), obtaining \((1-e^{-t})/t\). When \(t=0\), the same result follows uniformly by factoring the removable quotient \((1-e^{-ms_m})/(m(1-e^{s_m}))\) and taking its continuous limit, or by the exact \(p=2/3\) formula along the zero sequence combined with this uniform factorization. This completes the proof.

## Verification

The standalone `checker.py` constructs a second computation of each tail: it solves the \((m-1)\)-state rational Dirichlet system by exact Gaussian elimination and averages the resulting hitting probabilities over the launch distribution, rather than using the closed-form expression. Running `python checker.py` reports `PASS 112 exact rational comparisons` for eight rational choices of \(p\) (including both exceptional values and the deterministic endpoint) and all \(1\le m\le14\). High-precision evaluations for both parameter–depth crossover profiles at multiple depths agreed with the proved limits; these finite tests corroborate but do not prove the asymptotics.

## Relationship to prior work

Yan, Majumdar, Ruffo, Sato, Beck and Klages (2023) introduced detailed analytical study of this random map's invariant densities, position correlations and anomalous dynamics, with the recurrence transition at \(p=1/2\). Brevitt and Klages (2026), in a generalised open version, derive a countable-state Markov representation and the **first-return-time** generating function. Those ingredients motivate the exact excursion extreme problem, but the first-return-time law alone does not state or directly calculate the maximum dyadic depth, its exact whole distribution, the geometric-reinjection threshold at \(p=2/3\), or the two scaling profiles proved above. No claim is made to priority for the basic gambler's-ruin recurrence, the Markov representation, or the known invariant-density phase transitions.

## Limitations

This theorem uses an upper-half uniform initial distribution, not the stationary one. Its observable is maximum **shell depth**, not duration or a continuous minimum-position density. It treats \(p\ge1/2\) only; below the recurrence threshold an excursion can fail to return and the same definition requires additional conditioning. The sharp two-threshold laws follow from a classical hitting calculation combined with this particular dynamical reinjection distribution, so independent priority checking against older renewal and branching-process treatments remains appropriate. No numerical finite-depth test certifies an infinite-depth asymptotic.

## References

1. J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck, R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269v1 (first posted 2023-08-18); subsequently *Chaos* 34, 023128 (2024).
2. S. Brevitt, R. Klages, *Quasi-stationary and quasi-ergodic distributions in the Pelikan random map*, arXiv:2607.19084v1 (2026), especially Section 2 and first-return-time equation (24).
