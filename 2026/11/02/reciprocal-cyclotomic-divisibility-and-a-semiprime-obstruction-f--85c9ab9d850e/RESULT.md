# Reciprocal cyclotomic divisibility and a semiprime obstruction for a gcd-reciprocal sum

## Finding
For positive integers \(a,b\), put \(F(t)=t^2-t+1\). The two divisibilities \(a\mid F(b)\) and \(b\mid F(a)\) hold simultaneously **if and only if** \(a=b=1\).

Consequently, for every positive integer \(n>1\) with at most two prime factors counted with multiplicity, the rational number
\[
S(n)=\sum_{i=1}^{n}\frac{1}{\gcd(n,i)}
\]
is nonintegral. Equivalently, an integer value \(S(n)\in\mathbb Z\) with \(n>1\) necessarily requires \(\Omega(n)\ge3\), where \(\Omega\) counts prime factors with multiplicity.

## Assumptions and scope
All divisibility assertions are in the positive integers. The symbol \(\Omega(n)\) counts prime factors with multiplicity, so \(\Omega(pq)=2\) for distinct primes \(p,q\), and \(\Omega(p^2)=2\). No claim is made when \(\Omega(n)\ge3\), nor about the existence of any such integral values.

## Proof
**Cyclotomic two-cycle lemma.** Suppose a counterexample \((a,b)\) exists with \(a,b>1\); among all counterexamples choose one minimizing \(\max(a,b)\), and exchange the coordinates so that \(a\le b\). Equality would give \(a\mid F(a)\), but \(F(a)\equiv1\pmod a\), impossible for \(a>1\). Hence \(a<b\).

By \(b\mid F(a)\), the integer \(c=F(a)/b\) is positive. Because \(b>a\),
\[
0<c=\frac{a^2-a+1}{b}<a
\]
(the last inequality holds for every \(a>1\)). The defining identity \(bc=F(a)\) gives \(bc\equiv1\pmod a\). Since \(a\mid F(b)\), we have
\[
0\equiv c^2F(b)=(bc)^2-(bc)c+c^2\equiv1-c+c^2=F(c)\pmod a.
\]
We also have \(c\mid F(a)\) by construction. Thus \((c,a)\) obeys both reciprocal divisibilities. If \(c=1\), the condition \(a\mid F(1)=1\) is impossible; otherwise \(1<c<a<b\), contradicting minimality of \(b=\max(a,b)\). Finally, if either initial coordinate equals \(1\), the other divides \(F(1)=1\), hence both equal \(1\). This proves the lemma for all positive integers.

**Application to the reciprocal gcd sum.** Grouping the indices according to \(d=\gcd(n,i)\), then substituting \(m=n/d\), yields
\[
S(n)=\sum_{d\mid n}\frac{\varphi(n/d)}d=\frac1n\sum_{m\mid n}m\varphi(m).
\]
The numerator is multiplicative. For \(n=p^e\), the sum of \(m\varphi(m)\) over divisors equals
\[
1+\sum_{j=1}^e p^j(p^j-p^{j-1})
=\frac{p^{2e+1}+1}{p+1}
\equiv1\pmod p.
\]
It follows immediately that \(S(p)\) and \(S(p^2)\) are nonintegral. If \(n=pq\) with distinct primes, multiplicativity instead gives
\[
S(pq)=\frac{F(p)F(q)}{pq}.
\]
Since \(F(p)\equiv1\pmod p\) and \(F(q)\equiv1\pmod q\), integrality requires \(p\mid F(q)\) and \(q\mid F(p)\), contradicting the two-cycle lemma. The only integers with \(n>1\) and \(\Omega(n)\le2\) are \(p,p^2,pq\); hence the asserted conclusion follows.

## Verification
The proof is deductive and does not depend on numerical experiments. The companion `verify.py` directly checks the reciprocal divisibility obstruction for small pairs and the rational-integrality obstruction for integers with at most two prime factors through an independently implemented arithmetic calculation. Its checks have finite scope and are not an exhaustive substitute for the argument.

## Relationship to prior work
De Koninck and Letendre, arXiv:2610.10572 (first publicly posted 2026-10-04), study the same reciprocal gcd sum and prove a global bound \(O_\varepsilon(X^{2/3+\varepsilon})\) for the number of integer-valued cases through \(X\). That sparsity theorem does not, as stated in its abstract, give the pointwise exclusion of every prime and semiprime. The present result is a qualitative first-factor-layer obstruction and an integer two-cycle rigidity statement, not a strengthening of the cited global counting estimate.

## Limitations
The original paper's complete text was not accessible through the available open routes; the literature comparison therefore cannot exclude an implicit or unindexed earlier proof of this special case. General integers with \(\Omega(n)\ge3\) remain outside the classification. No assertion of an independently certified novelty or independent mathematical review is made.

## References
- J.-M. De Koninck and P. Letendre, *The Integer Values of \(\sum_{i=1}^{n}1/\gcd(n,i)\)*, arXiv:2610.10572, first posted 2026-10-04, https://arxiv.org/abs/2610.10572.
- OEIS A070999, denominators of \(\sum_{i=1}^{n}1/\gcd(n,i)\), https://oeis.org/A070999 (context for the denominator-reduction identity; not a classification of integrality).
