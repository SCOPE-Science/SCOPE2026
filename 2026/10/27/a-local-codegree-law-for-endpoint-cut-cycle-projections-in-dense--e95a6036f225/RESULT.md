# A local-codegree law for endpoint cut–cycle projections in dense regular complements

## Finding

Let \(H\) be **any** finite simple \(r\)-regular graph on \(N\) vertices, with integer \(r\ge1\) and \(N\ge4r\). Form its unweighted simple complement \(G=\overline H\), which is connected under these hypotheses. Fix any orientation of the edges of \(G\), let \(B\) be its vertex–edge incidence matrix, and set
\[
Q=B^{\mathsf T}(BB^{\mathsf T})^+B,\qquad P=I-Q.
\]
These are the Euclidean-orthogonal cut-space and cycle-space projections on the **real** edge-coordinate space. For every edge \(e=\{u,v\}\in E(G)\), define its deleted-graph codegree and two absolute column sums by
\[
c_e=|N_H(u)\cap N_H(v)|,\qquad
q_e=\sum_{f\in E(G)}|Q_{fe}|,\qquad
p_e=\sum_{f\in E(G)}|P_{fe}|.
\]
Then, uniformly over all such graphs and edges,
\[
\boxed{\left|q_e-\left(2+\frac{2r-2c_e-2}{N}\right)\right|\le\frac{32r^2}{N^2}}
\]
and
\[
\boxed{\left|p_e-\left(3+\frac{2r-2c_e-6}{N}\right)\right|\le\frac{44r^2}{N^2}.}
\]
Consequently, whenever \(N>44r^2\), **every edge attaining either projection's endpoint operator norm has the smallest deleted-graph codegree among all edges of \(G\)**. This conclusion includes ties between edges with the same minimum codegree; it does not determine which of those edges maximize.

Since \(Q\) and \(P\) are symmetric, their induced real \(\ell_1\) and \(\ell_\infty\) norms coincide, and equal respectively \(\max_e q_e\) and \(\max_e p_e\). If \(c_*\) is the minimum of \(c_e\), the preceding two estimates also give both operator norms to the displayed additive accuracy with \(c_e\) replaced by \(c_*\), without requiring \(N>44r^2\).

In particular, for any sequence with fixed \(r\) and fixed selected codegree \(c_e\), the coefficients of \(N^{-1}\) in the two estimates are genuine limits:
\[
N(q_e-2)\longrightarrow 2r-2c_e-2,\qquad
N(p_e-3)\longrightarrow 2r-2c_e-6.
\]
For the complement of a long cycle, pairs at deleted-cycle distance two have codegree one and pairs at distance at least three have codegree zero. Their projection columns therefore separate by \(2/N+O(N^{-2})\). More concretely, on \(\overline{C_N}\) for \(N\ge177\), no distance-two pair can maximize either projection norm. For the complement of the binary hypercube \(Q_m\), the criterion excludes Hamming-distance-two edges as maximizers in **both** projections for every \(m\ge13\).

## Assumptions and scope

All graphs are finite, simple, unweighted, and undirected. The graph \(H\) is regular but need not be connected, transitive, or strongly regular. Edges of \(G\) are precisely nonedges of \(H\). The condition \(N\ge4r\) makes \(G\) connected: any disconnected component would have at least \(N-r\) vertices, which is incompatible with two or more components when \(N>2r\).

All operator norms concern the fixed canonical Euclidean-orthogonal projections, acting on real edge coordinates with their induced \(\ell_1\) or \(\ell_\infty\) norm. The theorem makes no claim about arbitrary nonorthogonal projections or positive conductance weightings.

## Proof

**1. An exactly controlled Laplacian inverse.** Write \(L_H\) and \(L_G\) for the combinatorial graph Laplacians. Since the Laplacian of the complete graph is \(NI-J\), on the zero-sum vertex subspace,
\[
L_G=NI-L_H.
\]
For a fixed \(G\)-edge \(e=uv\), use the signed source \(s=\mathbf e_u-\mathbf e_v\), and let \(h=L_G^+s\), which is a zero-sum electrical potential. Because \(\|L_H\|_{1\to1}=2r\) and \(2r/N\le1/2\), the absolutely convergent Neumann expansion gives
\[
h=\frac{s}{N}+\frac{L_Hs}{N^2}+R,\qquad
\|R\|_1\le\frac{8r^2}{N^3(1-2r/N)}\le\frac{16r^2}{N^3}.
\]
Here \(\|s\|_1=2\), and the constants follow by summing the geometric tail beginning at the second power of \(L_H/N\).

**2. The exact first-order potential profile.** Put \(A=r-c_e\) and \(h^{(0)}=s/N+L_Hs/N^2\). Since \(uv\notin E(H)\),
\[
h^{(0)}(u)=\frac1N+\frac r{N^2},\qquad
h^{(0)}(v)=-\frac1N-\frac r{N^2}.
\]
For \(w\notin\{u,v\}\), set
\[
\delta_w=\mathbf1_{\{wv\in E(H)\}}-\mathbf1_{\{wu\in E(H)\}}.
\]
Then \(h^{(0)}(w)=\delta_w/N^2\). Exactly \(A\) of the \(\delta_w\)'s equal \(+1\), exactly \(A\) equal \(-1\), and the other \(N-2-2A\) equal zero. In particular \(\sum_w\delta_w=0\). Notice that the signs are established by these exact values, not inferred from a finite experiment.

Let \(\operatorname{TV}_F(z)=\sum_{\{x,y\}\in E(F)}|z(x)-z(y)|\) for any graph \(F\). Summing all complete-graph pairs gives
\[
\operatorname{TV}_{K_N}(h^{(0)})
=\frac{2(N-1)}N+\frac{2r(N-1)+2A(N-2-A)}{N^2}.
\]
The first two terms come from pairs incident to \(u\) or \(v\), and the remaining term comes from the three possible values of \(\delta\) on other vertices.

Define the nonnegative integer
\[
T=\sum_{\substack{\{w,z\}\in E(H)\\w,z\notin\{u,v\}}}|\delta_w-\delta_z|.
\]
The deleted edges incident to \(u\) and to \(v\) contribute, together, \(2r/N+2(r^2+A)/N^2\). Consequently subtraction of the deleted edges yields the **exact finite identity**
\[
\operatorname{TV}_G(h^{(0)})
=2+\frac{2A-2}{N}
-\frac{2r(r+1)+2A(A+3)+T}{N^2}.
\]
At most \(2A\) vertices have nonzero \(\delta\), each has at most \(r\) incident deleted edges, and \(|\delta_w-\delta_z|\le2\). Thus \(0\le T\le4Ar\le4r^2\). Since \(0\le A\le r\) and \(r\ge1\),
\[
0\le2r(r+1)+2A(A+3)+T\le8r^2+8r\le16r^2.
\]

**3. Control of every absolute-current column.** The column of \(Q\) indexed by \(e\) is the oriented gradient of \(h\), hence \(q_e=\operatorname{TV}_G(h)\). For every vertex vector \(z\),
\[
\operatorname{TV}_G(z)\le(N-1-r)\|z\|_1\le N\|z\|_1.
\]
The triangle inequality and Step 1 therefore give
\[
|\operatorname{TV}_G(h)-\operatorname{TV}_G(h^{(0)})|
\le N\|R\|_1\le\frac{16r^2}{N^2}.
\]
Combining this with the exact identity and bound from Step 2 proves the displayed \(q_e\) estimate, with constant \(32\).

The diagonal \(Q_{ee}=h(u)-h(v)\) is the effective resistance of the edge. Its approximation satisfies
\[
\left|Q_{ee}-\left(\frac2N+\frac{2r}{N^2}\right)\right|
\le\|R\|_1\le\frac{16r^2}{N^3}.
\]
Because \(Q\) is an orthogonal projection, \(0\le Q_{ee}\le1\). Its complementary projection thus obeys the exact column identity
\[
p_e=q_e+1-2Q_{ee}.
\]
Substituting the two estimates gives
\[
\left|p_e-\left(3+\frac{2A-6}{N}\right)\right|
\le\frac{32r^2}{N^2}+\frac{4r}{N^2}+\frac{32r^2}{N^3}
\le\frac{44r^2}{N^2},
\]
where the last step uses \(r\ge1\) and \(N\ge4r\).

**4. Rigorous selection by minimum codegree.** Let \(e\) have larger codegree than some \(e'\), so \(c_e\ge c_{e'}+1\). The main terms differ by at least \(2/N\), in favor of \(e'\). The two \(q\)-errors total at most \(64r^2/N^2\), and the two \(p\)-errors at most \(88r^2/N^2\). For \(N>44r^2\), both totals are strictly below \(2/N\). Hence \(q_{e'}>q_e\) and \(p_{e'}>p_e\). Neither projection's maximum can occur at \(e\). Symmetry of the real projections gives equality of the \(\ell_1\)- and \(\ell_\infty\)-operator norms.

For a cycle \(H=C_N\), the deleted-graph neighborhoods of a distance-two pair intersect in one vertex once \(N\ge6\), whereas distance-at-least-three pairs have no common neighbor. Set \(r=2\) and use \(N>176\). For \(H=Q_m\), \(r=m\), \(N=2^m\), and common-neighbor counts are two at Hamming distance two and zero at all distances at least three. The inequality \(2^m>44m^2\) holds for \(m\ge13\), proving the two stated applications.

## Verification

Run `python3 CHECKER.py` with Python 3, NetworkX 3.6.1 and SymPy 1.14.0. The standalone exact-rational checker constructs the complements of cycles, sample regular graphs, and a four-dimensional cube, independently solves their grounded graph Laplacians, and checks **all** cut/cycle columns against the theorem's constants. It separately verifies the exact truncated-potential total-variation identity and the finite bound on \(T\). The recorded run returned:

`DENSE_COMPLEMENT_EXACT_OK graphs=11 columns=606 examples=[(8, 2, 20), (10, 2, 35), (12, 2, 54), (14, 2, 77), (12, 3, 48), (14, 3, 70), (16, 4, 88), (12, 3, 48), (16, 4, 88), (8, 1, 24), (12, 2, 54)]`

These are finite consistency checks; the unrestricted quantifiers are established analytically by the four proof steps above.

## Relationship to prior work

Schild, Rao and Srivastava (arXiv:1708.01632, 2017) formulate absolute electrical-current lengths and prove a universal logarithmic-squared **average** bound. Dilworth, Kutzarova and Ostrovskii (arXiv:2305.12582, 2023) develop cycle/cut projection geometry and explicit families, concentrating their calculations on Hamming graphs and tori. Gurel-Gurevich, Nachmias and Sachdeva (arXiv:2605.24130, 2026) prove a universal logarithmic localization bound. Their inspected general theorems do not supply the present **edgewise** first-order law for complements of arbitrary regular deleted graphs, its codegree coefficient, or its quantitative extremizer selection. This is a statement-level distinction rather than a claim that a literature search proves novelty.

## Limitations

The constants \(32\) and \(44\), and the sufficient threshold \(N>44r^2\), are not claimed optimal. The theorem does not rank edges sharing the minimum codegree or provide a closed exact norm value for each individual graph. It is an additive second-order estimate, not an exact operator-norm classification. No result is claimed for weighted graphs, irregular deleted graphs, intermediate \(\ell_p\) norms, or minimum norms among nonorthogonal projections. As with all literature comparisons, equivalent specialized results that are not indexed or accessible remain a residual risk.

## References

1. A. Schild, S. Rao, N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632 (first posted 4 August 2017), especially §§1–2, https://arxiv.org/abs/1708.01632.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first posted 21 May 2023), especially §§1, 2.1, 2.6–2.7, https://arxiv.org/abs/2305.12582.
3. O. Gurel-Gurevich, A. Nachmias, S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130 (first posted 22 May 2026), especially §§1–2, https://arxiv.org/abs/2605.24130.
