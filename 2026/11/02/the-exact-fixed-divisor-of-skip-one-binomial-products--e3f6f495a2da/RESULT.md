# The exact fixed divisor of skip-one binomial products

## Finding

For each positive integer \(k\) put
\[P_k(n)=\binom{n}{k}\binom{n+2}{k},\qquad B_k=\binom{k+2}{2}.\]
Then the entire infinite sequence \(P_k(k),P_k(k+1),\ldots\) has exact greatest common divisor
\[\boxed{\gcd_{n\ge k}P_k(n)=
\begin{cases}
B_k/3,&k\equiv1\pmod3,\\
B_k,&k\not\equiv1\pmod3.
\end{cases}}\]
In fact, two values are a certificate for the exact answer:
\[\gcd_{n\ge k}P_k(n)=\gcd(P_k(k),P_k(k+1)).\]
Equivalently, the natural normalization \(P_k(n)/B_k\) is integral for all \(n\ge k\) precisely when \(k\not\equiv1\pmod3\). For \(k\equiv1\pmod3\), its exact universal denominator is \(3\). This is a complete classification for the first nonadjacent (gap-two) product of equal-order binomial coefficients.

## Assumptions and scope

Here \(k\) is any integer at least one and \(n\) is any integer at least \(k\); \(\binom nk\) has the usual factorial meaning. The fixed divisor of an integer-valued rational polynomial means the positive gcd of its values on the indicated integer domain. For prime \(p\), \(\nu_p(r)\) is the exponent of \(p\) in a nonzero integer \(r\), with \(\nu_p(0)=+\infty\). All claims are exact and unconditional.

## Proof

**1. Two sharp witnesses.** Direct evaluation yields
\[P_k(k)=B_k,\qquad P_k(k+1)=\frac{B_k(k+1)(k+3)}3.\]
The last expression is an integer even when its written multiplier has denominator \(3\). If \(k\not\equiv1\pmod3\), then \(3\mid(k+1)(k+3)\), so \(B_k\) divides both witness values. If \(k\equiv1\pmod3\), then \(3\nmid(k+1)(k+3)\) while \(3\mid B_k\), giving \(\gcd(P_k(k),P_k(k+1))=B_k/3\). Thus the infinite gcd divides the displayed candidate \(D_k\). It remains to prove that \(D_k\) divides every value.

**2. Prime powers arising from \(k+1\).** Let \(p^a\parallel(k+1)\) and \(n\ge k\). The integer binomial identities
\[(k+1)\binom{n+1}{k+1}=(n+1)\binom nk,\]
\[(k+1)\binom{n+3}{k+1}=(n+3)\binom{n+2}k\]
show that
\[\nu_p\binom nk\ge\max(0,a-\nu_p(n+1)),\]
\[\nu_p\binom{n+2}k\ge\max(0,a-\nu_p(n+3)).\]
For odd \(p\), the integers \(n+1\) and \(n+3\) differ by \(2\), so at least one is prime to \(p\). Hence \(p^a\mid P_k(n)\). When \(p=2\), at least one of them has two-adic valuation at most \(1\); hence \(2^{a-1}\mid P_k(n)\). These exponents are exactly those required by \(B_k=(k+1)(k+2)/2\), because \(p\nmid(k+2)\).

**3. Prime powers arising from \(k+2\).** Let \(p^a\parallel(k+2)\) and write \(m=n-k\ge0\). Two further integer binomial identities are
\[(k+1)(k+2)\binom n{k+2}=m(m-1)\binom nk,\]
\[(k+1)(k+2)\binom{n+2}{k+2}=(m+2)(m+1)\binom{n+2}k.\]
Because \(p\nmid(k+1)\), they imply the following: if at least one of the disjoint products \(m(m-1)\) and \((m+1)(m+2)\) has \(p\)-adic valuation at most \(c\), then \(\nu_p(P_k(n))\ge a-c\). This remains valid when a product is zero by assigning it infinite valuation and choosing the other product.

For \(p\ge5\), four consecutive integers cannot contain two multiples of \(p\), so one product is a \(p\)-unit. Therefore \(p^a\mid P_k(n)\). For \(p=3\), one product has three-adic valuation at most \(1\): if each is divisible by \(3\), the two multiples of \(3\) must be \(m-1\) and \(m+2\), separated by exactly \(3\), so one has valuation exactly \(1\). Thus \(3^{a-1}\mid P_k(n)\). For \(p=2\), the two even members of any four consecutive integers differ by \(2\), so at least one is divisible by \(2\) but not by \(4\); it lies in one of the two pairs, and that pair has valuation exactly \(1\). Therefore \(2^{a-1}\mid P_k(n)\).

**4. Assemble the local conclusions.** Consecutive \(k+1,k+2\) are coprime. Steps 2 and 3 show that every prime-power factor of \((k+1)(k+2)/2=B_k\) divides \(P_k(n)\), except potentially for one factor of \(3\) arising from \(k+2\) (precisely when \(k\equiv1\pmod3\)). Hence \(D_k\mid P_k(n)\) for every \(n\ge k\). Coupled with the two witnesses, this proves the theorem.

**5. Extension to every integer argument.** The rational polynomial \(P_k(X)=\binom Xk\binom{X+2}k\), divided by \(D_k\), is integer-valued for all sufficiently large nonnegative integers by Step 4. The finite-difference identity \(Q(z)=\sum_{j=0}^{2k}\Delta^jQ(0)\binom zj\) for any degree-at-most-\(2k\) rational polynomial \(Q\) (after translating its initial point to \(k\)) shows that its values at every integer are integral. Conversely the first two positive arguments already realize exact gcd \(D_k\). Thus the same fixed divisor applies on \(\mathbb Z\). Here \(\binom Xk\) denotes the falling-factorial polynomial, defined even at negative integers.

## Verification

Run the standalone `verify.py` with a Python 3 interpreter. It obtains binomial coefficients through two independent paths: direct factorial cancellation via `math.comb` and a separately constructed Pascal array. For each \(1\le k\le100\) it checks the complete prefix through \(n=5k+25\), its computed gcd, both witness formulas, and the exact universal denominator. It also checks the value-gcd against the gcd of Newton forward-difference coefficients of the translated degree-\(2k\) polynomial for \(1\le k\le20\). These are finite tests, not a replacement for the universal prime-local proof.

## Relationship to prior work

The fixed-divisor question belongs to integer-valued polynomial theory; standard binomial-basis methods characterize gcds of polynomial values by their Newton coefficients. The explicit gap-two product formula proved here gives a uniform sharp closed form and shows that the first two nonzero values alone determine the entire fixed divisor. The general theory does not itself state this particular \(3\)-exceptional classification.

Sun's 2010 work (arXiv:1004.4623) studies different divisibilities for products of binomial coefficients normalized by central binomial coefficients. McTague's 2015 work (arXiv:1510.06696) studies gcds of binomial coefficients with a fixed upper index and varying lower index. Neither the inspected statement of the former nor the inspected abstract of the latter gives the varying-upper-index fixed divisor here. The source inspection of McTague was limited to the abstract and available statement. Nonmatching titles or unsuccessful searches are not proofs of novelty.

## Limitations

The result is for two factors with shift precisely \(2\) and a common lower index; it does not classify all gaps or unequal lower indices. A general fixed-divisor theorem or a later specialization not identified in the searched literature could subsume the claim. No independent mathematical audit has been performed.

## References

1. Zhi-Wei Sun, *Products and sums divisible by central binomial coefficients*, arXiv:1004.4623 (initial public submission April 26, 2010), https://arxiv.org/abs/1004.4623 .
2. Carl McTague, *On the Greatest Common Divisor of Binomial Coefficients* (2015), arXiv:1510.06696, https://arxiv.org/abs/1510.06696 .
3. SageMath, *Integer-valued polynomial rings*, reference documentation, https://doc.sagemath.org/html/en/reference/polynomial_rings/sage/rings/polynomial/integer_valued_polynomials.html .
4. *Primary decomposition of the ideal of polynomials whose fixed divisor is divisible by a prime power*, Journal of Algebra (2014), DOI 10.1016/j.jalgebra.2013.09.016; only bibliographic and abstract-level material was accessible in this review.
