# Cyclotomic rigidity of the first short cycles of the reciprocal map over finite fields

## Finding
For every prime power \(q=p^r\), let \(f(x)=x+x^{-1}\) over \(\mathbb F_q\), evaluated only when the current iterate is nonzero. Let \(N_j(q)\) denote the number of points with well-defined *least* positive period \(j\). There are no fixed points, and
\[
N_2(q)=\begin{cases}0,&p=2,\\2,&p\ne2\text{ and }-2\text{ is a square in }\mathbb F_q,\\0,&\text{otherwise},\end{cases}
\]
\[
N_3(q)=\begin{cases}
3,&p=2\text{ and }3\mid r,\\
6,&p>3\text{ and }q\equiv1\pmod 9,\\
0,&\text{otherwise}.
\end{cases}
\]
Thus there are exactly \(N_2(q)/2\) distinct two-cycles and \(N_3(q)/3\) distinct three-cycles, with no further cycles of lengths at most three. Moreover, in characteristic zero the third-period polynomial
\[
P_3(X)=3X^6+9X^4+6X^2+1
\]
has splitting field \(\mathbb Q(\zeta_9)\), and its six roots are \((\zeta_9^a-\zeta_9^{-a})^{-1}\) for \(a\in(\mathbb Z/9\mathbb Z)^\times\). The map permutes them by multiplying the index by \(-2\) modulo \(9\).

## Assumptions and scope
A periodic point is a nonzero element whose required iterates under the partially defined affine map \(f\) all exist and whose eventual return is to the original point. This is not a claim about points whose orbit reaches zero or about projective dynamics at infinity. The field may have any prime characteristic and any finite extension degree. The characteristic-zero splitting-field assertion concerns the displayed polynomial over \(\mathbb Q\).

## Proof
**Rational-iteration identities.** Direct composition in \(\mathbb Q(X)\) gives
\[
f(X)-X=\frac1X,\qquad
f^{\circ2}(X)-X=\frac{2X^2+1}{X(X^2+1)},
\]
and
\[
f^{\circ3}(X)-X=
\frac{3X^6+9X^4+6X^2+1}{X(X^2+1)(X^4+3X^2+1)}.
\]
These are rational identities with integer coefficients, so they reduce to every characteristic wherever denominators are nonzero. The numerator of the third identity and its denominator have integer resultant \(1\); alternatively, evaluate the numerator at the successive denominator roots to see that no common root exists, in any characteristic. Thus all zeros of \(P_3\) are valid three-periodic points. There are no fixed points by the first identity. Hence the second and third return equations describe *least* periods two and three, respectively.

**Period two.** If \(p=2\), the second numerator is \(1\), so there are no period-two points. Otherwise it is \(2X^2+1\), which has exactly two distinct roots in \(\mathbb F_q\) if \(-1/2=-2^{-1}\) is a square and none otherwise. This has the same quadratic character as \(-2\), because their quotient is a square. For either root, \(f(X)=-X\); the two roots form one cycle.

**Cyclotomic structure of period three.** Suppose first that the characteristic is not three, and fix a primitive ninth root of unity \(\zeta\) in an algebraic closure. For \(a\) prime to nine put \(u_a=\zeta^a-\zeta^{-a}\), \(t_a=\zeta^a+\zeta^{-a}\), and \(x_a=u_a^{-1}\). We have \(t_a^3-3t_a+1=0\) since \(\zeta^{3a}+\zeta^{-3a}=-1\). Therefore \(t_a(t_a^2-3)=-1\), while \(u_a^2=t_a^2-4\). Squaring the relation \(t_a(u_a^2+1)=-1\) yields
\[
(u_a^2+4)(u_a^2+1)^2=1.
\]
On substituting \(u_a=x_a^{-1}\) and clearing denominators one obtains \(P_3(x_a)=0\). Moreover,
\[
f(x_a)=\frac{1+u_a^2}{u_a}=-\frac1{u_at_a}=-x_{2a}=x_{-2a}.
\]
For odd characteristic, the six values \(x_a\) are pairwise distinct: equality of \(u_a\) and \(u_b\), with \(A=\zeta^a,B=\zeta^b\), implies \((A-B)(1+(AB)^{-1})=0\). The second factor cannot vanish because \(-1\) has order two, whereas \(AB\) has odd order. Hence \(a=b\pmod9\). They exhaust the six roots of \(P_3\), and the index action \(a\mapsto -2a\pmod9\) consists of two three-cycles. For \(q\) of characteristic greater than three, the Frobenius \(x_a\mapsto x_{qa}\) fixes such a root exactly if \(q\equiv1\pmod9\); if so, all six roots lie in \(\mathbb F_q\), and otherwise none does. In characteristic zero, the distinct six Galois conjugates of \(x_1\) prove \([\mathbb Q(x_1):\mathbb Q]=6\). As \(x_1\in\mathbb Q(\zeta_9)\), whose degree is six, its splitting field is exactly \(\mathbb Q(\zeta_9)\).

**Exceptional characteristics.** In characteristic three, \(P_3(X)=1\), so no period-three points exist. In characteristic two,
\[
P_3(X)=(X^3+X^2+1)^2.
\]
The cubic has no root in \(\mathbb F_2\) and is irreducible, with three distinct roots in \(\mathbb F_8\). They form one exact three-cycle (the rational return identity applies and no fixed points exist). They all lie in \(\mathbb F_{2^r}\) if and only if \(3\mid r\), proving the remaining case.

## Verification
The included standard-library Python program `verify_cycles.py` constructs finite fields by irreducible polynomial quotients and directly enumerates periodic points, never inferring infinite statements from finite enumerations. Executing it returned `VERIFY_OK prime_fields=168 extension_fields=19 all_exact_2_and_3_cycles_match`. It tests both least periods for every prime field of order at most \(1000\), plus nineteen extensions in characteristics \(2,3,5,7,11,13,17,19\). Separately, symbolic cancellation of the displayed iteration identities and exact integer resultant \(\operatorname{Res}(P_3,D)=1\) were checked. The proof, not the finite testing, establishes the theorem for all prime powers.

## Relationship to prior work
The rational map \(x\mapsto x+x^{-1}\) arises in the transformation of reciprocal-sum recurrences studied by Matijasevick, Rodríguez, and Salazar, *Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields*, arXiv:2610.00765, initially public September 30, 2026. Their accessible abstract concerns rational integrality and quadratic-field inertness, not finite-field short periodic orbits. The complete primary text could not be inspected, so coverage in an uninspected section is a material residual priority risk. Searches for rational-map period-three cycles, the exact sextic, cyclotomic ninth-root descriptions, and equivalent finite-field criteria found no covering statement in accessible sources or the checked public mathematical research records. Absence of a search hit is not proof of novelty.

## Limitations
No claims are made for least periods greater than three, for integral or rational starting values, or for periodic dynamics on a projective compactification with conventions at poles. The associated 2026 primary article's complete text was unavailable for full-text coverage comparison. This result has undergone self-review only, not independent audit or independent priority verification.

## References
1. M. Matijasevick, S. Rodríguez, G. Salazar, *Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields*, arXiv:2610.00765 (first public 2026-09-30), https://arxiv.org/abs/2610.00765.
2. Standard finite-field fact: \(\mathbb F_q^\times\) is cyclic and \(\mathbb F_q\cap\mu_9\) has order \(\gcd(q-1,9)\); used through Frobenius and the explicit ninth-root parametrization.
