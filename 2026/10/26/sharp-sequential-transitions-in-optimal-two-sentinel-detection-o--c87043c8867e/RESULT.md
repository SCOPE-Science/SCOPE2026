# Sharp sequential transitions in optimal two-sentinel detection on epidemic paths

## Finding

In homogeneous independent-edge epidemic transmission along a contact path, the optimal **pair** of fixed sentinels for detecting a uniformly located single-seed outbreak changes separation in a complete, strictly ordered staircase as transmissibility increases. Every separation from \(\lfloor n/3\rfloor+1\) through \(n-1\) is uniquely optimal on a nonempty open interval of transmissibilities. There are no skipped distances, and each transition joins two neighboring separations only.

More formally, for each integer \(n\ge4\), put \(d_0=\lfloor n/3\rfloor+1\). For each integer \(d_0\le d\le n-2\), set \(q_d=\lfloor(n-d)/2\rfloor\) and define \(\alpha_d\in(0,1)\) as the unique root strictly below \(1\) of
\[
p^{d-q_d}(d+1-dp)=1.
\]
These roots exist and satisfy
\[
0<\alpha_{d_0}<\alpha_{d_0+1}<\cdots<\alpha_{n-2}<1.
\]
If \(0<p<\alpha_{d_0}\), optimal separation is \(d_0\). Each strict crossing of \(\alpha_d\) increases the optimal separation from \(d\) to \(d+1\); equality gives exactly these two optimal separations. Above \(\alpha_{n-2}\) the endpoints are uniquely optimal. For each separation, optimal positions place the two residual outside gaps as equally as possible (unique up to reflection).

For \(n=4\), the only transition is at \(p=1/2\), when optimal distance changes from two edges to three edges. In this smallest example, the difference between detection probabilities at separations three and two, for a uniform nonsentinel seed, equals \(p(1-p)(2p-1)/2\).

## Assumptions and scope

The graph is the simple path with labeled vertices \(1,\ldots,n\), \(n\ge4\). Every edge is independently open with the same probability \(0<p<1\). Select distinct sentinels \(a<b\) in advance; an infected seed is selected uniformly from the remaining \(n-2\) vertices. All vertices connected to the seed by open edges are eventually infected, and detection succeeds if at least one sentinel is in this open component. There are no edge retries, spontaneous infections, detection errors, or transmission-time penalties. The objective is **eventual probability of any detection**, not expected detection time and not the probability of detecting *both* sentinels.

Let \(d=b-a\), \(L=a-1\), and \(R=n-b\), so \(L+R=n-d-1\). Define the geometric partial sum \(G_m(p)=\sum_{j=1}^m p^j\) for integers \(m\ge0\), with \(G_0=0\).

## Proof

**1. Exact infection and detection probabilities.** For a seed strictly left of \(a\), reaching at least one sentinel is equivalent to reaching \(a\), with probability \(p^{a-i}\). For a seed strictly right of \(b\), probability is \(p^{i-b}\). For a seed between sentinels, the two events of reaching the left and right sentinels use respective disjoint edge sets and have probabilities \(p^{i-a}\) and \(p^{b-i}\), with intersection probability \(p^d\). Thus inclusion–exclusion gives \(p^{i-a}+p^{b-i}-p^d\). Including, solely for algebraic convenience, the two sentinel seeds with automatic detection probability one, the sum over all possible seeds is
\[
H_n(d,L,R;p)=2+2G_d(p)+G_L(p)+G_R(p)-(d+1)p^d.
\]
The actual detection probability for a uniformly random **nonsentinel** seed is exactly
\[
\mathcal D_n(a,b;p)=\frac{H_n(d,L,R;p)-2}{n-2}.
\]
The added two terms are constant across placements and hence do not alter optimizers.

**2. Fixed-distance placement.** Since \(G_m-G_{m-1}=p^m\) decreases strictly with \(m\), if \(L\ge R+2\), moving one unit of margin from \(L\) to \(R\) strictly increases \(G_L+G_R\). The symmetric argument covers \(R\ge L+2\). Consequently for each \(d\), all maximizing placements have \(\lvert L-R\rvert\le1\); they differ at most by reflection. Put \(L_d=\lfloor(n-d-1)/2\rfloor\), \(R_d=\lceil(n-d-1)/2\rceil\), and \(F_d(p)=H_n(d,L_d,R_d;p)\).

**3. Neighboring-distance increment.** Replacing \(d\) by \(d+1\) shortens the larger outside gap by one, subtracting \(p^{q_d}\) from its geometric sum, where \(q_d=\lfloor(n-d)/2\rfloor\). Direct subtraction therefore yields, for every \(1\le d\le n-2\),
\[
F_{d+1}(p)-F_d(p)=p^d(d+1-dp)-p^{q_d}.
\]
If \(d\le\lfloor n/3\rfloor\), then \(d\le q_d\); because \(d+1-dp>1\) and \(p^{q_d}\le p^d\), this increment is strictly positive for every \(0<p<1\). All globally optimal separations must therefore be at least \(d_0=\lfloor n/3\rfloor+1\).

**4. One and only one interior transition at each remaining distance.** Fix \(d_0\le d\le n-2\), and put \(k=d-q_d\). Here \(1\le k<d\) because \(q_d\ge1\). The sign of the increment in step 3 is the sign of \(h_d(p)-1\), where
\[
h_d(p)=p^k(d+1-dp).
\]
We have \(h_d(0)=0\), \(h_d(1)=1\), and
\[
h_d'(p)=p^{k-1}\bigl(k(d+1)-d(k+1)p\bigr).
\]
Its derivative changes from positive to negative exactly at \(c_d=k(d+1)/(d(k+1))\in(0,1)\). Therefore \(h_d\) rises to a strict maximum exceeding one, then decreases strictly to one at the right endpoint. Exactly one root \(\alpha_d\in(0,c_d)\) satisfies \(h_d(\alpha_d)=1\), with \(h_d(p)<1\) for \(p<\alpha_d\) and \(h_d(p)>1\) for \(\alpha_d<p<1\). The crossing is strict and transverse.

**5. Increasing transitions and no skipped distances.** The quantity \(q_d\) either stays constant or decreases by one when \(d\) increases, so \(k_{d+1}-k_d\in\{1,2\}\). For \(0<p<1\),
\[
p\,[d+2-(d+1)p]<d+1-dp,
\]
since the difference is \((d+1)(1-p)^2>0\). It follows that \(h_{d+1}(p)<h_d(p)\) for every \(0<p<1\). In particular, at \(p=\alpha_d\), \(h_{d+1}(p)<1\), so \(\alpha_d<\alpha_{d+1}\). At fixed \(p\), consecutive differences of \(F_d\) consequently have the sign pattern positive, possibly zero once, then negative. The globally optimal distance therefore traverses each successive integer from \(d_0\) through \(n-1\) at its own unique transition; all intervening open parameter intervals are nonempty. Together with step 2, this establishes the stated complete placement classification.

## Verification

The standalone `verify.py` performs exact-rational checks on 26,946 placement/parameter cases with \(4\le n\le30\); compares the analytical placement probabilities with a direct open-edge-subset enumeration in 483 cases for \(4\le n\le10\); checks 2,430 exact neighboring-distance differences; and verifies the increasing critical-threshold ordering with rational bisection for \(4\le n<100\). Run `python3 verify.py`; the one-line JSON output is also stored in `verification_certificate.json`. Those finite checks corroborate, but cannot establish, the universal theorem proved above.

## Relationship to prior work

Christakis and Fowler (2010) motivate outbreak sentinel surveillance; Bajardi, Barrat, Savini and Colizza (2012) optimize sentinels on time-dependent livestock networks; Takaguchi, Hasegawa and Yoshida (2013/2014) introduce **active immunizing observers**, a distinct intervention objective. Holme (2017, 2018) considers exact importance rankings and distinct sentinel objectives (including eventual detection frequency) but studies small graphs and empirical networks rather than giving this all-path, exact two-sentinel transition sequence. Haldar et al. (2023) develop general temporal-cascade sentinel-set algorithms, not the explicit path transition roots and proof. O'Hanley, Scaparra and García (2013) develop reliability-aware location formulations; their accessible description does not state this epidemic-percolation placement classification.

The novelty claim is only for the complete closed-form staircase, ordered unique thresholds, and exact layouts in this specific model, not for the established notion of sentinel coverage, random-edge reachability, or generic optimization algorithms. A relevant paper using different reliability-location terminology could imply an equivalent special case; that residual bibliographic risk remains.

## Limitations

This is a static, homogeneous independent-edge transmissibility model on a path with one uniform nonsentinel source and exactly two perfectly observed sentinels. It does not cover temporal/contact-correlated transmissions, heterogeneous source weights, noisy testing, earlier detection deadlines, general graphs, or the different minimum-time surveillance objective. The arrangement is optimized for eventual any-sentinel detection; practical interventions may require other criteria. Bibliographic originality has not been independently audited.

## References

1. Christakis, N. A., and Fowler, J. H. (2010), “Social Network Sensors for Early Detection of Contagious Outbreaks,” *PLoS ONE* 5:e12948. First arXiv version 27 April 2010, arXiv:1004.4792; doi:10.1371/journal.pone.0012948.
2. Bajardi, P., Barrat, A., Savini, L., and Colizza, V. (2012), “Optimizing surveillance for livestock disease spreading through animal movements,” *Journal of the Royal Society Interface* 9:2814–2825, doi:10.1098/rsif.2012.0289; arXiv:1210.0692.
3. Takaguchi, T., Hasegawa, T., and Yoshida, Y. (2014), “Suppressing epidemics on networks by exploiting observer nodes,” *Physical Review E* 90:012807, arXiv:1312.6468.
4. Holme, P. (2017), “Three faces of node importance in network epidemiology: Exact results for small graphs,” *Physical Review E* 96:062305, arXiv:1708.06456.
5. Holme, P. (2018), “Objective measures for sentinel surveillance in network epidemiology,” arXiv:1803.10637.
6. O'Hanley, J. R., Scaparra, M. P., and García, S. (2013), “Probability chains: A general linearization technique for modeling reliability in facility location and related problems,” *European Journal of Operational Research* 230:63–75, doi:10.1016/j.ejor.2013.03.021.
7. Haldar, A., et al. (2023), “Temporal Cascade Model for Analyzing Spread in Evolving Networks,” *ACM Transactions on Spatial Algorithms and Systems* 9:12, doi:10.1145/3579996.
