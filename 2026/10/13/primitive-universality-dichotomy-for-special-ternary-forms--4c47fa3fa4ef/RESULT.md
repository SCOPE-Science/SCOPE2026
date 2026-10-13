# Primitive universality dichotomy for special ternary forms

## Finding
For a positive integer \(d\), write
\[
Q_d(a,b,c)=a^2+b^2-dc^2.
\]
A representation \(m=Q_d(a,b,c)\) is called primitive here when
\[
a,b,c\ne0,
\qquad
\gcd(a,b,c)=1.
\]

Let \(d\) be special in the sense of the cited literature. Equivalently,
\[
d=q\quad\text{or}\quad d=2q,
\]
where \(q=1\) or every prime divisor of \(q\) is congruent to \(1\pmod 4\).

Then the primitive value set is exact:
\[
\{Q_d(a,b,c):a,b,c\ne0,\ \gcd(a,b,c)=1\}
=
\begin{cases}
\mathbb Z,& d\text{ odd},\\
\{m\in\mathbb Z:m\not\equiv4\pmod 8\},& d\text{ even}.
\end{cases}
\]
Moreover, every integer in the displayed primitive value set has infinitely many primitive nonzero representations.

Thus a special form is primitively universal precisely in the odd branch. In the even branch, the failure is exactly one residue class modulo \(8\).

## Assumptions and scope
The classification of special parameters used here is the established characterization: \(d\) is special exactly for the displayed \(q\)- or \(2q\)-forms. The proof below refines the representation construction by tracking the common divisor of the three coordinates.

The statement concerns integral triples and all integers \(m\), positive, zero, or negative. The requirement that all three coordinates be nonzero is retained from the definition of a special number.

## Proof
First suppose \(d>1\). The cited sum-of-two-squares characterization gives coprime positive integers \(A,B\) such that
\[
d=A^2+B^2.
\]
If \(d\) is odd, then \(A,B\) have opposite parity; if \(d\) is even, they are both odd.

### Odd special parameters
Assume \(d\) is odd. Choose integers \(u,v\) with
\[
Au+Bv=1.
\]
All solutions are
\[
u_t=u+Bt,
\qquad
v_t=v-At.
\]
Because \(A,B\) have opposite parity, one can choose the parity of \(t\) so that
\[
m-u_t^2-v_t^2
\]
is even. Keeping that parity fixed and varying \(t\) by steps of \(2\), define
\[
c_t=\frac{m-u_t^2-v_t^2}{2},
\qquad
a_t=Ac_t+u_t,
\qquad
b_t=Bc_t+v_t.
\]
Then
\[
Q_d(a_t,b_t,c_t)
=2(Au_t+Bv_t)c_t+u_t^2+v_t^2
=m.
\]
If an integer \(g\) divides \(a_t,b_t,c_t\), then it divides \(u_t\) and \(v_t\), hence it divides
\[
Au_t+Bv_t=1.
\]
Therefore every such representation is primitive.

As \(|t|\to\infty\) along the chosen parity class, \(|c_t|\to\infty\). Each of \(a_t,b_t,c_t\) is a nonzero polynomial in \(t\), so only finitely many parameter values make one coordinate zero. Removing those finitely many values leaves infinitely many primitive nonzero representations of \(m\).

The exceptional parameter \(d=1\) is also primitively universal. Choose any nonzero integer \(v\) of a parity for which
\[
c=\frac{m-1-v^2}{2}
\]
is integral, and set
\[
a=c+1,
\qquad b=v.
\]
Then
\[
a^2+b^2-c^2=m
\]
and \(\gcd(a,c)=1\), so the triple is primitive. Varying \(v\) in the fixed parity class gives infinitely many nonzero triples after excluding finitely many exceptional values.

### Even special parameters: construction
Now suppose \(d\) is even. Write
\[
d=C^2+D^2
\]
with coprime positive odd integers \(C,D\).

If \(m\) is odd, choose
\[
Cu+Dv=1.
\]
Then \(u,v\) have opposite parity, so
\[
c=\frac{m-u^2-v^2}{2}
\]
is integral. Setting
\[
a=Cc+u,
\qquad b=Dc+v
\]
gives \(Q_d(a,b,c)=m\), and any common divisor of \(a,b,c\) divides \(Cu+Dv=1\). Shifting \((u,v)\) through all solutions yields infinitely many nonzero primitive triples.

If
\[
m\equiv2\pmod4,
\]
choose a solution of
\[
Cu+Dv=2
\]
with \(u,v\) both odd. Such a solution exists: doubling a Bezout solution of \(Cr+Ds=1\) gives an even-even solution, and one shift by \((D,-C)\) makes both entries odd. Define
\[
c=\frac{m-u^2-v^2}{4},
\qquad
a=Cc+u,
\qquad b=Dc+v.
\]
Then \(Q_d(a,b,c)=m\). A common divisor divides \(2\), but it cannot be \(2\) because \(u,v\) are odd. Hence the triple is primitive. Shifts by \((2D,-2C)\) preserve the parity and again give infinitely many nonzero primitive triples.

Finally suppose
\[
m\equiv0\pmod8.
\]
Take \(r,s\) with \(Cr+Ds=1\) and put
\[
u=2r,
\qquad v=2s.
\]
Because \(C,D\) are odd, \(r,s\) have opposite parity, so
\[
u^2+v^2\equiv4\pmod8.
\]
Thus
\[
c=\frac{m-u^2-v^2}{4}
\]
is an odd integer. With \(a=Cc+u\) and \(b=Dc+v\), the same identity gives \(Q_d(a,b,c)=m\). Any common divisor divides \(2\), while the oddness of \(c\) excludes \(2\). Hence the triple is primitive. Varying the Bezout solution preserves these facts and yields infinitely many nonzero primitive representations.

These three cases cover every residue class except \(4\pmod8\).

### Even special parameters: the obstruction
For even special \(d\), every odd prime factor is \(1\pmod4\), hence
\[
d\equiv2\pmod8.
\]
Suppose
\[
m\equiv4\pmod8
\]
and \(m=a^2+b^2-dc^2\).

If \(c\) is odd, then
\[
dc^2\equiv2\pmod8,
\]
so
\[
a^2+b^2\equiv6\pmod8,
\]
which is impossible because a sum of two squares modulo \(8\) never equals \(6\).

If \(c\) is even, then
\[
dc^2\equiv0\pmod8,
\qquad
a^2+b^2\equiv4\pmod8.
\]
The latter congruence forces \(a,b\) both even. Thus \(a,b,c\) are all even, contradicting primitivity. Therefore no integer congruent to \(4\pmod8\) is primitively represented.

This completes the exact classification.

## Verification
The accompanying `verify.py` independently implements the constructive formulas for representative special parameters
\[
1,2,5,10,13,17,25,26,34,50
\]
and every integer
\[
-200\le m\le200.
\]
For every admissible pair it checks the defining identity, nonzero coordinates, and \(\gcd(a,b,c)=1\). For even parameters it also exhaustively checks the predicted forbidden residue class in a bounded coordinate box as a regression test.

These finite checks do not prove the infinite theorem. The proof is the symbolic Bezout construction and the modulo-\(8\) obstruction above.

## Relationship to prior work
Lam proved in 2015 that the parameters described above are exactly sufficient for ordinary specialness, using the same basic identities
\[
(Ac+u)^2+(Bc+v)^2-(A^2+B^2)c^2.
\]
Dung and Thang revisited the question in 2021, again proving the ordinary nonzero representation theorem and explicitly constructing the odd and even residue classes. Their Theorem 5 supplies the coprime sum-of-two-squares representation of \(d\).

Neither inspected paper imposes \(\gcd(a,b,c)=1\) in the definition or states the primitive value set. In particular, the published even-parameter construction covers integers congruent to \(4\pmod8\) only with triples that the congruence argument above forces to be imprimitive. Tracking the common divisor through the Bezout identities produces the exact primitive refinement.

Targeted searches for the phrases “primitive representation”, “primitively universal”, the exact form \(a^2+b^2-dc^2\), and the residue obstruction did not locate a source stating this classification. General literature on primitive representations by ternary quadratic forms was also checked; the surfaced results concern genus or positive-definite local theory and do not state this indefinite special-family value set.

## Limitations
The theorem classifies primitive values only for parameters already known to be special. It does not classify primitive value sets for arbitrary positive \(d\).

No formula for the number of primitive representations of bounded height is claimed. The argument proves infinitude but not an asymptotic count.

The main residual originality risk is that a broader classical theorem on primitive representations of indefinite ternary quadratic forms may imply the same family after specialization, although the targeted searches and the two directly relevant full texts inspected here did not expose such a result.

## References
1. Nguyen Viet Dung and Luu Ba Thang, “The Number \(a^2+b^2-dc^2\) Revisited,” Journal of Integer Sequences 24 (2021), Article 21.9.3, published October 1, 2021.
2. Peter Cho-Ho Lam, “Representation of Integers Using \(a^2+b^2-dc^2\),” Journal of Integer Sequences 18 (2015), Article 15.8.6.
3. Andrzej Nowicki, “The Numbers \(a^2+b^2-dc^2\),” Journal of Integer Sequences 18 (2015), Article 15.2.3.
4. A. G. Earnest, J. S. Hsia, and D. C. Hung, “Primitive Representations by Spinor Genera of Ternary Quadratic Forms,” Journal of the London Mathematical Society 50 (1994), 222–230.
