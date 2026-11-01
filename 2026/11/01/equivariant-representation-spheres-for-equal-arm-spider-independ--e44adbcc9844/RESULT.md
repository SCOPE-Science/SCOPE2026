# Equivariant representation spheres for equal-arm spider independence complexes

## Finding
Let \(T_{m,L}\) be a tree consisting of \(m\ge3\) paths of \(L\ge1\) edges meeting only at their common central vertex \(c\). The symmetric group \(S_m\) permutes the arms. Let \(X_{m,L}=|\operatorname{Ind}(T_{m,L})|\) with the induced simplicial group action, and let \(V_m=\mathbb R^m\) be the standard real **permutation** representation. For the unit representation sphere \(S(V)\), there are genuine equivariant homotopy equivalences
\[
X_{m,L}\simeq_{S_m}\begin{cases}
*,&L=3q,\ q\ge1,\\
S(\mathbb R\oplus qV_m),&L=3q+1,\ q\ge0,\\
S((q+1)V_m),&L=3q+2,\ q\ge0.
\end{cases}
\]
Here \(\mathbb R\) has trivial action. This classifies an **equivariant homotopy type**, not merely the ranks of homology. In particular, for every subgroup \(H\le S_m\) and its number \(o(H)\) of orbits on the arms, the **actual** geometric fixed-point space is PL-homeomorphic to the independence complex of an ordinary spider on \(o(H)\) arms of the same length:
\[
X_{m,L}^{H}\cong_{\rm PL}|\operatorname{Ind}(T_{o(H),L})|.
\]
Consequently these fixed spaces are, respectively, contractible, homotopy equivalent to \(S^{q o(H)}\), or to \(S^{(q+1)o(H)-1}\). In the two noncontractible cases the only nonzero reduced integral homology is rank one, in degree \(qm\) or \((q+1)m-1\), and the full \(S_m\) action is \(\operatorname{sgn}^{q}\) or \(\operatorname{sgn}^{q+1}\), respectively.

## Assumptions and scope
The ordinary path \(P_t\) has \(t\) vertices; \(P_0\) is the empty graph, and its augmented independence complex is the single empty face (formal sphere \(S^{-1}\) for join calculations). Each arm of \(T_{m,L}\) has vertices \(v_{i,1},\ldots,v_{i,L}\) with edges \(cv_{i,1}\) and \(v_{i,j}v_{i,j+1}\). Every group action is induced by \(\sigma v_{i,j}=v_{\sigma(i),j}\) and \(\sigma c=c\). Geometric fixed points mean points fixed in the realization, not the realization of the vertexwise fixed subcomplex. The group is finite and all spaces are finite simplicial \(S_m\)-spaces. A representation sphere means the **unit sphere**, not the one-point compactification. A point denotes an equivariantly contractible space. The case \(L=1\) is included and yields a trivially acted-on \(S^0\).

## Proof
**1. Path factors and their explicit fold.** For \(t\ge3\), in the path with consecutive vertices \(1,\ldots,t\), the open neighborhoods satisfy \(N(1)\subseteq N(3)\). The standard independent-set folding map deletes vertex \(3\) and is a homotopy equivalence, giving
\[
|\operatorname{Ind}(P_t)|\simeq |\operatorname{Ind}(P_2)*\operatorname{Ind}(P_{t-3})|.
\]
One can see the fold directly: replace vertex \(3\) by vertex \(1\) in each face. The replacement is simplicial, fixes the subcomplex without vertex \(3\), and its composite with inclusion is contiguous to the identity because whenever \(3\) belongs to an independent face, vertex \(1\) can be added without violating independence (any neighbor of \(1\) is a neighbor of \(3\)). Iterate the same fold on the remaining path. Since \(\operatorname{Ind}(P_1)\) is a point and \(\operatorname{Ind}(P_2)\) consists of two points,
\[
|\operatorname{Ind}(P_{3q})|\simeq S^{q-1},\quad
|\operatorname{Ind}(P_{3q+1})|\simeq *,\quad
|\operatorname{Ind}(P_{3q+2})|\simeq S^q.
\]
The last two identities hold also for \(q=0\), with the convention on \(P_0\) confined to augmented joins.

**2. An equivariant center decomposition.** Put \(A=\operatorname{Ind}(T_{m,L}-c)\) and \(B=\operatorname{lk}_{\operatorname{Ind}(T_{m,L})}(c)\). Since no edge joins distinct arms once the center is removed,
\[
A=\mathop{*}_{i=1}^m\operatorname{Ind}(P_L),\qquad
B=\mathop{*}_{i=1}^m\operatorname{Ind}(P_{L-1}),\qquad
\operatorname{Ind}(T_{m,L})=A\cup_B(c*B).
\]
The action permutes factors. The inclusion \(B\to A\) is the join of the identical path inclusions \(\operatorname{Ind}(P_{L-1})\to\operatorname{Ind}(P_L)\). The union is the equivariant (homotopy) cofiber because simplicial inclusions are equivariant cofibrations.

**3. The subgroup fixed-point lemma.** Let \(H\le S_m\). Each orbit of vertices at a fixed depth \(j\) consists of vertices on distinct arms and is independent. An independent face of \(T_{m,L}\) is \(H\)-stable precisely when it is a union of full vertex orbits, and the allowed orbit sets have the same incidence rules as the vertices of \(T_{o(H),L}\). On the realization, barycentric coordinates must be constant within each vertex orbit. Sending the coordinate of a quotient vertex to the sum of the coordinates on its orbit (and using uniform inverse distribution) gives compatible affine homeomorphisms on each simplex. They assemble into the claimed PL homeomorphism
\[
|\operatorname{Ind}(T_{m,L})|^H\cong_{\rm PL}|\operatorname{Ind}(T_{o(H),L})|.
\]
The same construction applies to \(A\), \(B\), and their inclusion. Their fixed-point diagram consists of \(o(H)\) copies of the respective path complexes, joined together, and the fixed central cone. In particular there are no spurious fixed simplices with internally adjacent vertices.

**4. Three residues.** Suppose \(L=3q\), with \(q\ge1\). The inclusion \(\operatorname{Ind}(P_{3q-1})\hookrightarrow\operatorname{Ind}(P_{3q})\) is a homotopy equivalence: adding the first endpoint is a cone attachment along its link \(\operatorname{Ind}(P_{3q-2})\), which is contractible by Step 1. Hence \(B^H\to A^H\) is a join of \(o(H)\) homotopy equivalences. Every \(X_{m,L}^H\) is thus contractible, and the finite-group equivariant Whitehead theorem makes \(X_{m,L}\to*\) an equivariant homotopy equivalence.

If \(L=3q+1\), first take \(q\ge1\). Every factor of \(A\) is contractible, and using the identical factor contraction on every arm followed by contraction of the simplex of chosen endpoints shows that \(A\) is **equivariantly** contractible. The homotopy cofiber is equivariantly equivalent to the unreduced suspension \(\Sigma B\), with trivial action on the suspension coordinate. An identical homotopy equivalence \(\operatorname{Ind}(P_{3q})\simeq S^{q-1}\) on each arm yields an \(S_m\)-equivariant equivalence of the \(m\)-fold join \(B\) with the join of \(m\) copies of \(S^{q-1}\). Since a join of unit spheres is the unit sphere of the direct sum, this is precisely \(S(qV_m)\) and the suspension is \(S(\mathbb R\oplus qV_m)\). When \(q=0\), \(B=\{\varnothing\}\) as an augmented complex and the original complex is a disjoint union of the central vertex and the simplex of all leaves. The latter contracts equivariantly to its barycenter, giving the trivially acted-on \(S(\mathbb R)=S^0\).

If \(L=3q+2\), the factors of \(B\) are \(\operatorname{Ind}(P_{3q+1})\), and the same identical-arm contraction makes \(B\) equivariantly contractible. The inclusion \(A\to X_{m,L}\) induces a homotopy equivalence on every subgroup fixed space, hence is an \(S_m\)-homotopy equivalence by equivariant Whitehead. Applying Step 1 uniformly to all arms gives \(A\simeq_{S_m}S((q+1)V_m)\). The use of one identical fold construction on every arm ensures that the join maps genuinely commute with permutations: no arbitrary order of arms is chosen.

**5. Fixed dimensions and integral characters.** If \(H\) has \(o(H)\) orbits on the \(m\) coordinate axes, the fixed subspace \(V_m^H\) has dimension \(o(H)\). Taking fixed points of the representation spheres now gives the stated formulas; they agree with the PL model in Step 3, including the one-orbit case. Both representation spheres are orientable spheres with integral top homology equal to the determinant character of the ambient orthogonal representation. Since \(\det(V_m)(\sigma)=\operatorname{sgn}(\sigma)\), their determinant characters are the advertised powers. Contractible cases have no reduced homology. This proves all assertions for every \(m,L,H\).

## Verification
The self-contained standard-library checker `verify_spider.py` independently enumerates all independent faces of spiders with \((m,L)\) among fifteen instances having \(2\le m\le4\) and \(1\le L\le6\). From the actual face boundaries it computes full mod-two reduced Betti vectors using exact binary elimination. For every permutation of the arms in each instance it computes the signed simplicial Lefschetz trace using the induced permutation parity on every invariant face, and compares that result with the predicted **fixed-sphere** reduced Euler characteristic (zero in contractible cases). Executing `python3 verify_spider.py` returned `VERIFY_OK 15 full mod-2 Betti vectors; 142 oriented Lefschetz characters; 142 orbit-fixed quotient predictions; 20915 independent face instances`. These are finite checks only: the infinite equivariant classification follows from the explicit joins, fold lemma and equivariant homotopy-cofiber argument above, not from enumeration.

## Relationship to prior work
Daundkar, Panja and Prasad (2023, arXiv:2303.08798v2, Theorem 3.8 and its proof) already show that the independence complex of a terminal wedge of paths is either contractible or a sphere, and describe reductions for the ordinary homotopy type. Our ordinary spider homotopy and Betti ranks are therefore **not new**. Pham and Vu (first submitted April 11, 2026, arXiv:2604.10269v1; inspected v2) give a general criterion for contractibility of tree independence complexes, but do not consider a group action. Neither statement identifies a single genuine \(S_m\)-equivariant representation-sphere homotopy type or the actual fixed-point spaces for **every** subgroup, including the integral determinant character. The fixed spaces are not determined by non-equivariant Betti numbers; the new step is a uniform group-equivariant center-cofiber construction, matched to orbitwise PL fixed models.

The related published-finding corpus record *Integral branch-permutation homology of extended-star Morse complexes* concerns the ordinary discrete-Morse matching complex, not \(\operatorname{Ind}(T_{m,L})\); its sign-twisted augmentation-lattice module is neither the rank-one module here nor a stronger general theorem for independence complexes. *The symmetric-group homology modules of generalized Mycielskians of complete graphs* uses an equivariant folding technique for different graphs and produces tensor-power homology modules, but its hypotheses do not cover these spiders. Search absence cannot prove absolute priority, and more abstract equivariant folding frameworks may subsume special steps of this argument.

## Limitations
The result requires arms of identical positive integer length and the natural full arm-permutation group; unequal-length spiders, larger graph automorphism groups and arbitrary tree actions are not classified. The displayed geometric fixed spaces are PL models, but the representation-sphere equivalences are **homotopy** equivalences, not assertions of PL homeomorphism. The path-fold proof verifies the homotopy equivalence without classifying equivariant simple-homotopy types. Ordinary homotopy types and the path-complex reduction are previously known. No claim of independent validation is made; an equivalent unindexed or abstract equivariant refinement might exist.

## References
1. M. H. Pham and T. Vu, *Contractible independence complexes of trees*, arXiv:2604.10269v1 (first submitted 2026-04-11), https://arxiv.org/abs/2604.10269; original theorem and Section 2 inspected in https://arxiv.org/html/2604.10269v2.
2. N. Daundkar, S. Panja and S. Prasad, *Independence complexes of wedge of graphs*, arXiv:2303.08798v2 (first submitted 2023-03-15), https://arxiv.org/html/2303.08798v2; especially Section 2 path fold and Theorem 3.8 on terminal wedges of paths.
3. K. Kawamura, *Homotopy types of independence complexes of forests*, Contributions to Discrete Mathematics 5 (2010), 67–75; general nonequivariant sphere-or-contractible theorem.
