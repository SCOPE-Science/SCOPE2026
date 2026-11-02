# Torsion jumps in a four-conic–line-fiber pencil of rational elliptic surfaces

## Finding
Let \(K=\mathbb C(t)\), and for each \(a\in\mathbb C\setminus\{0,1\}\) consider the smooth generic plane cubic
\[
E_a:\quad (x-ay)(x^2+y^2-z^2)+t(x-y)(x^2-xy+y^2-z^2)=0.
\]
It has the rational point \(O=[0:0:1]\), taken as the identity. The full torsion subgroup of its Mordell–Weil group is
\[
\boxed{E_a(K)_{\mathrm{tors}}\cong
\begin{cases}
\mathbb Z/2\mathbb Z,&a^2-a+1=0,\\
\{0\},&a^2-a+1\ne0.
\end{cases}}
\]
At either of the two nontrivial parameters, the unique nonidentity two-torsion point is the branch point of projection from \(O\) with slope \(x/y=a\). The resulting exceptional group is of order two, not an unbounded two-primary group.

## Assumptions and scope
All curves and sections are over \(\mathbb C\). The parameter \(t\) is transcendental, so this theorem concerns the generic fiber over \(\mathbb C(t)\), not the torsion of an individual complex elliptic fiber. The parameters \(a=0,1\) are excluded. The elliptic surface is obtained by resolving the nine (possibly infinitely near) base points of this cubic pencil; its relatively minimal model is a rational elliptic surface with section and \(\chi(\mathcal O)=1\). A section of this model is the same as a \(K\)-rational point.

## Proof
**1. The double cover and its rational branch points.** In the chart \(y\ne0\), set \(r=x/y\) and write
\[
\begin{aligned}
f(r)&=(r-a)(r^2+1),&g(r)&=(r-1)(r^2-r+1),\\
P(r)&=f(r)+tg(r),&L(r)&=(r-a)+t(r-1).
\end{aligned}
\]
The cubic becomes \(P(r)=(z/y)^2L(r)\). Multiplication by \(L(r)\) makes it the genus-one quartic double cover \(w^2=P(r)L(r)\), with \(w=(z/y)L(r)\). The rational branch point at \(L=0\) represents \(O\). For a smooth genus-one double cover with a rational branch point as identity, its other \(K\)-rational branch points are exactly the nonidentity \(K\)-rational points of order two.

A root of \(P\) fixed in \(\mathbb C\) is present precisely when \(f,g\) have a common root, while a nonconstant rational root \(r(t)\in K\) would give a rational right inverse to the map \(r\mapsto -f(r)/g(r)\). Its degree must then be one. Exact elimination gives
\[
\operatorname{Res}_r(f,g)=2(a-1)(a^2-a+1).
\]
If \(a^2-a+1\ne0\), the rational map has degree three, so \(P\) has no \(K\)-rational root. At \(a^2-a+1=0\), the only common factor is \(r-a\); the remaining map has degree two and therefore no rational right inverse. Thus \(P\) has exactly one \(K\)-rational root, \(r=a\). Consequently \(E_a(K)[2]\) is trivial except at the two roots of \(a^2-a+1\), where it contains exactly one nonidentity element.

**2. Fiber groups needed to exclude all further torsion.** Let \(Q_a(t)\) be
\[
\begin{aligned}
Q_a(t)={}&3t^4+10(a+1)t^3+(59a^2-70a+59)t^2\\
&+4(7a^3-a^2-a+7)t+4(a^2+1)^2.
\end{aligned}
\]
Up to a nonzero scalar, the quartic-cover discriminant is \(t^2(t+1)^2(t+a)^2Q_a(t)\), with another double zero at \(t=\infty\). The degree-four binary-quartic invariant controlling multiplicative reduction is
\[
I_a(t)=(a^2+1)^2+6(a^3+1)t+(11a^2-9a+11)t^2+3(a+1)t^3+t^4.
\]
The following factorizations provide the critical fiber collisions:
\[
\begin{aligned}
\operatorname{Disc}_t(Q_a)&=512(a-1)^4(a^2-a+1)(71a^2-196a+71)^3,\\
Q_a(-1)&=(a-2)^2(4a^2-12a+7),\\
Q_a(-a)&=(2a-1)^2(7a^2-12a+4),\\
Q_a(0)&=4(a^2+1)^2.
\end{aligned}
\]
Examining zero orders of the discriminant and \(I_a\), including the four distinguished fibers, gives the Kodaira multisets: generically \(4I_2+4I_1\); at \(a\in\{2,1/2,i,-i\}\), \(3I_2+III+3I_1\); at roots of \(4a^2-12a+7\) or \(7a^2-12a+4\), \(3I_2+I_3+3I_1\); at roots of \(a^2-a+1\), \(5I_2+2I_1\); at roots of \(71a^2-196a+71\), \(4I_2+II+2I_1\). The parameter cases are disjoint. The displayed formulas allow these local classifications to be checked by Kodaira's characteristic-zero valuation criteria, and the degree-twelve discriminant accounts for all fibers.

The component groups at \(I_2\) and \(III\) have exponent two; those at \(I_1\) and \(II\) are trivial; the only possible odd-order component group is a single \(\mathbb Z/3\mathbb Z\) at \(I_3\). Shioda's height formula on a rational elliptic surface gives, for any section \(S\),
\[
\langle S,S\rangle=2+2(S\cdot O)-\sum_v\operatorname{contr}_v(S),
\]
where the contributions are \(1/2\) for a nonidentity \(I_2\) or \(III\) component, and \(2/3\) for a nonidentity \(I_3\) component. For nonzero sections \(S\), the intersection number \(S\cdot O\) is nonnegative. A torsion section has height zero.

If \(S\) has odd prime order, its image in each order-two component group vanishes. There is at most one order-three group, whose total contribution is at most \(2/3\). Hence \(\langle S,S\rangle\ge 2-2/3>0\), a contradiction. If \(S\) has order four, then its double \(2S\) has order two and maps trivially into every component group, since each local component group has exponent two or three and the image of \(S\) has order dividing four. Thus \(\langle2S,2S\rangle\ge2>0\), also a contradiction. Higher two-power torsion would contain an element of order four. There is therefore no odd or higher two-power torsion. Together with Step 1 this proves the complete torsion classification.

## Verification
The included `verify_torsion.py` requires Python 3 and SymPy. Run `python verify_torsion.py` to check the quartic discriminant factorization, the common-root resultant, the collision-discriminant identity, the quartic invariant, and exact representatives of the relevant parameter strata. The independent mathematical argument is the degree-of-rational-map criterion and Shioda's height formula; finite symbolic tests do not substitute for those infinite-family arguments.

## Relationship to prior work
Suluyer constructs the explicit family and identifies its four distinguished conic–line members. The classical Shioda–Oguiso theory determines height pairings, torsion constraints, and possible Mordell–Weil lattices of rational elliptic surfaces. Those theorems are used here, not claimed as new. The added assertion is the complete torsion-stratum equation in the specified one-parameter family and the geometric identification of its unique exceptional torsion section. In particular, the singular-fiber configuration alone does not generally determine whether a rational elliptic surface possesses a two-torsion section.

## Limitations
The result is over characteristic zero and concerns the generic group over \(\mathbb C(t)\). It makes no assertion about ranks or explicit free generators, the torsion after finite extensions of \(K\), or specialization of torsion in individual fibers. Historical priority is provisional; existing classifications of Mordell–Weil lattices can give indirect information, and a complete search of every earlier presentation is not claimed.

## References
1. H. Suluyer, *Pencils of Conic-Line Curves*, arXiv:2412.06928, first publicly submitted 2024-12-09; journal version *On the Number of Conic-Line Curves in a Pencil*, Mediterranean Journal of Mathematics 23 (2026), 127, DOI 10.1007/s00009-026-03125-z, Theorem 4.1.
2. K. Oguiso and T. Shioda, *The Mordell-Weil lattice of a rational elliptic surface*, Commentarii Mathematici Universitatis Sancti Pauli 40 (1991), 83–99, especially Proposition 3.5.
3. T. Shioda, *On the Mordell-Weil lattices*, Commentarii Mathematici Universitatis Sancti Pauli 39 (1990), 211–240.
