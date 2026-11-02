# Exact weighted-variation amplification at every radius of tree max-dilation

## Finding

Let \(T=(V,E)\) be any finite undirected tree with at least two vertices, and give each edge a strictly positive variation weight \(w_e\). Define the radius-\(k\) neighborhood-max operator for real vertex signals by
\[
 (M_k f)(v)=\max\{f(u):d_T(u,v)\le k\},\qquad k\in\mathbb Z_{\ge0},
\]
where graph distance counts edges, independently of their variation weights. Define \(J_w(f)=\sum_{uv\in E}w_{uv}|f(u)-f(v)|\) and the sharp **one-input variation-gain constant**
\[
 K_k(T,w)=\sup_{J_w(f)>0}\frac{J_w(M_k f)}{J_w(f)}.
\]
For any oriented edge \(a\to b\), delete \(ab\) and write \(C_b\) for the component containing \(b\). Define its outward weighted wave
\[
 F_k(a\to b)=\sum_{\substack{xy\in E(C_b)\\
 \{d_{C_b}(b,x),d_{C_b}(b,y)\}=\{k-1,k\}}}w_{xy}\qquad(k\ge1).
\]
Then, for every \(k\ge1\),
\[
 \boxed{K_k(T,w)=\max_{a\to b\in\vec E}\frac{F_k(a\to b)}{w_{ab}}.}
\]
Every individual ratio is realized by the two-level indicator of the component containing \(a\) after deleting \(ab\). Thus the optimum, including the case \(K_k=0\), is attained by a single-edge separating cut. Also \(K_0=1\).

For one step this specializes to
\[
 K_1(T,w)=\max_{a\to b\in\vec E}\frac{\sum_{bc\in E,\ c\ne a}w_{bc}}{w_{ab}}.
\]
Consequently \(J_w(M_1 f)\le J_w(f)\) for all \(f\) **if and only if** \(T\) is a path and all its edge variation weights are equal (the single-edge path is included). The same assertions hold for the radius-\(k\) neighborhood-min operator by sign reversal.

For unit edge weights and maximum degree \(\Delta\ge2\),
\[
 \boxed{K_k(T,1)\le(\Delta-1)^k\qquad(k\ge1).}
\]
The exponential bound is simultaneously sharp over any prescribed initial range of radii: for every integers \(b\ge1\), \(h\ge1\), take the full \(b\)-ary rooted tree of height \(h\), and attach one extra leaf to its root. On this tree, whose maximum degree is \(b+1\) for \(b\ge2\),
\[
 K_k=b^k\quad(1\le k\le h),\qquad K_k=0\quad(k\ge\operatorname{diam}(T)).
\]
For \(b=1\), it is a path and the same initial-radius formula holds. This exhibits large but transient variation amplification followed by eventual constant-output collapse.

## Assumptions and scope

The graph is a finite tree on at least two vertices; all variation edge weights are strictly positive real numbers, but the max-filter radius uses **unweighted hop distance**. Signals are arbitrary real-valued functions on vertices. The exact constant is the ratio of the variation of **one output** to that of its input, not the global two-input Lipschitz constant of this nonlinear operator. Graph distance, variation weights, and the interpretation of sharpness must not be interchanged. The orientation in \(a\to b\) denotes a directed choice of a tree edge, not a directed tree.

## Proof

**1. Threshold decomposition.** For a real signal \(f\) set \(S_t=\{v:f(v)>t\}\). For any edge \(uv\), the layer-cake identity gives
\[
 |f(u)-f(v)|=\int_{\mathbb R}|\mathbf 1_{S_t}(u)-\mathbf 1_{S_t}(v)|\,dt.
\]
Writing \(\partial S\) for the set of edges with exactly one endpoint in \(S\), it follows that \(J_w(f)=\int_{\mathbb R}w(\partial S_t)\,dt\). The superlevel set of \(M_kf\) is exactly \(N_k[S_t]=\{v:d_T(v,S_t)\le k\}\). Consequently
\[
 K_k=\max_{\varnothing\ne S\subsetneq V}\frac{w(\partial N_k[S])}{w(\partial S)}.
\]
All denominators are positive because the tree is connected. Equality in this reduction is attained with \(f=\mathbf 1_S\).

**2. Charging the outer boundary to original cut edges.** Fix \(k\ge1\), a nonempty proper \(S\), and an edge \(xy\in\partial N_k[S]\), oriented so that \(x\in N_k[S]\), \(y\notin N_k[S]\). The graph-distance Lipschitz property forces \(d_T(x,S)=k\) and \(d_T(y,S)=k+1\). Choose any nearest \(s\in S\) to \(x\). Along the unique \(s\)-to-\(x\) path, the first edge is \(e=sb\in\partial S\): if the first step stayed inside \(S\), that step would furnish a closer vertex of \(S\). The same unique path gives \(d_{C_b}(b,x)=k-1\). The edge \(xy\) points away from \(s\), since otherwise \(d_T(y,S)\le k-1\). Hence \(xy\in E(C_b)\) lies between levels \(k-1\) and \(k\) from \(b\), and is counted in \(F_k(s\to b)\).

Assign each boundary edge \(xy\) to one such \(e\) (using any deterministic tie-break). Distinct assigned boundary edges remain distinct, so
\[
 w(\partial N_k[S])\le\sum_{s\to b\in\partial S} F_k(s\to b)
 \le\biggl(\max_{a\to b}\frac{F_k(a\to b)}{w_{ab}}\biggr)w(\partial S).
\]
This proves the upper bound simultaneously for all real signals by Step 1.

**3. Exact witnesses.** Fix \(a\to b\) and let \(S\) be the entire component containing \(a\) after deletion of \(ab\). Its boundary is just \(\{ab\}\). Vertices in \(C_b\) lie in \(N_k[S]\) precisely when their distance from \(b\) is at most \(k-1\); vertices of \(S\) are all included. The outer boundary is therefore exactly the level-\((k-1,k)\) wave of total weight \(F_k(a\to b)\). Its indicator attains the ratio \(F_k(a\to b)/w_{ab}\). Maximization gives the claimed formula, including zero gain when every wave is empty. For \(k=0\), \(M_0\) is the identity.

**4. Characterization of one-step contraction.** With \(k=1\), the wave is the sum of all edges incident to \(b\) other than \(ab\). If a vertex \(b\) has degree at least three and \(ab\) is incident with minimum weight, the remaining weight is at least twice \(w_{ab}\), contradicting \(K_1\le1\). Thus a contractive tree has degree at most two and is a path. At an internal path vertex, the two orientations imply simultaneously \(w_1\le w_2\) and \(w_2\le w_1\), so adjacent weights are equal; connectivity makes every path weight equal. The converse follows directly from the one-step formula. For a single edge, \(K_1=0\), consistent with the criterion.

**5. Growth and exhaustion.** If every degree is at most \(\Delta\ge2\), the outward component from any oriented edge has at most \(\Delta-1\) children per vertex. Induction shows its \(k\)-th frontier contains at most \((\Delta-1)^k\) edges. With unit weights this bounds every ratio. On the full \(b\)-ary height-\(h\) tree with one extra root leaf, orient the extra leaf's edge toward the root. Its outward wave has exactly \(b^k\) edges for \(1\le k\le h\), attaining the universal bound. Finally, when \(k\) is at least the tree diameter, every radius-\(k\) neighborhood is the whole vertex set, so \(M_k f\) is constant and \(K_k=0\). The minimum operator is \(-M_k(-f)\), preserving the variation ratio.

## Verification

Run the standalone `verify.py` using Python 3 and its standard library. It independently constructs each oriented-edge frontier, exhaustively searches every nontrivial indicator cut on 304 reproducible random positively integer-weighted trees with 2–10 vertices, and compares the two sharp constants at 1,628 tree-radius combinations. This amounts to 318,280 tested indicator cuts. It also verifies 11,309 nonconstant integer-valued signal inequalities and 12 explicitly constructed branching families. Exact rational arithmetic is used for variation ratios. The successful run prints `PASS`. None of these finite tests is used as a substitute for the universal proof above.

## Relationship to prior work

Classical graph mathematical morphology defines dilation and its neighborhood iterations, including grayscale threshold stacking; see Najman–Cousty (2014) and Cousty–Najman–Dias–Serra (2013). Finite tree total variation is a separate established setting, as in Kolmogorov–Pock–Rolinek (2015), whose topic is optimization by dynamic programming. Sandryhaila–Moura (2013) investigates a different adjacency-based graph-signal variation functional and linear filters. The mathematical object proved here is neither a new definition of graph dilation nor a new definition of graph variation: it is their **exact all-radius weighted seminorm gain** on trees, with single-edge extremizers and sharp branching transients. A previously implicit equivalent in earlier morphology literature has not been excluded.

## Limitations

The theorem is for finite trees and the one-input output/input variation ratio. It does not establish the two-input global Lipschitz constant of the nonlinear dilation, characterize arbitrary cyclic graphs, or apply to radius defined using the positive variation weights as metric lengths. A highly relevant 2013 morphology paper was not available for full-text inspection; therefore priority remains conditional on the incompleteness of that literature comparison. Independent external mathematical validation has not been performed.

## References

1. L. Najman and J. Cousty, *A graph-based mathematical morphology reader* (first public arXiv version 2014-04-30), arXiv:1404.7748, https://arxiv.org/abs/1404.7748.
2. J. Cousty, L. Najman, F. Dias and J. Serra, *Morphological filtering on graphs*, Computer Vision and Image Understanding 117 (2013), 370–385, DOI:10.1016/j.cviu.2012.08.016. Public abstract: https://cris.technion.ac.il/en/publications/morphological-filtering-on-graphs/.
3. V. Kolmogorov, T. Pock and M. Rolinek, *Total variation on a tree* (first public arXiv version 2015-02-26), arXiv:1502.07770, https://arxiv.org/abs/1502.07770.
4. A. Sandryhaila and J. M. F. Moura, *Discrete Signal Processing on Graphs: Frequency Analysis* (first public arXiv version 2013-07-01), arXiv:1307.0468, https://arxiv.org/abs/1307.0468.
