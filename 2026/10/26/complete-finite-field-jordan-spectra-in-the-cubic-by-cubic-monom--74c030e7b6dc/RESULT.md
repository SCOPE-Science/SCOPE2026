# Complete finite-field Jordan spectra in the cubic-by-cubic monomial complete intersection

## Finding
Let \(k=\mathbb F_q\) have characteristic \(p\ge5\), where \(q\) is an arbitrary prime power, and put \(A=k[x,y]/(x^3,y^3)\), \(\mathfrak m=(x,y)\). For each \(u\in\mathfrak m\), write \(\lambda(u)\) for the Jordan partition of multiplication \(L_u:A\to A\). The following ten partitions, and no others, occur. Their exact multiplicities are:

| Jordan partition \(\lambda\) | \(\#\{u\in\mathfrak m:\lambda(u)=\lambda\}\) |
|---|---:|
| \((5,3,1)\) | \((q-1)^2q^6\) |
| \((4,3,2)\) | \(2(q-1)^2q^5\) |
| \((3,3,3)\) | \(2(q-1)q^5\) |
| \((3,2,2,1,1)\) | \(q^3(q-1)(q^2-q+1)\) |
| \((2,2,2,2,1)\) | \(q^3(q-1)^2\) |
| \((3,2,1,1,1,1)\) | \(q^3(q-1)^2\) |
| \((2,2,2,1,1,1)\) | \(2q^3(q-1)\) |
| \((2,2,1,1,1,1,1)\) | \(q(q^2-1)\) |
| \((2,1,1,1,1,1,1,1)\) | \(q-1\) |
| \((1,1,1,1,1,1,1,1,1)\) | \(1\) |

All counts are strictly positive. In particular, \(\#\mathfrak m=q^8\), the proportion of elements having the largest attainable nilpotency index \(5\) is \((1-q^{-1})^2\), and the generic Jordan type is \((5,3,1)\). No nilpotent multiplication operator on this algebra consists of a single block of length nine.

## Assumptions and scope
The monomials \(x^iy^j\), \(0\le i,j\le2\), form a basis of the nine-dimensional algebra. A general element of its maximal ideal has the unique expansion
\[
u=ax+by+cx^2+dxy+ey^2+fx^2y+gxy^2+hx^2y^2.
\]
The theorem counts **elements**, not conjugacy orbits or distinct quotient ideals. No algebraic closure or primality assumption on \(q\) is made. Characteristic \(2\) or \(3\) is excluded because coefficients \(2,3,6\) used below become singular there.

## Proof
**Case I: nonzero linear part.** Suppose first \(ab\ne0\). Because the coefficient of \(x\) in \(u\) is a unit, elimination in the complete local power-series ring expresses \(x\) modulo \((u)\) as a polynomial in \(y\) with zero constant term. Imposing \(x^3=y^3=0\) introduces no further restriction, so \(A/(u)\cong k[y]/(y^3)\). Thus \(L_u\) has exactly three Jordan blocks. Degree considerations give \(u^5=0\), whereas
\[
u^4=6a^2b^2x^2y^2\ne0.
\]
To determine the other block sizes, consider multiplication by the lowest-degree term \(\ell^2=(ax+by)^2\) of \(u^2\) on the associated degree filtration. It has nonzero degree-two image from constants, rank two from degree one to degree three (determinant \(3a^2b^2\)), and nonzero degree-four image from degree two. These lie in distinct degrees and force \(\operatorname{rank}(L_{u^2})\ge4\). Among partitions of nine with three blocks and maximum part five, this forces \((5,3,1)\). There are \((q-1)^2q^6\) choices.

Next suppose \(a\ne0,b=0\), the other case being symmetric. Elimination still gives \(\dim_k A/(u)=3\). If \(e\ne0\), then \(u^3=3a^2e x^2y^2\ne0\) and \(u^4=0\), so exactly one of the three blocks has size four; the other two have sizes three and two. This is \((4,3,2)\), with \((q-1)^2q^5\) possibilities per choice of which linear coefficient is nonzero. If \(e=0\), every monomial in \(u\) is divisible by \(x\), and \(u=xv\) for a unit \(v\in A\). Multiplication by \(u^j=x^jv^j\) has the same rank as multiplication by \(x^j\) for every \(j\), hence \(\lambda(u)=(3,3,3)\). There are \((q-1)q^5\) such elements per orientation.

**Case II: vanishing linear part, nonzero quadratic part.** Suppose \(a=b=0\) and \(Q=cx^2+dxy+ey^2\ne0\). Contributions from the cubic and quartic terms cannot change multiplication ranks: the leading images occupy degrees two, three and four, and the degree-four image from the quadratic basis absorbs higher-degree corrections. Thus
\[
\operatorname{rank}L_u=2+\operatorname{rank}
\begin{pmatrix}d&c\\e&d\end{pmatrix}
=\begin{cases}4,&D\ne0,\\3,&D=0,\end{cases}\qquad D=d^2-ce.
\]
Also \(u^3=0\) and \(u^2=(d^2+2ce)x^2y^2\). Put \(S=d^2+2ce\). Therefore \(\operatorname{rank}L_{u^2}=1\) if \(S\ne0\), and zero otherwise. For a nilpotent operator with all blocks of size at most three, the number of blocks of size three is \(\operatorname{rank}L_{u^2}\), and the number of size-two blocks is \(\operatorname{rank}L_u-2\operatorname{rank}L_{u^2}\). This gives, in the order \((D\ne0,S\ne0)\), \((D\ne0,S=0)\), \((D=0,S\ne0)\), \((D=S=0)\), exactly
\[
(3,2,2,1,1),\ (2,2,2,2,1),\ (3,2,1,1,1,1),\ (2,2,2,1,1,1).
\]
Each of \(D=0\) and \(S=0\) is a nonsingular split conic in the projective plane over \(k\); each has \(q+1\) rational points and hence \(q^2-1\) nonzero affine triples. Their nonzero intersections satisfy \(3ce=0\), so consist exactly of \((c,0,0)\) and \((0,0,e)\), totaling \(2(q-1)\) triples. Inclusion–exclusion gives the four respective counts of nonzero \((c,d,e)\):
\[
(q-1)(q^2-q+1),\quad(q-1)^2,\quad(q-1)^2,\quad2(q-1).
\]
The coefficients \(f,g,h\) are completely free, multiplying each count by \(q^3\).

**Case III: order at least three.** If \(a=b=c=d=e=0\) and \((f,g)\ne(0,0)\), the map \(L_u\) has rank two and square zero: its degree-three image from the unit and its degree-four image from a linear monomial are independent. Hence the partition is \((2,2,1,1,1,1,1)\), with \(q(q^2-1)\) choices. If only \(h\ne0\), the rank is one and the partition \((2,1,1,1,1,1,1,1)\), with \(q-1\) choices. Finally \(u=0\) has partition \((1,1,1,1,1,1,1,1,1)\). The three cases are exhaustive and disjoint, and the displayed numbers add to \(q^8\). Every step uses coefficients invertible in characteristic at least five. \(\square\)

## Verification
The supplied `verify_jordan_33.py` constructs the multiplication matrices directly in the monomial basis, computes successive powers using finite-field arithmetic, and reconstructs each Jordan partition from differences of their ranks. It independently checks the quadratic discriminant strata over \(\mathbb F_5,\mathbb F_7,\mathbb F_{11}\); it exhausts a 3125-element quadratic-and-higher slice over \(\mathbb F_5\) and tests 1500 deterministic full-radical samples over each of the three prime fields. The replay prints `VERIFY_OK_JORDAN_33_COMPLETE_SPECTRUM`. The general theorem over all finite extension fields follows from the proof, not from those finite experiments.

## Relationship to prior work
Harima–Migliore–Nagel–Watanabe provide foundational results on Lefschetz properties for Artinian algebras; Cook studies monomial complete intersections in positive characteristic. Iarrobino–Macias Marques–McDaniel explicitly calculate the Jordan partition \((3,2,2,1,1)\) for the individual element \(x^2+y^2\) of this very algebra (Example 3.8); that individual case is prior knowledge. Altafi–Iarrobino–Khatami study complete-intersection Jordan types, especially linear forms. The additional assertion here is the **full finite-field frequency distribution for all elements of the maximal ideal**, including arbitrary nonlinear components and all ten strata in characteristics at least five. No claim is made that generic Lefschetz behavior or the example \(x^2+y^2\) is novel.

## Limitations
This result concerns the fixed cubic-by-cubic algebra only and fields of characteristic at least five. It counts finite-field points, not scheme-theoretic multiplicities of Jordan strata. Numerical checking is not a substitute for the stated proof. The possibility of implicit coverage by broader published classifications remains a historical-priority risk, and the mathematics has not undergone independent audit.

## References
1. Harima, Migliore, Nagel and Watanabe, *The Weak and Strong Lefschetz Properties for Artinian K-Algebras*, initial arXiv version 2002-08-26, https://arxiv.org/abs/math/0208201.
2. D. Cook II, *The Lefschetz Properties of Monomial Complete Intersections in Positive Characteristic*, initial arXiv version 2011-11-21, https://arxiv.org/abs/1111.4979.
3. Iarrobino, Macias Marques and McDaniel, *Artinian Algebras and Jordan Type*, Example 3.8, https://arxiv.org/abs/1802.07383.
4. Altafi, Iarrobino and Khatami, *Complete Intersection Jordan Types in Height Two*, https://arxiv.org/abs/1810.00716.
