# Exact fourth moments of unit-perturbed quartic graphs over prime-square rings

## Finding
Let \(p\ge 5\) be a prime, \(R=\mathbb Z/p^2\mathbb Z\), and let \(c\in R\) satisfy \(p\nmid c\). Consider the polynomial graph
\[
\Gamma_c=\{(x,x^4+cx^2):x\in R\}\subset R^2.
\]
For the quadratic character \(\chi=\chi_p\) of \(\mathbb F_p\), extended by \(\chi(0)=0\), put
\[
\delta=\chi(-3),\qquad \eta=\chi(6c),\qquad J=1+\chi(-6c).
\]
Its *additive energy*, the number of ordered quadruples \((a,b,d,e)\in R^4\) satisfying
\[
(a,a^4+ca^2)+(b,b^4+cb^2)
=(d,d^4+cd^2)+(e,e^4+ce^2),
\]
has the exact value
\[
\boxed{E(\Gamma_c)=p^2\bigl(3p^2+p(\eta-3)+2\delta+J\bigr)
+p^2(p-1)\bigl(3p-2\delta-2J\bigr).}
\tag{1}
\]
Equivalently,
\[
E(\Gamma_c)=6p^4+p^3(\eta-6-2\delta-2J)
+p^2(4\delta+3J).
\tag{2}
\]
In particular, the energy depends only on the quadratic-residue class of \(c\pmod p\), not on its finer residue modulo \(p^2\).

The two possible unit-coefficient energies are distinct for every \(p\ge5\). Denote by \(E_+\) and \(E_-\) the values for \(\chi(6c)=+1\) and \(\chi(6c)=-1\), respectively. Then
\[
\boxed{E_+-E_-=
\begin{cases}
-2p^2(p-3),&p\equiv1\pmod4,\\
6p^2(p-1),&p\equiv3\pmod4.
\end{cases}}
\tag{3}
\]
Thus the energy ordering *reverses* across the two odd-prime congruence classes modulo four. There is one value for each quadratic-residue class of the coefficient, with exactly \(p(p-1)/2\) unit coefficients in each class modulo \(p^2\).

For a fixed nontrivial additive character of \(R\), set
\[
\mathcal E_c1(u,v)=\sum_{x\in R}\exp\!\left(\frac{2\pi i}{p^2}\bigl(ux+v(x^4+cx^2)\bigr)\right).
\]
With probability measure on \(R^2\), character orthogonality yields the *exact constant-input Fourier fourth moment*
\[
\|\mathcal E_c1\|_{L^4(R^2)}^4=E(\Gamma_c).
\tag{4}
\]
No assertion is made that constant input is optimal for the full \(\ell^2\)-to-\(L^4\) extension operator norm.

## Assumptions and scope
All operations in the graph and equality constraints are modulo \(p^2\). The parameter \(c\) is an arbitrary *unit* of \(R\), and \(p\ge5\) is essential to the nondegenerate conic and lifting arguments. A quadratic character of an integer means its image in \(\mathbb F_p\). The energy counts ordered quadruples, including diagonal/permutation collisions. The Fourier transform in (4) uses the *unnormalized* exponential sum and the *normalized probability* norm \(p^{-4}\sum_{u,v\in R}\lvert\cdot\rvert^4\).

## Proof
**1. A triple parametrization and its three-factor congruence.** Put \(s=a+b=d+e\), \(t=a-b\), and \(w=d-e\). Since \(2\) is a unit in \(R\), choosing a triple \((s,t,w)\in R^3\) is bijective with choosing an ordered quadruple with equal first-coordinate sums. The polynomial identities
\[
a^4+b^4=\frac{s^4+6s^2t^2+t^4}{8},\qquad
 a^2+b^2=\frac{s^2+t^2}{2}
\]
show that equality of second-coordinate sums is exactly
\[
(t-w)(t+w)\bigl(t^2+w^2+6s^2+4c\bigr)=0\pmod{p^2}.
\tag{5}
\]
Write the three factors as \(L_-=t-w\), \(L_+=t+w\), and \(Q=t^2+w^2+6s^2+4c\).

**2. Modulo-\(p\) geometry controls all lifts.** Reduce triples modulo \(p\). Let \(U\) be the number of points on the union of the three zero loci \(L_-=0\), \(L_+=0\), and \(Q=0\), and let \(I\) count points lying on at least two of these loci. Because \(p\nmid c\), the quadric \(Q=0\) is nonsingular modulo \(p\): its gradient can vanish only at \((s,t,w)=(0,0,0)\), where \(Q=4c\ne0\). The two linear factors also have nonzero gradients.

At a residue triple where exactly one factor vanishes, the gradient of the full product in (5) is nonzero. Its Taylor expansion in the three new base-\(p\) digits imposes one nontrivial affine linear equation over \(\mathbb F_p\), leaving exactly \(p^2\) lifts satisfying (5). At a residue triple where two or three factors vanish, their product is divisible by \(p^2\) for every one of its \(p^3\) lifts. No triple with no zero factor lifts. Consequently,
\[
E(\Gamma_c)=p^2(U-I)+p^3 I=p^2U+(p^3-p^2)I.
\tag{6}
\]
This is an exact lifting count, including all singular intersections; it is not a heuristic Hensel approximation.

**3. Sizes of the components and their intersections.** The two planes each contain \(p^2\) points, and their intersection \(t=w=0\) is a line with \(p\) points. The two plane–quadric intersections each reduce to
\[
t^2+3s^2=-2c\pmod p,
\]
which has precisely \(H=p-\chi(-3)=p-\delta\) solutions by the binary quadratic-character sum for a nonzero right-hand side. Their common triple intersection is \(t=w=0\), \(6s^2+4c=0\), and therefore has precisely
\[
J=1+\chi(-2c/3)=1+\chi(-6c)
\tag{7}
\]
points.

For the quadric \(Q=0\) alone, fixing \(s\) requires \(t^2+w^2=-6s^2-4c\). Over \(\mathbb F_p\), the count of representations of a nonzero element as a sum of two squares is \(p-\chi(-1)\), whereas at zero it is \(p+(p-1)\chi(-1)\). The number of values of \(s\) with zero right-hand side is \(J\). Thus the quadric has
\[
|Q=0|=p^2+p\chi(-1)(J-1)=p^2+p\chi(6c)
=p^2+p\eta
\tag{8}
\]
points. The representation counts follow directly from the standard identity \(\sum_{x\in\mathbb F_p}\chi(d-x^2)=-\chi(-1)\) when \(d\ne0\), with its elementary zero case.

Inclusion–exclusion for the union of the three components yields
\[
U=2p^2+(p^2+p\eta)-\bigl(p+2H\bigr)+J
=3p^2+p(\eta-3)+2\delta+J.
\tag{9}
\]
The set of points on at least two components is the union of their three pairwise intersections. Each of those intersection sets meets the other two precisely in the common \(J\)-point triple intersection. Hence
\[
I=p+2H-2J=3p-2\delta-2J.
\tag{10}
\]
Substitution of (9) and (10) into (6) proves (1), and algebra gives (2).

**4. The reversible Legendre-character split.** Set \(\varepsilon=\chi(-1)\). With \(\eta=\chi(6c)\) one has \(J=1+\varepsilon\eta\). Formula (2), viewed as a function of \(\eta\in\{-1,+1\}\), gives
\[
E_+-E_-=2p^2\bigl(p(1-2\varepsilon)+3\varepsilon\bigr).
\]
Taking \(\varepsilon=+1\) or \(-1\) yields (3). Both values occur: multiplication by a nonsquare exchanges the two unit classes. The formula only uses \(c\pmod p\), proving invariance under replacement \(c\mapsto c+pk\). Finally, expanding the fourth moment and averaging the character factors over \(R^2\) retains exactly the two additive collision congruences, proving (4).

## Verification
The dependency-free `artifacts/verify.py` computes pair-sum multiplicity tables *directly from the graph values*, independently of the three-factor reduction. Its exact integer program checks (1) for all coefficient choices \(c\in\{1,2,1+p,2+p\}\) and primes \(p\in\{5,7,11,13,17\}\). It separately enumerates the three-component geometry modulo each of nine primes through \(31\), verifying (9), (10), both conic intersections, the triple intersection, and (6). The completed test reports `PASS direct_fibers=518996 residue_points=328460 cases=20 moduli=5 geometry_primes=9 pure_comparison=1 phase_split=5`. Additional checks test the class-order reversal for five primes and the pure-quartic comparison at \(p=5\).

The computations establish the stated finite checks; the exact algebraic argument above establishes (1)–(4) for *all* primes and unit coefficients in scope.

## Relationship to prior work
Hickman and Wright [1] formulate finite-ring Fourier restriction for polynomial graphs and investigate estimates on prime-power rings. Their polynomial-graph setup includes the kind of graph considered here, but the inspected general setup and restriction sections do not give a unit-perturbed quartic fourth-moment formula or the residue-class reversal (3). Mockenhaupt and Tao [2] develop the finite-field extension and additive-collision mechanism, not the singular-lift count of (6) over a nonfield ring.

Exact energy formulas for the unperturbed quartic graph over finite fields are known. Those statements concern \((x,x^4)\), not the present \((x,x^4+cx^2)\) with \(p\nmid c\). The quadratic coefficient is not a mere constant or linear shear of the graph. In a simple affine parameter change, a nonzero translation introduces a cubic coefficient, while a pure scaling leaves a unit quadratic coefficient; this is not an affine normalization of the unperturbed equation. More decisively, the computed energies generally differ even at the same prime, for example at \(p=5\), the pure quartic energy is \(2225\) while coefficients \(c=1\) and \(c=2\) give \(2925\) and \(3025\), respectively (these comparison values can be checked directly with the provided code). Thus the established field energy formula does not imply the displayed unit-deformation invariant.

Results for prime-square *parabolic* Fourier extension instead concern \((x,x^2)\), including sharp operator norms and packet extremizers; no substitution supplies the unit-deformed quartic collision congruence (5). The displayed statement is a constant-input fourth moment, not an assertion of an optimal operator norm or an improvement of an established restriction bound.

## Limitations
The result is limited to primes \(p\ge5\), exponent-two rings, and unit quadratic perturbations. It does not classify individual two-sum fiber multiplicities, establish sharp unrestricted extension norms, or address the singular-parameter regime \(p\mid c\). Its originality assessment is by comparison with identified primary and published sources; older or unindexed equivalent arithmetic counts are possible. Independent validation has not been performed.

## References
1. J. Hickman and J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo N*, arXiv:1801.03176v1 (first posted 9 January 2018), Discrete Analysis 2018:11; particularly Sections 2 and 6.
2. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234v1 (first posted 18 April 2002); Section 5.
3. *Exact additive energy of the finite-field quartic graph*, published mathematical note (2026); the pure finite-field graph, not this unit-perturbed prime-square graph.
4. *Exact parabolic Fourier deficit and extremizer rigidity over prime-square rings*, published mathematical note (2026); the quadratic graph, not this quartic deformation.
