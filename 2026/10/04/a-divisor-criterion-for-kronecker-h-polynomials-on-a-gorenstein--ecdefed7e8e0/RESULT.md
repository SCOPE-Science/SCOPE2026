# A divisor criterion for Kronecker \(h^*\)-polynomials on a Gorenstein canonical boundary
## Finding
For every integer \(r\ge 2\), consider a weighted projective space
\[
X=\mathbb P(1^r,a,b),\qquad 1\le a\le b,
\]
that is Gorenstein, canonical, and non-terminal. Associate to it the weighted-projective simplex
\[
\Delta_X=\Delta_{(1,\mathbf q)},\qquad \mathbf q=(1^{r-1},a,b).
\]
Then \(h^*(\Delta_X;z)\) is a Kronecker polynomial if and only if
\[
(a,b)=(r,r)
\]
or
\[
(a,b)=(c,c+r)\quad\text{with}\quad c\mid r.
\]
Consequently, the Gorenstein canonical non-terminal boundary contains exactly \(\tau(2r)+1\) spaces, and exactly \(\tau(r)+1\) of their associated reflexive simplices have every \(h^*\)-root on the unit circle.

More explicitly, if \(c\mid r\) and \(m=r/c\), then
\[
h^*(\Delta_X;z)=
(1+z^m+\cdots+z^{(c-1)m})(1+z)(1+z+\cdots+z^m).
\]
For the equal-weight member,
\[
h^*(\Delta_X;z)=(1+z+\cdots+z^{r-1})(1+z+z^2).
\]
Both are products of geometric series and hence are Kronecker.

## Assumptions and scope
The statement is over the usual complex weighted projective space with positive integral weights. The notation \(1^r\) means that the weight \(1\) occurs \(r\) times. A monic integral polynomial is called Kronecker when all of its roots lie in the closed unit disk. Here each relevant \(h^*\)-polynomial is monic with constant term \(1\), so being Kronecker is equivalent to all roots lying on the unit circle.

The finding concerns precisely the Gorenstein canonical but non-terminal locus inside this two-heavy-weight family. It does not classify Kronecker \(h^*\)-polynomials for arbitrary weighted projective spaces or arbitrary reflexive simplices.

## Proof
Set \(d=b-a\). In the \(b\)-chart and \(a\)-chart, the Reid--Tai ages for a nonidentity element indexed by \(k\) are respectively
\[
A_b(k)=\frac{rk}b+\left\{\frac{ak}b}\right\},
\qquad
A_a(k)=\frac{rk}a+\left\{\frac{bk}a}\right\}.
\]
For the first chart, \(a=b-d\). If \(b\nmid dk\), then
\[
A_b(k)=1+\frac{rk-(dk\bmod b)}b,
\]
while if \(b\mid dk\), then \(A_b(k)=rk/b\). These expressions show that the \(b\)-chart is canonical for every nonidentity element exactly when \(d\le r\); necessity already follows from \(k=1\). Under \(d\le r\), the \(a\)-chart is canonical exactly when \(a\le r+d\): if \(dk<a\), its age is \((r+d)k/a\), and once \(dk\ge a\), the term \(rk/a\ge dk/a\ge1\). Replacing weak by strict inequalities gives terminality. Hence
\[
X\text{ canonical}\iff d\le r\text{ and }a\le r+d,
\]
\[
X\text{ terminal}\iff d<r\text{ and }a<r+d.
\]
Thus the canonical non-terminal boundary consists of \(d=r\) and \(a=r+d\).

Let \(S=r+a+b\). Gorensteinness is equivalent to \(a\mid S\) and \(b\mid S\). On \(d=r\), write \(a=c\), so \(b=c+r\) and \(S=2(c+r)\). The condition is then exactly \(c\mid2r\). On the other boundary write \(d=c\), so \(a=r+c\), \(b=r+2c\), and \(S=3(r+c)\). The condition \(b\mid S\) is equivalent to \(b\mid3c\). For \(0<c<r\), one has \(b=r+2c>3c\), so this is impossible; \(c=0\) gives \((r,r)\), and \(c=r\) gives \((2r,3r)\), already on the first branch. Therefore the complete Gorenstein canonical non-terminal family is
\[
(r,r),\qquad (c,c+r)\quad(c\mid2r).
\]

For \(\Delta_{(1,\mathbf q)}\), the standard weighted-simplex floor formula gives
\[
h^*(\Delta_X;z)=\sum_{k=0}^{S-1}z^{k-\lfloor ka/S\rfloor-\lfloor kb/S\rfloor}.
\]
Consider first \(a=c\), \(b=c+r\) with \(c\mid r\), and put \(m=r/c\). Directly grouping the summation index modulo \(2(m+1)\) yields
\[
h^*(\Delta_X;z)=
(1+z^m+\cdots+z^{(c-1)m})(1+z)(1+z+\cdots+z^m),
\]
so all roots are roots of unity.

It remains to exclude the divisors of \(2r\) that do not divide \(r\). For such a \(c\), write
\[
c=2p,\qquad t=\frac{2r}c=2m-1.
\]
The same floor sum factors as
\[
h^*(\Delta_X;z)=(1+z^t+\cdots+z^{(p-1)t})C_t(z),
\]
where
\[
C_t(z)=(1+z)(1+z+\cdots+z^t)+2z^m.
\]
Suppose \(|z|=1\) and \(C_t(z)=0\). The points \(z=1\) and \(z=-1\) are not roots. Writing \(z=e^{i\theta}\) and using \(t=2m-1\) gives
\[
z^{-m}C_t(z)=2\left(\cot(\theta/2)\sin(m\theta)+1\right).
\]
Thus a unit-circle root must satisfy
\[
\sin(m\theta)=-\tan(\theta/2),
\]
so \(|\tan(\theta/2)|\le1\), hence \(\operatorname{Re}z\ge0\). If all \(2m\) roots of \(C_t\) were on the unit circle, their real parts would therefore sum to a nonnegative number. But \(C_t\) is monic of degree \(2m\) and its coefficient of \(z^{2m-1}\) is \(2\), so Vieta's formula gives
\[
\sum C_t\text{-roots}=-2,
\]
a contradiction. Hence these and only these divisor-branch members are non-Kronecker.

Finally, the equal-weight member follows directly from the same floor formula:
\[
h^*(\Delta_X;z)=(1+z+\cdots+z^{r-1})(1+z+z^2).
\]
Counting divisors gives \(\tau(2r)+1\) total Gorenstein boundary members and \(\tau(r)+1\) Kronecker members.

## Verification
The accompanying exact-arithmetic checker reconstructs the floor-sum \(h^*\)-polynomial for every divisor-branch member with \(2\le r\le240\). It verifies the two closed factorizations coefficient by coefficient, checks the equal-weight factorization, confirms the divisor counts, and checks the parity reduction \(c\mid2r\), \(c\nmid r\Rightarrow c=2p\) with odd \(t=2r/c\). The infinite exclusion of the odd-\(t\) branch is proved analytically above; no finite root computation is used as a substitute for that argument.

## Relationship to prior work
Kasprzyk's arXiv:1304.3029 develops the canonical and terminal weighted-projective setting and its lattice-simplex correspondence. Braun and Liu's arXiv:1807.00105 studies Kronecker \(h^*\)-polynomials for weighted-projective simplices \(\Delta_{(1,\mathbf q)}\), proves general reflexive factorization machinery, classifies selected two-support families, and explicitly identifies three-support cases as a further direction. The family here has support \(\{1,c,c+r\}\) with multiplicities \((r-1,1,1)\) in the nontrivial cases. The divisor criterion above was not found in the inspected classifications, questions, or published-finding corpus records, and it is not implied by the previously recorded unimodality classification for the same Gorenstein boundary.

## Limitations
The originality check cannot rule out an equivalent statement in literature not surfaced by the searches. Braun--Liu's general factorization framework is broad enough that a specialization could conceivably recover parts of the calculation, although the inspected stated classifications and three-support discussion do not give this divisor criterion. The result is restricted to the Gorenstein canonical non-terminal boundary of \(\mathbb P(1^r,a,b)\), not to all canonical members.

## References
1. A. Kasprzyk, *Classifying terminal weighted projective space*, arXiv:1304.3029, first posted 2013-04-10.
2. B. Braun and F. Liu, *\(h^*\)-Polynomials With Roots on the Unit Circle*, arXiv:1807.00105, first posted 2018-06-30.
3. B. Braun, R. Davis, and L. Solus, *The Integer Decomposition Property for Weighted Projective Spaces*, arXiv:1608.01614, first posted 2016-08-04.
