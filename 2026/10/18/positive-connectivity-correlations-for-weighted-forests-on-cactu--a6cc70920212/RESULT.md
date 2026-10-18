# Positive connectivity correlations for weighted forests on cactus graphs

## Finding
Let \(G=(V,E)\) be any finite connected simple cactus graph: every two distinct simple cycles have at most one common vertex. Give each edge \(e\) an arbitrary fugacity \(\lambda_e>0\), and draw a spanning forest \(F\subseteq E\) with law
\[
 \mathbb P(F=A)=\frac{\prod_{e\in A}\lambda_e}{\sum_{B\subseteq E:\,B\text{ acyclic}}\prod_{e\in B}\lambda_e}
 \quad\text{for each acyclic }A\subseteq E.
\]
For every four vertices \(s,t,u,v\in V\), with coincident vertices allowed,
\[
 \boxed{\mathbb P(s\leftrightarrow t,\ u\leftrightarrow v)
 \ge \mathbb P(s\leftrightarrow t)\mathbb P(u\leftrightarrow v).}
\]
Connectivity refers to the same sampled forest. The statement holds for arbitrary, independently specified positive fugacities and an unbounded number of cycles, at every fugacity scale.

## Assumptions and scope
A cactus may have bridges and cycles meeting at articulation vertices; it has no graph block other than an edge or a simple cycle. An event \(x\leftrightarrow y\) means that the forest contains a path between \(x\) and \(y\); when \(x=y\), this event is certain. No regularity, uniformity, or lower bound is assumed for the edge weights besides strict positivity. For each edge define \(p_e=\lambda_e/(1+\lambda_e)\in(0,1)\).

## Proof
**1. Reduction to independent cyclic blocks.** Let independent bond-percolation indicators have inclusion probabilities \(p_e\). Conditional on having no cycle, their law is exactly the displayed forest law: the product of the omitted-edge factors is a constant multiple of \(\prod_{e\in A}\lambda_e\). In a cactus the acyclicity condition is precisely that no cyclic block has all its edges present. These conditions involve disjoint sets of edges, hence the conditional law factors over its blocks. Bridge indicators remain independent Bernoulli variables; on a cycle the edge indicators are independent Bernoulli variables conditioned on not all being one.

In the block-cut tree, a connection between two vertices occurs exactly when the corresponding entry and exit vertices are connected within **each** block on the unique block-tree route. Thus its indicator is a product of independent block-local connection indicators, including constants one for blocks not traversed. It suffices to show nonnegative covariance of any two connection indicators on a single cycle; for an edge block, both such indicators are either one or the same Bernoulli edge indicator, so the assertion is immediate. If each block has \(\mathbb E[A_bB_b]\ge\mathbb E[A_b]\mathbb E[B_b]\), independence gives
\[
 \mathbb E\left[\prod_b A_b\prod_b B_b\right]
 =\prod_b\mathbb E[A_bB_b]
 \ge\prod_b\mathbb E[A_b]\prod_b\mathbb E[B_b].
\]

**2. Reduction of one cycle to at most four Bernoulli variables.** If an endpoint pair coincides, its connection event is certain. If both pairs coincide as *unordered pairs*, their covariance is a variance. Otherwise, order the three or four distinct marked vertices cyclically and group all edges between consecutive marks into segments. The indicator that every edge of segment \(i\) is open is Bernoulli with probability equal to the product of its edge-open probabilities; these segment indicators are independent before conditioning. The forest condition excludes exactly the all-open segment configuration. Write \(r\) for the product of the three or four segment probabilities. Every conditional event probability below has denominator \(1-r\); consequently its covariance has denominator \((1-r)^2>0\).

**3. Three distinct marks.** Up to cyclic relabeling, put segment success probabilities \(x,y,z\in(0,1)\), and let the connection events join the first mark to the second and to the third. Their *unconditioned numerators after excluding the all-open state* are
\[
 N_A=x+yz-2xyz,\quad N_B=z+xy-2xyz,\quad
 N_{AB}=xy+xz+yz-3xyz.
\]
A direct expansion yields
\[
 (1-xyz)N_{AB}-N_AN_B
 =y(1-x)(1-z)\bigl[x(1-z)+z(1-x)+xz(1-y)\bigr]\ge0.
\]

**4. Four distinct marks, noncrossing pairing.** With consecutive segment probabilities \(a,b,c,d\), consider the endpoint pairs formed by the first two and the last two marks. Set \(r=abcd\). The corresponding numerators are
\[
 N_A=a+bcd-2r,\qquad N_B=c+abd-2r,\qquad
 N_{AB}=ac+abd+bcd-3r.
\]
Consequently
\[
 (1-r)N_{AB}-N_AN_B
 =bd(1-a)(1-c)\bigl[a(1-c)+c(1-a)+ac(1-bd)\bigr]\ge0.
\]
The other noncrossing pairing is a cyclic rotation of this case.

**5. Four distinct marks, crossing pairing.** Now connect the first mark to the third, and the second to the fourth. The numerators are
\[
 N_A=ab+cd-2r,\quad N_B=bc+da-2r,\quad
 N_{AB}=abc+abd+acd+bcd-4r.
\]
Define \(\beta_0(t)=(1-t)^2\), \(\beta_1(t)=2t(1-t)\), and \(\beta_2(t)=t^2\). For a four-digit tuple \(k=(k_1,k_2,k_3,k_4)\in\{0,1,2\}^4\), let
\[\mathcal B_k=\beta_{k_1}(a)\beta_{k_2}(b)\beta_{k_3}(c)\beta_{k_4}(d).\]
Let \(\operatorname{Cyc}(k)\) denote the set of its distinct cyclic rotations, and let \(\operatorname{Dih}(k)\) denote its distinct cyclic rotations and reversals. Expansion of the polynomial gives the positive Bernstein certificate
\[
\begin{aligned}
 (1-r)N_{AB}-N_AN_B
 &=\tfrac18\sum_{k\in\operatorname{Cyc}(0,1,1,1)}\mathcal B_k
 +\tfrac14\sum_{k\in\operatorname{Dih}(0,1,1,2)}\mathcal B_k\\
 &\quad+\tfrac12\sum_{k\in\operatorname{Cyc}(0,2,1,2)}\mathcal B_k
 +\tfrac14\mathcal B_{(1,1,1,1)}
 +\tfrac18\sum_{k\in\operatorname{Cyc}(1,1,1,2)}\mathcal B_k\ge0.
\end{aligned}
\]
The orbit sizes are respectively \(4,8,4,1,4\). Every summand is nonnegative for \(0\le a,b,c,d\le1\). The identity is independently reproducible using exact rational arithmetic in `verify.py`. Both sides have degree at most two in each variable; agreement on the \(3^4\) grid with coordinates \(0,1/2,1\) is therefore an exact polynomial identity by repeated univariate interpolation, not numerical evidence. This completes the cycle inequality and, by step 1, the cactus theorem.

## Verification
Run `python3 verify.py` using the standard library. The program checks the shared-vertex identity at \(3^3\) rational grid points, the noncrossing and crossing identities at \(3^4\) points each, the explicit positivity of the Bernstein certificate at the same grid, and exhaustive weighted forest enumeration for several cycles and multi-cycle cacti. The grid checks prove the finite polynomial identities because of the stated coordinate-wise degree bound. Forest enumerations independently check the setup but do not replace the general block argument.

## Relationship to prior work
Çiçeksiz and Ravichandran [1] study edge-negative correlation of weighted forests and the \(q<1\) random-cluster model, and discuss positive correlation of vertex-connectivity events as a broader problem; their Proposition 6.1 proves a large-fugacity case while Conjecture 6.2 explicitly asks for positive correlation at arbitrary fugacities. The present theorem instead establishes the two-connectivity inequality **for all arbitrary positive edge fugacities**, on every cactus graph. Bauerschmidt, Crawford, Helmuth and Swan [2], especially their definition (1.2), give the conditioning representation used in step 1 and study global forest behavior, not the stated cactus covariance inequality. Grimmett and Winkler [3] study edge-negative dependence, a different inequality. Neither edge-negative dependence nor the large-fugacity-only regime is, by itself, the all-fugacity positive connectivity statement established here.

## Limitations
The theorem does not cover graphs with overlapping cycles in one 2-connected block, random-cluster models at positive \(q\), or arbitrary increasing events. No statement about general graphs is proved. Section 6 of the full HTML preprint [1] was examined: Proposition 6.1 gives a large-fugacity assertion and Conjecture 6.2 explicitly states the general all-fugacity correlation inequality, without a cactus-class result. The 2021 thesis [4] also discusses connectivity-event correlations and remains a specific comparison risk because its full text could not be examined.

## References
1. R. A. Çiçeksiz and M. Ravichandran, *Negative Correlations for Forests and the \(q<1\) Random Cluster Model*, arXiv:2610.00549, first submitted 2026-09-30, https://arxiv.org/abs/2610.00549.
2. R. Bauerschmidt, N. Crawford, T. Helmuth, and A. Swan, *Random spanning forests and hyperbolic symmetry*, Communications in Mathematical Physics 381 (2021); preprint arXiv:1912.04854; accepted version https://www.repository.cam.ac.uk/bitstreams/fee3fef0-bc79-42b7-ad9c-6e8cdf671716/download.
3. G. R. Grimmett and S. N. Winkler, *Negative association in uniform forests and connected graphs*, Random Structures & Algorithms 24 (2004), 444–460; arXiv:math/0302185.
4. R. A. Çiçeksiz, *Negative dependence in discrete probability: notions, models and consequences*, M.S. thesis, Bogazici University (2021), https://digitalarchive.library.bogazici.edu.tr/items/15112caf-2516-46e5-b5f7-0cf73e2800af.
