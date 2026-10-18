# A cubic directional-width law detects degree assortativity in tree graphical zonotopes

## Finding

**Theorem (complete cubic width law).** Let \(G=(V,E)\) be a finite, connected, simple, triangle-free graph, with \(n=|V|\ge4\) and \(m=|E|\). Embed its standard graphical zonotope as \(Z_G=\sum_{\{i,j\}\in E}[e_i,e_j]\), considered intrinsically in the Euclidean affine hyperplane parallel to \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\). For a uniform unit vector \(U\in H\), let \(W_G=\max_{z\in Z_G}\langle U,z\rangle-\min_{z\in Z_G}\langle U,z\rangle\).

Define the graph invariants
\[
L=\sum_{v\in V}\binom{d_v}{2},\qquad
S=\sum_{v\in V}\binom{d_v}{3},\qquad
T=\sum_{\{v,w\}\in E}(d_v-1)(d_w-1).
\]
Here \(L\) counts adjacent pairs of edges, \(S\) counts three-edge stars, and \(T\) counts length-three simple paths by their middle edge (triangle-freeness ensures the latter identification). Put
\[
R_n=\frac{2^{3/2}\Gamma((n+2)/2)}{\Gamma((n-1)/2)},\quad
c_M=\frac8{\pi^{3/2}},\quad
c_W=\frac8{\pi^{3/2}}\left(\frac{\sqrt3}2+\frac\pi{12}\right),
\]
\[
c_P=\frac8{\pi^{3/2}}\left(\frac1{\sqrt2}+\arcsin\frac1{\sqrt3}-\frac14\arcsin\frac13\right),\qquad
c_S=\frac8{\pi^{3/2}}\left(\frac1{\sqrt2}+\frac94\arcsin\frac13\right).
\]
Then the exact third spherical directional-width moment is
\[
\boxed{\mathbb E[W_G^3]=\frac1{R_n}\left[\frac{8m}{\sqrt\pi}+\frac6{\sqrt\pi}\left(4\binom m2+L\right)+6\left(c_M\binom m3+(c_W-c_M)(m-2)L+(c_S-3c_W+2c_M)S+(c_P-2c_W+c_M)T\right)\right].}
\]

**Strict cubic discrimination for trees.** If two trees on the same \(n\) vertices have the same degree multiset, their first and second spherical width moments coincide, whereas
\[
\boxed{\mathbb E[W_{G_2}^3]-\mathbb E[W_{G_1}^3]=\frac{6\beta}{R_n}(T_2-T_1),\qquad \beta=c_P-2c_W+c_M<0.}
\]
Thus their third moments strictly order the number of length-three paths in reverse. Equivalently, within a degree class they are strictly decreasing with the second Zagreb index \(\sum_{\{v,w\}\in E}d_vd_w\). This is a degree-assortativity discriminator that cannot be recovered from the first two width moments.

For example, on vertices \(0,\ldots,5\), compare the edge sets \(\{01,12,23,04,05\}\) and \(\{01,13,02,24,05\}\). Both have degree multiset \((3,2,2,1,1,1)\), but respectively \(T=3\) and \(T=4\). Their exact third moments differ by \(6\beta/R_6\), numerically about \(-0.0121693420\).

## Assumptions and scope

All graphs are finite, connected, undirected, simple, and triangle-free. The Euclidean metric is the one induced by standard unit coordinate vectors; no arbitrary affine transformation or rescaling is implied. Unit directions are sampled using rotation-invariant spherical probability measure in the \((n-1)\)-dimensional linear span. A graph with cycles is allowed in the first theorem, but the strict fixed-degree comparison is asserted for trees. Connectedness guarantees that the zonotope has intrinsic dimension \(n-1\). The result does not classify possible values of \(T\) inside a prescribed tree degree sequence.

## Proof

**1. Gaussian lift.** Let \(X_i\) be independent standard Gaussian variables, project \(X=(X_1,\ldots,X_n)\) orthogonally onto \(H\), and write its projection as \(RU\). The direction \(U\) is uniform on the unit sphere of \(H\), independent of \(R\), and \(R\) has the \(\chi_{n-1}\) distribution. A Minkowski sum of segments has additive widths. Thus
\[
RW_G(U)=\sum_{\{i,j\}\in E}|X_i-X_j|,
\quad
\mathbb E[R^3]=R_n.
\]
Consequently the cubic moment is the cubic absolute-Gaussian edge-difference moment divided by \(R_n\). This step fixes the normalization and is valid for all connected graphs.

**2. Terms with repeated edges.** Write \(Y_e=|X_i-X_j|\). Every difference has variance two, whence \(\mathbb E[Y_e^3]=8/\sqrt\pi\). If \(e\ne f\) share a vertex, their signed Gaussian correlation has magnitude \(1/2\), and conditional Gaussian integration gives \(\mathbb E[Y_e^2Y_f]=5/\sqrt\pi\). If they are disjoint, independence gives \(4/\sqrt\pi\). Expanding the cube and using the \(L\) incident pairs of edges yields the first two terms in the displayed formula:
\[
\mathbb E\sum_eY_e^3=8m/\sqrt\pi,\qquad
3\sum_{e\ne f}\mathbb E[Y_e^2Y_f]=6(4\binom m2+L)/\sqrt\pi.
\]

**3. Three distinct edges and the known Gaussian absolute-moment identity.** For a nonsingular centered trivariate normal vector \((Z_1,Z_2,Z_3)\) with unit variances and correlations \(r_{ij}\), set \(r_{ij\mid k}=(r_{ij}-r_{ik}r_{jk})/\sqrt{(1-r_{ik}^2)(1-r_{jk}^2)}\). Its classical third absolute-product moment is
\[
\mathbb E|Z_1Z_2Z_3|=\left(\frac2\pi\right)^{3/2}\left[\sqrt{\det(r_{ij})}+\sum_{\substack{i<j\\\{i,j,k\}=\{1,2,3\}}}(r_{ij}+r_{ik}r_{jk})\arcsin(r_{ij\mid k})\right].
\]
This identity is prior Gaussian-moment theory, **not** claimed as a new result; see Nabeya and Song–Lee–Kim–Park in the references. In edge differences, each marginal standard deviation is \(\sqrt2\). Triangle-freeness leaves exactly four possible three-edge configurations: a matching (all signed correlations zero), a wedge plus a disjoint edge (one correlation of magnitude \(1/2\)), a length-three path (two correlations of magnitude \(1/2\), the remaining one zero), and a three-star (three correlations with compatible signs and magnitudes \(1/2\)). Substituting these matrices, and accounting for the marginal scale factor \(2^{3/2}\), gives respectively \(c_M,c_W,c_P,c_S\). For a path, the standardized determinant equals \(1/2\), and the three weighted partial-correlation terms reduce to \(\arcsin(1/\sqrt3)-\arcsin(1/3)/4\). For a star, the standardized determinant equals \(1/2\) and all partial correlations are \(1/3\).

**4. Exact motif partition.** Among unordered triples of distinct edges, the number of stars is \(S\), the number of paths is \(T\), and the number of wedges plus an isolated edge is \((m-2)L-3S-2T\): count an incident edge pair, choose one of the remaining \(m-2\) edges, and subtract the three pairs in a star and the two pairs in a path. Therefore the number of three-edge matchings is \(\binom m3-(m-2)L+2S+T\). Multiplying the sum of the four configuration expectations by six (the permutations of three distinct factors), and collecting terms, gives the boxed cubic formula. The argument also handles any configuration count equal to zero.

**5. Strict negative path coefficient.** Algebraically, \(\beta=8B/\pi^{3/2}\), where
\[
B=1+\frac1{\sqrt2}-\sqrt3-\frac\pi6+\arctan\frac1{\sqrt2}-\frac14\arctan\frac1{2\sqrt2}.
\]
Use the alternating rational Taylor bounds for arctangent, the exact Machin identity \(\pi/4=4\arctan(1/5)-\arctan(1/239)\), and rational lower/upper bounds on the square roots. The standalone checker gives exact rational endpoints with the strictly negative certified upper bound \(B<-0.018\). Since the cubic coefficient is \(6\beta/R_n\), the claimed strict reverse order follows.

**6. Why degree-equivalent trees agree at first and second moments.** For one edge \(\mathbb E[Y_e]=2/\sqrt\pi\); for incident pairs \(\mathbb E[Y_eY_f]=2\sqrt3/\pi+1/3\); for disjoint pairs \(\mathbb E[Y_eY_f]=4/\pi\). Since \(\mathbb E[R]=\sqrt2\Gamma(n/2)/\Gamma((n-1)/2)\) and \(\mathbb E[R^2]=n-1\),
\[
\mathbb E W_G=\frac{\sqrt2\,m\Gamma((n-1)/2)}{\sqrt\pi\Gamma(n/2)},
\]
\[
\mathbb E W_G^2=\frac{2m+2L(2\sqrt3/\pi+1/3)+2(\binom m2-L)(4/\pi)}{n-1}.
\]
For trees with a fixed degree multiset, \(n\), \(m=n-1\), \(L\), and \(S\) are fixed. All terms in the third-moment formula except the \(T\) term cancel between such trees. Finally, \(T=\sum_{\{v,w\}\in E}d_vd_w-\sum_vd_v^2+m\) by direct edgewise expansion; the second term is fixed in a degree class. This proves the inverse second-Zagreb-index interpretation.

## Verification

`checker.py` is a standalone Python 3 script requiring only the standard library. Execute `python3 checker.py`. It checks the four-class motif count by direct enumeration for paths and stars through nine edges and for the two degree-equivalent six-vertex trees, independently integrates the star and path Gaussian products, verifies the moment contrast, and computes a **rigorous exact-rational** upper bound proving the crucial sign \(B<0\). The Gaussian integrals are finite numerical corroboration; the all-dimensional theorem follows from the analytical argument and established absolute-moment identity. The exact-rational sign certificate uses no floating-point comparisons for its conclusion.

## Relationship to prior work

Padrol, Pilaud, and Poullot (arXiv:2111.12422, first publicly submitted 2021-11-24) define and study the same standard graphical zonotope, but the full accessible paper develops deformation cones, not the cubic spherical width moment. A published finding entitled *Sharp width-variance extremizers among tree graphical zonotopes* covers the **second** directional-width moment/variance and its tree-degree consequences, not the third moment, the length-three-path coefficient or the fixed-degree assortativity discrimination. The Gaussian absolute-product identity used in the proof is classical (Nabeya, with later formulas by Song and collaborators); the novelty assessed here is the geometric graph-motif specialization and strict cubic separation, not a new Gaussian identity. General-width and Gaussian-total-variation formulations were included in the search comparisons.

## Limitations

The stated closed graph-motif formula assumes triangle-free graphs. For graphs with triangles, triples of edges forming a cycle furnish an additional configuration requiring separate treatment. The proof concerns the third moment of the **directional width** under the intrinsic rotation-invariant measure, not the third moment of its vertex radii or the volume of the zonotope. The formula does not determine the full distribution of widths. Numerical integrations do not establish an infinite-dimensional claim. Residual bibliographic risk remains because a relevant indexed second-moment research record was available only as its public abstract, and earlier equivalent formulas under graph Gaussian total-variation terminology may exist; no independent audit has been performed.

## References

1. Arnau Padrol, Vincent Pilaud, Germain Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, version 1 submitted 2021-11-24; *Discrete & Computational Geometry* 73 (2025), 447–465.
2. Seiji Nabeya, *Absolute moments in 3-dimensional normal distribution*, *Annals of the Institute of Statistical Mathematics* 4 (1952), 15–30, DOI: 10.1007/BF02949786.
3. Iickho Song, Seungwon Lee, Y. Kim, S. Park, *Explicit formulae and implication of the expected values of some nonlinear statistics of tri-variate Gaussian variables*, *Journal of the Korean Statistical Society* 49 (2020), 117–138, DOI: 10.1007/s42952-019-00009-9.
4. *Sharp width-variance extremizers among tree graphical zonotopes*, publicly indexed 2026-10-11, reference ID `482983ab9269` (second-moment comparison; full paper not available for inspection in this review).
