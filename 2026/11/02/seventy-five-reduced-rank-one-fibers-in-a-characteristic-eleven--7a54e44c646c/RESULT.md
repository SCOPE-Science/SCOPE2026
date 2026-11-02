# Seventy-five reduced rank-one fibers in a characteristic-eleven cyclic-quartic genus-six family

## Finding
Let \(k=\overline{\mathbb F}_{11}\). For each \((a,b)\in k^2\) for which \(F=x^5+ax^3+bx+1\) is separable, let \(C_{a,b}\) be the smooth projective model of \(y^4=F(x)\), of genus \(6\). All displayed polynomial coefficients are reduced modulo \(11\).

Define
\[
\begin{aligned}
 v_0&=5a^3b+2a^2b^4-3ab^7+4ab^2+3b^5-5,\\
 v_2&=4a^4+3a^2b-5b^2,\\
 m_{01}&=-a^3-a^2b^3+5ab+5b^4,\\
 m_{10}&=-a^2+5b,\\
 L&=v_0+2a^{11}v_2,\\
 D&=-a^5-a^4b^3-a^2b^4-3b^5-5,\\
 K&=m_{10}^{11}m_{01}+3.
\end{aligned}
\]
The exact Jacobian \(11\)-rank \(f_{11}\) and \(a\)-number are
\[
 f_{11}(C_{a,b})=2\mathbf1_{L\ne0}+
 \begin{cases}2&D\ne0,\\1&D=0,\ K\ne0,\\0&D=K=0,\end{cases}
 \qquad a(C_{a,b})=2+\mathbf1_{D=0}.
\]
In particular, the Jacobian is never ordinary, never has \(11\)-rank zero, and has only \(a\)-numbers \(2\) and \(3\). **The rank-one locus is exactly the scheme \(V(L,D)\), consisting of 75 reduced geometric coefficient-marked points, all smooth curves.** The additional rank-two, \(a\)-number-three locus \(V(D,K)\) consists of 70 reduced smooth points and is disjoint from \(V(L,D)\). Ranks \(1,2,3,4\) all occur. No assertion about curve-isomorphism classes, Newton polygons, or higher Ekedahl–Oort types is made.

## Assumptions and scope
The base field is algebraically closed of characteristic \(11\), and the parameter domain is precisely \(U=\{\Delta\ne0\}\), where the discriminant of \(F\) is
\[
\Delta=-2a^5+5a^4b^3+2a^3b+4a^2b^4-2ab^2+3b^5+1.
\]
All ranks refer to the Jacobian of the smooth completion, and geometric points of \(U\) are counted as ordered coefficient pairs, without quotienting by coordinate automorphisms.

## Proof
The pole orders at the unique point above infinity are \(\operatorname{ord}(x)=-4\), \(\operatorname{ord}(y)=-5\), and \(\operatorname{ord}(dx)=-5\). Thus a basis of holomorphic differentials is
\[
 \frac{dx}{y},\quad \frac{dx}{y^2},\quad\frac{x\,dx}{y^2},\quad
 \frac{dx}{y^3},\quad\frac{x\,dx}{y^3},\quad\frac{x^2dx}{y^3}.
\]
For input \(x^i dx/y^j\), the Cartier coefficient of output \(x^r dx/y^\ell\) is the \(11\)-th root of the coefficient of \(x^{11r+10-i}\) in \(F^{(11\ell-j)/4}\), with \(11\ell\equiv j\pmod4\). In the displayed ordering its coefficient matrix \(E\) has blocks \(V\) from the first to the last three basis elements, \(W\) from the last three to the first, and \(B\) on the two middle elements. Specifically,
\[
V=\begin{pmatrix}
5a^3b+2a^2b^4-3ab^7+4ab^2+3b^5-5\\
-3a^7-5a^5b-3a^3b^2-a^2-2ab^3+5b\\
4a^4+3a^2b-5b^2
\end{pmatrix},\quad W=\begin{pmatrix}1&0&2a\end{pmatrix},
\]
\[
 B=\begin{pmatrix}
-2a^3b+5ab^2-1&-a^3-a^2b^3+5ab+5b^4\\
-a^2+5b&5
\end{pmatrix},\quad \det(B)=D.
\]
Since the Cartier map is \(11^{-1}\)-semilinear, the rank of its twice-iterated map is computed, after applying the \(11^2\)-power automorphism to entries, by \(E^{(11)}E\), **not** by an ordinary matrix square over the generic coefficient field. The pair of unequal-dimensional eigenspaces has eventual rank two precisely when
\(W^{(11)}V=v_0+2a^{11}v_2=L\) is nonzero, and rank zero when \(L=0\); this follows by composing the two maps in both directions, with subsequent two-step compositions multiplying by powers of \(L\). The middle \(2\)-dimensional block contributes rank two when \(D\ne0\). When \(D=0\), its bottom-right entry \(5\) makes it rank one; writing it as the outer product of its second column and its second row divided by \(5\), the next twisted composition remains rank one exactly when \(m_{10}^{11}m_{01}+25=K\ne0\). This proves the rank formula.

For the \(a\)-number, \(W\ne0\) always, and the three entries of \(V\) vanish simultaneously only when \(b^5=-2\) and \(a=6b^3\), as obtained from the exact lexicographic Gröbner basis \(\bigl(a-4b^{13}-b^8-3b^3,\ (b^5+2)^3\bigr)\). The discriminant vanishes identically on these points. Hence on \(U\), \(V\ne0\), \(W\ne0\), and \(\operatorname{rank}(E)=2+\operatorname{rank}(B)\). Since \(B_{22}=5\), its rank is two for \(D\ne0\), one for \(D=0\), giving the stated \(a\)-numbers.

The claimed geometric point counts are **exact elimination statements**. Over \(\mathbb F_{11}\), the reduced lexicographic Gröbner bases of \((L,D)\) and \((D,K)\), in variable order \((a,b)\), each consist of one polynomial linear and monic in \(a\) and one polynomial in \(b\). The univariate generators are respectively
\[
\begin{aligned}
 h_{75}={}&b^{75}+3b^{70}-3b^{65}-3b^{60}-2b^{55}-b^{50}
 +2b^{45}-b^{40}+5b^{35}+5b^{20}+5b^{15}-3b^{10}-3b^5-4,\\
 h_{70}={}&b^{70}-4b^{65}+2b^{60}+5b^{55}+2b^{50}-4b^{45}
 +b^{40}+3b^{30}+4b^{25}+4b^{20}-3b^{15}+4b^{10}-5b^5+4.
\end{aligned}
\]
Both are squarefree (their gcd with their formal derivative is \(1\)), giving respectively 75 and 70 distinct geometric points with reduced local rings. Moreover, each has gcd \(1\) with the resultant \(\operatorname{Res}_a(D,\Delta)\); hence no point of either scheme is singular as a curve parameter. The ideal \((L,D,K)\) has Gröbner basis \((1)\), establishing disjointness and exclusion of \(11\)-rank zero. An explicit rank-one point is obtained by choosing \(b^5=-2\) and \(a=-3b^3\); substitution gives \(L=D=0\), \(\Delta=-1\), and \(K=-3\). The prime-field examples \((a,b)=(0,0),(1,4),(1,5)\) have respectively \((f_{11},a)=(4,2),(2,2),(3,3)\). Therefore all four positive ranks occur.

## Verification
Run `python verify_symbolic.py` using SymPy and `python verify_finite.py` using only the Python standard library. The symbolic script reconstructs \(V,W,B\) from powers of \(F\), verifies \(\Delta,L,D,K\), computes both elimination ideals, proves the squarefree-degree statements, compares against the discriminant and excludes the triple intersection. The independent finite-field script constructs the full six-by-six coefficient matrix directly for every ordered pair over \(\mathbb F_{11}\), computes its ordinary and sixfold stable ranks (valid over the prime field), and checks every formula. Of the 121 pairs it finds 10 singular models and, for smooth models, 86 with \((f,a)=(4,2)\), 15 with \((2,2)\), and 10 with \((3,3)\). The finite census does not substitute for the elimination or universal proof; the 75 and 70 geometric-point counts require exact polynomial arithmetic over \(\mathbb F_{11}\).

## Relationship to prior work
Borges–Gonçalves (arXiv:2212.03987, first public December 7, 2022) determine \(p\)-ranks of Fermat-type \(y^m=x^n+1\), including \(m=4,n=5\), with additional applications to other families. Their inspected introduction, main theorems, examples, and Section 6 do not give the complete two-parameter characteristic-eleven semilinear strata or these two reduced schemes. General Cartier coefficient methods are established mathematics, not an originality claim. The present contribution concerns the degeneration geometry and the precise finite rank-one and rank-two incidence counts of a deformation family, beyond its Fermat fiber. Camacho-Navarro (arXiv:2012.08705) studies genus-four invariants; England–Gibbons (2009) concerns a genus-six cyclic-tetragonal family with a different analytic focus. Their published subject matter provides context but no identified implication to the two 75/70-point schemes.

## Limitations
Novelty is best-knowledge relative to the retrieved research records and inspected literature, not a proof against unindexed work. The 2009 genus-six cyclic-tetragonal paper could not be fully inspected; an earlier equivalent characteristic-eleven finite-incidence computation is a residual priority risk. All results concern the specified coefficient chart, not geometric isomorphism classes or the full moduli of genus-six cyclic covers. The verification is a reproducible symbolic computation plus an independent prime-field census; it is not an independent external mathematical audit.

## References
Borges, H. and Gonçalves, C., *The p-rank of curves of Fermat type*, arXiv:2212.03987 (first version December 7, 2022), https://arxiv.org/html/2212.03987v3.

Camacho-Navarro, C., *The a-number, p-rank and Cartier points of genus 4 curves*, arXiv:2012.08705 (December 16, 2020), https://arxiv.org/abs/2012.08705.

England, M. and Gibbons, J., *A genus six cyclic tetragonal reduction of the Benney equations*, J. Phys. A 42 (2009), 375202, doi:10.1088/1751-8113/42/37/375202.
