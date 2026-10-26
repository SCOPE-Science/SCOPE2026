# Exact spacing and opposing alarm objectives for epidemic sentinels on cycles

## Finding

**Theorem.** Let \(n\ge3\), \(1\le k<n\), and \(0<p<1\). Place exactly \(k\) perfect monitors at distinct vertices of the undirected cycle \(C_n\). Choose one outbreak seed uniformly from **all** \(n\) vertices, including monitors. Independently retain each cycle edge with probability \(p\); the epidemic eventually visits exactly the open-edge component of its seed. Let \(X\) be the number of monitors in that component.

Let \(\ell_1,\ldots,\ell_k\) be the successive clockwise numbers of unmonitored vertices between consecutive monitors, so \(\ell_i\ge0\) and \(\sum_i\ell_i=n-k\). Define
\[
H_p(0)=0,\qquad H_p(\ell)=\sum_{j=1}^{\ell}(1-p^j)(1-p^{\ell+1-j})\quad(\ell\ge1).
\]
Then the exact probability of at least one alarm is
\[
\Pr(X\ge1)=1-\frac1n\sum_{i=1}^k H_p(\ell_i).
\]
Among all \(k\)-monitor placements, this probability is **maximized exactly** when the \(k\) gap sizes differ by at most one. It is **minimized exactly** when all unmonitored vertices form a single gap (equivalently, the monitors are consecutive), allowing the trivial ties when \(k=1\) or \(n-k\le1\). Every nontrivial balancing move strictly increases the probability, for every \(0<p<1\).

For **every** \(k\) and placement, the expected number of monitors receiving an alarm is independent of placement:
\[
\mathbb E X=\frac{k}{n}\left(1+2\sum_{d=1}^{n-1}p^d-(n-1)p^n\right).
\]
For \(k=2\), the full law is determined by \(\Pr(X\ge1)\) and this common mean, since
\[
\Pr(X=2)=\mathbb E X-\Pr(X\ge1),\quad
\Pr(X=1)=2\Pr(X\ge1)-\mathbb E X.
\]
Consequently, on every cycle with \(n\ge4\), widely separated monitors maximize the probability of **at least one** alarm but minimize the probability of **two corroborating alarms**; neighboring monitors have the exactly opposite extremal properties. These inequalities are strict whenever the two placements have distinct gap-size multisets.

For example, on \(C_6\) at \(p=1/2\), neighboring monitors have \(\Pr(X\ge1)=5/8\) and \(\Pr(X=2)=21/64\). Opposite monitors have \(\Pr(X\ge1)=3/4\) and \(\Pr(X=2)=13/64\). Thus maximal detection diversity entails reduced double confirmation in this model.

## Assumptions and scope

The epidemic model is homogeneous independent *undirected bond transmission* on a simple finite cycle; an infected cluster is the undirected connected component of the seed in the retained-edge graph. The seed is uniform over **all** vertices and independent of the edges. Monitors observe infection perfectly but do not interrupt transmission. No time-to-detection objective or directed transmission is assumed. Optimality ranges simultaneously over all integer \(n\ge3\), integer \(1\le k<n\), and real \(0<p<1\). The limiting values \(p=0\) or \(p=1\) are deliberately excluded from strict comparisons.

## Proof

**1. Non-detection decomposes over monitor gaps.** A seed located at the \(j\)-th unmonitored vertex of a gap of size \(\ell\) can reach a monitor only by traversing one of the two edge-disjoint routes to the bordering monitors, of lengths \(j\) and \(\ell+1-j\). If neither route is fully retained, no monitor anywhere on the cycle is reachable; conversely, either fully retained route reaches a monitor. Independence gives non-detection probability \((1-p^j)(1-p^{\ell+1-j})\). A seed at a monitor is detected immediately. Summing over all possible uniform seeds proves the claimed exact formula.

**2. Strict balancing and concentration.** A geometric-sum rearrangement yields
\[
H_p(\ell)=\ell-2\sum_{j=1}^{\ell}p^j+\ell p^{\ell+1}.
\]
Its exact discrete second difference at every integer \(\ell\ge0\) is
\[
H_p(\ell+2)-2H_p(\ell+1)+H_p(\ell)
=(\ell+2)p^{\ell+1}(1-p)^2>0.
\]
Thus forward increments of \(H_p\) strictly increase. If two gap sizes satisfy \(a\ge b+2\), moving one unmonitored vertex from the larger gap to the smaller gap strictly decreases \(H_p(a)+H_p(b)\), increasing the detection probability. Repeated such transfers terminate exactly at gap vectors whose entries differ by at most one. Conversely, reversing these transfers increases \(\sum H_p\); repeated concentration puts all \(n-k\) unmonitored vertices into one gap, the unique maximal-sum multiset when a nontrivial choice exists. Every such nonnegative integer gap vector is realizable as a cyclic monitor placement. This proves both exact extremal classifications and their strictness, including the degenerate cases.

**3. Placement-independent mean.** Fix a monitor vertex \(v\). For any other vertex \(u\), the two simple routes from \(v\) to \(u\) around \(C_n\) are edge-disjoint, with lengths \(d\) and \(n-d\). Thus the probability that they lie in one open component equals \(p^d+p^{n-d}-p^n\). The expected size of the open component containing \(v\) is therefore
\[
T_n(p)=1+2\sum_{d=1}^{n-1}p^d-(n-1)p^n.
\]
Because the seed is uniform over all \(n\) vertices, the probability that this monitor is reached equals \(T_n(p)/n\). Linearity of expectation over the \(k\) monitors proves the mean formula, independently of their positions.

**4. Opposing objectives for two monitors.** For \(k=2\), \(X\) takes values in \(\{0,1,2\}\), hence \(\mathbb E X=\Pr(X\ge1)+\Pr(X=2)\). With the mean independent of placement, every strict increase of \(\Pr(X\ge1)\) entails an equal decrease of \(\Pr(X=2)\). Combining this identity with Step 2 gives the claimed opposite maximizers and minimizers. For \(n\ge4\), the balanced and concentrated gap multisets differ, so the inequalities are strict.

## Verification

The accompanying standalone `verify_cycle_surveillance.py` enumerates all retained-edge masks, every possible seed, and every monitor placement for all cycle sizes \(3\) through \(8\), using integer-weighted exact probability arithmetic at \(p=1/4,1/2,3/4\). It compares the direct event distribution with the gap formula and, for two monitors, checks the entire two-alarm distribution and mean formula. It also verifies discrete convexity and balanced-versus-concentrated inequalities for integer ranges \(3\le n<80\). Its actual machine-readable output is `verification_certificate.json`. These finite tests supplement, rather than replace, the general proof above.

## Relationship to prior work

Kiss, Green and Kao (2005) analyze tracing in epidemic contact networks and establish a connection between contact structure and tracing effectiveness; the studied model is not this static percolation monitor-placement objective. Leskovec et al. (2007) show that detection likelihood is submodular and develop approximation algorithms for general outbreak-monitor placement. Their general approximation framework does not state an exact all-size cyclic-gap classification, nor a strict converse optimization for two simultaneous alarms. Miller (2008) analyzes probability and size of epidemics under transmission heterogeneity, with a different extremal variable. Christakis and Fowler (2010) motivate network sentinel selection empirically. Their monitored outcome is early observed incidence, not the present eventual-component alarm law. General coverage/submodularity principles are prior knowledge, not claimed as new. Exact equality cases and the opposed corroboration objective for this specified bond-transmission cycle are the contributions assessed here.

## Limitations

This is a model-specific mathematical theorem, not a clinical surveillance deployment rule. It assumes undirected independent edges, homogeneous transmission, no timing or recovery mechanism, perfect passive detection, uniformly distributed seeding including sentinels, and a ring contact topology. Results need not survive directed or correlated transmission, partial sensor sensitivity, nonuniform seed risk, deadlines, or adaptive controls. The rarity or uniqueness of this precise formulation has not been independently established; an equivalent cyclic-coverage theorem under other terminology could already exist.

## References

1. Kiss, I. Z., Green, D. M., and Kao, R. R. (2005). *Disease contact tracing in random and clustered networks*. Proceedings of the Royal Society B 272:1407–1414. DOI: 10.1098/rspb.2005.3092. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC1560336/ .
2. Leskovec, J., Krause, A., Guestrin, C., Faloutsos, C., VanBriesen, J., and Glance, N. (2007). *Cost-effective Outbreak Detection in Networks*. Technical report CMU-ML-07-111 (June 2007); ACM KDD 2007. Open report: https://www-cs.stanford.edu/~jure/pubs/detect-techRept.pdf .
3. Miller, J. C. (2008). *Bounding the Size and Probability of Epidemics on Networks*. Journal of Applied Probability 45:498–512. Public preprint: arXiv:0803.0999, first posted 2008-03-06. DOI: 10.1239/jap/1214950363.
4. Christakis, N. A., and Fowler, J. H. (2010). *Social Network Sensors for Early Detection of Contagious Outbreaks*. PLoS ONE 5:e12948. DOI: 10.1371/journal.pone.0012948. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC2939797/ .
