# Chi-square facet-incidence fluctuations in cocktail-party Lipschitz-free balls

## Finding
For every integer \(m\ge3\), let \(G_m=K_{2,2,\ldots,2}\) denote the cocktail-party graph: its \(2m\) vertices occur in \(m\) distinguished pairs, and two different vertices are adjacent exactly when they are not paired. Let \(B_m\) be the real Lipschitz-free unit ball of its shortest-path metric. Write \(I(F)\) for the number of vertices belonging to a facet \(F\) of \(B_m\), and put
\[
P_m(t)=\sum_{F\text{ facet}}t^{I(F)}.
\]
Then the **entire facet-incidence distribution** is given by
\[
\boxed{P_m(t)=\sum_{\substack{a,b,c\ge0\\a+b+c=m}}
\frac{m!\,2^c}{a!b!c!}\,t^{m^2-(a-b)^2-c}
-2-4m\,t^{2m-2}+2m\,t^{4m-4}.}
\]
In particular, the coefficient of \(t^j\) counts exactly the facets containing \(j\) vertices. The previously established total facet number is \(F_m=P_m(1)=4^m-2m-2\); the new subject here is their incidence distribution, its statistics, and natural symmetry refinement.

The total first and second powers of facet incidence obey the exact formulas
\[
\boxed{\sum_F I(F)=4^m m(m-1),}
\]
\[
\boxed{\sum_F I(F)^2=4^m\left[m^2(m-1)^2+\frac{m(m-1)}2\right]+16m(m-1)^2.}
\]
For a uniformly chosen facet with incidence \(I_m\), these yield its exact mean and variance on division by \(F_m\). In particular,
\[
\operatorname{Var}(I_m)\sim\frac{m^2}{2}.
\]
There is a **non-Gaussian limit law**:
\[
\boxed{\frac{m^2-I_m}{m}\ \xrightarrow{\mathrm d}\ \frac{1+Z^2}{2},\qquad Z\sim N(0,1).}
\]
The maximum facet incidence equals \(m^2\) for even \(m\), and \(m^2-1\) for odd \(m\). Its exact multiplicity is
\[
\boxed{M_m=\begin{cases}
\binom{m}{m/2},&m\text{ even},\\
2\binom{m}{(m-1)/2}+2m\binom{m-1}{(m-1)/2},&m\ge5\text{ odd},\\
24,&m=3.
\end{cases}}
\]
All facets fall into
\[
\boxed{O_m=\frac12\left[\binom{m+2}{2}+\left\lfloor\frac m2\right\rfloor+1\right]-1}
\]
orbits under the action of \(\operatorname{Aut}(G_m)\) and global sign reversal. Their full sizes are provided explicitly in the proof.

## Assumptions and scope
The graph has unit-length edges, with the graph shortest-path metric. For a finite metric space \(X\), the real Lipschitz-free unit ball is the convex hull of the normalized molecules \((e_x-e_y)/d(x,y)\) in the zero-sum hyperplane. Here a nonadjacent pair has distance two, and its molecule is a midpoint of two edge molecules, so
\[
B_m=\operatorname{conv}\{\pm(e_u-e_v):\{u,v\}\in E(G_m)\}
\subseteq\{x\in\mathbb R^{2m}:\sum x_i=0\}.
\]
Every oriented edge molecule is an actual vertex, by its unit-distance transport minimality; there are no other vertices. Since \(G_m\) is connected, \(\dim B_m=2m-1\). The statistic \(I(F)\) counts actual polytope vertices, equivalently the directed tight graph edges of the facet potential. The orbit action is the graph's natural wreath-product automorphism group, enlarged by central inversion; it is not a claim about all unrestricted linear polytope symmetries.

## Proof
**1. Facets and integer potentials.** The dual polar of \(B_m\) is the quotient by constants of the real functions \(f\) satisfying \(|f(u)-f(v)|\le1\) on each graph edge. The active inequalities of \(f\) have normals \(e_u-e_v\); their span has rank \(2m-1\) exactly when the undirected graph of tight edges is connected and spanning. Thus \(f\) defines a facet of \(B_m\) precisely when that graph is connected and spanning. This is the known symmetric-edge-polytope criterion, used here with its underlying rank justification. A spanning tree of tight edges also forces each normalized potential to take integer values: fix one vertex at zero, and integrate \(\pm1\) along its tree paths. As the diameter is two, an integral Lipschitz potential shifted to minimum zero takes values only in \(\{0,1,2\}\).

**2. Complete enumeration, with established ingredients distinguished.** A three-level potential has a zero and a two. Those vertices cannot be adjacent, so they form one distinguished nonedge pair. Every other vertex is adjacent to both and must have potential one. Conversely each choice of pair and orientation produces a connected spanning tight graph; there are \(2m\) such facets, with \(4m-4\) tight edges each. For a two-level potential, assign each vertex zero or one. The tight edges comprise the complete bipartite cut between its color classes with only the cross-pair matching edges removed. When both classes have at least two vertices, this graph is connected for \(m\ge3\): any two cut vertices on the same side have a common opposite neighbor if that opposite side has at least three elements, while the remaining case of a two-vertex opposite side is connected through a third vertex on the larger side. Conversely a constant coloring has no tight edges, and a singleton color class isolates its matched mate; these are the only failures. Thus from \(4^m\) binary assignments exactly \(2\) constant and \(4m\) singleton/complement-singleton assignments must be removed. Adding the three-level potentials gives \(4^m-2m-2\). This facet classification and total are also consequences of the general multipartite result of Higashitani–Jochemko–Michałek (Proposition 3.5), and are **not** asserted as newly discovered.

**3. Exact incidence polynomial.** In a binary coloring, let \(a\) pairs have values \((0,0)\), let \(b\) pairs have values \((1,1)\), and let \(c\) pairs be split; hence \(a+b+c=m\). The zero class has size \(2a+c=m+(a-b)\), and the one class has size \(2b+c=m-(a-b)\). Precisely the \(c\) split pairs account for missing crossing graph edges. Consequently the facet contains
\[
(2a+c)(2b+c)-c=m^2-(a-b)^2-c
\]
vertices. This class has exactly \(m!2^c/(a!b!c!)\) labeled assignments. The two constants contribute two formal degree-zero terms. Each of the \(4m\) invalid singleton assignments has \(2m-2\) crossing edges. Each of the \(2m\) genuine three-level facets has \(4m-4\) tight edges. Removing and adding these contributions gives the claimed \(P_m(t)\), with no overcounting because potentials are normalized by their minimum.

**4. Moments and limiting fluctuations.** Sample each of the \(2m\) binary vertex labels independently and uniformly. For the \(i\)-th pair put \(X_i=1\) for \((0,0)\), \(X_i=-1\) for \((1,1)\), and \(X_i=0\) for a split pair. Thus \(\mathbb P(X_i=\pm1)=1/4\) and \(\mathbb P(X_i=0)=1/2\), independently. Define \(D=\sum_iX_i=a-b\), and \(C=\sum_i(1-X_i^2)=c\). The incidence of this unconditioned binary cut, including the invalid cases, is
\[
J=m^2-D^2-C=m(m-1)-2\sum_{i<j}X_iX_j.
\]
Since the variables are centered, independent, and satisfy \(\mathbb E X_i^2=1/2\), cross-covariances between distinct pair products vanish. Consequently
\[
\mathbb E J=m(m-1),\qquad\operatorname{Var}(J)=\frac{m(m-1)}2.
\]
The \(4^m\) binary labelings therefore have first raw sum \(4^m m(m-1)\) and second raw sum \(4^m[m^2(m-1)^2+m(m-1)/2]\). Removing the \(4m\) singleton assignments of incidence \(2m-2\) and adding the \(2m\) exceptional potentials of incidence \(4m-4\) leaves the first raw sum unchanged and adds exactly \(16m(m-1)^2\) to the second; constants contribute zero. This proves both exact moment formulas.

By the central limit theorem, \(D/\sqrt m\) converges to \(N(0,1/2)\); by the law of large numbers, \(C/m\) converges in probability to \(1/2\). Hence \((m^2-J)/m=(D/\sqrt m)^2+C/m\) converges to \((Z^2+1)/2\). Conditioning on the valid binary colorings and mixing in the \(2m\) exceptional facets changes the unconditioned labeling law in total variation by at most a constant multiple of \(m/4^m\). Thus the same distributional limit holds for uniformly sampled facets. Their exact moments also give \(\operatorname{Var}(I_m)\sim m^2/2\), with the correction terms exponentially negligible.

**5. Maximizers and symmetry types.** Maximal incidence minimizes \(D^2+C\). If \(m\) is even, the minimum zero is possible only for \(c=0\) and \(a=b=m/2\), yielding \(\binom m{m/2}\) maximal facets. If \(m\) is odd, the minimum is one, attained by \(c=0\), \(|a-b|=1\), or \(c=1\), \(a=b\), giving the two binomial terms displayed above; the three-level facets tie only at \(m=3\), contributing another six. The graph automorphism group permutes distinguished pairs and exchanges the two entries within each; binary-coloring orbits are therefore labeled by \((a,b,c)\). Global inversion swaps \(a\) and \(b\). Discard the constant and singleton orbits and add one orbit of three-level facets. Writing \(N_m=[\binom{m+2}{2}+\lfloor m/2\rfloor+1]/2\) for the number of unordered \(a,b\) choices with \(a+b\le m\), the result is \(O_m=N_m-1\). If \(a=b\), the orbit has size \(m!2^c/(a!b!c!)\); if \(a\ne b\), it has twice that size. The exceptional orbit has size \(2m\). This specifies every orbit and its cardinality.

## Verification
The standalone program `verify.py` uses only Python's standard library. It independently enumerates normalized integral functions on all \(2m\) vertices, checks every edge-Lipschitz inequality, constructs the graph of tight edges, and tests spanning connectivity; it **does not assume the incidence-polynomial classification to decide eligibility**. For \(m=3,4,5,6\) it independently computes every facet, the full histogram of facet vertex counts, the maximum incidence and multiplicity, and the complete orbits under natural generators. It compares all results with the theorem and checks the exact moment identities.

It reports respectively \(56,246,1012,4082\) facets, \(5,8,11,15\) symmetry orbits, and incidence histograms
\[
\begin{array}{c|l}
3&(6:32),(8:24)\\
4&(10:48),(12:96),(14:96),(16:6)\\
5&(14:80),(16:20),(18:160),(20:272),(22:400),(24:80)\\
6&(18:120),(20:24),(24:320),(26:120),(28:480),(30:928),(32:1470),(34:600),(36:20).
\end{array}
\]
Its exhaustive finite calculations corroborate, but do not substitute for, the all-\(m\) combinatorial proof and probabilistic limit argument.

## Relationship to prior work
Higashitani, Jochemko and Michałek (2018, arXiv:1807.07678v1), Theorem 3.1 and Proposition 3.5, already provide the connected-tight-edge facet criterion and **a complete facet-potential classification and total facet count for arbitrary complete multipartite graphs**. The specialization \(F_m=4^m-2m-2\) is therefore known; it is included solely for context and normalizing the uniform facet distribution. D'Alì, Delucchi and Michałek (arXiv:1910.05193v1; Electronic Journal of Combinatorics 2022, Theorem 11) explain the same criterion and the correspondence between a facet's vertices and its oriented tight edges. Aliaga (2021, arXiv:2102.01219v1) concerns extreme molecules and real Lipschitz-free spaces. Chen, Davis and Korchevskaia (2021, arXiv:2107.12315v1) study facet subgraphs more generally. Mori, Mori and Ohsugi (2023, arXiv:2312.11287v1) analyze facet-number formulas, including the earlier multipartite theorem. The specific evaluated incidence generating polynomial, its moment sequence, its non-Gaussian limit, and its symmetry-refined multiplicity law were not found in the inspected works. These statements are new calculations from established structural inputs, not an assertion that the structural inputs are original.

## Limitations
The scope is the real unit-edge cocktail-party graph family \(m\ge3\), with its natural graph symmetry and central inversion. The limiting distribution describes a **uniform random facet**, not uniform random graph vertices, uniformly random supporting hyperplanes, or arbitrary complete multipartite graphs. Other combinatorial or probabilistic formulations of the same quantities could exist in literature or datasets not identified by the searches; that residual novelty risk remains. No independent scientific audit has been conducted.

## References
1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (first public July 20, 2018), Theorem 3.1, Proposition 3.5.
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (2019); *Electronic Journal of Combinatorics* 29(3), P3.24 (2022), Theorem 11.
3. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219v1 (2021).
4. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315v1 (2021).
5. A. Mori, K. Mori, H. Ohsugi, *Number of facets of symmetric edge polytopes arising from join graphs*, arXiv:2312.11287v1 (2023).
6. A. Alexander, M. Fradelizi, R. García-Lirola, A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642v1 (2019).
