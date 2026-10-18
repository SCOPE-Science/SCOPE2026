# Sharp negative influence in signed Friedkin–Johnsen networks

## Finding

For every integer \(n\ge3\) and every connected, undirected, simple \(n\)-vertex graph with edge signs in \(\{-1,1\}\), let \(L_\sigma\) be its *opposing signed Laplacian*: an edge \(ij\) contributes \((e_i-\sigma_{ij}e_j)(e_i-\sigma_{ij}e_j)^\top\). Put
\[
h=(I+L_\sigma)^{-1}\mathbf1.
\]
For arbitrary innate opinions \(s\), the sum of equilibrium expressed opinions is \(h^\top s\). Every coordinate obeys the *sharp universal bound*
\[
\boxed{h_i\ge \frac{3-n}{n+1}\qquad(1\le i\le n).}
\]
For every \(n\ge3\), equality is attained by a hostile hub joined negatively to all other vertices, with any subset of positive links among those other vertices. In that family the hub's centrality is \((3-n)/(n+1)\) and every other centrality is \((n-1)/(n+1)\). Consequently, for \(n\le3\) a nonnegative innate-opinion vector cannot yield a negative aggregate equilibrium opinion, whereas four vertices suffice: set the sole positive innate opinion at the hostile hub of a four-vertex negative star, obtaining total expressed opinion \(-1/5\).

The entire first negative layer can also be characterized. Among the \(624\) connected labeled four-vertex signed simple graphs (absent, positive or negative edge for each of six pairs), exactly \(104\) have at least one negative coordinate of \(h\). These comprise exactly eight isomorphism classes. Equivalently, negativity occurs exactly when **all negative edges are incident to one vertex, at least two such negative edges exist, and that vertex has no positive incident edge**. Connectedness is retained in this characterization.

## Assumptions and scope

Every present edge has *unit absolute weight*; no loops or parallel edges occur. Every vertex has a unit innate-opinion/stubbornness coefficient. The graph is fixed and connected. The synchronous FJ update is
\[
z_i(t+1)=\frac{s_i+\sum_{j\sim i}\sigma_{ij}z_j(t)}{1+d_i}.
\]
The strict row-substochastic absolute-value update matrix makes this converge from every initial expressed-opinion vector to \(z=(I+L_\sigma)^{-1}s\). The aggregate objective is the unnormalized sum \(\mathbf1^\top z\), not centered polarization or absolute influence.

A signed graph on four labeled vertices is encoded in the edge order \((01,02,03,12,13,23)\), where `-` means negative, `+` means positive and `.` means absent. The eight representative strings, with the number of labeled realizations of each class, are:

| Representative | Labeled realizations |
|---|---:|
| `---...` | 4 |
| `---..+` | 12 |
| `---.++` | 12 |
| `---+++` | 4 |
| `--...+` | 24 |
| `--..++` | 12 |
| `--.+.+` | 24 |
| `--.+++` | 12 |

The counts sum to \(104\). Candidate labels here are graph vertices rather than election candidates.

## Proof

**Existence and centrality identity.** For real \(x\),
\[
x^\top(I+L_\sigma)x=\sum_i x_i^2+\sum_{ij\in E}(x_i-\sigma_{ij}x_j)^2>0
\]
when \(x\ne0\), so the inverse exists and is symmetric. Hence
\(\mathbf1^\top(I+L_\sigma)^{-1}s=h^\top s\).

**Comparison lemma.** Fix vertex \(i\). Write the signed and unsigned (all-positive, same support) matrices in block form
\[
I+L_\sigma=\begin{pmatrix}1+d&-b^\top\\-b&C\end{pmatrix},\qquad
I+L_+=\begin{pmatrix}1+d&-a^\top\\-a&C_+\end{pmatrix},
\]
where \(d=d_i\), \(a=|b|\), and \(C,C_+\) are the principal blocks deleting row and column \(i\). Every principal block is strictly diagonally dominant after taking absolute values: its diagonal is \(1+d_j\), while its off-diagonal absolute row sum is at most \(d_j\). Therefore the Neumann series, using the common positive diagonal matrix, proves the *entrywise* resolvent comparison
\[
|C^{-1}|\le C_+^{-1}.
\]
In particular \(C_+^{-1}\) is entrywise nonnegative. Let
\[
t=a^\top C_+^{-1}\mathbf1,\qquad
w=a^\top C_+^{-1}a,\qquad D_+=1+d-w>0.
\]
Schur complementation gives
\[
h_i=\frac{1+b^\top C^{-1}\mathbf1}{1+d-b^\top C^{-1}b}.
\]
Its denominator is positive and at least \(D_+\); its numerator is at least \(1-t\). If its numerator is nonnegative, then \(h_i\ge0\). If negative, dividing the lower (nonpositive) bound by the larger denominator yields
\[
h_i\ge\frac{1-t}{D_+}.
\]
Since \((I+L_+)\mathbf1=\mathbf1\), the lower block gives \(C_+\mathbf1=\mathbf1+a\). Thus \(C_+^{-1}\mathbf1=\mathbf1-C_+^{-1}a\) and \(t=d-w\). Consequently \(1-t=2-D_+\). Put \(G=(I+L_+)^{-1}\); its diagonal entry satisfies \(G_{ii}=1/D_+\). Both numerator cases therefore give the graph-specific barrier
\[
\boxed{h_i\ge\min\{0,\,2G_{ii}-1\}.}
\]
This is a sufficient lower bound for each fixed underlying unsigned graph; it is not claimed to be the sharp fixed-graph bound in the nonnegative regime.

**Universal bound.** An unsigned simple \(n\)-vertex graph has \(L_+\preceq L_{K_n}\), because each missing edge contributes a positive semidefinite rank-one Laplacian. Therefore
\[
G\succeq(I+L_{K_n})^{-1}
=\frac{I+\mathbf1\mathbf1^\top}{n+1},\qquad
G_{ii}\ge\frac2{n+1}.
\]
For \(n\ge3\), the graph-specific barrier implies
\[
h_i\ge\min\left\{0,\frac{3-n}{n+1}\right\}
=\frac{3-n}{n+1}.
\]

**Sharpness.** Give a chosen hub all \(n-1\) negative incident edges and choose any collection of positive edges between leaves. Setting hub centrality \(u=(3-n)/(n+1)\) and each leaf centrality \(v=(n-1)/(n+1)\) solves the signed centrality system: at the hub \(nu+(n-1)v=1\); at every leaf \(2v+u=1\), and positive leaf–leaf contributions vanish because those values agree. Uniqueness follows from positive definiteness. With innate opinion \(s=e_{\mathrm{hub}}\), the aggregate is exactly \(u\). In particular \(u=0\) for three vertices and \(u=-1/5\) for four.

**Small orders.** With one vertex, \(h=(1)\). With two connected vertices, a positive edge gives \(h=(1,1)\) and a negative edge gives \(h=(1/3,1/3)\). The universal bound excludes negativity for three vertices.

**Exhaustive first layer.** On four vertices there are exactly \(3^6=729\) labeled ternary edge assignments. The companion `verify_signed.py` iterates all assignments in the displayed fixed edge order, tests connectedness by graph search, and solves the four linear equations by exact rational Gauss–Jordan elimination. It checks the explicit three-condition structural criterion on **each** connected assignment, not just the assignments with negative centrality. Canonicalization takes the lexicographically least signed-edge string over all \(4!=24\) vertex permutations, giving the eight representatives and counts above. This is an exhaustive finite certificate for the four-vertex assertion, not a simulation or an inference about larger graphs. The analytical comparison argument independently proves the unrestricted-\(n\) bound.

## Verification

Run `python3 verify_signed.py` using only the Python standard library. Its exact-fraction elimination checks residual equations, the graph-specific comparison barrier, the all-order bound, and the complete connected four-vertex census. Expected results: connected signed graphs at sizes two, three and four number \(2,20,624\); negative-centrality counts are \(0,0,104\); the four-vertex negative family decomposes into orbit sizes \(4,4,12,12,12,12,24,24\). The checker tests closed-form hostile-hub equality witnesses for each \(3\le n\le30\); all larger orders are covered by the displayed proof, not by that finite range. No external data or software library is needed.

## Relationship to prior work

Zhou, Sun, Xu, Li and Zhang (arXiv:2407.10680v1, first public July 15, 2024), especially their definitions of the opposing Laplacian, formula for \(z\), and Section V-A, already establish the equilibrium formula and signed *structure centrality*, including the possibility of negative coordinates. These are **not** claimed as new. The present claim is the sharp all-order magnitude barrier, its extremal hostile-hub construction, the four-vertex onset, and the complete eight-class first negative layer. Shrinate and Tripathy (arXiv:2410.00456v1) consider a more general signed FJ-related influence measure, primarily using the absolute values of influence coefficients; their stated theorem does not supply this bound or census. Razaq and Altafini (CDC 2023, DOI 10.1109/CDC49753.2023.10383479) analyze stability of signed FJ dynamics, not this fixed-graph extremal centrality bound. Shi, Altafini and Baras survey opposing signed-network dynamics (SIAM Review 2019), without an identified competing statement. Razaq and Altafini (arXiv:2510.19123v1, 2025) additionally analyze signed-FJ wisdom of crowds using a *repelling* signed-degree Laplacian and a variance-concentration objective; this differs from the opposing, absolute-degree Laplacian and aggregate-influence extremum here. The possibility of a broader unlocated M-matrix or signed-resolvent theorem implying the comparison remains a priority risk.

## Limitations

The bounds rely on **unit** innate anchoring and **unit** absolute edge weights; weighted, directed, heterogeneous-stubbornness and time-varying networks are not covered. They concern the signed sum \(\sum_i z_i\), not robustness to strategic opinion changes, centered polarization, or individual expressed-opinion sign. The four-vertex characterization is finite and exact, but no structural characterization for all orders greater than four is asserted. The mathematical review is not independent publication verification.

## References

1. X. Zhou, H. Sun, W. Xu, W. Li and Z. Zhang, *Friedkin-Johnsen Model for Opinion Dynamics on Signed Graphs*, arXiv:2407.10680, first posted 2024-07-15, https://arxiv.org/html/2407.10680v2.
2. A. Shrinate and T. Tripathy, *Absolute centrality in a signed Friedkin-Johnsen based model: a graphical characterisation of influence*, arXiv:2410.00456, first posted 2024-10-01, https://arxiv.org/abs/2410.00456.
3. M. A. Razaq and C. Altafini, *Propagation of Stubborn Opinions on Signed Graphs*, Proceedings CDC 2023, DOI:10.1109/CDC49753.2023.10383479.
4. G. Shi, C. Altafini and J. S. Baras, *Dynamics over Signed Networks*, SIAM Review 61 (2019), 229–257, DOI:10.1137/17M1134172.
5. M. A. Razaq and C. Altafini, *Wisdom of Crowds Effects under Antagonistic Interactions and Correlated Opinions*, arXiv:2510.19123v1 (2025), https://arxiv.org/html/2510.19123v1.
