# Exact sixth Fourier moment of cubic moment curves over cube-free moduli

## Finding
Let \(N>1\) be cube-free with \(\gcd(N,6)=1\), let \(d\geq3\), and define the moment curve
\[
\mathcal M_N^{(d)}=\{(t,t^2,\ldots,t^d):t\in\mathbb Z/N\mathbb Z\}\subseteq(\mathbb Z/N\mathbb Z)^d.
\]
Use the unitary Fourier transform
\[
\widehat f(\xi)=N^{-d/2}\sum_{x\in(\mathbb Z/N\mathbb Z)^d}f(x)e^{-2\pi i x\cdot\xi/N}
\]
and counting-measure \(\ell^r\) norms. For a nonempty support \(S\), put
\[
\mathcal C_6(S)=\sup_{0\ne f,\ \operatorname{supp}f\subseteq S}
\frac{\|\widehat f\|_\infty}{\|\widehat f\|_6}.
\]
For \(e\in\{1,2\}\), define
\[
A_1(p)=6-\frac9p+\frac4{p^2},\qquad
A_2(p)=16-\frac{27}{p}+\frac{12}{p^2}.
\]
Then the **exact sharp constant** is
\[
\boxed{\mathcal C_6(\mathcal M_N^{(d)})=
N^{-(d-3)/6}\prod_{p^e\parallel N}A_e(p)^{-1/6}.}
\]
Every nonzero extremizer is a scalar multiple of an additive-character modulation of the moment-curve indicator, equivalently its values at the distinct support points are
\[
f(t,t^2,\ldots,t^d)=\lambda\exp\!\left(\frac{2\pi i}{N}\sum_{j=1}^d a_jt^j\right),
\quad \lambda\ne0,\ a_j\in\mathbb Z/N\mathbb Z.
\]
The genuinely ramified ingredient is the exact six-variable power-sum count
\[
\boxed{J_{3,d}(p^2)=16p^6-27p^5+12p^4\quad(p\ge5\text{ prime}),}
\]
which is **not** obtained by squaring the prime-level factor.

In dimension \(d=3\), for any unbounded family of such cube-free moduli, uniform \(\ell^6\) spectral synthesis holds precisely when the number \(\omega(N)\) of distinct prime factors tends to infinity. In particular, \(\mathcal C_6(\mathcal M_{p^2}^{(3)})\to16^{-1/6}\) along primes, whereas \(\mathcal C_6(\mathcal M_p^{(3)})\to6^{-1/6}\). Thus passing from primes to their squares changes the limiting sharp constant but does not by itself produce endpoint synthesis.

## Assumptions and scope
The result uses ordinary residue rings, not finite fields of order \(p^2\). Cube-free means that each prime appears to exponent at most two. The condition \(\gcd(N,6)=1\) ensures that \(2\) and \(3\) are invertible modulo every prime divisor. The first coordinate of the moment curve is \(t\), so its parameterization has exactly \(N\) distinct points.

For \(s\ge1\), let \(J_{s,d}(N)\) count ordered pairs of \(s\)-tuples \(\mathbf t,\mathbf u\in(\mathbb Z/N\mathbb Z)^s\) with
\[
\sum_{i=1}^s t_i^k\equiv\sum_{i=1}^s u_i^k\pmod N\qquad(1\le k\le d).
\]
We evaluate \(J_{3,d}\) exactly. The classification of all \(\ell^6\) extremizers is a consequence of the already-known affine-symmetry principle; the new arithmetic input is the prime-square count and its product across cube-free moduli.

## Proof
**1. Only the first three power sums matter.** For a triple over any commutative ring in which \(2\) and \(3\) are units, Newton's identities recover its elementary symmetric functions \(e_1,e_2,e_3\) from the first three power sums \(P_1,P_2,P_3\):
\[
e_1=P_1,\quad 2e_2=e_1P_1-P_2,\quad 3e_3=e_2P_1-e_1P_2+P_3.
\]
Every later power sum obeys the recurrence
\[
P_k=e_1P_{k-1}-e_2P_{k-2}+e_3P_{k-3}\qquad(k\ge4).
\]
Therefore \(J_{3,d}(N)=J_{3,3}(N)\) for every \(d\ge3\) under the stated coprimality condition. The recurrence works over rings with zero divisors: it does not require unique factorization of polynomials into linear factors there.

**2. The prime factor.** Modulo a prime \(p>3\), Newton's identities show that two triples with the same three power sums have the same monic root polynomial. Unique factorization over \(\mathbb F_p\) says that the triples have identical multisets. Count ordered pairs by residue multiplicity: three distinct roots contribute \(36\binom p3\), a double root contributes \(9p(p-1)\), and a triple root contributes \(p\). Hence
\[
J_{3,d}(p)=36\binom p3+9p(p-1)+p
=p^3A_1(p).
\]

**3. The prime-square factor: all singular lifts included.** Fix \(p>3\). Reduce each of the six variables modulo \(p\). By Step 2, their two residue triples must be rearrangements of one multiset. Choose ordinary representatives \(a_i,b_i\in\{0,\ldots,p-1\}\) of such a pair and write the lifted variables as \(a_i+px_i\) and \(b_i+py_i\), with \(x_i,y_i\in\mathbb F_p\). Because \((a_i)\) and \((b_i)\) have the same multiset **as integers**, their base power sums agree exactly. Modulo \(p^2\), the three equations become the homogeneous linear system
\[
\sum_{i=1}^3 a_i^{k-1}x_i-\sum_{i=1}^3 b_i^{k-1}y_i=0
\quad\text{in }\mathbb F_p,\qquad k=1,2,3,
\]
after dividing the \(k\)-th equation by its invertible coefficient \(k\). If the residue multiset has \(r\in\{1,2,3\}\) distinct elements, the coefficient matrix has rank exactly \(r\): identical residues yield identical columns, while the first \(r\) powers give a nonsingular Vandermonde matrix on the distinct residues. Consequently, there are exactly \(p^{6-r}\) ordered lifts of each fixed pair of residue triples.

There are \(6p(p-1)(p-2)\) ordered residue-triple pairs with three distinct values, \(9p(p-1)\) with exactly two distinct values, and \(p\) with one distinct value. Including every singular rank gives
\[
\begin{aligned}
J_{3,d}(p^2)
&=6p(p-1)(p-2)p^3+9p(p-1)p^4+p\,p^5\\
&=16p^6-27p^5+12p^4=p^6A_2(p).
\end{aligned}
\]
No Hensel genericity assumption has been made: all repeated-root residue classes, which supply the extra mass, were counted explicitly.

**4. Chinese remaindering.** The congruence equations separate under the Chinese remainder theorem. For any cube-free \(N\) coprime to \(6\),
\[
J_{3,d}(N)=\prod_{p^e\parallel N}J_{3,d}(p^e)
=N^3\prod_{p^e\parallel N}A_e(p).
\]

**5. Sharp Fourier constant and equality.** The binomial transformations corresponding to \(t\mapsto t+b\) act by invertible affine maps on the moment curve: their linear parts are triangular with diagonal entries one. They act transitively on the support. For any supported \(f\), modulate so a maximal Fourier coefficient is at frequency zero and average \(f\) over these affine symmetries. The average is a constant times \(1_{\mathcal M}\), preserves the chosen Fourier coefficient, and cannot increase the Fourier \(\ell^6\) norm by affine invariance and the triangle inequality. Thus the indicator is extremal. Since \(\ell^6\) is strictly convex, equality in averaging forces the modulated function to be constant on the support, giving precisely the displayed extremizers.

Orthogonality of characters gives the exact sixth moment
\[
\|\widehat{1_{\mathcal M}}\|_6^6=N^{-2d}J_{3,d}(N),
\qquad\|\widehat{1_{\mathcal M}}\|_\infty=N^{1-d/2}.
\]
Their ratio is
\[
\mathcal C_6(\mathcal M_N^{(d)})
=(N^{d-6}J_{3,d}(N))^{-1/6}
=N^{-(d-3)/6}\prod_{p^e\parallel N}A_e(p)^{-1/6}.
\]

**6. Endpoint criterion.** For all primes \(p\ge5\), both \(A_1(p)\) and \(A_2(p)\) lie between two fixed constants strictly greater than one and finite (for example \(4<A_1(p)<6\) and \(11<A_2(p)<16\)). Thus in dimension three the product of the local factors diverges exactly when \(\omega(N)\to\infty\). Exact sharpness of \(\mathcal C_6\) makes this equivalent to uniform synthesis. For \(d>3\), the factor \(N^{-(d-3)/6}\) alone forces decay along any unbounded family of allowed moduli.

## Verification
The standalone `verify.py` independently enumerates all first-three-power-sum fibers for moduli \(5,25,7,49,35\), checks prime and prime-square exact counts, and verifies the mixed-prime Chinese-remainder factor. The observed counts are respectively \(545,173125,1645,1457407,896525\), all matching the formulas. The program also checks the decomposition by Vandermonde rank using exact integer arithmetic. These are finite consistency checks, not a replacement for Steps 1–6 of the proof.

## Relationship to prior work
Iosevich, Li and Yu, arXiv:2609.25404v1 (first public 2026-09-21), prove the affine-transitivity reduction of sharp spectral synthesis constants to indicator moments and explicitly propose precise moment-curve arithmetic profiles as further work (Section 9). Their identities leave the local congruence count unevaluated; the present result calculates the first ramified local factor \(p^2\) exactly and deduces the cube-free product formula.

A publicly available earlier result, *Exact squarefree endpoint profile for the cubic moment curve* (published-finding corpus, 2026), evaluates the \(p\)-factor and its squarefree product. That result assumes squarefree modulus, and its finite-field multiset argument does not determine the new \(p^2\)-factor: the square of \(A_1(p)\) is not \(A_2(p)\). Its squarefree statement is included here only as the already-established unramified component of the new cube-free formula.

Hickman and Wright, arXiv:1801.03176v2 (2018), establish moment-curve Fourier restriction and prime-power growth/endpoint bounds (notably Section 7 and Corollary 7.3); these do not give the exact six-variable count at \(p^2\). The prime-square factor is obtained instead from the singular Vandermonde lifting calculation above.

## Limitations
The arithmetic count is proved only at prime exponents \(1\) and \(2\), and only where \(2,3\) are invertible. No claim is made about prime cubes, higher prime powers, or moduli divisible by \(2\) or \(3\). The formula concerns the sharp sixth Fourier synthesis constant, not all restriction or extension constants at other exponents. An unindexed exact enumeration for cubic moment congruences could overlap with the prime-square factor despite the comparisons described here. No independent mathematical audit is claimed.

## References
1. A. Iosevich, Z. Li, K. Yu, *Spectral synthesis with the complexity parameter in \(\mathbb Z_N^d\)*, arXiv:2609.25404v1, first public 2026-09-21. https://arxiv.org/abs/2609.25404
2. J. Hickman, J. Wright, *The Fourier restriction and Kakeya problems over rings of integers modulo \(N\)*, Discrete Analysis 2018:11, arXiv:1801.03176v2. https://arxiv.org/abs/1801.03176
3. *Exact squarefree endpoint profile for the cubic moment curve*, published-finding corpus, 2026. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-squarefree-endpoint-profile-for-the-cubic-moment-curve--54592470800c
