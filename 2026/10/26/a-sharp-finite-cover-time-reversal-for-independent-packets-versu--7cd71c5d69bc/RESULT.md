# A sharp finite cover-time reversal for independent packets versus adaptive coupon replacement

## Finding

Fix integers \(n>r\ge1\) and write \(m=n-r\). Start with any \(r\)-element set \(H_1\subseteq[n]\). At each time \(t\ge1\), select a departing element \(e_t\in H_t\) by a possibly randomized policy depending on the complete history up to that time. **Before selecting the incoming label**, choose this departure without observing the incoming label. Independently draw \(x_t\) uniformly from \([n]\setminus H_t\), and set \(H_{t+1}=(H_t\setminus\{e_t\})\cup\{x_t\}\). Let \(T_{\mathrm{rep}}\) be the first positive round by which \(\bigcup_{i=1}^{T_{\mathrm{rep}}}H_i=[n]\).

The entire sequence of discovered-label sets, conditional on \(H_1\), is equal in distribution to that obtained by making independent uniform draws from the initially missing \(m\) labels. Consequently, with \(\tau_m\) the draw count of the ordinary \(m\)-coupon collector,

\[
T_{\mathrm{rep}}\ \stackrel{\mathrm d}{=}\ 1+\tau_m,
\qquad \mathbb E T_{\mathrm{rep}}=1+mH_m,
\qquad \operatorname{Var}(T_{\mathrm{rep}})=m^2H_m^{(2)}-mH_m,
\]
where \(H_m=\sum_{j=1}^m 1/j\), \(H_m^{(2)}=\sum_{j=1}^m 1/j^2\). At every nonnegative integer \(t\), its exact cumulative distribution is
\[
\mathbb P(T_{\mathrm{rep}}\le 1+t)=
\sum_{j=0}^m(-1)^j\binom mj(1-j/m)^t,
\]
with \(0^0\) interpreted as \(1\) in the empty-draw case.

Now let \(T_{\mathrm{iid}}\) be the analogous number of rounds needed when independent uniformly random \(r\)-subsets are drawn in every round, rather than retaining \(r-1\) labels. Conditional on the first iid packet, the number of initially absent labels is also \(m\). For **all** \(n>r\ge1\), the exact sharp comparison is
\[
\begin{cases}
\mathbb E T_{\mathrm{iid}}<\mathbb E T_{\mathrm{rep}}, &2\le r\le n-2,\\
\mathbb E T_{\mathrm{iid}}>\mathbb E T_{\mathrm{rep}}, &r=1\text{ or }r=n-1.
\end{cases}
\]
No equality case occurs. In the interior regime,
\[
\mathbb E T_{\mathrm{iid}}<1+\frac nr H_{n-r}\le \mathbb E T_{\mathrm{rep}}.
\]
The upper-bound inequality is strict even at the small corner \(n=4,r=2\) where the second inequality is equality. An exact formula for the iid mean, valid throughout the domain, is
\[
\mathbb E T_{\mathrm{iid}}=
\sum_{j=1}^{n}(-1)^{j+1}\binom nj
\left[1-\frac{\binom{n-j}{r}}{\binom nr}\right]^{-1},
\]
where \(\binom ar=0\) if \(a<r\).

## Assumptions and scope

The population \([n]\) is finite and labels are distinct. The outgoing label may be chosen adversarially from the entire observed past, may vary with time, and may be randomized, but cannot depend on the incoming draw of the same step. Every incoming draw is uniform over the complement of the **pre-deletion** packet \(H_t\), conditionally independent of the prior history and of the outgoing choice. This is the natural Johnson-graph replacement process when departure is uniform; the theorem holds for a much larger class of adaptive policies. Both cover times count the initial packet as round one. The iid packet draws are independent and each is uniform among the \(\binom nr\) size-\(r\) subsets. The comparison concerns expectations, not a claimed stochastic order of the two complete times.

## Proof

**1. A distributional coupling independent of the eviction policy.** Set \(B=[n]\setminus H_1\), so \(|B|=m\), and let \(C_t=\bigcup_{i=1}^{t+1}H_i\) for \(t\ge0\). Because every \(H_{t+1}\) retains all but one element of \(H_t\),
\[
C_{t+1}=C_t\cup\{x_{t+1}\}.
\]
For any as-yet-unseen label \(a\in B\setminus C_t\), we have \(a\notin H_{t+1}\). Conditioned on the entire past at time \(t+1\), including the outgoing choice, the chance that the next incoming label is \(a\) is precisely \(1/m\). The probability of no new label is therefore \(1-|B\setminus C_t|/m\). These probabilities are exactly the transition probabilities of the discovered-label set for iid uniform draws from \(B\). With the same deterministic initial set \(C_0=H_1\), induction proves equality of the whole discovered-set process, not merely the cover-time marginal. The departure policy disappears from this transition kernel. The usual coupon-collector decomposition into independent geometric waiting times of respective success probabilities \(j/m\), \(1\le j\le m\), proves the mean and variance. Inclusion–exclusion on missing labels gives the displayed cumulative distribution.

**2. A superharmonic covering potential for independent packets.** Work conditional on the first iid packet. Suppose \(k\in\{1,\ldots,m\}\) labels remain unseen before the next independent packet. Its number \(J\) of newly seen labels has the hypergeometric law
\[
\mathbb P(J=j\mid k)=\frac{\binom kj\binom{n-k}{r-j}}{\binom nr},\qquad
\mathbb E[J\mid k]=\frac{rk}{n}.
\]
Define \(V(0)=0\) and \(V(k)=(n/r)H_k\) when \(k\ge1\). For each \(j\) with \(0\le j\le k\),
\[
V(k)-V(k-j)=\frac nr\sum_{i=k-j+1}^{k}\frac1i
\ \ge\ \frac nr\frac jk.
\]
The inequality is strict for \(j\ge2\). Hence the conditional expected potential decrement at each nonabsorbing state is at least
\[
\mathbb E[V(k)-V(k-J)\mid k]
\ge \frac nr\frac{\mathbb E[J\mid k]}k=1.
\]
The iid chain absorbs almost surely with finite mean because, from every nonabsorbing state, the next packet has a uniformly positive chance of including at least one missing label. Summing the drift inequality until absorption, or stopping at a bounded horizon and passing to the limit, gives the expected number \(\sigma\) of **additional** draws after the initial packet as \(\mathbb E\sigma\le V(m)\). If \(r\ge2\) and \(m\ge2\), the **first** additional iid packet contains at least two of the \(m\) unseen labels with positive probability: take two unseen labels and \(r-2\) labels from the initial \(r\) seen labels. Its expected drift is then strictly larger than one. The sum of nonnegative drift excesses is strictly positive; therefore
\[
\mathbb E T_{\mathrm{iid}}=1+\mathbb E\sigma
<1+\frac nr H_m.
\]

**3. Sharp comparison and every boundary.** When \(r,m\ge2\),
\[
\frac nr=1+\frac mr\le m
\quad\Longleftrightarrow\quad
(r-1)(m-1)\ge1.
\]
Combining the strict bound from step 2 with \(\mathbb E T_{\mathrm{rep}}=1+mH_m\) proves the interior direction. When \(r=1\), the iid process is classical collection on \(n\) labels, with mean \(nH_n\); consequently
\[
\mathbb E T_{\mathrm{iid}}-\mathbb E T_{\mathrm{rep}}
=nH_n-[1+(n-1)H_{n-1}]=H_{n-1}>0.
\]
When \(m=1\), the replacement process covers the only missing label in exactly one transition, so \(T_{\mathrm{rep}}=2\). Each subsequent independent packet includes that missing label with probability \(r/n\), yielding
\[
\mathbb E T_{\mathrm{iid}}=1+\frac nr
=2+\frac1r>2.
\]
The overlap of the boundary descriptions at \(n=2,r=1\) is consistent. These exhaust the admissible integer parameters and prove the sharp if-and-only-if statement.

**4. Exact iid formula.** For an arbitrary specified set \(A\) of \(j\) labels, one iid uniform size-\(r\) packet avoids all of \(A\) with probability \(\binom{n-j}{r}/\binom nr\). Independence across rounds and inclusion–exclusion show that the probability the entire population is not yet covered after \(t\) rounds is
\[
\sum_{j=1}^n(-1)^{j+1}\binom nj
\left(\frac{\binom{n-j}{r}}{\binom nr}\right)^t.
\]
Summing over \(t\ge0\) proves the exact mean formula, as all ratios inside the geometric sums are strictly less than one.

## Verification

The standalone standard-library program `verify_coupon_comparison.py` executes exact rational checks. It gives `PASS: 1736 exact occupancy/coupling assertions; 1011 exact expected-time and drift assertions; total 2747.` It enumerates the coverage-state process with multiple history-dependent eviction policies for \(3\le n\le6\), checks coupon-collector occupancy identities, and independently compares the dynamic-programming and inclusion–exclusion iid expectations and strict sign classification for \(2\le n\le16\). It checks the harmonic drift inequalities throughout the tested ranges. The mathematical proof, rather than this finite enumeration, establishes unrestricted integers and adaptive eviction policies. Run `python3 verify_coupon_comparison.py` from the same directory.

## Relationship to prior work

Athreya, Mukherjee and Mukherjee (arXiv:2304.01145, first public 2023-04-03) formulate a Markovian subset-replacement cover-time conjecture (Conjecture 2.4) for collecting all size-\(s\) subsets. Their proved case is \(s=r\) (Theorem 2.5); their independent-packet model has its own asymptotic results. Setting \(s=1\) in their conjectural main term yields \(n\log n\), consistent with the present exact law \(1+(n-r)H_{n-r}\) for fixed \(r\) as \(n\to\infty\). The new structural elements claimed here are the exact distribution under arbitrary nonanticipating departures and the strict **finite** iid-versus-replacement comparison, including the complete boundary reversal. The latter is not inferred solely from their asymptotic slowdown.

Falgas-Ravry, Larsson and Markström (arXiv:1601.04455) treat broad **independent** random-subset coupon collectors, including uniform packets and concentration, but their independent-draw model does not itself entail the adaptive dependent-process law or the finite comparison. Adler and Ross's *The Coupon Subset Collection Problem* (2001), Section 2.3, **already gives the iid uniform-packet inclusion–exclusion mean formula** as its equation (7), crediting an earlier source. The finite formula displayed here is supporting prior machinery, not claimed as a new discovery. That paper's model is explicitly independent packet arrivals; it neither analyzes a Markovian replacement walk nor states the sharp finite comparison. Broader priority remains uncertain. The elementary geometric-waiting decomposition and hypergeometric law are standard; novelty is not claimed for those ingredients individually.

## Limitations

This concerns coverage of individual labels (\(s=1\)), not the general \(s\ge2\) super-coupon conjecture. The comparison is a theorem on expected completion times and does not assert that independent-packet time is stochastically smaller for all sample sizes. Adaptivity is allowed only for the outgoing choice, and the incoming label must be uniform from the pre-deletion complement independently of the outgoing policy. Neither a proof of historical uniqueness nor external independent verification is supplied. General coupon-collector inequalities and earlier subset-collection articles could contain equivalent conclusions.

## References

1. S. Athreya, S. Mukherjee and S. Mukherjee, *On a Generalisation of the Coupon Collector Problem*, arXiv:2304.01145 (first public 2023-04-03), Conjecture 2.4 and Theorem 2.5. https://arxiv.org/abs/2304.01145
2. V. Falgas-Ravry, J. Larsson and K. Markström, *Speed and concentration of the covering time for structured coupon collectors*, arXiv:1601.04455 (first public 2016-01-18). https://arxiv.org/abs/1601.04455
3. I. Adler and S. M. Ross, *The Coupon Subset Collection Problem*, Journal of Applied Probability (2001). https://doi.org/10.1239/jap/1005091036
