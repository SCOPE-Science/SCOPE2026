# Toric isomorphism classes and the unique symmetry jump in a canonical tensor-generating threefold family

## Finding
Let \(X_a\), for each integer \(a\), be the smooth complete toric threefold \(Z''_{13}(a,2,a+2,a+1)\) defined in Ito–Zeng–Zeng. Then for all integers \(a,b\),
\[
X_a\cong_{\mathrm{toric}}X_b\quad\Longleftrightarrow\quad b=a\ \text{or}\ b=-a-4.
\]
Consequently the family has infinitely many distinct toric isomorphism classes, represented uniquely by integers \(a\geq-2\). The group of lattice automorphisms preserving the fan of \(X_a\) is trivial except at \(a=-2\), where it has order two. This is a classification of toric isomorphisms, not a separately proved classification of unmarked abstract-variety isomorphisms. The canonical tensor-generation and nonprojectivity of these threefolds are prior results, not claims established here.

## Assumptions and scope
Work over \(\mathbb C\). For \(a\in\mathbb Z\), the primitive ray generators are
\[
\begin{aligned}
v_1&=(1,1,2),&v_2&=(1,0,0),&v_3&=(0,-1,0),&v_4&=(0,0,-1),\\
v_5&=(-1,a,a+1),&v_6&=(0,1,0),&v_7&=(0,0,1),&v_8&=(-1,a+2,a+2).
\end{aligned}
\]
The maximal cones, with \(ijk\) denoting the cone on rays \(i,j,k\), are \(124,234,345,456,146,167,127,237,358,568,378,678\). They specify the published smooth complete fan. A toric isomorphism is an isomorphism respecting the dense torus action, up to a torus isomorphism; it therefore induces a unimodular lattice map of these fans.

## Proof
Any toric isomorphism induces a permutation of the eight rays preserving the set of twelve maximal cones. Enumerating the \(8!\) permutations and testing the unordered cone triples gives exactly eight combinatorial automorphisms. To determine which lift to lattice isomorphisms between the fans of \(X_a\) and \(X_b\), take the basis \(v_1,v_2,v_4\), whose determinant is \(\pm1\). For a candidate permutation \(h\), the lattice map is uniquely forced:
\[
U_h=[v_{h(1)}(b)\;v_{h(2)}(b)\;v_{h(4)}(b)]
[v_1(a)\;v_2(a)\;v_4(a)]^{-1}.
\]
The necessary and sufficient conditions are the 24 scalar equations \(U_hv_i(a)=v_{h(i)}(b)\), for \(1\leq i\leq8\). Computing their exact polynomial ideals in \(\mathbb Z[a,b]\) or \(\mathbb Q[a,b]\) yields only two consistent candidates. The identity \(h=(1,2,3,4,5,6,7,8)\) forces \(a-b=0\). The permutation \(h=(5,8,7,6,1,4,3,2)\) forces \(a+b+4=0\). Each of the other six permutations gives the unit ideal and can never lift, even over \(\mathbb C\).

For the second permissible permutation, the map is explicitly
\[
U_a=\begin{pmatrix}-1&0&0\\-a-2&0&-1\\-a-2&-1&0\end{pmatrix},\qquad \det U_a=1.
\]
Direct substitution sends each source ray to its permuted target ray of parameter \(-a-4\), and preservation of maximal cones was already checked. Moreover \(U_{-a-4}U_a=I\). Thus these conditions are sufficient as well as necessary. A self-isomorphism requires \(b=a\); the second candidate then occurs exactly when \(a=-2\). At this parameter the identity and the nonidentity reflection are the only two fan automorphisms. Every equivalence class \(\{a,-a-4\}\) has exactly one representative satisfying \(a\geq -2\).

## Verification
The standalone program `verify_fan_isomorphism.py` enumerates all \(40320\) ray permutations, verifies the twelve maximal cones, solves each candidate's exact ray equations over \(\mathbb Q[a,b]\) using Gröbner bases, and verifies the explicit unimodular involution. Run `python verify_fan_isomorphism.py` with SymPy installed. Its expected terminal message begins `VERIFY_OK`. This is an exhaustive finite combinatorial calculation for each symbolic integer parameter, not a finite parameter sample.

## Relationship to prior work
Ito, M. R. Zeng and X. Zeng, arXiv:2610.22279v1, Theorem 6.3, introduce the whole family \(X_a\) and prove that its canonical bundles tensor-generate on smooth nonprojective complete toric threefolds. Their theorem does not classify repetitions among its integer parameters or its fan symmetry groups. Fujino and Sato, arXiv:2412.02392v2, Section 4, [8-13''], describe the full four-parameter fan and associated toric flips and nonprojectivity, but do not provide this pairwise isomorphism test. Our calculation compares induced lattice maps, not merely names of families, and classifies a distinct parameter-identification question.

## Limitations
The classification concerns toric isomorphisms and automorphisms of fans; it does not assert the complete abstract automorphism group, derived equivalence classes or all isomorphisms after forgetting the torus structure. It relies on the published fan description and does not reprove the published tensor-generation theorem. Absence of a matching result in searched sources is not a proof of priority; an earlier equivalent parameter classification could be implicit in less accessible toric literature. Independent mathematical validation has not been performed.

## References
1. D. Ito, M. R. Zeng, X. Zeng, *Tensor-generating line bundles on toric varieties*, arXiv:2610.22279v1 (first posted 2026-10-15), Theorem 6.3 and Section 6.1. https://arxiv.org/html/2610.22279v1
2. O. Fujino, H. Sato, *On non-projective complete toric varieties*, arXiv:2412.02392v2, Section 4 [8-13''], https://arxiv.org/pdf/2412.02392
