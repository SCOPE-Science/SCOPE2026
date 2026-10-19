# Exact optimal pinning and convergence rates on five-neighbor opinion rings

## Finding

**Theorem.** Fix an integer \(n\ge5\), a real target opinion \(u\), and a set of pinned agents \(P\subseteq\mathbb Z/n\mathbb Z\). Every agent assigns weight \(1/5\) to itself and to the two nearest agents on either side around a circle. Pinned agents are drawn toward \(u\) with unit relaxation rate; unpinned agents are drawn at unit rate toward their five-input median. Then the following are equivalent:

1. Every initial opinion vector in \(\mathbb R^n\) converges to the constant target vector \(u\mathbf1\).
2. The induced graph on the unpinned agents is a forest, where edges connect circular distances one or two.
3. The clockwise distances between consecutive pinned indices, when the pinned indices are listed cyclically, all belong to \(\{1,2,3\}\), and at least one such distance equals one.

In particular, **the exact minimum number of pinned agents** is
\[
p_n=\left\lceil\frac{n+2}{3}\right\rceil.
\]
The exact number \(N_n\) of labelled optimal pinning sets is
\[
N_n=\begin{cases}
n(p_n-1),&n\equiv0\pmod3,\\
n,&n\equiv1\pmod3,\\
\frac{n(p_n-1)^2}{2},&n\equiv2\pmod3.
\end{cases}
\]
All effective pinning layouts, not only optimal layouts, are characterized by condition 3. This distinction matters: pinning every third agent leaves a closed chain of unpinned agents, whereas making at least one pair of pinned agents adjacent breaks that chain.

**Quantitative extension.** For any finite, simple, undirected four-regular graph \(G\), give each agent weight \(1/5\) on itself and its four neighbors, with the same dynamics. Every initial vector converges to \(u\mathbf1\) exactly when the induced graph \(G[V\setminus P]\) is a forest. Whenever it is, write \(m=|V\setminus P|\) and \(R=\max_{i\in V}|x_i(0)-u|\). For every real \(t\ge0\),
\[
\max_{i\in V}|x_i(t)-u|\le R e^{-t}\sum_{j=0}^{m}\frac{t^j}{j!}.
\]
Thus the convergence is global and exponentially fast up to an explicit degree-\(m\) polynomial factor, for arbitrary real initial states and arbitrary real target opinions.

## Assumptions and scope

The vertex set of the ring is \(\mathbb Z/n\mathbb Z\) with \(n\ge5\), and circular distance is the shorter of the clockwise and anticlockwise distances. The five influences at agent \(i\) are exactly \(x_{i-2},x_{i-1},x_i,x_{i+1},x_{i+2}\), with indices read modulo \(n\). They are distinct when \(n\ge5\). For any five real numbers, \(\operatorname{med}_5\) is their third order statistic. For all \(t\ge0\), the equations are
\[
\dot x_i(t)=\begin{cases}
u-x_i(t),&i\in P,\\
\operatorname{med}_5(x_{i-2}(t),x_{i-1}(t),x_i(t),x_{i+1}(t),x_{i+2}(t))-x_i(t),&i\notin P.
\end{cases}
\]
Here \(\nu=u\) is the fixed target; the symbol \(\nu\) emphasizes it is not a time-varying control. This is the full-pinning specialization of constant prejudice in continuous-time weighted-median dynamics. An order statistic is \(1\)-Lipschitz for the maximum norm; the right-hand side is globally Lipschitz, so there is a unique solution for every real initial vector and all future times.

For an arbitrary four-regular graph, the median comprises the agent itself and its four distinct neighbors. A **feedback vertex set** is a vertex set whose removal leaves an acyclic graph. The pinning criterion is exact for this graph class; it is not claimed for differently weighted or differently connected graphs.

## Proof

**Step 1: cohesive subsets are graph cycles.** Let \(Q=V\setminus P\). Call a nonempty \(S\subseteq Q\) cohesive when the weight assigned within \(S\) is at least one half for every \(v\in S\). For a four-regular graph with one self-weight and four neighbor-weights, all equal to \(1/5\), the condition is exactly
\[
\frac{1+\deg_{G[S]}(v)}5\ge\frac12\quad\Longleftrightarrow\quad \deg_{G[S]}(v)\ge2\qquad(v\in S).
\]
A finite induced subgraph has a nonempty subgraph of minimum degree at least two if and only if it contains a cycle. Thus a nonempty unpinned cohesive subset exists precisely when \(G[Q]\) contains a cycle.

**Step 2: necessity of destroying every unpinned cycle.** Suppose \(C\subseteq Q\) is a simple cycle. Choose any \(a>u\), set every opinion on \(C\) initially equal to \(a\), and set all other initial opinions to \(u\). The interval \([u,a]\) is forward invariant because the five-input median and the pinned target both lie in that interval when every opinion does. At every vertex of \(C\), the vertex itself and both cycle neighbors have opinion \(a\), so the median is \(a\), irrespective of the other two inputs. Uniqueness/invariance shows these cycle opinions remain exactly \(a\) forever. Global target consensus therefore fails. The argument also handles extra chords on \(C\): they cannot reduce the three guaranteed entries equal to \(a\).

**Step 3: sufficiency and an explicit convergence rate.** Suppose \(G[Q]\) is a forest. Repeatedly remove a leaf or an isolated vertex from the remaining forest to order its vertices \(v_1,\ldots,v_m\). At the time \(v_j\) is removed, it has at most one neighbor among \(v_j,\ldots,v_m\) other than itself. Therefore at least three of its five median inputs come from pins or from \(v_1,\ldots,v_{j-1}\). A median of five lies between the minimum and maximum of any three specified inputs. For \(i\in P\) the scalar solution is \(x_i(t)-u=(x_i(0)-u)e^{-t}\). Inductively assume for all \(k<j\) that
\[
|x_{v_k}(t)-u|\le R e^{-t}\sum_{\ell=0}^{k}\frac{t^\ell}{\ell!}.
\]
The three specified inputs to the median of \(v_j\) are consequently within \(R e^{-t}\sum_{\ell=0}^{j-1}t^\ell/\ell!\) of \(u\). The variation-of-constants formula for the scalar equation \(\dot x_{v_j}=\operatorname{med}_5-x_{v_j}\) yields
\[
|x_{v_j}(t)-u|\le R e^{-t}+\int_0^t e^{-(t-s)}R e^{-s}\sum_{\ell=0}^{j-1}\frac{s^\ell}{\ell!}\,ds
=R e^{-t}\sum_{\ell=0}^{j}\frac{t^\ell}{\ell!}.
\]
This completes the induction. Its largest right-hand side is the asserted bound with \(m\) unpinned vertices, which tends to zero as \(t\to\infty\).

**Step 4: forests in the squared ring.** Let \(P\ne\varnothing\), write its elements in clockwise order, and denote by \(g_1,\ldots,g_p\) the positive clockwise steps from each pin to the next; their sum is \(n\). If some \(g_i\ge4\), there are three consecutive unpinned vertices in that gap, and they form a triangle because the ring connects distances one and two. If every \(g_i\) is two or three, the unpinned vertices in each gap form a path of one or two vertices, and the ends of successive paths are adjacent across their single separating pinned vertex. The resulting unpinned graph has a cycle winding around the ring. Conversely, if all gaps are at most three and some gap equals one, two consecutive pins cut this winding chain; all remaining unpinned edges lie in disjoint paths, so the induced graph is a forest. This proves the equivalence of the three conditions in the theorem, including the edge cases \(n=5,6\).

**Step 5: sharp minimum.** Any effective set with \(p\) pins has gaps at most three and at least one gap one; hence \(n=\sum g_i\le3p-2\). Necessarily \(p\ge\lceil(n+2)/3\rceil\). Conversely let \(p=\lceil(n+2)/3\rceil\) and \(d=3p-2-n\in\{0,1,2\}\). The positive clockwise gap list
\[
(1,\,3-d,\,\underbrace{3,\ldots,3}_{p-2\ \text{entries}})
\]
has sum \(n\), all entries at most three, and an entry one. It constructs an effective set attaining the lower bound.

**Step 6: enumeration of all optimal layouts.** Let \(p=p_n\) and let \(\delta_i=3-g_i\in\{0,1,2\}\). Then \(\sum\delta_i=D:=3p-n\), and an effective layout has at least one \(\delta_i=2\). Let \(c_p(D)\) be the number of ordered \(p\)-tuples of deficits satisfying these conditions. Double count pairs consisting of a labelled effective \(p\)-pin layout and a distinguished first pin: each layout is counted \(p\) times, while each starting ring vertex and allowed ordered deficit tuple determines one such pair. Therefore \(N_n=n c_p(D)/p\). If \(n\equiv1\pmod3\), \(D=2\) and \(c_p(D)=p\). If \(n\equiv0\pmod3\), \(D=3\) and \(c_p(D)=p(p-1)\). If \(n\equiv2\pmod3\), \(D=4\) and
\[
c_p(D)=\binom p2+p\binom{p-1}2=\frac{p(p-1)^2}{2}.
\]
Substitution proves the stated three exact counting formulas.

## Verification

The standalone, standard-library-only file `verification/verify.py` independently constructs the squared-cycle adjacency, tests its induced-forest condition by depth-first search, evaluates the cyclic gap criterion, and exhaustively enumerates every labelled pin subset for each ring order from 5 through 18. All 524,256 subsets satisfy the claimed equivalence; their minimum pin sizes and optimal-layout counts match the formulas. For 982 further orders from 19 through 1000, the program generates and checks an optimal gap construction. Forty-eight numerical Runge–Kutta trajectories provide supplementary checks against the quantitative upper bound. Run from the package root with `python verification/verify.py`.

The finite checks are not a proof for unbounded ring order or arbitrary initial opinions; Steps 1–6 provide those proofs.

## Relationship to prior work

Han, Hendrickx, Chen, and Mei (arXiv:2404.16318, originally posted 25 April 2024; current accessible text v3) prove that pinning achieves target consensus from all initial conditions exactly when every cohesive subset meets the pin set (Proposition 14, Section 4 and Appendix F). Their numerical investigation studies random weighted networks, not the exact optimum and all optimal layouts of the uniform five-neighbor ring. The graph-cycle equivalence above specializes their cohesive-set criterion to a concrete network family and adds a fully explicit exact pinning number, a structural characterization of every successful layout, an optimal-layout count, and a uniform time-dependent error estimate. The general cohesive-set criterion is explicitly prior work, not claimed as new.

Zhang, Liu, Chen, and Mei (arXiv:2408.01899v1, 4 August 2024) study a discrete-time prejudiced weighted-median system, prove a related cohesive-set control condition, and identify determination of minimum prejudiced sets as future work in their conclusion. The earlier weighted-median analysis of Mei and colleagues (arXiv:2212.08808) concerns the unpinned discrete-time model. Standard feedback-vertex-set terminology and its complexity are classical; the squared-cycle graph is not the Cartesian product of two cycles considered in Pike and Zou's decycling work. No claim of priority over an unexamined exact graph-power decycling formula is made.

## Limitations

The theorem is about *uniform five-input median weights*, a *fixed shared target*, and the *full-pinning* unit-rate control law defined above. Heterogeneous median weights, time-dependent targets, nonunit controls, different update mechanisms, and asymptotic consensus restricted to generic initial states are outside its scope. The quantitative bound is a general global upper bound, not asserted to be optimal for a given layout. Cyclic symmetry is not factored out in the enumeration: sites are distinctly labelled. The literature comparison is best-knowledge rather than a proof of uniqueness; specialist graph-power results outside the inspected sources could further limit originality.

## References

1. Y. Han, J. M. Hendrickx, G. Chen, W. Mei, *Modeling, Analysis, and Control of Continuous-Time Weighted-Median Opinion Dynamics*, arXiv:2404.16318 (v1 2024-04-25), Proposition 14, Section 4 and Appendix F. https://arxiv.org/html/2404.16318v3
2. R. Zhang, Z. Liu, G. Chen, W. Mei, *Convergence Analysis of Weighted-Median Opinion Dynamics with Prejudice*, arXiv:2408.01899v1 (2024-08-04), Theorem 4.1 and Section VI. https://arxiv.org/pdf/2408.01899
3. W. Mei, J. M. Hendrickx, G. Chen, F. Bullo, F. Dörfler, *Convergence, Consensus and Dissensus in the Weighted-Median Opinion Dynamics*, arXiv:2212.08808v1 (2022-12-17). https://arxiv.org/abs/2212.08808
4. D. A. Pike, Y. Zou, *Decycling Cartesian Products of Two Cycles*, SIAM J. Discrete Math. (2005), DOI:10.1137/S089548010444016X. https://doi.org/10.1137/S089548010444016X
