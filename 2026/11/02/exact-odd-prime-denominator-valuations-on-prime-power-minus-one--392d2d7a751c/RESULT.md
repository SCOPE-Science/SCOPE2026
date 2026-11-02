# Exact odd-prime denominator valuations on prime-power-minus-one binomial rows

## Finding
For every odd prime \(p\), integer \(m\ge1\), and integer \(r\) with \(1\le r<p^m\), put \(q=p^m\), \(s=\nu_p(r)\), and
\[
S_r(n)=\sum_{k=0}^n\binom{n}{k}\frac{k}{k+r}.
\]
Then
\[
\boxed{\nu_p(S_r(q-1))=s-m.}
\]
In fact, the following sharper congruence determines the leading nonzero \(p\)-adic digit:
\[
\boxed{p^{m-s}S_r(q-1)\equiv(-1)^{q-r}\frac{q-r}{p^s}\pmod p.}
\]
The right-hand side is a unit modulo \(p\). Thus \(S_r(q-1)\notin\mathbb Z\) for all parameters in the stated domain. If \(B=\binom{q-1+r}{r}\), then the \(p\)-power in the reduced denominator of \(S_r(q-1)\) equals the \(p\)-power in \(B\), namely \(p^{m-s}\).

## Assumptions and scope
\(p\) is **odd and prime**; \(m\) is a positive integer; \(r\) is an integer between \(1\) and \(q-1\) inclusive; \(q=p^m\). For a nonzero rational number \(x\), \(\nu_p(x)\) is the exponent of \(p\) in its numerator minus that in its denominator when reduced. Congruences of rational numbers modulo \(p\) are used only when their denominators are units modulo \(p\). No asymptotic or bounded-parameter assumption is imposed.

## Proof
**1. Binomial coefficients in a prime-power-minus-one row.** Since \((1+X)^q\equiv1+X^q\pmod p\), coefficient comparison in
\[
(1+X)^{q-1}\equiv\frac{1+X^q}{1+X}\equiv\sum_{k=0}^{q-1}(-1)^kX^k\pmod p
\]
shows that \(\binom{q-1}{k}\equiv(-1)^k\pmod p\) for every \(0\le k\le q-1\). In particular all these coefficients are \(p\)-adic units.

**2. Unique term with minimum valuation.** The integers \(r+k\), for \(0\le k\le q-1\), form exactly one block of \(q\) consecutive positive integers inside \([1,2q-2]\). The unique multiple of \(q\) in this block is \(q\), occurring at
\[
k_*=q-r\in\{1,\ldots,q-1}.
\]
Write \(s=\nu_p(r)<m\). Then \(\nu_p(k_*)=s\), because \(k_*=q-r\) and \(\nu_p(q)=m>s\). The \(k_*\)-term
\[
a_*=\binom{q-1}{k_*}\frac{k_*}{q}
\]
therefore satisfies \(\nu_p(a_*)=s-m<0\).

For every other \(k\in\{1,\ldots,q-1}\), set \(b=\nu_p(k+r)\). Uniqueness of the multiple of \(q\) gives \(b<m\). By the ultrametric valuation inequality,
\[
\nu_p(k)=\nu_p((k+r)-r)\ge\min\{b,s\},
\]
so that, using the unit binomial coefficient,
\[
\nu_p\!\left(\binom{q-1}{k}\frac{k}{k+r}\right)
\ge\min\{b,s\}-b\ge\min\{0,s-m+1\}>s-m.
\]
(The \(k=0\) summand is zero.) Thus one and only one summand has the minimal \(p\)-adic valuation. The valuation of a sum with a unique lowest-valuation summand equals that valuation, proving \(\nu_p(S_r(q-1))=s-m\).

**3. Leading residue.** Multiplying by \(p^{m-s}\) kills every non-distinguished term modulo \(p\), while
\[
p^{m-s}a_*=\binom{q-1}{q-r}\frac{q-r}{p^s}
\equiv(-1)^{q-r}\frac{q-r}{p^s}\pmod p.
\]
Because \(\nu_p(q-r)=s\), the displayed residue is nonzero.

**4. Sharp denominator saturation.** For any positive integers \(n,r\), let \(B=\binom{n+r}{r}\). Each \(0\le k\le n\) satisfies the integer identity
\[
B\binom{n}{k}\frac{r}{r+k}
=\binom{n+r}{r+k}\binom{r+k-1}{k}\in\mathbb Z.
\]
Since \(S_r(n)=2^n-\sum_{k=0}^n\binom{n}{k}r/(r+k)\), its reduced denominator divides \(B\). For \(n=q-1\),
\[
\nu_p(B)=\nu_p\!\left(\frac{q(q+1)\cdots(q+r-1)}{r!}\right)
=m+\nu_p((r-1)!)-\nu_p(r!)=m-s,
\]
because \(1\le j<r<q\) implies \(\nu_p(q+j)=\nu_p(j)\). Combined with the established valuation of \(S_r(q-1)\), this proves saturation of the complete \(p\)-part of the universal denominator bound. \(\square\)

## Verification
The accompanying standalone `verify.py` evaluates the sums as exact rational numbers, independently recomputes their reduced denominators, checks the valuation formula, the leading residue congruence, the general denominator bound, and its sharp \(p\)-part. The program checks complete parameter intervals \(1\le r<p^m\) for the documented finite list of odd prime powers; no finite range is used to establish the universal theorem.

## Relationship to prior work
López-Aguayo and Luca (arXiv:1508.02927; first public posting 2015-07-30) proved nonintegrality for \(r\in\{1,2,3,4,5,6\}\) and \(n\le r-1\), not an exact odd-prime valuation at \(n=p^m-1\) for arbitrary \(r\). Laishram, López-Aguayo, Pomerance and Thongjunthug (arXiv:1903.08043) proved nonintegrality for \(r\le22\) and a density bound; neither assertion determines the present leading \(p\)-adic residue or arbitrarily large \(r\).

Kellner, *On the nonintegrality of certain generalized binomial sums* (INTEGERS 23 (2023), #A45), obtained the general denominator upper bound and criteria for nonintegrality, including exact denominator valuations at primes dividing the evaluation parameter \(\ell\). The sum here corresponds to evaluation \(\ell=2\); therefore those latter criteria directly cover the prime \(2\), which is **intentionally excluded** from the statement above. They do not assert the present exact valuation or residue for **odd** \(p\) in the prime-power-minus-one row. The general upper bound is independently reproved above. Thongjunthug's 2018 paper gives sufficient nonintegrality criteria and an algorithm, not a located exact valuation statement of this form. No claim of exhaustive novelty certification is made.

## Limitations
The theorem concerns only the rows \(n=p^m-1\), odd primes \(p\), and \(1\le r<p^m\). It does not determine the full denominator away from \(p\), the corresponding valuations for arbitrary \(n\), or settle the entire nonintegrality conjecture. An equivalent consequence in broader historical literature remains a residual originality risk. The universal argument is elementary and independent of the finite checks.

## References
1. D. López-Aguayo and F. Luca, *Sylvester's Theorem and the Non-integrality of a Certain Binomial Sum*, arXiv:1508.02927 (first posted 2015-07-30), https://arxiv.org/abs/1508.02927.
2. S. Laishram, D. López-Aguayo, C. Pomerance and T. Thongjunthug, *Progress Towards a Nonintegrality Conjecture*, arXiv:1903.08043 (2019), https://arxiv.org/abs/1903.08043.
3. B. C. Kellner, *On the Nonintegrality of Certain Generalized Binomial Sums*, INTEGERS 23 (2023), #A45, https://math.colgate.edu/~integers/x45/x45.pdf.
4. T. Thongjunthug, *Nonintegrality of Certain Binomial Sums*, European Journal of Mathematics 5 (2019), 571–584, first online 2018-06-19, doi:10.1007/s40879-018-0260-y.
