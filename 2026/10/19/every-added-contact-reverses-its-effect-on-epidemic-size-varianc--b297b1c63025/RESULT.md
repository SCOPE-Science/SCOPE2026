# Every added contact reverses its effect on epidemic-size variance as transmissibility rises

## Finding

For every finite connected simple undirected graph \(G=(V,E)\) with \(n=|V|\ge3\), every missing edge \(e=uv\), and every independent bond-retention probability \(p\in(0,1)\), let \(X_G(p)\) count the vertices in the open connected component of a uniformly chosen seed. Then:

1. **Mean monotonicity:** \(\mathbb E X_{G+e}(p)>\mathbb E X_G(p)\) for all \(p\in(0,1)\).
2. **Universal low/high reversal:** with
   \[
   \Delta_v(p)=\operatorname{Var}(X_{G+e}(p))-\operatorname{Var}(X_G(p)),
   \]
   one has \(\Delta_v(p)=2p/n+O(p^2)>0\) as \(p\downarrow0\), but \(\Delta_v(p)<0\) for all \(p\) sufficiently close to \(1\).
3. **A network-independent high-mean guarantee:** writing \(\mu_G(p)=\mathbb E X_G(p)\), the explicit condition \(\mu_G(p)\ge3n/4\) implies \(\Delta_v(p)<0\) for **every** missing edge \(e\). The constant \(3/4\) is a sufficient threshold, not claimed sharp.

The signs therefore reverse at least once in \(p\in(0,1)\) for *every* missing edge, while the expected outbreak size increases at all transmission probabilities. No uniqueness of the variance crossover is asserted.

## Assumptions and scope

All graphs are finite, simple, connected, undirected and fixed (not sampled from a graph ensemble). The vertices \(u,v\) are distinct and nonadjacent. Existing edges are retained independently with common probability \(p\in(0,1)\). A new edge, when added, has the *same* independent retention probability. The seed \(U\) is uniformly distributed over all \(n\) vertices and independent of edge states. A single-seed independent-bond Reed–Frost outbreak has the same final-size law as \(X_G(p)\) [2,3]. This statement is not extended to SIR models whose infectious-period dependence induces correlated incident-edge transmissions [3].

All variances refer to the joint randomness of the seed, existing retained edges, and the new edge (if present); they are unconditional final-size variances. The lower expansion keeps the graph fixed as \(p\downarrow0\).

## Proof

Let \(H\) be the random retained-edge subgraph of \(G\), and \(U\) an independent uniform vertex. Let \(X=|C_H(U)|\) and \(\mu=\mathbb E X\). For each realization \(H\), if \(u,v\) are in different components of sizes \(a,b\), let \(a,b\) denote those two sizes; otherwise set all terms involving their product \(ab\) to zero. Define
\[
 A=\mathbb E_H\!\left[\frac{2ab}{n}\mathbf1_{\{u\not\leftrightarrow_Hv\}}\right],
 \qquad
 B=\mathbb E_H\!\left[\frac{3ab(a+b)}{n}\mathbf1_{\{u\not\leftrightarrow_Hv\}}\right].
\]
Equivalently, the indicator may be suppressed by declaring \(ab=0\) when \(u,v\) are connected.

**Conditional component-merger identities.** If the two components are distinct and the new edge is retained, their sizes \(a,b\) become one component of size \(a+b\). Because \(U\) is uniform, the conditional increase in the first moment is
\[
 \frac{(a+b)^2-a^2-b^2}{n}=\frac{2ab}{n}.
\]
The conditional increase in the second moment is
\[
 \frac{(a+b)^3-a^3-b^3}{n}=\frac{3ab(a+b)}n.
\]
When \(u,v\) are already connected, these increases vanish. Independence of the new edge gives the *exact* equalities
\[
 \mathbb E X_{G+e}-\mu=pA,\qquad
 \mathbb E X_{G+e}^2-\mathbb E X^2=pB.
\]
Consequently,
\[
 \boxed{\Delta_v(p)=p(B-2\mu A)-p^2A^2
 =\frac pn\mathbb E_H[ab(3(a+b)-4\mu)\mathbf1_{\{u\not\leftrightarrow_Hv\}}]-p^2A^2.}
\tag{1}
\]
For \(p\in(0,1)\), the event that all existing edges fail has strictly positive probability \((1-p)^{|E|}\), and on that event \(u,v\) are separate with \(a=b=1\). Thus \(A>0\) and the mean increase \(pA\) is strict.

**Low transmissibility.** For fixed \(G\), as \(p\downarrow0\), all existing edges fail with probability \(1-O(p)\). On that event \(a=b=1\) and \(X=1\) for all seeds. Boundedness of the component sizes and finiteness of \(E\) imply
\[
 \mu=1+O(p),\quad A=\frac2n+O(p),\quad B=\frac6n+O(p).
\]
Substitution in (1) yields \(\Delta_v(p)=2p/n+O(p^2)>0\) for all sufficiently small positive \(p\).

**High-mean sufficient condition.** Whenever \(\mu\ge3n/4\), the two different components satisfy \(a+b\le n\), hence \(3(a+b)-4\mu\le3n-4\mu\le0\). Formula (1) yields \(\Delta_v(p)\le-p^2A^2<0\). Finally, connectedness ensures that as \(p\uparrow1\), every existing edge is present with probability tending to one and \(X=n\) with probability tending to one. Therefore \(\mu_G(p)\to n>3n/4\), establishing the high-transmissibility reversal for every \(e\). The variance difference is a polynomial in \(p\) on each finite graph, so its opposite endpoint signs also imply at least one crossover inside \((0,1)\).

**Smallest illustrating network.** Let \(G\) be the three-vertex path \(P_3\) and add its missing closing edge, producing the triangle. By enumerating retained subsets, at \(p=1/2\) the mean increases by \(5/12\) and the variance by \(7/144\). At \(p=4/5\), the mean increases by \(136/375\) while the variance changes by \(-47816/140625\). These are examples, not inputs to the universal argument.

## Verification

Run `python3 verify.py` with the Python standard library. The program computes exact rational first and second seed-component moments by enumerating every retained-edge subgraph. It independently calculates conditional merging increments and compares both sides of (1), mean monotonicity, and the \(3n/4\) sufficient condition for **every connected labeled graph on two through five vertices, every nonedge, and four rational probabilities** \(1/4,1/2,3/4,9/10\). The run completed **12,908 graph–edge–probability comparisons** and checked the high-mean implication in 5,756 applicable comparisons. It reproduces both path-to-triangle examples exactly. The universal quantifiers are established by the proof above; this finite exercise only checks implementation and algebra.

## Relationship to prior work

Moore and Newman [1] derived outbreak-size moments on small-world percolation ensembles and identified the size bias from uniformly sampled outbreak origins. Their formulas are for specified ensembles, not the variance response to inserting an arbitrary edge in every fixed connected contact network.

Becchetti et al. [2] explicitly relate finite-graph bond percolation to the Reed–Frost and independent-cascade processes and study component-size and connectivity regimes of power-law small-world networks. Their results do not establish an edge-by-edge, all-graphs variance sign reversal.

Kenah and Robins [3] prove that a general SIR process with random infectious periods cannot always be replaced by independent bond percolation. This explains why the present theorem is explicitly limited to independent-bond transmission rather than being asserted for arbitrary SIR models.

The contribution is the universal single-edge mean/variance contrast, the exact merger identity, and the model-independent sufficient condition for variance reduction. No claim is made to have discovered the percolation–epidemic mapping, the moment definitions, or general mean monotonicity.

## Limitations

The \(3n/4\) condition is sufficient, not shown to be optimal. There may be multiple variance sign changes as \(p\) varies; neither uniqueness nor a location formula for them is established. No conclusion is given for nonuniform seeds, heterogeneous or dependent edge transmission, dynamical infection-duration statistics, directed networks, or finite-time epidemic trajectories. The result is about the *unconditional variance* of final outbreak size; lower variance alone is not a statement of lower epidemic harm, since the mean strictly increases.

## References

[1] C. Moore and M. E. J. Newman, *Exact solution of site and bond percolation on small-world networks*, arXiv:cond-mat/0001393 (first posted 2000-01-26), Physical Review E 62 (2000), 7059–7064. https://arxiv.org/html/cond-mat/0001393v1

[2] L. Becchetti, A. Clementi, F. Pasquale, L. Trevisan, and I. Ziccardi, *Bond Percolation in Small-World Graphs with Power-Law Distribution*, arXiv:2205.08774 (first posted 2022-05-18). https://arxiv.org/html/2205.08774v2

[3] E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, arXiv:q-bio/0610057 (first posted 2006-10-30), Physical Review E 76 (2007), 036113. https://arxiv.org/html/q-bio/0610057v5
