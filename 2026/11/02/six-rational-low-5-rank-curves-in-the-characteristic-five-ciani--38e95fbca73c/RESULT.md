# Six rational low-\(5\)-rank curves in the characteristic-five Ciani family

## Finding
Let \(k=\overline{\mathbb F}_5\), and let \(U\subset\mathbb A^3_k\) be the smooth-parameter locus defined below. For the genus-three Ciani quartic \(C_{a,b,c}\) associated to a point \((a,b,c)\in U\), write \(f(C_{a,b,c})\) for the \(5\)-rank of its Jacobian. Then the locus \(\{f\le1\}\subset U\) is the union of exactly six geometrically irreducible, smooth, rational curves. Each is isomorphic, over \(\mathbb F_5\), to
\[
\mathbb A^1\setminus\{0,2,-2,\sqrt3,-\sqrt3\}.
\]
The six curves meet only at eight points, all defined over \(\mathbb F_{25}\) and none over \(\mathbb F_5\). At every such point exactly three components meet with independent tangent directions in the smooth threefold \(U\). These eight points comprise exactly the superspecial locus (equivalently, the \(5\)-rank-zero locus).

For every \(m\ge1\), let \(q=5^m\) and let \(\epsilon_m=0\) for odd \(m\) and \(\epsilon_m=1\) for even \(m\). The numbers of **normalized coefficient triples**, not isomorphism classes, with \(5\)-rank zero and one are respectively
\[
N_0(q)=8\epsilon_m,\qquad N_1(q)=6(q-3)-36\epsilon_m.
\]
At \(5\)-rank one the \(a\)-number is two and the Newton slopes are \(0,(1/2)^4,1\); at \(5\)-rank zero the \(a\)-number is three and all six Newton slopes are \(1/2\).

## Assumptions and scope
Work over the characteristic-five algebraic closure or its finite subfields. The marked normalized family is
\[
C_{a,b,c}:\quad x^4+y^4+z^4+a x^2y^2+b x^2z^2+c y^2z^2=0.
\]
Its smooth-parameter space is the principal open set
\[
U=\{(a,b,c): (a^2-4)(b^2-4)(c^2-4)(a^2+b^2+c^2-abc-4)\ne0\}.
\]
All equations for parameters, points, and components refer to this marked affine parameter space. No quotient by coordinate permutations, sign changes, or geometric curve isomorphisms is taken.

## Proof
**1. Elliptic quotients and Hasse equations.** The three coordinate-sign involutions yield elliptic quotients \(E_x,E_y,E_z\). Their Jacobians give an isogeny of degree \(8\) from \(\operatorname{Jac}(C)\) to \(E_x\times E_y\times E_z\), prime to five. For \(E_x\), complete the square in \(X=x^2\) to obtain the binary quartic equation
\[
W^2=(a^2-4)y^4+(2ab-4c)y^2z^2+(b^2-4)z^4.
\]
For a smooth elliptic double cover \(W^2=A y^4+B y^2z^2+Cz^4\) in characteristic five, its Hasse invariant vanishes precisely when the coefficient of \(y^4z^4\) in \((Ay^4+By^2z^2+Cz^4)^2\) vanishes, namely \(B^2+2AC=0\). Reducing this coefficient modulo five gives the three supersingularity equations
\[
\begin{aligned}
F_x&=a^2b^2+2a^2+2b^2+c^2-abc+2,\\
F_y&=a^2c^2+2a^2+b^2+2c^2-abc+2,\\
F_z&=b^2c^2+a^2+2b^2+2c^2-abc+2.
\end{aligned}
\]
An elliptic quotient is ordinary unless its associated \(F\) vanishes. Since the isogeny is prime to five, the Jacobian's \(5\)-rank equals three minus the number of vanishing \(F\)'s; its \(a\)-number and Newton slopes likewise split into elliptic factors.

**2. The six pairwise-intersection components.** Polynomial subtraction gives identities in \(\mathbb F_5[a,b,c]\):
\[
\begin{aligned}
F_x-F_y&=(a^2+1)(b^2-c^2),\\
F_x-F_z&=(b^2+1)(a^2-c^2),\\
F_y-F_z&=(c^2+1)(a^2-b^2).
\end{aligned}
\]
On \(U\) all three factors \(a^2+1,b^2+1,c^2+1\) are invertible, because in characteristic five \(v^2+1=v^2-4\). Therefore \(F_x=F_y=0\) forces \(c=\varepsilon b\) for exactly one \(\varepsilon\in\{1,-1\}\). On this plane the remaining equation is
\[
(b^2+2)a^2-\varepsilon b^2a+3b^2+2=0.
\]
For \(\varepsilon=1\), the two roots are \(a=2\) and \(a=(4b^2+1)/(b^2+2)\). For \(\varepsilon=-1\), they are \(a=-2\) and \(a=(b^2+4)/(b^2+2)\). The constant roots are excluded from \(U\). At a zero of \(b^2+2\), the remaining linear equation has only that excluded constant root; hence there is no missing point at the denominator pole.

Thus the two components of \(\{F_x=F_y=0\}\cap U\) have explicit parametrizations
\[
P_+(t)=\left(\frac{4t^2+1}{t^2+2},t,t\right),\qquad
P_-(t)=\left(\frac{t^2+4}{t^2+2},t,-t\right).
\]
Substitution into the smoothness factors, for both signs, gives
\[
(a^2-4)=\frac{2t^2(t^2+1)}{(t^2+2)^2},\quad
b^2-4=c^2-4=t^2+1,\quad
a^2+b^2+c^2-abc-4=\frac{3t^2(t^2+1)^2}{(t^2+2)^2}.
\]
It follows that the exact parameter domain is \(t\notin\{0,\pm2,\pm\sqrt3\}\). Both maps are isomorphisms onto their components, with inverse the second coordinate. Cyclic permutations of coordinates yield the two components for each of the other two pairs. Different components from the same pair are disjoint on \(U\), since \(t\ne0\); a point common to different pairs necessarily has all three \(F\)'s zero.

**3. Triple crossings.** If all three \(F\)'s vanish, their pairwise differences and smoothness imply \(a^2=b^2=c^2\). Thus write
\[
(a,b,c)=(\varepsilon\delta t,\delta t,\varepsilon t),\qquad \varepsilon,\delta\in\{1,-1\}.
\]
Every \(F\) then becomes \(t^4-t^3+2\), which factors in \(\mathbb F_5[t]\) as
\[
t^4-t^3+2=(t-2)^2(t^2-2t-2).
\]
Smoothness excludes \(t=2\). The quadratic factor is separable and irreducible over \(\mathbb F_5\), since its discriminant is \(2\), a nonsquare. Its two roots, times the four sign choices, give eight distinct points in \(U(\mathbb F_{25})\). At the roots \(a^2+b^2+c^2-abc-4=3\ne0\).

For transversality, the gradients of \(F_x-F_y\) and \(F_x-F_z\) impose independent linear equations at a triple point; they have nonzero coefficients because \(t\ne0\) and \(t^2+1\ne0\). Their common tangent is the signed diagonal. The derivative of the restriction \(t^4-t^3+2\) to that diagonal equals \(t^2(4t-3)\), nonzero at either quadratic root. Hence the three \(F\)-divisors have independent differentials. Every triple point lies on precisely three of the six rational component curves, crossing with the three coordinate-axis tangent directions.

**4. Finite-extension counts.** In \(\mathbb F_{5^m}\), each of the six components contains exactly \(q-3-2\epsilon_m\) rational points: the two roots of \(t^2-3\) are rational precisely when \(m\) is even. All eight triple points are rational precisely when \(m\) is even. Summing the six component counts, each triple point is counted three times whereas each \(5\)-rank-one point is counted once. Thus \(N_1=6(q-3-2\epsilon_m)-3(8\epsilon_m)=6(q-3)-36\epsilon_m\), and \(N_0=8\epsilon_m\), as claimed.

## Verification
The independent symbolic script `verify_symbolic.py` checks the quotient Hasse formula, all three divisor-difference identities, both rational parametrizations, the smoothness factors, and the triple-point factorization using exact polynomial operations modulo five. The self-contained `verify_ciani_p5.py` enumerates all smooth normalized triples over \(\mathbb F_5\) and \(\mathbb F_{25}\) and independently checks the six parameter maps and their incidence multiplicities. It obtains 12 rank-one and zero rank-zero triples over \(\mathbb F_5\), and 96 rank-one and eight rank-zero triples over \(\mathbb F_{25}\). The infinite-field statements and all-extension formula follow from the preceding algebraic argument, not from extrapolation of finite enumeration.

Run `python3 verify_symbolic.py` (with SymPy) and `python3 verify_ciani_p5.py` (Python standard library only). Their actual outputs are recorded in `verification_output.txt`.

## Relationship to prior work
The Ciani family and automorphism structure are classical. Lercier–Ritzenthaler–Rovetta–Sijsling, arXiv:1403.0562 (first public version 2014-03-03), develops representative families and their moduli interpretations, including the Ciani quartic. Ohashi, arXiv:2201.12996 (2022), proves the smoothness criterion, writes the three elliptic quotients and degree-eight isogeny explicitly, and studies *superspecial* Ciani quartics and maximality. Ohashi also cites Brock's 1993 thesis for earlier superspecial enumerations. The statement proved here is not the known elliptic decomposition or the isolated superspecial condition: it identifies the entire \(5\)-rank-one (two-supersingular-quotient) geometry as six rational components, their eight transverse triple crossings, and exact coefficient counts over every finite extension. Those geometric incidence and rank-one counting conclusions were not found explicitly in the inspected sources; priority outside indexed/accessibly inspected literature remains unresolved.

## Limitations
This is a classification in the normalized **marked coefficient** family, not a count of curve isomorphism classes and not a description of the coarse moduli quotient. It does not give the full counts of rank-two and rank-three parameters, nor does it generalize to characteristics other than five. The two computations over small fields confirm but do not prove the geometric claims. The 1993 Brock thesis could not be inspected in full, leaving residual historical-priority risk. The result has not been independently audited.

## References
1. R. Lercier, C. Ritzenthaler, F. Rovetta, J. Sijsling, *Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields*, arXiv:1403.0562, first version 2014-03-03. https://arxiv.org/abs/1403.0562
2. R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996, 2022, especially Lemma 2.1, Section 3, and Theorem 1.1. https://arxiv.org/abs/2201.12996
3. N. Brock, *Superspecial curves of genera two and three*, 1993 thesis, cited as Theorem 3.15 in Ohashi; full text not inspected here.
