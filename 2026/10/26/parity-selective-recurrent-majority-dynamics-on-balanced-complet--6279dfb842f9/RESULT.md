# Parity-selective recurrent majority dynamics on balanced complete multipartite graphs

## Finding

Let \(G_{r,s}=K_{s,\ldots,s}\) be the loopless complete \(r\)-partite graph with \(r\ge 2\) labelled parts, each of size \(s\ge 1\). Update all binary vertex states synchronously by strict open-neighbourhood majority, retaining the present state on a tie. Write \(F=F_{r,s}\), \(Q_{r,s}=|\operatorname{Fix}(F)|\), and \(P_{r,s}=|\operatorname{Fix}(F^2)|\). Put

\[
C_s=\begin{cases}\binom{s}{s/2},&s\text{ even},\\0,&s\text{ odd},\end{cases}\qquad D_s=2^s-2.
\]

Then the exact labelled counts for every \(r\ge2,s\ge1\) are

\[
\boxed{Q_{r,s}=2+C_s^r,}\qquad
\boxed{P_{r,s}=2+[z^0](C_s+z+z^{-1})^r+\mathbf1_{\{r\text{ odd}\}}\,r\binom{r-1}{(r-1)/2}(D_s-C_s).}
\]

Every recurrent orbit has period one or two; the number of distinct primitive two-cycles is \((P_{r,s}-Q_{r,s})/2\). Every configuration is periodic by time three, with the uniform identity

\[\boxed{F^5=F^3.}\]

The entry-time bound three is attained, for example, for \((r,s)=(5,5)\). The exact formulas give distinct parity regimes. For fixed odd \(s\ge3\), as \(r\to\infty\) along even and odd subsequences respectively,

\[
P_{r,s}-2\sim\begin{cases}
2^r\sqrt{2/(\pi r)},&r\text{ even},\\
(2^s-2)\,2^r\sqrt{r/(2\pi)},&r\text{ odd}.
\end{cases}
\]

For fixed even \(s\), with \(C_s\ge2\), the asymptotic is instead

\[
P_{r,s}\sim(C_s+2)^r\sqrt{\frac{C_s+2}{4\pi r}}.
\]

Thus part-size parity changes the exponential base, while for odd part size the number-of-parts parity changes the polynomial prefactor by a full factor of order \(r\).

## Assumptions and scope

The vertex set comprises \(r\) disjoint labelled parts \(V_i\) of equal positive size \(s\), with edges exactly between different parts. States lie in \(\{0,1\}^{rs}\). Every vertex updates in parallel to one if more than half its \((r-1)s\) neighbours are one, to zero if fewer than half are one, and otherwise retains its prior bit. A configuration is recurrent if \(F^k(x)=x\) for some positive integer \(k\); the theorem proves that \(k\) can be chosen as two. Part labels and individual vertex labels are retained in all counts; there is no quotient by automorphisms.

## Proof

**1. Exact part dynamics.** Let \(t_i\) be the number of one-bits in part \(V_i\), let \(T=\sum_i t_i\), and let \(h=(r-1)s/2\). Each vertex in part \(V_i\) has precisely \(T-t_i\) neighbours in state one. Therefore after one update the entire part becomes all one if \(T-t_i>h\), becomes all zero if \(T-t_i<h\), and remains unchanged if \(T-t_i=h\). A homogeneous part stays homogeneous under every future update. A mixed part (one with \(0<t_i<s\)) can remain mixed only through an exact tie, and hence keeps all its individual bits when it does so.

**2. Classify periodic configurations.** Consider a periodic configuration. Each of its mixed parts must remain mixed throughout its orbit, so each sees a tie in every time step. If mixed parts exist, their one-counts are all a common integer \(t\) with \(1\le t\le s-1\), and the global count must satisfy \(T=h+t\). Every homogeneous empty part then sees \(h+t>h\) and becomes full; every homogeneous full part sees \(h+t-s<h\) and becomes empty. Write \(k\) for the number of mixed parts, \(\alpha\) for full parts and \(\beta\) for empty parts. Since the global count is constant, switching all homogeneous parts requires \(\alpha=\beta=(r-k)/2\). Substituting \(T=\alpha s+kt=h+t\) yields

\[
(k-1)(2t-s)=0.
\]

Consequently, either \(k=1\), in which case \(t\) may be any integer in \(\{1,\ldots,s-1\}\), or \(k\ge2\) and every mixed part must contain exactly \(s/2\) ones (possible only for even \(s\)). In either case every homogeneous part swaps between full and empty; if \(k=r\), the configuration is fixed.

With no mixed parts, suppose \(\alpha\) parts are full. An empty part becomes full exactly when \(\alpha>(r-1)/2\), while a full part becomes empty exactly when \(\alpha<(r+1)/2\). Apart from the all-zero and all-one fixed points, a periodic configuration must therefore have \(r\) even and \(\alpha=r/2\), and every part flips. This exhausts the possibilities and proves that recurrent periods are one and two.

**3. Exact counting.** Every mixed half-filled part has \(C_s\) possible labelled internal words; there are \(D_s\) possible mixed internal words in total. Assign the weights \(z\), \(z^{-1}\), and \(C_s\) to a homogeneous full, homogeneous empty, and half-filled mixed part respectively. The coefficient \([z^0](z+z^{-1}+C_s)^r\) counts exactly the configurations with equally many full and empty parts, all remaining parts half-filled mixed. When \(r\) is odd, configurations having exactly one mixed part also allow internal words not half-filled; their number beyond those already in the coefficient is \(r\binom{r-1}{(r-1)/2}(D_s-C_s)\). Add the two unanimous fixed points to obtain \(P_{r,s}\). The only fixed configurations other than those two have all \(r\) parts half-filled and mixed; hence \(Q_{r,s}=2+C_s^r\). Dividing the number \(P_{r,s}-Q_{r,s}\) of primitive period-two states by two counts distinct orbits.

**4. Global entry bound.** From any state, after one update every part is homogeneous except possibly some mixed parts, all having the same one-count \(t\) (because the tie equation forces a common value). If there are none, the resulting homogeneous state reaches a recurrent state in at most one more update. Otherwise, at time one let \(\alpha\) parts be full and \(\beta\) empty. If the mixed parts are not tied at time one, all parts are homogeneous at time two, and time three is recurrent. If they are tied, all homogeneous parts switch. When \(\alpha=\beta\), the time-one state already has period at most two. When \(\beta>\alpha\), the time-two global one-count exceeds the time-one count by \((\beta-\alpha)s\), so at the next update every part becomes full: its mixed parts see more than \(h\) neighbours in state one, full parts see at least \(h+t\), and empty parts see more than \(h\). The case \(\alpha>\beta\) analogously becomes all zero. Hence every state is recurrent by update three, proving \(F^5=F^3\). At \((r,s)=(5,5)\), part one-count vector \((0,3,3,3,4)\) evolves as

\[
(0,3,3,3,4)\to(5,3,3,3,0)\to(0,5,5,5,5)\to(5,5,5,5,5),
\]

and is not recurrent at earlier updates, proving sharpness somewhere in the family.

**5. Asymptotics.** If \(s\) is odd, \(C_s=0\). For even \(r\) the balanced coefficient is \(\binom r{r/2}\), and for odd \(r\) it vanishes; the additional single-mixed-part term then gives the two displayed estimates by Stirling's formula. For even \(s\), \(C_s\ge2\), and the constant term has the integral representation \((2\pi)^{-1}\int_{-\pi}^{\pi}(C_s+2\cos\theta)^r\,d\theta\). The unique dominant maximum is at zero; Laplace's method gives the stated coefficient with variance scale \(2/(C_s+2)\). The exceptional odd-\(r\) correction has exponential base two and is negligible against \((C_s+2)^r\).

## Verification

The accompanying standalone Python checker uses two distinct finite models: independent vertex-bit enumeration of all \(2^{rs}\) labelled configurations and separate enumeration of part-population vectors weighted by the appropriate binomial coefficients. For 20 pairs \((r,s)\) with \(rs\le16\), encompassing 167,116 fully enumerated configurations, both models agree with the closed formulas for \(Q_{r,s}\) and \(P_{r,s}\). The vertex-level computation also checks \(F^5(x)=F^3(x)\) for every enumerated configuration, and the separate size-\((5,5)\) part-vector example attains entry time three. Run `python3 verify.py`; expected final output is `VERIFY_OK`. The infinite-parameter conclusions are established by the preceding proof, not by finite enumeration.

## Relationship to prior work

The finite-graph period-one-or-two theorem belongs to Goles and Olivos (1980) and is not claimed as new. Benjamini and collaborators (arXiv:1405.2486v1) develop broader majority convergence results on unimodular and random graphs; their finite periodicity discussion does not enumerate recurrent states of balanced complete multipartite graphs. Turau (arXiv:2202.01580) characterizes recurrent majority configurations on trees, a different graph family. A previously recorded complete-tripartite exact census gives the \(r=3\) instance of the count, which this theorem reproduces but does not claim as independently novel. The contribution here is the uniform formula across every number of equal parts, the parity-dependent asymptotic spectrum, and the sharp uniform three-step entry bound. A public majority-C-coloring computation for multipartite graphs addresses a static coloring invariant rather than this synchronous dynamical count. See REVIEW.md and AUDIT.json for bounded coverage comparisons and access limitations.

## Limitations

The theorem assumes equal part sizes, synchronous updating, strict majority of open neighbours, and tie retention. It does not assert an exact basin-size distribution or cover unequal multipartitions, stochastic/asynchronous dynamics, or other thresholds. The entry bound is globally sharp but does not classify parameter pairs for which it is attained. The scientific originality assessment is bounded by accessible and indexed sources; the possibility of an unindexed equivalent exact formula cannot be excluded. Independent validation has not been performed.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI:10.1016/0012-365X(80)90121-1.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (first submitted 2014-05-11), https://arxiv.org/abs/1405.2486.
3. V. Turau, *Fixed Points and 2-Cycles of Synchronous Dynamic Coloring Processes on Trees*, arXiv:2202.01580 (2022), https://arxiv.org/abs/2202.01580.
4. A published published-finding corpus record, *Majority C-colorings of complete multipartite graphs*, 2026-10-04, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-majority-c-colorings-of-complete-multipartite-graphs--dd5898d7bbc5 (only its indexed summary was accessible in this check).
