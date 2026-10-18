# Derivation-rank polynomials and a nonsmooth symmetry jump in a four-dimensional monomial complete intersection

## Finding

For every prime power \(q\), let \(k=\mathbb F_q\) and let the commutative unital algebra be \(A=k[X,Y]/(X^2,Y^2)\). For \(0\le r\le3\), let \(N_r(q)\) count the \(k\)-derivations \(D:A\to A\) whose rank as a \(k\)-linear endomorphism is exactly \(r\). The complete rank polynomial \(P_q(z)=\sum_{r=0}^{3}N_r(q)z^r\) has the following two cases. When \(\operatorname{char}k\ne2\),

\[
P_q(z)=1+(q^2-1)z+3q^2(q-1)z^2+q^2(q-1)(q-2)z^3.
\]

When \(\operatorname{char}k=2\),

\[
\begin{aligned}
P_q(z)={}&1+(q-1)(q+1)^2z\\
&+q(q-1)(q^4+3q^3+2q^2-1)z^2\\
&+q^3(q-1)(q^4+q^3-2q-1)z^3.
\end{aligned}
\]

The dimension of \(\operatorname{Der}_k(A)\) is \(4\) in odd characteristic and \(8\) in characteristic \(2\). Over fields of characteristic \(2\), the automorphism group scheme \(\underline{\operatorname{Aut}}_k(A)\) has nonreduced coordinate ring

\[
k[a_0,b_0,a_1,a_2,a_3,b_1,b_2,b_3,\Delta^{-1}]/(a_0^2,b_0^2),\quad \Delta=a_1b_2-a_2b_1,
\]

so its reduced geometric dimension is \(6\), while its tangent-space dimension at the identity is \(8\). In odd characteristic it is smooth at the identity, with both dimensions equal to \(4\). For reference, the orders of the groups of rational automorphisms are \(q^2|\operatorname{GL}_2(k)|\) in characteristic \(2\) and \(2q^2(q-1)^2\) in odd characteristic.

## Assumptions and scope

The formula counts all \(k\)-linear derivations, not only those preserving the maximal ideal and not only those tangent to the reduced automorphism group. The algebra is the **commutative** length-four monomial complete intersection with basis \((1,X,Y,XY)\). Its rank-polynomial statement covers all prime powers including non-prime fields. The group-scheme statement concerns the functor of unital \(k\)-algebra automorphisms after arbitrary commutative base change.

## Proof

**Derivation coordinates.** Every derivation annihilates \(1\), and is determined by \(u=D(X)\) and \(v=D(Y)\). The complete presentation relations impose \(2Xu=2Yv=0\); conversely these relations suffice to define a derivation, since the polynomial-ring derivation specified by \(u,v\) descends precisely when it preserves the defining ideal.

When \(\operatorname{char}k\ne2\), write \(u=aX+bXY\) and \(v=cY+dXY\), with \(a,b,c,d\in k\). On \((X,Y,XY)\), the derivation has matrix

\[
\begin{pmatrix}a&0&0\\0&c&0\\b&d&a+c\end{pmatrix}.
\]

If \(a=c=0\), the matrix has rank \(0\) only for \(b=d=0\) and otherwise rank \(1\). If precisely one of \(a,c\) is nonzero, or if both are nonzero with \(a+c=0\), the rank is \(2\). If both are nonzero and \(a+c\ne0\), it is \(3\). Counting these four disjoint cases gives the odd-characteristic coefficients above.

When \(\operatorname{char}k=2\), all eight coefficients of \(u=a_0+a_1X+a_2Y+a_3XY\) and \(v=b_0+b_1X+b_2Y+b_3XY\) are free. On the three input columns \((X,Y,XY)\), the full derivation matrix (rows \((1,X,Y,XY)\)) is

\[
M=\begin{pmatrix}
a_0&b_0&0\\a_1&b_1&b_0\\a_2&b_2&a_0\\a_3&b_3&a_1+b_2
\end{pmatrix}.
\]

First suppose \((a_0,b_0)\ne(0,0)\). Any invertible linear substitution of \((X,Y)\) defines an automorphism, since in characteristic \(2\) all its linear combinations square to zero. Conjugating the derivation normalizes the constant pair to \((1,0)\) and preserves rank. With this normalization the columns are \((1,a_1,a_2,a_3)^T\), \((0,b_1,b_2,b_3)^T\), and \((0,0,1,a_1+b_2)^T\). Rank \(2\) holds precisely for \(b_1=0\) and \(b_3=b_2(a_1+b_2)\); there are \(q^4\) such choices among the \(q^6\) remaining coordinates. Thus the nonzero constant pairs contribute \((q^2-1)q^4\) rank-two and \((q^2-1)(q^6-q^4)\) rank-three derivations.

For \((a_0,b_0)=(0,0)\), the effective matrix is

\[
\begin{pmatrix}a_1&b_1&0\\a_2&b_2&0\\a_3&b_3&a_1+b_2\end{pmatrix}.
\]

Let \(B\) be its upper-left \(2\)-by-\(2\) block, and \(\tau=\operatorname{tr}B\). Among the \(q^4\) possible \(B\)'s, the numbers with rank/tracestatus \((0,0),(1,0),(1,\ne0),(2,0),(2,\ne0)\) are respectively

\[
1,\quad q^2-1,\quad q(q^2-1),\quad q^2(q-1),\quad |\operatorname{GL}_2(k)|-q^2(q-1).
\]

Indeed every nonzero trace-zero rank-one matrix is \(uv^T\) with \(v^Tu=0\), giving \(q^2-1\); the remaining entries follow from the usual rank-one count and the \(q^3\) trace-zero matrices. For \(B=0\), the lower row yields one rank-zero and \(q^2-1\) rank-one cases. For rank-one trace-zero \(B\), exactly \(q\) of the \(q^2\) lower rows lie in its row space and give rank one, while the others give rank two. For rank-one nonzero-trace or rank-two zero-trace \(B\), every lower row gives rank two. For rank-two nonzero-trace \(B\), every lower row gives rank three. Therefore, within the zero-constant slice the four rank counts are

\[
1,\quad(q-1)(q+1)^2,\quad q(q-1)(2q^3+2q^2-1),\quad q^3(q-1)(q^2-q-1).
\]

Adding the nonzero-constant slice and collecting powers gives the stated characteristic-two rank polynomial. Its coefficient sum is \(q^8\), while the odd-characteristic coefficient sum is \(q^4\), as required.

**Automorphism scheme.** In characteristic \(2\), a base-changed algebra endomorphism must send \(X\) and \(Y\) to \(u,v\) with \(u^2=a_0^2=0\) and \(v^2=b_0^2=0\). The ideal \((a_0,b_0)\) in the parameter ring is nilpotent, and reducing modulo this ideal shows that the determinant of the induced \(4\)-by-\(4\) linear endomorphism is \(\Delta^2\). Hence the endomorphism is invertible if and only if \(\Delta\) is invertible. This proves the coordinate-ring presentation. The reduced scheme is \(\operatorname{GL}_2\times\mathbb A^2\), of dimension \(6\), whereas the two square-zero equations have zero linear terms at the identity, giving tangent dimension \(8\) and proving nonsmoothness.

For odd characteristic, over field points the coefficient-field constants vanish and the square-zero conditions force each column of the degree-one matrix to contain exactly one nonzero entry for invertibility. Thus there are two monomial configurations, each with \((q-1)^2q^2\) choices. Near the identity in the automorphism scheme the coefficients of \(X\) in its own image and of \(Y\) in its own image are units; the coefficients of \(X\) and \(Y\) in the defining square-zero identities force both constants and both off-diagonal linear terms to vanish. The four remaining coefficients are free, with two units, giving a smooth identity neighborhood of dimension \(4\). These calculations also prove the rational automorphism counts.

## Verification

Run `python3 check.py` in the directory containing this document. The standalone checker builds the multiplication table of \(A\), constructs every possible pair \((D(X),D(Y))\) for \(q=2,3,4\), tests the Leibniz rule on all basis-product pairs, computes ranks by field Gaussian elimination, and compares exact counts to the formulas. Separately, it enumerates all possible square-zero substitutions and tests full-rank invertibility, comparing the rational automorphism counts. The characteristic-two extension field \(\mathbb F_4\) is represented as \(\mathbb F_2[t]/(t^2+t+1)\). All checks pass; the algebraic proof, not the finite experiments, establishes the arbitrary-field theorem.

## Relationship to prior work

Díaz, Liendo, Manzano-Flores and Regeta, *The Automorphism groups of zero-dimensional monomial algebras* (arXiv:2408.02197; initially public 2024-08-05), study characteristic-zero monomial algebras and explicitly treat the same quotient \(k[X,Y]/(X^2,Y^2)\) in Example 4.25. Their Theorem 3.7 concerns homogeneous locally nilpotent derivations, and their Example 4.25 describes automorphism generators. The present statement neither claims these classifications nor follows from their characteristic-zero hypotheses: it counts finite-field ranks for **all** derivations and identifies the characteristic-two nonreduced automorphism scheme. Basic descriptions of derivations of monomial quotients are also classical; the new question here is the exact characteristic-dependent rank distribution and its connection to infinitesimal symmetry.

## Limitations

The rank polynomial is proved for this specified four-dimensional algebra, not for arbitrary monomial complete intersections, and it counts derivations rather than their conjugacy classes or Jordan types. Finite exhaustive tests cover the stated small fields only. The automorphism-scheme result does not assert a group-scheme product decomposition, only an underlying coordinate-ring presentation. Equivalent finite-field counts in unindexed literature are not ruled out by literature searches.

## References

1. R. Díaz, A. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197, first posted 2024-08-05; see the introduction, Theorem 3.7, and Example 4.25. https://arxiv.org/abs/2408.02197
2. P. Brumatti and A. Simis, *The module of derivations of a Stanley–Reisner ring*, Proc. Amer. Math. Soc. **123** (1995), 1309–1318. (Background on derivation modules, cited in reference 1.)
