# Four-prime squarefree numerators for rational arithmetic antiderivatives of one

## Finding

Let \(D\) be the arithmetic derivative, characterized on primes by \(D(p)=1\) and on products by \(D(uv)=uD(v)+vD(u)\), extended to positive rational numbers by the quotient rule. Write \(x=a/b\) in lowest positive terms with \(b>1\) and \(a\) squarefree. If \(D(x)=1\), then \(a\) has at least four distinct prime divisors. Exactly four distinct prime divisors occur **if and only if** there is a prime \(q\ge 7\) for which \(r=q^q-30\) is prime and

\[
x=\frac{30(q^q-30)}{q^q}=\frac{30r}{q^q}.
\]

This is a complete parameterization of the four-prime squarefree-numerator stratum; it does not assert that the displayed prime-value condition has infinitely many solutions, or certify any particular large candidate.

## Assumptions and scope

For a nonzero rational \(x=\prod_p p^{e_p}\) with integral exponents of finite support, set \(D(x)=x\sum_p e_p/p\). In particular, \(D(p)=1\), \(D(1)=0\), and the product and quotient rules hold. The numerator \(a\) and denominator \(b\) are positive coprime integers and \(b>1\). Squarefree means no prime square divides \(a\). The number of distinct prime divisors of \(a\) is \(\omega(a)\). The theorem does not concern negative rationals, integers (which include the obvious prime solutions), or non-squarefree numerators.

## Proof

**Denominator rigidity.** Write \(b=\prod_{p\mid b}p^{e_p}\) and suppose \(D(a/b)=1\). The quotient rule gives

\[
D(a)-a\frac{D(b)}b=b.
\]

Because the outer terms are integers and \(\gcd(a,b)=1\), one has \(b\mid D(b)\). Thus

\[
K:=\frac{D(b)}b=\sum_{p\mid b}\frac{e_p}{p}
\]

is a positive integer. In fact, each \(p\mid b\) divides its exponent \(e_p\): multiply the integrality equation by the squarefree kernel \(P=\prod_{p\mid b}p\) and reduce modulo a chosen \(p\); the sole surviving term is \(e_pP/p\). Hence \(e_p=p k_p\) with positive integers \(k_p\), and \(K=\sum k_p\). Our equation is now

\[
D(a)-Ka=b>0. \tag{1}
\]

**Small squarefree numerators.** For squarefree \(a\) with at most four prime factors,

\[
\frac{D(a)}a=\sum_{p\mid a}\frac1p\le\frac12+\frac13+\frac15+\frac17=\frac{247}{210}<2.
\]

Consequently (1) forces \(K=1\), and therefore the denominator is exactly \(b=q^q\) for one prime \(q\). Furthermore \(D(a)>a\).

If \(\omega(a)\le2\), then \(D(a)/a\le1/2+1/3<1\). If \(\omega(a)=3\), the only prime triple with reciprocal sum greater than one is \(\{2,3,5\}\): the next possible triple \(\{2,3,7\}\) has sum \(41/42<1\), and any triple omitting \(2\) or \(3\) is still smaller. For \(a=30\), one has \(D(30)-30=1\), impossible since \(b=q^q\ge4\). Thus \(\omega(a)\ge4\).

Now assume \(\omega(a)=4\), and write the four primes in increasing order. Since \(1/2+1/5+1/7+1/11<1\), the first two must be \(2,3\). The third prime can only be \(5,7,11\), because \(5/6+1/13+1/17<1\).

If the third prime is \(11\), the fourth must be \(13\), as \(5/6+1/11+1/17<1\). In that case \(a=858=2\cdot3\cdot11\cdot13\), and \(D(a)-a=1\), contradicting (1). If the third prime is \(7\), the fourth prime \(s\) must satisfy \(s<42\), and direct differentiation yields

\[
D(2\cdot3\cdot7\cdot s)-2\cdot3\cdot7\cdot s=42-s\le31.
\]

Yet \(2,3\mid a\) and \(\gcd(a,q)=1\), so \(q\ge5\) and \(b=q^q\ge5^5>31\), again impossible.

The third prime must therefore be \(5\). Write the fourth as \(r\ge7\), so \(a=30r\) with \(r\) prime. Since \(D(30)=31\), the product rule gives \(D(a)=31r+30\), hence \(D(a)-a=r+30\). Equation (1) now forces \(r+30=q^q\). Coprimality with \(a\) excludes \(q=2,3,5\), so \(q\ge7\).

Conversely, if \(q\ge7\) and \(r=q^q-30\) are prime, then \(r\) is distinct from \(2,3,5,q\): \(r>5\), and \(r\equiv-30\not\equiv0\pmod q\). Thus \(30r/q^q\) is reduced and its numerator is squarefree with exactly four prime factors. Since \(D(q^q)=q^q\),

\[
D\!\left(\frac{30r}{q^q}\right)
=\frac{D(30r)-30r}{q^q}
=\frac{r+30}{q^q}=1.
\]

Both directions are proved.

## Verification

All proof-critical inequalities and differentiations above are exact. The included standalone script `checks/arithmetic_derivative_check.py` independently verifies these local inequalities, the exceptional four-prime surplus formulas, and finite direct searches in reduced fractions. Its finite searches are illustrative, not a substitute for the proof. The result uses no unverified large-prime primality claim.

## Relationship to prior work

Ufnarovski and Åhlander introduced the rational arithmetic-derivative equation \(D(x)=1\) as Conjecture 12 and proved the underlying denominator-divisibility machinery (2003, Sections 7–8). Dahl, Olsson and Loiko (arXiv:1108.4762v1, 2011) developed further theory of arithmetic differentiation on the rationals. In October 2026, a Mathematics Stack Exchange discussion supplied explicit counterexamples to the old conjecture and a **sufficient construction** using \(A=30\) and primes of the form \(q^q-30\). The converse established here is different: among **all** reduced positive rational solutions with a squarefree numerator of at most four prime factors and arbitrary denominator, no other form is possible. Neither the cited sufficient construction nor the basic denominator lemma supplies that classification alone without the prime-support case analysis above.

## Limitations

The result classifies the smallest possible squarefree numerator support but leaves the distribution, infinitude and primality testing of the integers \(q^q-30\) for prime \(q\) open. It makes no claim about non-squarefree numerators. The cited October 2026 discussion already contains the sufficient construction, so novelty is restricted to its necessary-and-sufficient small-support converse. An unindexed or inaccessible source could establish the same converse.

## References

1. V. Ufnarovski and B. Åhlander, *How to Differentiate a Number*, Journal of Integer Sequences **6** (2003), Article 03.3.4, published 2003-09-17. https://cs.uwaterloo.ca/journals/JIS/VOL6/Ufnarovski/ufnarovski.pdf
2. N. Dahl, J. Olsson and A. Loiko, *Investigations on the properties of the arithmetic derivative*, arXiv:1108.4762v1, first submitted 2011-08-24. https://arxiv.org/html/1108.4762v1
3. *Status of the conjecture that primes are the only positive rationals with arithmetic derivative equal to one*, Mathematics Stack Exchange, question 5151793, discussion dated 2026-10-13 through 2026-10-15. https://math.stackexchange.com/questions/5151793/
4. *We Can Differentiate Numbers, Too*, College Mathematics Journal **55** (2024), 2024 article; accessible preview discusses the original rational antiderivative problem. https://researchportal.tuni.fi/files/129275632/CollMathJ-S-19-00063.pdf
