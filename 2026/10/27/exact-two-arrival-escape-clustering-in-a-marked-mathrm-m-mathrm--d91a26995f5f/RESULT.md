# Exact two-arrival escape clustering in a marked \(\mathrm{M}/\mathrm{M}/1\) queue

## Finding

Consider the stationary first-come-first-served \(\mathrm{M}/\mathrm{M}/1\) infection queue described below. Let \(0<\rho=\lambda/\mu<1\), and let \(0<p<1\) be the independent probability that an arrival is originally infectious. Choose two *consecutive arrivals in the complete arrival stream* and condition on both being originally susceptible. Let \(E_0,E_1\) be their indicators of leaving the queue without having overlapped with any originally infectious customer for a positive duration.

**Theorem (complete adjacent-pair escape law).** For every \(\lambda>0\), \(\mu>\lambda\), and \(0<p<1\), under the foregoing conditioning, both marginal escape probabilities equal
\[
 s:=\Pr(E_0=1)=\Pr(E_1=1)
 =\frac{(1-\rho)(1+2p\rho)}{(1+p\rho)(1-\rho+2p\rho)}.
\]
Their joint escape probability is
\[
 j:=\Pr(E_0=E_1=1)
 =\frac{(1-\rho)(1+2p\rho)}{(1+p\rho)^2(1-\rho+2p\rho)}
 =\frac{s}{1+p\rho}.
\]
In particular the complete ordered \(2\times2\) distribution has cell probabilities \(j,s-j,s-j,1-2s+j\) for \((E_0,E_1)=(1,1),(1,0),(0,1),(0,0)\), respectively. Their escape indicators—and likewise their infection indicators—have strictly positive covariance
\[
 \operatorname{Cov}(E_0,E_1)
 =\frac{2p\rho^2(1-\rho)(1+2p\rho)}
 {(1+p\rho)^2(1-\rho+2p\rho)^2}>0
\]
and the simple exact Pearson correlation
\[
 \boxed{\operatorname{Corr}(E_0,E_1)
 =\frac{2\rho}{1+\rho+2p\rho}.}
\]
Equivalently,
\[
 \Pr(E_1=1\mid E_0=1)=\frac{1}{1+p\rho}.
\]
The number of infections within this conditioned pair, \(Z=2-E_0-E_1\), consequently satisfies
\[
 \operatorname{Var}(Z)=2s(1-s)\left(1+\frac{2\rho}{1+\rho+2p\rho}\right).
\]
Treating the two infection outcomes as independent at their correct marginals underestimates the pair-count variance by the exact multiplicative factor in parentheses.

The two conditional escape indicators are not independent for any interior parameters. In the heavy-traffic limit, with fixed \(0<p<1\), their common marginal escape probability tends to zero while
\[
 \lim_{\rho\uparrow1}\Pr(E_1=1\mid E_0=1)
 =\lim_{\rho\uparrow1}\operatorname{Corr}(E_0,E_1)
 =\frac1{1+p}.
\]
Thus the rare escapes of neighbouring susceptible customers retain a nonzero clustering strength as utilization approaches one.

## Assumptions and scope

The queue has stationary Poisson arrivals with intensity \(\lambda\), independent exponential service requirements with rate \(\mu\), infinitely many waiting places, and a first-come-first-served single server. A customer arrives with an independent infectious mark of probability \(p\); the arrival and service processes do not depend on marks. An originally susceptible customer acquires an infection whenever it shares strictly positive time in the system with at least one *originally* infectious customer. Customers newly infected while queued do not transmit onward in this model. The zero overlap threshold is the instantaneous-exposure boundary of the strictly positive exposure-time threshold model: almost surely overlapping visits have positive duration, and contacts only at departure/arrival instants have probability zero.

The consecutive arrival-index pair is conditioned on the *two original marks* being susceptible, not on the pair being the next two susceptible arrivals after skipping other customers. These original marks are independent of the queue history, so the conditioning does not change the distribution of queue length, interarrival times or service times. Probabilities throughout the theorem are conditional on this two-mark event. The result makes no assertion for strictly positive exposure thresholds, dependence of original marks, service disciplines other than FCFS, or secondary onward infectiousness.

## Proof

Set \(u=1-p\), and define three factors
\[
 a=\frac{\mu}{\mu+\lambda p}=\frac1{1+\rho p},\qquad
 d=\frac{\mu}{\lambda+\mu}=\frac1{1+\rho},\qquad
 b=\frac{\lambda}{\lambda+\mu}=\frac\rho{1+\rho}.
\]
All infinite series below converge absolutely because \(0<\rho u<1\). By PASTA, the number \(Q\) in the system immediately before the first tagged arrival has
\(\Pr(Q=q)=(1-\rho)\rho^q\) for integers \(q\ge0\). Old marks are independently noninfectious with probability \(u\). Given \(Q=q\), the first tagged customer's sojourn time \(D\) has an Erlang distribution with \(q+1\) exponential stages of rate \(\mu\), by service memorylessness.

**First tagged marginal.** Write \(T\) for the time to the *next* arrival, independently \(\operatorname{Exp}(\lambda)\). That arrival is the other tagged susceptible. Subsequent arrival marks are independent. For \(D=t\), thinning of the later arrival stream gives the factor \(e^{-\lambda p(t-T)_+}\) for avoiding infectious arrivals before the first tagged departure. Direct integration against the exponential law of \(T\) yields
\[
 \mathbb E[e^{-\lambda p(t-T)_+}]
 =\frac{e^{-\lambda pt}-p e^{-\lambda t}}{1-p}.
\]
Old customers must also all be noninfectious. Consequently the first marginal is
\[
 s_0=\frac{1-\rho}{1-p}
 \left(\frac a{1-\rho ua}-\frac{p d}{1-\rho ud}\right).
 \tag{1}
\]
This identity is valid for every interior parameter; its denominators are strictly positive.

**Second tagged marginal.** By stationarity and PASTA, the number \(Q_1\) present just before the next arrival again has the geometric marginal law \((1-\rho)\rho^q\). If \(Q_1=q\ge1\), the first tagged customer must be the last of these \(q\) predecessors: FCFS and absence of intervening arrivals force that ordering. Since the first tag is known noninfectious, the remaining \(q-1\) predecessors must be noninfectious for the second tagged customer to escape. If \(Q_1=0\), no predecessor is present. Given \(Q_1=q\), the second customer's future sojourn is Erlang with \(q+1\) memoryless service stages; the absence of later originally infectious arrivals contributes the factor \(a^{q+1}\). Hence
\[
 s_1=(1-\rho)\left(a+\sum_{q=1}^{\infty}
 \rho^q u^{q-1}a^{q+1}\right)
 =(1-\rho)\left(a+\frac{\rho a^2}{1-\rho ua}\right).
 \tag{2}
\]
Elementary rational simplification of (1) and (2) gives the claimed common value \(s_0=s_1=s\).

**Joint escape.** Since the arrivals are consecutive, no other customer arrives between them. The union of the two tagged customers' contacts with other customers consists exactly of (i) all \(Q\) pre-first customers and (ii) arrivals strictly after the second tagged arrival but before the second tagged departure. The second tagged customer's conditional sojourn transform is \(a^{Q_1+1}\). Therefore
\[
 j=\mathbb E[u^Q a^{Q_1+1}]. \tag{3}
\]
For a direct two-arrival embedded-chain calculation, keep independent Poisson arrival and potential service-completion clocks running with intensities \(\lambda\) and \(\mu\). Before the next arrival, the number \(G\) of potential completions has the geometric distribution \(\Pr(G=g)=b d^g\) for \(g\ge0\), independent of \(Q\). Potential events after the queue empties do not change the actual queue. Because the first tagged customer is immediately behind its \(q\) predecessors,
\[
 Q_1=(Q+1-G)_+.
\]
Thus, for every \(z\in[0,1]\) and integer \(q\ge0\),
\[
 \mathbb E[z^{Q_1}\mid Q=q]
 =b\sum_{g=0}^{q}d^g z^{q+1-g}+d^{q+1}.
\]
Multiply by \((1-\rho)(\rho u)^q\), sum over \(q\), and rearrange the nonnegative double geometric series:
\[
 H(z):=\mathbb E[u^Qz^{Q_1}]
 =\frac{1-\rho}{1-\rho ud}
 \left(d+\frac{bz}{1-\rho uz}\right). \tag{4}
\]
Inserting \(z=a\) into (4), then using (3), gives
\[
 j=\frac{(1-\rho)a}{1-\rho ud}
 \left(d+\frac{ba}{1-\rho ua}\right)
 =\frac{(1-\rho)(1+2p\rho)}
 {(1+p\rho)^2(1-\rho+2p\rho)}.
\]
This is the claimed joint probability and equals \(s/(1+p\rho)\).

**Dependence.** A direct subtraction gives
\[
 j-s^2=\frac{2p\rho^2(1-\rho)(1+2p\rho)}
 {(1+p\rho)^2(1-\rho+2p\rho)^2}.
\]
Moreover,
\[
 1-s=\frac{p\rho(1+\rho+2p\rho)}
 {(1+p\rho)(1-\rho+2p\rho)}.
\]
Dividing the positive covariance by \(s(1-s)\) yields the exact correlation. Replacing \(E_i\) by \(1-E_i\) leaves covariance and correlation unchanged. Finally take \(\rho\uparrow1\) in the displayed rational expressions to obtain the heavy-traffic statements. This establishes every asserted formula.

## Verification

Run `python3 verification.py` from this document's directory. The file `verification_output.txt` records the replay. The script executes 840 exact rational assertions over an interior parameter grid, including two independent marginal decompositions, the joint two-arrival geometric-clock transform, positive cell probabilities, exact covariance and correlation, and nonnegative partial-sum bounds for the infinite joint transform. It also performs three seeded forward queue-path Monte Carlo checks, using no third-party dependencies. The finite assertions are corroborative only: the proof above establishes the unrestricted parameter range and infinite geometric sums. The simulation uses independent arrival and service streams and customer infection marks, not merely the target rational formulas.

## Relationship to prior work

Newman and Pender (arXiv:2610.09019v1, first publicly submitted 2026-10-06) introduced the present labelled \(\mathrm{M}/\mathrm{M}/1\) infection model and derived single-susceptible infection probabilities and infectious-customer transmission-count moments for their exposure thresholds. Their one-susceptible zero-threshold escape formula is \((1-\rho)/(1-\rho+2p\rho)\); it differs from the present marginal because *both adjacent original marks* are conditioned susceptible. The present bivariate probability and covariance cannot be deduced merely from a one-tag marginal.

Boxma and Pender, *The Overlapping Time Distribution in the M/M/1 Queue* (DOI:10.1017/jpr.2026.10107), derive a joint transform of infectious-overlap times **before and after one tagged arrival** (their Theorem 4), rather than the joint infection/escape status of **two different successive tagged arrivals**. Palomo and Pender, *The Maximum Overlap Time in the M/M/1 Queue* (arXiv:2311.04387), quantify overlap durations of adjacent customers but do not combine all overlapping originally infectious predecessors and successors to obtain the present pairwise escape law. Kang et al. (arXiv:2103.13441) introduced general service-facility infection-overlap risk measures, without the exact two-mark-conditioned finite-queue distribution here. These sources motivate the natural bivariate question; the present statement is a separate joint-distribution calculation, not a claim to introduce marked queues or queue overlaps.

## Limitations

Only instantaneous-contact infection (zero exposure-time threshold) is treated; no assertion extends to positive required overlap time. Both customers must be consecutive in *all* arrivals and their original marks must be susceptible. There is no infectiousness acquired within the queue, no feedback into service or arrival processes, no general service-time law, and no assertion about nonstationary queues or wider-lag correlations. The finite calculation and simulation are not exhaustive mathematical certification. Although the primary articles and several adjacent-overlap sources were compared at statement and argument level, a historical equivalent formula for paired marked-customer coverage may exist outside the inspected literature; originality has not been independently audited.

## References

1. L. Newman and J. Pender, *When Lines Become Contagious: Analyzing the Spread of Infection in the M/M/1 Queue*, arXiv:2610.09019v1 (first publicly submitted 2026-10-06), https://arxiv.org/html/2610.09019v1.
2. O. Boxma and J. Pender, *The Overlapping Time Distribution in the M/M/1 Queue*, Journal of Applied Probability, DOI:10.1017/jpr.2026.10107, https://doi.org/10.1017/jpr.2026.10107.
3. S. Palomo and J. Pender, *The Maximum Overlap Time in the M/M/1 Queue*, arXiv:2311.04387v1 (2023), https://arxiv.org/abs/2311.04387.
4. K. Kang, S. Doroudi, M. Delasay, and A. Wickeham, *A Queueing-Theoretic Framework for Evaluating Transmission Risks in Service Facilities During a Pandemic*, arXiv:2103.13441 (2021), https://arxiv.org/abs/2103.13441.
