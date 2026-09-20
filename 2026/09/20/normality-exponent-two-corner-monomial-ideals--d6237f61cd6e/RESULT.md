# Normality of exponent-two corner monomial ideals

Let \(k\) be a field and let \(b,c\ge 2\). Put
\[
I_{b,c}=\overline{(x^2,y^b,z^c)}\subset k[x,y,z].
\]
Thus a monomial \(x^i y^j z^k\) lies in \(I_{b,c}\) exactly when
\[
\frac{i}{2}+\frac{j}{b}+\frac{k}{c}\ge 1.
\]

## Theorem

The ideal \(I_{b,c}\) is non-normal if and only if all three conditions hold:

1. \(b\) and \(c\) are odd;
2. \(\gcd(b,c)=1\);
3. \((bc+1)/2\notin\langle b,c\rangle\), where \(\langle b,c\rangle=\{rb+sc:r,s\in\mathbb N\}\).

Equivalently, \(I_{b,c}\) is normal if and only if at least one of the following holds:

- \(bc\) is even;
- \(\gcd(b,c)>1\);
- \(b,c\) are odd and coprime and \((bc+1)/2\in\langle b,c\rangle\).

For odd coprime \(b,c\), let \(q\in\{1,\dots,b-1\}\) be the unique residue satisfying
\[
2cq\equiv 1\pmod b.
\]
Then the last condition is equivalently
\[
q\le \frac{b-1}{2}.
\]

If \(b,c\) are odd and coprime and \((bc+1)/2\notin\langle b,c\rangle\), then
\[
\frac{bc-1}{2}=cu+bv
\]
for some \(u,v\ge1\), and the monomial
\[
xy^{b-u}z^{c-v}
\]
is an explicit element of \(\overline{I_{b,c}^2}\setminus I_{b,c}^2\).

## Proof

A theorem of Reid--Roberts--Vitulli says that a monomial ideal in three variables is normal once its first two positive powers are integrally closed. Since \(I_{b,c}\) is integrally closed by definition, it is enough to decide when \(I_{b,c}^2\) is integrally closed.

Write
\[
w(i,j,k)=\frac{i}{2}+\frac{j}{b}+\frac{k}{c}.
\]
The Newton-polyhedron description of integral closure gives
\[
x^iy^jz^k\in\overline{I_{b,c}^2}
\quad\Longleftrightarrow\quad
w(i,j,k)\ge2.
\tag{1}
\]

Take a monomial satisfying (1).

If \(i\ge2\), then subtracting the exponent vector \((2,0,0)\) leaves weight at least \(1\), so the monomial lies in \(I_{b,c}^2\).

If \(i=0\), the problem is two-dimensional: with
\[
J=\overline{(y^b,z^c)}\subset k[y,z],
\]
we have \(y^jz^k\in\overline{J^2}\). Integrally closed monomial ideals in two variables are normal, hence \(y^jz^k\in J^2\subset I_{b,c}^2\).

It remains to consider \(i=1\). If \(j\ge b\), subtracting \((0,b,0)\) leaves weight at least \(1\); likewise if \(k\ge c\). Thus any obstruction has
\[
0\le j<b,\qquad 0\le k<c.
\]
Set
\[
u=b-j\ge1,\qquad v=c-k\ge1.
\]
Then (1) is equivalent to
\[
cu+bv\le \frac{bc}{2}.
\tag{2}
\]

We now characterize membership in \(I_{b,c}^2\). Because the total \(x\)-exponent is \(1\), one factor has \(x\)-exponent \(1\) and the other has \(x\)-exponent \(0\). Write the first factor as \(xy^rz^s\). The two factors belong to \(I_{b,c}\) exactly when
\[
cr+bs\ge \frac{bc}{2}
\]
and
\[
c(j-r)+b(k-s)\ge bc.
\]
The second inequality is
\[
cr+bs\le bc-cu-bv.
\]
Moreover these inequalities automatically force \(r\le j\) and \(s\le k\). Therefore
\[
xy^jz^k\in I_{b,c}^2
\]
if and only if the numerical semigroup \(S=\langle b,c\rangle\) meets the interval
\[
\left[\frac{bc}{2},\ bc-cu-bv\right].
\tag{3}
\]
Consequently \(I_{b,c}\) is normal if and only if (3) is nonempty for every positive \(u,v\) satisfying (2).

### Case 1: \(bc\) is even

If \(b\) is even, then
\[
\frac{bc}{2}=c\frac b2\in S;
\]
if \(c\) is even, the analogous representation holds. Thus the left endpoint of every interval (3) belongs to \(S\), so \(I_{b,c}\) is normal.

### Case 2: \(b,c\) are odd and \(d=\gcd(b,c)>1\)

Write \(b=dB\), \(c=dC\) with \((B,C)=1\). Set
\[
M=\frac{bc+d}{2}=d\frac{dBC+1}{2}.
\]
Since \(d\ge3\),
\[
\frac{dBC+1}{2}>BC-B-C,
\]
which is the Frobenius number of \(\langle B,C\rangle\). Hence
\[
M\in\langle b,c\rangle=S.
\tag{4}
\]
Every quantity \(cu+bv\) is a multiple of \(d\). Because \(bc/d=dBC\) is odd, (2) implies
\[
cu+bv\le \frac{bc-d}{2}.
\]
Therefore
\[
bc-cu-bv\ge \frac{bc+d}{2}=M.
\]
Together with (4), this places \(M\) in every interval (3), so \(I_{b,c}\) is normal.

### Case 3: \(b,c\) are odd and coprime

Put
\[
T=\frac{bc+1}{2},\qquad H=\frac{bc-1}{2}.
\]
Exactly one of \(T,H\) belongs to \(S\). Indeed, let \(q\in\{1,\dots,b-1\}\) satisfy
\[
2cq\equiv1\pmod b.
\]
For an integer below \(bc\), the coefficient of \(c\) in an \(S\)-representation is uniquely determined modulo \(b\). Thus
\[
T\in S
\iff cq\le T
\iff q\le\frac{b-1}{2}.
\tag{5}
\]
The corresponding coefficient for \(H\) is \(b-q\), so
\[
H\in S
\iff b-q\le\frac{b-1}{2}
\iff q\ge\frac{b+1}{2}.
\tag{6}
\]
Hence precisely one of \(T,H\) lies in \(S\).

If \(T\in S\), then every integer \(cu+bv\le bc/2\) is at most \(H\), and therefore
\[
bc-cu-bv\ge T.
\]
So \(T\) lies in every interval (3), proving normality.

If \(T\notin S\), then \(H\in S\). Write
\[
H=cu+bv.
\]
The representation may be chosen with \(u,v\ge1\): neither coefficient can vanish, since \(H\) is divisible by neither \(b\) nor \(c\). For this pair, the interval (3) is
\[
\left[\frac{bc}{2},T\right].
\]
Because \(bc\) is odd, its only integer is \(T\), which is not in \(S\). Hence the associated monomial
\[
xy^{b-u}z^{c-v}
\]
belongs to \(\overline{I_{b,c}^2}\) but not to \(I_{b,c}^2\). Thus \(I_{b,c}\) is not normal.

This proves the theorem. \(\square\)

## Relation to earlier criteria

For pairwise coprime \((2,b,c)\), Reid--Roberts--Vitulli prove that normality implies the numerical-semigroup condition
\[
L+1\in\langle \omega_1,\omega_2,\omega_3\rangle,
\]
where \(L=\operatorname{lcm}(2,b,c)=2bc\) and \((\omega_1,\omega_2,\omega_3)=(bc,2c,2b)\). Since \(2bc+1\) is odd and is less than \(3bc\), this condition is exactly
\[
\frac{bc+1}{2}\in\langle b,c\rangle.
\]
The theorem above shows that in the exponent-two slice this previously necessary condition is also sufficient.

The published open Problem 41 of Cahen--Fontana--Frisch--Glaz asks for a classification of all triples \((a,b,c)\) for which \(\overline{(x^a,y^b,z^c)}\) is normal. Reid--Roberts--Vitulli already give \((2,3,7)\) as a non-normal example. Coughlin's 2004 thesis treats, among other cases, the consecutive family \((j,j+1,j+2)\), and later work gives broader sufficient conditions and transfer principles. Ataka--Matsuoka (2026) prove that every integrally closed height-three monomial ideal in \(k[x,y,z]\) with at most seven minimal generators is normal, with the bound sharp via the exponent permutation \((7,3,2)\). The present result instead gives a closed arithmetic classification for every pair \((b,c)\) in the entire slice with first exponent \(2\).

## Reproducibility

The file `artifacts/verify.py` independently enumerates the finite obstruction criterion (3) and compares it with the theorem for \(2\le b\le100\) and \(2\le c\le150\). It reports zero mismatches.

## Limitations and originality

This is a partial classification of Problem 41, not a classification of arbitrary \((a,b,c)\). The argument exploits the fact that the first exponent is exactly \(2\), which reduces every possible obstruction in the second power to a single midpoint interval in the two-generator numerical semigroup \(\langle b,c\rangle\).

Originality is asserted only to the best of our knowledge. Targeted searches of the Reid--Roberts--Vitulli line of work, Coughlin-related citations, later Newton-polyhedron criteria, and 2026 monomial-normality literature did not locate this exponent-two classification or the midpoint criterion above. The full text of Heather Coughlin's 2004 dissertation was not inspected; accessible citations identify its principal three-variable theorem as the consecutive family \((j,j+1,j+2)\). A differently phrased or unindexed specialization of a general criterion could therefore still exist.

## References

1. L. Reid, L. G. Roberts, M. A. Vitulli, “Some Results on Normal Homogeneous Ideals,” *Communications in Algebra* 31 (2003), 4485–4506. https://arxiv.org/abs/math/0209285
2. S. Cahen, M. Fontana, S. Frisch, S. Glaz (eds.), *Open Problems in Commutative Ring Theory*, Springer (2014), Problem 41. https://www2.math.uconn.edu/~glaz/Publications_Selected%20Articles/OpenProblemsInCommutativeRingTheory.Springer14.pdf
3. H. Coughlin, *Classes of Normal Monomial Ideals*, Ph.D. thesis, University of Oregon (2004).
4. I. Al-Ayyoub, “On the Normality of a Class of Monomial Ideals via the Newton Polyhedron,” *Mediterranean Journal of Mathematics* 16 (2019), Article 77. https://doi.org/10.1007/s00009-019-1337-7
5. M. Ataka, N. Matsuoka, “Normality of monomial ideals in three variables,” arXiv:2602.01782 (2026). https://arxiv.org/abs/2602.01782
