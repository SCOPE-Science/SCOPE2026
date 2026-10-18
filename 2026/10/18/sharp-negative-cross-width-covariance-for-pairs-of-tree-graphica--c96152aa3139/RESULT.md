# Sharp negative cross-width covariance for pairs of tree graphical zonotopes

## Finding

Fix an integer \(n\ge4\), and let \(T,S\) be two (not necessarily isomorphic) unweighted spanning trees on the **same labelled vertex set** \([n]\). Work in the intrinsic Euclidean hyperplane \(H=\{x\in\mathbb R^n:\sum_i x_i=0\}\), and define the centered graphical zonotope
\[
 Z_T=\sum_{\{i,j\}\in E(T)}[-(e_i-e_j)/2,(e_i-e_j)/2].
\]
Its width in a unit direction \(U\in H\) is \(W_T(U)=\sum_{ij\in E(T)}|U_i-U_j|\). The same uniformly distributed spherical direction \(U\) is used for both widths.

Set \(d=n-1\), \(r_d=\sqrt2\,\Gamma((d+1)/2)/\Gamma(d/2)\), and
\[
\delta=\frac13+\frac{2\sqrt3-4}{\pi}>0,\qquad
\lambda=\frac43+\frac{4-4\sqrt3}{\pi}>0.
\]
For every pair of trees, the exact cross-width covariance is
\[
\boxed{\operatorname{Cov}(W_T,W_S)=\frac4\pi\left(d-\frac{d^2}{r_d^2}\right)
+\frac{\delta}{d}\sum_{v=1}^n\deg_T(v)\deg_S(v)
+\frac{\lambda}{d}|E(T)\cap E(S)|.}\tag{1}
\]
Its **sharp minimum over all ordered pairs of spanning trees** is
\[
\boxed{M_n=\frac4\pi\left(d-\frac{d^2}{r_d^2}\right)
+\delta\frac{3n-4}{n-1}.}\tag{2}
\]
Equality holds **if and only if** (i) the sets of vertices having degree at least two in \(T\) and \(S\) are disjoint, and (ii) the two trees have no common edges. Such pairs exist for every \(n\ge4\).

Most strikingly, this sharp minimum has a strictly negative nonzero limit:
\[
\boxed{\lim_{n\to\infty}M_n=3\delta-\frac2\pi
=1+\frac{6\sqrt3-14}{\pi}=-0.1483650340\ldots<0.}\tag{3}
\]
Already for \(n=4\), the exact minimum is
\[
 M_4=\frac{4+16\sqrt3}{3\pi}-\frac{65}{18}=-0.2462771539\ldots<0.
\]
Thus two combinatorially cubical, equal-volume graphical zonotopes can have strictly *negatively* correlated widths under a shared random Euclidean direction, and the strongest possible anticorrelation in this covariance sense is classified exactly.

## Assumptions and scope

Every tree is finite, simple, undirected, and spanning on the same set of labels; their embeddings use the same standard coordinate vectors. Tree pairs are allowed to coincide, but negative minimum pairs must be distinct. Widths use the same normalized rotation-invariant measure on the unit sphere in \(H\); they are **not** evaluated in independent directions. The standard root generators have norm \(\sqrt2\). Centering the segments is a translation and does not alter widths. The minimum theorem is for \(n\ge4\); the exact covariance identity applies to any connected simple graph pair on \([n]\) with the corresponding edge counts (see proof).

## Proof

**1. Cross-edge Gaussian angular kernel.** Let \(g\) be an isotropic standard Gaussian vector in \(H\) and write \(g=RU\), where \(U\) is spherical uniform, \(R\) is independent of \(U\), \(\mathbb E R=r_d\), and \(\mathbb E R^2=d\). Put \(X_T=\sum_{ij\in E(T)}|g_i-g_j|=RW_T\). Each edge difference is centered normal with variance two, so \(\mathbb E|g_i-g_j|=2/\sqrt\pi\). Consequently,
\[
 \mathbb E W_T=\frac{2|E(T)|}{\sqrt\pi\,r_d}.
\]
For distinct edges the Gaussian edge differences have correlation zero when disjoint and correlation \(\pm1/2\) when they share a vertex. The standard bivariate identity
\[
\mathbb E|AB|=\frac2\pi\bigl(\sqrt{1-\rho^2}+\rho\arcsin\rho\bigr)
\]
for standard Gaussian \(A,B\) of correlation \(\rho\) gives the following expectations for the absolute *variance-two* edge differences: \(4/\pi\) for disjoint edges, \(2\sqrt3/\pi+1/3=4/\pi+\delta\) for distinct incident edges, and \(2\) for an identical edge. No independence assertion is made for incident edges.

**2. Graph-pair bookkeeping.** Write \(m_T=|E(T)|\), \(m_S=|E(S)|\), \(c=|E(T)\cap E(S)|\), and \(s=\sum_v\deg_T(v)\deg_S(v)\). Among the \(m_Tm_S\) ordered cross-edge pairs, there are \(c\) identical pairs, \(s-2c\) pairs of distinct edges sharing one endpoint, and all remaining pairs are disjoint. Thus
\[
 \mathbb E[X_TX_S]=\frac4\pi m_Tm_S+\delta s+\left(2-\frac4\pi-2\delta\right)c.
\]
The last parenthesis is precisely \(\lambda\). Radial independence yields \(\mathbb E[W_TW_S]=\mathbb E[X_TX_S]/d\), whereas \(\mathbb E W_T\,\mathbb E W_S=4m_Tm_S/(\pi r_d^2)\). For trees \(m_T=m_S=d\), proving (1). Both \(\delta>0\) and \(\lambda>0\) follow from \(\pi>3\), \(\sqrt3<7/4\), and their displayed definitions.

**3. Exact pair minimization and equality.** For each vertex set \(a_v=\deg_T(v)-1\ge0\) and \(b_v=\deg_S(v)-1\ge0\). The tree degree-sum identity gives \(\sum_v a_v=\sum_v b_v=n-2\), and therefore
\[
 s=\sum_v(1+a_v)(1+b_v)=3n-4+\sum_va_vb_v\ge3n-4.
\]
Equality holds if and only if no vertex has positive excess degree in both trees. Since \(c\ge0\), and both coefficients in (1) are strictly positive, equality in the claimed global lower bound holds exactly when \(s=3n-4\) and \(c=0\). This proves the necessity and sufficiency of conditions (i) and (ii), not merely their sufficiency.

For existence at \(n=4\), take
\[
 E(T)=\{01,02,13\},\qquad E(S)=\{03,12,23\}.
\]
Each graph is a tree, their edge sets are disjoint, and their nonleaf sets are respectively \(\{0,1\}\) and \(\{2,3\}\). For each new vertex \(k\ge4\), attach it to vertex \(0\) in \(T\) and vertex \(2\) in \(S\). These operations retain two trees, edge disjointness, and disjoint nonleaf sets at every order. Hence the lower bound (2) is attained for every \(n\ge4\).

**4. Sharp asymptotic negative covariance.** Stirling's expansion with its standard remainder gives
\[
 r_d^2=d-\frac12+\frac1{8d}+O(d^{-2}),\qquad
 \frac{d^2}{r_d^2}=d+\frac12+O(d^{-1}).
\]
Substitution into (2) proves (3), since \((3n-4)/(n-1)\to3\). Strict negativity follows from \(14-6\sqrt3>\pi\), which follows for instance from \(\sqrt3<7/4\) and \(\pi<22/7\). Substituting \(r_3^2=8/\pi\) yields the stated exact four-vertex value; \(\sqrt3<7/4\) and \(\pi>3\) also show it is strictly negative. The limiting statement is about covariance, not about correlation coefficients or an asserted central limit theorem.

## Verification

The accompanying pure-Python program `verify.py` checks all \(1,695,497\) ordered pairs of labeled trees at orders four through six using Prüfer codes, verifying the lower bound and the precise equality conditions for every pair. The numbers of minimizing ordered pairs at these orders are respectively \(12\), \(480\), and \(28,080\). It separately computes direct segment-sum vertex supports in \(160\) cases and compares the resulting width with the edge-difference formula. Fixed-seed Monte Carlo samples of \(150,000\) spherical directions each at dimensions three and eleven corroborate the negative covariance and gamma normalization. These finite checks are diagnostics; the preceding proof applies to every order.

To reproduce: run `python3 verify.py` using Python 3 standard library. The expected last line is `VERIFY_OK`.

## Relationship to prior work

The graphical-zonotope construction, its braid-hyperplane geometry, and the fact that all tree graphical zonotopes have cubical face lattices are established; see Grujić and Padrol–Pilaud–Poullot. A previously published note *Sharp width-variance extremizers among tree graphical zonotopes* already gives the bivariate Gaussian absolute-edge kernel and the individual-tree width-variance extremizers. **Neither that kernel nor single-tree extremality is asserted to be new here.** The new statement is the universal *two-tree coupling* optimum (2), the exact characterization of all minimizers, and its strictly negative limit under one shared direction. The prior single-tree result does not state the coupled edge-disjoint/nonleaf-disjoint equality classification; extending the pair kernel and solving this coupled combinatorial problem are the steps needed here.

## Limitations

The optimum concerns standard unweighted embeddings of two trees on the same labels and covariance, not independently sampled directions or Pearson correlation. Different relative label embeddings of two isomorphic trees can have different covariance; the theorem deliberately optimizes over label-compatible pairs. The cross-moment identity itself uses standard bivariate Gaussian mathematics, and an equivalent coupled-tree minimization may have been formulated in prior work under graph-variation or zonotope mixed-moment terminology. No independent audit has been performed; the standalone checker does not prove the theorem beyond its finite test range.

## References

1. A. Padrol, V. Pilaud and G. Poullot, *Deformed Graphical Zonotopes*, first publicly posted 24 November 2021, arXiv:2111.12422, https://arxiv.org/abs/2111.12422; *Discrete & Computational Geometry* (open access), https://doi.org/10.1007/s00454-023-00586-x. Graphical-zonotope construction, deformation theory; classification begins with MSC2020 52B11.
2. V. Grujić, *Counting Faces of Graphical Zonotopes*, first publicly posted 23 April 2016, arXiv:1604.06931, https://arxiv.org/abs/1604.06931. Sections 1–2 and Example 5.1 establish combinatorial information about tree zonotopes.
3. *Sharp width-variance extremizers among tree graphical zonotopes*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-width-variance-extremizers-among-tree-graphical-zonotopes--482983ab9269/RESULT.md. Exact previously published individual-graph width moments and the edge-pair angular kernel.
