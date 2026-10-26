# Dyadic-exponent rigidity for equality of unitary and exponential divisor sums

## Finding
For each integer \(k\ge1\) and every pair of distinct primes \(p,q\),
\[
\sigma^*(p^{2^k}q)=\sigma^{(e)}(p^{2^k}q)
\quad\Longleftrightarrow\quad
(k,p,q)\in\{(1,2,5),(1,3,5)\}.
\]
Here \(\sigma^*\) is the unitary divisor sum and \(\sigma^{(e)}\) is the exponential divisor sum. Thus, across the entire infinite family with one prime exponent a power of two and the other exponent one, equality occurs only at the integers \(20\) and \(45\).

The underlying stronger, prime-independent statement is that for every integer \(x\ge2\) and every integer \(k\ge2\),
\[
Q_k(x)=\sum_{j=0}^{k-1}x^{2^j}-1
\quad\text{does not divide}\quad x^{2^k}+1.
\]
This is an exact divisibility obstruction, not a density estimate or finite search statement.

## Assumptions and scope
An exponential divisor of a prime power \(p^a\) is \(p^d\) with \(d\mid a\), while a unitary divisor of \(p^a\) is either \(1\) or \(p^a\). The sums are multiplicative on coprime arguments, so for distinct primes \(p,q\),
\[
\sigma^*(p^a q)=(p^a+1)(q+1),\qquad
\sigma^{(e)}(p^a q)=q\sum_{d\mid a}p^d.
\]
The theorem treats \(a=2^k\), \(k\ge1\), and cofactor exponent exactly one. It asserts nothing about cofactor exponents greater than one, arbitrary other exponents, or the global infinitude of solutions.

## Proof
First reduce the divisor-sum equality. With \(a=2^k\), its divisors are \(2^j\) for \(0\le j\le k\). Cancel the common \(q p^{2^k}\) terms to obtain the equivalence
\[
\sigma^*(p^{2^k}q)=\sigma^{(e)}(p^{2^k}q)
\quad\Longleftrightarrow\quad
p^{2^k}+1=qQ_k(p),\tag{1}
\]
where \(Q_k(p)=\sum_{j=0}^{k-1}p^{2^j}-1>0\).

For \(k=1\), equation (1) gives
\[
q=\frac{p^2+1}{p-1}=p+1+\frac2{p-1}.
\]
Integrality forces \(p-1\mid2\). Since \(p\) is prime, \(p\in\{2,3\}\), and each gives \(q=5\); these are distinct primes and direct substitution confirms equality.

For \(k=2\), put \(Q=x^2+x-1\). Since \(x^2\equiv1-x\pmod Q\),
\[
x^4+1\equiv R=(x-1)^2+1\pmod Q.
\]
For \(x\ge2\) the inequalities \(0<R<Q\) follow from \(Q-R=3(x-1)>0\). Therefore \(Q\nmid x^4+1\).

It remains to prove the assertion for every \(k\ge3\) and integer \(x\ge2\). Set
\[
U=x^{2^{k-2}},\qquad
V=\sum_{j=0}^{k-3}x^{2^j},\qquad
Q=U^2+U+V-1.
\]
The highest proper dyadic term is \(U^2\); consequently \(U^2\equiv-(U+V-1)\pmod Q\), and squaring gives
\[
x^{2^k}+1=U^4+1\equiv R=(U+V-1)^2+1\pmod Q.\tag{2}
\]
We claim the *strict interval*
\[
Q<R<2Q.\tag{3}
\]
For its first inequality, direct expansion yields
\[
R-Q=U(2V-3)+(V-1)(V-2)+1>0,
\]
because \(U\ge4\) and \(V\ge x\ge2\).

For the second inequality, establish by induction on \(k\ge3\) that
\[
U\ge3(V-2).\tag{4}
\]
At \(k=3\) this says \(x^2\ge3(x-2)\), true since \(x^2-3x+6>0\) for every real \(x\). When \(k\) increases by one, \((U,V)\) becomes \((U^2,U+V)\). Since \(U\ge4\), condition (4) implies
\[
3(U+V-2)\le4U\le U^2,
\]
so the induction closes. A second expansion now gives
\[
2Q-R=U^2-2U(V-2)-(V-2)^2
\ge\frac{2}{9}U^2>0.
\]
Thus (3) holds. If \(Q\mid x^{2^k}+1\), congruence (2) would imply \(Q\mid R\), contradicting \(Q<R<2Q\). This excludes all \(k\ge3\), proving both the stronger divisibility assertion and the divisor-sum classification.

## Verification
The accompanying self-contained `verify.py` uses only Python's standard library. It checks the exact divisor-sum identity against the reduction (1) for distinct primes at most \(100\) and \(1\le k\le7\); it tests the modular remainders and strict inequalities for every integer \(2\le x\le200\) and \(2\le k\le10\). Its exact-arithmetic output is

`VERIFY_OK: 4200 prime-pair equalities and 1791 integer-base dyadic layers`

These bounded checks are consistency tests only. The unrestricted result follows from the induction and interval argument above, independently of the checks.

## Relationship to prior work
Trudgian's 2013 preprint, *The sum of the unitary divisor function*, asks whether infinitely many integers have \(\sigma^*(n)=\sigma^{(e)}(n)\) and exhibits isolated examples, including \(20\) and \(45\). OEIS A236474 lists equality values but does not provide the present infinite-exponent restriction. The published mathematical result *The first 49 exponent layers of the unitary–exponential divisor-sum equality* classifies \(p^a q\) for \(2\le a\le49\), which in particular covers \(k\le5\) here; its fixed finite cutoff has no implication for \(k\ge6\). The present argument proves the full infinite dyadic-exponent branch by a uniform modular interval, without testing primes individually.

## Limitations
The result rules out equality only when the larger exponent is an exact positive power of two and the remaining prime factor has exponent one. It neither proves that all other exponent shapes admit equality nor resolves whether equality occurs infinitely often in general. A logically equivalent polynomial-divisibility obstruction in unlocated literature remains a possible originality risk. Independent mathematical validation has not been performed.

## References
Tim Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615, first submitted 2013-12-17; *Publications de l'Institut Mathématique* 97 (2015), 175–180. https://arxiv.org/abs/1312.4615

OEIS Foundation, A236474, *Numbers whose sum of unitary divisors is equal to the sum of exponential divisors*, first authored 2014-01-29. https://oeis.org/A236474

*The first 49 exponent layers of the unitary–exponential divisor-sum equality*, published research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-first-49-exponent-layers-of-the-unitary-exponential-divisor--59314f8e910e
