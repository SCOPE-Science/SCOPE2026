# Exact prime-adic values of consecutive-multiple binomial gcds

## Finding
For each integer \(k\ge2\), set \(n=k+1\) and
\[
D(k)=\gcd_{2\le q\le n}\binom{qk}{k}.
\]
For every exact prime-power component \(p^a\parallel n\), write \(b=n/p^a\) and \(j=\lfloor\log_p b\rfloor\). Then
\[
\boxed{D(k)=\prod_{p^a\parallel n}p^{\max\{0,a-j\}}.}
\]
Thus this formula determines the entire positive integer gcd, not merely whether it equals one. If \(2\le b<p^a\), the explicit multiplier
\[
q=1+p^a\bigl(1+((b-1)\bmod p^j)\bigr)
\]
attains the minimum valuation \(a-j\) among all \(2\le q\le n\). If \(b=1\), multiplier \(q=2\) attains the minimum \(a\).

## Assumptions and scope
All variables are ordinary integers. The prime \(p\) can equal two. The exponent \(a\ge1\), \(p\nmid b\), and \(b\ge1\). The notation \(p^a\parallel n\) means exact divisibility; \(\lfloor\log_p b\rfloor\) is the largest integer \(j\ge0\) with \(p^j\le b\). The theorem is unconditional for all \(k\ge2\). The case \(b=1\) was independently covered by an earlier exact prime-power result; the substantive extension is the entire family with \(b>1\).

## Proof
Write \(K=p^ab-1=n-1\). Kummer's theorem says that \(\nu_p\binom{qK}{K}\) is exactly the number of base-\(p\) carries in \(K+(q-1)K\). We establish the local formula, then identify which primes can occur.

**Local zero case.** If \(j\ge a\), then \(b>p^a\), because \(p\nmid b\). Guo--Qiu--Cao--Feng--Gao, Lemma 9, proves \(p\mid D(k)\) exactly when \(b\le p^a\). Consequently \(\nu_p(D(k))=0\). The cited result is proved by Lucas's theorem and the digit-box argument in the original paper, and its hypotheses match these definitions.

**Local lower bound when \(j<a\).** Now \(b<p^{j+1}\le p^a\). Fix \(1\le t=q-1\le p^ab-1\), put \(v=\nu_p(t)\), and count carries in \(K+tK\). The lowest \(a\) digits of \(K\) are all \(p-1\), and the next digits represent \(b-1\), whose digits vanish above position \(a+j\).

If \(v\le j\), then \(tK\) has its first nonzero digit at position \(v\). It initiates a carry against the \(p-1\) digit of \(K\), which continues through positions \(v,v+1,\ldots,a-1\). There are at least \(a-v\ge a-j\) carries.

If \(j<v<a\), write \(t=p^vu\) with \(p\nmid u\). Since \(t<p^ab\), one has \(0<u<p^{a-v}b<p^a\). The lowest \(a\) digits of \(uK\) represent \(p^a-u\). As before, in \(K+p^vuK\), carries occur at all positions \(v,\ldots,a-1\), giving \(a-v\) carries and an entering carry at position \(a\). Put \(c=\lceil u/p^{a-v}\rceil\), so \(1\le c\le b<p^{j+1}\). The next block of \(j+1\) digits of \(p^vuK\), at positions \(a,\ldots,a+j\), represents \(p^{j+1}-c\): indeed these are the corresponding digits of \(p^a-u\), shifted by \(v\), and \(v\ge j+1\). The corresponding digits of \(K\) represent \(b-1\). Including the entering carry, their sum is \(p^{j+1}+b-c\ge p^{j+1}\). Hence a carry exits this block and at least one carry occurs inside it. At positions \(a+j+1,\ldots,a+v-1\), the digits of \(K\) vanish and those of \(p^vuK\) equal \(p-1\): this follows from \(u<p^{a+j+1-v}\), which makes those upper digits of \(p^a-u\) all \(p-1\). Thus the carry continues over another \(v-j-1\) positions. Total carries are at least \((a-v)+1+(v-j-1)=a-j\).

Finally if \(v\ge a\), write \(t=p^aw\), with \(1\le w\le b-1\). No carry occurs below position \(a\); after shifting \(a\) digits, we add \(b-1\) to \(wK\). As \(w<p^{j+1}\le p^a\), the lowest \(a\) digits of \(wK\) are \(p^a-w\). Their sum with \(b-1\) is \(p^a+(b-1-w)\ge p^a\), so a carry exits the entire block. All digits in positions \(j+1,\ldots,a-1\) of \(p^a-w\) are \(p-1\), and those of \(b-1\) are zero. Consequently that exiting carry requires at least one earlier carry in positions \(0,\ldots,j\) and propagates through all \(a-j-1\) subsequent positions: at least \(a-j\) carries. This proves \(p^{a-j}\mid D(k)\).

**Explicit matching upper bound.** For \(b\ge2\), let \(b-1=s p^j+r\), with \(1\le s\le p-1\) and \(0\le r<p^j\). Put \(\ell=r+1\), so \(1\le\ell\le p^j\le b-1\) and \(p\nmid\ell\) (for \(j>0\), \(\ell\equiv b\pmod p\); for \(j=0\), \(\ell=1\)). Set \(q=1+p^a\ell\), within \([2,n]\). The low \(a\) digits of \(tK=p^a\ell K\) are zero. After shifting those digits, the relevant addition is
\[
(b-1)+\ell K=(b-1)+(p^a-\ell)+p^a(\ell b-1).
\]
Now \((p^a-\ell)+(b-1)=p^a+s p^j-1\). In its lowest \(a\) digits there are no carries below position \(j\), and exactly one carry at every position \(j,\ldots,a-1\), since \(s\in[1,p-1]\) and the upper digits of \(p^a-\ell\) are \(p-1\). This is exactly \(a-j\) carries. The final carry entering the next digit stops: that digit of \(\ell b-1\) is not \(p-1\), because \(p\nmid\ell b\). There are no further carries. Thus this admissible \(q\) satisfies \(\nu_p\binom{qK}{K}=a-j\).

When \(b=1\), \(K=p^a-1\). The argument above with \(j=0\) and \(t\in[1,p^a-1]\) gives at least \(a\) carries: writing \(t=p^vu\) with \(v<a\), there are \(a-v\) lower carries, followed by \(v\) carries because \(tK=t p^a-t\) has upper quotient \(t-1\), whose lowest \(v\) digits equal \(p-1\). At \(q=2\), adding \(K+K\) has exactly \(a\) carries. Hence the local exponent is \(a\).

**No extraneous primes.** Let \(F(X)=\binom{kX}{k}\), a degree-\(k\) rational polynomial taking integer values at nonnegative integers. If a prime \(r\) divides all \(F(2),\ldots,F(k+1)\), then \(\Delta^hF(1)\equiv(-1)^h\pmod r\) for every \(0\le h\le k\), because \(F(1)=1\). Newton's forward-difference identity at \(X=0\) gives \(0=F(0)=\sum_{h=0}^k(-1)^h\Delta^hF(1)\equiv k+1\pmod r\). Thus \(r\mid n\). Together with the local valuation formulas for every prime divisor of \(n\), this proves the product formula.

## Verification
The independent executable `verify.py` computes exact Kummer carries directly for each prime divisor of \(n\) and each multiplier \(2\le q\le n\) on an exhaustive finite range. It compares the minimum with the stated prime-adic formula, independently compares small integer gcds of actual binomial coefficients, and tests the explicit minimizing multiplier. It reports the precise checked ranges. These finite checks corroborate but do not replace the all-integer carry argument above.

## Relationship to prior work
Guo et al., *A Greatest Common Divisor Criterion of Certain Binomial Coefficients* (arXiv:2606.22997v1, publicly posted June 22, 2026), prove the unit criterion \(D(k)=1\) iff the cofactor of the largest exact prime-power component exceeds that component; their Lemma 9 characterizes only whether a given prime divides the gcd. The present theorem strictly strengthens this to each **exact valuation**, and gives a constructive minimizing multiplier when the cofactor is nontrivial. The OEIS A080170 record lists the unit cases but not a complete value formula. The pure prime-power subcase \(D(p^a-1)=p^a\) was already established separately, and is not independently claimed new here. No earlier exact composite-case formula was found in the consulted records.

## Limitations
The theorem concerns only the specified consecutive-multiple family and its complete range \(2\le q\le k+1\); it makes no claim for truncated or other binomial subfamilies. Priority beyond the inspected primary literature and available mathematical records is not independently certified. Verification is finite, while the proof is uniform.

## References
1. Dakai Guo, Ruichen Qiu, Yichuan Cao, Ruyong Feng, Xiao-Shan Gao, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997v1 (first public June 22, 2026), https://arxiv.org/html/2606.22997v1 .
2. OEIS Foundation, A080170, https://oeis.org/A080170 (consulted October 29, 2026).
3. E. E. Kummer, 1852, classical carry interpretation of prime valuations of binomial coefficients.
