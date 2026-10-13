# Sharp Barber modularity in two-tier perfectly nested ecological networks

## Finding

Consider a simple bipartite interaction network with \(p\ge1\) specialist species, \(q\ge1\) generalist species, \(a\ge1\) core partners and \(b\ge1\) peripheral partners, where \(m=p+q\ge3\). Each specialist interacts with every core partner and with no peripheral partner; each generalist interacts with every core and peripheral partner. This is a connected Ferrers (chain) graph: the neighborhoods within either guild are linearly ordered by inclusion, so it is perfectly nested in the neighborhood-inclusion sense.

For Barber's standard bipartite modularity \(Q_B\), maximized over **all partitions of all vertices, with no restriction on the number or sizes of modules**, the exact optimum is

\[
Q_B^{\max}=\frac{2abpq}{\bigl((p+q)a+qb\bigr)^2}.
\]

Its **unique maximizing partition**, apart from module labels, places all specialists with all core partners in one module and all generalists with all peripheral partners in another. For fixed specialist/generalist counts, optimizing over all positive integer \(a,b\) gives the sharp ceiling

\[
Q_B^{\max}\le\frac{p}{2(p+q)},
\quad\text{with equality iff}\quad qb=(p+q)a.
\]

The equality condition is attainable for every \(p,q\): choose \(a=q\) and \(b=p+q\). Over all two-tier networks with a fixed total \(m\ge3\) of primary-guild species, the sharp ceiling is \((m-1)/(2m)\), attained for \((p,q,a,b)=(m-1,1,1,m)\). Thus a sequence of **perfectly nested** interaction networks has optimal Barber modularity tending to \(1/2\).

## Assumptions and scope

The interaction matrix is unweighted and binary, with \(m=p+q\) rows and \(n=a+b\) columns. All four parameters are positive integers, and the novelty claim concerns \(m\ge3\). There are no isolated species. Its \(E=(p+q)a+qb\) interactions have two row-neighborhood types and two column-neighborhood types. All module assignments, including mixed-guild modules, are admissible. The modularity normalization is precisely Barber's \(Q_B=E^{-1}\sum_{i,j}(A_{ij}-d_i e_j/E)\mathbf 1\{g_i=h_j\}\), where \(d_i\) and \(e_j\) denote row and column degrees. The resolution parameter is fixed to one.

Perfect nestedness here means nested neighborhoods (Ferrers/chain graph), **not** that a tie-penalizing empirical NODF normalization equals its maximum: both guilds contain degree-twin classes. No statement of general optimal modularity over every Ferrers graph is made.

## Proof

Every specialist row has degree \(a\); every generalist row has degree \(a+b\). Each core column has degree \(p+q\), and each peripheral column has degree \(q\). Put \(E=(p+q)a+qb\) and \(B_{ij}=A_{ij}-d_i e_j/E\). Direct substitution gives the complete four-block sign table

\[
\begin{array}{c|cc}
 &\text{core column}&\text{peripheral column}\\ \hline
\text{specialist row}&qb/E&-aq/E\\
\text{generalist row}&-pb/E&pa/E
\end{array}.
\]

All displayed positive and negative entries are strictly nonzero because \(p,q,a,b>0\). For **any** partition, the numerator \(E Q_B\) can include at most the sum of all positive entries of \(B\); including a negative entry cannot increase it. The sum of positive entries is

\[
pa\frac{qb}{E}+qb\frac{pa}{E}=\frac{2abpq}{E}.
\]

Assign all specialist rows and all core columns to module one, and all generalist rows and all peripheral columns to module two. This partition includes every positive entry and excludes every negative entry, attaining the upper bound. Equality forces every specialist-core pair into the same module and every generalist-peripheral pair into the same module. Since all four parameter sets are nonempty, these force exactly the two stated modules; the negative cross-block entries force the two modules to be distinct. This proves both the optimum and uniqueness.

For the sharp parameter bound, set \(X=(p+q)a\), \(Y=qb\). The formula becomes

\[
Q_B^{\max}=\frac{2p}{p+q}\frac{XY}{(X+Y)^2}
\le\frac{p}{2(p+q)}
\]

by \(4XY\le(X+Y)^2\). Equality holds exactly when \(X=Y\), equivalently \(qb=(p+q)a\), and the positive integer choice \(a=q\), \(b=p+q\) realizes it. Finally \(p=m-q\le m-1\) for fixed \(m\), with equality only when \(q=1\). Then choose \(a=1\), \(b=m\) to meet \(qb=ma\), giving \((m-1)/(2m)\) and the limit \(1/2\) as \(m\to\infty\). No limiting value is attained at finite \(m\).

## Verification

The standalone standard-library checker `verify.py` independently enumerates partitions of the primary guild and optimizes all secondary-vertex assignments; for small profiles it independently enumerates **every partition of all vertices** and checks both the optimum and its uniqueness. It checks \(156\) integer parameter profiles and \(2279\) full-vertex partitions in the independent small cases. Running `python verify.py` in a directory containing the file prints `VERIFY_OK parametric_profiles=156 full_vertex_partitions=2279`. Exact rational arithmetic is used throughout. This finite check corroborates, rather than substitutes for, the unrestricted algebraic proof.

## Relationship to prior work

Bascompte and coauthors (2003) identify nested-neighborhood structure in plant-animal mutualistic networks. Barber (arXiv:0707.1616, first submitted July 11, 2007) defines the bipartite modularity and its module-optimization problem. Fortuna and coauthors (2010) examine empirical relationships between nestedness and modularity, but optimize a **unipartite** modularity on bipartite data rather than the exact Barber statistic. Pinheiro and coauthors (2022) study hierarchical combinations of nested and modular topologies and **do** optimize Barber modularity for empirical networks; their paper does not give the two-tier exact optimum, uniqueness and sharp specialist-fraction ceiling stated here. Earlier exact analyses already cover the two-primary-species situation; that case is not claimed as a new result. The mathematical contribution here is the complete arbitrary-multiplicity two-tier classification for \(p+q\ge3\), including sharp fixed-guild ceilings and the near-\(1/2\) family.

## Limitations

Only binary, unweighted, two-neighborhood-level Ferrers networks are classified. The result is **not** a sharp ceiling for arbitrary Ferrers graphs, does not assert significance under any randomized ecological null model, and says nothing about species persistence, dynamics, or observed field networks. Apparent perfect nestedness by neighborhood inclusion does not imply a maximal value of tie-sensitive NODF indices. The claim of originality depends on the inspected published literature and available indexed records; broader unpublished or unindexed treatments could exist. Independent validation has not been performed.

## References

1. J. Bascompte, P. Jordano, C. J. Melián, J. M. Olesen, “The nested assembly of plant–animal mutualistic networks,” *PNAS* 100 (2003), 9383–9387. DOI: 10.1073/pnas.1633576100.
2. M. J. Barber, “Modularity and community detection in bipartite networks,” arXiv:0707.1616 (first submitted 2007-07-11); *Physical Review E* 76 (2007), 066102. DOI: 10.1103/PhysRevE.76.066102.
3. M. A. Fortuna et al., “Nestedness versus modularity in ecological networks: two sides of the same coin?” *Journal of Animal Ecology* 79 (2010), 811–817. DOI: 10.1111/j.1365-2656.2010.01688.x.
4. R. B. P. Pinheiro et al., “Hierarchical compound topology uncovers complex structure of species interaction networks,” *Journal of Animal Ecology* (2022). DOI: 10.1111/1365-2656.13806.
5. “The ambiguity of nestedness under soft and hard constraints,” *Scientific Reports* (2020). DOI: 10.1038/s41598-020-76300-1 (definition of perfectly nested/chain networks).
