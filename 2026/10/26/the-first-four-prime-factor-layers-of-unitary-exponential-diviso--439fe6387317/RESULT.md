# The first four prime-factor layers of unitary–exponential divisor-sum equality

## Finding
Let \(\sigma^*(n)\) denote the sum of unitary divisors of a positive integer \(n\), let \(\sigma^{(e)}(n)\) denote the sum of exponential divisors, and let \(\Omega(n)\) count prime factors with multiplicity. Then, for **every** positive integer \(n\) with \(\Omega(n)\le4\),
\[
\sigma^*(n)=\sigma^{(e)}(n)\quad\Longleftrightarrow\quad n\in\{1,20,45\}.
\]
In particular, every other positive solution of this divisor-sum equality has at least five prime factors counted with multiplicity. The structural step not captured by a two-prime-support classification is the unconditional exclusion
\[
\sigma^*(p^2qr)\ne\sigma^{(e)}(p^2qr)
\]
for all **pairwise distinct** primes \(p,q,r\).

## Assumptions and scope
For a prime-power factorization \(n=\prod_p p^{a_p}\), a unitary divisor chooses either \(1\) or \(p^{a_p}\) at each prime. An exponential divisor chooses \(p^{d_p}\) with \(d_p\mid a_p\) at each prime. Thus both sums are multiplicative, with
\[
\sigma^*(p^a)=1+p^a,\qquad
\sigma^{(e)}(p^a)=\sum_{d\mid a}p^d.
\]
The empty products give \(\sigma^*(1)=\sigma^{(e)}(1)=1\) and \(\Omega(1)=0\). No primality or size restriction beyond those explicitly stated is imposed. The result concerns the complete \(\Omega\le4\) layer; it makes no assertion about existence or classification of solutions at higher multiplicities.

## Proof
**Step 1: prime powers, squarefree numbers, and doubly repeated factors.** For a prime \(p\), \(\sigma^*(p)=p+1>p=\sigma^{(e)}(p)\). For every exponent \(a\ge2\), the divisors \(1,a\) of \(a\) yield \(\sigma^{(e)}(p^a)\ge p+p^a>1+p^a=\sigma^*(p^a)\). Multiplicativity therefore excludes every nonunit squarefree number, every prime power, and every \(p^2q^2\) with distinct primes.

**Step 2: one repeated factor and one singleton.** Suppose \(p,q\) are distinct primes and \(a\in\{2,3\}\). Since both possible exponents \(a\) are prime,
\[
\sigma^*(p^aq)=(1+p^a)(1+q),\qquad
\sigma^{(e)}(p^aq)=(p+p^a)q.
\]
Equality is equivalent to \((p-1)q=p^a+1\). Reducing modulo \(p-1\) gives \(p-1\mid2\), hence \(p\in\{2,3\}\). For \(a=2\), both choices give \(q=5\) and the unequal primes yield exactly \(20\) and \(45\). For \(a=3\), the respective values \(q=9\) and \(q=14\) are not prime. Direct substitution verifies the two equality cases.

**Step 3: exclusion of three distinct primes with a single square.** Suppose \(n=p^2qr\), where \(p,q,r\) are pairwise distinct primes, and assume equality. Then
\[
(p^2+1)(q+1)(r+1)=p(p+1)qr.\tag{1}
\]
Dividing by \((p^2+1)qr\) shows
\[
(1+1/q)(1+1/r)=\frac{p(p+1)}{p^2+1}=1+\frac{p-1}{p^2+1}.
\]
Because each factor on the left exceeds \(1\), both \(q\) and \(r\) are strictly greater than \((p^2+1)/(p-1)>p+1\).

If \(p=2\), equation (1) implies \(5\mid qr\), whereas \(q,r>5\) and neither equals \(5\), a contradiction.

Let \(p\) be odd and put \(h=(p+1)/2\) and \(B=(p^2+1)/2=2h(h-1)+1\). Thus \(B>1\) and \(\gcd(B,p(p+1))=1\): indeed \(B\equiv1\pmod h\), \(B\) is odd, and \(\gcd(B,p)=1\). Equation (1) implies \(B\mid qr\). Since \(q,r>p+1\), we have \(qr>(p+1)^2>B\). The only positive divisors of the squarefree product \(qr\) are \(1,q,r,qr\), so \(B=q\) or \(B=r\). By symmetry take \(q=B\).

Then \(p^2+1=2q\), and cancellation in (1) gives
\[
(p^2+3)(r+1)=p(p+1)r,
\qquad (p-3)r=p^2+3.\tag{2}
\]
The case \(p=3\) is impossible in (2). For \(p\ge5\), integer \(r\) requires
\[
p-3\mid p^2+3=(p-3)(p+3)+12,
\]
so \(p-3\) is a positive even divisor of \(12\), giving \(p\in\{5,7\}\) among primes. At \(p=5\), equation (2) gives \(r=14\), not prime; at \(p=7\), the forced \(q=(p^2+1)/2=25\) is not prime. Contradiction in all cases.

**Step 4: exhaustive shape split.** Every \(n>1\) with \(\Omega(n)\le4\) is either a prime power, squarefree, or—up to renaming primes—one of \(p^2q\), \(p^3q\), \(p^2q^2\), and \(p^2qr\). Steps 1–3 exclude all shapes except \(p^2q\), for which Step 2 gives \(20,45\). Together with \(n=1\), this proves the theorem.

## Verification
The standalone Python file `verify.py` builds the smallest-prime-factor sieve through \(10^6\), independently constructs both multiplicative divisor sums from prime factorizations, and checks the complete \(\Omega\le4\) stratum within that finite range. The run tested \(737449\) integers with \(\Omega\le4\), including \(87338\) instances of the \(p^2qr\) shape. Its only equality hits were \(1,20,45\), with sums \((1,1)\), \((30,30)\), and \((60,60)\), respectively. This finite check is ancillary; Step 3 and the shape split prove the theorem without a numerical cutoff.

## Relationship to prior work
Trudgian introduced the unitary/exponential divisor-sum comparison, asked whether equality holds infinitely often, and listed sporadic examples. OEIS A236474 tabulates examples but does not prove an exhaustive low-\(\Omega\) classification. The published *The first 49 exponent layers of the unitary–exponential divisor-sum equality* classifies \(p^a q\) only for \(2\le a\le49\); it therefore covers the two-prime subcases \(p^2q\) and \(p^3q\) but does not address \(p^2qr\). The additional prime-support exclusion proved here completes the full multiplicity layer \(\Omega\le4\). Neither the known examples nor the two-prime exponent-layer result alone implies that exclusion. No originality is asserted for the individual numbers \(20\) and \(45\).

## Limitations
This is a low-multiplicity classification and does not resolve infinitude of equal-sum numbers or exclude any possible form with \(\Omega(n)\ge5\). The proof is independent of the finite experiment. Priority against unindexed notes and literature not available for full-text inspection remains uncertain; an independent mathematical audit has not been performed.

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615v1, first publicly submitted 2013-12-17; later published in *Publications de l'Institut Mathématique* 97(111) (2015), 175–180. https://arxiv.org/html/1312.4615v3
2. OEIS A236474, *Numbers whose sum of unitary divisors is equal to the sum of exponential divisors*. https://oeis.org/A236474
3. *The first 49 exponent layers of the unitary–exponential divisor-sum equality*, published research record, 2026-10-04. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-the-first-49-exponent-layers-of-the-unitary-exponential-divisor--59314f8e910e
