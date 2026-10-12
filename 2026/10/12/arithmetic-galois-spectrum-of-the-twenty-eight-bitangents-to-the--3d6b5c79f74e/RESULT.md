# Arithmetic Galois spectrum of the twenty-eight bitangents to the order-forty-eight quartic

## Finding
Let \(C\subset\mathbb P^2_{\mathbb Q}\) be the smooth plane quartic
\[
X^4+Y^4+XZ^3=0.
\]
Its \(28\) geometric bitangent lines form exactly five orbits under \(\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q)\), of sizes
\[
1,\quad1,\quad2,\quad8,\quad16.
\]
The minimal common field of definition of all \(28\) lines is the Galois extension
\[
K=\mathbb Q\!\left(i,\sqrt3,\alpha\right),\qquad
\alpha^4=\frac{3+2\sqrt3}{12},\qquad [K:\mathbb Q]=16.
\]
In particular, exactly two bitangent lines are individually defined over \(\mathbb Q\).

For every prime \(p\ge5\), the reduction \(C_p\) is smooth and has \(28\) distinct geometric bitangents. Its number \(N_p\) of \(\mathbb F_p\)-rational bitangent lines is
\[
N_p=\begin{cases}
2,&p\equiv5\pmod{12},\\
4,&p\equiv7,11\pmod{12},\\
28,&p\equiv1\pmod{12}\ \text{and}\ (3+2r)/12\ \text{is a fourth power in}\ \mathbb F_p,\\
4,&p\equiv1\pmod{12}\ \text{and that element is not a fourth power},
\end{cases}
\]
where in the final two cases \(r\in\mathbb F_p\) is either square root of \(3\); the fourth-power test is independent of that choice. The natural densities of primes with \(N_p=2,4,28\) are respectively \(1/4,11/16,1/16\).

## Assumptions and scope
A bitangent means an individual projective line whose scheme-theoretic intersection divisor on the smooth quartic is twice a divisor of degree two; hyperflexes count as bitangents. We consider the fixed integral equation above, its reduction at every prime \(p\ge5\), and rationality of the **lines**, not their contact points. All algebraic roots below lie in a fixed algebraic closure. Characteristic two and three are excluded.

## Proof
**Exhaustion of lines.** The polynomial has partial derivatives \(4X^3+Z^3\), \(4Y^3\), and \(3XZ^2\). They have no common projective zero when the characteristic is greater than three, so each \(C_p\) is smooth. The line \(Z=0\) meets the curve in four reduced points; it is not bitangent. Every remaining line is either \(X=\lambda Z\) or \(Y=mX+cZ\). For \(X=\lambda Z\), the intersection equation is \(Y^4+(\lambda^4+\lambda)Z^4\), a square of a quadratic precisely when \(\lambda^4+\lambda=0\). These four lines have parameters \(\lambda=0\) and the three roots of \(\lambda^3=-1\). A line \(Y=mX\) passes through \([0:0:1]\), where it has simple intersection multiplicity: its restricted equation is \((1+m^4)X^4+XZ^3\). If its fourth-degree coefficient vanishes it instead has multiplicities one and three, so none is bitangent.

For \(c\ne0\) write \(k=mc^3\), substitute \(X=c^4T,Z=1,Y=c(1+kT)\), and divide the resulting equation by \(c^4\). The resulting quartic is
\[
(c^{12}+k^4)T^4+4k^3T^3+6k^2T^2+(4k+1)T+1.
\]
Because its constant term is one, any square root polynomial may be normalized to have constant term one. Its linear and quadratic coefficients force the square root to be \(A T^2+B T+1\) with
\[
B=2k+\tfrac12,\qquad A=k^2-k-\tfrac18.
\]
Comparing the cubic and quartic coefficients gives exactly
\[
24k^2+12k+1=0,\qquad c^{12}=A^2-k^4.
\tag{1}
\]
The two roots of the first equation and the corresponding right-hand sides are
\[
k_{\pm}=\frac{-3\pm\sqrt3}{12},\quad
 a_{\pm}=\frac{3\pm2\sqrt3}{12},\quad
 A(k_+)^2-k_+^4=a_-^3,\quad A(k_-)^2-k_-^4=a_+^3.
\tag{2}
\]
The two values \(k_\pm\) are distinct in every characteristic greater than three, both \(a_\pm\) are nonzero since \(a_+a_-=-1/48\), and each equation \(c^{12}=a_{\mp}^3\) has twelve distinct solutions in the algebraic closure. As a line recovers \(c\) and then \(k=mc^3\) uniquely, equations (1)–(2) yield exactly \(24\) other bitangents. Together with the four hyperflex lines, these are the \(28\) distinct geometric bitangents for every \(p\ge5\).

**Splitting field and orbits.** Set \(F=\mathbb Q(i,\sqrt3)=\mathbb Q(\zeta_{12})\), where \(\zeta_{12}=(\sqrt3+i)/2\), and put
\[
\gamma=\frac{(1+i)(1+\sqrt3)}2,\qquad
\gamma^4=\frac{a_+}{a_-}.
\]
For \(\alpha^4=a_+\), all solutions in (2) are
\[
 c=\alpha\zeta_{12}^j\ \text{when } k=k_-,\qquad
 c=(\alpha/\gamma)\zeta_{12}^j\ \text{when } k=k_+,
 \qquad 0\le j<12.
\]
This proves every bitangent is defined over \(K=F(\alpha)\). Because \(a_+a_-=-1/48\) is **not a square** in \(\mathbb Q(i)\), \(a_+\) cannot be a square in \(F\): otherwise its norm from \(F\) to \(\mathbb Q(i)\) would be a square. The nonsquare assertion follows since a square in \(\mathbb Q(i)\) that is a negative rational is the negative of a rational square, while \(1/48\) is not a rational square. Since \(i\in F\), the binomial \(U^4-a_+\) is therefore irreducible over \(F\); hence \([K:F]=4\) and \([K:\mathbb Q]=16\). The display above and the relation for \(\gamma\) show that the splitting field is stable under all conjugations of \(i\), \(\sqrt3\), and \(\alpha\), hence is Galois.

The four vertical bitangents have rational orbit sizes \(1,1,2\). Among the other lines, the eight roots of
\[
P_8(U)=48U^8-24U^4-1
\]
are the fourth roots of \(a_+\) and \(a_-\). They lie in the degree-eight real field \(\mathbb Q(\alpha)\), as \(\sqrt3=6\alpha^4-3/2\); their minimal polynomial has degree eight because \(a_+\) is not a square in \(F\), so this is one orbit of eight distinct lines. The remaining sixteen values \(c\), with \(c^4\in\{a_+\zeta_3,a_+\zeta_3^2,a_-\zeta_3,a_-\zeta_3^2\}\), are precisely the roots of
\[
P_{16}(U)=2304U^{16}+1152U^{12}+624U^8-24U^4+1.
\]
Any such \(c^4\) generates \(F\) over \(\mathbb Q\): its degree-four minimal polynomial is \(2304V^4+1152V^3+624V^2-24V+1\), irreducible over \(\mathbb Q\). Because \(c\) then generates \(F(c)=K\) over \(\mathbb Q\), the sixteen lines form one orbit. Thus the orbit sizes are exactly \(1+1+2+8+16\), and because a degree-sixteen bitangent has coefficient field \(K\), this is the **minimal common** field.

**Reduction counts.** Over \(\mathbb F_p\), the four vertical candidates contribute \(1+\gcd(3,p-1)\) rational lines. The nonvertical lines require \(\sqrt3\in\mathbb F_p\), so for \(p\equiv5,7\pmod{12}\) there are none. For \(p\equiv11\pmod{12}\), only the \(j=0\) fourth-power tests of \(a_+\) or \(a_-\) can produce rational \(c\). Their product \(-1/48\) is a nonsquare for these primes and the multiplicative group has order congruent to two modulo four; exactly one of the two elements is a square, yielding exactly two nonvertical lines. For \(p\equiv1\pmod{12}\), all elements of \(F\), including \(\gamma\) and \(\zeta_{12}\), reduce to the prime field. Since \(a_+/a_-\) and each cube root of unity are fourth powers there, either all twenty-four or none of the nonvertical bitangents are rational according as \(a_+\) is, or is not, a fourth power. The condition is symmetric in the choice of \(\sqrt3\), proving the formula, including the small primes \(5,7,11,13\).

Finally, \(K/\mathbb Q\) is Galois of degree sixteen and generated by the line coefficients. Thus all twenty-eight bitangents descend to a prime field precisely for primes splitting completely in \(K\), apart from finitely many ramified primes. Chebotarev gives density \(1/16\) for \(N_p=28\). The class \(p\equiv5\pmod{12}\) has Dirichlet density \(1/4\) and exactly \(N_p=2\); all remaining primes have \(N_p=4\), giving density \(11/16\).

## Verification
The accompanying standalone `verify.py` uses exact SymPy rational and algebraic arithmetic to verify both elimination identities, the \(\gamma\)-identity, both minimal polynomials, and irreducibility. It independently enumerates line restrictions and perfect-square tests for all \(44\) primes in the interval \(5\le p<200\), including \(p=5,7,11,13,37\). Its output is `VERIFY_OK`. These computations are supplementary checks; the proof for every prime and the density statement are the symbolic and field-theoretic arguments above.

## Relationship to prior work
M. Janasz, *On symmetric plane quartic curves* (2024), supplies explicit bitangent equations, the \(28\)-line complex incidence arrangement, and free-curve calculations for this quartic. Its parametrizations establish geometric existence and an algebraic upper bound, but the exact minimal common field, arithmetic Galois orbit partition, and counts for **every prime** are not stated there. Bethea–Brazelton (2024) analyze **complex projective automorphism-group** orbits of the relevant symmetric quartic, with a \(24+4\) partition; this differs from the Galois action over \(\mathbb Q\) calculated here. The former and latter results are not claimed as new. The arithmetic classification is the present assertion; no absence-of-prior-literature assertion is proved by unsuccessful searches.

## Limitations
The theorem is restricted to the displayed rational model and characteristics \(p\ge5\). It classifies rational bitangent **lines**, not their contact divisors, incidence points, or fields of all tangent contact points. Characteristic two and three are excluded. The cited complex-geometric results are previously known, and literature searching cannot exclude an unindexed prior arithmetic treatment. Independent validation of the present analysis has not been performed.

## References
1. M. Janasz, *On symmetric plane quartic curves*, arXiv:2406.07015v1 (publicly posted June 11, 2024), especially the bitangent parametrizations and incidence theorem. https://arxiv.org/abs/2406.07015
2. C. Bethea and T. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242v1 (October 11, 2024), Type III automorphism-orbit calculation. https://arxiv.org/abs/2410.09242
3. Chebotarev density theorem and elementary theory of splitting in Galois extensions (standard results).
