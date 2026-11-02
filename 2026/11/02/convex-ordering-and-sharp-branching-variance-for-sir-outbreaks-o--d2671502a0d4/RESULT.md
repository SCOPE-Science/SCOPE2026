# Convex ordering and sharp branching variance for SIR outbreaks on finite trees

## Finding

**Theorem (finite rooted-tree transmissibility dispersion).** Let \(G=(V,E)\) be a finite tree on \(n\ge2\) vertices with one initially infected root \(r\). Each infected vertex \(v\) draws an independent identically distributed random variable \(\Theta_v\in[0,1]\). Conditional on \(\Theta_v=\theta\), it independently transmits to each of its susceptible neighbors with probability \(\theta\); transmission along the tree produces no reinfection. Let \(N\) be the total number ever infected, \(p=\mathbb E\Theta_v\in(0,1)\), \(q=\mathbb E\Theta_v^2\), and \(d_v=d(r,v)\). Write \(a(v,w)\) for the least common ancestor of \(v,w\), and \(\ell(v,w)=d_{a(v,w)}\). Two vertices are *incomparable* when neither lies on the other's root path.

The expected outbreak size is independent of the distribution beyond its mean:
\[
\mathbb E N=\sum_{v\in V}p^{d_v}.
\]
The variance is exactly
\[
\boxed{\operatorname{Var}(N)=V_{\rm ind}(G,r,p)+\operatorname{Var}(\Theta_v)\,B(G,r,p),}
\]
where \(V_{\rm ind}\) is the variance for independent Bernoulli transmission of probability \(p\), given explicitly by
\[
V_{\rm ind}=\sum_{v\in V}p^{d_v}(1-p^{d_v})
+2\sum_{\{v,w\}\subset V}\left(p^{d_v+d_w-\ell(v,w)}-p^{d_v+d_w}\right),
\]
and the strictly nonnegative branching index is
\[
\boxed{B(G,r,p)=2\sum_{\substack{\{v,w\}\subset V\\v,w\ \mathrm{incomparable}}}
 p^{d_v+d_w-\ell(v,w)-2}.}
\]
For every \(n\ge3\) and \(0<p<1\), the sharp structural bounds are
\[
0\le B(G,r,p)\le(n-1)(n-2).
\]
Equality at the lower endpoint holds **exactly** for a path rooted at an endpoint; equality at the upper endpoint holds **exactly** for a star rooted at its center. Since \(0\le\operatorname{Var}(\Theta_v)\le p(1-p)\), the resulting variance bounds are sharp among all laws on \([0,1]\) with mean \(p\):
\[
\boxed{V_{\rm ind}\le\operatorname{Var}(N)\le V_{\rm ind}+p(1-p)B(G,r,p).}
\]
The lower bound is attained by the deterministic \(\Theta_v\equiv p\); the upper bound is attained by the two-point law \(\mathbb P(\Theta_v=1)=p\), \(\mathbb P(\Theta_v=0)=1-p\).

More strongly, **all convex outbreak-size costs are ordered**: for two i.i.d. transmissibility laws satisfying \(\Theta^{(1)}\le_{\rm cx}\Theta^{(2)}\) (convex order, necessarily with the same mean),
\[
\boxed{N^{(1)}\le_{\rm cx}N^{(2)}.}
\]
Thus the preceding variance inequality is part of a distributional ordering, not merely a moment comparison. If \(G\) branches as a rooted tree and \(\operatorname{Var}(\Theta^{(1)})<\operatorname{Var}(\Theta^{(2)})\), the variance inequality is strict. If the root has exactly one descendant chain, the entire outbreak-size distribution depends only on \(p\).

## Assumptions and scope

The graph is finite, simple, undirected, acyclic, and completely susceptible except for one designated initial case. Each \(\Theta_v\) is sampled independently, and conditional child-edge trials from that vertex are independent; different vertices' trials are independent conditional on all \(\Theta_v\). A standard continuous-time SIR realization has independent Poisson transmission-attempt processes of common rate \(\beta>0\) on each directed edge and i.i.d. infectious durations \(T_v\ge0\), in which case \(\Theta_v=1-e^{-\beta T_v}\). The theorem compares distributions with the *same mean transmissibility* \(\mathbb E(1-e^{-\beta T_v})=p\), **not** necessarily the same mean duration. The upper two-point law permits \(\Theta_v=1\), which corresponds to an infinite duration in that realization; among finite-duration laws it is a sharp supremum, approximable by arbitrarily long durations.

The comparison is for the complete eventual outbreak count; it is not a statement about epidemic timing or about graphs containing cycles. For \(n=2\), the branching index is zero.

## Proof

**1. Pairwise infection indicators.** Orient each edge away from \(r\). There is exactly one route from the initial case to any \(v\). Let \(I_v\) denote the indicator of eventual infection. Every edge on that route has marginal success probability \(p\), and its transmitting source is different from the source of every other route edge; therefore
\[
\mathbb E I_v=p^{d_v}.
\]
For two distinct vertices \(v,w\) with least-common-ancestor depth \(\ell=\ell(v,w)\), if one is an ancestor of the other, both are infected precisely when the deeper one is infected, so
\[
\mathbb E(I_vI_w)=p^{d_v+d_w-\ell}.
\]
If neither is an ancestor, their common initial route has \(\ell\) transmissions, then two distinct outgoing trials from their common ancestor must both succeed. Those two trials have unconditional joint probability \(\mathbb E\Theta^2=q\), while all remaining source vertices on the two branches are distinct. Hence
\[
\mathbb E(I_vI_w)=q\,p^{d_v+d_w-\ell-2}.
\]
The exponent is a nonnegative integer because the two vertices are incomparable. Subtracting the independent-edge benchmark, whose joint probability equals \(p^{d_v+d_w-\ell}\), leaves precisely \((q-p^2)p^{d_v+d_w-\ell-2}\) for each incomparable pair and zero for each comparable pair. Using \(N=\sum_v I_v\), expanding \(\mathbb E N^2\), and subtracting \((\mathbb E N)^2\) proves the mean, variance identity, and displayed formula for \(V_{\rm ind}\).

**2. Structural bounds and computation.** Every unordered incomparable pair consists of two nonroot vertices and contributes \(2p^k\) with \(k\ge0\). Thus \(B\le 2\binom{n-1}{2}\). The index vanishes exactly when no vertex has two children, i.e. the oriented tree is a single path. For \(n\ge3\), attaining the upper bound requires every pair of nonroot vertices to be incomparable and every exponent to vanish, which is equivalent to every nonroot vertex being a child of \(r\). Conversely both extremal configurations give the stated equalities. To calculate the index without enumerating vertex pairs, define for each vertex
\[
h(v)=1+p\sum_{c\text{ child of }v}h(c).
\]
Grouping incomparable pairs by their least common ancestor gives the equivalent dynamic formula
\[
B=2\sum_{v\in V}p^{d_v}
\sum_{c<c'\text{ children of }v}h(c)h(c').
\]
Finally \(p^2\le q\le p\) follows from Jensen and \(0\le\Theta\le1\), with the stated equality distributions; it gives both sharp variance bounds.

**3. Convex ordering.** Fix a convex function \(\varphi\) on the integers \(\{1,\ldots,n\}\). We may compare two product laws for the vertex transmissibilities by replacing one vertex's law at a time. Fix a vertex \(v\), and condition on all independent randomness except \(\Theta_v\) and the outgoing trials from \(v\). Whether \(v\) was reached does not depend on \(\Theta_v\). If it was not reached, \(N\) is unaffected by the replacement. If reached, pre-sample the independent subtree outbreak sizes \(A_1,\ldots,A_k\ge1\) that would result conditional on transmitting to each child, and let \(C\) count infections outside these subtrees. For a fixed \(\Theta_v=\theta\), the conditional total is
\[
N=C+\sum_{i=1}^k A_i Z_i,
\qquad Z_i\mid\theta\ \mathrm{independent\ Bernoulli}(\theta).
\]
For fixed nonnegative \(A_i\), the function \(g(\theta)=\mathbb E[\varphi(C+\sum_i A_iZ_i)]\) is convex in \(\theta\in[0,1]\). Indeed, differentiating the multivariate Bernoulli expectation twice gives a sum over distinct indices \(i,j\) of expectations of
\[
\varphi(C'+A_i+A_j)-\varphi(C'+A_i)-\varphi(C'+A_j)+\varphi(C'),
\]
where \(C'\) includes the other activated subtrees, each term nonnegative by the monotonicity of the increments of a convex function. Averaging over \(A_i,C\) and reachability preserves convexity. Therefore replacing \(\Theta_v^{(1)}\) by the larger-in-convex-order \(\Theta_v^{(2)}\) cannot decrease \(\mathbb E\varphi(N)\); repeating through every vertex establishes \(N^{(1)}\le_{\rm cx}N^{(2)}\). The equality of outbreak means established in step 1 verifies the equal-mean requirement.

## Verification

The standalone Python files `verify_tree_variance.py` and `check_convex_order.py` use only the standard library. Run `python verify_tree_variance.py` and then `python check_convex_order.py` in the directory containing both files. The first constructs independent exact-rational probability-generating functions over every labelled rooted tree on \(2\le n\le6\) and three transmissibility laws, verifying the mean, variance, both branching-index formulas, and the upper bound in 25,428 comparisons. The second compares every integer stop-loss function \(\varphi_k(s)=(s-k)_+\) for two explicit convex-order chains on the same tree family, obtaining 117,088 exact checks. These computations are finite corroboration, not proofs for unbounded \(n\); the preceding steps establish the theorem for all finite rooted trees.

For an exact illustrative five-vertex star rooted at the center, \(p=1/2\) yields \(\mathbb EN=3\), \(V_{\rm ind}=1\), \(B=12\). Fixed duration \(T=\log(2)/\beta\) gives variance \(1\). Exponential duration with rate \(\beta\) produces a uniform \(\Theta\) on \([0,1]\), so its variance is \(2\). The abstract all-or-nothing transmission law yields variance \(4\). All three have the same mean final size.

## Relationship to prior work

Kenah and Robins (2006 preprint, 2007 journal) already demonstrate that nondegenerate infectious periods invalidate independent bond percolation as a description of the *outbreak-size distribution*, and establish a general epidemic-percolation equivalence. Miller (2008) derives sharp extremal results for the probability and large-population relative size of epidemics on networks with heterogeneous transmissibility, with different limiting observables. Sharkey and coauthors (2013 online, 2015 journal) establish exact Markovian node and pair dynamics on trees. Wilkinson and Sharkey (2017 preprint, 2018 journal) prove a convex-order comparison for the probability of reaching prescribed subsets at given times under transmissibility variability; that is a different observable from convex ordering of the **entire final outbreak count**, and their results do not state this branching-index identity. Lefèvre and Picard (1993) study stochastic orderings and severity in collective Reed–Frost models with homogeneous mixing; a full text could not be inspected, so possible broader connections remain a priority risk. The assessed contribution is the combined finite-*fixed*-tree count-convexity theorem and explicit all-size variance penalty, together with its sharp rooted-tree extremizers, not the existence of epidemic percolation or ordinary tree moment recursions.

## Limitations

The count-order proof uses one unique route from root to each vertex and therefore does not extend by this argument to cyclic networks or multiple initial cases. The variance coefficient depends on the chosen root and the mean transmission probability; it is a *sensitivity penalty* and is not a ranking of total outbreak variances across different tree topologies, whose baseline variances and means differ. The upper variance equality law permits infinite infectious periods in the Poisson-contact representation; finite durations yield a supremum only. Real epidemics need not have independent and identically distributed durations, homogeneous contact rates, static networks, or completely susceptible vertices. The result has undergone an internal mathematical review and finite exact checks; no independent validation or complete historical-priority determination is claimed.

## References

- E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, first arXiv version 30 October 2006, arXiv:q-bio/0610057; *Physical Review E* 76 (2007), 036113. https://arxiv.org/abs/q-bio/0610057 . DOI: 10.1103/PhysRevE.76.036113.
- J. C. Miller, *Bounding the Size and Probability of Epidemics on Networks*, first arXiv version 6 March 2008, arXiv:0803.0999; *Journal of Applied Probability* 45 (2008), 498–512. https://arxiv.org/abs/0803.0999 . DOI: 10.1239/jap/1214950363.
- K. J. Sharkey, I. Z. Kiss, R. R. Wilkinson, and P. L. Simon, *Exact Equations for SIR Epidemics on Tree Graphs*, *Bulletin of Mathematical Biology* 77 (2015), 614–645. https://doi.org/10.1007/s11538-013-9923-5.
- R. R. Wilkinson and K. J. Sharkey, *Impact of the infectious period on epidemics*, first arXiv version 16 October 2017, arXiv:1710.05730; *Physical Review E* 97 (2018), 052403. https://arxiv.org/abs/1710.05730 . DOI: 10.1103/PhysRevE.97.052403.
- C. Lefèvre and P. Picard, *An unusual stochastic order relation with some applications in sampling and epidemic theory*, *Advances in Applied Probability* 25 (1993), 63–81. DOI: 10.2307/1427496. Full text was not accessible for comparison.
