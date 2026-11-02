# A fractional Gumbel correction for simple-walk cover times on friendship graphs

## Finding

For each integer \(n\ge1\), let \(F_n\) be the graph formed by \(n\) edge-disjoint triangles sharing exactly one vertex \(o\). Run discrete-time, non-lazy simple random walk from \(o\), and let \(T_n\) be the number of steps until all \(2n+1\) vertices have first been visited. The following second-order limits hold for every fixed real \(x\):

\[
\Pr\{T_n\le4n(\log n+x)\}
=e^{-2e^{-x}}\left(1+n^{-1/3}e^{-4x/3}+o(n^{-1/3})\right).
\tag{1}
\]

Here \(T_n\) is integer-valued and the inequality has its usual real threshold interpretation. In particular \(T_n/(4n)-\log n\) converges in distribution to a Gumbel variable shifted by \(\log2\), but the first nonvanishing distribution-function correction is of order \(n^{-1/3}\), not \(n^{-1}\). Moreover, writing \(\gamma\) for Euler's constant,

\[
\mathbb ET_n=4n(\log n+\log2+\gamma)
-\frac{4\Gamma(4/3)}{2^{4/3}}n^{2/3}+o(n^{2/3}).
\tag{2}
\]

The positive constant multiplying \(n^{2/3}\) is approximately \(1.4175166161\). The negative correction arises from the rare event that an entire triangle remains unentered, rather than merely having one unvisited leaf.

There is also an exact finite-size excursion law. Write \(M_n\) for the first number of complete excursions from \(o\) back to \(o\) needed to see every vertex, where excursions are counted even if they discover no new vertex. Then, for all integers \(m\ge0\),

\[
\Pr\{M_n\le m\}=\sum_{\substack{a,b\ge0\\a+b\le n}}
\frac{n!}{a!b!(n-a-b)!}(-2)^a
\left(1-\frac{3a+4b}{4n}\right)^m.
\tag{3}
\]

Consequently, exactly for every \(n\ge1\),

\[
\mathbb ET_n=3\mathbb EM_n-2,
\qquad
\mathbb EM_n=4n\!\sum_{\substack{a,b\ge0\\1\le a+b\le n}}
\frac{(-1)^{a+1}2^a n!}{a!b!(n-a-b)!(3a+4b)}.
\tag{4}
\]

Equations (3)–(4) serve as exact checks and starting points; the new asymptotic information is specifically the fractional correction in (1) and (2), rather than the general availability of finite-graph cover-time inclusion-exclusion.

## Assumptions and scope

A triangle has two distinct outer vertices, both adjacent to \(o\) and to each other. At every discrete step a walker chooses uniformly among the current vertex's neighbors; thus \(o\) has degree \(2n\) and every outer vertex degree two. There are no holding steps, resets, external randomness in the graph, or non-backtracking restrictions. The walk starts at \(o\). All limits refer to integer \(n\to\infty\) with fixed real \(x\); no uniformity for diverging \(x\) is asserted. Define \(S_m\) to be the time of the \(m\)-th completed return excursion, with \(S_0=0\), and let \(M_n=\min\{m:\text{the first }m\text{ excursions visit every outer vertex}\}\).

## Proof

**1. One-excursion law.** At the hub, the next triangle index is uniform in \(\{1,\ldots,n\}\), and the initially visited leaf within that triangle is a fair choice. Thereafter each outer step chooses the hub or the other leaf with probability \(1/2\). The total excursion length \(L\) has distribution \(L=2+J\), where \(\Pr(J=j)=2^{-j-1}\) for integers \(j\ge0\). In particular the excursions are independent and identically distributed and \(\mathbb EL=3\); their lengths have a common finite exponential moment. Conditional on a selected triangle, the excursion visits just its initial leaf with probability \(1/2\), or both outer leaves with probability \(1/2\). Hence a specified outer leaf is visited in one excursion with probability \(3/(4n)\), whereas both outer vertices of a specified triangle are avoided with probability \(1-1/n\). Different triangles cannot be entered during the same excursion.

**2. Finite distribution and mean.** To apply inclusion-exclusion to the event that all \(2n\) outer vertices have been seen, select \(a\) triangles with one marked outer vertex and \(b\) other triangles with both vertices marked. In one excursion all these marked vertices are avoided with probability \(1-(3a+4b)/(4n)\). There are \(n!/[a!b!(n-a-b)!]\) assignments of the marked triangles; the one-mark case has two choices with negative inclusion-exclusion sign, contributing \((-2)^a\). Independence across excursions proves (3). Summing \(\Pr(M_n>m)\) over \(m\ge0\) proves the second equality of (4). The time \(S_{M_n}\) is a stopped sum of iid excursion lengths, so Wald's identity gives \(\mathbb ES_{M_n}=3\mathbb EM_n\). At the actual cover time the walk is on an outer vertex. By the strong Markov property, its expected additional time to hit \(o\) is exactly two steps (solve \(h=1+h/2\)). Thus \(\mathbb E(S_{M_n}-T_n)=2\) and (4) follows.

**3. Independent-triangle Poissonization.** Put excursions at the arrivals of a rate-one Poisson process, independently of excursion contents. Up to Poisson time \(t\), observations from distinct triangles are independent by Poisson splitting. For a given triangle, the probability neither leaf is seen is \(e^{-t/n}\); the probability a specified leaf is unseen is \(e^{-3t/(4n)}\). Inclusion-exclusion within one triangle therefore shows that the time \(\widetilde M_n\) at which all leaves have been seen has CDF

\[
G_n(t)=\Pr(\widetilde M_n\le t)
=\left(1-2e^{-3t/(4n)}+e^{-t/n}\right)^n,
\qquad t\ge0.
\tag{5}
\]

For \(t_n(x)=(4n/3)(\log n+x)\) and \(u=e^{-x}\), the quantity inside parentheses is \(1-2u/n+u^{4/3}/n^{4/3}\). Taylor expansion of the logarithm at any fixed \(u>0\) gives

\[
G_n(t_n(x))
=e^{-2u}\left(1+n^{-1/3}u^{4/3}+O_u(n^{-2/3})\right).
\tag{6}
\]

This identifies the unentered-triangle term \(e^{-t/n}\), whose cumulative contribution over \(n\) triangles is of order \(n^{-1/3}\).

**4. Depoissonization and discrete-step conversion.** The sequence \(m\mapsto\Pr(M_n\le m)\) is nondecreasing. Fix \(x\) and let \(m_x=\lfloor t_n(x)\rfloor\) and \(d_n=\lceil n^{3/5}\rceil\). A Poisson random variable with mean \(m_x\pm d_n\) differs from its mean by more than \(d_n\) with probability at most \(\exp[-c n^{1/5}/\log n]\) for a suitable constant \(c>0\). Monotonicity sandwiches \(\Pr(M_n\le m_x)\) between \(G_n(m_x-d_n)\) and \(G_n(m_x+d_n)\), up to errors smaller than every fixed negative power of \(n\). Shifting the Poisson time by \(d_n\) shifts \(x\) by \(O(n^{-2/5})=o(n^{-1/3})\). Equation (6) therefore remains valid with \(G_n(t_n(x))\) replaced by \(\Pr(M_n\le m_x)\), retaining its \(o(n^{-1/3})\) remainder.

For the return-excursion lengths \(L_i\), put \(S_r=\sum_{i=1}^rL_i\). A union bound on as-yet-unseen individual leaves yields

\[
\Pr\{M_n>\lceil8n\log n\rceil\}
\le2n\left(1-\frac{3}{4n}\right)^{\lceil8n\log n\rceil}
\le2n^{-5}.
\]

As \(L_i-3\) are independent, centered variables with a uniform exponential moment, an exponential-martingale maximal inequality gives

\[
\Pr\left\{\max_{r\le\lceil8n\log n\rceil}|S_r-3r|>n^{3/5}\right\}
\le2\exp[-c' n^{1/5}/\log n].
\]

The maximal excursion length among these excursions is also \(O(\log n)\) with probability \(1-O(n^{-5})\). Since \(S_{M_n-1}<T_n\le S_{M_n}\), it follows that

\[
\Pr\{|T_n-3M_n|>2n^{3/5}\}=o(n^{-1/3}).
\tag{7}
\]

At threshold \(4n(\log n+x)\), this coupling shifts \(m_x\) by at most \(O(n^{3/5})\), an \(x\)-shift \(O(n^{-2/5})\), and changes the CDF by \(o(n^{-1/3})\). Combining (6)–(7) proves (1), including its coefficient.

**5. Expected-cover-time correction.** The exponential interarrival times in the Poissonization are iid mean one and independent of \(M_n\); consequently \(\mathbb E\widetilde M_n=\mathbb EM_n\). Write \(u=e^{-x}\) and

\[
\Phi_n(u)=\left(1-\frac{2u}{n}+\left(\frac un\right)^{4/3}\right)^n,
\quad 0\le u\le n.
\]

Comparing the expectation of \(3\widetilde M_n/(4n)-\log n\) with that of a random variable having distribution function \(e^{-2e^{-x}}\), whose mean is \(\gamma+\log2\), gives

\[
\frac{3\mathbb EM_n}{4n}-\log n-(\gamma+\log2)
=-\int_0^n\frac{\Phi_n(u)-e^{-2u}}u\,du
+\int_n^{\infty}\frac{e^{-2u}}u\,du.
\tag{8}
\]

To justify the first correction by dominated convergence rather than integrating a merely pointwise distributional limit, split the integral at \(u=n/3\). For \(0<u\le n/3\), the mean-value bound for powers yields

\[
0\le\Phi_n(u)-(1-2u/n)^n
\le n^{-1/3}u^{4/3}e^{-u/2},
\]

and the standard logarithmic inequality gives

\[
0\le e^{-2u}-(1-2u/n)^n\le C u^2e^{-2u}/n.
\]

After multiplication by \(n^{1/3}/u\), both terms have integrable exponential upper bounds independent of \(n\). For \(u\ge n/3\), \(\Phi_n(u)\le e^{-u}\), so the remaining integral is exponentially small. Thus dominated convergence in (8), using the expansion \(n^{1/3}(\Phi_n(u)-e^{-2u})\to e^{-2u}u^{4/3}\), proves

\[
\lim_{n\to\infty}n^{1/3}\left(\log n+\gamma+\log2-\frac{3\mathbb EM_n}{4n}\right)
=\int_0^\infty e^{-2u}u^{1/3}\,du
=\frac{\Gamma(4/3)}{2^{4/3}}.
\]

Using \(\mathbb ET_n=3\mathbb EM_n-2\) proves (2). This completes the proof for every fixed real \(x\).

## Verification

The accompanying standalone `checker.py` evaluates the inclusion-exclusion CDF (3) using exact fractions and independently computes the excursion-state transition process on pairs with zero, one, or two unseen leaves. It compares their CDFs for \(1\le n\le6\) and \(0\le m\le15\), compares two independent exact computations of the excursion mean for \(1\le n\le6\), and directly solves the visited-state Markov-chain linear system for the actual random-walk cover time for \(1\le n\le3\). It additionally evaluates the Poissonized correction numerically for four fixed locations and four large sizes. One completed execution passed 137 assertions; finite cases are cross-checks only and do not replace the analytic argument.

## Relationship to prior work

The 2009 work of Zlatanov and Kocarev already gives a general exact cover-time inclusion-exclusion method valid for arbitrary finite graphs. Equation (3) is a graph-specific simplification, not a claim that generic exact cover-time formulas were unknown. Ferrante and Frigo (2012) also give finite expectation formulas for generalized coupon collection in batches; those formulas do not themselves state a fractional finite-size correction for this walk. Doumas and Papanicolaou (2017) analyze asymptotics of collections from different uniform groups with one coupon per trial, unlike the correlated one-or-two-leaf excursions here. Xu and Zhang's graph-cover study, first public February 13, 2023, concerns first-order optimal \(N\log N\) scaling on other sparse networks rather than the friendship-graph second-order distribution and mean. The distinct contribution claimed here is (1)–(2), especially the structural \(n^{-1/3}\) and \(n^{2/3}\) corrections arising from fully unentered paired leaves. A related result for non-backtracking motion along petal cycles, if considered, does not imply these formulas because backtracking is essential to the present one-or-two-leaf excursion law.

## Limitations

The theorem is proved only for non-lazy nearest-neighbor simple random walk on equal three-cycle petals, starting at the common hub. The expansion in (1) is pointwise for fixed \(x\); uniform tail expansions, general petal lengths, altered hub transition rules, starting positions other than the hub, and higher-order error terms are not asserted. The fractional term is an asymptotic coefficient, not a finite-\(n\) error bound of fixed sign. These results have not undergone independent mathematical validation. Historical priority is a best-knowledge literature comparison and not a proof of uniqueness.

## References

1. N. Zlatanov and L. Kocarev, *Random walks on networks: Cumulative distribution of cover time*, Physical Review E 80, 041102 (2009), DOI: 10.1103/PhysRevE.80.041102; freely accessible preprint https://manmade.maths.qmul.ac.uk/publications/CUmulativeTimeDistr_PRE.pdf.
2. M. Ferrante and N. Frigo, *A note on the coupon-collector's problem with multiple arrivals and the random sampling*, first posted September 12, 2012, https://arxiv.org/abs/1209.2667.
3. A. V. Doumas and V. G. Papanicolaou, *Sampling from a mixture of different groups of coupons*, first posted September 13, 2017, https://arxiv.org/abs/1709.04500.
4. W. Xu and Z. Zhang, *Optimal Scale-Free Small-World Graphs with Minimum Scaling of Cover Time*, first posted February 13, 2023, https://arxiv.org/abs/2302.06372.
