# Sharp degree-targeting losses in directed-tree opinion optimization

## Finding

**Theorem (sharp failure hierarchy of highest-in-degree intervention, and a linear-time exact alternative).** Fix an integer \(\Delta\ge 2\). Consider all finite directed trees on \(n\) vertices in which every arc points toward a unique sink, precisely one vertex \(h\) has in-degree \(\Delta\), and every other vertex has in-degree at most \(\Delta-1\). Give every agent innate opinion \(1\), and apply the unweighted directed Friedkin–Johnsen update
\[
 z_i(t+1)=\frac{s_i+\sum_{i\to j}z_j(t)}{1+\deg^+(i)}.
\]
An intervention changes one innate opinion from \(1\) to \(0\); the benefit is the resulting decrease in the sum of equilibrium expressed opinions. Let \(G_i\) denote that benefit for intervention at \(i\). Let \(R_\Delta(n)\) be the supremum of \(\max_i G_i/G_h\) over the stated class of \(n\)-vertex trees. For all sufficiently large admissible \(n\),
\[
 R_\Delta(n)=
 \begin{cases}
 \Theta_\Delta(1),&\Delta=2,\\
 \Theta(\log n),&\Delta=3,\\
 \Theta_\Delta\!\left(n^{\log_{\Delta-1}((\Delta-1)/2)}\right),&\Delta\ge4.
 \end{cases}
\]
Here \(\Theta_\Delta\) means that positive upper and lower constants may depend on the *fixed* integer \(\Delta\), but not on \(n\). The highest-in-degree choice is unambiguous because the maximizer of in-degree is unique. The logarithmic and polynomial lower bounds hold on explicit, weakly connected trees with uniform innate opinions; they do not rely on strategic tie-breaking or heterogeneous parameters.

More generally, consider any finite loop-free directed functional graph: each vertex has at most one outgoing arc, with successor \(f(i)\) if one exists. Let \(q_i\in[0,1)\) be susceptibility, with \(q_i=0\) at sinks, let \(s_i\in[0,1]\) be innate opinion, and let \(a_i\ge0\) be the importance weight of observing expressed opinion \(z_i\). Under
\[
 z_i(t+1)=(1-q_i)s_i+q_i z_{f(i)}(t)
\]
(the second term is absent at sinks), all \(n\) exact one-vertex intervention gains and an optimal intervention set of **any prescribed cardinality** \(k\in\{0,\ldots,n\}\) can be computed in \(O(n)\) real-arithmetic and comparison operations and \(O(n)\) space. This algorithm makes the above inefficiency of a local degree rule avoidable on this entire network class. Its linear bound is in the arithmetic/comparison model, not a uniform bit-complexity claim.

## Assumptions and scope

All graphs are finite, with no self-loops or parallel arcs. In-degree means number of arcs entering a vertex; out-degree means number leaving it. A directed in-arborescence is a weakly connected acyclic directed graph with a unique sink in which each non-sink vertex has exactly one outgoing arc directed to its parent. The integer \(\Delta\) is fixed as \(n\) grows. For \(n\ge\Delta+1\), examples exist. The denominator \(G_h\) is always positive. No probabilistic initial states, random graphs, or approximation assumptions are used. For the algorithmic statement, susceptibilities may differ between vertices but satisfy \(q_i<1\), including on all directed cycles. The nonnegative observation weights and innate opinions are arbitrary.

Benefits are stated as reductions in the **sum** of expressed opinions; dividing every benefit by \(n\) gives precisely the same ratios and optimal intervention sets for average expressed opinion.

## Proof

**1. Exact influence reduction.** Define a sparse matrix \(Q\) by \(Q_{i,f(i)}=q_i\) at a non-sink vertex and zero row at each sink. Let \(B=\operatorname{diag}(1-q_i)\). The update is \(z(t+1)=Bs+Qz(t)\). Because \(\lVert Q\rVert_\infty=\max_i q_i<1\), the equilibrium exists uniquely and equals \(z=(I-Q)^{-1}Bs\). For arbitrary observation weights \(a\ge0\), set
\[
 v=(I-Q^\top)^{-1}a,\qquad G_i=(1-q_i)s_iv_i.
\]
Indeed, by linearity, changing \(s_i\) to zero decreases \(a^\top z\) by exactly \(G_i\). Thus the optimal set of cardinality \(k\) consists of the \(k\) largest nonnegative gains. This recovers the top-influence selection principle of Sun and Zhang; the new performance statement below concerns the *degree-based* proxy on a sharply specified graph class.

**2. Linear-time functional-graph calculation.** The sparse linear system for \(v\) is
\[
 v_i=a_i+\sum_{j:f(j)=i}q_jv_j.
\]
Initialize \(h_i=a_i\). Iteratively peel every vertex having zero current incoming-arc count: set \(v_i=h_i\), and if \(f(i)\) exists, add \(q_iv_i\) to \(h_{f(i)}\) before decrementing the incoming-arc count of its successor. Each vertex and arc is processed once. The unpeeled subgraph is a disjoint union of directed cycles. For a cycle \(c_0\to c_1\to\cdots\to c_{m-1}\to c_0\), with indices interpreted modulo \(m\), the equations are
\[
 v_{c_j}=h_{c_j}+q_{c_{j-1}}v_{c_{j-1}}.
\]
They have the explicit solution
\[
 v_{c_0}=
 \frac{\displaystyle\sum_{t=0}^{m-1}
      h_{c_{-t}}\prod_{r=1}^{t}q_{c_{-r}}}
      {\displaystyle1-\prod_{j=0}^{m-1}q_{c_j}}.
\]
The denominator is strictly positive because all \(q_i<1\). A forward traversal recovers the other \(m-1\) values. Total work is \(O(n)\). After computing gains, a deterministic linear-time selection algorithm isolates the top \(k\); ties can be settled by vertex index. No matrix inverse needs to be constructed.

**3. Weighted descendant formula on trees.** In the original unweighted model, every non-sink has out-degree \(1\), so \(q_i=1/2\); the unique sink has \(q_i=0\). Observation and innate weights are all \(1\). For every vertex \(i\), let \(N_t(i)\) count descendants whose directed distance to \(i\) is \(t\), with \(N_0(i)=1\). The finite Neumann series for the transposed system gives
\[
 v_i=\sum_{t\ge0}2^{-t}N_t(i),\quad
 G_i=\begin{cases}v_i/2,&i\text{ is not the sink},\\v_i,&i\text{ is the sink}.\end{cases}
\]
This rooted-tree centrality expression is a specialization of established PageRank level-count formulas; it is included to prove the new extremal performance theorem rather than claimed as a new formula.

**4. Universal upper bounds.** Put \(b=\Delta-1\). Except for the single exceptional vertex \(h\), every vertex has at most \(b\) children; \(h\) has \(b+1\). In a descendant tree with no exceptional vertex, \(N_t(i)\le b^t\). If \(h\) occurs at a depth less than \(t\), its one extra child adds at most \(b^{t-1}\) vertices at depth \(t\). Consequently, for all vertices and all \(t\ge0\),
\[
 N_t(i)\le2b^t,\qquad N_t(i)\le n.
\]
For \(b=1\), \(v_i\le2\sum_{t\ge0}2^{-t}=4\). For \(b=2\), splitting the sum at \(\lceil\log_2 n\rceil\) gives \(v_i=O(\log n)\). For \(b\ge3\), splitting at \(\lceil\log_b n\rceil\) gives
\[
 v_i\le 2\sum_{t\ge0}2^{-t}\min\{b^t,n\}
 =O_b\!\left(n^{\log_b(b/2)}\right).
\]
Since \(h\) is either the sink or a non-sink, its gain obeys \(G_h=(1-q_h)v_h\ge1/2\), because \(v_h\ge1\). Since \(G_i\le v_i\), the same upper bounds apply to \(\max_iG_i/G_h\).

**5. Matching lower bounds with a unique high-degree decoy.** For each \(b=\Delta-1\ge2\) and integer \(L\ge1\), take a complete \(b\)-ary tree of depth \(L\), orient every arc toward its root \(y\), and append \(P=L\lceil\log_2 b\rceil\) intermediate vertices in a directed path from \(y\) to a new sink \(h\). Add exactly \(b\) fresh leaves pointing into \(h\). Now \(h\) has in-degree \(b+1\), the sole maximum; every other vertex has in-degree at most \(b\). The node count is
\[
 n_L=\frac{b^{L+1}-1}{b-1}+P+b+1=\Theta_b(b^L).
\]
At the root \(y\) of the complete subtree and at the sink \(h\), direct substitution into the recurrence gives
\[
 v_y=\sum_{t=0}^{L}(b/2)^t,
 \qquad
 v_h=2+\frac b2-2^{-P}+2^{-(P+1)}v_y.
\]
As \(2^P\ge b^L\), the second quantity is bounded above by a constant depending on \(b\) alone; in fact \(2^{-(P+1)}v_y\le \tfrac12\sum_{t=0}^L(b/2)^t b^{-L}\), which is bounded. But \(G_y=v_y/2\) while \(G_h=v_h\). Thus \(G_y/G_h=\Omega(L)\) for \(b=2\) and \(\Omega_b((b/2)^L)=\Omega_b(n_L^{\log_b(b/2)})\) for \(b\ge3\). For every sufficiently large intermediate order \(n\), take the largest \(L\) with \(n_L\le n\), and subdivide the directed path between \(y\) and \(h\) using the \(n-n_L\) surplus vertices. This leaves \(v_y\) unchanged, decreases the contribution of \(y\) to \(v_h\), and preserves the unique maximum in-degree. Since \(n<n_{L+1}=O_b(b^L)\), the same asymptotic lower bound holds for every large \(n\), not merely a subsequence. For \(b=1\), the trivial inequality \(\max_i G_i/G_h\ge1\), together with Step 4, completes the constant-order case.

All cases, including \(\Delta=2\) and the logarithmic transition at \(\Delta=3\), follow.

## Verification

The standalone standard-library script `verify.py` implements exact rational peeling/cycle resolution and an independent Gaussian-elimination baseline. Running `python verify.py` performs: (a) 3,413 exhaustive functional-successor configurations on up to five vertices; (b) 880 heterogeneous rational-model comparisons; (c) 880 brute-force intervention-set optimality checks; (d) nine explicit decoy-family checks and 27 further variable-degree family checks. It terminates with `ALL_CHECKS_PASS`. These finite checks test the implementation and special cases, while the proof above establishes the unbounded asymptotic statements.

## Relationship to prior work

Sun and Zhang (2023) establish the centrality-product criterion for exactly optimal opinion intervention on arbitrary directed networks, with an \(O(n^3)\) inverse-based method and a fast randomized approximation. Their Section 6 explicitly compares an in-degree heuristic experimentally. The present theorem does **not** reassert their selection criterion as new; it determines the sharp order of the worst-case loss of that heuristic on fixed-degree directed trees, including a transition from bounded to logarithmic to polynomial loss.

Arratia and Marijuán (2016) derive a PageRank formula using rooted-tree level counts and study effects of link rearrangements. That known formula supports Step 3, but a root-score formula by itself does not imply the two-sided worst-case degree-heuristic ratio with a unique high-in-degree decoy. Fortunato and colleagues (2005) study approximating PageRank from in-degree in Web networks, chiefly under degree-correlation assumptions; their abstract is available but the complete work was not examined here. Shrinate and Tripathy (2024) study influence centrality in signed FJ systems, rather than the stated degree-heuristic extremal guarantee. A 2026 paper by Sun and collaborators develops faster sampling-based FJ algorithms; its contributions are not asserted to provide this degree-heuristic ratio.

## Limitations

The sharp \(R_\Delta(n)\) theorem requires constant \(\Delta\), all innate opinions equal to \(1\), a *unique* highest-in-degree vertex, uniform averaging, and a single selected intervention on an in-arborescence. It is an asymptotic order-of-growth statement, not an exact finite-\(n\) extremal value or a claim for networks with unrestricted in-degree or multiple outgoing arcs. The exact algorithm is stated for functional directed networks with \(q_i<1\), without self-loops, under a real-arithmetic cost model; exact rational bit lengths can grow with input. No claim is made that the rooted-tree PageRank formula, centrality-product selection rule, or generic sparse-matrix solution methods are new. Exhaustiveness of external priority search is not guaranteed; an equivalent result under another name or formulation remains possible. No independent external validation has occurred.

## References

1. H. Sun and Z. Zhang, *Opinion Optimization in Directed Social Networks*, Proceedings of the AAAI Conference on Artificial Intelligence 37(4), 4623–4632 (2023), first published 2023-06-26, https://doi.org/10.1609/aaai.v37i4.25585 ; full text https://arxiv.org/abs/2306.16847 .
2. A. Arratia and C. Marijuán, *On graph combinatorics to improve eigenvector-based measures of centrality in directed networks*, Linear Algebra and its Applications 504, 325–353 (2016), https://doi.org/10.1016/j.laa.2016.04.011 .
3. S. Fortunato, M. Boguñá, A. Flammini and F. Menczer, *How to make the top ten: Approximating PageRank from in-degree* (2005), https://arxiv.org/abs/cs/0511016 .
4. A. Shrinate and T. Tripathy, *Absolute centrality in a signed Friedkin-Johnsen based model: a graphical characterisation of influence* (2024), https://arxiv.org/abs/2410.00456 .
5. H. Sun, Y. Sun, X. Zhou and Z. Zhang, *Fast Computation and Optimization for Opinion-Based Quantities of Friedkin-Johnsen Model* (2026), https://arxiv.org/abs/2606.26601 .
