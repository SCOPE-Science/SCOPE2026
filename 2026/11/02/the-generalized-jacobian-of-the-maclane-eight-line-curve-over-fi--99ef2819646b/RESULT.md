# The generalized Jacobian of the MacLane eight-line curve over finite fields

## Finding
Let \(k=\mathbb F_q\) have characteristic different from \(3\), and put
\[
C:\quad (X^2+XY+Y^2)(Y^3-Z^3)(Z^3-X^3)=0\ \subset\ \mathbb P^2_k.
\]
Let \(J=\operatorname{Pic}^0_{C/k}\), the connected Picard group of the reduced, connected projective curve. Let \(C_m\) denote a cyclic group of order \(m\), and \((k,+)\) the additive group of the field. Then \(C\) has arithmetic genus \(21\), and the following are **isomorphisms of finite abelian groups**, not merely group-order identities:
\[
\boxed{J(k)\cong (k,+)^8\times C_{q-1}^{13}\quad (q\equiv1\pmod3),}
\]
\[
\boxed{J(k)\cong (k,+)^8\times C_{q+1}\times C_{q^2-1}^{6}\quad (q\equiv2\pmod3).}
\]
The maximal torus has dimension \(13\), and the unipotent part has dimension \(8\). In the nonsplit case the torus has an **integral**, Galois-equivariant character-lattice decomposition
\[
\mathbb Z_{-}\oplus\mathbb Z[\operatorname{Gal}(\mathbb F_{q^2}/\mathbb F_q)]^6,
\]
where \(\mathbb Z_{-}\) is the rank-one sign module. In particular the nonsplit torus is \(R^1_{\mathbb F_{q^2}/k}\mathbb G_m\times(R_{\mathbb F_{q^2}/k}\mathbb G_m)^6\), **up to isomorphism**, not just isogeny.

Additionally the zeta function of the underlying reduced curve is
\[
Z(C,T)=\begin{cases}
\dfrac{(1-T)^{12}}{(1-qT)^8},&q\equiv1\pmod3,\\[4pt]
\dfrac{(1-T^2)^7}{(1-T)^2(1-qT)^2(1-q^2T^2)^3},&q\equiv2\pmod3.
\end{cases}
\]
Thus \(\#C(\mathbb F_{q^n})=8q^n-12\) if \(q^n\equiv1\pmod3\), while \(\#C(\mathbb F_{q^n})=2q^n+2\) if \(q^n\equiv2\pmod3\).

## Assumptions and scope
The characteristic is any prime other than \(3\), including \(2\). The curve is the **reduced** degree-eight plane divisor specified by the displayed polynomial; no claim concerns its characteristic-three nonreduced specialization. A geometric component is a projective line. All computations of the integral graph use the eight lines over the quadratic splitting field \(k(\omega)\), where \(\omega^2+\omega+1=0\). For \(q\equiv2\pmod3\), \(k(\omega)=\mathbb F_{q^2}\); for \(q\equiv1\pmod3\), the eight lines are already defined over \(k\).

## Proof
**1. Stable geometric incidence.** Label the lines \(L_0,L_1\) by \(X-\omega Y\), \(X-\omega^2Y\); label \(L_2,L_3,L_4\) by \(Y-Z\), \(Y-\omega Z\), \(Y-\omega^2Z\); and \(L_5,L_6,L_7\) by \(Z-X\), \(Z-\omega X\), \(Z-\omega^2X\). Their coefficient vectors lie in \(\mathbb Z[\omega]^3\). Exact calculation of all \(\binom83=56\) determinants gives exactly eight zero determinants and forty-eight nonzero determinants of norm \(3\). For every residue characteristic different from \(3\), none of the nonzero determinants vanishes, and no two lines coincide. Consequently precisely eight points are ordinary triple points and the four remaining line pairs give ordinary double points. Their \(12\) point labels, specified as incident line subsets, are
\[
01,\ 027,\ 036,\ 045,\ 126,\ 135,\ 147,\ 234,\ 25,\ 37,\ 46,\ 567.
\]
Here, for example, \(027\) denotes the point on \(L_0,L_2,L_7\). The normalization \(\nu:\widetilde C\to C\) is the disjoint union of eight copies of \(\mathbb P^1\). Its \(12\) singular points have \(32\) geometric preimages, hence the bipartite incidence graph \(\Gamma\) has \(20\) vertices and \(32\) edges. Its first Betti number is \(32-20+1=13\). Each ordinary triple point contributes delta-invariant \(\binom32=3\), and each double point contributes \(1\). Thus \(p_a(C)=8\cdot3+4-8+1=21\), also equal to \((8-1)(8-2)/2\).

**2. Local multiplicative and additive parts.** At a transverse double point the unit quotient of the normalization by the local ring has a one-dimensional torus and no additive factor. At a transverse triple point, after an étale linear change of local coordinates, the completed equation is \(uv(u-v)=0\) (the same conclusion holds in characteristic \(2\)). The normalization has three formal branches. Matching the three constant terms imposes two independent multiplicative conditions; the images of linear forms on the three branches impose one additional first-order linear condition. Quadratic monomials already span all three second-order branch jets, so there are no further conditions. Accordingly the local quotient of normalization units has torus rank two and unipotent part \(\mathbb G_a\). Summing over eight triple points gives an eight-dimensional vector unipotent part \(U\) over the perfect field \(k\). The étale orbits of the triple points give additive Weil restrictions, so \(U(k)\cong(k,+)^8\). The component normalization contributes no Jacobian.

The gluing constants at the singular points, modulo changes of constant on individual components, give a torus \(T\) whose integral character (equivalently, cocharacter after dualizing) lattice is the rank-\(13\) cycle lattice \(H_1(\Gamma,\mathbb Z)\), with Frobenius acting through incidence permutations. This follows directly from the normalization exact sequence of sheaves of units. The connected Picard group is an extension of this torus by \(U\); over \(k\), \(H^1(k,U)=0\) and the finite groups \(U(k)\) and \(T(k)\) have coprime orders (a power of the characteristic versus a prime-to-characteristic number). Hence their exact sequence splits as finite abelian groups.

**3. Exact integral Frobenius module.** In the nonsplit case, conjugation \(\omega\mapsto\omega^2\) acts on the line labels by \((0\ 1)(3\ 4)(6\ 7)\), fixing \(2,5\). It therefore permutes the twelve point labels and the thirty-two incidence edges. Orient each graph edge from its line vertex to its singular-point vertex. A fixed spanning tree with edge indices \(0,1,2,3,4,5,6,7,8,9,10,11,14,17,20,23,25,27,29\) determines thirteen fundamental cycles \(e_0,\ldots,e_{12}\), ordered by the remaining edge indices \(12,13,15,16,18,19,21,22,24,26,28,30,31\). Let \(F\) denote the resulting integral Frobenius matrix. The exact certificate checks \(F^2=I\) and shows that the thirteen vectors
\[
(e_1,Fe_1,e_2,Fe_2,e_6,Fe_6,e_8,Fe_8,e_9,Fe_9,e_{11},Fe_{11},e_0)
\]
form a \(\mathbb Z\)-basis: the corresponding integer determinant is \(+1\). Moreover \(Fe_0=-e_0\) and Frobenius exchanges each of the six displayed pairs. Thus the lattice is *integrally* \(\mathbb Z_-\oplus\mathbb Z[\mathbb Z/2]^6\), establishing the asserted torus decomposition. For split Frobenius the full rank-thirteen lattice is fixed. The rational-point groups of the norm-one and induced tori are respectively \(C_{q+1}\) and \(C_{q^2-1}\), completing the group classification.

**4. Zeta calculation.** With \(v_d,p_d,b_d\) the orbit counts of size \(d\) on components, singular points, and normalization branches, respectively, finite-set gluing yields
\[
Z(C,T)=\prod_{d\ge1}\frac{(1-T^d)^{b_d-v_d-p_d}}{(1-q^dT^d)^{v_d}}.
\]
For split Frobenius there are \((v_1,p_1,b_1)=(8,12,32)\). For nonsplit Frobenius the counts at orbit sizes one and two are \((v_1,p_1,b_1)=(2,4,4)\) and \((v_2,p_2,b_2)=(3,4,14)\). Substitution proves both displayed zeta formulas and the point counts.

## Verification
Run `python3 verify.py` in the same directory. This is Python-standard-library-only exact arithmetic. It constructs the eight coefficient vectors over \(\mathbb Z[\omega]\), verifies all \(56\) triple determinants and their norm distribution, builds the entire incidence graph and its \(13\)-cycle integer basis, applies Frobenius to its \(32\) oriented edges, and checks the integral change-of-basis determinant using exact fraction-free elimination. It also verifies the orbit counts used for the zeta function and independently counts the projective rational points directly in the five prime fields of sizes 2, 5, 7, 11, and 13. The included `verification_output.txt` records `VERIFY_OK`. The local normalization-units calculation and Picard functor argument are mathematical proofs, not claims established merely by finite enumeration.

## Relationship to prior work
The MacLane matroid and its nonreal realizations are classical. Artal Bartolo–Florens–Guerville-Ballé explicitly treat the MacLane and extended MacLane arrangements, giving equations and topology; Malara–Pokora–Tutaj-Gasińska identify the eight-line case with a deletion of the Fermat arrangement and compute near-freeness. Geisser's general Picard-scheme theory characterizes toric and unipotent parts over perfect fields (with a later corrigendum to some separate assertions). These foundations do not themselves give the integral Frobenius lattice decomposition, arithmetic generalized-Jacobian group isomorphisms, or evaluated two-case curve zeta functions here. The computation is a specialized explicit application of classical normalization/Picard theory, not a new general Picard-structure theorem.

## Limitations
The claim is confined to the given reduced projective plane curve and excludes characteristic \(3\). No claim is made that its combinatorics or near-freeness is new. The computed abelian groups are groups of \(\mathbb F_q\)-rational points, and their p-primary factors are field-additive groups rather than necessarily cyclic factors. The zeta function of a reduced curve does not determine its unipotent Picard structure; that structure is supplied separately by the local ring calculation. Historical priority for this explicit specialization remains subject to independent literature review.

## References
1. E. Artal Bartolo, V. Florens, and B. Guerville-Ballé, *A topological invariant of line arrangements*, arXiv:1407.3387v1 (12 July 2014), sections 1 and 5, https://arxiv.org/abs/1407.3387.
2. T. Geisser, *The affine part of the Picard scheme*, arXiv:0704.0479 (4 April 2007), *Compositio Mathematica* 145 (2009), 415–422, https://doi.org/10.1112/S0010437X08003710; and corrigendum, *Compositio Mathematica* 157 (2021), 2338–2340, https://doi.org/10.1112/S0010437X21007612.
3. G. Malara, P. Pokora, and H. Tutaj-Gasińska, *On 3-syzygy and unexpected plane curves*, *Geometriae Dedicata* 214 (2021), 49–63, sections 2 and 6, https://doi.org/10.1007/s10711-021-00602-5.
4. S. MacLane, *Some Interpretations of Abstract Linear Dependence in Terms of Projective Geometry*, *American Journal of Mathematics* 58 (1936), 236–240 (historical reference; complete text not inspected).
