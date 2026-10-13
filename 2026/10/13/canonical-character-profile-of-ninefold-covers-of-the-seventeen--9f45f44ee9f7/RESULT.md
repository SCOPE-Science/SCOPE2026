# Canonical character profile of ninefold covers of the seventeen-cusp quintic family

## Finding
Let \(S\subset\mathbb P^3_{\mathbb C}\) be a normal quintic surface with exactly seventeen isolated \(A_2\) singularities. Suppose two independent ternary cusp-code words have supports of size twelve meeting in seven positions. Then there is a connected smooth projective Galois cover
\[
f:X\longrightarrow S,\qquad G\cong(\mathbb Z/3)^2,
\]
of degree nine that is étale over the smooth locus. Exactly three smooth points lie over each cusp. Among the four order-three subgroups of \(G\), three have precisely fifteen fixed points and the fourth has precisely six fixed points.

The canonical bundle is ample and
\[
(K_X^2,c_2(X),\chi(\mathcal O_X),q(X),p_g(X))=(45,87,11,0,10).
\]
As a complex representation of \(G\), the canonical space \(H^0(X,K_X)\) has a four-dimensional trivial isotypic component, six distinct one-dimensional nontrivial character components, and two missing nontrivial character components. Hence the map \(X\to S\subset\mathbb P^3\) is **not** the complete canonical morphism. Borisov--Rito's six-dimensional family of double-Barth--Rams quintics satisfies these hypotheses at its general seventeen-cusp member [1].

## Assumptions and scope
The base field is \(\mathbb C\). An ordinary surface cusp means the rational double point \(A_2\), analytically the quotient \(\mathbb A^2/\mu_3\) where a generator acts on tangent coordinates by \((\zeta,\zeta^2)\). Write \(\rho:\widetilde S\to S\) for the minimal resolution with exceptional chains \(E'_i\cup E''_i\) for \(1\le i\le17\). A ternary cusp-code word is a vector \(c=(c_i)\in\mathbb F_3^{17}\) for which the class of \(\sum_i c_i(2E'_i+E''_i)\) vanishes in \(H^2(\widetilde S,\mathbb F_3)\). For these quintics the cohomological condition is equivalent to divisibility by three of an integral exceptional divisor class [1,2]. Its weight is the number of nonzero coordinates. The two stipulated supports have intersection seven and union seventeen. All statements concern this precise class, not all seventeen-cusp quintics.

## Proof
**1. The code and local inertia.** The two words are independent because their distinct supports both have size twelve. By Tan's cusp-weight theorem [2], a nonzero word on a quintic has weight twelve, fifteen, or eighteen; length seventeen excludes the last. The Griesmer inequality excludes a three-dimensional ternary code of minimum weight twelve because \(12+4+2=18>17\). Thus the code has dimension exactly two. On the seven common positions, let \(t\) count the places where the two generator coordinates agree. Their sum and difference have weights \(10+t\) and \(17-t\). The only allowable pair is \((12,15)\) in some order, so the weight enumerator is \(1+6z^{12}+2z^{15}\).

**2. Connected simultaneous cover.** Put \(U=S_{\mathrm{reg}}\). For any codeword \(c\) take a divisor class \(L_c\) on \(\widetilde S\) with \(3L_c\sim\sum_i c_i(2E'_i+E''_i)\), using integral representatives of the coefficients. Its restriction to \(U\) has order dividing three. A nonzero word gives a nontrivial restriction: if the restriction were trivial, \(L_c\) would be linearly equivalent to an integral exceptional divisor \(E\). Then the exceptional divisor \(\sum_i c_i(2E'_i+E''_i)-3E\) would be principal. Its defining rational function is a unit on \(U\), hence constant, because a regular function on \(U\) extends over the finitely many deleted points of the normal projective surface \(S\); the exceptional coefficients would have to be divisible by three, impossible at a nonzero coordinate. The two words therefore yield independent elements of \(\operatorname{Pic}(U)[3]\). Since \(\Gamma(U,\mathcal O_U^*)=\mathbb C^*\) and every complex constant has a cube root, Kummer theory gives independent \(\mu_3\)-torsors with connected fiber product \(V\to U\) of degree nine and deck group \(G\).

Normalize \(S\) in \(\mathbb C(V)\), obtaining \(f:X\to S\). At an \(A_2\) cusp, the two local characters are the corresponding two code coordinates. They are not both zero, because the supports cover all seventeen cusps. Local monodromy therefore has image of order three in \(G\). The local normalization of the degree-nine covering is consequently the disjoint union of three copies of the universal local \(\mu_3\)-cover \(\mathbb A^2\to\mathbb A^2/\mu_3\). Every point of \(X\) is smooth, and exactly three lie above each cusp. Finiteness over projective \(S\) makes \(X\) projective.

**3. Fixed points.** Each cusp has a nontrivial inertia line \(I_i\le G\) of order three. For a nontrivial character \(\lambda\) with kernel \(H\le G\), the number of cusps whose inertia lies in \(H\) equals \(17-\operatorname{wt}(\lambda)\). The four character-kernel lines correspond to three projective codewords of weight twelve and one of weight fifteen, so their cusp counts are \(5,5,5,2\). Every such cusp contributes three fixed points of each nonidentity element of its inertia line and there are no other fixed points. Thus the four subgroup fixed-point counts are \(15,15,15,6\). Tangent weights at any fixed point are \((1,2)\) modulo three.

**4. Chern and Hodge numbers.** Adjunction gives \(K_S\cong\mathcal O_S(1)\). The cover is unramified in codimension one, hence \(K_X=f^*\mathcal O_S(1)\), which is ample, and \(K_X^2=9\cdot5=45\). The minimal resolution of a quintic with only rational double points has \(\chi(\mathcal O_{\widetilde S})=5\) and \(K_{\widetilde S}^2=5\). Noether's formula gives \(e(\widetilde S)=55\). Each exceptional \(A_2\) chain has Euler number three, so \(e(U)=55-17\cdot3=4\). Since \(V\to U\) is étale of degree nine and the cusp fibers each comprise three points,
\[
e(X)=9\cdot4+17\cdot3=87,\qquad
\chi(\mathcal O_X)=(45+87)/12=11.
\]
For every order-three subgroup \(H\), the intermediate surface \(X/H\to S\) is a cyclic triple cover ramified over precisely twelve or fifteen cusps. Any singularities above the remaining cusps are rational double points. Tan's classification [2, Theorem 4.3.1] says that the minimal resolution of either kind of triple cover has irregularity zero. Thus \(H^1(X,\mathcal O_X)^H\cong H^1(X/H,\mathcal O_{X/H})=0\) for every order-three \(H\). Every character of \(G\) is trivial on some such \(H\); consequently \(H^1(X,\mathcal O_X)=0\). Therefore \(q(X)=0\) and \(p_g(X)=\chi(\mathcal O_X)-1=10\).

**5. Canonical character decomposition.** For \(g\ne1\), each fixed point contributes \(1/((1-\zeta)(1-\zeta^2))=1/3\) to the holomorphic Lefschetz number of \(\mathcal O_X\). For the three order-three lines with fifteen fixed points the number is five, and for the fourth line it is two. The identity Lefschetz number is eleven. Fourier inversion on \(G\) gives multiplicity five of the trivial character in the virtual \(\sum_i(-1)^iH^i(X,\mathcal O_X)\). For a nontrivial character whose kernel line has \(m\) cusps, the multiplicity is \((m-2)/3\), namely one if \(m=5\) and zero if \(m=2\). Since \(H^1(X,\mathcal O_X)=0\) and \(H^0(X,\mathcal O_X)\) is one-dimensional and trivial, the representation \(H^2(X,\mathcal O_X)\) has four trivial dimensions, six one-dimensional nontrivial components, and two absent characters. Serre duality yields the same multiplicities for \(H^0(X,K_X)\), with characters inverted (the multiplicity pattern is invariant under inversion). The full canonical system is nine-dimensional projectively, whereas the composite \(X\to S\subset\mathbb P^3\) uses only the four invariant canonical sections.

## Verification
Run \(`python3 verify_cusp_cover.py`\) with Python 3 and its standard library. It checks the stated two-word support pattern, the entire nine-word ternary code, the four inertia-block sizes, the subgroup fixed-point counts, the Chern-number arithmetic, and the exact integral Fourier multiplicities. The program prints `CUSP_NINEFOLD_CHARACTER_AND_CHERN_CHECK_OK`. The universal existence and smoothness of the algebraic covering are mathematical steps 2--4 above, not consequences of this finite computation.

## Relationship to prior work
Borisov--Rito [1, Section 5] prove the six-dimensional family of seventeen-cusp quintics with two distinct twelve-cusp Barth--Rams decompositions intersecting in seven cusps. They do not give the corresponding **simultaneous smooth degree-nine cover or its full fixed-point, Chern and canonical-character profile**. Tan [2, Sections 3--4] proves the general single-cyclic-triple-cover formulas, including irregularity zero for twelve- and fifteen-cusp covers; those published ingredients are used explicitly here. Rito [3, Sections 1 and 6] studies degree-three canonical covers of fifteen-cusp quintics and a separate isolated seventeen-cusp example, not the specified simultaneous degree-nine cover. The theorem concerns a specific recently constructed six-dimensional family and does not change any of these earlier statements.

## Limitations
The cover's explicit defining equations are not supplied, and uniqueness among all connected non-abelian or higher-degree coverings is not asserted. The result does not determine the degree of the complete canonical map onto its image or the topological fundamental group of \(X\). Tan's earlier cyclic-cover theorem and standard Kummer/holomorphic-Lefschetz formalisms are substantial established inputs; the contribution is the simultaneous geometric and representation-theoretic classification for the double-decomposition family.

## References
[1] Lev Borisov and Carlos Rito, *Quintic surfaces with 18 cusps*, arXiv:2608.12305v1 (12 August 2026), Sections 1, 2, 3 and 5. https://arxiv.org/abs/2608.12305

[2] Sheng-Li Tan, *Cusps on some algebraic surfaces and plane curves*, in *Complex Analysis, Complex Geometry and Related Topics—Namba 60*, 2003, 106–121, Sections 3.1, 3.2 and 4.3. https://math.ecnu.edu.cn/~sltan/tan-cusp.pdf

[3] Carlos Rito, *Cuspidal quintics and surfaces with geometric genus zero, canonical square three and five-torsion*, *LMS Journal of Computation and Mathematics* 19 (2016), 42–53, DOI: 10.1112/S1461157015000315. https://doi.org/10.1112/S1461157015000315
