# A parity law for integral symmetry coinvariants of complete-bipartite higher independence complexes

## Finding
Let \(m,n\ge2\) and \(2\le r<m+n\). Write \(K=\operatorname{Ind}_r(K_{m,n})\), where a vertex set is a face when every connected component of its induced bipartite graph contains at most \(r\) vertices. The natural group \(G=S_m\times S_n\) permutes vertices within the two parts. Define the **integral homology coinvariant group**
\[
Q_{m,n,r}=\widetilde H_{r-1}(K;\mathbb Z)_G
=\widetilde H_{r-1}(K;\mathbb Z)/\langle gz-z:g\in G\rangle.
\]
This is not asserted to be the homology of the geometric quotient.

Put \(k=r+1\), \(L=\max(1,k-n)\) and \(U=\min(k-1,m)\). The group \(Q_{m,n,r}\) is an **elementary abelian two-group**, \((\mathbb Z/2)^{d}\), with the following exact rank, valid at all stated boundaries:

* If \(r\) is odd and \(m+n=k\), then \(d=1\).
* If \(r\) is odd and \(m+n>k\), then \(d\) is the number of odd integers in the inclusive interval \([L,U]\).
* If \(r\) is even, partition \(\{0,1,\dots,k\}\) into pairs \(\{0,1\},\{2,3\},\ldots,\{k-1,k\}\). Let \(c\) count pairs meeting \([L,U]\). Then
\[
d=c-\mathbf 1_{n\ge k}-\mathbf 1_{m\ge k}.
\]
In particular, in the stable range \(m,n\ge r+1\),
\[
Q_{m,n,r}\cong\begin{cases}
(\mathbb Z/2)^{(r+1)/2},&r\text{ odd},\\
(\mathbb Z/2)^{(r-2)/2},&r\text{ even}.
\end{cases}
\]
The underlying homology \(\widetilde H_{r-1}(K;\mathbb Z)\) is free abelian, so this two-torsion records an **integral symmetry obstruction**, not torsion in the homology before taking coinvariants. The nonequivariant homotopy rank was established previously by Deshpande and Singh and is **not** claimed as new.

## Assumptions and scope
The two vertex parts \(A,B\) have sizes \(m,n\ge2\); \(2\le r<m+n\); actions are simplicial vertex permutations and induce the usual signed action on oriented chains. All homology is reduced integral simplicial homology. The result concerns the coinvariants of degree \(r-1\) homology under the **part-preserving** group \(S_m\times S_n\), not the larger group swapping parts when \(m=n\). Values of \(r=1\) and \(r\ge m+n\) are excluded; no claim is made for them.

## Proof
A face using vertices from both parts induces a connected complete bipartite graph, and hence is allowed exactly when its total size is at most \(r\). A face contained in one part is always allowed. Therefore, writing \(\Delta(V)^{(r-1)}\) for the full \((r-1)\)-skeleton,
\[
K=\Delta(A\sqcup B)^{(r-1)}\cup\Delta(A)\cup\Delta(B).
\]
Every \((r-1)\)-cycle of the full skeleton is the boundary of an oriented \(r\)-chain of the full simplex, since that full simplex is acyclic. If \(C_j\) denotes its integral oriented \(j\)-chain group, exactness gives an equivariant presentation
\[
\widetilde H_{r-1}(K;\mathbb Z)
\cong C_r(\Delta(A\sqcup B))\big/
\bigl(\partial C_{r+1}(\Delta(A\sqcup B))
+C_r(\Delta(A))+C_r(\Delta(B))\bigr).
\]
Indeed, the two pure-part summands account precisely for the boundaries in \(K\) at this degree. No additional high-dimensional pure-part boundary changes this quotient, since such boundaries already lie in the pure-part \(r\)-chains.

Taking \(G\)-coinvariants is right exact, so first take coinvariants of the oriented \(r\)-simplex group. Its simplex orbits are determined by \(a=\lvert T\cap A\rvert\) and \(k-a=\lvert T\cap B\rvert\). Every orbit contains a permutation interchanging two vertices in the same part, because \(k=r+1\ge3\). That element fixes the underlying simplex and reverses its orientation. Hence each orbit contributes **exactly** \(\mathbb Z/2\) before imposing chain-boundary relations. (The orbit module is the sign-induced module from its stabilizer, whose coinvariants are \(\mathbb Z/2\).) The pure-part simplices remove \(a=0\) and \(a=k\). The remaining generators \(e_a\) have \(L\le a\le U\).

An \((r+1)\)-simplex of type \((a,b)\), \(a+b=k+1\), contributes \(a\) faces of type \((a-1,b)\) and \(b\) faces of type \((a,b-1)\). In the exponent-two coinvariant group their orientation signs disappear. Thus its boundary supplies exactly
\[
(a\bmod2)e_{a-1}+(b\bmod2)e_a=0,
\]
for every feasible \(0\le a\le m\), \(0\le b\le n\), with \(e_j=0\) outside the mixed interval. These are **all** the relations, by the displayed equivariant presentation. In particular, the quotient has exponent at most two and has no free or odd-torsion summands.

If \(r\) is odd, then \(k+1=r+2\) is odd. The relation for each feasible \((a,b)\) kills the even-indexed mixed generator on one side and never involves an odd-indexed mixed generator. Whenever \(m+n>k\), every feasible mixed \(k\)-subset has an available extension vertex in at least one part, so every even-indexed mixed generator is killed. All odd-indexed ones remain freely independent over \(\mathbb F_2\). When \(m+n=k\), no \((k+1)\)-subset exists and the unique feasible mixed type survives. This proves both odd cases.

If \(r\) is even, then \(k\) is odd. A nonzero relation occurs only when \(a,b\) are both odd; it relates exactly the pair \(e_{a-1}+e_a\). These are disjoint pairs \((0,1),(2,3),\ldots,(k-1,k)\). Each interior pair meeting the feasible interval contributes one class: if both types occur, they are identified by the corresponding feasible boundary; if only one occurs, the missing adjacent type is excluded precisely by a saturated part and the boundary does not exist. At the left endpoint, the relation from the type \((1,k)\) kills \(e_1\) precisely when \(n\ge k\); symmetrically the type \((k,1)\) kills \(e_{k-1}\) precisely when \(m\ge k\). Subtracting these two endpoints gives the stated even formula. In the stable range, there are \((r+1)/2\) possible pairs and exactly two killed endpoints, whereas the odd case has \((r+1)/2\) surviving odd-index generators. This completes the proof.

## Verification
The accompanying dependency-free Python program `verify.py` constructs the original signed-simplex orbit relations (reduced modulo two) independently of the reduced color-count presentation, for all \(70\) triples with \(2\le m,n\le5\) and \(2\le r<\min(m+n,7)\). It verifies agreement between the original-chain presentation, the orbit relation matrix and the closed formula. It also checks the orbit formula for every \(2\le m,n\le35\), \(2\le r<m+n\). Its recorded output is in `verify-output.txt`. Crucially, the **proof** of the integral exponent-two claim is the orientation-reversing stabilizer argument above; finite field calculations alone would not prove it.

## Relationship to prior work
Deshpande and Singh, Theorem 3.5 of arXiv:2001.05448 (first version January 15, 2020), already classify the nonequivariant homotopy type of higher independence complexes of **all complete multipartite graphs**, including this bipartite family, by explicit sphere multiplicities. Their statement is stronger for ordinary nonequivariant homotopy types; the result here concerns a different, integral **part-permutation coinvariant** invariant and does not reproclaim that classification. Sawant, arXiv:2605.25150 (first submitted May 24, 2026), establishes vertex decomposability for the corresponding complexes of trees; that theorem does not cover complete bipartite graphs with cycles nor their integral symmetry modules. Targeted mathematical-record and primary-source comparisons identified no formula for the coinvariant groups above. This is a best-knowledge originality assessment, not a uniqueness certificate.

## Limitations
This result does not determine the full integral \(\mathbb Z[S_m\times S_n]\)-module, the action of interchanging parts, or integral homology of a geometric quotient. It does not imply that the original homology has torsion. The available literature comparison cannot exclude an unindexed equivalent result. The verifier checks finite cases; the infinite theorem rests on the chain-orbit proof.

## References
1. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, first public version January 15, 2020; Theorem 3.5. https://arxiv.org/abs/2001.05448
2. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150, first public version May 24, 2026. https://arxiv.org/abs/2605.25150
