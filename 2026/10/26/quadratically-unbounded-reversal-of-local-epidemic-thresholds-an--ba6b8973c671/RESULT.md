# Quadratically unbounded reversal of local epidemic thresholds and endemic burden

## Finding

For every integer \(m\ge4\), construct a connected simple undirected graph \(G_m\) partitioned into **three connected induced communities of the same size \(m\)**, denoted \(A,B,C\). The isolated epidemic threshold of \(A\) is strictly *smaller* than that of \(B\). Nevertheless, for the independent-state discrete-time SIS product map below, the unique positive equilibrium satisfies

\[
\lim_{\beta\downarrow\beta_c}
\frac{Q_B(\beta)}{Q_A(\beta)}>\frac{m^2}{8},
\qquad \beta_c=\frac{\delta}{\lambda_1(G_m)},
\]

for every fixed recovery probability \(0<\delta<1\). Here the limit is from above, and \(Q_D(\beta)\) is the sum of endemic infection probabilities in community \(D\). Moreover, for all sufficiently close \(\beta>\beta_c\), **each isolated community is itself below its epidemic threshold**, although the coupled network has this positive equilibrium. Thus, for arbitrarily large \(m\), the *less vulnerable in isolation* of two equal-sized communities carries more than \(m^2/8\) times as much near-onset infection as the other when both are embedded in the same network.

This is a deliberately constructed boundary example for what rankings by induced-subgraph thresholds can say about endemic burden. It is not a claim that such a reversal occurs in typical empirical community partitions.

## Assumptions and scope

Take three disjoint sets of vertices \(A=\{a_1,\ldots,a_m\}\), \(B=\{b_1,\ldots,b_m\}\), and \(C=\{c_1,\ldots,c_m\}\). Put a clique on \(A\), a path in the listed order on \(B\), and a clique on \(C\). Add every edge from \(B\) to \(C\), and add the single edge \(a_1b_1\). Add no other edges. This is a connected simple graph with three connected induced blocks, each on \(m\) vertices. Write \(M\) for its symmetric adjacency matrix and \(\Lambda=\lambda_1(M)\).

For \(0<\delta<1\) and \(0<\beta<1\), consider the deterministic *independent-state approximation*, not the absorbing finite-state Markov SIS chain,

\[
F_i(p;\beta,\delta)
=1-\bigl(1-(1-\delta)p_i\bigr)
\prod_{j\sim i}(1-\beta p_j),
\qquad p\in[0,1]^{3m}.
\]

When a positive fixed point exists, denote it by \(p^*(\beta)\) and define \(Q_D(\beta)=\sum_{i\in D}p^*_i(\beta)\). The *isolated* threshold \(\tau_D\) of a block is the inverse spectral radius of its induced adjacency matrix, so the corresponding isolated infection condition is \(\beta/\delta>\tau_D\). This terminology follows the source model and does not imply separate dynamics remain autonomous after adding cross-community edges.

The claim concerns equilibrium values and the one-sided \(\beta\downarrow\beta_c\) limit, for fixed finite \(m\) and \(\delta\). It makes no interchange of the limits \(m\to\infty\) and \(\beta\downarrow\beta_c\).

## Proof

**1. Local thresholds and global spectral bounds.** The isolated adjacency spectrum gives

\[
\tau_A=\tau_C=\frac{1}{m-1},\qquad
\tau_B=\frac{1}{2\cos(\pi/(m+1))}.
\]

For \(m\ge4\), \(m-1>2\cos(\pi/(m+1))\), hence \(\tau_A<\tau_B\): in isolation the clique \(A\) is the more readily invaded community.

The subgraph consisting only of the complete bipartite \(B\)-to-\(C\) links and the clique on \(C\) has a two-constant-vector invariant subspace, with quotient

\[
\begin{pmatrix}0&m\\ m&m-1\end{pmatrix}.
\]

Rayleigh's principle (or entrywise monotonicity of the Perron root) therefore gives

\[
\Lambda\ge\frac{m-1+\sqrt{(m-1)^2+4m^2}}{2}>m.
\]

Since every vertex degree is at most \(2m-1\), also \(\Lambda\le2m-1\). Set \(d=\Lambda-(m-1)\). These inequalities give

\[
\frac{m+1}{2}\le d\le m,
\qquad \Lambda>m-1.
\]

In particular, the global critical infection probability \(\beta_c=\delta/\Lambda\) lies strictly below all three isolated critical probabilities \(\delta/\lambda_1(M_D)\).

**2. The unique endemic branch and its Perron direction.** For an arbitrary connected simple graph with at least two vertices, fixed \(0<\delta<1\), and \(0<\beta<1\), the product map \(F\) is continuous, order preserving, and maps the unit cube to itself. If \(\beta\Lambda>\delta\), let \(v>0\) be a Perron vector of \(M\). For small enough \(s>0\),

\[
F(sv;\beta,\delta)-sv
=s(\beta\Lambda-\delta)v+O(s^2)>0
\]

coordinatewise. Monotone iteration from \(sv\) converges to a positive fixed point.

For completeness, positive fixed points are unique. For every positive vector \(q\in(0,1)^{3m}\), the function

\[
\psi_i(t)=F_i\bigl((\min\{1,tq_j\})_j;\beta,\delta\bigr)
\]

is increasing and concave on \(t\ge0\): it is one minus a product of positive decreasing piecewise-affine factors, whose derivative is a sum of nonincreasing nonnegative products and decreases at any saturation breakpoint. Because both the retained-infection term and at least one neighbor term are positive, it is strictly concave on \([0,1]\). Therefore \(\psi_i(t)<t\psi_i(1)\) for every \(t>1\). If \(p,q\) were two positive fixed points and \(t=\max_i p_i/q_i>1\), monotonicity and this inequality, at an index attaining the maximum, would give

\[
p_i=F_i(p)\le\psi_i(t)<tF_i(q)=tq_i=p_i,
\]

an impossibility. Applying the same argument with \(p,q\) reversed excludes two distinct positive fixed points. No coordinate of a positive fixed point equals \(1\), because \(\delta>0\) and \(\beta<1\). Thus the above argument applies to all positive equilibria.

At \(\beta=\beta_c\), there is no nonzero fixed point. A nonzero fixed point must be positive at every vertex by connectivity. For every positive \(p\), the strict union-bound inequality (there are at least two positive transmission/retention terms) gives

\[
F(p;\beta_c,\delta)
<(1-\delta)p+\beta_c Mp
\]

coordinatewise. Multiplication by the strictly positive left Perron vector contradicts the fixed-point identity. By compactness, the unique positive fixed point for \(\beta>\beta_c\) consequently tends to zero as \(\beta\downarrow\beta_c\). Divide its equation by its Euclidean norm and use

\[
F(p;\beta,\delta)-p
=(\beta M-\delta I)p+O(\|p\|^2).
\]

Every limit point of the normalized equilibria is a nonzero nonnegative null vector of \(\beta_c M-\delta I\), hence equals the normalized Perron vector. Consequently

\[
\lim_{\beta\downarrow\beta_c}
\frac{Q_B(\beta)}{Q_A(\beta)}
=\frac{V_B}{V_A},
\qquad V_D:=\sum_{i\in D}v_i.
\]

**3. A quadratic inversion bound for the Perron masses.** Sum \(Mv=\Lambda v\) over the clique \(A\), and then over the clique \(C\). Only the bridge enters \(A\); each vertex of \(C\) is linked to every vertex of \(B\). Therefore the identities are exact:

\[
dV_A=v_{b_1},\qquad dV_C=mV_B.
\]

At the bridge vertex \(b_1\), the eigenvector equation and positivity give

\[
\Lambda v_{b_1}=v_{b_2}+V_C+v_{a_1}
\le V_B+V_C+V_A.
\]

Substituting the preceding identities and rearranging yields

\[
\frac{V_B}{V_A}
=d\frac{V_B}{v_{b_1}}
\ge\frac{d(\Lambda d-1)}{d+m}.
\]

The right side increases with both \(d>0\) and \(\Lambda>0\) in the relevant range; in the numerator substitute \(d\ge(m+1)/2\) and \(\Lambda>m\), and bound the denominator by \(d+m\le2m\). This gives

\[
\frac{V_B}{V_A}
>\frac{(m+1)[m(m+1)-2]}{8m}
=\frac{(m+1)(m+2)(m-1)}{8m}
>\frac{m^2}{8}
\]

for every \(m\ge4\). The second strict inequality follows from \(2m^2-m-2>0\). The strict limit and the continuity of the positive equilibrium imply \(Q_B(\beta)/Q_A(\beta)>m^2/8\) for all sufficiently close \(\beta>\beta_c\), while step 1 ensures \(\beta/\delta<\tau_A,\tau_B,\tau_C\). This proves the claim.

## Verification

The standalone `checker.py` constructs \(M\) directly and calculates its Perron eigenpair and isolated spectra for \(m=4,6,10,20,40\). It verifies the exact block-sum eigenvector identities numerically, then solves the original nonlinear fixed-point equations at \(\beta=(1+\varepsilon)\beta_c\) with \(\delta=1/2\) and \(\varepsilon\in\{0.02,0.005\}\). For each case it checks positivity, the residual, the isolated subcriticality conditions, and the claimed bound.

For \(m=4\), the Perron mass ratio is approximately \(14.158776\), while the endemic ratios at the two tested distances from threshold are \(13.656880\) and \(14.031254\). For \(m=40\), the corresponding values are approximately \(1037.294417\), \(985.960018\), and \(1024.268795\), versus the proved lower bound \(200\). All ten tested positive fixed points had maximum coordinate residual below \(10^{-8}\). These finite checks illustrate, but do not prove, the universal statement, which follows from the preceding analytical argument.

Reproduce using `python checker.py` with NumPy and SciPy installed.

## Relationship to prior work

Dung and Phuc (first publicly posted 15 July 2026) defined and ranked the isolated community threshold set for this discrete-time independent-state SIS map, proved each isolated threshold is at least the global threshold, and simulated aggregate infection levels by community. Their stated results do not give an upper bound, lower bound, or monotone implication from the isolated-threshold ranking to the relative endemic burdens, nor a family with unbounded reversal.

Prasse and Van Mieghem (2020, Theorem 1) proved the near-threshold principal-eigenvector form of the endemic state for the distinct **continuous-time NIMFA SIS equations**. Thus Perron dominance near onset is established background, not claimed as a general discovery here. The contribution is the concrete three-community construction, the analytic \(m^2/8\) lower bound for the reverse burden ranking, and its verification for the source's nonlinear **discrete-time product map**.

Bonaccorsi and collaborators (2015) analyzed SIS epidemics with equitable or nearly equitable community partitions and quotient spectra, again principally in a continuous-time model. The present path–clique–bridge partition is not equitable and has strongly unequal within- and between-community edge densities; the cited spectral quotient theory does not supply this quantified burden-order reversal. Other epidemiological work recognizes that cross-community coupling changes prevalence and that invasion thresholds alone need not capture local risk. The present theorem isolates a precise, arbitrarily large, equal-community-size extremal effect under the stated model.

## Limitations

The map is a deterministic independent-state approximation and is not a theorem about the stationary distribution of a finite absorbing SIS Markov chain. The graph is deliberately nonmodular: the \(B\)-to-\(C\) inter-community connections are dense, so the construction is not an empirical model of weakly linked social communities. The statement concerns positive fixed points, not globally stable trajectories at all update parameters. The ratio limit takes fixed \(m\) first; no uniform onset window is asserted in \(m\). The bound is a rigorous lower bound, **not an optimal exponent or sharp coefficient**. Related continuous-time Perron-mode theory substantially precedes this result. Independent validation and a comprehensive publication-priority determination have not occurred.

## References

1. H. P. Dung and N. H. Phuc, *An Epidemic Threshold Set for Networks*, arXiv:2607.14048, first posted 2026-07-15. https://arxiv.org/abs/2607.14048 . Read as lawful open HTML text at https://academ.us/article/2607.14048/ , especially Sections 2–4.
2. B. Prasse and P. Van Mieghem, *Time-dependent solution of the NIMFA equations around the epidemic threshold*, Journal of Mathematical Biology 81 (2020), 1299–1355, DOI:10.1007/s00285-020-01542-6. Full open-access HTML: https://link.springer.com/article/10.1007/s00285-020-01542-6 , especially Section 4 and Theorem 1.
3. S. Bonaccorsi, S. Ottaviano, D. Mugnolo, and F. De Pellegrini, *Epidemic Outbreaks in Networks with Equitable or Almost-Equitable Partitions*, SIAM Journal on Applied Mathematics 75 (2015), 2421–2443, arXiv:1412.6157, DOI:10.1137/140995829. Author-provided full text at https://www.researchgate.net/publication/269877151_Epidemic_Outbreaks_in_Networks_with_Equitable_or_Almost-Equitable_Partitions , especially the quotient-matrix result and community dynamics.
