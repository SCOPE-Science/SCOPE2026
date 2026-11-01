# Mixed sphere wedges and integral symmetry of degree-bounded bipartite subsets

## Finding
Let \(m,n,r\) be integers with \(r\ge 2\) and \(m,n\ge r+1\). Write \(G=K_{m,n}\) with labeled parts \(L\) and \(R\), and let \(D_r(G)\) be the abstract simplicial complex on \(V(G)\) whose faces are exactly those vertex sets \(F\) for which the induced graph \(G[F]\) has maximum degree at most \(r\). Put \(a=\binom{m-1}{r}\) and \(b=\binom{n-1}{r}\).

There is a nonequivariant integral homotopy equivalence
\[
D_r(K_{m,n})\simeq\bigvee^{a+b}S^r\ \vee\ \bigvee^{ab}S^{2r-1}.
\]
For \(W_k=\ker(\varepsilon:\mathbb Z^k\to\mathbb Z)\), where \(\varepsilon\) sums coordinates, the *complete integral* \(S_m\times S_n\)-homology modules are
\[
\widetilde H_r(D_r;\mathbb Z)\cong
 (\bigwedge^r W_m\boxtimes\mathbb Z)\oplus
 (\mathbb Z\boxtimes\bigwedge^r W_n),
\qquad
\widetilde H_{2r-1}(D_r;\mathbb Z)\cong
 \bigwedge^r W_m\boxtimes\bigwedge^r W_n.
\]
Every other reduced integral homology group vanishes. In particular the groups have no torsion.

When \(m=n\), the automorphism that exchanges the two graph parts swaps the two summands of degree \(r\) without a sign and acts on degree \(2r-1\) as \((-1)^r\) times the tensor flip. Thus, writing \(d=\binom{m-1}{r}\), its trace in the two degrees is respectively \(0\) and \((-1)^r d\). More generally, for a part-preserving automorphism \((\sigma,\pi)\), put \(c_r(\sigma)=[t^r]\det(I+t\sigma\mid W_m\otimes\mathbb Q)\) and define \(c_r(\pi)\) similarly. The degree-\(r\) and degree-\(2r-1\) characters are respectively \(c_r(\sigma)+c_r(\pi)\) and \(c_r(\sigma)c_r(\pi)\). For a balanced-graph part-exchanging automorphism \((\sigma,\pi)\tau\), they are \(0\) and \((-1)^r c_r(\sigma\pi)\).

## Assumptions and scope
Here \(D_r\) is a *vertex-set* complex defined by bounded maximum induced degree, not an edge-set matching complex and not the distinct convention in which an independence complex bounds connected-component sizes. The ground graph is the ordinary simple, loopless complete bipartite graph. Part-permuting actions are on vertex labels, preserving the simplicial orientation signs. The two nonzero degrees are distinct because \(r\ge 2\); the theorem makes no assertion about the exceptional degree-collision case \(r=1\).

## Proof
**1. Exact decomposition.** Let \(A=\operatorname{sk}_{r-1}\Delta_L\) and \(B=\operatorname{sk}_{r-1}\Delta_R\), where \(\Delta_L\) and \(\Delta_R\) are full simplices on the two parts. A mixed vertex set with \(u>0\) left vertices and \(v>0\) right vertices induces \(K_{u,v}\), with maximum degree \(\max(u,v)\); therefore it is a face precisely when \(u,v\le r\). Pure sets are always faces. Hence, as an equality of subcomplexes,
\[
D_r=J\cup\Delta_L\cup\Delta_R,\qquad J=A*B,
\quad J\cap\Delta_L=A,\quad J\cap\Delta_R=B,\quad \Delta_L\cap\Delta_R=\varnothing
\]
(where the last equality means the empty geometric realization).

**2. The skeleton modules and homotopy types.** For a simplex on \(k\) vertices, oriented simplicial chains identify \(C_{r-1}\) with \(\bigwedge^r\mathbb Z^k\). Its degree-\((r-1)\) boundary is contraction by the coordinate-sum functional \(\varepsilon\). Since \(\mathbb Z^k=W_k\oplus\mathbb Z e_0\) integrally, the kernel of this contraction is exactly \(\bigwedge^r W_k\). There are no \(r\)-faces in the skeleton, so
\[
\widetilde H_{r-1}(\operatorname{sk}_{r-1}\Delta^{k-1};\mathbb Z)=\bigwedge^r W_k.
\]
All other reduced homology groups vanish. Explicitly, match each nonempty face not containing a chosen vertex \(0\) and of size at most \(r-1\) to the face obtained by adding \(0\); the unmatched cells are a point and precisely the \(\binom{k-1}{r}\) faces of size \(r\) avoiding \(0\). This acyclic simplicial matching proves the skeleton is a wedge of \(\binom{k-1}{r}\) spheres of dimension \(r-1\). The choice of \(0\) is solely for this nonequivariant homotopy argument; the chain-kernel module identification is natural for vertex permutations.

**3. Homotopy splitting.** The join \(J=A*B\) is a wedge of \(ab\) spheres of dimension \(2r-1\). The inclusions \(A\hookrightarrow J\) and \(B\hookrightarrow J\) are nullhomotopic: each is coned off by any fixed vertex in the opposite part. Attach the contractible simplex \(\Delta_L\) along \(A\), and then attach \(\Delta_R\) along \(B\). The homotopy-pushout/cofibration splitting for these null maps gives
\[
D_r\simeq J\vee\Sigma A\vee\Sigma B,
\]
and the claimed integral sphere-wedge decomposition follows. This splitting is not asserted to be equivariant.

**4. Integral equivariance.** Consider the pair \((D_r,J)\). In positive degrees its relative chains split naturally as the direct sum of the relative chains of \((\Delta_L,A)\) and \((\Delta_R,B)\). The latter relative homology groups are concentrated in degree \(r\), where the connecting homomorphisms give the integral \(S_m\times S_n\)-equivariant identifications with \(\widetilde H_{r-1}(A)\) and \(\widetilde H_{r-1}(B)\). Since \(J\) has reduced homology only in degree \(2r-1\), and \(r\ge2\), the pair long exact sequence yields exactly the two integral module isomorphisms displayed in the finding. The degree-\((2r-1)\) isomorphism comes from inclusion of \(J\) and the standard natural join-Künneth isomorphism; all groups involved are free over \(\mathbb Z\).

**5. Exchanging equal-sized parts.** On \(\widetilde H_r(D_r)\), the exchange interchanges the two relative summands naturally, with no sign. On \(\widetilde H_{2r-1}(J)\), interchange of two reduced join cycles of dimension \(r-1\) carries the Koszul sign \((-1)^{((r-1)+1)((r-1)+1)}=(-1)^r\). This proves the signed tensor flip. The trace identity for a twisted tensor flip follows from \(\operatorname{tr}((P\otimes Q)\circ\mathrm{Flip})=\operatorname{tr}(PQ)\), giving the formulas.

## Verification
The accompanying standard-library Python file `verify_bipartite.py` generates **all actual faces** for four small parameter sets, independently forms their integer simplicial boundary matrices, and performs modular row reductions at primes \(2\) and \(3\). It verifies the predicted reduced Betti numbers for \((m,n,r)=(3,3,2),(4,4,2),(4,5,2),(5,5,3)\). It also computes signed simplex-permutation Lefschetz traces, checking every part-preserving permutation for \((3,3,2),(4,4,2),(4,5,2),(4,4,3)\) and every part-exchanging permutation for the balanced cases. Output is recorded in `verification_output.txt`. The infinite-parameter and integral conclusions come from the proof, not from modular sampling.

## Relationship to prior work
The induced-degree definition follows the established notion of \(k\)-independent graph vertex sets: Guo, Zhao, Lai, and Mao (arXiv:1505.04867, initial release May 19, 2015) study numerical regular \(k\)-independence parameters and explicitly treat complete multipartite graphs. Their arguments do not compute the simplicial topology of *all* allowable vertex sets, homology representations, or the sign of part interchange. The theorem converts that natural extremal-graph family into a topological classification; it does not claim the definition or numerical independence parameters are new. A separately used convention for higher independence complexes bounds connected-component size, not maximum induced degree, and is not equivalent here.

## Limitations
No equivariant homotopy *splitting* is asserted: the explicit wedge splitting uses non-equivariant choices. Only the integral homology modules and the balanced part-interchange action are equivariant. The case \(r=1\), where the homological degrees coincide and an integral module extension can arise, is excluded. No assertion is made about arbitrary noncomplete bipartite graphs. An equivalent unindexed decomposition in combinatorial-topology literature remains possible; this is not independent mathematical certification.

## References
1. Z. Guo, H. Zhao, H.-J. Lai, and Y. Mao, *On the regular k-independence number of graphs*, arXiv:1505.04867, first public version May 19, 2015, https://arxiv.org/abs/1505.04867. Definitions in Section 1 and complete multipartite numerical cases in Section 2.
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418 (2010), https://arxiv.org/abs/1007.0418. General homotopy background for ordinary independence complexes, a distinct degree-zero construction.
