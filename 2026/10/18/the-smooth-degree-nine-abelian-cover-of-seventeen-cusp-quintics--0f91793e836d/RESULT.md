# The smooth degree-nine abelian cover of seventeen-cusp quintics

## Finding
Let \(S\subset\mathbb P^3_{\mathbb C}\) be a normal quintic surface whose singular set consists of exactly 17 ordinary cusps (rational double points of type \(A_2\)). Assume there are two three-divisible 12-element subsets \(A,B\) of the cusp set with \(|A\cap B|=7\). Then:

1. The complete ternary cusp code \(C(S)\) is a \([17,2,12]_3\) linear code with weight enumerator \(W(z)=1+6z^{12}+2z^{15}\). Its distinct nonempty supports comprise three 12-cusp sets (pairwise intersection seven, triple intersection two) and one 15-cusp set. The cusp labels partition into four blocks of cardinalities \(2,5,5,5\), with the 12-cusp sets consisting of the first block and two of the remaining blocks.
2. For \(U=S_{\mathrm{sm}}\), the entire abelianization is \(H_1(U,\mathbb Z)\cong(\mathbb Z/3)^2\), and each singular-point meridian has nonzero image. The associated connected maximal finite abelian unramified covering \(U'\to U\) has degree nine.
3. Its normalization \(f:Y\to S\) is a *smooth* finite quasi-étale Galois map of degree nine, with group \((\mathbb Z/3)^2\). The source \(Y\) is a canonically polarized minimal surface of general type, with
\[
K_Y^2=45,\quad e(Y)=87,\quad \chi(\mathcal O_Y)=11,\quad q(Y)=0,\quad p_g(Y)=10.
\]
4. The three distinct 12-cusp supports and the 15-cusp support correspond to exactly four intermediate connected cyclic triple normal covers of \(S\). In particular, the third 12-cusp subset is forced even though only two contact-cubic decompositions are part of the hypotheses.

The hypotheses hold for every general member of the six-dimensional 17-cusp double-decomposition component constructed by Borisov and Rito in 2026 [1, Section 5].

## Assumptions and scope
All spaces and (co)homology groups are over \(\mathbb C\), and integral singular (co)homology is meant unless otherwise specified. An ordinary cusp is a surface singularity analytically equivalent to \(xy=z^3\), or to the quotient \(\mathbb C^2/\mu_3\) with weights \((1,2)\). Write \(\pi:\widetilde S\to S\) for the minimal resolution, with exceptional \(A_2\) chain \(E_i',E_i''\) above the \(i\)-th cusp. The cusp code is
\[
C(S)=\ker\left((\mathbb F_3)^{17}\longrightarrow H^2(\widetilde S,\mathbb F_3),\quad
(c_i)\longmapsto\sum_i c_i[2E_i'+E_i'']\right).
\]
The phrase *three-divisible support* means the support of a nonzero codeword; interchanging exceptional branches amounts to changing its nonzero coordinate sign. The theorem is conditional on the existence of two 12-supports intersecting in seven and does not classify all 17-cusp quintics. The existence of such surfaces is supplied by [1], not reproved here.

## Proof
**1. Exact code and forced third decomposition.** Tan's classification [2, Theorem 4.3.1], also recalled in [1, Section 2], says that the possible nonzero weights for a cusp code on a normal quintic are \(12,15,18\). Here length 17 excludes 18. Two distinct supports of size 12 cannot be scalar multiples, so their representing words \(a,b\in C(S)\) are independent and the minimum nonzero weight is 12. The ternary Griesmer bound gives, for dimension at least three, a minimum length of
\[
12+\lceil 12/3\rceil+\lceil12/9\rceil=18>17.
\]
Consequently, \(\dim C(S)=2\).

The sets of nonoverlap coordinates each have cardinality five, and there are seven overlap coordinates. Rescale each coordinate, if needed, so that on the shared coordinates each ratio \(b_i/a_i\) is either \(+1\) or \(-1\). Let \(r\) be the number of shared positions with equal ratio \(+1\). The two new projective codeword representatives \(a+b\) and \(a-b\) have weights \(10+r\) and \(17-r\), respectively. They are nonzero and neither is proportional to \(a\) or \(b\). Both must have weight 12 or 15; their sum 27 forces the pair \((12,15)\), hence \(r\in\{2,5\}\). Change the sign of \(b\) so that \(r=2\). The 17 cusps then split into four disjoint sets \(T,B_1,B_2,B_3\) of sizes \(2,5,5,5\), with the three weight-12 supports equal to \(T\cup B_i\cup B_j\) as \(\{i,j\}\) ranges over pairs from \(\{1,2,3\}\); the weight-15 support is \(B_1\cup B_2\cup B_3\). Each nonzero projective word gives two nonzero scalar words. This proves \(W(z)=1+6z^{12}+2z^{15}\). By the Barth--Rams description [3] each weight-12 support also determines a contact-cubic presentation, but the construction of a third explicit equation is not asserted.

**2. The abelianized fundamental group.** The minimal resolution \(\widetilde S\) is simply connected [1, Section 2]. Remove disjoint tubular neighbourhoods of all 17 exceptional \(A_2\) configurations. Each boundary is a lens space with \(H_1\cong\mathbb Z/3\). Mayer--Vietoris, or equivalently the discriminant-lattice exact sequence for the negative-definite \(A_2^{17}\) root lattice, identifies
\[
H_1(U,\mathbb Z)=\operatorname{coker}\left(H_2(\widetilde S,\mathbb Z)
\longrightarrow \bigoplus_{i=1}^{17} A_2^*/A_2\right).
\]
This is a quotient of \((\mathbb Z/3)^{17}\), so it has exponent three. Under the nondegenerate local linking pairing, its \(\mathbb F_3\)-linear dual is the kernel of the map from local discriminant groups to \(H^2(\widetilde S,\mathbb F_3)\); writing the fundamental discriminant class as \(2E_i'+E_i''\) identifies that kernel with \(C(S)\) exactly as above. It follows that \(H_1(U,\mathbb Z)\cong (\mathbb Z/3)^2\). A meridian about the \(i\)-th cusp maps trivially precisely when every codeword has zero \(i\)-th coordinate. The two original 12-supports cover all 17 cusps, so no meridian maps trivially.

**3. Smoothness and canonical invariants of the degree-nine cover.** The covering classified by \(\pi_1(U)\twoheadrightarrow H_1(U,\mathbb Z)\) is connected and Galois of degree nine. Normalize \(S\) in its function field. This yields a finite normal projective \(G\)-cover \(f:Y\to S\) étale over \(U\), where \(G=(\mathbb Z/3)^2\). Each cusp meridian has nonzero image, hence order three. The analytic punctured \(A_2\) neighbourhood has fundamental group \(\mu_3\), and its universal cover is \(\mathbb C^2\setminus\{0\}\). The inverse image of such a punctured neighbourhood has three components, each its universal degree-three cover, so its normalization across the puncture consists of three copies of \(\mathbb C^2\), all smooth. Thus \(Y\) is smooth over every point of \(S\).

The singularities of \(S\) are Du Val, so its canonical class is Cartier and \(\omega_S\simeq\mathcal O_S(1)\) by hypersurface adjunction. The finite map has no branch divisor. The ramification formula therefore gives \(K_Y=f^*K_S\), an ample line bundle. Hence \(Y\) is minimal of general type and \(K_Y^2=9\cdot5=45\).

The minimal resolution satisfies \(e(\widetilde S)=55\) by Noether's formula, because \(K_{\widetilde S}^2=5\) and \(\chi(\mathcal O_{\widetilde S})=5\). Contracting each \(A_2\) pair replaces a union of two meeting rational curves (Euler number three) with one point (Euler number one), so \(e(S)=55-2\cdot17=21\). Therefore \(e(U)=21-17=4\). The inverse image of \(U\) is a degree-nine unramified covering, and each of 17 cusps has three preimages, yielding \(e(Y)=9\cdot4+17\cdot3=87\). Smooth-surface Noether gives \(\chi(\mathcal O_Y)=(45+87)/12=11\).

**4. Irregularity.** Decompose \(H^1(Y,\mathcal O_Y)\) into character subspaces for the abelian deck group \(G\); characteristic zero makes the representation semisimple. The trivial-character part equals \(H^1(S,\mathcal O_S)=0\), because the cusps are rational singularities and the quintic resolution has irregularity zero. Every nontrivial character has a kernel of order three, and its eigenspace is contained in the invariant cohomology of the associated intermediate degree-three normal quotient. The latter quotient is the triple cover associated with one of the four nonzero projective cusp-code words. Its smooth resolution has \(q=0\) by Tan's theorem [2, Theorem 4.3.1], for both possible weights 12 and 15; the remaining quotient singularities are rational \(A_2\)'s and do not change irregularity. Since finite-quotient cohomology is the invariant part in characteristic zero, all nontrivial eigenspaces vanish, giving \(q(Y)=0\). Finally \(p_g(Y)=\chi(\mathcal O_Y)-1+q(Y)=10\).

## Verification
The standalone `verify_cusp_code.py` checks all \(2^7=128\) relative sign choices on seven overlap positions and confirms that the 42 cases allowed by Tan's weight restriction have shared equal-sign counts two or five. It independently enumerates the nine words in the normalized two-generator code, tests the exact weight enumerator, all three 12-support intersections and the common two-element intersection, and verifies the Griesmer inequality. It requires only standard Python 3.

The geometric proof is not a computer census. The fundamental-group calculation uses the integral \(A_2\) discriminant exact sequence; smoothness uses the explicit local quotient group; the Chern-number computation is exact; and the irregularity uses Tan's established result for both intermediate triple-cover types. No code establishes the original existence of the double-decomposition family or independently checks Tan's global theorem.

## Relationship to prior work
Borisov and Rito [1, Section 5, Theorem 3] construct a six-dimensional family of quintics with exactly 17 cusps admitting two Barth--Rams decompositions whose 12-cusp supports meet in seven. Their paper states these two supports and the deformation result but does not calculate the entire code, the 17-cusp smooth locus's first integral homology, or this family's smooth maximal degree-nine abelian cover and its numerical invariants. Their introduction discusses a **hypothetical 20-cusp** surface whose suitable degree-nine abelian cover would instead have \(p_g=4\), \(q=0\), and \(K^2=45\); that different singularity count and conditional construction do not determine the presently proved 17-cusp covering invariants.

Tan [2] proved the allowed weights and classified the invariants of individual cyclic triple covers. Barth and Rams [3] supplied the contact-cubic presentation for a weight-12 set. These are essential inputs, not new results here. Rito [4] constructed another 17-cusp quintic in a separate tangent-hyperplane setting and earlier cyclic degree-three examples; the present claim is conditioned on the two specified 12-supports and gives an abelian degree-nine construction. General finite-cover, rational-double-point and discriminant-lattice facts are standard.

## Limitations
This does not prove that arbitrary 17-cusp quintics have the stated code or cover, nor that the ninefold cover is the universal topological covering of \(U\); it is only the maximal **abelian** one. It does not classify the nonabelian fundamental group, prove uniqueness of the double-decomposition family, exhibit equations for the third contact-cubic presentation, determine canonical-map degree of \(Y\), or address the speculative 20-cusp extremal case. Older general cusp-code or abelian-cover treatments may contain equivalent formulations; the explicitly inspected primary papers do not state the combined 17-cusp conclusion. Independent external audit has not been performed.

## References
[1] Lev Borisov and Carlos Rito, *Quintic surfaces with 18 cusps*, arXiv:2608.12305 (first public 12 August 2026), Sections 1, 2, 3 and 5; author-hosted full text, https://www.researchgate.net/publication/412211241_Quintic_surfaces_with_18_cusps .

[2] Sheng-Li Tan, *Cusps on some algebraic surfaces and plane curves*, Theorem 4.3.1 and Sections 3.1–3.2 (2003), https://studylib.net/doc/8225720/cusps-on-some-algebraic-surfaces-and-plane-curves .

[3] Wolf P. Barth and Sławomir Rams, *Equations of low-degree projective surfaces with three-divisible sets of cusps*, arXiv:math/0112046 (first posted 2001; subsequent published version); statement as used in [1].

[4] Carlos Rito, *Cuspidal quintics and surfaces with \(p_g=0\), \(K^2=3\) and 5-torsion*, arXiv:1310.4071 (2013), later LMS Journal of Computation and Mathematics 19 (2016), pp. 42–53.
