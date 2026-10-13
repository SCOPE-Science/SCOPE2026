# Sharp coextinction-variance minimizers in two-partner ecological networks

## Finding

**Theorem (exact variance minimizers and equality classes).** Fix integers \(n\ge4\) and \(\lceil n/2\rceil\le m\le\binom n2\). Consider every binary bipartite ecological interaction network with \(n\) primary species and \(m\) secondary species, no isolated primary species, and exactly **two distinct** primary partners for each secondary species. A secondary species is lost precisely when *both* its partners become extinct. Networks may have different secondary species with the same pair of partners.

Represent each secondary species by an edge in a loopless multigraph \(G\) on the \(n\) labeled primary species. Let \(d_v\) be the primary degrees (counted with multiplicity), let \(\mu_{uv}\) be the number of secondary species using the same unordered partner pair \(\{u,v\}\), and set
\[
 W(G)=\sum_v\binom{d_v}{2},\qquad D(G)=\sum_{u<v}\binom{\mu_{uv}}{2}.
\]
Write \(2m=nr+s\), where \(0\le s<n\), and set
\[
 W_*= (n-s)\binom r2+s\binom{r+1}{2}.
\]

If exactly \(h\) primary species become extinct, chosen uniformly among all \(h\)-subsets, define \(t_j=\binom{n-j}{h-j}/\binom nh\) for \(j=2,3,4\), with \(t_j=0\) whenever \(h<j\). For the secondary-extinction count \(X_h\), the sharp minimum of the variance across *all* these networks is
\[
 \boxed{V_*(h)=m t_2(1-t_2)+m(m-1)(t_4-t_2^2)+2(t_3-t_4)W_*.}
\]
The exact nonnegative excess above this minimum is
\[
\boxed{\operatorname{Var}(X_h)-V_*(h)=2(t_3-t_4)(W(G)-W_*)+2(t_2-2t_3+t_4)D(G).}
\]
The complete equality classification is: every network is optimal for \(h=0,1,n\); for \(h=2\), exactly those with no repeated partner pair are optimal; for \(3\le h\le n-2\), exactly those with no repeated partner pair **and** all primary degrees in \(\{r,r+1\}\) are optimal; for \(h=n-1\), exactly those with primary degrees in \(\{r,r+1\}\) are optimal, even if some partner pairs repeat. An interval with lower bound larger than upper bound is empty.

For independent primary extinctions with common probability \(q\in(0,1)\), the same networks with distinct partner pairs and primary degrees in \(\{r,r+1\}\) simultaneously and *exactly* minimize secondary-extinction variance for every \(q\). The sharp variance and gap are
\[
\begin{aligned}
 V_*(q)&=m q^2(1-q^2)+2q^3(1-q)W_*,\\
 \operatorname{Var}(X_q)-V_*(q)&=2q^3(1-q)(W(G)-W_*)+2q^2(1-q)^2D(G).
\end{aligned}
\]
In either extinction model the expectation is independent of network topology: \(\mathbb E X_h=mt_2\) and \(\mathbb E X_q=mq^2\). Thus the theorem compares genuine *uncertainty* while holding mean secondary loss fixed.

## Assumptions and scope

Every interaction is binary and unweighted, every secondary species has exactly two distinct primary partners, all primary species appear in at least one interaction, and secondary species are distinct even when their two partner sets are equal. The regime \(\lceil n/2\rceil\le m\le\binom n2\) guarantees both feasibility with no isolated primary species and the existence of a simple \(m\)-edge interaction graph. Primary losses are either a uniform exact-size subset or independent and identically distributed Bernoulli losses; secondary extinction requires the loss of both original partners and involves no rewiring, rescue, or higher-order cascade.

## Proof

For each secondary species \(e\), let \(I_e\) be the indicator that its two partners have disappeared. The indicator has mean \(t_2\) in the fixed-size model. For distinct secondary species \(e,f\), their four partner occurrences can involve four different primary species, three different species if the partner sets meet in exactly one primary, or two different species if the sets coincide. Consequently \(\mathbb E[I_eI_f]\) is respectively \(t_4,t_3,t_2\). There are \(D(G)\) pairs of secondary species with identical partner sets. Every pair sharing both primary species contributes twice to the primary-degree wedge count \(W(G)\), so there are \(W(G)-2D(G)\) pairs sharing exactly one primary and \(\binom m2-W(G)+D(G)\) disjoint pairs. Expanding \(\operatorname{Var}(\sum_e I_e)\) therefore gives
\[
 \operatorname{Var}(X_h)=m t_2(1-t_2)+m(m-1)(t_4-t_2^2)
 +2(t_3-t_4)W(G)+2(t_2-2t_3+t_4)D(G).
\]

The two structural coefficients have the direct nonnegative forms
\[
 t_3-t_4=\frac{(h)_3(n-h)}{(n)_4},\qquad
 t_2-2t_3+t_4=\frac{(h)_2(n-h)_2}{(n)_4},
\]
where \((z)_j=z(z-1)\cdots(z-j+1)\). They count, respectively, the events that three specified primary species disappear but a fourth survives, and that two specified species disappear while two specified others survive. The first is positive precisely at \(3\le h\le n-1\); the second precisely at \(2\le h\le n-2\).

The degree sum is \(\sum_v d_v=2m\). Since \(\binom d2\) is discretely strictly convex, transferring one unit from a degree at least two larger than another strictly decreases the sum of degree binomial coefficients. Hence \(W(G)\ge W_*\), and equality occurs exactly when the degrees are all \(r\) or \(r+1\). Moreover, \(D(G)\ge0\), with equality exactly when all secondary partner sets are distinct.

Both lower bounds are achievable simultaneously within the permitted domain. Begin with any simple graph with \(m\) edges on \(n\) vertices. If its maximum and minimum degrees differ by at least two, choose vertices \(u,v\) with \(d_u\ge d_v+2\). A neighbor \(w\ne v\) of \(u\) must exist that is not a neighbor of \(v\), for otherwise \(d_u\le d_v+1\). Replace edge \(uw\) by \(vw\). This keeps the graph simple, preserves \(m\), and strictly reduces \(\sum_v d_v^2\). After finitely many steps all degrees differ by at most one. Because \(2m\ge n\), their minimum is at least one, so no primary species is isolated. This simple almost-regular graph has \(W=W_*\) and \(D=0\), proving sharpness.

The displayed coefficient positivity immediately yields the equality cases at each \(h\), including the three deterministic sampling sizes. In the independent model, each partner-set event has probability \(q^{j}\) when its union contains \(j\) distinct species, so substitution \(t_j=q^j\) gives the independent-model formulas. Both structural coefficients \(q^3(1-q)\) and \(q^2(1-q)^2\) are strictly positive for \(0<q<1\), proving simultaneous sharpness and its equality characterization. This completes the proof.

## Verification

The supplied standard-library Python checker `verify_degree_two_extinction.py` directly enumerates secondary-extinction counts over every primary-survivor subset and compares exact rational variances with the formulas. It exhaustively tests \(7{,}132\) loopless multigraph profiles (with small \(n,m\)) and \(1{,}362{,}496\) exact event contributions, tests the predicted equality classes at every fixed subset size, and independently checks independent extinction at \(q\in\{1/4,1/2,3/4\}\). Its successful output is `VERIFY_OK profiles=7132 exact_event_contributions=1362496 equality_cases=25081`. These finite computations corroborate but do not replace the unrestricted algebraic argument.

For a concrete **connected** example with six primary and six secondary species, the simple cycle of six primary partners has \(W=6\) and \(D=0\). The interaction graph with partner pairs \(\{01,01,02,03,04,05\}\) has \(W=16\) and \(D=1\). Their variances are respectively \(15/8\) and \(13/4\) when \(q=1/2\), and \(9/25\) and \(39/25\) when exactly three of six primaries disappear. The expected extinction count is identical in each pair.

## Relationship to prior work

Memmott, Waser and Price (2004) modeled secondary plant extinctions after removing pollinators when all partners are lost, with random and degree-ordered primary losses. Burgos and collaborators (2006) studied network nestedness and expected robustness/attack-tolerance curves. Chabert-Liddell, Barbillon and Donnet (2021) calculated variance of a robustness statistic over randomly generated bipartite stochastic-block-model networks and analyzed its parameter extrema; their distribution over **network realizations** and time-averaged statistic are not the distribution of the *fixed-incidence secondary-extinction count* treated here. Jones, Zurell and Wiesner (2024) developed analytic predictions and an expected-robustness optimum based on balancing **secondary** degrees; those claims do not imply this variance minimum from balancing **primary** degrees while every secondary degree equals two.

The exact degree-pair overlap decomposition is related to classical random-induced-subgraph edge-count calculations, and degree balancing is elementary. The particular simultaneous extremum and the complete stage-dependent equality classification are the claim of this note, not an assertion that covariance counting or convexity is new.

## Limitations

There is no claim for secondary species with one or at least three partners, heterogeneous or correlated primary risks, survival after loss of only one partner, network adaptation, or ecological population viability. Biological species dynamics are replaced by a one-step all-partners-lost proxy. The theorem characterizes variance minima, not extrema of skewness, tail probabilities, or worst-case losses. It does not require every network to be connected, although the demonstrated six-primary comparison uses connected networks. The proof is self-contained; an undiscovered graph-theoretic characterization of fixed-size induced-edge variance might imply it.

## References

1. Memmott, J., Waser, N. M. & Price, M. V. (2004), *Tolerance of pollination networks to species extinctions*, Proceedings of the Royal Society B, doi:10.1098/rspb.2004.2909. First published online 2004-12-06. https://www.bio.bris.ac.uk/research/community/article_PDF/Memmottetal2004.pdf
2. Burgos, E., Ceva, H., Hernández, L., Perazzo, R. P. J., Devoto, M. & Medan, D., *Why Nestedness in Mutualistic Networks?* arXiv:q-bio/0609005. https://arxiv.org/pdf/q-bio/0609005
3. Chabert-Liddell, S., Barbillon, P. & Donnet, S., *Impact of the mesoscale structure of a bipartite ecological interaction network on its robustness through a probabilistic modeling*. arXiv:2106.06348. https://arxiv.org/pdf/2106.06348
4. Jones, C., Zurell, D. & Wiesner, K., *Novel analytic methods for predicting extinctions in ecological networks*, Ecological Monographs (2024), doi:10.1002/ecm.1601. https://esajournals.onlinelibrary.wiley.com/doi/full/10.1002/ecm.1601
