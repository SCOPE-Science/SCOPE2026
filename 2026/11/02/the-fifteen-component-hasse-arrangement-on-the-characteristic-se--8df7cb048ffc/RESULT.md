# The fifteen-component Hasse arrangement on the characteristic-seven Humbert locus

## Finding

Consider the characteristic-seven Humbert--Edge curves of type four over \(k=\overline{\mathbb F}_7\). Their ordered five-point branch parameter space is
\[
M_{0,5}(k)=\{(u,v)\in k^2 : u,v\notin\{0,1\},\ u\ne v\}.
\]
The corresponding curve \(C_{u,v}\) has Jacobian \(7\)-rank \(f_7\) and \(a\)-number \(a\) in precisely the three pairs
\[
(f_7,a)\in\{(5,0),(4,1),(2,3)\}.
\]
The last pair occurs exactly at the twenty **ordered** parameter pairs
\[
(u,v)\in\{2,3,4,5,6\}^2,\qquad u\ne v.
\]
These are precisely all of \(M_{0,5}(\mathbb F_7)\). Every such point is in one orbit under the branch-label action of \(S_5\), hence the maximal-degeneration locus corresponds to one unordered branch configuration.

For each omitted branch point there is a natural elliptic quotient. Its supersingular locus is a union of three smooth irreducible curves in the parameter surface. Collectively the five supersingular divisors form **fifteen components and twenty ordinary triple points**. Every component contains four triple points, every triple point belongs to three components, and distinct components have no other intersections. Thus the finite incidence structure is of type \((15_4,20_3)\), where these numbers indicate the two incidence multiplicities (not a moduli-space intersection number). No geometric parameter lies on precisely two, four, or five of the five elliptic supersingular divisors.

## Assumptions and scope

The base field is algebraically closed of characteristic \(7\). The curve \(C_{u,v}\) means the smooth projective normalization of the four-fold quadratic fiber product
\[
s_0^2=-x,\qquad s_1^2=x-1,\qquad s_2^2=x-u,\qquad s_3^2=x-v,
\]
with distinct \(\infty,0,1,u,v\). Equivalently, it is a smooth complete intersection of three diagonal quadrics in \(\mathbb P^4\). It is a maximal elementary abelian \(2\)-cover with deck group \(G\cong(\mathbb Z/2\mathbb Z)^4\). Riemann--Hurwitz gives \(2g-2=16(-2+5/2)=8\), so \(g=5\).

All parameter counts in this paper are counts on the **ordered** branch moduli space \(M_{0,5}\), not numbers of abstract isomorphism classes or points of a coarse unmarked stack. The local intersection assertions refer to that smooth marked parameter surface.

## Proof

**1. Five elliptic factors and their arithmetic invariants.** A nontrivial character of \(G\) determines a quadratic quotient of \(C_{u,v}\) whose branch subset is even. Among the fifteen characters, ten have two branch points and genus zero, and five have four branch points and genus one. The five elliptic quotients correspond to omitting one of the five branch points. Their pullbacks together induce an isogeny to the Jacobian whose degree is a power of two. One can see this directly from the orthogonal character projectors in \(\mathbb Z_7[G]\), whose denominators divide \(16\), or via the explicit Humbert--Edge Prym--Tyurin decomposition. Consequently the induced map on \(7\)-divisible groups is an isomorphism. Both \(7\)-rank and \(a\)-number are therefore sums of the five corresponding elliptic invariants. A supersingular elliptic factor contributes \((f_7,a)=(0,1)\), and an ordinary one contributes \((1,0)\).

**2. The five supersingularity tests.** Label the marked branch points \((\infty,0,1,u,v)\). Under a change of Legendre coordinate, the five four-point subsets have parameters
\[
r_0=u,\quad r_1=v,\quad r_2=\frac vu,\quad r_3=\frac{v-1}{u-1},\quad r_4=\frac{u(v-1)}{v(u-1)}.
\]
The order of the five tests is immaterial. In characteristic seven the cubic Deuring polynomial is
\[
h(t)=\sum_{j=0}^3\binom3j^2t^j=t^3+2t^2+2t+1=(t-2)(t-4)(t-6).
\]
It is, up to a nonzero scalar, the coefficient of \(x^6\) in \([x(x-1)(x-t)]^3\). Therefore a Legendre elliptic curve is supersingular precisely for \(t\in S=\{2,4,6\}\). The supersingular divisors are \(D_i=\{h(r_i)=0\}\), with all rational denominators invertible on the parameter space. The three fibers \(r_i=s\), \(s\in S\), are distinct, smooth, irreducible rational curves (punctured fibers of the forgetful map \(M_{0,5}\to M_{0,4}\)), proving that there are fifteen components.

**3. Pairwise intersections and completeness over the algebraic closure.** The branch permutation group \(S_5\) permutes the five divisors transitively on unordered pairs. It suffices to intersect \(D_0\) and \(D_1\), where \(r_0=u\) and \(r_1=v\). Their intersection consists of exactly six reduced points \((u,v)\in S^2\) with \(u\ne v\). The subgroup of permutations of \((\infty,0,1)\) acts on cross ratios through \(t\mapsto1-t\) and \(t\mapsto1/t\), which realize the full symmetric group on the three elements of \(S\). Hence all six points lie in the \(S_5\)-orbit of \((2,4)\).

At \((u,v)=(2,4)\), exactly \(r_0=2\), \(r_1=4\), and \(r_2=2\) lie in \(S\); the other two ratios are \(3\) or \(5\), neither in \(S\). Every point in any pairwise intersection consequently lies on **exactly three** of the five divisors, by permutation symmetry. There are \(\binom52=10\) unordered divisor pairs, each meeting in exactly six points. Every such geometric point is counted exactly \(\binom32=3\) times. Therefore the union of all pairwise intersections has exactly \(10\cdot6/3=20\) geometric points. Each is defined over \(\mathbb F_7\), since the six initial points and all permuting Möbius transformations are defined over \(\mathbb F_7\). But \(M_{0,5}(\mathbb F_7)\) itself consists of exactly \(5\cdot4=20\) pairs, namely the claimed set. This proves the exhaustive classification over \(k\), not merely over a finite sampling field.

Away from these points at most one \(D_i\) vanishes. All three counts \(0,1,3\) are attained, since each \(D_i\) has nonempty complement of its intersections and the union is a proper divisor. The isogeny decomposition then yields exactly \((f_7,a)=(5,0),(4,1),(2,3)\), respectively.

**4. Scheme structure and incidences.** Each \(D_i\) is reduced: the three zeros of \(h\) are simple, and each forgetful map is smooth. Two distinct \(D_i\) meet transversely because, after relabeling, their local defining equations are \(u-s\) and \(v-t\) for distinct \(s,t\in S\). At the representative point \((2,4)\), the three local components have equations, up to units,
\[
u-2=0,\qquad v-4=0,\qquad v-2u=0,
\]
with pairwise distinct tangent lines. The same holds at every point by symmetry: all are ordinary triple intersections. Each of the fifteen irreducible components contains four of the triple points: for the component \(u=s\), these are the four other allowed \(\mathbb F_7\)-values of \(v\); all components are conjugate under permutations. There are no other intersections by the completeness argument above.

## Verification

The bundled standard-library program `verify_humbert7.py` recomputes the Deuring polynomial, every one of the twenty normalized rational points and its five tests, all ten pairwise intersection sizes, the unique twenty-point orbit under 120 label permutations, and the \((15_4,20_3)\) incidence counts. It also checks the three independent local tangent directions. The infinite-field completeness and prime-to-seven isogeny are proved above and do not depend on finite-field enumeration.

## Relationship to prior work

Hidalgo, Kontogeorgis, Leyton-Álvarez, and Paramantzoglou give the positive-characteristic generalized Fermat geometry. Carvacho, Hidalgo, and Quispe establish the elliptic quotient decomposition for genus-five generalized Fermat curves (over complex fields). Auffarth, Lucchini Arteche, and Rojas refine Humbert--Edge decompositions and calculate the isogeny kernel of \(2\)-power order over fields of characteristic different from two. Martínez-Núñez presents the broader group-algebra decomposition. These results give the framework and are **not** claimed as new. The additional assertion here concerns the complete **characteristic-seven arithmetic stratification**, the exact twenty rational marked points, and the fifteen-component triple-point Hasse arrangement. In the inspected passages of these works no implication establishing these precise characteristic-seven intersections or the rank gap was found.

## Limitations

The classification applies to the indicated genus-five maximal elementary-abelian cover, not arbitrary genus-five curves or all generalized Fermat types or all characteristics. It describes the reduced marked Hasse divisor and its intersections, not its compactification at boundary points nor multiplicities on coarse quotient spaces. The ordinary-versus-nonordinary quotient decomposition is a prime-to-characteristic isogeny, not an isomorphism of polarized Jacobians. No claim is made about independent historical-priority certification: equivalent old work in alternate coordinates may exist, and external audit has not been performed.

## References

1. Hidalgo, Kontogeorgis, Leyton-Álvarez, Paramantzoglou, *Automorphisms of the generalized Fermat curves*, first arXiv public version 2014-09-10. https://arxiv.org/abs/1409.3063
2. Carvacho, Hidalgo, Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, first arXiv public version 2015-07-10, especially Section 5.1. https://arxiv.org/abs/1507.02903
3. Auffarth, Lucchini Arteche, Rojas, *A decomposition of the Jacobian of a Humbert-Edge curve*, first arXiv version 2019-05-29, especially Theorems 2.1 and 4.1. https://arxiv.org/html/1905.12690v2
4. Martínez-Núñez, *Decomposition of jacobians of generalized Fermat curves*, first arXiv version 2023-03-31, introduction and factor description. https://arxiv.org/abs/2303.18056
