# A universal perfect-power perimeter counting law for primitive right triangles

## Finding

For each fixed integer \(k\ge2\), write \(N_k(X)\) for the number of primitive right triangles with positive integer side lengths, perimeter at most the real number \(X\), and perimeter a perfect \(k\)-th power. Interchanging the legs does not produce a second triangle. As \(X\to\infty\),

\[
\boxed{N_k(X)=\frac{\log 2}{k\pi^2}X^{1/k}+O_k\!\left(X^{1/(2k)}\log(2X)\right).}
\]

In particular, all fixed power exponents occur infinitely often. The constants for squares and cubes are, respectively, \(\log 2/(2\pi^2)\) and \(\log 2/(3\pi^2)\). No assertion of uniformity when \(k\) varies with \(X\) is made.

## Assumptions and scope

A primitive right triangle is one whose three positive integral sides have gcd \(1\). We use the classical unique Euclid parametrization up to interchanging the legs:

\[
(a,b,c)=(m^2-n^2,2mn,m^2+n^2),\quad m>n\ge1,\quad (m,n)=1,\quad m\not\equiv n\pmod2.
\]

Its perimeter is \(P=2m(m+n)\). A perfect \(k\)-th power means \(P=t^k\) for an integer \(t\ge1\). All constants implicit in \(O_k\) may depend on the fixed exponent \(k\).

The exact parameter domain is

\[
\mathcal R_k(X)=\{(u,v)\in\mathbb Z_{>0}^2:(u,v)=1,\ v\equiv1\pmod2,\ 2^{1-1/k}u<v<2u,\ (2uv)^k\le X\}.
\]

There is a bijection between \(\mathcal R_k(X)\) and the triangles counted by \(N_k(X)\), given by

\[
m=2^{k-1}u^k,\quad n=v^k-2^{k-1}u^k,\quad (a,b,c)=(m^2-n^2,2mn,m^2+n^2).
\]

## Proof

**1. Exact power parametrization.** Put \(s=m+n\), so \((m,s)=1\) and \(P=2ms\). If \(m\) were odd, then \(s\) would also be odd (because \(m,n\) have opposite parity), and \(v_2(P)=1\), impossible for \(P=t^k\) with \(k\ge2\). Thus \(m\) is even, \(s\) is odd, and \((2m,s)=1\). From \((2m)s=t^k\), unique prime factorization forces each coprime factor to be a \(k\)-th power: \(2m=(2u)^k\) and \(s=v^k\), for positive integers \(u,v\) with \(v\) odd and \((u,v)=1\). Consequently \(m=2^{k-1}u^k\), \(n=v^k-m\), and \(P=(2uv)^k\). The constraints \(0<n<m\) are equivalent to \(2^{1-1/k}u<v<2u\). Conversely, every such \((u,v)\) produces \(m>n>0\), opposite parity, \((m,n)=(m,v^k)=1\), so a unique primitive triangle. This proves the exact bijection.

**2. Area of the parameter region.** Put \(Y=X^{1/k}/2\) and \(\alpha_k=2^{1-1/k}\). In the positive real plane let

\[
R_k(Y)=\{(u,v):\alpha_k u<v<2u,\ uv\le Y\}.
\]

Writing \(t=v/u\) and \(w=uv\), the Jacobian of \((w,t)\mapsto(u,v)\) is \(1/(2t)\). Therefore

\[
\operatorname{area}(R_k(Y))=\int_{\alpha_k}^{2}\int_0^Y\frac{dw\,dt}{2t}
=\frac Y2\log\frac2{\alpha_k}=\frac{Y\log2}{2k}.
\]

The region \(R_k(1)\) is bounded, with a boundary comprising two radial segments and a smooth hyperbola arc. Its dilation \(R_k(Y)=\sqrt Y\,R_k(1)\) has boundary length \(O_k(\sqrt Y)\). Tiling the plane by unit-by-two rectangles gives, for \(Y\ge1\),

\[
L_k(Y):=\#\{(u,v)\in R_k(Y)\cap\mathbb Z_{>0}^2:v\text{ odd}\}
=\frac12\operatorname{area}(R_k(Y))+O_k(\sqrt Y+1).
\]

The discrepancy estimate follows because only rectangles meeting the boundary can differ between their expected area contribution and lattice-point contribution; their number is \(O_k(\sqrt Y+1)\). This also covers weak equality at the hyperbolic boundary.

**3. Primitivity sieve and main term.** Since \(v\) is odd, every common divisor \(d\mid(u,v)\) is odd. Möbius inversion, scaling, and the exact bijection imply

\[
N_k(X)=\sum_{\substack{1\le d\le\sqrt Y\\d\text{ odd}}}\mu(d)L_k(Y/d^2).
\]

The upper bound on \(d\) is valid because \(d^2\mid uv\le Y\). Inserting the lattice estimate yields

\[
N_k(X)=\frac{Y\log2}{4k}\sum_{\substack{d\le\sqrt Y\\d\text{ odd}}}\frac{\mu(d)}{d^2}
+O_k\!\left(\sqrt Y\sum_{d\le\sqrt Y}\frac1d+\sqrt Y\right).
\]

The omitted tail of the absolutely convergent Dirichlet series contributes \(O_k(\sqrt Y)\). Its full odd-part Euler product is

\[
\sum_{\substack{d\ge1\\d\text{ odd}}}\frac{\mu(d)}{d^2}
=\prod_{p\ne2}(1-p^{-2})
=\frac{1}{\zeta(2)(1-2^{-2})}=\frac8{\pi^2}.
\]

Thus

\[
N_k(X)=\frac{2Y\log2}{k\pi^2}+O_k(\sqrt Y\log(2Y))
=\frac{\log2}{k\pi^2}X^{1/k}
+O_k\!\left(X^{1/(2k)}\log(2X)\right).
\]

Every step holds for each fixed integer \(k\ge2\). The positive leading constant implies infinitely many such triangles.

## Verification

Run `python artifacts/verify.py` with Python 3; only the standard library is required. The script independently enumerates Euclid parameter pairs with \(m\le2200\) and tests exact membership in precomputed integer perfect-power sets for exponents \(k=2,3,4,5\). It independently enumerates the \((u,v)\) parameter region, comparing the complete sets of \((m,n,P)\) and their counts under three perimeter cutoffs. It verifies seven cube-perimeter solutions and the first fourth-power case within this Euclid range, plus an explicit fifth-power example beyond the range. These finite regressions check the exact parametrization only: neither they nor floating-point approximations certify the asymptotic.

For \(k=3\), \((m,n)=(108,17)\) gives the triangle \((3672,11375,11953)\) with perimeter \(27000=30^3\). For \(k=4\), \((m,n)=(2048,353)\) gives a perimeter \(56^4\).

## Relationship to prior work

The ordinary enumeration of primitive Pythagorean triangles by perimeter, with main term \((\log2/\pi^2)X\) and error \(O(X^{1/2}\log X)\), is classical (Lehmer; Lambek and Moser). It counts *all* primitive triangles, not the sparse subclass with power perimeters. That theorem cannot be specialized merely by replacing its bound \(X\) by \(X^{1/k}\): it would count all triangles below a smaller bound, not triangles whose perimeter is a perfect power.

Yiu's treatment of square perimeters gives the \(k=2\) exact power parametrization and examples; those are prior work. OEIS A077177 records the general fixed-semiperimeter count through odd unitary divisors; OEIS A120089 tabulates square-perimeter examples. A published fixed-prime-support study of square-perimeter triangles proves a different, logarithmic asymptotic for *each fixed odd-prime support*; it does not count the union over unrestricted, growing prime support or higher powers. The present finding is the all-support counting law for every fixed \(k\ge2\), including the leading constant and error term.

## Limitations

No uniform statement in \(k\) is proved. The count is of triangles rather than distinct perimeter values; several different triangles can share a perimeter. Exact finite checks do not prove an asymptotic. The novelty comparison covers the cited sources and targeted literature searches, not all unindexed problem literature, so unrecognized earlier equivalents remain possible.

## References

1. J. Lambek and L. Moser, *On the distribution of Pythagorean triangles*, Pacific Journal of Mathematics **5** (1955), 73–83. https://msp.org/pjm/1955/5-1/pjm-v5-n1-p07-s.pdf
2. P. Yiu, *Recreational Mathematics*, §6.2, “Primitive Pythagorean triangles with square perimeters,” p. 211. https://web.bogazici.edu.tr/topcu/RecreationalMathematics.pdf
3. K. Rose and R. L. Rathbun, OEIS A077177, “Number of primitive Pythagorean triangles with perimeter equal to primorial.” https://oeis.org/A077177
4. OEIS A120089, “Square perimeters of primitive Pythagorean triangles.” https://oeis.org/A120089
5. *Fixed prime support in square-perimeter primitive Pythagorean triangles* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/21/SCOPE-pythagorean-square-perimeter-fixed-prime-support--1c78d6da7690
