# First-contact reversal of hub deprioritization on the four-vertex path

## Finding
Consider a four-individual population whose fixed replacement graph is the path \(0-1-2-3\). An interaction period contains each of its three edges exactly once, with one active edge per discrete update, and repeats indefinitely. In the donation game, a cooperator on the active edge pays cost \(c>0\) and supplies benefit \(b>0\) to its partner; only that edge produces payoffs. Under uniform-vertex death–birth replacement (defined below), introduce either one cooperator into defectors or one defector into cooperators, with its position uniform, **at the start of the first period**.

Let \(L=(0,1)\), \(M=(1,2)\), and \(R=(2,3)\). For any order \(\sigma\) of these edges, write \(\rho_C(\delta;\sigma)\) and \(\rho_D(\delta;\sigma)\) for the respective fixation probabilities at selection intensity \(\delta\ge0\). The exact weak-selection comparison is
\[
\left.\frac{\mathrm d}{\mathrm d\delta}(\rho_C-\rho_D)\right|_{\delta=0}
=A_\sigma b-\frac4{21}c,
\qquad
A_\sigma=\begin{cases}
12920/259077,&\text{if }M\text{ is first},\\
1730/37011,&\text{if }M\text{ is last},\\
11981/259077,&\text{if }M\text{ is in the middle}.
\end{cases}
\]
Thus the three exact benefit-to-cost thresholds are respectively
\[
\frac{12337}{3230},\qquad \frac{24674}{6055},\qquad\frac{49348}{11981}.
\]
In particular, with \(b=4\) and \(c=1\), the derivative is \(2332/259077>0\) when the central edge is first, but \(-908/259077<0\) when it is last and \(-1424/259077<0\) when it is in the middle. Consequently, **for all sufficiently small positive \(\delta\)**, central-edge-first ordering favors a rare cooperator over a rare defector while central-edge-last ordering does the opposite. The simple ascending edge-hub score \((\deg u+\deg v)/2\), which gives \(3/2,2,3/2\) for \(L,M,R\), schedules the high-degree central edge last and therefore selects the inferior ordering in this example.

This is a minimal connected simple-graph witness for a distinction among orders of one occurrence of each edge in a period: with at most three vertices, automorphisms permute the edges of each connected graph transitively when there is more than one edge. The statement concerns one-edge snapshots, phase-zero mutant introduction, and the precisely defined replacement process; it does not assert optimality properties of every scheduling metric or phase-averaged introductions.

## Assumptions and scope
For any strategy vector \(x\in\{0,1\}^4\), \(x_i=1\) means cooperation. The replacement graph is fixed and undirected, with neighbor probabilities \(p_{ij}=1/\deg(i)\) for adjacent \(i,j\) and zero otherwise. At time \(t=0,1,2,\ldots\), the current active edge is \(e_t=\sigma_{t\bmod3}\). Its endpoints \(u,v\) receive payoffs \(f_u=b x_v-c x_u\), \(f_v=b x_u-c x_v\); the other payoffs are zero. One individual \(i\) is selected uniformly to update and copies neighbor \(j\) with probability
\[
\frac{p_{ij}(1+\delta f_j)}{\sum_k p_{ik}(1+\delta f_k)}.
\]
Selection is sufficiently weak that all fitnesses are positive. The all-cooperator and all-defector states are absorbing. Mutation does not occur after introduction. Fixation probabilities sample the unique initial mutant uniformly from the four vertices, at phase zero. A positive derivative of \(\rho_C-\rho_D\) is called cooperation favored to first order. At derivative zero, no preference is asserted.

## Proof
Write \(\pi=(1,2,2,1)/6\), the neutral reproductive values. At \(\delta=0\), the voter-model martingale \(h(x)=\sum_i\pi_i x_i\) has limit the indicator of all-cooperator fixation. Its conditional first-order drift in a round with active edge \(e\) is
\[
g_e(x)=\frac1{48}\bigl[(f_0-f_2)(x_0-x_2)+(f_1-f_3)(x_1-x_3)\bigr].
\]
Indeed, only the two degree-two vertices can have fitness-biased copying; expanding their neighbor-choice denominator gives this expression. Differentiation of the finite absorbing-chain equations at neutrality, or summing this martingale drift to absorption, gives the derivative of fixation probability as the neutral expectation of \(\sum_{t\ge0}g_{e_t}(X_t)\), for each initial law.

To compare the two uniform single-mutant laws, add their expectations. For each pair of distinct vertices \(i,j\), the neutral voter dual has two independent ancestral lineages which move when their current vertex updates; coalescence makes their descendants agree. Let \(S_{ij}(t)\) be the probability the two ancestral lineages have not coalesced after \(t\) neutral updates, and put \(S_{ii}(t)=0\). For the sum of the two initial laws, the expectation of any \(x_i\) is \(1\), and
\[
\mathbb E_C[x_ix_j]+\mathbb E_D[x_ix_j]=1-\frac12S_{ij}(t).
\]
Use pair order \((01,02,03,12,13,23)\). The six-component survival column satisfies \(S(t)=Q^t\mathbf1\), where
\[
Q=\frac18\begin{pmatrix}
4&1&0&0&0&0\\
1&4&1&2&0&0\\
0&2&4&0&2&0\\
0&1&0&4&1&0\\
0&0&1&2&4&1\\
0&0&0&0&1&4
\end{pmatrix}.
\]
For example, the diagonal half of each row is the probability that neither ancestral position updates; the remaining transitions move one of the two lineages one step along the path, with coalesced transitions discarded. Because the path is connected, coalescence occurs almost surely, so \(\rho(Q)<1\).

On substituting the payoffs into \(g_e\), the total expected drift at time \(t\) becomes \((b v_e-cw)Q^t\mathbf1\), where
\[
\begin{aligned}
96v_L&=(-2,0,1,1,0,0),\\
96v_M&=(1,0,0,-2,0,1),\\
96v_R&=(0,0,1,1,0,-2),\\
96w&=(0,1,0,0,1,0).
\end{aligned}
\]
Summing the periodic sequence yields the exact rational identity
\[
D_\sigma(b,c)=\left(b\sum_{r=0}^2v_{\sigma_r}Q^r-c\sum_{r=0}^2wQ^r\right)(I-Q^3)^{-1}\mathbf1.
\]
The cost part is independent of edge order since \(\sum_{r=0}^2Q^r(I-Q^3)^{-1}=(I-Q)^{-1}\); exact rational elimination gives \(w(I-Q)^{-1}\mathbf1=4/21\). Evaluating the three benefit row combinations by the same rational elimination gives the coefficients stated in the Finding. Reversing the path interchanges \(L\) and \(R\), proving the two schedules within each class agree. Multiplying the three coefficients by \(4\) and subtracting \(4/21\) gives the stated signed fractions. Analyticity around \(\delta=0\) follows from inversion of the finite transient transition matrix, establishing the small-positive-selection assertions.

Finally, no connected graph with fewer than four vertices has three nonequivalent edge positions in a permutation of its edges: the graph with one edge is trivial; the two-edge path is swapped by reflection; the triangle has all six edge permutations induced by its vertex automorphisms. Hence no order dependence of this kind can arise below four vertices under the same uniform initial-mutant and symmetric updating convention.

## Verification
The included standalone `verify.py` uses Python standard-library rational arithmetic. It constructs \(Q\) and solves \((I-Q^3)z=\mathbf1\), evaluates the six edge orders, and matches every rational coefficient and threshold above. Independently it constructs the full neutral transition matrix on all \(14\) transient binary profiles, differentiates the death–birth expectation for every edge and profile, and verifies exact agreement with the pair-duality route. Run `python3 verify.py` from a directory containing the extracted file. All six orders and both independent finite-state computations pass. The script is a reproducible finite exact calculation of matrix entries; the displayed mathematical derivation explains why it proves the infinite-time fixation derivative.

## Relationship to prior work
Meng, McAvoy and Li [1] give a general analytical framework for weak-selection cooperation on temporal networks and identify late involvement of high-degree individuals as an empirically useful **rule of thumb**. Their work motivates the precise question of whether ascending edge-hub scheduling must improve cooperation. The present result does not challenge their general coalescent framework: it computes a previously unreported exact small-instance threshold and identifies the reverse scheduling preference under explicit phase-zero, single-edge-periodic conditions. Allen and collaborators [2] derive static-graph coalescent methods; those results do not identify these three period-dependent coefficients. The exact finding is not a counterexample to a theorem asserting universal hub-priority optimality, because no such universal theorem is attributed to [1].

## Limitations
The mutant enters at the first phase, **not** a uniformly randomized temporal phase. The interaction snapshots contain exactly one active edge, and the fixed replacement graph is the same path. A different updating rule, simultaneous multi-edge payoffs, stochastic or finite-duration snapshots, or introducing mutants after a randomly chosen number of rounds can alter the ranking. This is a complete classification only for the six period-three edge permutations on \(P_4\), not a universal best-ordering theorem for arbitrary temporal networks. It provides the exact first-order weak-selection comparison and no claim at the zero-derivative thresholds. A broad general method in [1] can specialize to this instance after nontrivial exact calculation; specialist literature or supplementary tables may already contain related small-network values.

## References
[1] Y. Meng, A. McAvoy, A. Li, *Promoting collective cooperation through temporal interactions*, arXiv:2404.07530v1 (first posted 2024-04-11); *Proceedings of the National Academy of Sciences* 122 (2025), e2509575122, doi:10.1073/pnas.2509575122.

[2] B. Allen, G. Lippner, Y.-T. Chen, B. Fotouhi, N. Momeni, S.-T. Yau, M. A. Nowak, *Evolutionary dynamics on any population structure*, *Nature* 544 (2017), 227–230, doi:10.1038/nature21723.
