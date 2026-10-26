# Exact parity-dependent p-rank strata of characteristic-five Ciani quartics

## Finding
Let \(q=5^n\), \(n\ge 1\), and let \(U_q\) be the set of triples \((r,s,t)\in\mathbb F_q^3\) for which
\[
C_{r,s,t}: X^4+Y^4+Z^4+rX^2Y^2+sY^2Z^2+tZ^2X^2=0
\]
is smooth. Write \(\varepsilon=(-1)^n\). The numbers \(N_f(q)\) of **marked coefficient triples**, not isomorphism classes, with Jacobian \(5\)-rank \(f\) are exactly
\[
\begin{aligned}
N_0(q)&=4(1+\varepsilon),\\
N_1(q)&=6q-36-18\varepsilon,\\
N_2(q)&=3\bigl(q^2-10q+30+(15-2q)\varepsilon\bigr),\\
N_3(q)&=q^3-10q^2+42q-75+(6q-31)\varepsilon.
\end{aligned}
\]
In particular \(\#U_q=q^3-7q^2+18q-17\). The superspecial marked locus consists of exactly eight geometric points, all defined over \(\mathbb F_{25}\) and absent over odd-degree extensions of \(\mathbb F_5\). At rank \(f\), the Jacobian has \(a\)-number \(3-f\) and Newton slopes \(0\) with multiplicity \(f\), \(1/2\) with multiplicity \(2(3-f)\), and \(1\) with multiplicity \(f\).

## Assumptions and scope
All fields have characteristic five; coefficient triples are ordered and counted separately even if the resulting curves are isomorphic. The smooth locus is precisely
\[
U_q=\{(r,s,t): (r^2-4)(s^2-4)(t^2-4)\Delta\ne0\},\quad
\Delta=4+rst-r^2-s^2-t^2.
\]
The elliptic quotients by independent sign involutions give a prime-to-five isogeny from the Jacobian to their product. A fixed quotient is supersingular if and only if its quartic branch polynomial has zero genus-one Hasse invariant. All assertions are for every \(n\ge1\), without restriction on the parity of \(n\).

## Proof
**1. Quotients and Hasse equations.** The quotient by the involution \(Z\mapsto-Z\), after completing the square, has a genus-one equation
\[
v^2=(t^2-4)u^4+(2st-4r)u^2+(s^2-4).
\]
Over a field of characteristic five, the coefficient of \(u^4\) in the square of the right-hand quartic is the Hasse invariant. It vanishes exactly when
\[
H_r=(2st-4r)^2+2(s^2-4)(t^2-4)
=r^2-rst+s^2t^2+2s^2+2t^2+2=0.
\]
The other two quotient invariants \(H_s,H_t\) are obtained by cyclic permutation. Let \(T_i\) be the count in \(U_q\) of simultaneous zeros of a prescribed set of \(i\) distinct Hasse equations, for \(i=1,2,3\). The quotient isogeny has power-of-two degree, so it preserves \(5\)-divisible groups, and hence \(f=3-\#\{H_r,H_s,H_t\text{ vanishing}\}\) and \(a=3-f\). These same factors give the Newton slopes in the statement.

**2. Counting smooth coefficients.** Put \(S=\mathbb F_q\setminus\{2,-2\}\). For fixed \(s,t\in S\), the equation \(\Delta=0\) is quadratic in \(r\), with discriminant \((s^2-4)(t^2-4)\). Its number of \(r\)-roots before excluding \(r=\pm2\) is \(1+\chi(s^2-4)\chi(t^2-4)\), where \(\chi\) is the quadratic character with \(\chi(0)=0\). The sum \(\sum_{s\in S}\chi(s^2-4)=-1\). Among those roots, \(r=2\) happens only when \(s=t\), and \(r=-2\) only when \(s=-t\). Consequently the number of \(\Delta\)-zero triples inside \(S^3\) is
\[
(q-2)^2+1-2(q-2)=(q-3)^2.
\]
Therefore \(\#U_q=(q-2)^3-(q-3)^2=q^3-7q^2+18q-17\).

**3. A single vanishing Hasse invariant.** For \(s,t\in S\), completing a square gives
\[
H_r=(r+2st)^2+2(s^2+1)(t^2+1).
\]
Since \(\chi(3)=\chi(2)=(-1)^n=\varepsilon\), summing the number of \(r\)-roots yields \((q-2)^2+\varepsilon\) before omitting \(r=\pm2\). The identity
\[
H_r+\Delta=(s^2+1)(t^2+1)
\]
shows that \(H_r\) and \(\Delta\) cannot vanish together for \(s,t\in S\). For \(r=2\), the equation becomes
\[
(s^2+1)(t^2+1)+(s-t)^2=0.
\]
Viewed as a quadratic in \(t\), this has discriminant \(2(s^2+1)^2\). For odd \(n\), no solution has \(s,t\in S\). For even \(n\), each \(s\in S\) gives two solutions except the two solutions of \(s^2=-2\), which give one each (the coefficient of \(t^2\) is then zero); none of these solutions has \(t=\pm2\). Thus the boundary \(r=2\) contributes \((1+\varepsilon)(q-3)\) solutions, and \(r=-2\) contributes the same number by \(t\mapsto-t\). It follows that
\[
T_1=(q-2)^2+\varepsilon-2(1+\varepsilon)(q-3)
=q^2-6q+10+(7-2q)\varepsilon.
\]

**4. Pairs of vanishing equations.** Direct subtraction gives
\[
H_r-H_s=-(r^2-s^2)(t^2+1).
\]
On \(U_q\), \(t^2+1\ne0\). Hence any point with \(H_r=H_s=0\) has \(s=\pm r\). The case \(r=s=0\) would force \(t^2=-1\), outside \(U_q\), so the two branches are disjoint. On the branch \(s=r\), cancellation of the excluded factor \(t-2\) gives
\[
r^2=-2\frac{t+2}{t+1},\qquad t\notin\{-2,2,-1\}.
\]
The fractional linear transformation on the right takes the allowed finite \(t\)'s bijectively to \(\mathbb F_q\setminus\{0,4,3\}\). The number of square roots there is \(q-4-\chi(3)=q-4-\varepsilon\). The smoothness determinant is nonzero on these solutions: substituting the formula into \(\Delta\) gives \(- (t-2)^2(t+2)/(t+1)\), nonzero on the allowed set. The second branch contributes equally by \(t\mapsto-t\), so
\[
T_2=2(q-4-\varepsilon).
\]

**5. Triple vanishing.** The three pairwise differences force \(r^2=s^2=t^2\), which cannot be zero on a triple Hasse zero. Sign changes of two parameters reduce to \(r=s=t=a\), with four distinct marked triples for each \(a\). Then the Hasse equation reads
\[
a^4-a^3+2=(a-2)^2(a^2-2a-2)=0.
\]
The root \(a=2\) is singular and excluded. The irreducible quadratic has discriminant \(2\) over \(\mathbb F_5\), and its two roots lie in \(\mathbb F_{25}\). They are smooth: \(a^2=2a+2\) implies \(\Delta=2\), while \(a^2\ne4\). Hence
\[
T_3=4(1+\varepsilon).
\]

**6. Recovering the strata.** Inclusion–exclusion among the symmetric three Hasse conditions gives
\[
N_0=T_3,\qquad N_1=3(T_2-T_3),\qquad
N_2=3(T_1-2T_2+T_3),\qquad
N_3=\#U_q-3T_1+3T_2-T_3.
\]
Substitution proves all four displayed formulas, with no extrapolation from experimental finite fields.

## Verification
The standalone standard-library script `CHECKER.py` independently enumerates every smooth marked triple over \(\mathbb F_5\), \(\mathbb F_{25}\), and \(\mathbb F_{125}\), computes the three Hasse invariants, and compares exact rank strata and intersection counts with the universal formulas. It prints `FINITE FIELD CHECKS PASS`. The verified rank-count vectors, in order \(f=0,1,2,3\), are \((0,12,0,11)\), \((8,96,1110,10469)\), and \((0,732,43920,1801331)\), respectively. This finite evidence checks the implementation; the infinite-family statement rests on the preceding character-sum proof.

## Relationship to prior work
Lercier, Ritzenthaler, Rovetta and Sijsling (arXiv:1403.0562, first posted 2014-03-03) use the Ciani family in parametrizing genus-three plane quartics and enumerate isomorphism classes and Frobenius traces for primes at least eleven. Their results do not give the characteristic-five marked \(5\)-rank census above. Ohashi (arXiv:2201.12996, first posted 2022-01-31), Sections 2–4, establishes the smoothness criterion, explicit elliptic quotients, and arithmetic of superspecial Ciani curves, but not the simultaneous four-stratum marked counts over every extension of \(\mathbb F_5\). Brock's 1993 thesis treats superspecial genera two and three; its full text was not available for detailed comparison, so historical overlap for the rank-zero subcount remains possible. The present theorem's distinguishing claim is the complete **all-extension marked p-rank distribution** with its parity terms, not novelty of the Ciani family, the quotient isogeny, or generic superspecial criteria.

## Limitations
The counts are for ordered coefficients, not geometric or arithmetic isomorphism classes; twists and automorphism identifications are not divided out. Characteristic five, smooth curves, and this fixed normalized quartic equation are essential. No assertion is made about higher Ekedahl–Oort strata, explicit Frobenius characteristic polynomials, singular boundary curves, or independent external validation. More obscure historical enumerations might overlap despite the inspected literature.

## References
- R. Lercier, C. Ritzenthaler, F. Rovetta, J. Sijsling, *Parametrizing the moduli space of curves and applications to smooth plane quartics over finite fields*, arXiv:1403.0562v1 (2014-03-03), especially Sections 3 and 5.
- R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996v1 (2022-01-31), especially Lemma 2.1 and Sections 3–4.
- B. W. Brock, *Superspecial curves of genera two and three*, Princeton University PhD thesis (1993); identified from Ohashi's bibliography, complete text not inspected.
- E. Ciani, *I varii tipi possibili di quartiche piane più volte omologico-armoniche*, Rend. Circ. Mat. Palermo 13 (1899), 347–373; historical origin, bibliographic record only.
