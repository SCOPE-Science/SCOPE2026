# Dyadic-exponent rigidity for equality of unitary and exponential divisor sums

## Finding
For distinct rational primes \(p,q\) and every integer \(t\ge1\),
\[
\sigma^*(p^{2^t}q)=\sigma^{(e)}(p^{2^t}q)
\quad\Longleftrightarrow\quad
(t,p,q)\in\{(1,2,5),(1,3,5)\}.
\]
Here \(\sigma^*\) is the sum of unitary divisors, and \(\sigma^{(e)}\) is the sum of exponential divisors. Thus no equality occurs when the exponent on one of the two prime factors is a power of two at least \(4\).

A stronger integer-polynomial statement drives the result. For every integer \(b\ge2\) and integer \(t\ge2\), let
\[
D_t(b)=\sum_{j=0}^{t-1}b^{2^j}-1.
\]
Then \(D_t(b)\) never divides \(b^{2^t}+1\). The conclusion is uniform in both the base and the exponent.

## Assumptions and scope
A positive divisor \(d\mid n\) is unitary if \(\gcd(d,n/d)=1\). An exponential divisor of \(n=\prod_i p_i^{a_i}\) is \(\prod_i p_i^{e_i}\) where \(e_i\mid a_i\) for each \(i\). Both sums are multiplicative, with
\[
\sigma^*(p^a)=1+p^a,\qquad
\sigma^{(e)}(p^a)=\sum_{d\mid a}p^d.
\]
All numbers and exponents here are positive. The main equality statement requires two *distinct* primes and the exponent \(2^t\) with \(t\ge1\). The auxiliary divisibility theorem requires only an integer base \(b\ge2\).

## Proof
Fix \(t\ge1\), an integer \(b\ge2\), and abbreviate \(D=D_t(b)\). Since the positive divisors of \(2^t\) are \(1,2,4,\ldots,2^t\), multiplicativity implies, for distinct primes \(p,q\),
\[
\begin{aligned}
\sigma^*(p^{2^t}q)&=(p^{2^t}+1)(q+1),\\
\sigma^{(e)}(p^{2^t}q)&=q\bigl(p^{2^t}+D_t(p)+1\bigr).
\end{aligned}
\]
Equality is therefore equivalent to the **exact integer equation**
\[
p^{2^t}+1=qD_t(p). \tag{1}
\]

**The initial exponent.** When \(t=1\), \(D_1(b)=b-1\). Divisibility in (1) forces
\[
b-1\mid b^2+1\quad\Longleftrightarrow\quad b-1\mid2.
\]
For prime \(b=p\), the only possibilities are \(p=2\) and \(p=3\), and in each case (1) gives \(q=5\). Substitution yields \(\sigma^*(20)=\sigma^{(e)}(20)=30\) and \(\sigma^*(45)=\sigma^{(e)}(45)=60\).

**The exponent \(4\).** When \(t=2\), \(D=b^2+b-1\), hence \(b^2\equiv -(b-1)\pmod D\) and
\[
b^4+1\equiv (b-1)^2+1=:R\pmod D.
\]
For every \(b\ge2\), \(R\ge2\) and
\[
D-R=3(b-1)>0.
\]
Thus \(0<R<D\) and \(D\nmid b^4+1\).

**All larger dyadic exponents.** Suppose \(t\ge3\) and put
\[
y=b^{2^{t-2}},\qquad u=\sum_{j=0}^{t-3}b^{2^j}-1.
\]
Then \(D=y^2+y+u\), \(y\ge4\), and
\[
1\le u\le\frac{y}{3}. \tag{2}
\]
Indeed, for \(t=3\), \(u=b-1\le b^2/3=y/3\) (because \(b^2-3b+3>0\)). If (2) holds at \(t\) with variables \(y,u\), at \(t+1\) the variables become \(y'=y^2\), \(u'=u+y\). Then \(u'\le4y/3\le y^2/3=y'/3\) because \(y\ge4\). The lower bound follows from \(b\ge2\).

Now \(y^2\equiv -(y+u)\pmod D\), so
\[
y^4+1\equiv R:=(y+u)^2+1\pmod D.
\]
This representative satisfies
\[
R-D=(2u-1)y+u^2-u+1>0
\]
and, from \(y\ge4\) and (2),
\[
R\le\frac{16y^2}{9}+1<2y^2<2D.
\]
Consequently \(D<R<2D\); the remainder of \(R\) on division by \(D\) equals \(R-D\), strictly between \(0\) and \(D\). In particular \(D\nmid y^4+1=b^{2^t}+1\).

Together the cases establish the integer-base divisibility obstruction for every \(t\ge2\). Equation (1) then gives the stated two-prime classification for all \(t\ge1\). \(\square\)

## Verification
The supplied standalone `verify.py` checks both divisor sums directly for the permitted finite test parameters; independently tests the integer-base denominator divisibility; and checks the two distinct remainder intervals for every tested exponent. It also tests the induction bound on \(u\). Run:

`python verify.py`

The finite tests are supplementary. The full infinite-range result follows from the exact inequalities in the proof, not from extrapolation of the test range.

## Relationship to prior work
Trudgian introduced the comparison between the unitary and exponential divisor sums in his 2013 preprint, listed equality examples, and asked whether the equality holds for infinitely many integers. His paper does not classify all dyadic exponents in the two-prime family.

The published result *The first 49 exponent layers of the unitary–exponential divisor-sum equality* completely classifies \(\sigma^*(p^a q)=\sigma^{(e)}(p^a q)\) for \(2\le a\le49\), including every dyadic exponent \(a\in\{2,4,8,16,32\}\). **Those small-exponent cases are prior coverage, not claimed as new.** Its finite theorem makes no claim for \(a\ge50\), whereas the present uniform remainder argument proves nonexistence for **all** dyadic exponents \(a=2^t\) with \(t\ge6\), infinitely many exponents beyond its bound. This unbounded implication does not follow from the published finite cutoff. OEIS A236474 records equality values but does not determine the infinite dyadic-exponent family.

## Limitations
The classification is limited to numbers with precisely two distinct prime factors, one occurring to an exponent of the form \(2^t\) and the other to exponent \(1\). It neither excludes equality at other exponent patterns nor resolves Trudgian's global infinitude question. The result is an exact self-contained arithmetic statement, but unlocated prior work may independently imply it; published finite-exponent classifications must be credited as overlapping for the initial dyadic cases.

## References
1. Tim Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615, publicly submitted 2013-12-17; section 4 poses the global equality question. https://arxiv.org/html/1312.4615v3
2. *The first 49 exponent layers of the unitary–exponential divisor-sum equality*, published research record, 2026-10-04. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-first-49-exponent-layers-of-the-unitary-exponential-divisor--59314f8e910e
3. OEIS A236474, *Numbers whose sum of unitary divisors is equal to the sum of exponential divisors*. https://oeis.org/A236474
