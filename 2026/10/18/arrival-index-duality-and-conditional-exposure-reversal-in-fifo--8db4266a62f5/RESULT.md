# Arrival-index duality and conditional exposure reversal in FIFO queues

## Finding

Consider a stationary, stable, first-come-first-served single-server queue indexed by customer number. Let \(A_i\) and \(D_i\) be its arrival and departure epochs, with strictly increasing arrivals and nondecreasing departures, and fix an overlap-duration threshold \(\ell\geq0\). Write \(B_i(\ell)\) for the number of earlier customers whose overlap with customer \(i\) lasts strictly longer than \(\ell\), and \(F_i(\ell)\) for the analogous number of later customers. For every customer index \(i\) and every integer \(k\geq1\), the following **pathwise** equivalence holds:

\[
\mathbf 1_{\{B_i(\ell)\geq k\}}=\mathbf 1_{\{F_{i-k}(\ell)\geq k\}}.
\]

Consequently, under stationarity in customer index, \(B_0(\ell)\) and \(F_0(\ell)\) have the same distribution for every \(\ell\). With independent Bernoulli infection labels of probability \(p\), the probabilities that a tagged susceptible customer is exposed to at least one infectious earlier or later customer are equal. For every deterministic finite index window and every \(k\), the two empirical exceedance frequencies differ by at most \(k\) observations, without requiring probabilistic assumptions.

In a stationary \(GI/GI/1\) queue with independent renewal interarrival times, independent service times, independent infection labels, and a **fixed** threshold, earlier- and later-customer infection events are independent *conditional on the tagged customer's sojourn time*. Nevertheless, conditional identical distribution is false in general, with a full conditional risk reversal in the following natural specialization.

In the \(M/D/1\) queue, take unit deterministic service time, Poisson arrival rate \(0<\lambda<1\), infection prevalence \(0<p<1\), and threshold \(0<\ell<1\). Let \(T\) be the tagged customer's sojourn time, and for \(t>1\) put

\[
b_\ell(t)=\lfloor t-1\rfloor+\mathbf1_{\{\{t-1\}>\ell\}},
\]

where \(\{x\}\) means the fractional part of \(x\); set \(b_\ell(1)=0\). Outside the null set of integer \(t>1\), the exact conditional infection risks are

\[
\Pr(I_-\mid T=t)=1-(1-p)^{b_\ell(t)},\qquad
\Pr(I_+\mid T=t)=1-e^{-\lambda p(t-\ell)}.
\]

For \(1\leq t<1+\ell\), the first risk is zero and the second strictly positive. Put \(a=-\log(1-p)\). For every

\[
t>\frac{2a-\lambda p\ell}{a-\lambda p},
\]

the first risk is strictly larger than the second. These opposite inequalities occur on sojourn-time sets of positive probability. Yet their unconditional probabilities coincide and are given exactly by

\[
\boxed{\Pr(I_-)=\Pr(I_+)
=1-e^{-\lambda p(1-\ell)}\frac{(1-\lambda)p}{p-1+e^{-\lambda p}}.}
\]

This gives a precise resolution of the two different symmetry assertions in Conjecture 3.10 of Newman--Pender (2026): unconditional symmetry holds throughout stationary FIFO queues, and conditional independence holds for renewal input with independent marks, but conditional identical distribution fails even for deterministic service times. It also supplies an exact, not approximate, one-sided exposure formula for the deterministic-service model.

## Assumptions and scope

A stationary arrival-indexed FIFO queue means that the **relative-time array** \((A_{j+k}-A_j,D_{j+k}-A_j)_{k\in\mathbb Z}\) has a law independent of the reference index \(j\); uncentered absolute arrival epochs are not stationary. Departures are in arrival order and satisfy \(D_i\geq A_i\), with finite sojourn times almost surely. Arrival epochs are strictly ordered, with no simultaneous arrivals; simultaneous departures may be allowed provided the overlap condition is strict. Overlap between \(i<j\) is \((D_i-A_j)_+\). The rank identity does not require independent arrival or service processes, and even holds along each deterministic sample path.

For the conditional-independence statement, the inputs are a two-sided iid sequence of positive interarrival times, an independent iid service sequence, and iid infection labels independent of both. The queue is stable and in its stationary Loynes regime. The tagged customer is conditioned susceptible. No secondary transmission occurs and the overlap threshold is fixed, not shared randomly across contacts.

For the explicit specialization, unit deterministic service and \(0<\lambda<1\) ensure a stationary \(M/D/1\) queue. The threshold range is strictly \(0<\ell<1\), and infection prevalence is \(0<p<1\). All strict comparisons are understood for almost every sojourn time under its law. The atom at \(T=1\) is included explicitly.

## Proof

**1. Pathwise rank identity.** Fix any \(i\) and \(k\geq1\). Since departures are in customer order, at least \(k\) earlier customers remain overlapping with \(i\) for more than \(\ell\) exactly when customer \(i-k\) does:

\[
B_i(\ell)\geq k\iff D_{i-k}>A_i+\ell.
\]

Similarly, since arrivals are in customer order,

\[
F_{i-k}(\ell)\geq k\iff A_i<D_{i-k}-\ell.
\]

These events are identical. Arrival-index stationarity and translation by \(k\) imply \(\Pr(B_0\geq k)=\Pr(F_0\geq k)\) for every \(k\); equality of the full nonnegative-integer distributions follows. For any window \(1\leq i\leq N\), summing the indicator identity and shifting the index yields

\[
\sum_{i=1}^N\bigl(\mathbf1_{\{B_i\geq k\}}-\mathbf1_{\{F_i\geq k\}}\bigr)
=\sum_{i=1-k}^0\mathbf1_{\{F_i\geq k\}}
-\sum_{i=N-k+1}^N\mathbf1_{\{F_i\geq k\}},
\]

whose absolute value is at most \(k\). Conditional on the unmarked queue, the chance of having no infectious earlier customer is \((1-p)^{B_i}\), and similarly later is \((1-p)^{F_i}\). The distributional equality therefore yields equality of the two unconditional infection risks for every \(p\in[0,1]\).

**2. Conditional independence.** In the stationary \(GI/GI/1\) construction, the tagged sojourn \(T\), the older-customer overlap events, and older labels are measurable with respect to the past arrivals, past services and tagged service. Future interarrival increments and future labels are independent of this information. Given \(T\), the later-customer infection event depends only on \(T\), future increments and future labels. Conditional factorization of bounded test functions proves \(I_-\perp I_+\mid T\). No conditional identity in distribution has been assumed or used.

**3. Exact conditional \(M/D/1\) risks.** Let \(W=T-1\) be the stationary workload seen upon arrival. At \(W=0\), no preceding customer is in the queue. When \(W>0\), write \(W=m+r\) where \(m=\lfloor W\rfloor\) and \(0<r<1\). In an \(M/D/1\) queue, there are exactly \(m+1\) existing customers: one has remaining service time \(r\) and the other \(m\) have one unit each. Their departure offsets from the tagged arrival are \(r,r+1,\ldots,r+m\). Because \(0<\ell<1\), exactly \(m+\mathbf1_{\{r>\ell\}}\) earlier customers overlap longer than \(\ell\). The integer exceptions have probability zero for \(W>0\). Independent Bernoulli labels give the first conditional risk.

Future arrivals form a rate-\(\lambda\) Poisson process independent of \(W\). A future customer overlaps longer than \(\ell\) precisely when it arrives within \((T-\ell)\) time units of the tagged arrival. Independently marking infectious arrivals with probability \(p\) makes their number Poisson with mean \(\lambda p(T-\ell)\), giving the second conditional risk.

For \(1\leq t<1+\ell\), \(b_\ell(t)=0\), whereas \(t-\ell>0\), so the later-customer risk strictly dominates. For large \(t\), \(b_\ell(t)\geq t-2\). Set \(a=-\log(1-p)>p>\lambda p\). Whenever \((a-\lambda p)t>2a-\lambda p\ell\), we have \(a b_\ell(t)>\lambda p(t-\ell)\), so \(e^{-a b_\ell(t)}<e^{-\lambda p(t-\ell)}\) and the earlier-customer risk dominates. The stationary \(M/D/1\) waiting-time distribution has positive probability on every nonempty interval within \((0,\infty)\) (this follows, for example, from positive-probability Poisson arrival patterns during an initially isolated service period and subsequently during finite busy stretches). Hence both regimes occur on positive-probability sojourn-time sets; the first also includes the atom \(\Pr(T=1)=1-\lambda\).

**4. Unconditional exact formula without a conjectural joint approximation.** The stationary workload transform follows directly from the piecewise-deterministic workload generator applied to \(f(v)=e^{-sv}\): for \(s>0\),

\[
0=s\left(\mathbb E e^{-sW}-(1-\lambda)\right)
+\lambda(e^{-s}-1)\mathbb E e^{-sW}.
\]

Here the stationary empty probability is \(1-\lambda\). Consequently

\[
\mathbb E e^{-sW}=\frac{(1-\lambda)s}{s-\lambda+\lambda e^{-s}}.
\]

With \(s=\lambda p\), conditional Poisson thinning yields

\[
\Pr(I_+)=1-e^{-s(1-\ell)}\mathbb E e^{-sW}
=1-e^{-\lambda p(1-\ell)}\frac{(1-\lambda)p}{p-1+e^{-\lambda p}}.
\]

The pathwise rank identity establishes the exact same value for \(\Pr(I_-)\), completing the proof.

## Verification

The companion standalone program `verify.py` reconstructs queue departures on finite sample paths, checks the deterministic rank identity for all customer pairs at several rational thresholds, checks its finite-window boundary formula, and evaluates the exact \(M/D/1\) conditional-risk expressions and their strict reversal at representative rational parameters. It additionally simulates independent Poisson arrival sequences solely as a sanity check of the closed-form *unconditional* risk. The proof above, not finite enumeration or Monte Carlo, establishes all quantified statements.

To reproduce, run `python3 verify.py` with Python 3 and NumPy installed. All random draws use a fixed seed; simulation comparisons use tolerances substantially above their anticipated sampling fluctuations.

## Relationship to prior work

Newman and Pender (2026), arXiv:2610.09019, Conjecture 3.10, explicitly conjecture equal before- and after-arrival infection probabilities throughout first-come-first-served \(G/G/1\) systems and conditional independence and identical distribution given the tagged sojourn. Their Theorems 3.4, 3.9 and 3.14 establish the relevant statements in \(M/M/1\), and Section 5.3 treats \(M/G/1\) total infection risk by an approximation. The present result determines exactly which pieces extend, gives a positive-measure counterexample to conditional identical distribution, and obtains an exact \(M/D/1\) directional formula.

Boxma and Pender (2025), *Overlap times in the G/G/1 queue via Laplace transforms*, Eq. (1) and Proposition 2.1, supply the pairwise overlap formula and a maximum-overlap representation. In particular their neighboring-customer formula, together with stationarity, implies equality of the **unmarked largest** overlap from each direction. The rank-by-rank pathwise identity is an elementary consequence of FIFO ordering and stationary indexing, not a new queueing transform. The claimed contribution is its explicit use to resolve the marked directional-exposure conjecture and its **simultaneous sharp conditional boundary**; no novelty is claimed for the pairwise overlap formula itself.

Boxma, Pender and Yechiali (2025), *The Number of Overlapping Customers in Priority Queues*, study the joint total overlap counts for priority disciplines, not the stated stationary FIFO rank shift or the deterministic-service conditional risk reversal. Their expected-count relations and general queueing identities are compatible with the result.

## Limitations

The marginal symmetry requires arrival-index stationarity when formulated probabilistically, and a nonovertaking/FIFO ordering. It need not hold for nonstationary tagged arrivals or overtaking service disciplines. Conditional independence requires future renewal increments, independent labels, and a fixed threshold; common random susceptibility thresholds can introduce dependence even when the queue is renewal. The explicit risk formula and sign reversal are proved only for unit deterministic service, Poisson arrivals, \(0<\lambda<1\), \(0<p<1\), and \(0<\ell<1\). We do not claim a unique crossing of the conditional risks; staircase discontinuities can cause additional crossings. We do not establish the total (two-sided union) infection probability in closed form. Independent priority determination is outside the mathematical statements proved here.

## References

1. Laurel Newman and Jamol Pender, *When Lines Become Contagious: Analyzing the Spread of Infection in the M/M/1 Queue*, arXiv:2610.09019v1 (first submitted 2026-10-06), https://arxiv.org/html/2610.09019v1 ; especially Conjecture 3.10 and Section 5.3.
2. Onno Boxma and Jamol Pender, *Overlap times in the G/G/1 queue via Laplace transforms*, Queueing Systems 109 (2025), article 10, DOI:10.1007/s11134-025-09938-1, https://d-nb.info/1367194253/34 ; especially Eq. (1) and Proposition 2.1.
3. Onno Boxma, Jamol Pender, and Uri Yechiali, *The Number of Overlapping Customers in Priority Queues* (2025), https://www.eurandom.tue.nl/wp-content/uploads/2025/05/Priority_Overlap-14.pdf ; especially Sections 3 and 5.
