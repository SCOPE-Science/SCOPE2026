# Projective stabilizers of the Klein-quartic four-bitangent Zariski triple
## Finding
For the Klein quartic
\[
Q:T^3X+X^3Z+TZ^3=0
\]
and the seven bitangent lines \(L_1,\ldots,L_7\) used by Bannai--Tokunaga--Yamamoto, define
\[
I_1=\{1,2,3,5\},\qquad I_2=\{1,2,3,6\},\qquad I_3=\{1,2,4,7\},
\]
and
\[
B_k=Q+\sum_{i\in I_k}L_i.
\]
These are the three explicit arrangements used in their four-bitangent Zariski triple. Their full projective stabilizers are
\[
\operatorname{Aut}_{\mathbb P^2}(B_1)\cong S_3,\qquad
\operatorname{Aut}_{\mathbb P^2}(B_2)=\operatorname{Aut}_{\mathbb P^2}(B_3)=1.
\]
For \(B_1\), the six automorphisms fix \(L_2\) and induce all six permutations of \(\{L_1,L_3,L_5\}\). Consequently, under the full projective automorphism group of \(Q\), the three marked four-bitangent subsets have orbit sizes
\[
28,\qquad 168,\qquad 168.
\]

## Assumptions and scope
Work is over \(\mathbb C\). Coordinates are \([T:X:Z]\), and \(\zeta\) is a primitive seventh root of unity. The line labels are exactly those of the source:
\[
L_1=L_{0,0},\ L_2=L_{1,0},\ L_3=L_{1,1},\ L_4=L_{3,3},\ L_5=L_{1,6},\ L_6=L_{3,4},\ L_7=L_{2,5}.
\]
The statement concerns projective automorphisms of the displayed reducible plane curves. It does not classify stabilizers for every four-subset of the \(28\) bitangents, nor does it classify all members of the corresponding deformation classes.

## Proof
A projective automorphism of any \(B_k\) must preserve \(Q\), because \(Q\) is the unique irreducible component of degree \(4\); it must also permute the four line components. Thus
\[
\operatorname{Aut}_{\mathbb P^2}(B_k)
=\operatorname{Stab}_{\operatorname{Aut}_{\mathbb P^2}(Q)}\bigl(\{L_i:i\in I_k\}\bigr).
\]

Use the three projective matrices
\[
S=\begin{pmatrix}\zeta&0&0\\0&\zeta^4&0\\0&0&\zeta^2\end{pmatrix},\qquad
T=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix},
\]
and
\[
U=\begin{pmatrix}a&b&c\\b&c&a\\c&a&b\end{pmatrix},
\qquad
a=\zeta-\zeta^6,\quad b=\zeta^2-\zeta^5,\quad c=\zeta^4-\zeta^3.
\]
Exact substitution shows that each matrix preserves the quartic equation up to a nonzero scalar. Exact projective closure under \(S,T,U\) produces \(168\) distinct elements. Since a smooth complex curve of genus \(3\) has at most \(84(3-1)=168\) automorphisms by the Hurwitz bound, these matrices generate the full projective automorphism group of \(Q\).

The source writes all \(28\) bitangents in four families \(L_{r,j}\), with \(0\le r\le3\) and \(0\le j\le6\). Substituting those exact equations into the contragredient action of the \(168\) matrices gives a faithful permutation action on all \(28\) bitangents. Exhaustive exact stabilizer computation for the three source subsets gives sizes
\[
6,\qquad1,\qquad1.
\]
For the first subset, the six induced permutations fix \(L_2\), act faithfully on \(\{L_1,L_3,L_5\}\), and have element-order profile
\[
1\text{ element of order }1,\qquad3\text{ of order }2,\qquad2\text{ of order }3.
\]
Hence that stabilizer is \(S_3\). The other two stabilizers are trivial. Orbit--stabilizer then gives orbit sizes \(168/6=28\), \(168\), and \(168\).

## Verification
The standalone file `verify.py` performs exact arithmetic in \(\mathbb Q(\zeta_7)\). It checks, without floating-point arithmetic, all of the following: the three generating matrices preserve \(Q\); their projective closure has \(168\) elements; the source formulas give \(28\) distinct lines; all \(168\) transformations permute those lines; the three setwise stabilizers have orders \(6,1,1\); the first stabilizer fixes \(L_2\), realizes all six permutations of \(\{L_1,L_3,L_5\}\), and has the stated order profile; and the orbit sizes are \(28,168,168\). A successful replay ends with `VERIFY_OK`.

## Relationship to prior work
Bannai--Tokunaga--Yamamoto exhibit this Klein-quartic configuration and prove that the three arrangements form a Zariski triple by connected-number data. Their paper gives the explicit bitangent equations and the three four-subsets but does not determine their projective stabilizers. Bannai--Ohno subsequently recast the embedded-topology distinction using two-graphs; the relevant material studies topological/two-graph equivalence rather than projective stabilizer groups. The present calculation refines the same canonical representatives at the quotient-by-projectivities level: one representative has a nontrivial \(S_3\) stabilizer, while the other two are projectively rigid.

## Limitations
The computation is specific to the three displayed Klein-quartic representatives and uses characteristic \(0\). It does not assert that every arrangement in the same topological component has the same projective stabilizer. The originality comparison found no covering statement in the inspected source, its direct two-graph follow-up, targeted literature searches, or the checked research database; an equivalent stabilizer computation could nevertheless exist in older finite-geometry literature on the Klein quartic and its \(28\) bitangents.

## References
1. S. Bannai, H. Tokunaga, M. Yamamoto, *A note on the topology of arrangements for a smooth plane quartic and its bitangent lines*, arXiv:1806.02982v1; Hiroshima Math. J. \(49\) (2019), 289--302, doi:10.32917/hmj/1564106549.
2. S. Bannai, M. Ohno, *Two-graphs and the Embedded Topology of Smooth Quartics and its Bitangent Lines*, Canad. Math. Bull. \(63\) (2020), 802--812, doi:10.4153/S0008439520000053.
3. N. D. Elkies, *The Klein Quartic in Number Theory*, in *The Eightfold Way: The Beauty of Klein's Quartic Curve*, MSRI Publications \(35\), Cambridge University Press, 1999, pp. 51--102.
