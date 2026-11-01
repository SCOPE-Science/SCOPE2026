# A sharp one-link crossover in two-hub bond-percolation networks

## Finding

**Theorem.** For every pair of integers \(a,b\ge1\), let \(D_{a,b}\) be the tree consisting of two adjacent hub vertices, with \(a\) distinct leaves attached to the first hub and \(b\) distinct leaves to the second. Set \(N=a+b+2\), and let \(0<p<1\). Independently retain every edge with probability \(p\), choose a source vertex uniformly from all \(N\) vertices, and let \(R(G;p)\) be the expected size of its retained-edge connected component. Add precisely one previously absent undirected edge, with the same retention probability \(p\), to maximize \(R\).

Assume \(a\ge b\) after relabeling the two hubs. Define
\[
H_{a,b}(p)=(a-1)(b-1)p^3+(-ab+4a+3b-6)p^2+(6-a-b)p-a.
\]
There exists exactly one \(p_*(a,b)\in(0,1)\) with \(H_{a,b}(p_*)=0\). Every optimal added edge is characterized as follows:

1. If \(0<p<p_*\), it connects a leaf of the *smaller* leaf class (the class with \(b\) leaves) directly to the opposite hub (the hub with \(a\) leaves). In the equal-size case \(a=b\), either orientation of this two-step shortcut is optimal.
2. If \(p=p_*\), the preceding two-step shortcuts tie exactly with every link between one leaf of each class.
3. If \(p_*<p<1\), precisely the links between a leaf of each class are optimal.

The word "precisely" includes all choices of leaves within a specified class. No new edge joining leaves within the same class is optimal. At \(p=0\) or \(p=1\), all added-edge placements have the same outcome, so those endpoints are excluded from the strict classification.

As exact examples, \(p_*(1,1)=1/4\), \(p_*(2,2)\approx0.4811943041\), and \(p_*(3,3)\approx0.5979116727\). The transition is between introducing a triangle and introducing a four-cycle. It occurs for *every* pair of positive leaf-class sizes, not just in a numerical example.

## Assumptions and scope

The model is finite, undirected, homogeneous independent **bond percolation**: the random status of each edge is independent. The mean outbreak interpretation applies to a one-source Reed–Frost-style model that is exactly coupled to independent retained edges. It does **not** assert equivalence for a general SIR epidemic with a variable individual infectious period or correlated outgoing contacts. Both hubs and all leaves are eligible as the uniformly sampled initial source. The optimization is over one added nonedge, not deletion, vaccination, temporal contact scheduling, optimization over a weighted edge, or a different initial-source law.

For \(G\) with connected components \(C\) in a sampled retained-edge subgraph, the conditional mean of the uniform-source cluster size is \(\sum_C|C|^2/N\). Thus \(R\) is a normalized all-pairs connectivity functional, not the expected number of connected components.

## Proof

**1. Baseline.** On the original tree, two vertices are connected exactly when every edge on their unique path is retained. Counting vertex pairs at distances one, two and three gives
\[
R(D_{a,b};p)=1+\frac2N\left[(a+b+1)p+
\left(a+b+\binom a2+\binom b2\right)p^2+abp^3\right].
\]

**2. Single-edge gain identity.** Let \(T\) be any finite tree, and let an added edge have endpoints \(v_0,v_d\), where \(v_0,v_1,\ldots,v_d\) is the original unique path and \(d\ge2\). Delete the path edges, and set \(W_i=\sum_{x\in B_i}p^{\operatorname{dist}(x,v_i)}\), where \(B_i\) is the component containing \(v_i\) after those deletions. For two vertices attached to distinct path vertices \(v_i,v_j\), \(i<j\), the new cycle offers two edge-disjoint ways to cross the path section: the original arc of length \(j-i\) and the alternative arc of length \(d+1-j+i\). Pendant paths must succeed in either case. Independence therefore makes their connectivity *gain* exactly
\[
p^{\operatorname{dist}(x,v_i)+\operatorname{dist}(y,v_j)}
 p^{d+1-(j-i)}(1-p^{j-i}).
\]
Pairs attached to the same path vertex do not gain a connection, because their sole pendant-tree path was already necessary and sufficient. Summing over all unordered pairs yields the exact identity
\[
R(T+v_0v_d;p)-R(T;p)=\frac2{|V(T)|}
\sum_{0\le i<j\le d}W_iW_jp^{d+1-j+i}(1-p^{j-i}).\tag{1}
\]
This is an identity for *every* finite tree, not a truncated low-transmission expansion.

**3. All possible edge placements.** There are five symmetry types: \(A\) joins two leaves at the first hub, \(B\) joins two leaves at the second hub, \(C\) joins a first-hub leaf to the second hub, \(D\) joins a second-hub leaf to the first hub, and \(E\) joins leaves from opposite hubs. Types \(A,B\) exist only if their leaf class has at least two members. Define \(g_X=N[R(D_{a,b}+e_X;p)-R(D_{a,b};p)]/2\). Evaluating (1) on the respective paths of lengths two, two, two, two and three gives
\[
\begin{aligned}
g_A={}&p(1-p)[1+3p+2(a-1)p^2+2bp^3],\\
g_B={}&p(1-p)[1+3p+2(b-1)p^2+2ap^3],\\
g_C={}&p(1-p)[1+(b+3)p+2(a+b-1)p^2+b(a-1)p^3],\\
g_D={}&p(1-p)[1+(a+3)p+2(a+b-1)p^2+a(b-1)p^3],\\
g_E={}&p(1-p)[1+3p+(a+b+4)p^2+3(a+b-2)p^3+(a-1)(b-1)p^4].
\end{aligned}
\]
For \(a\ge2\) and \(b\ge2\), respectively,
\[
\begin{aligned}
g_C-g_A&=bp^2(1-p)[1+2p+(a-3)p^2]>0,\\
g_D-g_B&=ap^2(1-p)[1+2p+(b-3)p^2]>0.
\end{aligned}
\]
The brackets are positive even in the smallest admissible case, since \(1+2p-p^2>0\) for \(0<p<1\). Also
\[
g_D-g_C=(a-b)p^2(1-p)^2(1+p)\ge0.
\]
Thus for \(a\ge b\) the sole remaining comparison is \(E\) against \(D\) (with a symmetric tie between \(C,D\) when \(a=b\)). Direct subtraction gives
\[
g_E-g_D=p^2(1-p)H_{a,b}(p).\tag{2}
\]

**4. The crossover is unique.** We have \(H_{a,b}(0)=-a<0\) and \(H_{a,b}(1)=a+b+1>0\). Express the cubic in its degree-three Bernstein basis as
\[
H_{a,b}(p)=\sum_{j=0}^3\binom3j B_jp^j(1-p)^{3-j},
\quad(B_0,B_1,B_2,B_3)
=\left(-a,\frac{6-4a-b}{3},\frac{6-ab-a+b}{3},a+b+1\right).
\]
For \(a\ge b\ge1\) with \(a\ge2\), the first two coefficients are strictly negative, the last is positive, and the third can have either sign. Therefore their sequence has precisely one sign change. In the only remaining case \(a=b=1\), the sequence is \((-1,1/3,5/3,3)\), again with exactly one sign change. On putting \(t=p/(1-p)>0\), the polynomial \(H_{a,b}(p)/(1-p)^3\) becomes \(B_0+3B_1t+3B_2t^2+B_3t^3\). Descartes' rule therefore bounds the number of positive zeros, counted with multiplicity, by one. The opposite endpoint signs guarantee one such zero, so it is simple and unique. By (2), \(D\) wins before it, \(E\) after it, and they tie at it. The strict comparisons in step 3 finish the complete optimizer classification.

## Verification

The self-contained Python 3 checker `verify.py` uses exact fractions and direct enumeration of retained-edge subsets; it has no external dependencies. Running `python verify.py` returned `VERIFY_OK assertions= 45695`. It checks all missing-edge classes for leaf-class sizes \(1\) through \(4\), at four rational probabilities; independently computes expected cluster size by summing squared component sizes for every retained-edge subgraph; and tests the algebraic comparison identities on a larger rational parameter grid through leaf size \(30\). The symbolic proof above, not this finite experiment, verifies the all-integer and all-real theorem. The printed assertion count is generated by the enclosed program, not an independent formal certificate.

## Relationship to prior work

Newman, Jensen and Ziff (2002) establish epidemic/percolation motivation for sparse networks. Kenah and Robins (2006/2007) explain when the bond-percolation representation of an epidemic is and is not valid. Youssef, Khorramzadeh and Eubank (2013) analyze network reliability and average-component attack-rate criteria, including the impact of triangles and degree mixing. Khorramzadeh and collaborators (2014/2015) analyze structural-motif reliability and already exhibit parameter-dependent edge-importance reversals for a different two-terminal deletion problem. Consequently neither the general bond-percolation framework nor the existence of *some* reliability-ranking crossover is claimed here as new.

The result here is the exact **all-pairs** optimizer classification after one added edge in every unequal-size double-star, with a unique algebraic crossover and all equality cases. No inspected primary work supplied the stated \(H_{a,b}\) optimizer criterion or a stronger theorem directly covering it. Earlier equivalent pair-connectivity augmentation literature remains a priority risk.

## Limitations

The link is optimized for **increasing** the expected cluster size; a public-health planner seeking containment would reverse the intervention objective, and the theorem does not compare deletion or vaccination. Independent homogeneous undirected edges, exactly one added nonedge, and a uniform seed are essential assumptions. The method does not address nonlinear disease dynamics, repeated contacts, nonuniform individual infectiousness, heterogeneous edge probabilities, multi-link investment, time-to-infection, or realized-outbreak variance. Exact originality beyond inspected literature is not independently certified.

## References

1. M. E. J. Newman, I. Jensen, R. M. Ziff, *Percolation and epidemics in a two-dimensional small world*, Physical Review E **65**, 021904 (first published 2002-01-16). https://doi.org/10.1103/PhysRevE.65.021904
2. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, arXiv:q-bio/0610057 (first posted 2006-10-30); Physical Review E **76**, 036113 (2007). https://arxiv.org/abs/q-bio/0610057
3. M. Youssef, Y. Khorramzadeh and S. Eubank, *Network reliability: The effect of local network structure on diffusive processes*, arXiv:1308.4577 (first posted 2013-08-21), Physical Review E **88**, 052810 (2013). https://arxiv.org/abs/1308.4577
4. Y. Khorramzadeh, M. Youssef, S. Eubank and S. Mowlaei, *Analyzing network reliability using structural motifs*, arXiv:1403.7074 (first posted 2014-02-05), Physical Review E **91**, 042814 (2015). https://arxiv.org/abs/1403.7074
