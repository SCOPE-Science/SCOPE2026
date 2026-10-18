# Equal-order radius-one nonlocality of random-walk cover-time response on trees

## Finding
For a connected finite simple graph \(G\), a starting vertex \(s\), and a nonedge \(uv\), let \(C_s(G)\) be the expected number of steps required by simple random walk started at \(s\) to visit every vertex, and define its signed edge-insertion response
\[
\Delta_s(G;u,v)=C_s(G+uv)-C_s(G).
\]
There exist **two trees of the same order, eleven**, with marked triples \((s,u,v)\) having identical ambient-degree-labelled rooted radius-one neighborhoods, all three pairwise marked distances, marked degrees, and effective resistance between \(u\) and \(v\), yet their responses have opposite signs. Explicitly, the trees below satisfy
\[
\Delta_1(T_A;10,0)=-\frac{1162717427}{813580152}<0,
\qquad
\Delta_4(T_B;9,5)=\frac{3127}{83076}>0.
\]
Thus these invariant data do not determine even the **sign** of the cover-time change when both configurations have the same number of vertices, already at radius one.

## Assumptions and scope
All graphs here are unweighted, connected, finite and simple. Walk steps are chosen uniformly among adjacent vertices; the starting vertex counts as visited at time zero. Vertex labels are \(0,1,\ldots,10\). The entire description of each tree is its edge set:

\[
\begin{aligned}
E(T_A)=\{&(0,3),(1,6),(2,3),(3,9),(4,5),\\
          &(4,9),(5,7),(5,8),(6,9),(9,10)\},\\[2pt]
(s_A,u_A,v_A)&=(1,10,0),\\[6pt]
E(T_B)=\{&(0,2),(0,6),(1,6),(2,3),(2,9),\\
          &(2,10),(3,5),(3,8),(4,10),(7,8)\},\\[2pt]
(s_B,u_B,v_B)&=(4,9,5).
\end{aligned}
\]
Both graphs have exactly ten edges and are connected, hence they are trees. Neither insertion edge is present initially. In both cases the degrees of \((s,u,v)\) equal \((1,1,1)\), and the marked distances are
\[
\bigl(d(s,u),d(s,v),d(u,v)\bigr)=(3,4,3).
\]
The three rooted radius-one neighborhoods are disjoint, because each inter-marker distance is at least three. Each consists of a marked leaf with its one neighbor. The corresponding neighbor's **ambient** degree is, respectively, \(2\), \(4\), and \(3\). Thus the three ambient-degree-labelled rooted neighborhoods match under a marked-root-preserving isomorphism. As every edge of a tree has unit electrical resistance, \(R_{\mathrm{eff}}(u,v)=d(u,v)=3\) in both cases.

## Proof
Write \(V=\{0,\ldots,10\}\). For every visited set \(S\subseteq V\) and current vertex \(x\in S\), let \(F_G(S,x)\) denote the expected additional steps before all vertices are visited. For \(S=V\), \(F_G(V,x)=0\). For every proper \(S\), first-step conditioning gives the following exact linear system in the unknowns \(F_G(S,x)\), \(x\in S\):
\[
\deg_G(x)F_G(S,x)-\sum_{y\sim x,\ y\in S}F_G(S,y)
=\deg_G(x)+\sum_{y\sim x,\ y\notin S}F_G(S\cup\{y\},y).
\tag{1}
\]
The right side only uses strictly larger visited sets. For each proper nonempty \(S\), the substochastic transition matrix of the walk killed on leaving \(S\) has spectral radius strictly less than one: the connected graph guarantees that, starting at any vertex in \(S\), the walk can exit \(S\) in finitely many steps with uniformly positive probability. Thus every system (1) is uniquely solvable over the rationals, descending through all visited sets. The answer is \(C_s(G)=F_G(\{s\},s)\).

Exact rational elimination on (1) for the four graphs \(T_A\), \(T_A+10\,0\), \(T_B\), and \(T_B+9\,5\) yields
\[
\begin{array}{c|cc}
 & C_s(T)& C_s(T+uv)\\ \hline
A & \dfrac{1409284291}{16327080} & \dfrac{16056931351603}{189157385340}\\[6pt]
B & \dfrac{3046636}{33495} & \dfrac{1722497083}{18929460}
\end{array}
\]
Subtracting gives the two exact differences displayed in the Finding. Their opposite signs prove the claim. All graph invariants asserted above follow by directly traversing the supplied ten-edge lists; the accompanying verifier checks them mechanically.

## Verification
Run `python3 verify_cover.py` with the Python standard library. The program builds all four graphs from the displayed edges, checks the order, degrees, pairwise distances, and degree-labelled radius-one rooted neighborhoods, then computes both cover times by rational first-step elimination. It independently recomputes each cover time from inclusion-exclusion over hitting times:
\[
C_s(G)=\sum_{\emptyset\ne B\subseteq V\setminus\{s\}}(-1)^{|B|+1}\,\mathbb E_s[\tau_B],
\qquad \tau_B=\inf\{t\ge0:X_t\in B\}.
\]
This identity follows by inclusion-exclusion for the events that particular vertices remain unvisited, summing over integer time. Each expected hitting time is determined by a separate rational Dirichlet system. The two computational routes agree exactly on every reported fraction and produce `VERIFY_OK`. This is an exact finite proof certificate, not a Monte Carlo experiment or a claim of a general all-orders classification.

## Relationship to prior work
Si's *Nonlocality of Cover-Time Changes Under Edge Addition* (first publicly available August 19, 2026, arXiv:2608.27474) proves a sign-changing nonlocality construction at every finite neighborhood radius while explicitly stating that its two graphs have different orders and that the equal-order version remains open. The present construction resolves the **fixed radius-one same-order instance**, even after matching all three marked distances; it makes no claim about radius two or higher. The source abstract was accessible; its complete manuscript could not be inspected, so possible unstated related examples are a residual priority risk.

Barlow, Ding, Nachmias, and Peres (2010), Proposition 1.4, give a general factor-four upper bound on the effect of adding an edge on worst-start cover time, not equal-order local sign indeterminacy for fixed-start cover times. Zlatanov and Kocarev (2009) supply general exact cover-time distribution formulas, including inclusion-exclusion; those formulas are compatible with and can be used to verify the numerical witnesses, but do not themselves exhibit the pair with these matching graph invariants.

## Limitations
This is an **existence theorem for two explicit eleven-vertex trees at radius one**. It does not prove that eleven is minimal, that a same-order construction works for every radius, or that any local invariant ever determines the response for restricted graph families. The second positive difference is small but strictly positive as an exact reduced rational number. Novelty is a reasoned comparison with the accessible literature, not a proof that no unindexed equivalent witness exists. Independent scientific validation has not been conducted.

## References
1. I. M. Si, *Nonlocality of Cover-Time Changes Under Edge Addition*, arXiv:2608.27474 (first publicly released 2026-08-19), https://arxiv.org/abs/2608.27474.
2. M. T. Barlow, J. Ding, A. Nachmias, and Y. Peres, *The evolution of the cover time*, arXiv:1001.0609; *Combinatorics, Probability and Computing* 20 (2011), 331–345, https://www.microsoft.com/en-us/research/wp-content/uploads/2017/01/1001.0609v2.pdf.
3. N. Zlatanov and L. Kocarev, *Random walks on networks: cumulative distribution of cover time*, *Physical Review E* 80 (2009), 041102, DOI:10.1103/PhysRevE.80.041102, https://manmade.maths.qmul.ac.uk/publications/CUmulativeTimeDistr_PRE.pdf.
