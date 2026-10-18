# Critical logarithmic intrinsic volumes of Cayley-tree graphical zonotopes

## Finding

For every integer \(n\ge3\), let \(T_n\) be a uniformly sampled labelled tree on \([n]\), and let
\[
 Z_T=\sum_{\{u,v\}\in E(T)}[e_u,e_v]
\]
be its standard graphical zonotope, equipped with the intrinsic Euclidean metric on the affine hyperplane \(\sum_i x_i=n-1\). Write \(V_j\) for the standard \(j\)-th intrinsic volume in its \((n-1)\)-dimensional affine hull. For any integers \(3\le r\le n\),
\[
\boxed{\displaystyle
 \mathbb E V_{n-r}(Z_{T_n})
 =\frac{n!\,n^{r-n}}{r!}
 \sum_{\substack{s_1+\cdots+s_r=n\\s_i\ge1}}
 \prod_{i=1}^r\frac{s_i^{s_i-1/2}}{s_i!}.}
\tag{1}
\]
For every **fixed** integer \(r\ge3\), as \(n\to\infty\),
\[
\boxed{\displaystyle
\mathbb E V_{n-r}(Z_{T_n})=
 \frac{n^{r-1/2}(\log n)^{r-1}}
 {(r-1)!(2\pi)^{(r-1)/2}}
 \left(1+O_r((\log n)^{-1})\right).}
\tag{2}
\]
In particular,
\[
\mathbb E V_{n-3}(Z_{T_n})\sim
 \frac{n^{5/2}(\log n)^2}{4\pi}.
\]
The preceding full-dimensional invariant \(V_{n-1}(Z_T)=\sqrt n\) is tree-independent; formula (2) shows a hierarchy of logarithmic enhancements at every fixed higher codimension.

There is also a geometric component-size law. Draw a pair \((T,F)\), where \(T\) is a labelled tree on \([n]\) and \(F\subseteq E(T)\) has exactly \(n-r\) edges, with probability proportional **over all such pairs** to
\[
 w(T,F)=\prod_{C\in\operatorname{Comp}([n],F)}\sqrt{|C|}.
\tag{3}
\]
Randomly order its \(r\) components and write their sizes as \(S_1,\ldots,S_r\). For each fixed \(r\ge3\), with probability tending to one exactly one component has size \(n-o(n)\). Conditional on that component's position, the logarithmic sizes of the other components converge jointly to independent uniforms:
\[
\boxed{\displaystyle
\left(\frac{\log S_i}{\log n}:i\ne J_n\right)
\ \Longrightarrow\ (U_1,\ldots,U_{r-1}),\qquad
 U_i\ \text{independent Uniform}(0,1),}
\tag{4}
\]
where \(J_n\) indexes the largest component (ties may be broken deterministically; they vanish asymptotically). The giant's logarithmic size divided by \(\log n\) converges to one. This is an **annealed, intrinsic-volume-weighted** law, not the law obtained by first sampling a tree uniformly and then cutting edges uniformly.

For a concrete codimension-two check, the expectation at \(n=5,r=3\) is
\[
\mathbb E V_2(Z_{T_5})=\frac{24}{5}+\frac{18\sqrt3}{5}.
\]
For a five-vertex star, \(V_2=6\sqrt3\), whereas for a five-vertex path, \(V_2=6+3\sqrt3\): the invariant distinguishes two combinatorially equivalent parallelotopes.

## Assumptions and scope

The trees are finite, simple, undirected and labelled, and all \(n^{n-2}\) trees receive equal probability before the tilting in (3). All coordinate segments have unit length in root-vector convention. No asymptotic statement is asserted uniformly when \(r\) grows with \(n\). The Euclidean normalization uses the ordinary scalar product inherited from \(\mathbb R^n\); it is not lattice-normalized volume. The intrinsic-volume convention is Steiner's formula
\[
 \operatorname{vol}_d(K+tB_d)=\sum_{j=0}^d \kappa_{d-j}t^{d-j}V_j(K),\quad d=n-1.
\]
In particular \(V_0(K)=1\), \(V_d(K)=\operatorname{vol}_d(K)\), and \(2V_{d-1}(K)\) is the boundary surface area.

## Proof

**1. Forest Gram determinants.** Fix \(T\) and \(F\subseteq E(T)\) containing \(k=n-r\) edges. Replace each unoriented segment by its incidence vector \(b_{uv}=e_u-e_v\); translation does not change intrinsic volumes. The Gram matrix \(B_F^{\mathsf T}B_F\) is block diagonal with blocks corresponding to the tree components. For a tree on \(s\) vertices, the product of its nonzero Laplacian eigenvalues is \(s\) by the matrix-tree theorem. These are exactly the eigenvalues of its edge-incidence Gram matrix. Thus, including singleton components,
\[
 \det(B_F^{\mathsf T}B_F)=\prod_{C\in\operatorname{Comp}(F)}|C|.
\tag{5}
\]
The standard zonotope intrinsic-volume expansion gives
\[
 V_k(Z_T)=\sum_{\substack{F\subseteq E(T)\\|F|=k}}
 \sqrt{\det(B_F^{\mathsf T}B_F)}
 =\sum_{\substack{F\subseteq E(T)\\|F|=n-r}}
 \prod_{C\in\operatorname{Comp}(F)}\sqrt{|C|}.
\tag{6}
\]
For \(k=0\) the empty Gram determinant equals one. Formula (6) is a geometric identity for every individual tree; no probability has yet entered.

**2. Cayley assembly.** Fix an ordered partition \((C_1,\ldots,C_r)\) of \([n]\) with positive sizes \((s_1,\ldots,s_r)\). Each induced component of \(F\) has \(s_i^{s_i-2}\) labelled trees, interpreted as one for a singleton. Joining the components into a spanning tree requires choosing a tree on the \(r\) contracted components and, for each contracted edge \(ij\), one of \(s_is_j\) actual crossing edges. The weighted Cayley identity gives
\[
 \sum_{R\text{ tree on }[r]}\prod_{i=1}^r s_i^{\deg_R(i)}
 =\left(\sum_i s_i\right)^{r-2}\prod_i s_i
 =n^{r-2}\prod_i s_i.
\tag{7}
\]
For \(r=1\) this is read by its one-vertex convention. Hence the total number of corresponding pairs \((T,F)\) for this ordered partition is \(n^{r-2}\prod_i s_i^{s_i-1}\). Their geometric weight (6) multiplies it by \(\prod_i\sqrt{s_i}\). Counting ordered vertex partitions contributes \(n!/\prod_i s_i!\), whereas each unoriented pair \((T,F)\) has \(r!\) component orders. Dividing by \(n^{n-2}\), Cayley's tree count, gives (1) exactly.

**3. Singular coefficient analysis.** Put \(c=(2\pi)^{-1/2}\) and
\[
 b_s=e^{-s}\frac{s^{s-1/2}}{s!},\qquad B(z)=\sum_{s\ge1}b_sz^s.
\]
Stirling's expansion gives \(b_s=c/s+O(s^{-2})\). Write
\[
 B(z)=cL(z)+R(z),\qquad L(z)=-\log(1-z),
\]
where the coefficients of \(R\) are \(O(s^{-2})\). For every fixed \(m\ge2\),
\[
 [z^n]L(z)^m
 =\frac{m(\log n)^{m-1}}n
 +O_m\!\left(\frac{(\log n)^{m-2}}n\right).
\tag{8}
\]
For example, (8) follows by differentiating \([z^n](1-z)^{-t}=\Gamma(n+t)/(\Gamma(t)\Gamma(n+1))\) \(m\) times at \(t=0\), uniformly for \(t\) in a small complex neighborhood of zero. Since the coefficients of \(R\) are absolutely summable and have an \(O(s^{-2})\) tail, convolution bounds show that every term containing \(R\) in \(B^r\) is \(O_r((\log n)^{r-2}/n)\). Therefore, for fixed \(r\ge2\),
\[
 [z^n]B(z)^r
 =\frac{r\,c^r(\log n)^{r-1}}n
 +O_r\!\left(\frac{(\log n)^{r-2}}n\right).
\tag{9}
\]
Rewrite (1) as
\[
\mathbb E V_{n-r}(Z_{T_n})
 =\frac{n!\,n^{r-n}e^n}{r!}[z^n]B(z)^r.
\tag{10}
\]
Applying Stirling to the prefactor and using (9) yields (2) with the claimed sharp constant. This argument is an infinite-dimensional asymptotic proof, not an extrapolation from finite computations.

**4. Critical component-size law.** The same assembly calculation shows that a uniformly ordered list of component sizes under (3) has the **exact** distribution
\[
 \Pr(S_1=s_1,\ldots,S_r=s_r)
 =\frac{\prod_i b_{s_i}}{[z^n]B(z)^r}
 \quad\text{for }s_i\ge1,\ \sum_i s_i=n.
\tag{11}
\]
Fix an index \(j\), and for each \(i\ne j\) fix \(0<a_i<b_i<1\). Restrict \(s_i\) to \(n^{a_i}<s_i\le n^{b_i}\) for all \(i\ne j\), and set \(s_j=n-\sum_{i\ne j}s_i\). In this region, \(s_j=n-o(n)\) uniformly and \(b_{s_j}\sim c/n\). Also
\[
 \sum_{n^{a}<s\le n^b}b_s\sim c(b-a)\log n.
\]
The numerator of (11) summed over the region is consequently
\[
 \frac{c^r(\log n)^{r-1}}n\prod_{i\ne j}(b_i-a_i)(1+o(1)).
\]
Divide by (9). The probability is \(r^{-1}\prod_{i\ne j}(b_i-a_i)+o(1)\), and distinct possible giant positions are asymptotically disjoint. Letting rectangle margins tend to zero and one shows that exactly one component takes proportion \(1-o(1)\), its index is asymptotically uniform, and the other logarithmic sizes converge jointly to independent uniforms. This proves (4). The method makes no assertion about the component law under unweighted uniform edge deletion.

## Verification

The accompanying `verify.py` is standalone Python 3 code using only the standard library. It independently enumerates all Prüfer-code labelled trees for orders \(2\) through \(6\) and all subsets of edges at every intrinsic-volume index. It constructs forest component sizes, computes Gram determinants by exact rational elimination, and compares the resulting squarefree-radical vectors with the independent ordered-composition formula (1) extended algebraically to all admissible indices. The first new index is additionally checked for all \(7^5=16807\) seven-vertex trees. In total, 294,278 forest-subset observations are checked, with every relevant small-order Gram determinant verified. Exact checks include \(\mathbb EV_2(Z_{T_5})=24/5+18\sqrt3/5\) and \(\mathbb EV_3(Z_{T_6})=80/9+5\sqrt6+10\sqrt2/9\). A successful run prints `VERIFY_OK`.

The checker validates finite identities only. Equations (2) and (4) are established analytically by the argument above; the finite computation is not represented as an exhaustive proof over arbitrary \(n\).

## Relationship to prior work

Graphical zonotopes and their normal fans are standard; Padrol, Pilaud and Poullot supply the canonical setting. Schneider proves expectation identities for zonotopes built from *independently identically distributed* random segment generators. A random tree's edge segments are globally constrained by connectivity and hence do not satisfy that hypothesis. Berestycki and Pitman establish general Gibbs-partition and Kolchin coefficient representations. Their general framework applies once the nontrivial geometric incidence weight \(s^{s-1/2}\) has been derived from the tree-forest decomposition; the underlying Gibbs representation is credited and is not claimed as new general partition theory. Hackl, Panholzer and Wagner analyze a vertex-uncover process in random labelled trees, not this intrinsic-volume weighting.

The closest earlier codimension-one surface-area calculation is outside the claimed new range: this finding concerns **all fixed codimensions at least two**, the exact higher-order geometric expectations, and the associated multiscale weighted component law. Ordinary Cayley enumeration, Gram determinant identities, and logarithmic combinatorial structures are also prior tools, not separately claimed discoveries.

## Limitations

The claims concern expectations over uniformly sampled labelled trees and the explicitly **annealed** measure (3); they do not prove concentration, central limit theorems, or a corresponding logarithmic law under ordinary uniform cutting. The asymptotics are only for fixed \(r\), and do not address a regime where \(r\) grows with \(n\). A search for equivalent results in geometry and random-tree literature found no formulation of the combined geometric theorem, but bibliographic exhaustiveness, including potentially equivalent Gibbs-assembly specializations, cannot be guaranteed.

## References

1. A. Padrol, V. Pilaud and G. Poullot, *Deformed Graphical Zonotopes*, first public version 2021-11-24, arXiv:2111.12422, DOI:10.1007/s00454-023-00586-x. Geometric setting and verified MSC2020 classification.
2. R. Schneider, *Random Zonotopes and Valuations*, first public version 2022-02-14, arXiv:2202.06774, DOI:10.1007/s00454-023-00514-z. Zonotope intrinsic-volume identities and independent-generator random models.
3. N. Berestycki and J. Pitman, *Gibbs Distributions for Random Partitions Generated by a Fragmentation Process*, arXiv:math/0512378. General Bell-polynomial and Kolchin representations; unweighted random tree forest models.
4. B. Hackl, A. Panholzer and S. Wagner, *The Uncover Process for Random Labeled Trees*, arXiv:2301.00664, DOI:10.1007/s44007-023-00060-3. Distinct labelled-tree forest dynamics.
5. A. Cayley, classical labelled-tree enumeration and its multivariate tree identity; and the matrix-tree theorem, used here as established combinatorial results.
