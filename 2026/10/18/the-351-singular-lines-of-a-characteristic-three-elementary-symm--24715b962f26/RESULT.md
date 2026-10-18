# The 351 singular lines of a characteristic-three elementary-symmetric quartic

## Finding

Let \(k\) be algebraically closed of characteristic \(3\). Write \(e_j\) for the degree-\(j\) elementary symmetric polynomial in nine variables and set
\[
X=V(e_4(x_1,\ldots,x_9))\subset\mathbb P^8_k.
\]
The **entire reduced projective singular locus** is a union of exactly \(351\) distinct projective lines. They have the following two types, and no others:

1. For every two-element subset \(\{i,j\}\subset[9]\), the coordinate line
\[
C_{ij}=\mathbb P\!\left(\operatorname{span}\{\mathbf e_i,\mathbf e_j\}\right).
\]
There are \(\binom92=36\) such lines.
2. Choose a singleton \(\{i\}\) and an **unordered** partition \([9]\setminus\{i\}=B\sqcup C\) with \(|B|=|C|=4\). Put \(v_{B,C}=\mathbf1_B-\mathbf1_C\). The line is
\[
D_{i;\{B,C\}}=\mathbb P\!\left(\operatorname{span}\{\mathbf e_i,v_{B,C}\}\right).
\]
There are \(9\binom84/2=315\) such lines. Interchanging \(B,C\) changes the sign of the second spanning vector, not the line.

Consequently the reduced singular locus is pure of dimension \(1\), its degree is \(351\), and \(X\) is a geometrically integral normal quartic hypersurface of dimension \(7\). The assertion is set-theoretic and reduced-scheme-theoretic; **the nonreduced Jacobian scheme is not classified here**.

## Assumptions and scope

All equations and all projective spaces are over an algebraically closed field \(k\) with \(\operatorname{char}(k)=3\). Coordinates are indexed by \([9]=\{1,\ldots,9\}\). The vectors \(\mathbf e_i\) denote standard basis vectors; \(\mathbf1_B\) is the zero-one indicator vector of \(B\). The singular locus of a hypersurface means the nonregular locus of its reduced variety; here it coincides in support with the zero locus of all nine ordinary first partial derivatives, because the quartic is squarefree and its degree \(4\) is nonzero in \(k\).

The exact numerical claim is about \(e_4\) in **nine** variables and characteristic \(3\); no formula is claimed for all dimensions or all positive characteristics. This distinction matters: the maximal-dimension and coordinate-local-structure theorems in the literature do not themselves determine the additional \(315\) lines.

## Proof

**Step 1: a universal cubic for singular coordinates.** The deletion identity for elementary symmetric functions gives, for every \(i\),
\[
\frac{\partial e_4}{\partial x_i}
=e_3-x_i e_2+x_i^2e_1-x_i^3.
\]
Thus if every derivative vanishes, every coordinate is a root of the monic cubic
\[
P(T)=T^3-e_1T^2+e_2T-e_3.
\]
There can be at most three distinct coordinate values. Euler's formula says \(\sum_i x_i\partial_i e_4=4e_4=e_4\) in characteristic \(3\), so simultaneous gradient vanishing already implies membership in \(X\).

**Step 2: exactly three distinct values.** Suppose the values are pairwise distinct \(a,b,c\), of respective positive multiplicities \(r,s,t\) with \(r+s+t=9\). Since \(P\) is monic of degree three, \(P(T)=(T-a)(T-b)(T-c)\). Matching its first and second elementary coefficients and using the identity \(2e_2=e_1^2-\sum_i x_i^2\) gives
\[
(r-1)a+(s-1)b+(t-1)c=0,
\qquad
(r-1)a^2+(s-1)b^2+(t-1)c^2=0.
\]
Set \(\delta_r=r-1\) in \(\mathbb F_3\), and similarly for \(s,t\). Since \(r+s+t=9\), these three elements sum to zero. Choosing representatives in \(\{-1,0,1\}\), the possibilities are all zero; all \(1\); all \(-1\); or a permutation of \((1,-1,0)\). The latter forces two values equal. Either all-equal-sign alternative forces
\(a+b+c=a^2+b^2+c^2=0\); setting \(c=-a-b\) then gives \((a-b)^2=0\), and hence \(a=b=c\), also a contradiction. Therefore
\[
r\equiv s\equiv t\equiv1\pmod3.
\]
With positive multiplicities totaling nine, up to permutation there are precisely two options: \((r,s,t)=(1,1,7)\) and \((1,4,4)\).

Write \(r=1+3R\), \(s=1+3S\), \(t=1+3T\) with \(R,S,T\in\{0,1,2\}\). In characteristic three the generating polynomial of the nine coordinates satisfies
\[
(1+az)^r(1+bz)^s(1+cz)^t
\equiv(1+az)(1+bz)(1+cz)
\bigl(1+(Ra^3+Sb^3+Tc^3)z^3\bigr)\pmod{z^4}.
\]
The equality of the third coefficients with those of \((T-a)(T-b)(T-c)\) is equivalent to
\[
Ra^3+Sb^3+Tc^3=(Ra+Sb+Tc)^3=0,
\]
and hence to \(Ra+Sb+Tc=0\). For the pattern \((1,1,7)\), the value carried by the seven-coordinate block must be zero, so the point lies on \(C_{ij}\), where \(i,j\) are the singleton positions. For \((1,4,4)\), the two four-coordinate values are negatives of one another, so the point lies on the corresponding \(D_{i;\{B,C\}}\).

Conversely, on \(C_{ij}\) the nine coordinates are \((a,b,0,\ldots,0)\) up to permutation and the cubic is \(P(T)=T(T-a)(T-b)\). On \(D_{i;\{B,C\}}\), they are \((a,b,b,b,b,-b,-b,-b,-b)\), up to permutation. Their generating polynomial modulo \(z^4\) is \((1+az)(1-b^2z^2)\), so \(P(T)=(T-a)(T-b)(T+b)\). In both cases every coordinate is a root of \(P\), proving all derivatives vanish **for every point of every indicated line**, including collision and zero-value specializations.

**Step 3: one or two distinct values.** A nonzero constant vector is not critical: each derivative equals \(\binom83a^3=56a^3=2a^3\ne0\) for \(a\ne0\).

For two distinct values \(u\) and \(v\), suppose \(u\) occurs \(r\) times and \(v\) occurs \(9-r\) times, \(1\le r\le8\). The two derivative equations are the cubics
\[
f_r(u,v)=e_3(u^{[r-1]},v^{[9-r]}),\qquad
g_r(u,v)=e_3(u^{[r]},v^{[8-r]}),
\]
where bracket exponents mean repeated entries, not ordinary powers. Expanding with binomial coefficients modulo three gives the complete table

| \(r\) | \(f_r\) | \(g_r\) | Projective solutions with distinct values |
|---|---|---|---|
| 1, 2 | \(-v^3\) | \(-v^3\) | \(v=0\) |
| 3 | \(-v^3\) | \(u^3+v^3\) | none |
| 4, 5 | \(u^3+v^3\) | \(u^3+v^3\) | \(v=-u\) |
| 6 | \(u^3+v^3\) | \(-u^3\) | none |
| 7, 8 | \(-u^3\) | \(-u^3\) | \(u=0\) |

When one value vanishes, at most two positions are nonzero, giving a point on a coordinate line. The \(r=4,5\) solutions are also on balanced lines: split the block of five equal entries into one singleton plus four entries. Thus **every** singular point, with one, two, or three coordinate values, lies in the asserted union.

**Step 4: components, degree, integrality, normality.** Each indicated subspace is a projective line; the coordinate lines are pairwise distinct. A balanced line contains precisely one coordinate vertex, its distinguished singleton, and has a direction vector supported on eight coordinates. Its singleton and unordered four/four partition can therefore be recovered from its line; it cannot equal a coordinate line. Hence the \(36+315=351\) lines are distinct and no one contains another. The reduced singular locus is their union, pure one-dimensional and of degree \(351\), as degree is additive on its one-dimensional irreducible components.

The gradient vanishing support has dimension one. If the quartic polynomial had a repeated nonconstant factor, the corresponding hypersurface would lie in the gradient zero locus and have dimension seven; if it had two distinct nonconstant factors, their projective intersection would lie in the gradient zero locus and have dimension at least six. Both contradict the computed singular support. Hence the quartic is geometrically irreducible and squarefree. As a hypersurface, \(X\) is Cohen--Macaulay (thus \(S_2\)); its singular locus has codimension six in the sevenfold, so it is regular in codimension one (\(R_1\)). Serre's criterion gives normality. This completes the proof.

## Verification

A standalone Python 3 checker `check.py` uses the standard library only. Run `python3 check.py` from the directory containing this file. It independently constructs all \(351\) line bases and verifies they span \(351\) distinct two-dimensional vector subspaces over \(\mathbb F_3\). It restricts each of the nine cubic gradient polynomials to each line and checks that **all four polynomial coefficients vanish**, rather than testing only sample points. It separately enumerates the entire projective space \(\mathbb P^8(\mathbb F_3)\) and finds exactly \(522\) critical points, exactly the union of the predicted \(\mathbb F_3\)-rational line points. Finally it checks the eight two-value binomial-coefficient derivative cases in the proof. The expected output begins `VERIFY_OK`.

An optional independently executable `gf9_stress.py` checks all 14,112 three-value multiplicity assignments over \(\mathbb F_9\), with 336 singular cases matching the two required patterns. The field enumeration is a finite consistency test, not a proof over \(k\). The proof of completeness over an algebraic closure is the root-and-multiplicity argument above; the line restrictions are symbolic polynomial identities in characteristic three.

## Relationship to prior work

Cafure--Matera--Privitelli's 2011 preprint established a partition-space bound for singularities of symmetric hypersurfaces (Theorem 3.1 and Remark 3.2); it does not enumerate the singular components of this characteristic-three quartic. Orzel studied the possible dimensions of positive-characteristic elementary-symmetric order-two zero loci, not this full component arrangement. Xie's 2026 preprint gives an exact dimension formula and generic coordinate-component local rings; for \(n=9,d=4,p=3\), it yields projective singular-locus dimension one and treats the \(36\) coordinate lines. It explicitly leaves smaller-dimensional components unclassified. The additional \(315\) balanced lines and exhaustion of all components are the proposed increment; no novel dimension formula or coordinate-local-ring formula is claimed.

Prior classifications for characteristic-three elementary-symmetric **cubics** and characteristic-two **quartics** concern different degree/characteristic pairs and do not imply this nine-variable characteristic-three quartic. Targeted literature and research-database checks did not locate an equivalent \(351\)-line classification. Absence of a search hit does not establish uniqueness, and implicit coverage in other literature remains possible.

## Limitations

This theorem concerns the complete **reduced** projective singular support for one natural quartic and its degree. It does not assert radicality of the Jacobian ideal, compute multiplicities or embedded components, describe the complete line-intersection lattice, or classify arbitrary numbers of variables. The closest broad positive-characteristic work already determines the dimension and some generic coordinate thickness. The distinction between those known results and the new \(315\)-line component family is essential.

## References

1. A. Cafure, G. Matera, M. Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed--Solomon codes*, arXiv:1109.2265v1 (first posted 2011-09-10), §3, Theorem 3.1 and Remark 3.2; later *Advances in Mathematics of Communications* 6 (2012), 69--94. https://arxiv.org/abs/1109.2265
2. I. Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics*, arXiv:2509.05009v3, §2, especially Conjecture 2.11. https://arxiv.org/abs/2509.05009
3. Y. Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259v1 (2026-09-24), Theorems 1.1, 1.3, 1.4 and §7. https://arxiv.org/abs/2610.00259
4. I. Meckler and G. Zaimi, *Singular locus of zero set of elementary symmetric polynomial*, MathOverflow question and answer 264226 (2017); characteristic-zero analysis and explicit discussion of failure in positive characteristic. https://mathoverflow.net/questions/264226/singular-locus-of-zero-set-of-elementary-symmetric-polynomial
