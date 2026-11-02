# Birational Gauss maps and a characteristic-dependent dual-degree drop for maximal Kummer plane curves

## Finding
Let \(p\ge3\) be an odd prime, \(q=p^e\), \(N=q+1\), and choose \(n\ge2\) with \(n\mid N\) and \(r=N/n\ge2\). Over \(k=\overline{\mathbb F}_p\), let \(D\subset\mathbb P^2_k\) be the integral plane curve
\[
F(X,Y,Z)=Y^N-X^{2n}Z^{N-2n}-X^nZ^{N-n}=0,
\]
interpreted literally with \(Z^0=1\) when \(r=2\). Let \(C\) be its normalization and \(D^\vee\) its projective dual curve. The Gauss map \(\gamma:C\to D^\vee\) is **birational**, and
\[
\deg D^\vee=\begin{cases}
2n^2,&r=2,\\
N(n+1)-2n,&r>2\text{ and }p\mid(r-2),\\
N(n+1),&r>2\text{ and }p\nmid(r-2).
\end{cases}
\]
In particular, \(q=9,n=2,r=5\) gives a degree-\(10\) model whose dual has degree \(26\) rather than the generic value \(30\); the corresponding \(q=5,n=2,r=3\) case has dual degree \(18\). The exceptional drop occurs for infinitely many \(q\): take \(q=3^{4s+2}\), \(s\ge0\), \(r=5\), and \(n=(q+1)/5\).

## Assumptions and scope
All geometric degrees and branches are over the algebraic closure \(k\). The positive integers \(p,e,n,r\) satisfy \(p\ge3\) prime, \(e\ge1\), \(N=p^e+1=nr\), \(n\ge2\), \(r\ge2\). Thus \(p\nmid Nn r\). The dual is the reduced closure of the family of tangent lines to the smooth locus of \(D\); its degree does not count inseparable multiplicity. The plane model has degree \(N\) even when its normalization is smooth. The underlying smooth curve is the maximal family studied in the cited 2026 work; the present claim concerns its *specified plane embedding*.

The polynomial \(y^N-x^n(x^n+1)\) is irreducible over \(k(x)\), since \(x^n+1\) has simple roots and its valuations there equal one, so it cannot be a proper power of any prime dividing \(N\). Consequently, the plane curve is integral and its normalization has function field \(K=k(x,y)\).

## Proof
**1. Singular branches and the polar base divisor.** In the affine chart \(Z=1\), write \(u=x^n\). The partial derivatives are
\[
F_X=-n x^{n-1}(2u+1),\quad
F_Y=N y^{N-1},\quad
F_Z=-(N-2n)u^2-(N-n)u.
\]
Since \(p\nmid nN\), the only affine singular point is \((x,y)=(0,0)\): at the other points with \(y=0\), one has \(u=-1\) and \(F_X\ne0\). At the origin, the local equation \(y^N=x^n(1+x^n)\) has exactly \(n\) branches, each admitting a uniformizer with \(v(x)=r\), \(v(y)=1\). On each branch the minimum valuation of the three polar coordinates \((F_X,F_Y,F_Z)\) is \(r(n-1)\): \(F_X\) attains it, \(v(F_Y)=N-1\) is larger, and \(v(F_Z)\ge nr\). The total common-polar vanishing at the origin is therefore
\[
B_0=nr(n-1)=N(n-1).
\]

If \(r=2\), the line \(Z=0\) meets \(D\) in \(N\) distinct points \([1:\zeta:0]\), \(\zeta^N=1\), all smooth because \(F_Y=N\zeta^{N-1}\ne0\). Thus the polar system has no base divisor at infinity.

Suppose \(r>2\). Infinity consists of the single point \([1:0:0]\), with local equation in the chart \(X=1\)
\[
Y^N=Z^{N-2n}(1+Z^n).
\]
Put \(g=\gcd(r,2)\). There are exactly \(ng\) branches; on each, \(v(Z)=r/g\), \(v(Y)=(r-2)/g\). The three polar valuations are
\[
\begin{aligned}
v(F_Y)&=(N-1)(r-2)/g,\\
v(F_X)&=(N-2n)r/g,\\
v(F_Z)&=\begin{cases}
(N-2n-1)r/g,&p\nmid(r-2),\\
(N-n-1)r/g,&p\mid(r-2),
\end{cases}
\end{aligned}
\]
where the second line for \(F_Z\) reflects vanishing of its first coefficient and nonvanishing of the second, because \(p\nmid n\) and \(r\equiv2\pmod p\). When \(p\nmid(r-2)\), \(F_Z\) has the smallest valuation, precisely \((N-2n-1)r/g\); note that \(v(F_Y)\) exceeds it by \(2/g\). In the exceptional case, \(F_Y\) has the smallest valuation and exceeds the generic minimum by \(2/g\); both \(F_X\) and the remaining term of \(F_Z\) have strictly larger valuation. Summing over the \(ng\) branches gives
\[
B_\infty=\begin{cases}
N(N-2n-1),&p\nmid(r-2),\\
N(N-2n-1)+2n,&p\mid(r-2).
\end{cases}
\]

**2. Degree of the Gauss linear series.** The three partial derivatives are sections of \(\nu^*\mathcal O_D(N-1)\), a line bundle of degree \(N(N-1)\) on \(C\), where \(\nu:C\to D\) denotes normalization. They have no common zero away from the singular points just listed, and their common vanishing divisor has degree \(B_0+B_\infty\). Thus the base-free Gauss linear series has degree
\[
\deg\gamma\cdot\deg D^\vee=N(N-1)-B_0-B_\infty
=\begin{cases}
2n^2,&r=2,\\
N(n+1)-2n,&r>2,\ p\mid(r-2),\\
N(n+1),&r>2,\ p\nmid(r-2).
\end{cases}
\]
The factor \(\deg\gamma\), including any inseparable degree, must still be determined; the polar calculation alone is not a dual-degree theorem.

**3. Birationality of the Gauss map.** On the dense affine open where all expressions are defined, set \(u=x^n\) and take the rational functions
\[
a=-F_X/F_Y=\frac{n y(2u+1)}{x(u+1)},\qquad
b=F_Z/F_Y=\frac{y((2n-1)u+(n-1))}{u+1}.
\]
Both lie in the function field \(k(D^\vee)\), viewed inside \(K\). Define
\[
c(u)=\frac{(2n-1)u+(n-1)}{n(2u+1)},\qquad h=b/a=xc(u),\qquad H=h^n=uc(u)^n.
\]
Then \(H\in k(D^\vee)\), and
\[
L=a^N=\frac{n^N u^{1-r}(2u+1)^N}{(u+1)^{N-1}}
\]
also lies in \(k(D^\vee)\). As functions on \(\mathbb P^1_u\), \(L\) has exactly two poles: order \(r-1\) at \(u=0\) and order \(N-1=q\) at \(u=-1\). Meanwhile \(H(0)=0\) and \(H(-1)=-1\), since \(c(-1)=1\).

Write \(M=k(H,L)\subseteq k(u)\). The derivative \(H'(u)\) is nonzero: apart from a nonzero rational factor, its numerator is
\[
2(2n-1)u^2+(5n-3)u+(n-1),
\]
which cannot vanish identically modulo \(p\) (if its constant term vanished, \(n\equiv1\pmod p\), and its quadratic term would equal \(2\ne0\)). Thus \(k(u)/M\) is a **separable** extension. If its degree were \(d>1\), Lüroth's theorem would give \(M=k(t)\) and a separable degree-\(d\) map \(\mathbb P^1_u\to\mathbb P^1_t\). Since \(L\in k(t)\) has precisely the two poles \(u=0,-1\), and these points have distinct values under \(H\in k(t)\), their two fibers under \(t\) must each consist of a single point. Consequently \(t\) is totally ramified of index \(d\) at both points. In particular, \(d\mid\operatorname{ord}_{u=-1}(L)=q=p^e\); hence \(d\) is divisible by \(p\). Both total ramifications are wild. For a separable local extension with wild ramification index \(d\), the different exponent is at least \(d\): in a source uniformizer \(s\), a target uniformizer has expansion \(a s^d+\sum_{j>d}a_j s^j\), and its leading derivative vanishes because \(p\mid d\), forcing the derivative valuation to be at least \(d\). The two different contributions therefore sum to at least \(2d\), contradicting Riemann--Hurwitz for the degree-\(d\) map \(\mathbb P^1\to\mathbb P^1\), whose total different degree equals \(2d-2\). Thus \(d=1\) and \(M=k(u)\).

Since \(u\in k(D^\vee)\), the identity \(h=xc(u)\) recovers \(x=h/c(u)\) in that field. Then \(a=n y(2u+1)/(x(u+1))\) recovers \(y\). Therefore \(k(D^\vee)=k(x,y)=K\), proving that \(\gamma\) is birational. Substituting \(\deg\gamma=1\) in step 2 proves the theorem.

## Verification
The accompanying standalone standard-library program `check_dual.py` checks the derivative numerator and exact base-divisor valuation identities for admissible parameters, including the exceptional modular cancellation. It checks \(625\) admissible prime-power/divisor parameter pairs, including \((q,n,r)=(9,2,5)\) and \((125,18,7)\). The program is finite arithmetic verification, **not** a replacement for the branch classification, the two-point ramification argument, or the all-parameter proof above.

Run `python check_dual.py`; the expected prefix is `VERIFY_OK`.

## Relationship to prior work
Guardieiro, da Silva and Tafazolian (2026) study exactly the normalization of \(y^{q+1}=x^n(x^n+1)\) and establish maximality, Weierstrass semigroups and automorphism results. Their inspected full text does not state the projective dual degree, polar-base correction or Gauss-map birationality. Tafazolian and Torres (2016/2019) study the broader superelliptic family \(y^a=x^b(x^c+1)\), including genus and maximality; their inspected 2016 seven-page report does not calculate these dual invariants. Komeda (2020) discusses a different positive-characteristic plane curve with a *nonbirational* Gauss map; it illustrates why step 3 cannot be omitted. This theorem concerns a specific plane embedding, so generic isomorphism classes and existing genus/semigroup information do not imply its numerical projective dual degree.

## Limitations
The result assumes odd characteristic, \(q=p^e\), \(2\le n\mid(q+1)\), and \(r\ge2\). It does not determine singularities of \(D^\vee\), arbitrary embeddings of the normalized curve, or the characteristic-two case. Previous Kummer literature could contain an equivalent calculation under alternate terminology; historical priority is not independently certified. The geometric proof does not rely on finite-field numerical extrapolation.

## References
1. J. P. Guardieiro, Y. da Silva and S. Tafazolian, *On the Maximality, Weierstrass Semigroups, and Automorphism Group of the Curve \(Y^{q+1}=X^n(X^n+1)\)*, arXiv:2605.25257v1, 2026-05-24, https://arxiv.org/html/2605.25257v1.
2. S. Tafazolian and F. Torres, *On the curve \(Y^a=X^b(X^c+1)\) over finite fields*, UNICAMP research report rp-2016-17, 2016, https://www.ime.unicamp.br/sites/default/files/pesquisa/relatorios/rp-2016-17.pdf; published *Advances in Geometry* 19 (2019), 263--268.
3. K. Komeda, *Singularities of the dual curve of a certain plane curve in positive characteristic*, arXiv:2002.10691, 2020, https://arxiv.org/abs/2002.10691.
