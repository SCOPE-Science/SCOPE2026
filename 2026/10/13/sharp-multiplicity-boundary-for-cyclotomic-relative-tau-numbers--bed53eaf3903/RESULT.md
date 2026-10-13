# Sharp multiplicity boundary for cyclotomic relative \(\tau\)-numbers

## Finding
Let \(p\) be a prime and \(k\ge1\). A positive integer \(n\) is a \(\tau\)-number relative to \(\Phi_{p^k}\) when
\[
\tau(n)\mid\Phi_{p^k}(n),
\]
where \(\tau(n)\) is the divisor-counting function and \(\Omega(n)\) counts prime factors with multiplicity. For every nontrivial relative \(\tau\)-number \(n>1\),
\[
\Omega(n)\ge p-1.
\]
This lower bound is sharp, and its equality cases are exactly
\[
\Omega(n)=p-1\quad\Longleftrightarrow\quad n=q^{p-1}
\]
with \(q\) a prime distinct from \(p\). Hence the minimum multiplicity is exactly \(p-1\) for every prime-power cyclotomic index \(p^k\), independently of \(k\).

## Assumptions and scope
Throughout, \(p\) and \(q\) denote primes, \(k\ge1\), and \(n>1\). The cyclotomic identity used is
\[
\Phi_{p^k}(x)=1+x^{p^{k-1}}+x^{2p^{k-1}}+\cdots+x^{(p-1)p^{k-1}}.
\]
The case \(p=2\) is included. No restriction on the size of \(n\), on \(k\), or on the prime \(q\ne p\) is imposed.

## Proof
First suppose \(p=2\). Since \(n>1\), trivially \(\Omega(n)\ge1=p-1\). Equality means that \(n=q\) is prime. Then
\[
\Phi_{2^k}(q)=q^{2^{k-1}}+1
\]
is even exactly when \(q\) is odd. Since \(\tau(q)=2\), the equality cases are precisely the primes \(q\ne2\), which are exactly the asserted numbers \(q^{p-1}\).

Now assume that \(p\) is odd. The value \(\Phi_{p^k}(n)\) is odd for every integer \(n\): if \(n\) is even, only the constant term is odd; if \(n\) is odd, the displayed sum has \(p\) odd summands. Thus \(\tau(n)\) is odd whenever it divides \(\Phi_{p^k}(n)\). The standard divisor-count criterion for odd \(\tau(n)\) shows that \(n\) is a square. Write
\[
n=\prod_{i=1}^s q_i^{e_i},\qquad e_i\ge2\text{ even},
\]
so \(\Omega(n)=\sum_i e_i\) and \(\tau(n)=\prod_i(e_i+1)\).

We use one local cyclotomic fact. Let \(r\) be a prime divisor of \(\Phi_{p^k}(n)\). If \(r\mid n\), then the displayed formula gives \(\Phi_{p^k}(n)\equiv1\pmod r\), a contradiction. Hence \(r\nmid n\). If additionally \(r\ne p\), then
\[
n^{p^k}\equiv1\pmod r.
\]
If \(n^{p^{k-1}}\equiv1\pmod r\), the displayed cyclotomic sum would give \(\Phi_{p^k}(n)\equiv p\pmod r\), forcing \(r=p\), again a contradiction. Therefore the multiplicative order of \(n\) modulo \(r\) is exactly \(p^k\), and consequently
\[
p^k\mid r-1,
\]
so \(r>p\).

Assume for contradiction that \(m=\Omega(n)<p-1\). Choose any prime \(r\mid\tau(n)\). Then \(r\mid e_i+1\) for some \(i\), so
\[
r\le e_i+1\le m+1\le p-1<p.
\]
But \(r\mid\tau(n)\mid\Phi_{p^k}(n)\). Since \(r<p\), the local fact applies and forces \(r>p\), a contradiction. Hence \(\Omega(n)\ge p-1\).

It remains to classify equality. Suppose \(\Omega(n)=p-1\). For any prime \(r\mid\tau(n)\), one has \(r\le e_i+1\le p\) for some \(i\). The local argument excludes every \(r<p\). Thus every prime divisor of each integer \(e_i+1\) is \(p\). Since \(2<e_i+1\le p\), necessarily \(e_i+1=p\), hence \(e_i=p-1\). The sum of all exponents is already \(p-1\), so there is only one prime-power block:
\[
n=q^{p-1}.
\]
The prime \(q\) cannot equal \(p\), because then \(\Phi_{p^k}(n)\equiv1\pmod p\) while \(\tau(n)=p\).

Conversely, let \(q\ne p\) be prime and set \(n=q^{p-1}\). Fermat's theorem gives \(n\equiv1\pmod p\), and therefore
\[
\Phi_{p^k}(n)\equiv\Phi_{p^k}(1)=p\equiv0\pmod p.
\]
Since \(\tau(n)=p\), this proves \(\tau(n)\mid\Phi_{p^k}(n)\). The equality classification follows.

## Verification
A finite regression program independently evaluated the relative divisibility condition for \(p\in\{2,3,5,7,11,13}\), \(1\le k\le3\), and \(2\le n\le100000\). It found no relative \(\tau\)-number below the claimed multiplicity boundary and no boundary case outside the prime powers \(q^{p-1}\) with \(q\ne p\). It also checked the converse for every boundary-shaped integer in that box. The output was:

`VERIFY_OK`, with `relative_hits=42475`, `boundary_hits=29001`, and `violations=0`.

This computation is only regression evidence. The proof above is symbolic and has no finite cutoff.

## Relationship to prior work
Zelinsky introduced \(\tau\)-numbers relative to integer polynomials. His 2002 Theorem 54 claimed infinitude for every integer polynomial, but Abel, Lauer, and Redi identified the gap in that argument and proved broad corrected infinitude criteria. Their Corollary 2 specifically proves that every cyclotomic polynomial \(\Phi_{p^k}\) has infinitely many relative \(\tau\)-numbers because \(\Phi_{p^k}(1)=p\). Their proof obtains witnesses from the general construction attached to the value at \(1\); it does not give a lower bound for \(\Omega(n)\), identify the minimum multiplicity, or classify all extremizers.

The present result supplies that missing sharp structural statement. It also strengthens the extremal existence part of the source construction: at the minimum layer, every prime \(q\ne p\) gives \(q^{p-1}\), not only primes selected from a particular congruence progression.

A semantic literature comparison also found a result for the different family \(\Phi_{2p^k}\), where certain indices have only the trivial relative \(\tau\)-number. That statement concerns a different cyclotomic index family and does not imply the prime-power-index boundary proved here.

## Limitations
The theorem determines only the first nontrivial \(\Omega\)-layer. It does not classify all relative \(\tau\)-numbers above multiplicity \(p-1\), give their counting function, or describe higher multiplicity fibers. The regression computation is not used to justify any unbounded claim.

## References
1. M. Abel, H. Lauer, and E. Redi, *About the number of \(\tau\)-numbers relative to polynomials with integer coefficients*, Acta et Commentationes Universitatis Tartuensis de Mathematica 25 (2021), 107–117, DOI 10.12697/ACUTM.2021.25.07.
2. J. Zelinsky, *Tau Numbers: A Partial Proof of a Conjecture and Other Results*, Journal of Integer Sequences 5 (2002), Article 02.2.8.
