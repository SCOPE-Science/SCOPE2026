# Exact joint fixation and neutral linkage on complete bipartite game-selection networks

## Finding

For the neutral two-coordinate game/strategy copying rule defined below on the complete bipartite graph \(K_{a,b}\), the full joint law of the two eventual consensus labels is explicit, for every pair of positive integers \(a,b\) and every deterministic initial assignment of strategy and game labels. Write \(A,B\) for the graph's vertex classes and \(D=4ab+a+b\). Let \(I_s\) and \(I_g\) denote the initial vertices supplying the final strategy and final game, respectively. The distribution of this **ordered pair of ancestral vertices** is uniform within each of six disjoint classes, whose total probabilities are

\[
\begin{array}{c|cccccc}
\text{class}&A{=}A&A{\ne}A&B{=}B&B{\ne}B&A\mathbin{\to}B&B\mathbin{\to}A\\
\hline
\text{mass}&\dfrac{a+3b}{2D}&\dfrac{b(a-1)}{D}&\dfrac{3a+b}{2D}&\dfrac{a(b-1)}{D}&\dfrac{ab}{D}&\dfrac{ab}{D}
\end{array}
\]

Here \(A{=}A\) means both ancestors are the same member of \(A\); \(A{\ne}A\) means distinct members of \(A\); and \(A\mathbin{\to}B\) means the strategy ancestor is in \(A\), the game ancestor in \(B\). Empty distinct-vertex classes have zero mass when a part has one vertex.

In particular, the probability that the terminal strategy and game trace to *one identical initial agent* is exactly

\[
\boxed{\Pr(I_s=I_g)=\frac{2(a+b)}{4ab+a+b}.}
\]

For a fixed number \(n=a+b\) of agents, this probability is largest on a star \(K_{1,n-1}\) and smallest on an as-balanced-as-possible bipartite graph. For a star it converges to \(2/5\) as \(n\to\infty\), while for a balanced even-order biclique it is \(2/(n+1)\), which tends to zero.

## Assumptions and scope

Let \(a,b\in\mathbb N\), \(a,b\ge1\), and \(n=a+b\). Each vertex \(v\) carries a strategy \(s_v\) (for example cooperation/defection) and a game label \(g_v\) (for example a pair of payoff parameters). The initial labels are arbitrary; only those initially present may subsequently occur. At each discrete asynchronous step, select the focal vertex uniformly from all \(n\) vertices and select one neighbor uniformly from the focal's neighbors. Independently for strategy and game, toss a fair coin. On heads, the focal copies that coordinate of the **same selected neighbor**; on tails, it retains that coordinate. All other vertices retain both coordinates. Selection intensity is exactly zero, with strategy-update and game-update propensities both equal to one. This is the \(w=0\), \(p_s=p_g=1\) specialization of the Fermi model in Sadekar et al., whose adoption probability equals one half at zero selection; it is **not** a claim about positive selective advantage or quasi-stationary conditioning.

Because the graph is finite and connected and each coordinate has a positive copying probability along each oriented edge, both coordinates reach unanimous absorbing labels almost surely. Denote these labels by \(S_\infty,G_\infty\). For arbitrary bounded functions \(f\) on strategy labels and \(h\) on game labels, the complete joint law is recovered from

\[
\begin{aligned}
\mathbb E[f(S_\infty)h(G_\infty)]
={}&\frac{a+3b}{2Da}\sum_{i\in A}f(s_i)h(g_i)
+\frac{b}{Da}\sum_{\substack{i,j\in A\\i\ne j}}f(s_i)h(g_j)\\
&+\frac{3a+b}{2Db}\sum_{i\in B}f(s_i)h(g_i)
+\frac{a}{Db}\sum_{\substack{i,j\in B\\i\ne j}}f(s_i)h(g_j)\\
&+\frac1D\sum_{i\in A,j\in B}f(s_i)h(g_j)
+\frac1D\sum_{i\in B,j\in A}f(s_i)h(g_j).
\end{aligned}
\]

Terms involving distinct vertices of a singleton part are empty sums. Substituting indicator functions gives every atom of the joint distribution, even when different initial agents carry identical labels.

## Proof

**Almost-sure fixation.** For one coordinate, each required directed copying event has strictly positive probability. On a connected finite graph, there exists a finite sequence of such events spreading the label of any fixed vertex across a spanning tree. The minimum probability of such a sequence from any state is positive. Repeating disjoint blocks gives a geometric tail bound for the first consensus time. This applies to both coordinates; consensus is absorbing.

**The two-lineage dual.** Fix a terminal observation vertex and follow its strategy and game labels backward through the independent random-update coins. The two ancestral positions form a Markov chain on ordered vertex pairs. Unlike ordinary same-coordinate coalescing walks, *the two lineages can split after meeting*, because the two coordinate coins are independent. For every positive \(a,b\), this chain is irreducible and aperiodic (holding moves are possible); therefore its long-time distribution is unique. Graph automorphisms and interchange of the two coordinates imply uniformity within each ordered category and equal total mass for the categories \(A\mathbin{\to}B\) and \(B\mathbin{\to}A\). A category indexed by distinct vertices of a singleton class is absent.

**Exact class balance.** Let \(u,v,x,y,z,z\) be the six stationary masses in the displayed order. Multiplying all nontrivial backward transition probabilities by \(n\), the contributions out of \(A{=}A\) are \(1/4\) to \(B{=}B\), and \(1/4\) to each mixed class; out of \(A{\ne}A\) they are \(1/2\) to each mixed class. The two analogous rules hold after interchanging \(A,B\). From a mixed class, contributions to \(A{=}A,A{\ne}A,B{=}B,B{\ne}B\) are, respectively,

\[
\frac1{2a},\quad\frac{a-1}{2a},\quad\frac1{2b},\quad\frac{b-1}{2b}.
\]

Thus the category balance equations are

\[
3u=x+\frac{4z}{a},\qquad
3x=u+\frac{4z}{b},\qquad
v=\frac{a-1}{a}z,\qquad
y=\frac{b-1}{b}z,
\]

with \(u+v+x+y+2z=1\). They yield \(z=ab/D\), \(u=(a+3b)/(2D)\), \(x=(3a+b)/(2D)\), and the other masses displayed above. These equations remain valid for singleton classes, where the corresponding distinct-vertex mass is zero; the chain on feasible classes is still irreducible.

**From ancestry to eventual consensus.** For every fixed time, the joint labels at the observation vertex are exactly the two initial labels read at the two backward ancestral positions. By almost-sure fixation, the joint labels at that vertex converge to \((S_\infty,G_\infty)\). By finite-chain convergence, their limiting joint law is the stationary ordered-ancestor-pair law, proving the formula for arbitrary initial labels.

**Topology and an observable correlation.** Summing the equal-vertex classes gives \(u+x=2n/(n+4ab)\). At fixed \(n\), the product \(ab\) is smallest for a star and largest for balanced part sizes. On \(K_{1,n-1}\), suppose the center alone initially has strategy label one and game label one and all leaves have both labels zero. Each marginal final-one probability is \(1/2\) (the one-lineage stationary weight assigns the two parts equal mass), while

\[
\Pr(S_\infty=1,G_\infty=1)=\frac{3n-2}{2(5n-4)}\longrightarrow\frac3{10}.
\]

Therefore \(\operatorname{Cov}(S_\infty,G_\infty)\to1/20\) and the binary Pearson correlation tends to \(1/5\): persistent terminal association arises under **zero selection**. By contrast, for the structured complete graph \(K_n\) with the same shared-neighbor copying rule, the diagonal probability of the ancestral pair is \(2/(n+1)\), derived by balancing the diagonal-to-off-diagonal and reverse transitions. It tends to zero. The complete-graph comparison is auxiliary; the principal theorem concerns bicliques.

## Verification

The included standalone \(verify.py\) independently constructs the **entire forward two-coordinate absorbing Markov chain** for every binary initial configuration on \(K_{1,1}\), \(K_{1,2}\), \(K_{2,1}\), \(K_{1,3}\), \(K_{2,2}\) and \(K_{3,1}\). It solves forward absorption linear systems and compares all four terminal label-pair probabilities with the theorem: 3,648 comparisons passed within numerical tolerance \(3\times10^{-10}\). It also verifies 196 rational pairs of graph sizes, checking all stationary balance and normalization identities exactly. Run with Python 3 and NumPy/SciPy installed: \(\texttt{python verify.py}\). These finite checks supplement, not replace, the infinite-parameter algebraic proof.

## Relationship to prior work

Sadekar et al. (2023, arXiv:2311.11128, original version) define the independent two-coordinate adoption mechanism (their equations (10)–(11)) and study selection, network topology, and quasi-stationary cooperation; the present theorem specializes to neutrality and provides the explicit **joint absorbing fixation law** for complete bipartite graphs. Aldous and Fill's treatment of voter-model duality supplies a standard one-coordinate ancestry principle but not the independent-coin *splitting* of two different coordinates or these six joint masses. Bhaskar and Song (2009) develop multi-locus Moran/Wright–Fisher matching probabilities, with random mating, mutation and different reproduction rules; those results do not supply this graph-specific fixed-initial-label law. Artime et al. (2017) study a multilayer voter model with ageing and intra-agent layer coupling, not the present fixed-graph two-coordinate shared-neighbor mechanism. These comparisons support a distinct stated contribution, not a claim that no equivalent specialized result can exist.

## Limitations

The exact weights require a complete bipartite, unweighted graph, uniformly chosen focal, uniformly chosen neighbor, **independent** adoption coins of probability one half, no mutation and zero payoff selection. The fully correlated copying case and arbitrary adoption rates are not covered. The theorem is about unconditional eventual absorption, not the quasi-stationary distributions conditioned on nonabsorption studied in the motivating work; terminal correlations alone do not establish selective causation. The pair-ancestor graph reduction follows established voter-duality ideas, and an unlocated specialized equivalent treatment remains a literature-priority risk. No claim of external independent audit is made.

## References

1. O. Sadekar, A. Civilini, J. Gómez-Gardeñes, V. Latora, and F. Battiston, *Evolutionary game selection creates cooperative environments*, original arXiv version submitted November 18, 2023, https://arxiv.org/abs/2311.11128 (eqs. (10)–(11), sections II–IV).
2. D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, section 14.3, *Coalescing random walks and the voter model*, https://www.stat.berkeley.edu/~aldous/RWG/Book_Ralph/Ch14.S3.html.
3. A. Bhaskar and Y. S. Song, *Multi-locus match probability in a finite population: a fundamental difference between the Moran and Wright–Fisher models*, Bioinformatics **25** (2009), i187–i197, DOI: 10.1093/bioinformatics/btp227, https://academic.oup.com/bioinformatics/article/25/12/i187/192085.
4. O. Artime, J. Fernández-Gracia, J. J. Ramasco, and M. San Miguel, *Joint effect of ageing and multilayer structure prevents ordering in the voter model*, Scientific Reports **7** (2017), 7166, DOI: 10.1038/s41598-017-07031-z.
