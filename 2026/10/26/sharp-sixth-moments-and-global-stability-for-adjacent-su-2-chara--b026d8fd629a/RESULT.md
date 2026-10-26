# Sharp sixth moments and global stability for adjacent \(SU(2)\) characters

## Finding
Let \(\chi_n\) and \(\chi_{n+1}\) be successive irreducible characters of \(SU(2)\), with Haar measure of mass one. Their span admits an **exact**, all-index sharp \(L^2\)-to-\(L^6\) constant, a complete complex equality classification, and a global identity for the stability deficit. This also gives the sharp sixth moment for two successive normalized zonal spherical harmonics on \(S^3\), since \(SU(2)\) is isometric to that sphere and \(\chi_n(\theta)=U_n(\cos\theta)\).

Write
\[
\begin{aligned}
A_n&=\tfrac12(n+1)(n^2+2n+2),\\
B_n&=\tfrac12(n+1)^2(n+2),\\
C_n&=\tfrac12(n+1)(n+2)^2,\\
D_n&=\tfrac12(n+2)(n^2+4n+5).
\end{aligned}
\]
Define
\[
P_n(x)=A_nx^3+15B_nx^2(1-x)+15C_nx(1-x)^2+D_n(1-x)^3.
\]
Its derivative has exactly one zero \(x_n\in(0,1)\), in fact \(0<x_n<1/2\). The exact sharp constant is \(K_n=P_n(x_n)\):
\[
\int_{SU(2)}|a\chi_n(g)+b\chi_{n+1}(g)|^6\,dg\le K_n(|a|^2+|b|^2)^3.
\]
For \((a,b)\ne(0,0)\), equality holds precisely when
\[
(a,b)=\zeta(\sqrt{x_n},\,\pm\sqrt{1-x_n}),\quad \zeta\in\mathbb C\setminus\{0\}.
\]
Thus both adjacent characters always mix, their relative phase is real, and the higher character receives strictly more squared coefficient mass. As \(n\to\infty\),
\[
x_n=\tfrac12-\tfrac1{4n}+O(n^{-2}),\qquad K_n=2n^3+9n^2+O(n).
\]

There is an exact *global* deficit. Set \(S=|a|^2+|b|^2>0\), \(x=|a|^2/S\); when \(ab\ne0\), put \(\phi=\arg a-\arg b\). Define
\[
Q_n(x)=6n^3+36n^2+63n+30-(6n^2+18n+11)(x+2x_n).
\]
Then
\[
\boxed{K_n-S^{-3}\int|a\chi_n+b\chi_{n+1}|^6dg
=(x-x_n)^2Q_n(x)+12x(1-x)[B_nx+C_n(1-x)]\sin^2\phi.}
\]
For \(ab=0\), define the second term as zero. On \([0,1]\), \(Q_n(x)\ge c_n=Q_n(1)>0\); the coefficient \(c_n\) is sharp in the corresponding global quadratic modulus-deficit bound, as witnessed by \(x=1\).

## Assumptions and scope
The index is any integer \(n\ge0\). The coefficients \(a,b\) are arbitrary complex numbers; \(S=0\) gives the trivial equality \(0=0\), while the equality classification above concerns nonzero vectors. The characters are the usual unnormalized traces of irreducible representations of highest weights \(n\) and \(n+1\); their \(L^2\) norms under probability Haar measure are exactly one. The sixth-power constant is \(K_n\), not its sixth root. The equivalent sphere formulation concerns the *two-dimensional zonal subspace*, not the entire degree-\(n\) plus degree-\(n+1\) harmonic spaces.

## Proof
**1. Mixed moments.** The Clebsch–Gordan rule gives
\[
\chi_j\chi_k=\sum_{r=|j-k|,\,r\equiv j+k\ (2)}^{j+k}\chi_r,
\qquad \chi_m^2=\sum_{j=0}^m\chi_{2j}.
\]
Consequently \(\int\chi_{2i}\chi_{2j}\chi_{2k}\,dg\) is one precisely when \(|i-j|\le k\le i+j\), and zero otherwise. Write \(T(r,s,t)\) for the number of integer triples \(0\le i\le r\), \(0\le j\le s\), \(0\le k\le t\) obeying these triangle inequalities. Then
\[
\int\chi_n^6=A_n=T(n,n,n),\quad
\int\chi_n^4\chi_{n+1}^2=B_n=T(n,n,n+1),
\]
\[
\int\chi_n^2\chi_{n+1}^4=C_n=T(n+1,n+1,n),\quad
\int\chi_{n+1}^6=D_n=T(n+1,n+1,n+1).
\]
Indeed,
\[
T(m,m,m)=(m+1)^3-3\sum_{k=1}^m\frac{k(k+1)}2
=\frac{(m+1)(m^2+2m+2)}2,
\]
because a triple fails the triangle inequalities exactly when one coordinate strictly exceeds the sum of the other two, and these three failure events are disjoint. Adding the layer \(k=n+1\) gives \(B_n-A_n=n(n+1)/2\); deleting that layer from \(T(n+1,n+1,n+1)\) gives \(D_n-C_n=(n+2)(n+3)/2\). This proves all four formulas for every \(n\ge0\), including the endpoint \(n=0\).

**2. Complex phases.** The central involution \(g\mapsto-g\) sends \(\chi_j\) to \((-1)^j\chi_j\). Hence all odd cross-character integrals of total degree six vanish. For \(S>0\), \(x=|a|^2/S\), and \(\phi=\arg a-\arg b\), expansion of \(|a\chi_n+b\chi_{n+1}|^6\) yields exactly
\[
S^{-3}\int|a\chi_n+b\chi_{n+1}|^6\,dg
=P_n(x)-12x(1-x)[B_nx+C_n(1-x)]\sin^2\phi.
\]
Both \(B_n\) and \(C_n\) are positive. At interior \(x\) the phase is maximizing precisely for \(\phi\equiv0\pmod\pi\).

**3. Unique maximum.** Direct expansion gives
\[
P_n(x)=\alpha_n x^3+\beta_n x^2+\gamma_n x+D_n,
\]
with
\[
\alpha_n=6n^2+18n+11>0,\qquad
\beta_n=-6n^3-36n^2-63n-30,
\]
\[
P_n'(0)=\tfrac32(n+2)(4n^2+11n+5)>0,
\quad P_n'(1)=-\tfrac32(n+1)(4n^2+13n+8)<0.
\]
The quadratic \(P_n'\) opens upward. It has exactly one zero in \((0,1)\) and its other zero lies in \((1,\infty)\). Thus the first zero \(x_n\) is the unique global maximizer on \([0,1]\), with strictly negative second derivative. Since \(P_n'(1/2)=-3(2n+3)^2/4<0\), it lies below \(1/2\). The phase identity proves the inequality and every equality case.

**4. Exact deficit and sharp stability.** Since \(P_n'(x_n)=0\), algebraic factorization gives
\[
P_n(x_n)-P_n(x)=(x-x_n)^2[-\beta_n-\alpha_n(x+2x_n)]
=(x-x_n)^2Q_n(x).
\]
For \(x\ne x_n\), positivity follows from the unique strict maximum; at \(x=x_n\), \(Q_n(x_n)=-P_n''(x_n)/2>0\). The function \(Q_n\) decreases strictly with \(x\), since \(\alpha_n>0\); therefore its minimum on the closed interval is \(c_n=Q_n(1)>0\). The exact deficit formula follows by adding back the nonnegative phase term. The coefficient \(c_n\) cannot be increased, because at \(x=1\) the phase term vanishes and the modulus deficit equals \(c_n(1-x_n)^2\).

**5. Growth.** One has \(P_n'(1/2)=-3(2n+3)^2/4\) and \(P_n''(1/2)=-3(2n+3)(2n^2+6n+3)\). Uniformly for \(x\in[0,1]\), \(n^{-3}P_n(x)\to(1+12x(1-x))/2\), whose strict unique maximum occurs at \(x=1/2\). Therefore \(x_n\to1/2\). Taylor expansion of \(P_n'(x_n)=0\) then gives \(x_n=1/2-1/(4n)+O(n^{-2})\). Finally \(P_n(1/2)=2n^3+9n^2+O(n)\), and the optimizing displacement changes its value by \(O(n)\), proving the stated \(K_n\) expansion.

## Verification
A standalone reproducibility script `verification_check.py` independently multiplies exact integer Clebsch–Gordan decompositions, checks the four moment formulas for \(0\le n\le30\), evaluates the sixth moment by independent high-order Chebyshev–Gauss quadrature for four complex phases per index, locates the maximizing root, and verifies the exact deficit factorization on a grid. The finite checks are diagnostics; the triangle-count and scalar-polynomial arguments above prove the result for all integer indices.

## Relationship to prior work
Dai, Gorbachev, and Tikhonov's 2019 lacunary spherical-polynomial theorem is a natural starting point for sharp few-degree Nikolskii estimates, but its displayed \(L^p\)-range does not contain the present \(L^2\)-to-\(L^6\) problem, and its lacunarity condition excludes the adjacent pair. Frank's 2022 coherent-state results concern one irreducible spin representation and a different coherent-state functional, not Haar sixth moments of sums of **characters of different spins**. Beiner and Verreault study positive/negative-part asymmetry for single zonal harmonics on \(S^2\), a different object. Classical Clebsch–Gordan identities are used as input; the sharp two-mode complex optimizer and the exact global deficit are the specific statements here. This finding is separate from previously established central fourth-moment character bounds and sixth moments for unrelated character pairs.

## Limitations
The claim is restricted to adjacent **zonal** characters on \(SU(2)\cong S^3\), not arbitrary pairs, nonzonal spherical harmonics, or higher even moments. No global sharp \(L^2\)-to-\(L^6\) inequality for the full spherical-harmonic band is asserted. Literature priority is not proved by search; older specialized Chebyshev and representation-theoretic inequalities may warrant additional historical examination. Independent external audit has not been performed.

## References
- F. Dai, D. Gorbachev, S. Tikhonov, *Nikolskii inequality for lacunary spherical polynomials*, arXiv:1905.00323 (first public version 2019-05-01), especially Theorem 1 and its admissible exponent range.
- R. L. Frank, *Sharp inequalities for coherent states and their optimizers*, arXiv:2210.14798 (first public version 2022-10-26), especially Theorem 4 and Section 4.2.
- F. Dai, D. Gorbachev, S. Tikhonov, *Nikolskii constants for polynomials on the unit sphere*, arXiv:1708.09837 (2017-08-31); background on sharp spherical polynomial inequalities.
- G. Beiner, W. Verreault, *Failure of \(L^p\) Symmetry of Zonal Spherical Harmonics*, arXiv:2209.00212 (2022-09-01); related single-harmonic phenomenon on \(S^2\).
