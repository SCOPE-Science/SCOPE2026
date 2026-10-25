# Exact ballot dispersion and the competence frontier for clockwise delegation on a cycle

## Finding

**Theorem (one directed-circle delegation model, finite and local-asymptotic laws).** Fix a clockwise directed circle of \(n\ge3\) labeled voters and a direct-voting probability \(q\in(0,1)\). Independently at each vertex, an expert/caster indicator is Bernoulli with parameter \(q\); casters vote directly and every noncaster forwards their entire ballot to the clockwise successor. Ballots are forwarded transitively. A chain ending at a caster is counted with unit weight per represented voter; if all vertices delegate, no ballot is counted. For independent correctness of all caster signals with common probability \(p\in[0,1]\), write \(C_n\) for total **correct represented weight**, \(W_j\) for the weight of caster \(j\) (zero for noncasters), and \(Q_n=\sum_j W_j^2\). Put \(r=1-q\) and
\[
 H(t,z)=(1-p)\frac{t}{1-t}+p\frac{tz}{1-tz}.
\]
Then for every integer \(n\ge3\), with coefficient extraction understood as a formal power series,
\[
 \mathbb E[z^{C_n}]=r^n+\sum_{k=1}^n\frac{n}{k}q^kr^{n-k}[t^n]H(t,z)^k,
\]
and the exact dispersion identity is
\[
 \mathbb E Q_n=n\left(\frac{2-q}{q}-\left(2n-1+\frac2q\right)r^n\right).
\]
These identities include the all-delegating outcome; there \(C_n=Q_n=0\).

Next fix constants \(c_D\ge c_A\ge0\), and, for all sufficiently large \(n\), let a caster's probability of a correct direct signal be \(p_{D,n}=\frac12+c_D/\sqrt n\), while a noncaster's **counterfactual direct-voting** accuracy would be \(p_{A,n}=\frac12+c_A/\sqrt n\). Conditional on the independent caster indicators, all possible direct signals are independent. In liquid democracy only casters' signals are used; in the matched direct-democracy benchmark all \(n\) would vote with their type-specific signals. Both rules choose the correct alternative only on a **strict** majority; a tie and an all-delegation event count as no correct decision.

With \(\Phi\) the standard normal cumulative distribution function, the limiting probabilities are
\[
 \lim_{n\to\infty}P_{\mathrm{LD},n}=\Phi\left(2c_D\sqrt{\frac q{2-q}}\right),\qquad
 \lim_{n\to\infty}P_{\mathrm{direct},n}=\Phi\left(2(qc_D+(1-q)c_A)\right).
\]
Consequently the delegated procedure has strictly higher **limiting** truth-tracking probability if and only if
\[
 c_D\left(\sqrt{\frac q{2-q}}-q\right)>(1-q)c_A.
\]
The reversed inequality gives strictly lower limiting probability. On the equality frontier the limiting probabilities coincide, without an assertion about any finite-size ordering. In particular, for \(q=\frac12\), \(c_D>0\), the favorable region is exactly \(c_A/c_D<2/\sqrt3-1\); if \(c_A=0\), delegated voting wins in the limit for every \(q\in(0,1)\), while if \(c_A=c_D>0\), direct voting wins in the limit for every \(q\in(0,1)\).

## Assumptions and scope

The network is a **fixed, oriented, directed cycle**: every delegator has precisely one allowed successor. Indicators of direct voting are independent across vertices, all with the same fixed probability \(q\); they are independent of other voters' indicators and of signals, conditional on their own type. There is one objectively correct binary alternative. A caster's signal is not recycled as an independent signal for each vote it represents: all represented votes use the same one signal. Every voter supplies one original unit-weight ballot, and forwarding is transitive. The matched direct benchmark uses the very same randomly assigned caster/noncaster types and their counterfactual signal qualities, with no delegation. The local-asymptotic theorem holds for constants \(c_D,c_A\) fixed as \(n\to\infty\), and only for fixed \(q\) strictly between zero and one.

When there is at least one caster, the nonzero guru weights are positive integers summing to \(n\). They are lengths of clockwise runs of delegations ending at each caster. Let \(Z_j\) equal \(+1\) for a correct signal and \(-1\) for an incorrect signal at caster \(j\). Define the weighted margin \(S_n=\sum_{j:W_j>0} W_jZ_j\), with \(S_n=0\) if all delegate. Then the correct decision event is exactly \(S_n>0\).

## Proof

**1. Full finite ballot-count distribution.** Suppose there are \(k\ge1\) direct voters. Listing them in clockwise order, the \(k\) successive positive clockwise gap lengths \(\ell_1,\ldots,\ell_k\) sum to \(n\). Each gap is the weight of the caster at its clockwise endpoint. Conversely, a starting labeled vertex and a positive ordered \(k\)-composition specify a direct-voter configuration with one distinguished caster. Every unmarked configuration with \(k\) casters arises exactly \(k\) times as the distinguished caster ranges over its \(k\) members, so the multiplicity is \(n/k\) per ordered composition. Each direct-indicator configuration has probability \(q^kr^{n-k}\). Conditional on the gaps, independent caster signals contribute \(\prod_{i=1}^k((1-p)+pz^{\ell_i})\) to the probability-generating function of \(C_n\). Summing over all positive compositions yields the coefficient \([t^n]H(t,z)^k\). The sole no-caster pattern has probability \(r^n\), contributes \(C_n=0\), and completes the identity.

**2. Exact dispersion.** Because \(\sum_j W_j^2\) is the number of *ordered pairs of original voters* whose ballots reach the same caster, take two distinct vertices at clockwise distance \(d\in\{1,\ldots,n-1\}\). Their ballots have the same caster if and only if either all \(d\) vertices from the first, inclusive, to the second, exclusive, delegate or all \(n-d\) vertices in the opposite arc delegate, **and** not all \(n\) delegate. The two arc events intersect exactly at the all-delegating pattern. Thus the shared-caster probability is \(r^d+r^{n-d}-2r^n\). A diagonal pair is represented with probability \(1-r^n\). There are \(n\) ordered pairs at each clockwise distance \(d\), giving
\[
 \mathbb E Q_n=n(1-r^n)+n\sum_{d=1}^{n-1}(r^d+r^{n-d}-2r^n)
 =n\left(\frac{2-q}{q}-\left(2n-1+\frac2q\right)r^n\right).
\]
This calculation counts the all-delegating case correctly as zero, unlike a conditional-on-participation variance formula.

**3. Dispersion law and small maximal weight.** Fix \(q\in(0,1)\). Write \(D_i\) for the Bernoulli caster indicator and take circular indices. For \(L=\lceil4\log n/|\log r|\rceil\), a union bound gives probability at most \(nr^L=O(n^{-3})\) of a run of \(L\) consecutive delegating vertices. On its complement every caster's represented weight is at most \(L\), so \(\max_jW_j=O_{\mathbb P}(\log n)=o_{\mathbb P}(\sqrt n)\). Define a truncated weight \(V_{i,L}=D_i(1+\sum_{h=1}^{L}\prod_{a=1}^{h}(1-D_{i-a}))\). When no \(L\)-long run occurs, \(V_{i,L}=W_i\) for every \(i\) (zero-weight noncasters included). The bounded random variables \(V_{i,L}^2\) depend only on \(L+1\) adjacent Bernoulli indicators, each is bounded by \((L+1)^2\), and on the circle each is dependent on at most \(2L\) others. Hence
\[
 \operatorname{Var}\left(\frac1n\sum_i V_{i,L}^2\right)=O(L^5/n)\longrightarrow0.
\]
For \(G\) geometric with \(\Pr(G=g)=qr^{g-1}\), \(g\ge1\), independence implies \(\mathbb E V_{i,L}^2=q\,\mathbb E[\min(G,L+1)^2]\to q\mathbb E G^2=(2-q)/q\). It follows that
\[
 \frac{Q_n}{n}\xrightarrow{\mathbb P}\frac{2-q}{q}.
\]

**4. Conditional central limit theorem.** On the event of at least one caster, \(\sum_jW_j=n\). Conditional on all \(D_i\), the caster signs \(Z_j\) are independent, with common mean \(2c_D/\sqrt n\) and variance \(1-4c_D^2/n\). Thus
\[
 \mathbb E[S_n\mid (D_i)]=2c_D\sqrt n,
 \qquad\operatorname{Var}(S_n\mid(D_i))=(1-4c_D^2/n)Q_n.
\]
The maximal absolute summand in the centered, \(\sqrt n\)-normalized sum is bounded by \(2\max_j W_j/\sqrt n=o_{\mathbb P}(1)\), while its conditional variance converges in probability to \((2-q)/q>0\). Conditional Lindeberg–Feller, followed by bounded convergence for characteristic functions, yields
\[
 S_n/\sqrt n\Longrightarrow N\left(2c_D,\frac{2-q}{q}\right).
\]
The no-caster event has probability \(r^n\to0\), so does not affect this limit. The limiting normal distribution has no atom at zero; therefore strict-majority success tends to \(\Phi(2c_D\sqrt{q/(2-q)})\), and tie probabilities vanish.

**5. Matched direct benchmark and sharp frontier.** Under all-direct voting, each voter has type \(D_i\), Bernoulli \(q\), and independently casts a potential sign of correctness with probability \(1/2+c_D/\sqrt n\) if \(D_i=1\) or \(1/2+c_A/\sqrt n\) otherwise. After averaging over independently chosen types, direct correctness indicators are independent Bernoulli with probability \(1/2+[qc_D+(1-q)c_A]/\sqrt n\). The ordinary triangular-array binomial central limit theorem gives the stated second limit. Since \(\Phi\) is strictly increasing, comparing the two normalized drifts yields the exact strict-inequality frontier. The two stated extreme cases use \(\sqrt{q/(2-q)}>q\) and \(\sqrt{q/(2-q)}<1\) for every \(0<q<1\). \(\square\)

## Verification

The accompanying standard-library-only `verify.py` independently enumerates every binary caster configuration and every independent caster-signal realization and compares their rational probability-generating functions to the cyclic-composition formula, for three rational pairs \((q,p)\) and every \(n=2,\ldots,9\). It also enumerates every represented-weight square sum and checks the exact rational dispersion formula. It reports `PASS: 24 complete rational joint-action-and-signal enumeration instances, n=2..9`. Although the theorem is stated for \(n\ge3\), the code additionally tests the formally valid two-vertex directed reciprocal cycle as a boundary check. Finite enumeration verifies the finite identities at tested parameters only; the asymptotic claims are proved by the uniform run bound, variance estimate and conditional central limit theorem above.

For a concrete asymptotic instance, \(q=1/2\), \(c_D=1\), \(c_A=0\) give the limiting delegated and direct accuracies \(\Phi(2/\sqrt3)\approx0.87589346\) and \(\Phi(1)\approx0.84134475\), a limiting improvement of about \(0.03454871\).

## Relationship to prior work

Berinsky, Halpern, Halpern, Jadbabaie, Mossel, Procaccia and Revel (initial arXiv public submission July 25, 2021) analyze transitive probabilistic delegations and how concentration affects truth tracking, primarily for nonlocal, random-target delegation. Their general framework motivates a *fixed local network* and a quantitative majority-accuracy calculation, but their inspected full text does not present this directed-cycle exact cyclic-composition PGF, exact second moment, or matched local-alternative competence frontier. Becker, D'Angelo, Delfaraz and Gilbert (2021) analyze optimization and hardness of accuracy-maximizing delegations on arbitrary networks, rather than independent Bernoulli forwarding on a ring. Kahng, Mackenzie and Procaccia (2018/2021) study local accuracy advantages when delegations follow more-competent neighbors, excluding directed cycles of delegations. Colley, Delemazure and Gilbert (2023) instead study voting-power indices and algorithms for different network families. Chatterjee, Gilbert, Schmid, Svoboda and Yeo (2025) address variance-related sufficient guarantees for local mechanisms on general classes of graphs, but do not give the ring-specific exact dispersion or this limiting frontier. These are statement/assumption comparisons, not claims that earlier work on delegation or concentration is absent.

A later closely relevant 2026 preprint by Grossi and collaborators studies first-moment *expected voting weights* and their network-centrality characterization for suspendible transitive delegations. Its abstract and secondary description were available, but its primary full text was not accessible for verification; possible additional mathematical overlap is an explicit residual bibliographic risk. Independent publication checks remain necessary.

## Limitations

The exact PGF requires independent direct/delegate decisions and conditionally independent caster correctness indicators. The sharp limit assumes a fixed \(q\), a **one-way** directed cycle, and competence deviations of order \(n^{-1/2}\). It is not a claim for strategic endogenous delegation, bidirectional cycles, arbitrary directed or undirected graphs, correlated source signals, rates \(q\to0\), multiple delegable candidates, or fixed positive competence gaps. On the equal limiting-accuracy frontier no second-order finite-size comparison is asserted. The finite exact formula is not claimed to be the first combinatorial cyclic-composition identity in general; the scientific claim is its application combined with the precise local information-versus-concentration decision threshold. This finding has received no independent mathematical audit or external validation.

## References

- A. Berinsky, D. Halpern, J. Y. Halpern, A. Jadbabaie, E. Mossel, A. D. Procaccia and M. Revel, *Tracking Truth with Liquid Democracy*, arXiv:2107.11868, first submitted 2021-07-25, https://arxiv.org/abs/2107.11868; https://www.cs.cornell.edu/info/people/halpern/papers/liquid1.pdf.
- R. Becker, G. D'Angelo, E. Delfaraz and H. Gilbert, *When Can Liquid Democracy Unveil the Truth?*, arXiv:2104.01828, first submitted 2021-04-05, https://arxiv.org/pdf/2104.01828.
- A. Kahng, S. Mackenzie and A. D. Procaccia, *Liquid Democracy: An Algorithmic Perspective*, 2018 preprint and later journal/conference version, https://cdn.aaai.org/ojs/11468/11468-13-14996-1-2-20201228.pdf.
- R. Colley, T. Delemazure and H. Gilbert, *Measuring a Priori Voting Power—Taking Delegations Seriously*, arXiv:2301.02462, https://arxiv.org/pdf/2301.02462.
- K. Chatterjee, S. Gilbert, S. Schmid, J. Svoboda and M. Yeo, *When is Liquid Democracy Possible? On the Manipulation of Variance*, PODC 2025, doi:10.1145/3732772.3733544, https://research-explorer.ista.ac.at/download/20053/20122/2025_PODC_Chatterjee.pdf.
- D. Grossi, A. Nitsche, G. Papasotiropoulos, O. Skibski, P. Skowron and T. Wąs, *Power in Liquid Democracy: A Network Centrality Approach*, arXiv:2608.13188, first submitted 2026-08-13, https://arxiv.org/abs/2608.13188 (primary full text not accessed).
