# Edge-selective short-distance laws reconstruct finite metric networks up to a sharp Whitney obstruction

## Finding
For every finite connected simple graph with at least one edge and arbitrary strictly positive edge lengths, short-radius distance distributions from a finite collection of **edge-mixture sampling experiments** determine the length of each named edge and the incidence adjacency of every edge pair. Specifically, one single-edge experiment per edge and one equal two-edge-mixture experiment per unordered edge pair recover the entire labeled line graph from the linear and quadratic coefficients of the cumulative distributions. Thus the abstract graph is determined up to isomorphism except for the triangle/claw ambiguity; when the underlying graph has at least five vertices, the complete edge-labeled weighted graph is determined. The triangle and claw with identical three edge lengths have identical short-radius distributions for *every* mixture, demonstrating that this limitation cannot be eliminated within this measurement class.

## Assumptions and scope
Let \(G=(V,E)\) be a finite connected simple undirected graph with \(m=|E|\ge1\). Every edge \(e\in E\) is a closed metric interval of known *identity* but initially unknown length \(\ell_e>0\), glued at common endpoint vertices, with shortest-path metric \(d_G\). Edge identities index permitted sampling experiments and do not label the sampled endpoints after they are drawn. Choose a probability vector \(p=(p_e)_{e\in E}\). Independently twice, select edge \(e\) with probability \(p_e\), then select a point uniformly on that edge by arclength. The only recorded outcome is the scalar intrinsic distance \(D_p=d_G(X_p,Y_p)\), not the two selected edges. Write \(F_p(r)=\Pr(D_p\le r)\) and \(\varepsilon=\min_e\ell_e\). The graph has no loops or multiple edges and the lengths are exact positive reals. The experiment mixtures and corresponding population distribution germs at zero are assumed exact.

## Proof
**Local distance decomposition.** For each \(0\le r<\varepsilon\), the complete formula is
\[
 F_p(r)=2r\sum_{e\in E}\frac{p_e^2}{\ell_e}
 +r^2\left[-\sum_{e\in E}\frac{p_e^2}{\ell_e^2}
 +\sum_{\substack{\{e,f\}\subset E\\e\ne f,\ e\cap f\ne\varnothing}}\frac{p_ep_f}{\ell_e\ell_f}\right]. \tag{1}
\]
To establish it, condition on the two selected edges. If both are \(e\), a pair of independent uniform coordinates on an interval of length \(\ell_e\) has distance at most \(r\) on a region of area \(2\ell_er-r^2\). Any alternative route that leaves this edge must traverse at least one entire other edge or, since the graph is simple, at least one entire edge in a nontrivial return walk; such a route is longer than \(r\). Hence its conditional probability is exactly \(2r/\ell_e-r^2/\ell_e^2\).

If the two sampled edges are distinct and incident at vertex \(v\), the only possible path shorter than \(\varepsilon\) goes through \(v\), and its length is the sum of distances to \(v\). The permitted pairs form a right triangle of area \(r^2/2\); the conditional probability is \(r^2/(2\ell_e\ell_f)\). The two orders of edge sampling contribute \(p_ep_f r^2/(\ell_e\ell_f)\). Distinct nonincident edges require any connecting path to traverse an entire intermediate edge; their conditional contribution vanishes when \(r<\varepsilon\). Summation proves (1). As all sets counted have polygonal boundaries of zero product arclength, the weak/strict distance threshold makes no difference.

**Explicit finite inversion.** For a pure-edge probe \(p=\delta_e\), let \(a_e=[r]F_{\delta_e}(r)\) and \(u_e=[r^2]F_{\delta_e}(r)\). Equation (1) yields \(a_e=2/\ell_e\), \(u_e=-1/\ell_e^2\); therefore
\[\ell_e=2/a_e.\tag{2}\]
For each distinct pair of named edges let \(p=(\delta_e+\delta_f)/2\), and let \(b_{ef}=[r^2]F_p(r)\). Then
\[b_{ef}=-\frac1{4\ell_e^2}-\frac1{4\ell_f^2}+\frac{\mathbf1_{e\cap f\ne\varnothing}}{4\ell_e\ell_f}.\]
Thus the integer
\[
 \boxed{\mathbf1_{e\cap f\ne\varnothing}=4\ell_e\ell_f b_{ef}+\ell_f/\ell_e+\ell_e/\ell_f}\tag{3}
\]
is determined and equals either zero or one. Equations (2)--(3) reconstruct the edge-indexed line graph \(L(G)\) with \(m+\binom m2\) separate population distribution germs. Formula (1) also shows that all other prescribed mixture germs carry no additional information: they depend only on these recovered lengths and edge adjacencies.

**Global identification and sharp obstruction.** Whitney's line-graph isomorphism theorem says a connected finite simple graph is determined by its line graph up to abstract isomorphism except for the pair \(K_3\) and \(K_{1,3}\). The strong version identifies edge-indexed incidence in graphs with more than four vertices; small exceptional graphs can also have extra edge permutations invisible to the line graph. Therefore for at least five vertices the full edge-labeled positive-length network is determined, and in general the abstract graph is determined except for the stated triangle/claw pair. For sharpness, assign the same three positive lengths, indexed identically, to a triangle and a three-arm claw. Their line graphs are both \(K_3\), hence (1) gives the same short-radius \(F_p\) for every mixture \(p\), even though the graphs are not homeomorphic as metric graphs (their first Betti numbers differ). This completes all assertions.

## Verification
The accompanying reproducible `check.py` evaluates true shortest-path distance probabilities by an independent two-coordinate integral, using shortest-path distances between vertices and Gauss--Legendre quadrature. It compares them against (1) for 19 named edges across five nondegenerate graph examples, including a triangle, claw, path, cyclic network with a diagonal, and higher-degree star, for single-edge, pair-mixture and all-edge-mixture probes. Additional exact rational arithmetic verifies (2)--(3) and the triangle/claw obstruction. Run `python check.py` with Python 3 and NumPy installed. The computation is an independent finite check, not a proof of the all-graphs theorem; the argument above provides the proof.

## Relationship to prior work
Network point-process studies by Baddeley and collaborators and by Rakshit, Nair, and Baddeley develop distance-based second-order summary statistics, including network \(K\)-functions, for a network whose structure is supplied to the analysis. Their program motivates observing scalar distance statistics, but the inspected materials do not reconstruct an unknown network's edge adjacency by deliberately mixing edgewise-uniform samples. Classical Whitney line-graph reconstruction supplies the last purely combinatorial inference from our independently derived analytic coefficients; that theorem is not claimed as new. Anderson and Bernshteyn's discussion of Whitney's strong theorem identifies the small exceptional graphs relevant to edge-labeled recovery.

## Limitations
The graph must be finite, connected and simple; edge identities are known for designing interventions, but sampled edge labels are not observed. The theorem requires an ideal population short-radius law with exact coefficients and does not address finite observations, ill-conditioned short-radius regression, uniform nonselective sampling alone, arbitrary nonuniform within-edge densities, loops, parallel edges, or recovery of a unique labeled network for graphs on at most four vertices. The triangle/claw pair is an unavoidable obstruction to recovering the abstract graph from the entire collection of local mixture laws. Historical priority is not independently certified; an uninspected equivalent network-correlation formulation remains a risk.

## References
1. A. Baddeley, G. Nair, S. Rakshit, T. McSwiggan, “'Stationary' point processes are uncommon on linear networks,” *Stat* (first available online February 8, 2017), DOI: 10.1002/sta4.135.
2. S. Rakshit, G. Nair, A. Baddeley, “Second-order analysis of point patterns on a network using any distance metric,” *Spatial Statistics* 22 (2017), 129--154, DOI: 10.1016/j.spasta.2017.10.002.
3. S. Rakshit, A. Baddeley, G. Nair, “Efficient Code for Second Order Analysis of Events on a Linear Network,” *Journal of Statistical Software* 90 (2019), 1--37, DOI: 10.18637/jss.v090.i01.
4. J. Anderson, A. Bernshteyn, “Borel Line Graphs,” *Journal of Symbolic Logic* (online November 11, 2024), DOI: 10.1017/jsl.2024.50, especially Theorem 3.8 and Table 1.
5. H. Whitney, “Congruent Graphs and the Connectivity of Graphs,” *American Journal of Mathematics* 54 (1932), 150--168, DOI: 10.2307/2371086.
