# A four-vertex Poisson law for the LCM density of random edge ideals

## Finding

**Theorem (finite characterization, sharp threshold, critical law).** Fix a field \(K\). For a simple graph \(G\) on \([n]\), write
\[
I(G)=(x_ix_j: \{i,j\}\in E(G))\subset K[x_1,\ldots,x_n],\qquad
\alpha(G)=\frac{|L(I(G))|}{2^{|E(G)|}},
\]
where \(L(I(G))\) contains the least common multiple of **every** subset of the minimal edge generators, including the empty subset. Thus \(0<\alpha(G)\le1\). Then:

1. \(\alpha(G)=1\) if and only if every nonisolated connected component of \(G\) is a star. Equivalently, every edge has an endpoint of degree one, or \(G\) has neither a (not necessarily induced) four-vertex path \(P_4\) nor a triangle as a subgraph.
2. Let \(G_n\sim G(n,p_n)\) with independent edges, and set \(A_n=\alpha(G_n)\). If \(n^{4/3}p_n\to0\), then \(\Pr(A_n=1)\to1\). If \(n^{4/3}p_n\to\infty\), then \(A_n\to0\) in probability (hence also \(\Pr(A_n=1)\to0\)).
3. If \(n^{4/3}p_n\to c\in(0,\infty)\), then
\[
A_n\ \xrightarrow{d}\ (7/8)^Z,\qquad
Z\sim\operatorname{Poisson}(c^3/2).
\]
In particular,
\[
\Pr(A_n=1)\longrightarrow e^{-c^3/2},\qquad
\mathbb E A_n\longrightarrow e^{-c^3/16}.
\]

Thus the normalized LCM-lattice size for this squarefree degree-two model has a threshold at \(p_n\asymp n^{-4/3}\), before the classical giant-component scale \(p_n\asymp n^{-1}\). The full critical distribution, not just a zero-one threshold, is explicit.

## Assumptions and scope

All graphs are finite and simple; isolated vertices are allowed. An edge ideal has one squarefree degree-two minimal generator per edge, regardless of the ground field. The empty-edge case has \(L(I(G))=\{1\}\) and \(\alpha(G)=1\). The random-graph parameter \(p_n\) belongs to \([0,1]\). Statements use the limit \(n\to\infty\); the critical law has \(c>0\) fixed. The normalization follows the LCM-density definition of Mohammadi, Petrović and Sáenz-de-Cabezón (2026), not the differently generated cut ideal of Mohammadi, Sáenz-de-Cabezón and Wynn (2025).

## Proof

**1. Exact finite criterion.** For any edge set \(F\subseteq E(G)\), the LCM of the corresponding generators is the squarefree monomial supported on \(U(F)=\bigcup_{e\in F}e\). Hence \(|L(I(G))|=|\{U(F):F\subseteq E(G)\}|\). If every edge \(e\) has a degree-one endpoint \(v_e\), the variable \(x_{v_e}\) appears in \(U(F)\) exactly when \(e\in F\); thus \(F\mapsto U(F)\) is injective and \(\alpha(G)=1\). Conversely, if \(e=uv\) has both endpoints of degree at least two, deleting \(e\) from the full edge set changes neither covered vertex, so \(U(E(G))=U(E(G)\setminus\{e\})\), giving \(\alpha(G)<1\). If such an edge exists, choose another edge at each endpoint. The two other edges either meet at their other endpoints, forming a triangle, or have distinct other endpoints, forming a \(P_4\). Conversely, the central edge of a \(P_4\), or any triangle edge, has two non-leaf endpoints. The absence of these subgraphs therefore characterizes star forests.

**2. A deterministic density bound and monotonicity.** If \(G'\) is obtained from \(G\) by adding one edge \(uv\), its LCM supports are in \(L(G)\cup\{S\cup\{u,v\}:S\in L(G)\}\). Therefore \(|L(G')|\le2|L(G)|\), so \(\alpha(G')\le\alpha(G)\). A path \(P_4\) with three edges has exactly seven distinct unions of endpoint sets among its eight edge subsets: the full path and its two disjoint outer edges both cover all four vertices. Suppose \(G\) contains \(k\) vertex-disjoint \(P_4\) subgraphs; reserve their \(3k\) distinct edges and fix an arbitrary subset of all other edges. Varying the edges in each reserved path contributes at most seven distinct support sets instead of eight. It follows that
\[
|L(I(G))|\le 2^{|E(G)|-3k}7^k,
\qquad\alpha(G)\le(7/8)^k.
\]
This bound does not require the paths to be induced or isolated components.

**3. Below the threshold.** The expected number of nonoriented copies of \(P_4\) in \(G(n,p_n)\) is \(12\binom n4p_n^3\), while the expected number of triangles is \(\binom n3p_n^3\). Both tend to zero when \(n^{4/3}p_n\to0\). Markov's inequality and Step 1 establish the first regime.

**4. At the threshold.** Put \(p_n\sim c n^{-4/3}\). A triangle has expected count \(O(n^3p_n^3)=O(n^{-1})\). Every connected graph with at least four edges contains a connected four-edge subgraph on at most five vertices; the expected number of such subgraphs is at most \(O(n^5p_n^4+n^4p_n^4+n^3p_n^4)=O(n^{-1/3})\). Therefore, with probability tending to one, every component is a tree with at most three edges. The only such component contributing an LCM collision is the four-vertex path; stars contribute Boolean LCM lattices, and disconnected components give direct products of LCM lattices. Thus \(A_n=(7/8)^{Z_n}\) on this probability-one-asymptotic event, where \(Z_n\) counts components isomorphic to \(P_4\).

For a specified four-element vertex set there are \(4!/2=12\) possible path edge sets. Consequently
\[
\mathbb E Z_n=12\binom n4 p_n^3(1-p_n)^{4(n-4)+3}
\longrightarrow c^3/2.
\]
The exponent excludes all other three possible internal edges and all \(4(n-4)\) external incidences. For each fixed \(j\ge1\), \(j\) distinct path components must be vertex-disjoint. Their factorial-moment count therefore tends to \((c^3/2)^j\): disjoint choices have the expected product asymptotics since \(np_n\to0\). The factorial-moment characterization gives \(Z_n\Rightarrow\operatorname{Poisson}(c^3/2)\). Convergence in distribution of \(A_n\) follows, and boundedness allows expectations to converge. Since \(\Pr(A_n=1)=\Pr(Z_n=0)+o(1)\), the displayed exact-critical probabilities follow as well.

**5. Above the threshold.** It suffices to prove many vertex-disjoint copies of \(P_4\) with high probability. Couple \(G(n,p_n)\) from below with \(G(n,q_n)\), where \(q_n=\min\{p_n,n^{-7/6}\}\). Then \(q_n\gg n^{-4/3}\) and \(nq_n\to0\). Let \(X_n\) count all (not necessarily induced) unoriented copies of \(P_4\) in this smaller graph. Its mean \(\mu_n=12\binom n4q_n^3\) tends to infinity. Overlapping ordered distinct path pairs, grouped by shared vertices and edges, have expected total at most
\[
O(n^7q_n^6+n^6q_n^5+n^5q_n^4+n^4q_n^4)=o(\mu_n^2).
\]
These terms correspond respectively to a one-vertex overlap, a shared edge, a shared two-edge path, and distinct paths on the same four vertices; cases with fewer shared edges are dominated for \(q_n\le1\). Pairs with no shared edges have zero covariance, so \(\operatorname{Var}X_n=o(\mu_n^2)\), hence \(X_n/\mu_n\to1\) in probability. Form the conflict graph whose vertices are the occurring path copies, adjacent when sharing any vertex. Its number \(J_n\) of conflict edges is \(o_{\mathbb P}(\mu_n^2)\). The standard independent-set bound \(\alpha_{\rm ind}\ge X_n^2/(X_n+2J_n)\) now gives a number \(k_n\to\infty\) in probability of vertex-disjoint paths. Step 2 implies \(\alpha(G(n,q_n))\le(7/8)^{k_n}\to0\). Monotonicity and coupling yield \(\alpha(G(n,p_n))\to0\), completing the proof.

## Verification

Run `python verify.py` using Python 3 and no third-party dependencies. The checker independently constructs all unions of edge-subsets; exhaustively tests the star-forest criterion on every labelled simple graph with at most six vertices (\(1,2,8,64,1024,32768\) graphs by order); checks density monotonicity under every single-edge addition through five vertices; checks \(|L(I(kP_4))|=7^k\) for \(1\le k\le4\); and verifies the labeled \(P_4\) copy factor \(12\binom n4\) for \(4\le n\le10\). It reports `VERIFY_OK`. All stochastic and asymptotic conclusions are proved in Step 3–5 rather than inferred from finite enumeration.

## Relationship to prior work

Mohammadi, Petrović and Sáenz-de-Cabezón (2026, §4.1 and Conjecture 4.1) introduce this precise edge-ideal LCM-density statistic and investigate its phase-transition behavior experimentally. The result here establishes the four-vertex obstruction, the exact threshold scale, and the full Poisson critical distribution for their edge-ideal model. Their experiments and conjecture do not supply these formulas. Mohammadi, Sáenz-de-Cabezón and Wynn (2025, Theorem 3.10) treat **cut ideals** of random graphs, whose generators are cuts rather than the edges of the present ideal; their giant-component-scale statement does not imply this distinct \(n^{-4/3}\) edge-ideal law. De Loera, Hoşten, Krone and Silverstein (2018/2019) establish asymptotic resolution/Scarf results in a different model with fixed number of variables and growing generator degree; those results do not cover the present growing-variable, fixed squarefree-degree-two critical distribution. Standard small-subgraph Poisson methods are used as a tool, not presented as novel.

## Limitations

The theorem concerns the normalized size of the LCM lattice for **squarefree degree-two** random ideals. It does not prove analogous thresholds for degree three or higher, Betti density, Scarfness, random cut ideals, or other graph models. The finite graph criterion is elementary and the Poisson convergence uses classical probability; originality lies in their combination into the complete LCM-density distribution. Prior literature may contain equivalent implicit statements not found in the cited comparisons. No independent audit has been performed.

## References

1. F. Mohammadi, S. Petrović and E. Sáenz-de-Cabezón, *Asymptotic properties of random monomial ideals*, arXiv:2605.03464v1 (first posted 5 May 2026), especially Definitions 1.2, 2.1 and §4.1. https://arxiv.org/html/2605.03464v1
2. F. Mohammadi, E. Sáenz-de-Cabezón and H. Wynn, *Redundancy analysis using lcm-filtrations: networks, system signature and sensitivity evaluation*, arXiv:2505.01416v2 (2025), §3 and Theorem 3.10 (for cut ideals). https://arxiv.org/html/2505.01416v2
3. J. A. De Loera, S. Hoşten, R. Krone and L. Silverstein, *Average behavior of minimal free resolutions of monomial ideals*, Proc. Amer. Math. Soc. 147 (2019), 3239–3257; arXiv:1802.06537 (first posted 2018). https://arxiv.org/abs/1802.06537
4. M. Miller and B. Sturmfels, *Combinatorial Commutative Algebra*, Springer, 2005 (background on LCM lattices and Taylor resolutions).
