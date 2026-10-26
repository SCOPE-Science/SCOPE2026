# A smooth ninefold cover of the seventeen-cusp quintic family

## Finding
Let \(S\subset\mathbb P^3_{\mathbb C}\) be a normal quintic surface whose only singularities are exactly seventeen ordinary cusps (surface singularities of type \(A_2\)). Assume that its cusp code contains two independent weight-twelve words whose supports meet in seven cusps. This holds for the general seventeen-cusp members of the two-Barth–Rams-decomposition family constructed by Borisov and Rito.

Then the cusp code \(\mathcal C(S)\) is, up to coordinate permutation and nonzero coordinate rescaling, the ternary \([17,2,12]\) code whose two-row generator matrix has projective column directions \((1:0),(0:1),(1:1),(1:-1)\) of respective multiplicities \(5,5,5,2\). Its weight enumerator is
\[
 W_{\mathcal C(S)}(t)=1+6t^{12}+2t^{15}.
\]
In particular, **exactly three** twelve-cusp sets and **exactly one** fifteen-cusp set are three-divisible. Each twelve-cusp set admits a Barth–Rams contact-cubic decomposition; thus the two exhibited weight-twelve structures necessarily yield a third three-divisible twelve-cusp structure. The unique fifteen-cusp set omits a canonically distinguished pair of cusps.

Writing \(U=S_{\rm reg}\), the connected maximal elementary-abelian three-cover of \(U\) has group \(G\cong(\mathbb Z/3\mathbb Z)^2\). Its normalization over \(S\) is a **smooth connected projective surface** \(f:Y\to S\) of degree nine, unramified over \(U\), and its canonical bundle is \(K_Y=f^*\mathcal O_S(1)\). Its invariants are
\[
 (K_Y^2,p_g(Y),q(Y),c_2(Y),\chi(\mathcal O_Y))=(45,10,0,87,11).
\]
The four order-three subgroups of \(G\) have nonidentity fixed-point counts \(15,15,15,6\), respectively. The four intermediate degree-three covers of \(S\) have branch supports of sizes \(12,12,12,15\); their minimal resolutions have geometric genera \(6,6,6,4\), and all have irregularity zero. This characterizes the complete elementary-abelian three-cover geometry attached to the cusp code.

## Assumptions and scope
Everything is over \(\mathbb C\). A cusp means a rational double point \(A_2\), analytically \(\mathbb C^2/\mu_3\) with the generator acting by \((s,t)\mapsto(\zeta s,\zeta^{-1}t)\). The minimal resolution \(\widetilde S\to S\) has two exceptional \((-2)\)-curves \(E_i',E_i''\) above each cusp. Define
\[
 \mathcal C(S)=\ker\left(\mathbb F_3^{17}\to H^2(\widetilde S,\mathbb F_3),\quad (a_i)\mapsto\sum_i a_i[2E_i'+E_i'']\right).
\]
Equivalently one may use \([E_i'-E_i'']\), since these differ by a unit modulo three. A nonzero codeword, modulo multiplication by \(\mathbb F_3^\times\), determines a connected cyclic triple covering of \(S\) branched precisely over the cusps in its support. The two specified independent codewords are required: no assertion is made about other seventeen-cusp families lacking them. The Borisov–Rito general family supplies this hypothesis and the intersection size seven [1].

## Proof
**1. Rank and weights of the cusp code.** By Tan's theorem [2], nonzero cusp-code words on a quintic surface have weight twelve, fifteen or eighteen; the last is impossible at length seventeen. Two independent words give rank at least two. The ternary Griesmer bound for rank three and minimum distance at least twelve reads
\[
 n\ge 12+\lceil12/3\rceil+\lceil12/9\rceil=18,
\]
so the code has rank exactly two. Write the two given words as \(a,b\). Their supports cover all seventeen cusps, since they each have weight twelve and meet in seven; consequently their two-row generator matrix has no zero column.

There are four projective nonzero words, represented by \(a,b,a+b,a-b\). At each nonzero column of a rank-two ternary code, exactly three of these four words evaluate nontrivially. Their weights therefore sum to \(3\cdot17=51\). Because \(a\) and \(b\) each have weight twelve, the remaining two weights sum to twenty-seven and each lies in \(\{12,15\}\), so they are twelve and fifteen. This proves the weight enumerator.

For a projective word \(v\), its zero set consists of columns on the unique perpendicular projective line in \(\mathbb F_3^2\). Hence the four column-direction multiplicities equal the four zero-set sizes, which are \(5,5,5,2\). The projective linear group permutes the four directions, and the nonzero values of each column may be removed by monomial rescaling. This proves the asserted complete code classification. In particular, the three weight-twelve supports are the complements of the three disjoint five-cusp blocks; the weight-fifteen support is the complement of the two-cusp block. Distinct projective words yield distinct cyclic covers, and Barth–Rams [3] gives contact-cubic decompositions for all twelve-cusp supports. Here the asserted existence of a third decomposition means a third twelve-cusp three-divisible structure and some contact-cubic presentation, **not** uniqueness of a contact-cubic equation for any support.

**2. The maximal three-cover and local smoothness.** By the simply connectedness of \(\widetilde S\) for a quintic with rational double points, \(H^1(\widetilde S,\mathbb F_3)=0\) [1,2]. The cohomology localization sequence for the complement of its exceptional curves identifies \(H^1(U,\mathbb F_3)\) with the kernel of the map from exceptional-component classes to \(H^2(\widetilde S,\mathbb F_3)\). On each \(A_2\) exceptional chain the intersection matrix modulo three has one-dimensional radical, spanned by \([E_i'-E_i'']\). Thus
\[
 H^1(U,\mathbb F_3)\simeq\mathcal C(S)\simeq\mathbb F_3^2.
\]
The joint kernel of all characters defines a connected étale \(G\)-cover of \(U\), with \(G\cong(\mathbb Z/3\mathbb Z)^2\), and normalization extends it to a finite degree-nine map \(f:Y\to S\).

At a cusp, the restriction of characters to the local punctured neighborhood is given by the corresponding column of the code generator matrix. No column vanishes. The local fundamental group of \(A_2\) is cyclic of order three; its image in \(G\) therefore has order three. The covering over a sufficiently small punctured cusp neighborhood is consequently three disjoint copies of the universal smooth local covering \(\mathbb C^2\setminus\{0\}\to(\mathbb C^2/\mu_3)\setminus\{0\}\). After normalization, each copy fills in a smooth point. All cusp preimages are smooth, so \(Y\) is smooth; each cusp has exactly three preimages, and the subgroup fixing those points is the projective column direction under the dual identification. The multiplicities \(5,5,5,2\) give fixed-point counts \(3\cdot(5,5,5,2)=(15,15,15,6)\). Since the cover is étale in codimension one, \(K_Y=f^*K_S=f^*\mathcal O_S(1)\), which is ample.

**3. Numerical invariants and intermediate quotients.** The minimal resolution of a normal quintic with only \(A_2\) singularities has \(K_{\widetilde S}^2=5\) and \(\chi(\mathcal O_{\widetilde S})=5\), so Noether's formula gives \(e(\widetilde S)=55\). Contracting each pair of exceptional curves changes the Euler characteristic by two; hence \(e(S)=55-2\cdot17=21\). The covering has degree nine away from the seventeen cusps and three smooth preimages at each cusp. Therefore
\[
 e(Y)=9(21-17)+3\cdot17=87,
 \qquad K_Y^2=9\cdot5=45,
 \qquad\chi(\mathcal O_Y)=(87+45)/12=11.
\]
Each order-three subgroup \(H\subset G\) gives a quotient \(Y/H\to S\) of degree three. The associated character vanishes on one column block and is nonzero on the other columns; its branch support has twelve cusps for the three blocks of size five and fifteen cusps for the block of size two. Tan's theorem [2, Theorem 4.3.1] gives geometric genera six (weight twelve) and four (weight fifteen), and irregularity zero, for the minimal resolutions. These quotients have only \(A_2\) singularities, since they are locally quotients of smooth points by the same order-three action, so resolving them does not change coherent cohomology of the structure sheaf.

For a complex \(G\)-representation \(V\), decomposing into characters shows
\[
 \sum_{\substack{H\subset G\\ |H|=3}}\dim V^H=\dim V+3\dim V^G.
\]
Apply this to \(V=H^j(Y,\mathcal O_Y)\), for \(j=1,2\), using \(H^j(Y,\mathcal O_Y)^G\cong H^j(S,\mathcal O_S)\), the rationality of \(A_2\), and the four intermediate quotient values. Since \(q(S)=0\) and \(p_g(S)=4\), this yields
\[
 q(Y)=0,\qquad p_g(Y)=3\cdot6+4-3\cdot4=10.
\]
In particular the Euler and Hodge calculations agree: \(p_g-q+1=11\).

## Verification
A self-contained standard-Python enumerator `check.py` verifies the canonical generator matrix, the complete nine-word weight distribution, the four subgroup fixed-point counts, the branch-support sizes, and the numerical identities \(K_Y^2=45\), \(c_2(Y)=87\), \(\chi=11\), \(p_g=10\), \(q=0\). The checker exhausts the **finite code model only**. The geometric existence, localization sequence, smoothness and universal assertions rest on the proof, not on numerical enumeration.

## Relationship to prior work
Borisov–Rito [1] construct a six-dimensional family with general member having seventeen cusps and two twelve-cusp Barth–Rams structures intersecting in seven cusps. They do not determine the entire cusp code or introduce the smooth degree-nine maximal three-cover, its invariant package, or its group fixed-point distribution. Tan [2] establishes the general restrictions on cusp-code weights and the canonical invariants of **individual cyclic triple covers**. Barth–Rams [3,4] provide the classical contact-cubic construction and the general code methods. The present contribution combines these ingredients with an exact code classification, cohomological identification of the maximal elementary-abelian cover, local smoothness, and simultaneous invariants for the resulting global surface. Established statements of the cited papers are not claimed as new.

## Limitations
The result is for characteristic zero and for seventeen-cusp quintics carrying the specified pair of independent weight-twelve classes. It does not assert a new explicit quintic equation, classify all seventeen-cusp families, classify contact-cubic presentations for a given support, or determine the degree of the complete canonical map of the ninefold cover. The source family is only a sufficient supply of surfaces satisfying the hypotheses. Historical priority remains open to older unindexed constructions of equivalent abelian covers. No independent audit has been performed.

## References
[1] L. Borisov and C. Rito, *Quintic surfaces with 18 cusps*, arXiv:2608.12305v1, first public 2026-08-12, especially Sections 2, 3 and 5. https://arxiv.org/abs/2608.12305

[2] S.-L. Tan, *Cusps on some algebraic surfaces and plane curves*, especially Sections 3.1–3.2 and Theorem 4.3.1 (1999). https://math.ecnu.edu.cn/~sltan/tan-cusp.pdf

[3] W. P. Barth and S. Rams, *Equations of low-degree projective surfaces with three-divisible sets of cusps*, arXiv:math/0112046, 2001; Math. Z. 249 (2005), 283–295. https://arxiv.org/abs/math/0112046

[4] W. P. Barth and S. Rams, *Cusps and codes*, arXiv:math/0403018, 2004; Math. Nachr. 280 (2007), 50–59. https://arxiv.org/abs/math/0403018

[5] C. Rito, *Cuspidal quintics and surfaces with \(p_g=0\), \(K^2=3\) and 5-torsion*, arXiv:1310.4071; LMS J. Comput. Math. 19 (2016), 42–53. https://arxiv.org/abs/1310.4071
