# A double Hasse divisor for genus-ten generalized Fermat curves in characteristic seven

## Finding
Let \(k=\overline{\mathbb F}_7\). For every \(\lambda\in k\setminus\{0,1\}\), let \(C_\lambda\) be the smooth projective curve whose function field is
\[
k(x,u,v,w),\qquad u^3=x,\quad v^3=x-1,\quad w^3=x-\lambda.
\]
This is the connected generalized Fermat cover of type \((3,3)\), of genus \(10\), ramified over \(0,1,\lambda,\infty\). Define
\[
A(\lambda)=\lambda^2-\lambda-1,\qquad
B(\lambda)=\lambda^2+\lambda-1,\qquad
D(\lambda)=\lambda^2-3\lambda+1.
\]
Its Jacobian has \(7\)-rank \(10\) and \(a\)-number \(0\) whenever \(ABD\ne0\), and \(7\)-rank \(8\) and \(a\)-number \(2\) whenever \(ABD=0\). No intermediate ranks occur. The three quadratics are pairwise coprime, separable, and irreducible over \(\mathbb F_7\); thus the nonordinary locus consists of precisely six parameters, all in \(\mathbb F_{49}\setminus\mathbb F_7\). They constitute one orbit under the six anharmonic changes of coordinate, equivalently the unique unordered four-branch-point configuration having
\[
j_{\rm br}=256\frac{(\lambda^2-\lambda+1)^3}{\lambda^2(\lambda-1)^2}=4\quad\text{in }k.
\]
The determinant of the Hasse–Witt coefficient matrix (the seventh powers of the semilinear Cartier scalars), in the explicit eigenbasis constructed below, is
\[
\lambda^6(\lambda-1)^6 A(\lambda)^2B(\lambda)^2D(\lambda)^2.
\]
Thus the nonordinary Hasse divisor has multiplicity exactly \(2\) at each of the six ordered parameters and at the single unramified moduli point \(j_{\rm br}=4\). The Newton slopes are \(0^{10},1^{10}\) at ordinary parameters and \(0^8,(1/2)^4,1^8\) at the six exceptional parameters.

## Assumptions and scope
All statements concern the smooth projective connected Kummer cover over the algebraic closure of the field with seven elements. The branch parameter excludes \(0,1\). The deck group is \((\mathbb Z/3\mathbb Z)^3\) and the four inertia groups are cyclic of order \(3\). Tame Riemann–Hurwitz gives
\[
2g-2=27(-2)+4\cdot9\cdot2=18,\quad g=10.
\]
The rank is that of the geometric \(7\)-torsion étale part of the Jacobian; its \(a\)-number is the dimension of the kernel of Cartier on holomorphic differentials. Neither statement is a census of arbitrary genus-ten curves.

## Proof
**Character eigenspaces.** The automorphism group has order prime to \(7\), so the regular differentials split as its character eigenspaces. Take one representative \(a=(a_0,a_1,a_\lambda)\) from each of the \(13\) nonzero pairs \(\{a,-a\}\) in \((\mathbb Z/3\mathbb Z)^3\), and put
\[
f_a=x^{a_0}(x-1)^{a_1}(x-\lambda)^{a_\lambda},\qquad y_a=u^{a_0}v^{a_1}w^{a_\lambda}.
\]
A differential with this character is of the form \(h(x)\,dx/y_a^j\), for \(j=1,2\). At a finite branch point of exponent \(a_i\), the local valuation is \(2-ja_i+3\operatorname{ord}_{x=r_i}h\). Hence the minimal polynomial numerator is \(h=\prod_{a_i=2}(x-r_i)\) when \(j=2\), and \(h=1\) when \(j=1\). At infinity, if \(s=a_0+a_1+a_\lambda\) is divisible by \(3\), regularity requires \(\deg h\le js/3-2\); otherwise it requires \(3\deg h\le js-4\). These bounds give exactly ten nonzero character eigenspaces, all one-dimensional (and no others). The following table lists every eigenform and its Hasse–Witt coefficient (the seventh power of its Cartier scalar); the exponent \(j\) specifies the denominator of \(h\,dx/y_a^j\).

| \(a\) | \(j\) | \(h\) | Hasse–Witt coefficient \(q_{a,j}\) |
| --- | --- | --- | --- |
| \((0,1,1)\) | \(2\) | \(1\) | \(-(\lambda-1)^2\) |
| \((1,0,1)\) | \(2\) | \(1\) | \(-\lambda^2\) |
| \((1,1,0)\) | \(2\) | \(1\) | \(-1\) |
| \((1,1,1)\) | \(2\) | \(1\) | \(-\lambda^2(\lambda-1)^2\) |
| \((1,1,2)\) | \(1\) | \(1\) | \(-A\) |
| \((1,1,2)\) | \(2\) | \(x-\lambda\) | \(-A\) |
| \((1,2,1)\) | \(1\) | \(1\) | \(B\) |
| \((1,2,1)\) | \(2\) | \(x-1\) | \(\lambda^2B\) |
| \((1,2,2)\) | \(1\) | \(1\) | \((\lambda-1)^2D\) |
| \((1,2,2)\) | \(2\) | \((x-1)(x-\lambda)\) | \(D\) |

**Cartier calculation.** Because \(7\equiv1\pmod3\), Cartier preserves each of the ten one-dimensional eigenspaces. For \(\omega=h(x)\,dx/y_a^j\), rewrite
\[
\omega=(hf_a^{2j})\,dx/y_a^{7j}.
\]
The seventh power of the Cartier scalar is the coefficient of \(x^{6+7\deg h}\) in \(hf_a^{2j}\), with its seventh root understood under the semilinearity convention. Expanding the product gives the ten Hasse–Witt coefficients in the table. The rank and stable rank of Cartier are equal: on each one-dimensional preserved eigenspace a nonzero semilinear map is bijective, and a zero map stays zero. Four coefficients never vanish on the smooth parameter domain; each of \(A,B,D\) appears in exactly two further coefficients. As the three quadratics have disjoint simple roots, the Cartier rank is \(10\) off their union and \(8\) on it. The geometric \(7\)-rank equals the stable Cartier rank, and the \(a\)-number is \(10-\operatorname{rank}\mathcal C\).

**Moduli divisor.** Each of \(A,B,D\) has discriminant \(5\), a nonsquare in \(\mathbb F_7\); their pairwise greatest common divisors are \(1\). The six roots therefore lie in \(\mathbb F_{49}\setminus\mathbb F_7\). Multiplication of the ten Hasse–Witt entries yields the displayed polynomial determinant. In \(\mathbb F_7[\lambda]\) there is the exact identity
\[
256(\lambda^2-\lambda+1)^3-4\lambda^2(\lambda-1)^2=4A(\lambda)B(\lambda)D(\lambda).
\]
The six solutions are precisely the six preimages of \(j_{\rm br}=4\); each is simple in that equation. The cross-ratio map is therefore unramified at them, and its full anharmonic orbit has size six. Consequently the order-two determinant vanishing descends to the unique moduli point with multiplicity two. Finally, rank \(8\) leaves a \(2\)-dimensional nonordinary factor in the Newton slope decomposition; symmetry and denominator divisibility force the remaining four slopes all to be \(1/2\).

## Verification
The accompanying standalone `verify_genus10.py` uses only the Python standard library. Run `python verify_genus10.py`. It enumerates the thirteen character pairs and checks that the local pole bounds produce exactly ten differential eigenlines. It computes each Hasse–Witt coefficient (the seventh power of its Cartier scalar) both by sparse bivariate polynomial expansion over \(\mathbb F_7\) and independently by binomial summation; it checks all ten against the displayed table. Exact polynomial arithmetic verifies pairwise coprimality, absence of rational roots, splitting in \(\mathbb F_{49}\), the cross-ratio identity, and the determinant factorization. These are symbolic identities over the whole algebraic closure, not extrapolations from an enumeration of rational parameters.

## Relationship to prior work
Carvacho–Hidalgo–Quispe (2015), especially their genus-ten \((3,3)\) example, establish the classical generalized Fermat curve and its Jacobian decomposition into cyclic-cover factors. This finding does not claim that decomposition. Hidalgo (2017) provides a general character basis and Cartier-operator framework for generalized Fermat curves in positive characteristic. Specializing that method is a useful independent comparison; the distinct contribution asserted here is the complete characteristic-seven rank locus, its reduction to one unordered moduli point, and the exact multiplicity-two Hasse divisor. Martínez-Núñez (2023) gives another general Jacobian decomposition, without this explicit moduli-stratum calculation in the inspected sections.

## Limitations
The result treats one characteristic and one classical one-dimensional family. Its Cartier computation, although exact, has not undergone independent external validation. General Cartier formulas may allow this calculation as a specialization, and historical priority for the explicit stratum remains open; the research comparison does not establish uniqueness in all literature. The branch-moduli point identifies an unordered four-point set, not a claimed classification of every possible geometric realization without the chosen generalized Fermat group.

## References
- M. Carvacho, R. A. Hidalgo, S. Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903 (initial public version 2015-07-10), especially the \((3,3)\) example.
- R. A. Hidalgo, *Holomorphic differentials of Generalized Fermat curves*, arXiv:1710.01349 (2017), sections on the standard differential basis and Cartier operator.
- G. Martínez-Núñez, *Decomposition of Jacobians of Generalized Fermat Curves*, arXiv:2303.18056 (2023).
