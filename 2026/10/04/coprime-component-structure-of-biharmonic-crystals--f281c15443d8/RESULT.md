# Coprime component structure of biharmonic crystals
## Finding
Let \(N=ab\) be an odd crystal with \(a,b>1\), where
\[
B_{\mathrm{pair}}(a,b)=\frac{(a+b)^2+(ab+1)^2}{2(a+1)(b+1)}\in\mathbb N.
\]
Then
\[
\gcd(a,b)=1
\qquad\text{and}\qquad
\gcd(a+1,b+1)=2.
\]
Thus every crystal factorization \(N=ab\) is a unitary factorization. As a consequence, if
\(\omega(N)=2\), the unordered pair of crystal components is unique. Therefore any
counterexample to the component-uniqueness conjecture stated by Abrate, Barbero,
Cerruti and Murru must satisfy \(\omega(N)\ge 3\).

## Assumptions and scope
A crystal is used exactly in the sense of the cited biharmonic-mean paper: \(N\) is
odd, \(N=ab\) with \(a,b>1\), and \(B_{\mathrm{pair}}(a,b)\) is integral. Since
\(N\) is odd, both components are odd. The result concerns crystal component pairs,
not all biharmonic divisor numbers.

Write
\[
Q(a,b)=\frac{(a+b)^2}{(a+1)(b+1)}.
\]
Proposition 1 of the source proves, for odd \(a,b\), that integrality of
\(B_{\mathrm{pair}}(a,b)\) is equivalent to integrality of \(Q(a,b)\).
For a crystal put \(w=Q(a,b)\in\mathbb N\), and set
\[
x=\frac{a+1}2,\qquad y=\frac{b+1}2.
\]
Then
\[
(x+y-1)^2=wxy.
\]

## Proof
First, \(\gcd(x,y)=1\). Indeed, if \(g\) divides both \(x\) and \(y\), reducing
\((x+y-1)^2=wxy\) modulo \(g\) gives \(1\equiv0\pmod g\). Hence
\[
\gcd(a+1,b+1)=2\gcd(x,y)=2.
\]

It remains to prove \(\gcd(a,b)=1\). The source's Theorem 4 classifies the positive
integer solutions of
\[
(x+y-1)^2=wxy
\]
as consecutive terms \(x=u_n(w)\), \(y=u_{n-1}(w)\), where
\[
u_0=0,\qquad u_1=1,\qquad
u_{k+1}=(w-2)u_k-u_{k-1}+2.
\]
Because \(a,b>1\), the relevant index satisfies \(n\ge3\).

Let \(d=\gcd(a,b)\). Since \(a,b\) are odd, \(d\) is odd. If \(d>1\), let \(h\)
be the inverse of \(2\) modulo \(d\). From \(a=2x-1\) and \(b=2y-1\),
\[
x\equiv y\equiv h\pmod d.
\]
The conic equation then gives \(w\equiv0\pmod d\), because its left side is
\(0\) modulo \(d\) while \(xy\equiv h^2\) is a unit.

Now use the recurrence backwards. If two consecutive terms satisfy
\(u_j\equiv u_{j-1}\equiv h\pmod d\), then
\[
u_{j-2}
=(w-2)u_{j-1}+2-u_j
\equiv 2-3h
\equiv h\pmod d,
\]
where the final congruence uses \(2h\equiv1\pmod d\). Starting from
\(u_n\equiv u_{n-1}\equiv h\), induction reaches \(u_1\equiv h\pmod d\).
But \(u_1=1\), so \(h\equiv1\pmod d\). Together with \(2h\equiv1\pmod d\),
this yields \(2\equiv1\pmod d\), impossible for \(d>1\). Therefore
\[
\gcd(a,b)=1.
\]

Finally, if \(\omega(N)=2\), write \(N=p^\alpha q^\beta\) with distinct odd
primes \(p,q\) and positive \(lpha,eta\). A nontrivial factorization
\(N=ab\) with \(\gcd(a,b)=1\) must, up to order, be
\[
(a,b)=(p^\alpha,q^\beta).
\]
Hence a crystal with two distinct prime divisors has unique components.

## Verification
The proof is symbolic and uses only Proposition 1 and Theorem 4 of the cited source.
The accompanying checker independently performs two finite sanity checks: it generates
recurrence solutions for many parameters and verifies both gcd conclusions, and it
exhaustively scans odd component pairs in a bounded box for integral \(Q(a,b)\) and
checks the same conclusions. These finite checks corroborate, but do not replace, the
unrestricted proof.

## Relationship to prior work
Abrate, Barbero, Cerruti and Murru introduce crystals, prove the equivalence between
integrality of \(B_{\mathrm{pair}}\) and \(Q\), classify all crystal pairs by the
recurrence above, and conjecture uniqueness of the component pair. Their full text
does not state either coprimality conclusion; searches within it for "gcd" and
"coprime" return no occurrence. The result here extracts a structural invariant from
their conic/recurrence classification and proves their uniqueness conjecture for the
entire two-prime-support stratum.

OEIS A210494 records biharmonic divisor numbers and the closed formula for their
divisor mean, but it is a table of integers rather than crystal factorizations and
does not contain the component coprimality or two-prime-support uniqueness statement.

## Limitations
This does not prove the full component-uniqueness conjecture. For
\(\omega(N)\ge3\), an integer has several possible nontrivial unitary splits, and the
argument above does not compare the crystal condition across those different splits.
The literature search found no equivalent statement, but absence from indexed search
results is not a proof that no unindexed source contains the same lemma.

## References
1. M. Abrate, S. Barbero, U. Cerruti and N. Murru, "The Biharmonic mean",
   arXiv:1601.03081v1, 12 January 2016; *Mathematical Reports* 18(68), no. 4
   (2016), 483--495. AMS Subject Classification: 11N80, 26E60.
2. OEIS Foundation, A210494, "Biharmonic numbers".
