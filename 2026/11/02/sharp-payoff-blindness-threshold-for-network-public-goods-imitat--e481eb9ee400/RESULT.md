# Sharp payoff-blindness threshold for network public-goods imitation

## Finding

**Theorem (exact threshold and neutral regime).** Let \(G=(V,E)\) be a finite connected simple \(d\)-regular graph with \(d\ge1\). Each vertex chooses cooperation \(s_v=1\) or defection \(s_v=0\). For every closed-neighborhood group \(N[z]\), its cooperators provide \(r\) units of shared benefit apiece, divided equally among the \(d+1\) group members; each cooperator pays one unit **in every group it joins**, hence \(d+1\) total. Here \(r>0\).

Let \(A\) be the adjacency matrix, \(M=(I+A)^2\), and for each adjacent ordered pair \(x,y\) define

\[
 h^{xy}_z=M_{xz}-M_{yz},\qquad
 a_{xy}=d-1-|N(x)\cap N(y)|,\qquad
 H_{xy}=\tfrac12\sum_{z\in V}|h^{xy}_z|.
\]

Define the exact structural cutoff

\[
\Theta_G(r)=\max_{\{x,y\}\in E}\max\!\left\{
\left|\frac{rH_{xy}}{d+1}-(d+1)\right|,
\left|\frac{r(2a_{xy}-H_{xy})}{d+1}-(d+1)\right|
\right\}.
\]

A payoff-thresholded Fermi update at temperature \(K\in(0,\infty)\) changes the payoff difference to zero when its absolute value is **strictly less** than the fixed cutoff \(\varepsilon\ge0\), and otherwise uses the actual difference. Then every comparison between adjacent opposite strategies has imitation probability exactly \(1/2\), for **every** binary configuration, if and only if

\[
\boxed{\varepsilon>\Theta_G(r).}
\]

The inequality is strict: at equality, an opposite-strategy edge and a configuration retain a nonzero payoff difference. For the square torus \(G=C_L\mathbin{\square} C_L\), \(L\ge6\),

\[
\boxed{\Theta_G(r)=\max\{5+r,|11r/5-5|\}
=\begin{cases}5+r,&0<r\le25/3,\\11r/5-5,&r\ge25/3.\end{cases}}
\]

By comparison, the complete graph \(K_5\), also four-regular, has \(\Theta_{K_5}(r)=5\) for every \(r>0\). Thus the cutoff detects interaction-group overlap rather than merely vertex degree.

For the uniform asynchronous protocol that chooses a vertex uniformly and then a uniformly random neighbor and applies the thresholded Fermi decision, any connected regular network in this regime is a lazy voter process. From a starting profile with \(b\) cooperators among \(n=|V|\) vertices, consensus occurs almost surely and

\[
\mathbb P(\text{all-cooperator consensus})=b/n.
\]

## Assumptions and scope

The game uses **standard shared-pool public goods**: both cooperator and defector receive the same benefit from the number of cooperators in a group, but only the former incurs the cost. Groups are closed neighborhoods, all groups have equal size \(d+1\), cooperation costs one **per group**, and accumulated payoffs determine Fermi comparisons. No conformity update, mutation, weighted groups, varying cutoffs, or adaptive thresholds are assumed. The threshold treats \(|\Delta|=\varepsilon\) as a consequential difference. The neutral fixation conclusion assumes uniform asynchronous selection and connectedness; the threshold result itself does not require that update schedule.

## Proof

**1. Exact accumulated payoff.** A vertex \(v\) belongs to the groups centered at \(N[v]\), so the sum of the numbers of cooperating group members over those groups is \(((I+A)^2s)_v\). Therefore

\[
\pi_v(s)=\frac r{d+1}(Ms)_v-(d+1)s_v.
\]

**2. Edge contrast and its exact extremizers.** Fix an edge \(xy\), with \(s_x=1\) and \(s_y=0\), and write \(h=h^{xy}\). Because \(G\) is regular, every row of \(M\) sums to \((d+1)^2\), hence \(\sum_z h_z=0\). The diagonal and adjacent off-diagonal entries satisfy \(M_{xx}=d+1\), \(M_{xy}=2+|N(x)\cap N(y)|\), giving

\[
h_x=a_{xy}\ge0,\quad h_y=-a_{xy},\quad
\sum_{h_z>0}h_z=H_{xy}=-\sum_{h_z<0}h_z.
\]

All other binary coordinates can be chosen independently. To maximize \(h\cdot s\), set all remaining positive-coefficient coordinates to one and negative-coefficient coordinates to zero, obtaining \(H_{xy}\). To minimize, set all remaining negative-coefficient coordinates to one and positive-coefficient coordinates to zero, obtaining \(a_{xy}-(H_{xy}-a_{xy})=2a_{xy}-H_{xy}\). Both extrema are **attained** (the fixed states of \(x,y\) are compatible with each selection). Consequently

\[
\pi_x-\pi_y\in\left[
\frac r{d+1}(2a_{xy}-H_{xy})-(d+1),\quad
\frac r{d+1}H_{xy}-(d+1)
\right],
\]

with attained endpoints. Reversing the endpoint strategies reverses the sign of the relevant payoff difference and has the same maximum absolute value. Taking absolute values of the endpoints, then maximizing over edges, gives precisely \(\Theta_G(r)\).

**3. Sharp payoff-blindness.** The Fermi probability \(1/(1+\exp(\Delta/K))\) is \(1/2\) for finite positive \(K\) exactly when its input is zero. If \(\varepsilon>\Theta_G(r)\), every eligible difference is discarded. If \(\varepsilon\le\Theta_G(r)\), one of the attained extremal profiles has a nonzero difference whose absolute value is at least \(\varepsilon\), so it is retained and yields a probability different from \(1/2\). This proves necessity and sufficiency.

**4. Square torus and clique.** For \(L\ge6\), no two distinct positions in the two-radius edge stencil coincide under wraparound. On any horizontal edge, the nonzero coefficients of \(h\) consist of one \(+3\), two \(+2\), four \(+1\), one \(-3\), two \(-2\), and four \(-1\). Hence \(a_{xy}=3\), \(H_{xy}=11\), and the attainable linear-contrast extrema are \(-5\) and \(11\). Translation and rotation symmetry cover all edges. The formula reduces to the stated piecewise expression. For \(K_5\), every closed neighborhood is all of \(V\); the rows of \(M\) are identical, so every opposing pair has payoff difference of magnitude five, independently of \(r\).

**5. Neutral fixation.** Under uniform asynchronous updating, each ordered edge is chosen with the same probability. Above the sharp threshold an opposite-strategy endpoint copies its neighbor with probability \(1/2\); this is the lazy voter chain. Symmetry of ordered-edge sampling makes the cooperation count a bounded martingale. Every non-consensus state admits a positive-probability finite sequence of copies to consensus, so the finite chain absorbs almost surely. Optional stopping of the bounded count martingale gives the stated fixation probability.

## Verification

The standalone `verify.py` uses exact rational arithmetic and the actual adjacency matrices to check the edge-contrast formula against exhaustive binary-profile enumeration for cycles, complete graphs, a triangular prism, and a complete bipartite graph. It checks six rational synergy values per graph, totaling 114 graph/rate comparisons including the torus formulas. For torus side lengths \(6,7,10\), it independently enumerates all \(2^{12}=4096\) assignments of the free nonzero-stencil spins after fixing a discordant edge and verifies the contrast extremes and the threshold formula. All tests passed. These finite calculations are checks of the algebra and implementation, not proofs for arbitrary graph order; the proof above is uniform in graph size.

Run `python verify.py` using Python's standard library.

## Relationship to prior work

Javarone and Singh (first posted October 23, 2023) formulate a Fermi strategy-revision rule that disregards sufficiently small payoff differences and investigate square-lattice public-goods outcomes by simulations. The present theorem isolates the **exact finite cutoff beyond which every possible update is payoff-blind**, and extends the cutoff calculation to any finite connected regular graph. The standard overlapping-neighborhood accumulated-payoff convention is made explicit here because the printed notation for the number of contributors in one of their payoff formulas is ambiguous.

Perc and collaborators describe the standard overlapping-group public-goods and neighbor-imitation framework. Takiguchi and Nemoto derive a large-noise voter-model approximation in an unthresholded public-goods setting; their asymptotic high-temperature statement does not give the present exact, finite-temperature, finite-cutoff criterion. The neutral-regime fixation probability itself is classical voter-process mathematics, not claimed as a new independent theorem.

## Limitations

This is a classification of **uniform statewise payoff blindness**, not a claim that every lower cutoff produces persistent strategic selection or a different eventual fixation probability. The cutoff is held fixed, unlike a threshold estimated anew from sample trajectories. Small square tori can have overlapping two-radius stencil sites, so the explicit torus constant is asserted only for \(L\ge6\). No claim of originality is made for the classical voter martingale argument. No independent external validation has been performed; equivalent finite-cutoff calculations under alternate terminology remain a priority risk.

## References

1. M. A. Javarone and S. P. Singh, *Strategy Revision Phase with Payoff Threshold in the Public Goods Game*, arXiv:2310.15096v1, first posted 2023-10-23. https://arxiv.org/abs/2310.15096
2. M. Perc, J. Gómez-Gardeñes, A. Szolnoki, L. M. Floría, and Y. Moreno, *Evolutionary dynamics of group interactions on structured populations: a review*, Journal of the Royal Society Interface 10 (2013), 20120997. https://pmc.ncbi.nlm.nih.gov/articles/PMC3565747/
3. Y. Takiguchi and K. Nemoto, *Approximate master equations for the spatial public goods game*, Phys. Rev. E 109 (2024), 024304; arXiv:2603.05001 (later preprint release). https://arxiv.org/abs/2603.05001
4. T. M. Liggett, *Interacting Particle Systems*, Springer (1985), for classical voter-model background.
