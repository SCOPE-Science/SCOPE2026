# Exact \(p\)-rank strata and a universal Cartier block for cyclic-octic plane quintics

## Finding
Let \(p=8h+1>13\) be prime, \(k=\overline{\mathbb F}_p\), and \(r\in k\) with \(r^2\ne4\). Let \(C_r\) be the smooth projective curve
\[
C_r:\qquad y^4=x^5+r x^3+x=x(1+r x^2+x^4).
\]
For integers \(m\ge0\) and \(0\le j\le2m\), define the coefficient polynomial
\[
T_{m,j}(r)=[z^j](1+rz+z^2)^m
=\sum_{a=\max(0,j-m)}^{\lfloor j/2\rfloor}
\binom ma\binom{m-a}{j-2a}r^{j-2a}.
\]
Put \(P_h=T_{2h,h}\) and \(Q_h=T_{4h,2h}\), reducing their integer coefficients modulo \(p\). Denote the geometric \(p\)-rank of \(\operatorname{Jac}(C_r)\) by \(\gamma_p(C_r)\). Then
\[
\boxed{\gamma_p(C_r)=2+2\,\mathbf1_{P_h(r)\ne0}+2\,\mathbf1_{Q_h(r)\ne0}.}
\]
Thus the entire parameter locus has \(p\)-rank at least two; the ordinary locus is exactly \(P_h(r)Q_h(r)\ne0\), and the exceptional loci of ranks four and two are specified exactly by vanishing of one or both coefficients. In particular, for \(p=17\), one has \(P_2=6(r^2-5)\), \(Q_2=2(r^2-5)(r^2-13)\) in \(\mathbb F_{17}[r]\), yielding rank two for \(r^2=5\), rank four for \(r^2=13\), and rank six elsewhere, with \(r^2=4\) excluded.

A stronger structural statement explains the lower bound. In the Cartier operator on the genus-six space of holomorphic differentials there is a two-dimensional invariant summand whose **unrooted coefficient matrix** has determinant
\[
\boxed{\binom{6h}{h}\binom{6h}{3h}(r^2-4)^{2h},}
\]
which never vanishes on the smooth parameter locus. The remaining contributions comprise two identical one-dimensional coefficients \(Q_h\) and two coefficients proportional to \(P_h\).

## Assumptions and scope
The characteristic is prime \(p>13\) with \(p\equiv1\pmod8\); the ground field is algebraically closed and \(r^2\ne4\). The polynomial \(x(1+r x^2+x^4)\) has five distinct roots, so the cyclic degree-four cover is smooth after projective normalization and has genus \((4-1)(5-1)/2=6\). The original projective model \(X^5+Y^4Z+XZ^4+rX^3Z^2=0\) is isomorphic over \(k\) after rescaling \(Y\) by a fourth root of \(-1\). The formula concerns geometric \(p\)-rank, not the \(a\)-number, Newton polygon or superspeciality.

## Proof
Write \(f(x)=x(1+r x^2+x^4)\). At each simple zero of \(f\), the local parameter is \(y\) and \(\operatorname{ord}(dx)=3\); at the unique point at infinity, \(\operatorname{ord}(x)=-4\), \(\operatorname{ord}(y)=-5\), and \(\operatorname{ord}(dx)=-5\). It follows that
\[
\omega_{j,i}=x^i\,dx/y^j,\quad 1\le j\le3,\quad 0\le i\le j-1,
\]
are six linearly independent holomorphic differentials, hence a basis by the genus computation.

Since \(p=8h+1\), put \(m_j=j(p-1)/4=2jh\). The Cartier rule \(\mathcal C(a^p\eta)=a\mathcal C(\eta)\) and \(\mathcal C(x^{pt+p-1}dx)=x^t dx\) show that the Cartier block on the \(j\)-th group has, up to entrywise \(p\)-th roots, row \(t\), column \(i\) equal to the coefficient of \(x^{p(t+1)-1-i}\) in \(f^{m_j}\). Since \(f^{m_j}=x^{m_j}(1+r x^2+x^4)^{m_j}\), these coefficients are \(T_{m_j,k}(r)\), with \(2k=p(t+1)-1-i-m_j\); a nonintegral or out-of-range index gives zero.

Consequently the \(j=1\) block is \((P_h)\), the \(j=2\) block is \(\operatorname{diag}(Q_h,Q_h)\), and the \(j=3\) block consists of an isolated scalar \(T_{6h,5h}\) and a two-by-two block, with a convenient ordering of rows and columns,
\[
M_h(r)=\begin{pmatrix}T_{6h,h}&T_{6h,h-1}\\T_{6h,3h-1}&T_{6h,3h}\end{pmatrix}.
\]
The actual semilinear Cartier matrix uses entrywise \(p\)-th roots. Consequently, the determinant of its two-dimensional block is the \(p\)-th root of the displayed unrooted determinant; taking these roots preserves zero/nonzero determinants and rank. In each group the Cartier operator preserves the corresponding \(k\)-subspace because \(p\equiv1\pmod4\), and the two-dimensional block is likewise invariant.

We prove two polynomial identities over \(\mathbb F_p[r]\):
\[
\begin{aligned}
\Delta_h&:=T_{6h,h}T_{6h,3h}-T_{6h,h-1}T_{6h,3h-1}
=\kappa_h(r^2-4)^{2h},\\
T_{6h,5h}&=c_h(r^2-4)^{2h}T_{2h,h},
\end{aligned}
\]
where \(\kappa_h=\binom{6h}{h}\binom{6h}{3h}\) and \(c_h=\binom{6h}{5h}/\binom{2h}{h}\) are nonzero modulo \(p\) (all factorial arguments are less than \(p\)).

For this purpose the generating polynomial \((1+rz+z^2)^m\) supplies the integral coefficient recurrences
\[
(k+1)T_{m,k+1}=(m-k)rT_{m,k}+(2m-k+1)T_{m,k-1},
\]
\[
(r^2-4)T'_{m,k}=krT_{m,k}-2(2m-k+1)T_{m,k-1},
\]
and the second-order equation
\[
(r^2-4)T''_{m,k}+(1-2m)rT'_{m,k}+k(2m-k)T_{m,k}=0.
\]
(The identities also follow directly by differentiating the finite coefficient sum.) Set \(A=T_{6h,h}\), \(B=T_{6h,h-1}\), \(D=T_{6h,3h}\), and \(E=T_{6h,3h-1}\). Reducing the first two recurrences modulo \(p=8h+1\) yields, with \(d=r^2-4\),
\[
\begin{array}{ll}
dA'=hrA-6hB,&dB'=-2hA+3hrB,\\
dD'=3hrD-2hE,&dE'=-6hD+hrE.
\end{array}
\]
Therefore \(d(AD-BE)'=4hr(AD-BE)\). Since \(\Delta_h\) has degree at most \(4h\), its leading coefficient is \(\kappa_h\), and \(d^{2h}\) solves the same first-order equation, their difference has degree less than \(4h\). No nonzero polynomial of that degree solves this equation: its highest coefficient would be multiplied by \(\deg-4h\ne0\pmod p\). This establishes the determinant identity.

To obtain the second identity, write \(U=T_{2h,h}\), \(R=d^{2h}U\). The displayed second-order equation for \(U\) becomes \(dU''+(1-4h)rU'+3h^2U=0\). Direct differentiation and \(8h+1=0\) in \(\mathbb F_p\) show that \(R\) satisfies \(dR''+(1-12h)rR'+35h^2R=0\), the same equation as \(T_{6h,5h}\). Their top coefficients have ratio \(c_h\). Their difference is a solution of degree less than \(5h\), but a highest-degree coefficient in degree \(t<5h\) would be multiplied by \((t-5h)(t-7h)\ne0\pmod p\). Hence the difference vanishes.

Both \(\kappa_h\) and \(c_h\) are nonzero, while \(d\ne0\) by smoothness. The two-dimensional Cartier block is therefore invertible at every smooth parameter, while the two one-dimensional blocks governed by \(P_h\) and the two governed by \(Q_h\) are zero precisely as specified. A nonzero semilinear endomorphism of a one-dimensional space and an invertible semilinear endomorphism of a finite-dimensional space retain full rank under every iterate; a zero block remains zero. The stable Cartier rank, equal to geometric \(p\)-rank, is consequently the stated formula. All ranks are even. This completes the proof.

## Verification
Run `python3 check.py` with Python 3 and no external packages. The checker separately forms the relevant coefficient polynomials, verifies both factorizations as polynomial identities for primes \(17,41,73,89,97,113,137,193\), then constructs full Cartier blocks directly from the monomial-exponent rule for every \(r\in\mathbb F_p\) with \(r^2\ne4\) and checks their ranks against the formula. It prints `VERIFY_OK` upon success. These finite-characteristic tests are not substitutes for the characteristic-uniform recurrence proof.

## Relationship to prior work
Ohashi (2026, arXiv:2605.29624) studies the same order-eight plane-quintic family and its superspeciality, and derives hypergeometric criteria for that different property. Bouw (2001) studies the generic \(p\)-rank of tame cyclic covers; generic ordinarity for the present congruence class falls within that broad framework and is **not** claimed as new. Cavalieri–Pries (2023/2025) give mass formulas for nonordinary members of four-branch-point cyclic-cover families; those formulas do not themselves state the present per-parameter three-stratum classification or the nonvanishing Cartier determinant. The new claim is the exact all-parameter rank formula together with the determinantal identity, not the cover, standard Cartier computation, or the general theory of \(p\)-ranks.

## Limitations
The argument is restricted to primes \(p>13\) congruent to one modulo eight and smooth parameters \(r^2\ne4\). It does not describe the other residue classes, count geometric isomorphism classes of each rank, or determine finer invariants such as Newton polygons. The formula permits a rank to have empty stratum in a given characteristic. Historical-priority comparisons cannot exclude a prior equivalent simplification in all literature; independent mathematical review has not been performed.

## References
1. Ryo Ohashi, *Superspecial plane quintics with large automorphism groups*, arXiv:2605.29624 (first version 2026-05-28), particularly the order-eight family in §3.3. https://arxiv.org/abs/2605.29624
2. Irene I. Bouw, *The p-Rank of Ramified Covers of Curves*, Compositio Mathematica **126** (2001), 295–322. https://doi.org/10.1023/A:1017513122376
3. Renzo Cavalieri and Rachel Pries, *Mass formula for non-ordinary curves in one dimensional families*, arXiv:2308.14891 (2023); Manuscripta Mathematica (2025). https://arxiv.org/abs/2308.14891
