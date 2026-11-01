# Integral Rips persistence and symmetry characters of type-\(A\) root sets

## Finding
For every integer \(n\ge4\), let
\[
R_n=\{e_i-e_j:1\le i,j\le n,\ i\ne j\}\subset\mathbb R^n
\]
with the unrescaled Euclidean distance, and let \(K_r=\operatorname{VR}_{\le r}(R_n)\) be the inclusive Vietoris–Rips complex at scale \(r\ge0\). Put \(N=\binom n2\) and \(b=n^2-3n+1\). Then the complete homotopy classification is
\[
K_r\simeq\begin{cases}
\bigvee^{n(n-1)-1}S^0,&0\le r<\sqrt2,\\
\bigvee^{b}S^1,&\sqrt2\le r<2,\\
S^{n-2},&2\le r<\sqrt6,\\
S^{N-1},&\sqrt6\le r<2\sqrt2,\\
\ast,&r\ge2\sqrt2.
\end{cases}
\]
In particular, for any coefficient field the complete reduced persistence barcode consists of \(n(n-1)-1\) degree-zero bars \([0,\sqrt2)\), \(b\) degree-one bars \([\sqrt2,2)\), one degree-\(n-2\) bar \([2,\sqrt6)\), and one degree-\(N-1\) bar \([\sqrt6,2\sqrt2)\); there are no other bars. All integral homology groups at all scales are free, and the same interval descriptions hold for reduced integral persistence modules.

The natural simultaneous coordinate-permutation action of \(S_n\) has the following rational reduced-homology representations on all nonzero reduced-homology stages:
\[
\begin{array}{c|c|c}
\text{scale interval}&\text{degree}&S_n\text{-module}\\\hline
[0,\sqrt2)&0&\mathbb Q[\{(i,j):i\ne j\}]/\mathbf1\\
[\sqrt2,2)&1&S^{(n-2,2)}\oplus S^{(n-2,1,1)}\\
[2,\sqrt6)&n-2&\operatorname{sgn}\\
[\sqrt6,2\sqrt2)&N-1&\operatorname{sgn}^{n-1}.
\end{array}
\]
Consequently, at every scale the quotient \(|K_r|/S_n\) is rationally acyclic in reduced homology except when \(n\) is odd and \(\sqrt6\le r<2\sqrt2\). In that case it has one-dimensional reduced rational homology in degree \(N-1\) and no other reduced rational homology.

## Assumptions and scope
The coordinate vectors \(e_i\) are the standard orthonormal basis; no normalization to unit-length roots is performed. A nonempty finite set of roots is a simplex exactly when the Euclidean distances between all of its pairs are \(\le r\). The action of \(S_n\) permutes coordinates; representations are over \(\mathbb Q\), while the stated homotopy and integral homology conclusions use the ordinary geometric realizations. The lower bound \(n\ge4\) ensures the three positive homology degrees are distinct, so the persistence interval calculation does not require a nontrivial same-degree inclusion-map calculation. The Specht modules use their ordinary rational characteristic-zero meaning.

## Proof
**1. Exact distance spectrum.** For \(a_{ij}=e_i-e_j\), distinct roots satisfy
\[
\lVert a_{ij}-a_{kl}\rVert^2=4-2(\delta_{ik}-\delta_{il}-\delta_{jk}+\delta_{jl}).
\]
The inner product is \(1\) precisely when the two roots have the same source or the same target, \(-2\) precisely when they are antipodal, \(-1\) precisely for a directed two-step configuration, and \(0\) otherwise. Every case occurs for \(n\ge4\), yielding squared distances \(2,4,6,8\). There are exactly \(n(n-1)\) vertices and \(N\) antipodal pairs.

**2. The \(\sqrt2\) stage.** Here two different roots are adjacent exactly when their first coordinates agree or their second coordinates agree. Every clique with at least two vertices is contained in one of the \(n\) source-row simplices or \(n\) target-column simplices. Any two distinct row simplices are disjoint, as are distinct column simplices; row \(i\) meets column \(j\) in one root when \(i\ne j\) and otherwise not at all. Thus the nerve of this cover by contractible simplices is the crown graph with bipartition size \(n+n\) and all edges except the \(n\) diagonal ones. It is connected with cycle rank \(n(n-1)-2n+1=b\). The simplicial nerve lemma gives \(K_{\sqrt2}\simeq\bigvee^bS^1\). For the \(S_n\)-module on \(H_1\), the equivariant nerve chain sequence gives, in the rational representation ring,
\[
[H_1]=[\mathbb Q\{(i,j):i\ne j\}]-2[\mathbb Q^n]+[\mathbf1]
=[S^{(n-2,2)}]+[S^{(n-2,1,1)}].
\]
The last equality follows from the standard decomposition of the permutation module on ordered distinct pairs. Equivalently, if \(\sigma\in S_n\) fixes \(f\) labels, its trace on this first homology is \(f^2-3f+1\).

**3. The \(2\) stage and an equivariant structural equivalence.** A set \(F\) of directed roots is a face at this scale if and only if no label occurs in \(F\) both as a source and as a target; equivalently, \(F\subseteq A\times B\) for some nonempty disjoint subsets \(A,B\subseteq[n]\). Let \(P\) be the poset of nonempty faces \(F\) ordered by inclusion, and \(Q\) the poset of nonempty ordered disjoint pairs \((A,B)\), ordered componentwise. There are \(S_n\)-equivariant order maps
\[
\Phi(F)=(\operatorname{src}F,\operatorname{tgt}F),\qquad
\Psi(A,B)=A\times B.
\]
They obey \(\Phi\Psi=\operatorname{id}_Q\), \(\Psi\Phi(F)\supseteq F\), and \(\Psi\Phi\) is an idempotent closure map. The standard order-homotopy argument provides an \(S_n\)-equivariant homotopy equivalence of their order complexes. The order complex of \(P\) is the barycentric subdivision of \(K_2\), and \(Q\) is the face poset of the polyhedral graph-homomorphism complex \(\operatorname{Hom}(K_2,K_n)\). This proves an equivariant equivalence, not merely a coincidence of Betti numbers.

Moreover, a cell \(\Delta_A\times\Delta_B\) of \(\operatorname{Hom}(K_2,K_n)\) maps by \((p,q)\mapsto p-q\) linearly and bijectively to the corresponding orthant cell of
\[
\Sigma_n=\{x\in\mathbb R^n:\textstyle\sum_i x_i=0,\ \sum_i|x_i|=2\}.
\]
The positive and negative supports of a nonzero \(x\in\Sigma_n\) uniquely recover \(A,B\), \(p\), and \(q\), so the assembled map is a continuous \(S_n\)-equivariant homeomorphism. Radial projection identifies \(\Sigma_n\) with the unit sphere of the \((n-1)\)-dimensional standard real \(S_n\)-representation. Hence \(K_2\simeq_{S_n}S^{n-2}\), and the top homology character is its orientation character \(\operatorname{sgn}\).

**4. The \(\sqrt6\) stage.** The only excluded edges are the antipodal pairs \(\{a_{ij},a_{ji}\}\), one for each unordered \(\{i,j\}\). Hence \(K_{\sqrt6}\) is exactly the join of \(N\) two-point complexes, homeomorphic to \(S^{N-1}\). The action on the \(N\) signed one-dimensional factors is the exterior-square representation \(\bigwedge^2\mathbb R^n\) (identify its axis \(\{i,j\}\) with \(e_i\wedge e_j\)). The induced action on top homology is its determinant,
\[
\det\big(\bigwedge^2\sigma\big)=(\det\sigma)^{n-1}=\operatorname{sgn}(\sigma)^{n-1}.
\]
At \(r\ge2\sqrt2\), all edges are present, so the complex is the full simplex and is contractible. For \(r<\sqrt2\), it consists of isolated vertices; the reduced zero-dimensional group is the augmentation quotient of the natural permutation module on ordered distinct pairs, as in the table. This proves the homotopy and representation assertions.

**5. Persistence and quotients.** The positive homology degrees in the three nontrivial stages are \(1\), \(n-2\), and \(N-1\), strictly increasing for \(n\ge4\); therefore each class dies at the next critical scale. The zero-dimensional reduced classes die upon connectedness at \(\sqrt2\). The homotopy descriptions imply torsion-free integral homology and the stated interval modules. For every finite group action on a finite simplicial complex, rational homology of the geometric quotient is the invariant part of rational homology (after equivariant barycentric subdivision, via chain averaging). The stage-one representation has no trivial Specht summand; the stage-two sign character is nontrivial; and the stage-three character is trivial precisely for odd \(n\). The rational quotient assertion follows.

## Verification
The companion `verify_type_a_rips.py` is a self-contained Python 3 program using exact integer distances, finite simplex enumeration, mod-two boundary reduction, and oriented fixed-simplex Lefschetz traces. It constructs all stage-one and stage-two simplices for \(n=4,5,6\) and compares Betti numbers with the theorem; for every element of \(S_4\) and \(S_5\), it compares the signed fixed-simplex Lefschetz number to the predicted homological character. It independently checks the antipodal-pair stage structure. The recorded output is in `verification_output.txt` and ends in `TYPE_A_RIPS_CHECKS_OK`. These finite checks are auxiliary consistency tests; the quantified all-\(n\) statements are established by the structural proof above, not extrapolation.

## Relationship to prior work
Babson and Kozlov's *Complexes of graph homomorphisms* (arXiv:math/0310056, first public 2003-10-05), Section 4, establishes the known complete-graph Hom topology that appears at the middle stage. The present claim does **not** attribute novelty to the sphere homotopy type of \(\operatorname{Hom}(K_2,K_n)\). Ayzenberg, Beketov, and Magai's *Coverings by open and closed hemispheres* (arXiv:2310.02827), particularly Proposition 1.1 and Section 3, studies the same type-\(A\) root point set but the strictly larger simplicial complex of all directed acyclic graphs and an unrelated large closed-hemisphere nerve. Their DAG complex includes directed paths of length two, which the scale-\(2\) Rips stage excludes. Their sphere conclusion therefore does not determine this Rips filtration or its stage-one and stage-three representations. Saleh, Titz Mite, and Witzel's *Vietoris–Rips complexes of Platonic solids* (arXiv:2302.14388) handles the five Platonic solids, not this general type-\(A\) series. A publicly available calculation titled *Complete Vietoris–Rips filtration of the Euclidean cuboctahedron* (research-record identifier `c10ad684de7e`) describes the exact \(n=4\) instance, which is not presented as independently new. The contribution here is the structural classification and its equivariant and quotient consequences for **all \(n\ge4\)**. These comparisons do not prove absence of differently indexed equivalent results.

## Limitations
This theorem is specific to the finite unrescaled Euclidean type-\(A\) root set, not its graph-shortest-path metric, entire root polytope, other root systems, or \(n=3\), where homology degrees can coincide. The quotient statement is about reduced **rational homology**, not integral quotient torsion or quotient homotopy types. The integral persistence statement follows from the uniform homotopy stages and distinct positive homology degrees, not an independently computed all-parameter Smith form. Bibliographic priority remains subject to later independent verification. Independent mathematical audit has not been performed.

## References
1. E. Babson and D. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056 (first public 2003-10-05), https://arxiv.org/abs/math/0310056.
2. A. Ayzenberg, M. Beketov, and G. Magai, *Coverings by open and closed hemispheres*, arXiv:2310.02827 (first public 2023-10-04), https://arxiv.org/abs/2310.02827.
3. N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388 (first public 2023-02-28), https://arxiv.org/abs/2302.14388.
4. *Complete Vietoris–Rips filtration of the Euclidean cuboctahedron*, public research record `c10ad684de7e` (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-complete-vietoris-rips-filtration-of-the-euclidean-cuboctahedron--c10ad684de7e.
