# Mod-two homology of the scale-four Vietoris–Rips complex of the six-by-six torus grid

## Finding

Let \(T_6=(\mathbb Z/6\mathbb Z)^2\) with the discrete torus Manhattan metric

\[
d((i,j),(u,v))=\delta_6(i,u)+\delta_6(j,v),\qquad
\delta_6(a,b)=\min\{|a-b|,6-|a-b|\},
\]

where coordinates are represented in \(\{0,1,2,3,4,5\}\). Let \(K=\operatorname{VR}_{\le4}(T_6)\): a subset is a simplex exactly when every pair of its points has distance at most \(4\). Then the reduced homology over \(\mathbb F_2\) is

\[
\widetilde H_q(K;\mathbb F_2)\cong
\begin{cases}
\mathbb F_2^{23},&q=5,\\
\mathbb F_2^{2},&q=8,\\
0,&q\notin\{5,8\}.
\end{cases}
\]

In particular, \(K\) is connected, with ordinary \(H_0(K;\mathbb F_2)\cong\mathbb F_2\). This is a coefficient-field homology result only; it does not assert an integral homology or homotopy classification.

## Assumptions and scope

The scale convention is inclusive: distance exactly \(4\) is allowed. The metric is the shortest-path Manhattan metric on the discrete Cartesian torus, not the geodesic metric on the continuous torus. Homology coefficients are \(\mathbb F_2\). The vertex set has \(36\) points. No statement is made for other side lengths, scales, or coefficient rings.

## Proof

Let \(H\) be the graph on \(T_6\) whose edges join pairs at distance greater than \(4\). A set is a simplex of \(K\) if and only if it is an independent set of \(H\), so \(K=\operatorname{Ind}(H)\). Directly from the metric, \(H\) is a five-regular graph with \(90\) edges: its difference vectors are \((3,2),(3,-2),(2,3),(-2,3),(3,3)\) modulo \(6\).

The two included C++17 programs enumerate every independent set of \(H\), hence every nonempty simplex of \(K\), and construct the simplicial boundary matrices over \(\mathbb F_2\). The face counts by simplex dimension \(0\) through \(12\) are

\[
(f_0,\ldots,f_{12})=(36,540,4440,22212,71244,151140,216360,210816,138688,59616,15408,1908,36).
\]

Their boundary-matrix ranks are

\[
(r_1,\ldots,r_{12})=(35,505,3935,18277,52967,98150,118210,92606,46080,13536,1872,36),
\]

where \(r_d=\operatorname{rank}_{\mathbb F_2}(\partial_d:C_d\to C_{d-1})\). For each dimension, the chain-complex identity gives \(\beta_d=f_d-r_d-r_{d+1}\), with \(r_0=r_{13}=0\). Substitution yields \(\beta_0=1\), \(\beta_5=23\), \(\beta_8=2\), and zero in all other positive degrees. The Euler characteristic check is \(\chi(K)=-20=1-23+2\).

The rank computation is finite and exact over \(\mathbb F_2\): each boundary column is the sum of its codimension-one faces, and sparse Gaussian elimination uses symmetric difference of sorted row-index lists. The full face enumeration and every boundary rank are reproduced by both included source files.

## Verification

Run `verify_mod2_primary.cpp` and `verify_mod2_relabelled.cpp` with a C++17 compiler. Both use only the standard library. The second program relabels the vertices by the permutation \(a\mapsto 7a+5\pmod{36}\), independently changing the indexing of the same metric graph; both runs return the same face vector and all twelve boundary ranks. The corresponding captured outputs are included. This checks the claimed mod-two Betti vector, not integral torsion or homotopy type.

## Relationship to prior work

Adams, Adetowubo, Barriga-Acosta, Feng, and Sterling study Vietoris–Rips complexes of discrete torus grids. Their paper explicitly asks for the homotopy types of \(\operatorname{VR}(T_{6,6};4)\), \(\operatorname{VR}(T_{7,7};4)\), and several further cases in Question 8.2; it proves the \(T_{7,7}\) scale-four case is a three-sphere and the \(T_{5,5}\) scale-three case is a wedge of nine four-spheres. The inspected text does not state the mod-two Betti vector for \(T_{6,6}\) at scale four. Related published-finding corpus records found in the search concern scale-two toroidal grids or other graph-metric Rips complexes and do not imply this parameter-specific vector.

The present claim answers a natural invariant question within the published open homotopy problem, but it is strictly weaker than identifying the homotopy type. The absence of an exact match in a database search is not a proof of global novelty.

## Limitations

The computation does not determine integral homology, possible torsion, cup products, the fundamental group, or the homotopy type of \(K\). It gives no general formula for \(\operatorname{VR}(T_{n,n};k)\). The result is a finite, coefficient-specific invariant for the single parameter pair \((n,k)=(6,4)\). Independent external validation has not been performed.

## References

- Henry Adams, Adenike Yeside Adetowubo, Hector Barriga-Acosta, Ziqin Feng, and John Sterling, “Vietoris–Rips complexes of torus grids,” arXiv:2502.07134, first publicly posted 2025-02-10; especially Section 7 and Question 8.2.
- published-finding corpus comparison record: “A thin toroidal grid has scale-two Rips type \(S^1\vee\bigvee^n S^3\)” (scale two, different parameters).
- published-finding corpus comparison record: “An explicit simplicial collapse of twisted grid Rips complexes to the Klein bottle” (twisted grids, scale two, different complexes).
