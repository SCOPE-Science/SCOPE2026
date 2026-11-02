# Bounded exceptions in dyadic Stirling valuation formulas

## Finding

Write \(S(n,k)\) for the Stirling number of the second kind, \(\nu _2\) for the exponent of two dividing a positive integer, and \(s_2(x)\) for the sum of the binary digits of a nonnegative integer \(x\). Fix an integer \(c\geq 1\). For each integer \(b\) with \(0\leq b<c\), define the nonnegative integer

\[
 t_b=\nu _2\binom{2c-b-1}{c}.
\]

**Theorem (interior formula).** For every \(h\geq 1\), put \(q=2^h\). For any \(b\in\{0,\ldots,c-1\}\) and \(a\in\{1,\ldots,q-1\}\) such that \(q-a\geq2t_b\), one has

\[
\boxed{\nu _2\bigl(S(cq,bq+a)\bigr)
=s_2(bq+a)-s_2(c)+\nu _2\binom{2cq-bq-a}{cq}
=s_2(a)+s_2(b)-s_2(c)+t_b.}
\]

**Theorem (uniform bounded-exception law).** For every \(h\geq1\), among the \(cq\) indices \(1\leq k\leq cq\), at most

\[
\boxed{E(c)=(c-1)+\sum_{b=0}^{c-1}\max\{2t_b-1,0\}}
\]

can violate the formula

\[
\nu _2\bigl(S(cq,k)\bigr)=s_2(k)-s_2(c)+\nu _2\binom{2cq-k}{cq}.
\]

Consequently the proportion of indices satisfying the formula is at least \(1-E(c)/(c2^h)\), hence tends to one with discrepancy \(O_c(2^{-h})\). This proves the positive-index version of Adelberg--Lengyel, *New Results on the p-adic Valuation of Stirling Numbers* (2021), Conjecture 3.1. The conjecture's displayed range includes \(k=0\), for which \(S(cq,0)=0\) and the ordinary finite valuation is undefined; under the convention \(\nu _2(0)=+\infty\), that index is simply an additional single exceptional position.

## Assumptions and scope

The theorem holds for every fixed positive integer \(c\), every positive integer \(h\), and every indicated interior index; no lower bound on \(h\) is needed. The bound \(E(c)\) is an explicit upper bound, not an assertion that all these positions actually fail. At the top endpoint \(k=cq\), the formula holds because \(S(cq,cq)=1\) and \(\binom{cq}{cq}=1\). The remaining excluded indices are the \(c-1\) internal multiples of \(q\) and a bounded collection of right-end positions in the interior blocks.

## Proof

We give the exact term-comparison proof. For arbitrary integers \(1\leq k\leq n\), set \(r=n-k\). A finite partition \(u=(u_1,u_2,\ldots)\) means that all \(u_i\) are nonnegative integers and all but finitely many vanish. Define

\[
 w(u)=\sum_{i\geq1} i u_i,\qquad d(u)=\sum_{i\geq1}u_i,\qquad
 \Lambda(u)=\prod_{i\geq1}(i+1)^{u_i}.
\]

The exact partition expansion for Stirling polynomials, explicitly given in [1, equations (5.2) and (5.4)], yields

\[
 S(n,k)=(-1)^r\binom nk r!
 \sum_{w(u)\leq r}(-1)^{d(u)}
 \binom{n+d(u)}n
 \frac{d(u)!}{\prod_i u_i!}\frac1{\Lambda(u)}.
 \tag{1}
\]

We recall why the expansion is applicable: [1] identifies \(S(n,k)=\binom nk B_r^{(-k)}\) and expresses this higher-order Bernoulli number as the displayed finite partition sum, with its generalized binomial factor at \(s=-n-1\). Formula (1) is an equality of rational numbers, not a congruence.

Fix \(c,h,b,a\) as above. Put \(n=cq\), \(k=bq+a\), \(B=q-a\), and \(T=(c-b-1)q\). Then \(1\leq B<q\), \(T\geq0\), and \(r=T+B\). Let \(t=t_b\). Kummer's binary carry theorem, or Legendre's factorial formula, gives

\[
 \nu _2\binom{n+r}{n}
 =\nu _2\binom{(2c-b-1)q+B}{cq}=t.
 \tag{2}
\]

In fact, for every integer \(d\) with \(T\leq d\leq r\), writing \(d=T+j\) with \(0\leq j\leq B<q\) gives

\[
\nu _2\binom{n+d}{n}
=\nu _2\binom{(2c-b-1)q+j}{cq}=t.
\tag{3}
\]

For the unique partition \(u^*\) with \(u^*_1=r\) and all other coordinates zero, one has \(d(u^*)=w(u^*)=r\), \(\Lambda(u^*)=2^r\), and the multinomial coefficient equals one. Thus the valuation of its entire summand *including* \(r!\), but excluding the common factor \(\binom nk\), is

\[
\nu _2(r!)+t-r=t-s_2(r).
\tag{4}
\]

For any partition \(u\) with \(w(u)\leq r\), the valuation of its summand including \(r!\) is

\[
\nu _2(r!)+\nu _2\binom{n+d(u)}n
+\nu _2\frac{d(u)!}{\prod_i u_i!}
-\nu _2\Lambda(u).
\tag{5}
\]

The multinomial factor is an integer, so its valuation is nonnegative. Also
\(\nu _2(i+1)\leq i\) for each integer \(i\geq1\), with equality *only* at \(i=1\). Consequently \(\nu _2\Lambda(u)\leq w(u)\leq r\), and equality \(\nu _2\Lambda(u)=r\) occurs only for \(u=u^*\).

If \(d(u)\geq T\), equation (3) makes the binomial valuation in (5) equal to \(t\). All terms other than \(u^*\) therefore have strictly larger valuation than (4).

If \(d(u)<T\), use the stronger elementary estimate \(\nu _2(i+1)\leq(i+1)/2\) for every \(i\geq1\), giving

\[
\nu _2\Lambda(u)
\leq\frac{w(u)+d(u)}2
\leq\frac{r+d(u)}2.
\]

Because \(d(u)\) and \(T\) are integers and \(d(u)<T\),

\[
 r-\nu _2\Lambda(u)\geq\frac{r-d(u)}2
 \geq\frac{B+1}2>t
 \quad\text{whenever }B\geq2t.
\tag{6}
\]

The other two terms in (5) after \(\nu _2(r!)\) are nonnegative; hence (6) also makes this summand strictly higher in valuation than (4). For \(T=0\), this second case is empty. Thus the \(u^*\) summand uniquely determines the \(2\)-adic valuation of the entire sum (1); there can be no cancellation of its lowest-valuation term. Combining (4) with \(\nu _2\binom nk=s_2(k)+s_2(r)-s_2(n)\) gives

\[
 \nu _2(S(n,k))
=s_2(k)-s_2(n)+t
=s_2(a)+s_2(b)-s_2(c)+t.
\]

Equations (2) and (3) yield the other displayed form. This proves the interior formula.

For each \(b\), the interior indices failing the *hypothesis* \(B\geq 2t_b\) correspond to positive integers \(B<2t_b\). Their number is at most \(\max\{2t_b-1,0\}\), independently of \(h\). The only positive indices not in any interior block are the \(c-1\) internal multiples of \(q\) and \(k=cq\); the latter satisfies the formula. Summing these bounds gives \(E(c)\) and the claimed density estimate. \(\square\)

## Verification

The accompanying `verify.py` computes Stirling numbers by the exact recurrence \(S(n,k)=S(n-1,k-1)+kS(n-1,k)\), reducing modulo \(2^{32}\). For \(1\leq c\leq12\) and \(1\leq h\leq7\), it compares all \(19{,}812\) positive-index valuations with the asserted target expression, verifies all \(18{,}537\) indices within the sufficient interior condition, checks that every observed disagreement falls within the bounded exception envelope, and checks the binomial carry valuation independently via binary digit sums. Every checked target valuation lies below 32, so the modular computation determines it exactly. The verifier is finite corroboration; the proof above establishes the infinite statements.

## Relationship to prior work

Adelberg and Lengyel [1, Theorem 3.1] prove the same valuation formula in the initial half of every dyadic block, subject to a condition on \(h\). Their [1, Conjecture 3.1] asks whether the formula holds for asymptotically almost all indices. The present argument retains their exact Stirling-partition expansion and dominant-term strategy, but replaces the first-half restriction by the local condition \(2^h-a\geq2t_b\), yielding a uniform-in-\(h\) bound on the total number of exceptions. No new formula for all of the finitely many exceptional indices is asserted. Earlier Adelberg [2] establishes broad binary valuation estimates and a scaled-index asymptotic theorem, but does not give this bounded-exception law. The result also encompasses the classical first-block exact formula rather than claiming that known case as new.

## Limitations

Originality is assessed against inspected mathematical sources and searches, not independently certified; an earlier unindexed proof or an implicit statement in a broader theorem remains possible. The numerical verification is not an infinite proof, and \(E(c)\) need not equal the exact number of exceptions. No claim is made for primes other than two or for Stirling numbers of the first kind. The interpretation of \(k=0\) depends on whether the valuation of zero is allowed to be infinite.

## References

[1] A. Adelberg and T. Lengyel, *New Results on the p-adic Valuation of Stirling Numbers*, arXiv:2111.08766v1 (first public posting 2021-11-16), especially Theorem 3.1, Section 3.4, and equations (5.2), (5.4). https://arxiv.org/html/2111.08766v1

[2] A. Adelberg, *The 2-Adic Analysis of Stirling Numbers of the Second Kind via Higher Order Bernoulli Numbers and Polynomials*, arXiv:1912.01090v1 (2019), especially Theorems 2.1--2.6 and Section 3. https://arxiv.org/html/1912.01090v1
