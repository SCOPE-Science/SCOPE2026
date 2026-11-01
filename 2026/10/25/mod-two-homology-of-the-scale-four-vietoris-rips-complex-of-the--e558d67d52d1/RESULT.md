# Complete mod-two homology of the scale-four Vietoris–Rips complex of the six-by-six torus grid

## Finding

Let \(T_6=(\mathbb Z/6\mathbb Z)^2\) with the discrete shortest-path Manhattan metric
\[
d((i,j),(u,v))=\delta_6(i,u)+\delta_6(j,v),\qquad
\delta_6(a,b)=\min\{|a-b|,6-|a-b|\}.
\]
For the **inclusive** scale-four Vietoris–Rips complex \(K=\operatorname{VR}_{\le4}(T_6)\), the **complete** reduced homology over \(\mathbb F_2\) is
\[
\widetilde H_q(K;\mathbb F_2)\cong
\begin{cases}
\mathbb F_2^{23},&q=5,\\
\mathbb F_2^{2},&q=8,\\
0,&\text{all other }q.
\end{cases}
\]
In particular, \(K\) is connected. **The ranks 23 in degree five and 2 in degree eight, and the absence of lower-degree features through degree eight, were already computed and published in Adams–Adetowubo–Barriga-Acosta–Feng–Sterling (2025), Table 1.** That table expressly stops the calculation for this parameter pair at degree eight. The additional result established here is the verified vanishing of homology in every higher degree, namely degrees nine through twelve, together with a complete independent-set enumeration and the exact boundary ranks in every degree. The already published low-degree ranks are corroborated, not claimed as new.

## Assumptions and scope

Vertices are the 36 elements of \(T_6\), with coordinate representatives in \(\{0,\dots,5\}\). A subset is a face if and only if **every** pair of its distinct vertices has distance at most four. The metric is the graph-distance \(\ell^1\) metric on the discrete torus, not the Euclidean or continuous-torus geodesic metric. Coefficients throughout are \(\mathbb F_2\). The result is for this one natural parameter pair only, not a statement about integral homology or homotopy.

## Proof by exhaustive finite chain reduction

Define the forbidden-pair graph \(H\) on the 36 vertices by placing an edge precisely when the metric distance exceeds four. The forbidden differences modulo six are \((\pm3,\pm2)\), \((\pm2,\pm3)\), and \((3,3)\), interpreted modulo six without duplicate signs. Consequently every vertex has five forbidden neighbors and \(H\) has 90 edges. A set is a simplex of \(K\) exactly when it is an independent set of \(H\).

A complete recursive enumeration selects the least available vertex, includes it and deletes its forbidden neighbors, or excludes it, with disjoint branches covering every independent subset. The nonempty independent sets, grouped by simplex dimension \(0\) through \(12\), have counts
\[
(f_0,\ldots,f_{12})=(36,540,4440,22212,71244,151140,216360,
210816,138688,59616,15408,1908,36).
\]
There are 892,444 nonempty faces. In particular, the complex is twelve-dimensional and has no chain groups in degrees thirteen and above.

Index faces of each dimension by their vertex masks. For every \(d\)-simplex, form its complete \(\mathbb F_2\) boundary column by deleting each of its \(d+1\) vertices. Deterministic sparse binary Gaussian elimination on these entire boundary matrices gives
\[
(r_1,\ldots,r_{12})=(35,505,3935,18277,52967,98150,
118210,92606,46080,13536,1872,36),
\]
where \(r_d=\operatorname{rank}_{\mathbb F_2}\partial_d\), and \(r_0=r_{13}=0\). This is a full finite-chain certificate, not extrapolation from a partial range. Chain-complex rank-nullity
\[
\beta_d=f_d-r_d-r_{d+1}
\]
gives ordinary \(\beta_0=1\), \(\beta_5=23\), \(\beta_8=2\), and zero in all other positive degrees. The reduced degree-zero group is zero because the complex is connected. Directly, \(r_9=46080\), \(r_{10}=13536\), \(r_{11}=1872\), and \(r_{12}=36\) force \(\beta_9=\beta_{10}=\beta_{11}=\beta_{12}=0\). The Euler-characteristic cross-check is \(\chi(K)=-20=1-23+2\).

## Reproducibility and limits of computation

The package's `verify_mod2_primary.cpp` and `verify_mod2_relabelled.cpp` independently index the same graph and enumerate every face, then perform exact sparse \(\mathbb F_2\) elimination. A separately implemented chain enumerator, `independent_torus.cpp`, uses an alternative recursive independent-set traversal and its own boundary-column reduction; all face counts and ranks agreed. Such exhaustive computation certifies the stated **finite complex** in the precise coefficient field. It is not a proof of an infinite family or an integral homotopy type.

## Prior results and contribution

Henry Adams, Adenike Yeside Adetowubo, Hector Barriga-Acosta, Ziqin Feng, and John Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134 (2025), Table 1, report the entry `5:23,8:2` for \((n,k)=(6,4)\). The legend explicitly specifies that cells **without** a subsequent parenthesized zero have been computed only up to their largest displayed homology degree: here **eight**. This previously published computation covers the nonzero numbers and lower-degree vanishing, but does **not** establish the zero higher-degree homology groups. The full finite-chain rank calculation above closes that specific gap. Question 8.2 of the same article asks for the *homotopy type* of the complex, and that question is **not** answered here.

Other related results on scale-two toroidal grids and on twisted-grid Rips complexes concern different metric complexes and do not imply the higher-degree vanishing at \((6,4)\). The new part is narrow but supplies the complete mod-two homology invariant of a parameter pair explicitly singled out in a current topological problem. Historical literature priority outside these inspected sources remains conditional.

## Limitations

No integral torsion, integral homology, cup product, fundamental group, or homotopy type is determined, and no claim is made for other torus sizes or Rips scales. The already published ranks and their lower-degree context are not novel. Exact finite rank computations establish only the finite mod-two conclusion; the natural remaining homotopy problem is open as far as the inspected literature shows.

## References

- H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, and J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134 (February 10, 2025), especially Table 1, its caption, and Question 8.2, https://arxiv.org/abs/2502.07134.
