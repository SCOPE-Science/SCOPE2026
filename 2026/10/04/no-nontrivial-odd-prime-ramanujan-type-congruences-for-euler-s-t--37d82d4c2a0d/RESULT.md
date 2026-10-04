# No nontrivial odd-prime Ramanujan-type congruences for Euler's totient

## Finding
Let \(p\) be an odd prime, and let \(A,B\) be coprime positive integers. Then there exists an integer \(n\ge0\) such that
\[
p\nmid\varphi(An+B).
\]
Thus there are no coprime \(A,B\) for which
\[
\varphi(An+B)\equiv0\pmod p
\]
holds for every \(n\ge0\).

The witness can be chosen with at most two prime factors. If either \(p\nmid A\), or \(p\mid A\) but \(B\not\equiv1\pmod p\), then one can choose \(An+B\) itself to be prime. In the only remaining case,
\[
p\mid A,\qquad B\equiv1\pmod p,
\]
no prime can be a witness, but one can choose
\[
An+B=qr
\]
with \(q\) and \(r\) distinct primes satisfying
\[
q\not\equiv1\pmod p,\qquad r\not\equiv1\pmod p.
\]

This proves Conjecture 2 of Craig and Merca.

## Assumptions and scope
Euler's totient function is denoted by \(\varphi\). The variables \(A,B\) are positive and satisfy \(\gcd(A,B)=1\); \(p\) is an odd prime. The conclusion is existential and unconditional, using Dirichlet's theorem on primes in reduced arithmetic progressions.

The theorem concerns congruences modulo an odd prime. It does not claim the analogous statement for arbitrary composite moduli, and the restriction to coprime \(A,B\) is exactly the setting of the conjecture being resolved.

## Proof
We first record the elementary criterion
\[
p\mid\varphi(m)
\]
if and only if either
\[
p^2\mid m
\]
or some prime divisor \(q\mid m\) satisfies
\[
q\equiv1\pmod p.
\]
Indeed, if
\[
m=\prod_q q^{e_q},
\]
then
\[
\varphi(m)=\prod_q q^{e_q-1}(q-1),
\]
so a factor \(p\) can arise only from a repeated prime factor \(q=p\), or from one of the factors \(q-1\).

We now construct a witness in three cases.

Suppose first that
\[
p\nmid A.
\]
Choose any residue
\[
u\in\{2,3,\ldots,p-1\}.
\]
By the Chinese remainder theorem there is a residue class \(c\) modulo \(Ap\) satisfying
\[
c\equiv B\pmod A,
\qquad
c\equiv u\pmod p.
\]
Because \(\gcd(A,B)=1\) and \(u\not\equiv0\pmod p\), one has
\[
\gcd(c,Ap)=1.
\]
Dirichlet's theorem therefore supplies infinitely many primes \(q\equiv c\pmod{Ap}\). Choose one with \(q\ge B\), and set
\[
n=\frac{q-B}{A}.
\]
Then \(n\ge0\), \(q=An+B\), and
\[
q\equiv u\not\equiv1\pmod p.
\]
Hence
\[
p\nmid\varphi(q)=q-1.
\]

Next suppose that
\[
p\mid A,
\qquad
B\not\equiv1\pmod p.
\]
Since \(\gcd(A,B)=1\), also \(B\not\equiv0\pmod p\). Dirichlet's theorem gives infinitely many primes
\[
q\equiv B\pmod A.
\]
Every such prime satisfies
\[
q\equiv B\not\equiv0,1\pmod p.
\]
Taking \(q\ge B\) and again setting \(n=(q-B)/A\) gives a prime witness.

It remains to treat the exceptional residue situation
\[
p\mid A,
\qquad
B\equiv1\pmod p.
\]
Write
\[
A=p^eC,
\qquad
\gcd(C,p)=1,
\qquad
e\ge1.
\]
Choose
\[
u\in\{2,3,\ldots,p-1\}.
\]
By the Chinese remainder theorem choose a unit \(c\) modulo \(A\) satisfying
\[
c\equiv u\pmod{p^e},
\qquad
c\equiv1\pmod C.
\]
Define another unit class \(d\) modulo \(A\) by
\[
d\equiv Bc^{-1}\pmod A.
\]
Then
\[
cd\equiv B\pmod A.
\]
Modulo \(p\), the two classes satisfy
\[
c\equiv u\not\equiv1\pmod p,
\qquad
d\equiv u^{-1}\not\equiv1\pmod p.
\]
Dirichlet's theorem gives infinitely many primes in each of the reduced residue classes \(c\) and \(d\) modulo \(A\). Choose distinct primes \(q\equiv c\pmod A\) and \(r\equiv d\pmod A\), both large enough that \(qr\ge B\). Then
\[
qr\equiv B\pmod A,
\]
so
\[
qr=An+B
\]
for some \(n\ge0\). Moreover neither \(q\) nor \(r\) is congruent to \(1\) modulo \(p\), and neither equals \(p\). Therefore
\[
p\nmid(q-1)(r-1)=\varphi(qr).
\]
This proves the theorem.

Finally, in this exceptional residue situation every prime \(q\equiv B\pmod A\) satisfies \(q\equiv1\pmod p\), so every prime value has \(p\mid\varphi(q)\). Thus the passage from a prime witness to a two-prime witness is genuinely necessary for this construction and exactly isolates the case left open by the prime-progression argument.

## Verification
The accompanying `verify.py` independently implements the three constructions for a finite regression family. It checks every odd prime \(p\le19\) and every coprime pair \(1\le A,B\le35\).

For the first two cases it searches an appropriate reduced residue class and confirms a prime witness. In the exceptional case it constructs the two unit residue classes, finds distinct prime representatives, and confirms a squarefree semiprime witness. Every output is checked to satisfy
\[
An+B=m
\]
and
\[
p\nmid\varphi(m).
\]

The finite computation is only regression evidence. The theorem for all \(p,A,B\) is the symbolic Dirichlet-and-CRT proof above.

## Relationship to prior work
Craig and Merca introduced Ramanujan-type congruences for multiplicative functions and treated Euler's totient function in Section 3.2. Their Proposition 3.5 gives the prime-progression obstruction when the progression residue is not \(1\) modulo the congruence prime. Immediately afterward they state Conjecture 2: for an odd prime \(p\), there should be no coprime \(A,B\) such that
\[
\varphi(An+B)\equiv0\pmod p
\]
for every \(n\ge0\).

The proof above completes the missing residue case \(p\mid A\) and \(B\equiv1\pmod p\) by replacing a prime witness with a product of two primes in complementary reduced residue classes. It also gives the sharper witness-size statement: one prime factor suffices outside the exceptional residue case, while two suffice in it.

Targeted searches for the exact conjecture, its coprime-progression formulation, the equivalent totient divisibility statement, and a later resolution did not locate a published proof. The canonical OEIS entry A000010 records Euler's totient and its prime-power formula but does not state this progression theorem.

## Limitations
The argument uses Dirichlet's theorem and is ineffective in the sense that it gives no explicit uniform bound for the least witness \(n\). Quantitative least-prime estimates could turn the existence proof into explicit bounds.

The theorem is for prime moduli. Composite-modulus analogues require simultaneous local conditions and are not settled here.

A later or unindexed source may contain an equivalent elementary resolution; the literature searches reduce but do not eliminate that residual originality risk.

## References
1. William Craig and Mircea Merca, “On Ramanujan-type Congruences for Multiplicative Functions,” arXiv:2112.05649v1, first public 10 December 2021; journal version, Results in Mathematics 77 (2022), DOI 10.1007/s13398-022-01272-y.
2. OEIS A000010, Euler totient function.
3. P. G. L. Dirichlet, theorem on primes in reduced arithmetic progressions.
