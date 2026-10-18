# Sharp graph and tree thresholds for edge-induced disagreement in two-leader harmonic opinions

## Finding
Let \(G=(V,E)\) be any finite connected simple unweighted undirected graph, with exactly two distinct pinned vertices whose opinions are \(0\) and \(1\). All other vertices adopt the unique harmonic equilibrium of neighbor averaging. Put \(n=|V|\), let \(h\) be this equilibrium including both pins, and define global quadratic disagreement by
\[
 P(G)=\sum_{v\in V}\bigl(h_v-\overline h\bigr)^2,
 \qquad \overline h=n^{-1}\sum_{v\in V}h_v.
\]
Add exactly one previously absent edge between two **unpinned** vertices, leaving pinned opinions and all other edges unchanged.

**Sharp unrestricted threshold.** For every such pair of connected graphs with \(n\le5\), the addition cannot increase \(P\). On six vertices a connected graph admits a strict increase.

**Sharp tree threshold.** If the original graph is a tree with \(n\le6\), the addition cannot increase \(P\). A tree with seven vertices admits a strict increase.

The first statement compares connected initial graphs; the second restricts only the **initial** graph to be a tree, so the augmented graph is unicyclic. Both statements quantify over all choices of the two pinned vertices and all admissible follower–follower nonedges. The equivalent global disagreement index \(\Gamma(G)=\sum_{u<v}(h_u-h_v)^2=nP(G)\) has the same signs of change.

## Assumptions and scope
An equilibrium assigns \(h_{z_0}=0\), \(h_{z_1}=1\) to the two pins and requires \(\deg(v)h_v=\sum_{u\sim v}h_u\) for every other vertex \(v\). The graph is connected, all edges have unit weight, there are no self loops, and the added edge is between two followers. All vertices—including both pinned leaders—enter \(P\) with equal weight. These restrictions matter: this is not a claim about transient disagreement, stochastic noise, directed or weighted graphs, edges incident to a leader, or measures defined only on followers or existing edges.

A connected grounded graph Laplacian is positive definite: for a follower vector \(y\) extended by zero on both pins, \(y^{\mathsf T}Ly=\sum_{uv\in E}(\widetilde y_u-\widetilde y_v)^2\), which vanishes only when \(y=0\). Therefore the equilibrium exists uniquely. The two different pinned opinions may be interpreted as opposite persistent external influences.

## Proof
**1. Exact edge-perturbation identity.** Fix vertex order with both pinned vertices first and let \(L\) be the grounded Laplacian on follower coordinates. If \(b\) counts incident edges to the opinion-\(1\) pin, the follower equilibrium is \(x=L^{-1}b\). For a missing follower edge \(uv\), put \(e=\mathbf e_u-\mathbf e_v\), \(z=L^{-1}e\), and
\[
 t=\frac{e^{\mathsf T}x}{1+e^{\mathsf T}z}.
\]
The grounded Laplacian becomes \(L+ee^{\mathsf T}\), whose inverse exists because \(L\) is positive definite. The Sherman–Morrison identity gives the new follower opinion vector exactly as \(x'=x-tz\). Extend \(z\) with zeros on the pinned coordinates and write \(C=I-\mathbf1\mathbf1^{\mathsf T}/n\). With the full original opinion vector \(h\),
\[
 P(G+uv)-P(G)=t^2\|Cz\|^2-2t\langle Ch,Cz\rangle.
\]
Thus an added link is not generally constrained to reduce global variance: the cross term can have either sign. This identity gives the mathematical mechanism, not by itself the finite minimality assertion.

**2. Six-vertex witness.** Label vertices \(0,1,2,3,4,5\), with pinned vertices \(0\) (opinion \(0\)) and \(1\) (opinion \(1\)). Take
\[
 E=\{03,05,12,15,23,24\},\qquad uv=35,
\]
where \(ij\) denotes an edge between vertex \(i\) and vertex \(j\). Direct substitution into every follower averaging equation gives the equilibrium vectors before and after addition:
\[
 h=(0,1,\tfrac23,\tfrac13,\tfrac23,\tfrac12),\qquad
 h'=(0,1,\tfrac9{13},\tfrac5{13},\tfrac9{13},\tfrac6{13}).
\]
Consequently
\[
 P(G)=\frac{125}{216},\qquad P(G+35)=\frac{98}{169},\qquad
 P(G+35)-P(G)=\frac{43}{36504}>0.
\]
The initial graph is connected with six edges (one cycle), and the new edge joins two genuine followers. Every follower opinion lies strictly between zero and one before and after insertion.

**3. Seven-vertex tree witness.** Here label vertices \(0,1,2,3,4,5,6\) and pin \(2\) at opinion \(0\), \(5\) at opinion \(1\). The six edges
\[
 E=\{01,12,04,06,23,45\}
\]
form a connected tree. Add the missing follower edge \(46\). The equilibria in the original vertex order are
\[
 h=(\tfrac12,\tfrac14,0,0,\tfrac34,1,\tfrac12),\qquad
 h'=(\tfrac6{11},\tfrac3{11},0,0,\tfrac8{11},1,\tfrac7{11}).
\]
Again each follower satisfies neighbor averaging, whence
\[
 P(G)=\frac{47}{56},\qquad P(G+46)=\frac{104}{121},\qquad
 P(G+46)-P(G)=\frac{137}{6776}>0.
\]
An interior follower at vertex \(3\) has value zero in both networks; the model permits such pinned-reachable absorbing plateaus. The two pins remain distinct, and \(46\) is absent from the original tree.

**4. Exhaustive lower bounds.** Because vertex relabeling does not change the equilibrium or \(P\), fix pinned vertices to be \(0\) and \(1\) for enumeration. For each \(n=2,3,4,5\), enumerate all \(2^{\binom n2}\) simple labeled edge masks, retain the connected graphs, and for each such graph enumerate all missing follower–follower edges. Compute its grounded Laplacian and both harmonic equilibria using exact rational arithmetic and evaluate the exact sign of \(P(G+uv)-P(G)\). The connected graph counts for \(n=2,3,4,5\) are, respectively, \(1,4,38,728\), with respectively \(0,0,14,942\) admissible (graph, edge) comparisons. The counts of strict decreases/ties are \((0,0),(0,0),(10,4),(708,234)\); no increases occur.

For the tree restriction, enumerate all \(n^{n-2}\) Prüfer sequences for each \(n=2,3,4,5,6\); these encode each labeled tree exactly once. Again compare all absent follower edges, with exact rational harmonic solutions. The tree counts are \(1,3,16,125,1296\); the eligible comparison counts are \(0,0,8,225,5184\); the decrease/tie counts are \((0,0),(0,0),(6,2),(156,69),(3456,1728)\). No increases occur. Exhaustiveness follows because each simple labeled graph is exactly one mask, each labeled tree exactly one Prüfer word, and every two-pin choice is relabelable to \(0,1\). Combining these verified finite lower bounds with the two explicit larger witnesses proves the two sharp thresholds.

## Verification
Two standalone standard-library programs accompany this statement. Run `python3 verify_harmonic.py` to compute every enumerated case using `fractions.Fraction` and exact grounded-Laplacian Gauss–Jordan elimination, plus the two witnesses. Run `python3 check_determinants.py` to repeat all cutoff enumerations with a separately implemented integer determinant and Cramer's rule. Both check every connected labeled graph through five vertices, every labeled tree through six vertices, and every possible missing follower–follower edge. The first also verifies both explicit witnesses. Both programs completed without exception and agree on the number of strict decreases and ties. No floating-point tolerances or graph sampling enter the certification of these *finite* ranges.

## Relationship to prior work
Dandekar, Goel and Lee [1] define the global disagreement index as pairwise squared opinion differences and study network disagreement under averaging on a fixed graph. Their fixed-graph monotonicity result concerns the **edge-based network disagreement index**, not a comparison of equilibria after follower–follower link insertion. Their global disagreement index is exactly \(nP\) used here.

Mackin and Patterson [2] use the same grounded-Laplacian equilibria for opposing pinned binary leaders, but optimize leader placement for binned Simpson and Shannon diversity measures. They do not obtain the graph-edit thresholds for quadratic global disagreement here. Zhou and Zhang [3] study edge insertion incident to opinion-\(1\) leaders to optimize aggregate opinion, a different edge class and functional. Xu and Zhang [4] study noisy followers with identically valued leaders, polarization identified with a grounded resistance sum, and leader-incident edge insertions; their monotonicity theorem does not imply the statements here. Bhalla, Lechowicz and Musco [5] analyze adaptive edge dynamics with Friedkin–Johnsen opinions; their abstract is related context, but the full technical comparison remains a literature-access risk. These distinctions concern actual implications of the source statements, not just nomenclature.

## Limitations
Only unweighted undirected connected simple graphs, two opposing fixed pins, equilibrium opinions, full-population quadratic variance, and one follower–follower edge are covered. The lower-bound classification is exhaustive only up to the stated finite cutoffs; it is not a classification of every larger graph and does not imply that all added edges increase disagreement. The two witness calculations have no experimental uncertainty, but unlocated equivalent presentations in a larger primary-literature corpus remain possible. Independent validation beyond the accompanying self-review is not asserted.

## References
[1] P. Dandekar, A. Goel, D. Lee, *Biased Assimilation, Homophily and the Dynamics of Polarization*, arXiv:1209.5998v1 (26 September 2012). https://arxiv.org/html/1209.5998v1

[2] E. Mackin and S. Patterson, *Maximizing Diversity of Opinion in Social Networks*, arXiv:1811.03706. https://arxiv.org/html/1811.03706v2

[3] X. Zhou and Z. Zhang, *Maximizing Influence of Leaders in Social Networks*, arXiv:2106.06128. https://arxiv.org/abs/2106.06128

[4] W. Xu and Z. Zhang, *Minimizing Polarization in Noisy Leader-Follower Opinion Dynamics*, arXiv:2308.07008. https://ar5iv.labs.arxiv.org/html/2308.07008

[5] N. Bhalla, A. Lechowicz and C. Musco, *Local Edge Dynamics and Opinion Polarization*, arXiv:2111.14020. https://arxiv.org/abs/2111.14020
