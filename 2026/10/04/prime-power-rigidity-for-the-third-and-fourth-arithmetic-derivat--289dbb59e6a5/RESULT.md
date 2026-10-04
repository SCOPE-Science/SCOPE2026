# Prime-power rigidity for the third and fourth arithmetic-derivative iterates

## Finding
Let \(D\) be the arithmetic derivative on the positive integers:
\[
D(p)=1
\]
for every prime \(p\), and
\[
D(ab)=D(a)b+aD(b).
\]
For every prime \(p\), every integer \(e\ge1\), and each
\[
r\in\{3,4\},
\]
one has
\[
D^r(p^e)=p^e
\]
if and only if
\[
e=p.
\]
Hence the only prime-power solutions of either \(D^3(n)=n\) or \(D^4(n)=n\) are the fixed points \(n=p^p\). In particular, no nontrivial cycle of exact period \(3\) or \(4\) contains a prime power.

## Assumptions and scope
The domain is the positive integers. A prime power is \(p^e\) with \(p\) prime and \(e\ge1\). The notation \(D^r\) means functional iteration.

The theorem does not classify arbitrary solutions of \(D^3(n)=n\) or \(D^4(n)=n\), and it does not settle the general conjecture that the only periodic points are the fixed points \(p^p\).

## Proof
For every positive integer \(n\),
\[
D(n)=n\sum_{q\mid n}\frac{\nu_q(n)}q.
\]
Thus
\[
D(n)\le\frac{n\Omega(n)}2\le\frac{n\log_2n}{2},
\]
because \(n\ge2^{\Omega(n)}\).

Suppose first that \(1\le e<p\). Whenever
\[
x=p^a u,\qquad p\nmid u,\qquad 1\le a<p,
\]
the Leibniz rule gives
\[
D(x)=p^{a-1}\bigl(au+pD(u)\bigr).
\]
The parenthesized factor is nonzero modulo \(p\), so
\[
\nu_p(D(x))=a-1.
\]
Starting from \(p^e\), induction yields
\[
\nu_p\!\left(D^j(p^e)\right)=e-j
\]
for \(0\le j\le e\). Hence if \(e<p\) and \(D^r(p^e)=p^e\), then \(e<r\).

If \(e>p\), write \(p^e=p^p m\) with \(m>1\). For every \(u>1\),
\[
D(p^p u)=p^p\bigl(u+D(u)\bigr)>p^p u.
\]
The next iterate again has the form \(p^p v\) with \(v>1\), so all later iterates increase strictly. Therefore \(p^e\) cannot be periodic. If \(e=p\), then \(D(p^p)=p^p\), so this case works for every iterate.

For \(r=3\), valuation descent leaves only \(e=1,2\). The case \(e=1\) follows the orbit
\[
p\mapsto1\mapsto0\mapsto0.
\]
For \(e=2\), necessarily \(p\ge3\), and
\[
D(p^2)=2p,\qquad D^2(p^2)=p+2.
\]
Set \(N=p+2\). Since \(2^p>p+2\) for \(p\ge3\),
\[
\log_2N<p.
\]
Therefore
\[
D^3(p^2)=D(N)\le\frac{N\log_2N}{2}
<\frac{(p+2)p}{2}<p^2.
\]
Thus no \(e<p\) works for the third iterate.

For \(r=4\), valuation descent leaves only \(e=1,2,3\). Again \(e=1\) reaches \(0\).

Take \(e=2\). Put \(N=p+2\) and \(a=D(N)\). The finitely many primes \(p<64\) are checked exactly by the accompanying program. For \(p\ge64\), let
\[
m=\lfloor\log_2p\rfloor\ge6.
\]
Since \(N<2p\),
\[
\log_2N<m+2,\qquad a<p(m+2).
\]
Also \(\log_2a<2(m+1)\), so
\[
D^4(p^2)=D(a)<p(m+2)(m+1).
\]
For every integer \(m\ge6\),
\[
(m+1)(m+2)<2^m.
\]
The base case is \(56<64\), and induction follows because the ratio of consecutive left sides is less than \(2\). Since \(2^m\le p\), we obtain \(D^4(p^2)<p^2\).

Now take \(e=3\). The case \(p=3\) is already the fixed case, so under \(e<p\) one has \(p\ge5\). The finitely many primes \(p<128\) are checked exactly by the accompanying program. For \(p\ge128\), let
\[
m=\lfloor\log_2p\rfloor\ge7,\qquad N=p+6,\qquad a=D(N).
\]
Directly,
\[
D(p^3)=3p^2,\qquad D^2(p^3)=p^2+6p=pN,
\]
and hence
\[
D^3(p^3)=N+pa.
\]
Since \(N<2p\) and \(\log_2N<m+2\),
\[
a<p(m+2)
\]
and therefore
\[
D^3(p^3)<p^2(m+3).
\]
Moreover
\[
\log_2\!\left(D^3(p^3)\right)<3(m+1),
\]
so
\[
D^4(p^3)<\frac32p^2(m+1)(m+3).
\]
For every integer \(m\ge7\),
\[
\frac32(m+1)(m+3)<2^m.
\]
The base case is \(120<128\), and the same ratio argument gives induction. Since \(2^m\le p\),
\[
D^4(p^3)<p^3.
\]

This exhausts all possibilities.

## Verification
The accompanying `verify.py` independently implements integer factorization and the arithmetic derivative using only the Python standard library.

It exhausts the only finite ranges left by the proof:
\[
e=2,\quad p<64,
\]
and
\[
e=3,\quad p<128
\]
for the fourth iterate. It also performs regression checks of both claimed classifications for all primes \(p<500\) and all exponents \(1\le e\le12\).

The wider finite scan is only a regression test. The infinite large-prime cases are proved symbolically above.

## Relationship to prior work
Emmons and Xiao restate the Ufnarovski--Åhlander conjecture that an arithmetic-derivative orbit should eventually reach \(0\), reach a fixed point \(p^p\), or diverge; in particular, eventual periodicity should have period \(1\). Their 2023 paper is the literature anchor here and has primary MSC \(11A25\).

Ufnarovski and Åhlander proved that the fixed points are exactly \(p^p\) and analyzed hypothetical period-\(2\) cycles, forcing both terms to be squarefree. Kovič later gave further constraints for \(D^2(n)=n\) and an abstract framework for homogeneous higher-order arithmetic differential equations.

The present theorem moves to the next two iterates and completely closes the prime-power branch for \(D^3(n)=n\) and \(D^4(n)=n\).

OEIS A099306 records the third arithmetic derivative and notes the forward fact that \(p^p\) is fixed under it. OEIS A258644 records the fourth arithmetic derivative. Neither inspected entry states the converse prime-power classification.

Targeted semantic searches, exact-phrase searches, and full-text comparisons did not locate a statement implying this theorem.

## Limitations
The theorem does not rule out non-prime-power cycles of period \(3\) or \(4\). It does not automatically extend to all iterate orders, because larger allowed exponents create more complicated intermediate factorizations.

The finite replay covers only the small ranges isolated explicitly in the proof. Those ranges are exhaustive, but they are not substitutes for the symbolic large-prime argument.

An equivalent elementary proof may exist in an unindexed source.

## References
1. Brad Emmons and Xiao Xiao, “A Generalization of Arithmetic Derivative to \(p\)-adic Fields and Number Fields,” arXiv:2307.04912v1, first public 10 July 2023, primary MSC \(11A25\).
2. Victor Ufnarovski and Bo Åhlander, “How to Differentiate a Number,” Journal of Integer Sequences 6 (2003), Article 03.3.4.
3. Jurij Kovič, “The Arithmetic Derivative and Antiderivative,” Journal of Integer Sequences 15 (2012), Article 12.3.8.
4. OEIS A099306, third arithmetic derivative.
5. OEIS A258644, fourth arithmetic derivative.
