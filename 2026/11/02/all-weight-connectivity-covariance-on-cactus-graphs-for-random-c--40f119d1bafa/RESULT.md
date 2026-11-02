# All-weight connectivity covariance on cactus graphs for random-cluster and forest laws

## Finding
Let \(G=(V,E)\) be a finite connected simple cactus graph: every edge belongs to at most one simple cycle. Give every edge an arbitrary positive weight. For any four vertices \(a,b,c,d\), write \(A=\{a\leftrightarrow b\}\) and \(B=\{c\leftrightarrow d\}\), where connectivity refers to the selected random subgraph. Under each of the following laws,

\[
\operatorname{Cov}(\mathbf1_A,\mathbf1_B)=\mathbb P(A\cap B)-\mathbb P(A)\mathbb P(B)\ge 0.
\]

The laws are (i) the arboreal-gas law, assigning a forest \(F\subseteq E\) probability proportional to \(\prod_{e\in F}w_e\), and (ii) the Fortuin–Kasteleyn random-cluster law, assigning any \(F\subseteq E\) probability proportional to \(q^{k(F)}\prod_{e\in F}w_e\), for every \(q>0\), with \(k(F)\) its number of connected components including isolated vertices. The nontrivial random-cluster regime is \(0<q<1\); for \(q\ge1\), positive association also follows from the known FKG inequality. The theorem settles the two-connectivity correlation inequality for every finite weighted cactus, including arbitrarily many cycles joined at cut vertices. It makes no claim for graphs with overlapping cycles.

## Assumptions and scope
The graph is finite, connected, loopless and simple; every biconnected block is an edge or a cycle. All edge weights are finite and strictly positive. The random-cluster parameter is any real \(q>0\), not necessarily integral. The four vertices may coincide, although the motivating conjectures require them distinct. Forests need not connect all vertices, and all random-cluster configurations are allowed. The normalization is exactly \(\prod_{e\in F}w_e\) times \(1\) for forests or \(q^{k(F)}\) for random-cluster configurations; there is no per-component factor in the forest law.

## Proof
**A two-partition nonempty-support lemma.** Partition a finite edge set in two ways, into two rows and two columns. Each of the four cells has independent closed-edge activity \(t_{ij}=\prod_{e\text{ in cell }ij}(1+\rho_e)-1\ge0\), where \(\rho_e>0\). Weight a nonempty closed-edge set by the product of its constituent \(\rho_e\), and the empty closed-edge set by an arbitrary extra factor \(\kappa\ge0\). Put \(x=t_{11},y=t_{12},z=t_{21},w=t_{22}\), and define

\[
U=(1+x)(1+y)(1+z)(1+w)-1,\quad S=x+y+z+w,
\]
\[
R=x+y+xy+z+w+zw,\qquad C=x+z+xz+y+w+yw.
\]

Let \(A_0\) be the event that the closed-edge set is entirely contained in one row, and \(B_0\) the analogous event for one column. Their unnormalized masses and the joint mass are, respectively, \(\kappa+R\), \(\kappa+C\), and \(\kappa+S\), with normalizer \(\kappa+U\). Indeed a nonempty set lies in both one row and one column exactly when it is contained in one cell. Hence

\[
(\kappa+U)^2\operatorname{Cov}(\mathbf1_{A_0},\mathbf1_{B_0})=SU-RC+\kappa(U+S-R-C).
\]

The second factor is explicitly

\[
U+S-R-C=xw+yz+xyz+xyw+xzw+yzw+xyzw\ge0.
\]

For the first factor, direct multiplication yields the coefficientwise nonnegative identity

\[
\begin{aligned}
SU-RC={}&xw(x+w)(1+y+z)+yz(y+z)(1+x+w)\\
&+xyz+xyw+xzw+yzw\\
&+xyzw(4+x+y+z+w)\ge0.
\end{aligned}
\]

This proves the lemma for every nonnegative choice of \(x,y,z,w,\kappa\), including empty cells. A standalone exact polynomial check is supplied, but the displayed identities are self-contained algebraic certificates.

**Cycle blocks.** For a simple cycle with positive open-edge activities \(a_e\), a configuration is specified by its closed-edge set \(D\). Give every nonempty \(D\) relative weight \(\prod_{e\in D}a_e^{-1}\) and the empty set relative weight \(\kappa\). For any distinct vertices \(u,v\), the cycle has precisely two edge-disjoint arcs between them. Since a closed edge destroys its arc, \(u\leftrightarrow v\) holds exactly when all closed edges lie in one of those two arcs (and it always holds when \(D\) is empty). For two vertex pairs, the two arc partitions form the rows and columns of the lemma, with \(\rho_e=a_e^{-1}\). Thus any two cycle-block connectivity indicators have nonnegative covariance for every \(\kappa\ge0\).

For the arboreal-gas law on a cycle, all edge subsets except the full cycle are allowed. Relative to the open-edge product, this is the preceding cycle law with \(a_e=w_e\) and \(\kappa=0\). For the random-cluster law, let \(a_e=w_e/q\) and \(\kappa=q\). A proper cycle-edge subset has component count \(|V|-|F|\) and hence relative weight \(\prod_{e\notin F}(q/w_e)\), while the full-cycle subset has component count one and an additional relative factor \(q\). Thus the lemma applies with no restriction \(q<1\).

**Factorization over cactus blocks.** In a cactus, the simple cycles are edge-disjoint, and a selected subgraph \(F\) has cyclomatic number exactly equal to the number \(c(F)\) of its original cycle blocks whose every edge is selected. Consequently

\[
k(F)=|V|-|F|+c(F),\qquad
q^{k(F)}\prod_{e\in F}w_e=q^{|V|}\prod_{e\in F}\frac{w_e}{q}\prod_{C\text{ cycle block}}q^{\mathbf1_{E(C)\subseteq F}}.
\]

The right side factors over edge-disjoint cycle and bridge blocks. The forest restriction likewise factors into the requirement that no cycle block be fully occupied. All blocks are therefore independent under either measure. A bridge block is an independent Bernoulli edge and has nonnegative covariance for two connection requirements (which are either that same edge be open or a trivial requirement). For arbitrary global vertices \(u,v\), their connectivity is the intersection of the local connectivity events along the unique block-cut-tree route from \(u\) to \(v\). Given two such global events \(A,B\), write their blockwise indicators as \(A_i,B_i\), using the constant one on blocks not on a route. Independence and cycle/bridge covariance yield

\[
\mathbb P(A\cap B)=\prod_i\mathbb E(A_iB_i)
\ge\prod_i\mathbb E(A_i)\mathbb E(B_i)
=\mathbb P(A)\mathbb P(B).
\]

This completes both claims, including coincident vertices and bridge-only routes.

## Verification
The standalone Python 3 program `verify_cactus.py` checks the two exact multivariate polynomial identities by coefficient dictionaries and confirms nonnegative coefficients. It independently enumerates all edge subsets, with exact rational weights, on seven finite cactus topologies (including cycles, attached bridges and multiple cycles). Across two edge-weight patterns and four laws per graph (arboreal gas, and random cluster with \(q=1/3,2/3,2\)), it checks 13,560 covariance numerators \(\mathbb P(A\cap B)-\mathbb P(A)\mathbb P(B)\) by cross multiplication of exact partition sums. Reproduce with `python3 verify_cactus.py`. These finite tests are not a proof of the universal theorem; the preceding block-factorization and positive-polynomial identities supply that proof.

## Relationship to prior work
Çiçeksiz and Ravichandran, *Negative Correlations for Forests and the \(q<1\) Random Cluster Model* (first public September 30, 2026), formulate positive covariance of arbitrary two vertex-connectivity events as Conjectures 6.2 (arboreal gas) and 6.3 (random cluster). Their Proposition 6.1 concerns sufficiently large equal fugacity under additional connectivity assumptions, not the all-weight cactus result here. The edge-negative-correlation conjecture of Grimmett and Winkler is a different inequality and does not by itself give these vertex-connectivity covariances. FKG already handles \(q\ge1\), but not \(0<q<1\). The present proof exploits the exact cycle-block factorization and a nonnegative two-partition support identity; it does not establish either conjecture for arbitrary graphs.

## Limitations
The argument requires edge-disjoint simple cycles. It does not cover theta graphs, general series-parallel graphs, graphs with overlapping cycles or the conjectured arbitrary-graph inequalities. It does not prove negative association of edges, nor coefficientwise positivity in the original edge-weight variables, nor higher-order association of three or more connectivity events. Historical priority should be checked independently, particularly against earlier graph-polynomial and block-factorization literature. Independent mathematical audit has not been performed.

## References
1. R. A. Çiçeksiz and M. Ravichandran, *Negative Correlations for Forests and the \(q<1\) Random Cluster Model*, arXiv:2610.00549, initial public version September 30, 2026, Section 6 and Conjectures 6.2–6.3. https://arxiv.org/abs/2610.00549
2. G. R. Grimmett and S. N. Winkler, *Negative association in uniform forests and connected graphs*, arXiv:math/0302185, 2003; Random Structures & Algorithms 24 (2004), 444–460. https://arxiv.org/abs/math/0302185
3. H. Park, *The \(q<1\) Random-Cluster Model on Wired Trees: Uniqueness and Negative Dependence*, arXiv:2608.08565, 2026. https://arxiv.org/abs/2608.08565
