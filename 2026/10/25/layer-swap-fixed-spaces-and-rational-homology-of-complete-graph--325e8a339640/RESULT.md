# Layer-swap fixed spaces and rational homology of complete-graph triple products

## Finding
For integers \(n,m\ge2\), let
\[
X_{n,m}=\operatorname{Ind}(K_2\times K_n\times K_m),
\qquad \tau(\epsilon,i,j)=(1-\epsilon,i,j).
\]
All graph products in this statement are **categorical**: two vertices are adjacent precisely when they differ in every coordinate. The involution \(\tau\) acts simplicially on \(X_{n,m}\), and fixed points below mean fixed points of its **geometric realization**, not merely vertices fixed individually.

Set \(b=(n-1)(m-1)\). There is a canonical piecewise-linear homeomorphism
\[
|X_{n,m}|^{\langle\tau\rangle}\cong
|\operatorname{Ind}(K_n\times K_m)|,
\]
intertwining the coordinate-relabeling action of \(S_n\times S_m\). In particular,
\[
|X_{n,m}|^{\langle\tau\rangle}\simeq \bigvee^{b}S^1,
\qquad
H_1\bigl(|X_{n,m}|^{\langle\tau\rangle};\mathbb Z\bigr)
\cong L_n\otimes_{\mathbb Z}L_m,
\]
where \(L_k=\ker(\mathbb Z^{[k]}\xrightarrow{\sum}\mathbb Z)\) is the integral augmentation lattice, and the last isomorphism is natural for \(S_n\times S_m\).

The unique nonzero reduced rational homology group of \(X_{n,m}\) occurs in degree three. The complete character under \(\langle\tau\rangle\) has trace and eigenmultiplicities
\[
\begin{split}
\operatorname{tr}(\tau\mid\widetilde H_3(X_{n,m};\mathbb Q))&=b,\\
\dim\widetilde H_3(X_{n,m};\mathbb Q)^{+}&=\frac{nm(n-1)(m-1)}4,\\
\dim\widetilde H_3(X_{n,m};\mathbb Q)^{-}&=\frac{(nm-4)(n-1)(m-1)}4.
\end{split}
\]
Consequently, the rational homology of the orbit space satisfies
\[
\widetilde H_k\bigl(|X_{n,m}|/\langle\tau\rangle;\mathbb Q\bigr)\cong
\begin{cases}
\mathbb Q^{nm(n-1)(m-1)/4},&k=3,\\
0,&k\ne3.
\end{cases}
\]
These are integer-valued expressions for every \(n,m\ge2\). The previously recorded special case \(n=m=4\), with eigenmultiplicities \(36\) and \(27\), is a consequence rather than a new finite result.

## Assumptions and scope
All simplicial complexes are ordinary abstract independence complexes on finite simple loopless graphs. The geometric realization of a complex with a simplicial action is taken in barycentric coordinates. All homology is reduced except where explicitly stated. The characterization of the ambient homotopy type is the published theorem of Antolín Camarena and Carnero Bravo, Proposition 25 of arXiv:2307.12401, which gives
\[
X_{n,m}\simeq\bigvee^{B}S^3,
\qquad B=\frac{(n-1)(m-1)(nm-2)}2.
\]
Our contribution concerns the involution-fixed space, its natural integral coordinate representation, and the induced rational involution character and quotient homology—not this prior nonequivariant sphere count.

## Proof
**1. Geometric fixed points are orbit simplices.** Write a graph vertex as \((\epsilon,i,j)\) with \(\epsilon\in\{0,1\}\), \(i\in[n]\), \(j\in[m]\). In an arbitrary point of \(|X_{n,m}|\), the minimal supporting face \(F\) is determined by the strictly positive barycentric coordinates. If the point is fixed by \(\tau\), then \(F=\tau F\), and the coefficients of \((0,i,j)\) and \((1,i,j)\) coincide. Thus every fixed point is uniquely a convex combination of midpoint vertices \(v_{ij}=\tfrac12((0,i,j)+(1,i,j))\), subject only to the condition that the union of the full corresponding two-vertex orbits is an independent face.

Let \(S\subseteq[n]\times[m]\) be nonempty. For two distinct pairs \((i,j),(i',j')\in S\), the opposite-layer vertices \((0,i,j)\) and \((1,i',j')\) are adjacent exactly when \(i\ne i'\) **and** \(j\ne j'\). Thus the union of the layer-orbits indexed by \(S\) is independent if and only if \(S\) contains no two pairs different in both coordinates. This is exactly the independence condition for \(K_n\times K_m\) on \([n]\times[m]\). Mapping each abstract vertex \((i,j)\) to the midpoint \(v_{ij}\) linearly on faces therefore yields the asserted canonical PL homeomorphism, with inverse given by summing each layer pair's barycentric coefficients. Both maps commute with all row and column permutations.

**2. The fixed-space integral module.** Every independent set in \(K_n\times K_m\) lies in a single row or a single column: if two members have different rows, their columns must coincide, and every further member must use that column. The full row and column simplices form a simplicial cover. Individual sets are contractible, each row-column intersection is a single vertex, and other nonempty intersections are absent. The ordinary nerve lemma gives the complete bipartite graph \(K_{n,m}\), whose reduced homology consists of \(b=(n-1)(m-1)\) degree-one generators. The cover and all of its intersection contraction data are natural under \(S_n\times S_m\); equivalently, use the canonical integral Mayer–Vietoris/nerve chain identification, so the isomorphism of first-homology modules is equivariant.

Orient every edge of the bipartite nerve from a row vertex to a column vertex. Its integral cycle lattice is the kernel of the incidence boundary \(\partial:\mathbb Z^{[n]\times[m]}\to\mathbb Z^{[n]}\oplus\mathbb Z^{[m]}\), which sends the edge \((i,j)\) to the difference of its endpoints. Identifying the edge lattice with \(\mathbb Z^{[n]}\otimes\mathbb Z^{[m]}\), this kernel consists of integer matrices with every row sum and column sum zero. It is canonically \(L_n\otimes L_m\), a free abelian group of rank \(b\), with its natural permutation action.

**3. Rational Lefschetz character.** For any finite simplicial automorphism, the simplicial Lefschetz number (the alternating signed trace of its cellular chain maps) equals the Euler characteristic of its geometric fixed-point subspace. This can also be seen directly by matching an invariant face made of \(k\) swapped vertex-pairs with the corresponding \((k-1)\)-simplex of orbit midpoints: the invariant face has dimension \(2k-1\) and the involution induces sign \((-1)^k\), yielding Lefschetz contribution \((-1)^{(2k-1)}(-1)^k=(-1)^{k+1}\), the usual alternating contribution of the orbit simplex. Our fixed-space calculation gives \(\chi(|X|^\tau)=1-b\).

The cited sphere-wedge theorem implies \(H_0(X_{n,m};\mathbb Q)=\mathbb Q\), \(\widetilde H_3(X_{n,m};\mathbb Q)=\mathbb Q^B\), and no other homology. Therefore
\[
1-b=\operatorname{Lef}(\tau)=1-\operatorname{tr}(\tau\mid\widetilde H_3),
\]
so the third-homology trace equals \(b\). As \(\tau^2=1\), its characteristic polynomial over \(\mathbb Q\) splits with eigenvalues \(\pm1\). Their multiplicities are \((B+b)/2\) and \((B-b)/2\), which simplify to the stated formulas.

**4. Quotient.** Because the action is finite and coefficients are rational, the transfer/averaging isomorphism identifies \(H_*(|X|/\langle\tau\rangle;\mathbb Q)\) with \(H_*(|X|;\mathbb Q)^{\langle\tau\rangle}\), even when fixed points are present. The positive-eigenspace dimension above gives the claimed quotient homology, including connected degree zero.

## Verification
Run the included standalone file `verify_layer_swap.py` with Python 3. It independently constructs the full face posets for \((n,m)=(2,2),(2,3),(3,2),(2,4),(3,3)\), identifies all involution-fixed faces with the two-factor orbit faces, checks signed Lefschetz counts and the two eigenmultiplicities, and computes all mod-two simplicial homology ranks in these examples. The output ends with `LAYER_SWAP_FIXED_SPACE_AND_TRACE_CHECKS_PASSED 5`. Exact finite computations are supporting tests and are **not** the proof for all parameters; the preceding arguments are.

## Relationship to prior work
Antolín Camarena and Carnero Bravo proved the ambient complete-graph triple-product sphere-wedge homotopy type used above; the fixed-point and rational homology-action refinements are not statements of their Proposition 25. Goyal, Shukla and Singh earlier established the two-factor ordinary homotopy type and row/column description. An earlier recorded result determined the much narrower \((n,m)=(4,4)\) involution eigenspace multiplicities, which are recovered here but are not independently novel. The present result is the all-parameter PL fixed-point identification and equivariant refinement. Searches also compared alternative names (categorical/tensor/direct graph product, independence/flag complex, geometric involution-fixed points, quotient homology), but no search is proof of priority.

## Limitations
The theorem concerns the exchange of the **binary factor only**; it does not determine characters of arbitrary permutations of the two other factors or the full automorphism group. Ambient homology character statements are rational, and no integral equivariant lattice in degree three is claimed. The fixed-space first-homology lattice, by contrast, is integral. The published nonequivariant sphere-wedge theorem is used as a known input rather than reproved. Unindexed preprints or equivariant reformulations may still affect priority; independent audit has not been conducted.

## References
- O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first posted 2023-07-23), Proposition 25, https://arxiv.org/abs/2307.12401 .
- S. Goyal, S. Shukla and A. Singh, *Homotopy type of independence complexes of certain families of graphs*, arXiv:1905.06926 (first posted 2019-05-16), Section 3 and Proposition 3.4, https://arxiv.org/abs/1905.06926 .
