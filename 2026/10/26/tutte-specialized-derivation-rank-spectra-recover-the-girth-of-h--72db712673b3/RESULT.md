# Tutte-specialized derivation rank spectra recover the girth of height-two incidence posets

## Finding
Let \(P\) be a finite poset in which no strictly increasing chain has three elements. Write \(G=(V,E)\) for its undirected Hasse graph and \(m=|E|\). Fix any finite field \(k=\mathbb F_q\). The incidence algebra \(A=I(P,k)\) has the **complete rank enumerator of its space of all \(k\)-linear derivations**
\[
R_{G,q}(t)=\sum_{D\in\mathrm{Der}_k(A)}t^{\mathrm{rank}_k(D)}
=\sum_{B\subseteq E}(q-1)^{|B|}t^{r(B)}\bigl(1+q(q-1)t\bigr)^{m-|B|}, \tag{1}
\]
where \(r(B)=|V|-c(B)\) and \(c(B)\) is the component count of the graph on **all** vertices with edge set \(B\). Formula (1) is a graphic-matroid invariant, valid without a restriction on characteristic. It gives \(R_{G,q}(1)=q^{2m}\), the number of derivations, and its degree is exactly \(m\) whenever \(m>0\).

Let \(F_{m,q}(t)=(1+(q^2-1)t)^m\). Acyclicity is equivalent to \(R_{G,q}=F_{m,q}\). For a graph with finite girth \(g\), let \(c_g\) count its distinct undirected simple cycles of length \(g\). Then
\[
[t^j](R_{G,q}-F_{m,q})=0\quad(0\le j<g-1),\qquad
[t^{g-1}](R_{G,q}-F_{m,q})=c_g(q-1)^g>0. \tag{2}
\]
Consequently the derivation rank histogram determines \(m\), whether there are any cycles, and, if so, both the girth and the number of shortest cycles. Since a height-two Hasse graph is bipartite, every finite \(g\) is even and at least four.

If \(G\) is unicyclic with unique cycle of length \(g\), then
\[
R_{G,q}(t)=F_{m,q}(t)+(q-1)^g t^{g-1}(1-t)F_{m-g,q}(t). \tag{3}
\]
For the four-cycle, over \(\mathbb F_2\), the coefficients in increasing rank order are \((1,12,54,109,80)\); over \(\mathbb F_3\) they are \((1,32,384,2064,4080)\).

## Assumptions and scope
A derivation is a \(k\)-linear map \(D:A\to A\) obeying \(D(ab)=D(a)b+aD(b)\). Ranks are ordinary \(k\)-vector-space ranks on \(A\), not ranks of inner derivations or dimensions of the derivation space. An isolated vertex contributes an extra scalar direct summand to \(A\) but no derivation parameters; all formulas allow isolated vertices and disconnected graphs. When \(m=0\), formula (1) gives the unique zero derivation and \(R_{G,q}(t)=1\). The statement has no asserted extension to length-three chains, where products of radical basis elements may be nonzero.

## Proof
**Step 1: all derivations and uniqueness of parameters.** The algebra has basis \(e_v=e_{vv}\) for \(v\in V\) and \(f_{uv}=e_{uv}\) for covers \(u<v\). Products involving two \(f\)-basis elements vanish, because the poset has height at most two. Let \(J\) be their \(k\)-span; thus \(J^2=0\). The diagonal span \(L=\bigoplus_{v\in V}ke_v\) is \(k^{|V|}\). For every derivation \(D\), the idempotent identities and pairwise orthogonality imply \(D(e_v)\in J\), while \(D(e_u f_{uv}e_v)=e_uD(f_{uv})e_v\) shows \(D(f_{uv})=\lambda_{uv} f_{uv}\), for uniquely determined \(\lambda_{uv}\in k\).

Indeed, the identity \(e_v^2=e_v\) forces each nonzero coefficient of \(D(e_v)\) to lie on an edge incident to \(v\). Differentiating \(e_u e_v=0\) for distinct vertices shows that on each cover edge \(u<v\) the coefficients in \(D(e_u)\) and \(D(e_v)\) are opposite. Hence there are unique \(x_{uv}\in k\) such that, for every diagonal \(h=\sum_v h_ve_v\),
\[
D(h)=\sum_{u<v}x_{uv}(h_v-h_u)f_{uv},
\qquad D(f_{uv})=\lambda_{uv}f_{uv}. \tag{4}
\]
Conversely, every independent choice of the \(2m\) scalars \(x_{uv},\lambda_{uv}\) defines a derivation: the first part of (4) is the inner commutator \([\sum x_{uv}f_{uv},h]\), the second is a bimodule-diagonal map on \(J\), and \(J^2=0\). Consequently \(|\mathrm{Der}_k(A)|=q^{2m}\), also when \(q\) has characteristic two.

**Step 2: operator rank.** Relative to \(A=L\oplus J\), the map (4) has output in \(J\) and is represented by the block row \([\,B_x\ \ \Lambda\,]\), where \(\Lambda\) is the diagonal \(m\times m\) matrix with entries \(\lambda_{uv}\), and the row of \(B_x\) indexed by the edge \(u<v\) is \(x_{uv}(e_v^*-e_u^*)\). Write \(S=\{e:\lambda_e\ne0\}\) and \(B=\{e:\lambda_e=0,\ x_e\ne0\}\); these are disjoint. Projection modulo \(\mathrm{im}\Lambda\) retains precisely rows of \(B_x\) indexed by zero \(\lambda_e\). Nonzero \(x_e\) scales oriented incidence rows without changing their span. Every oriented incidence matrix, over any field, has row rank \(|V|-c(B)=r(B)\), by reducing to a spanning forest and using that cycle rows depend on the forest rows. Therefore
\[
\mathrm{rank}_k(D)=|S|+r(B). \tag{5}
\]
For each edge in \(S\), there are \(q(q-1)\) choices of \((x_e,\lambda_e)\); in \(B\), there are \(q-1\) choices; outside \(S\cup B\), both parameters vanish. Fixing \(B\) and summing over \(S\subseteq E\setminus B\) yields (1).

**Step 3: Tutte specialization.** Let \(\rho=r(E)\), \(\alpha=q-1\), and \(\beta=1+q(q-1)t\). For the graphic matroid, define the Tutte polynomial by
\[
T_G(X,Y)=\sum_{B\subseteq E}(X-1)^{\rho-r(B)}(Y-1)^{|B|-r(B)}.
\]
The identity \(\beta^m\sum_B(\alpha/\beta)^{|B|}t^{r(B)}=\beta^{m-\rho}(\alpha t)^\rho T_G(1+\beta/(\alpha t),1+\alpha/\beta)\) is an equality of rational expressions whose value is the polynomial (1). This proves the asserted graphic-matroid invariance. The degree is \(m\) because taking all \(\lambda_e\ne0\) gives nonzero contributions to rank \(m\), and all ranks are at most \(m\).

**Step 4: forest baseline and first-cycle coefficient.** Replacing \(r(B)\) by \(|B|\) in (1) gives exactly \(F_{m,q}(t)\). Subtracting termwise,
\[
R_{G,q}(t)-F_{m,q}(t)=\sum_{\substack{B\subseteq E\\ \nu(B)>0}}(q-1)^{|B|}\beta^{m-|B|}t^{r(B)}(1-t^{\nu(B)}),\qquad \nu(B)=|B|-r(B). \tag{6}
\]
Only cyclic edge sets occur in the sum. If the shortest graph cycle has length \(g\), every cyclic \(B\) contains at least \(g\) edges and has rank at least \(g-1\), since a connected component containing a cycle contains at least \(g\) vertices and hence has rank at least \(g-1\). Equality \(r(B)=g-1\) occurs exactly when \(B\) consists of the edges of one shortest cycle: any extra edge raises rank or produces a chord yielding a shorter cycle. Consequently no term of (6) contributes below degree \(g-1\), and at that degree each shortest cycle contributes \((q-1)^g\); this proves (2) and the forest criterion. For a unicyclic graph, cyclic \(B\) are precisely the full cycle together with an arbitrary subset of the remaining tree edges. Summing them in (6) gives (3). \(\square\)

## Verification
The accompanying `verify_derivation_rank.py` constructs the incidence-algebra multiplication table, solves **all Leibniz equations** for the entries of an unknown linear operator, enumerates every resulting derivation over small prime fields, and computes each matrix rank by elimination; it does not assume (4) or (5). It independently computes the right-hand side of (1) by enumerating graph edge subsets and union-find component counts. Direct exhaustive cases include a single edge, disconnected edges, a star, a path, a four-cycle in characteristics two and three, a four-cycle with one leaf, and a six-cycle. In particular, the four-cycle coefficient rows cited above agree exactly, and every case has \(q^{2m}\) derivations. Separate polynomial-identity checks for \(q\in\{2,3,4,5,7,9\}\) confirm total counts and the four-cycle leading correction, but these arithmetic checks do not substitute for the proof for nonprime fields. Run `python3 verify_derivation_rank.py`; success prints `VERIFY_OK`.

## Relationship to prior work
Krylov and Tuganbaev describe the structure of derivations of general incidence rings (arXiv:2305.02984, especially Sections 14–19; journal treatment DOI 10.3390/math12070999). Their results include the decomposition into inner and additive derivations, transitive functions, and cycle-space conditions. Fornaroli and Khrypchenko describe skew derivations and related poset cohomology (arXiv:2307.08439, especially Sections 2–3). These descriptions establish the structural existence of the parameters used above, but the specified operator-rank distribution (1) and the shortest-cycle recovery law (2) are different statistical statements. The familiar Tutte polynomial and incidence-matrix rank theorem supply classical tools, not novelty assertions.

The rank distribution of **inner** derivations, equivalently the element-centralizer codimension distribution, is a different invariant: only potential edge weights occur there. For a forest every derivation is inner, so the binomial specialization is not claimed as a new standalone result. For a cyclic poset, outer derivations are present and the two distributions differ; formula (1) counts them all. For example, for the four-cycle over \(\mathbb F_2\), the inner-derivation rank histogram is \((1,4,30,53,40)\), while the all-derivation histogram is \((1,12,54,109,80)\). This non-equivalence is central to the scope distinction.

## Limitations
The finite-field result does not cover nonlinear or field-semilinear derivations, higher-height posets, or arbitrary preorders. The Tutte formula may have equivalent expressions under graph-matroid rank enumerators or incidence-algebra differential-operator terminology; no exhaustive priority claim is made. The structural derivation decomposition and basic Tutte identities are prior mathematics. The result does not reconstruct the entire graph: it recovers only the stated cycle data and is invariant under graphic-matroid equivalence. Exhaustive tests were restricted to modest examples and prime fields; the proof is the basis for the universal quantifiers.

## References
1. P. Krylov and A. Tuganbaev, *Incidence Rings: Automorphisms and Derivations*, arXiv:2305.02984, first posted 2023-05-04, particularly Sections 14–19. https://arxiv.org/abs/2305.02984
2. P. Krylov and A. Tuganbaev, *Derivations of Incidence Algebras*, Mathematics **12** (2024), 999, DOI:10.3390/math12070999. https://doi.org/10.3390/math12070999
3. É. Z. Fornaroli and M. Khrypchenko, *Skew derivations of incidence algebras*, arXiv:2307.08439, first posted 2023-07-17. https://arxiv.org/abs/2307.08439
