# A twelve-point superspecial stratum and missing intermediate ranks for genus-five Humbert curves in characteristic seventeen

## Finding
Let \(k=\overline{\mathbb F}_{17}\). For \(u,v\in k\) satisfying \(uv(u-1)(v-1)(u-v)\ne0\), define the smooth, marked genus-five Humbert curve
\[
C_{u,v}:\quad
X_1^2+X_2^2+X_3^2=0,\quad
u X_1^2+X_2^2+X_4^2=0,\quad
v X_1^2+X_2^2+X_5^2=0
\]
in \(\mathbb P^4\). The five natural elliptic quotients are supersingular on five divisors in the parameter surface. Each pair of these divisors meets transversely at exactly \(56\) geometric points; precisely \(12\) points lie on all five divisors, while the remaining \(44\) points on each pair lie on no other divisor. There are **no** triple-only or quadruple-only intersections. Thus the global incidence configuration has \(440\) distinct ordinary double intersections and \(12\) distinct ordinary fivefold intersections, with no points of exact multiplicity three or four. All intersections lie in \(\mathbb F_{289}\); the twelve fivefold points form a single orbit under permutations of the five branch labels, of size \(12\) and stabilizer order \(10\).

Let \(N_s(q)\) count *ordered marked* pairs \((u,v)\in\mathbb F_q^2\) in this smooth parameter open for which exactly \(s\) of the five elliptic quotients are supersingular. For every integer \(m\ge1\), put \(q=17^m\). If \(m\) is odd, then
\[
N_0(q)=(q-2)(q-3),\qquad N_1(q)=N_2(q)=N_5(q)=0.
\]
If \(m\) is even, then
\[
\begin{aligned}
N_5(q)&=12,&N_2(q)&=440,\\
N_1(q)&=40(q-3)-940,&
N_0(q)&=(q-2)(q-3)-40(q-3)+488.
\end{aligned}
\]
In both cases \(N_3(q)=N_4(q)=0\). The Jacobian \(17\)-rank is \(5-s\), and its \(a\)-number is \(s\). In particular, the possible geometric \(17\)-ranks in this smooth family are exactly \(\{0,3,4,5\}\): neither rank one nor rank two occurs. At each of the twelve fivefold points the Jacobian is **superspecial**. Over \(\mathbb F_{17}\) all \(210\) smooth marked pairs are ordinary; over \(\mathbb F_{289}\) the four nonempty strata, ordered by \(s=0,1,2,5\), have cardinalities \((71130,10500,440,12)\).

## Assumptions and scope
The characteristic is exactly \(17\); the five branch values \(\infty,0,1,u,v\) must be pairwise distinct. The marking is their *order*, so the numerical formulas do not count unmarked geometric isomorphism classes. We use supersingular for an elliptic quotient in the usual sense, and superspecial for an abelian variety with geometric \(a\)-number equal to its dimension. We work with reduced supports of the five divisors in the smooth two-dimensional parameter space, rather than their closure on a compactification.

The five quotient Legendre parameters, in the order of Carvacho–Hidalgo–Quispe (Theorem 5.1), are
\[
\lambda_1=\frac{v-1}{u-1},\quad
\lambda_2=\frac{v}{u},\quad
\lambda_3=\frac{v(1-u)}{v-u},\quad
\lambda_4=v,\quad
\lambda_5=u.
\]
Each quotient is isomorphic over the algebraic closure to a Legendre elliptic curve \(E_\lambda:y^2=x(x-1)(x-\lambda)\). The Jacobian decomposition is induced by the action of a group of order \(16\), and the corresponding isogeny has kernel killed by a power of \(2\); hence it induces an isomorphism on \(17\)-divisible groups. This is stronger than an unspecified isogeny and permits exact \(17\)-rank and \(a\)-number statements.

## Proof
**Step 1: five supersingularity equations.** The Deuring–Hasse polynomial of a Legendre elliptic curve in characteristic \(17\) is
\[
H(T)=\sum_{j=0}^{8}\binom8j^2T^j
=T^8-4T^7+2T^6+8T^5+4T^4+8T^3+2T^2-4T+1.
\]
It factors in \(\mathbb F_{17}[T]\) as
\[
H(T)=(T^2+T-1)(T^2-3T+1)(T^2-T+1)(T^2-T-1).
\]
Each displayed quadratic is irreducible over \(\mathbb F_{17}\) and separable. Hence the complete set \(R\) of eight geometric roots lies in \(\mathbb F_{289}\), and \(R\cap\mathbb F_{17}=\varnothing\). The five supersingularity divisors are precisely \(H(\lambda_i)=0\), for \(1\le i\le5\).

**Step 2: one pair controls every geometric multiple intersection.** The permutation group on the five labeled branch points acts on the smooth parameter surface \(M_{0,5}\). It acts transitively on unordered pairs of the five omitted-branch elliptic quotients. After relabeling, an intersection of any two distinct supersingularity divisors becomes \(H(u)=H(v)=0\). Thus any geometric parameter lying on at least two divisors can be studied by the \(8\cdot7=56\) ordered pairs \((u,v)\in R^2\) with \(u\ne v\). This is a *geometrically exhaustive* list because \(H\) has exactly the eight roots given in Step 1; it is not a partial finite-field sample.

For a replayable exact certificate, represent \(\mathbb F_{289}\) as \(\mathbb F_{17}[z]/(z^2-3)\). In the coordinate representation \(a+bz\), the eight Hasse roots are
\[
(8,4),\ (8,13),\ (9,2),\ (9,4),\ (9,13),\ (9,15),\ (10,4),\ (10,13).
\]
The standalone verifier evaluates the five explicit rational expressions \(\lambda_i\) on all \(56\) distinct root pairs, using only exact modular arithmetic. Exactly \(44\) of the ordered pairs satisfy precisely two supersingularity equations and exactly \(12\) satisfy all five; none satisfies exactly three or four. Permutation symmetry therefore excludes every geometrically possible triple-only or quadruple-only intersection, not just those defined over a chosen finite field.

**Step 3: incidence, fields of definition, and transversality.** Each pair of distinct divisors consequently has \(44+12=56\) intersection points, all \(\mathbb F_{289}\)-rational. The ten pairs of divisors have disjoint exact-double loci (since no triple-only points exist), giving \(10\cdot44=440\) exact-double geometric points. The twelve all-five points are counted in every pair but form only twelve geometric parameters. For any chosen pair of omitted-branch divisors, the same branch-label change identifies its two cross ratios with the local coordinates \(u,v\). As all eight Hasse roots are simple, the two local equations have linearly independent differentials. Hence *any two distinct* divisors meet transversely at their common points. Thus the twelve fivefold points have five pairwise distinct tangent directions.

The verifier further applies all \(120\) permutations of the five branch labels to one fivefold configuration, followed by the unique fractional-linear normalization of its first three branch points to \(\infty,0,1\). Its orbit consists of exactly twelve marked parameters and equals the complete twelve-point fivefold set. In particular there is just one marked-parameter orbit, with stabilizer order ten. The classical golden-ratio configuration \(u^2-u-1=0\), \(v=u-1\), described as five isomorphic elliptic factors in the cited foundational work, supplies a concrete representative of this orbit. Its reduction to characteristic \(17\) gives a superspecial example; **the existence of that example alone is not claimed as new**.

**Step 4: exact counts over all extensions.** For \(q=17^m\), there are \((q-2)(q-3)\) smooth marked pairs. If \(m\) is odd, the field \(\mathbb F_q\) has intersection \(\mathbb F_{289}\cap\mathbb F_q=\mathbb F_{17}\); it contains no Deuring–Hasse roots. As all \(\lambda_i\) are rational functions of \(u,v\), every quotient is ordinary. If \(m\) is even, all eight Hasse roots and all \(452\) multiple-intersection parameters lie in \(\mathbb F_q\). Each of the five supersingularity divisors has exactly \(8(q-3)\) marked points: after relabeling, fixing \(u\) to any root leaves \(q-3\) possible values of \(v\). Thus the total incidence count (each parameter counted once per supersingular quotient) is \(40(q-3)\). Of these incidences, exact doubles contribute \(2\cdot440=880\) and the twelve fivefold points contribute \(5\cdot12=60\), so \(N_1(q)=40(q-3)-940\). Subtracting the three nonordinary strata gives the displayed \(N_0(q)\). This establishes the formulas for *all* positive \(m\) rather than extrapolating from finite enumerations.

**Step 5: Jacobian invariants.** The five quotient elliptic curves have ordinary \(17\)-divisible groups of \(17\)-rank one and \(a\)-number zero, or supersingular groups of \(17\)-rank zero and \(a\)-number one. Because the quotient-product isogeny has degree a power of two, their product and the Jacobian have isomorphic \(17\)-divisible groups. Hence \(17\)-rank equals \(5-s\), \(a\)-number equals \(s\), and the Newton slopes are \(0^{5-s},(1/2)^{2s},1^{5-s}\). For \(s=5\) the Jacobian is superspecial, rather than merely supersingular up to unspecified isogeny.

## Verification
Run the self-contained Python standard-library script `verify.py` with Python 3.10 or later. It checks the exact factorization, builds \(\mathbb F_{289}\), enumerates all eight Hasse roots and all \(56\) ordered distinct pairs, establishes the 12-point orbit under all branch-label permutations, and independently enumerates the full \(82,082\)-point smooth marked parameter set over \(\mathbb F_{289}\). Its exact output is provided in `verification_output.txt` and concludes `VERIFY_OK`. All field operations are modular integer operations; no probabilistic calculations, external data, or network calls are used. The finite root-pair calculation is exhaustive for the *geometric intersection question* by Step 2; the all-extension counts are deductions from that finite classification, not extrapolations.

## Relationship to prior work
Carvacho, Hidalgo, and Quispe (arXiv:1507.02903, Theorem 5.1 and §5.2) establish the five elliptic quotients and give a special golden-ratio configuration where they are mutually isomorphic. This material already provides the key *existence mechanism* and is not new here. Auer and Top (arXiv:math/0106273, §3) study supersingular Legendre parameters, the Deuring polynomial, and their quadratic-field rationality; these ingredients are also prior results. The present claim concerns their **simultaneous** incidence in the entire characteristic-seventeen marked Humbert parameter surface, the absence of exact triple or quadruple intersections, the unique twelve-point fivefold orbit, and the exact count and Jacobian-rank stratification over every finite extension. More recent general genus-five superspecial-curve existence results, such as Ohashi (arXiv:2604.18074), do not state this explicit Humbert parameter classification. Previous computations at other characteristics do not imply this characteristic-seventeen incidence table.

## Limitations
The counts are for ordered marked parameters, not unmarked isomorphism classes. No claim is made about the boundary of a compactified moduli space, higher-dimensional deformations, or primes other than \(17\). The particular superspecial golden-ratio configuration is already present in earlier work as an all-isomorphic-elliptic configuration; the asserted new structural content is the exhaustive incidence arrangement and field-by-field stratification. Historical priority remains provisional: an unindexed prior parameter-table calculation might cover some or all of these exact values. The mathematical verification is not an independent external audit.

## References
1. R. Auer and J. Top, *Legendre elliptic curves over finite fields*, arXiv:math/0106273 (first public version 2001-06-22), especially §3. https://arxiv.org/abs/math/0106273
2. M. Carvacho, R. A. Hidalgo, and S. Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903 (first public version 2015-07-10), especially Theorem 5.1 and §5.2. https://arxiv.org/abs/1507.02903
3. R. Ohashi, *Generalized Howe curves of genus 4, 5, and 6 with completely decomposable Jacobians*, arXiv:2604.18074 (first public version 2026-04-20), Theorem 1.2 and Appendix A, for contextual genus-five existence results. https://arxiv.org/abs/2604.18074
