# Exact prime-power valuations of a binomial-coefficient gcd

## Finding

For every integer \(k\ge2\), let
\[
D(k)=\gcd_{2\le q\le k+1}\binom{qk}{k},\qquad n=k+1.
\]
For each exact prime-power component \(p^a\parallel n\), put \(b=n/p^a\). Then
\[
\boxed{\nu_p(D(k))=\begin{cases}
a,&b=1,\\
\max\{0,a-\lfloor\log_p(b-1)\rfloor\},&b>1.
\end{cases}}
\]
All prime divisors of \(D(k)\) divide \(n\). Moreover, at most one exact prime-power component \(p^a\parallel n\) has \(b\le p^a\). Thus the entire gcd is either \(1\) or a power of a *single prime*, given explicitly above.

For example, the values for \(k=11,23,35,71,224,255\) are respectively \(2,4,3,3,5,256\).

## Assumptions and scope

Every binomial coefficient uses ordinary integers, \(\gcd\) is positive, \(\nu_p\) denotes the usual \(p\)-adic valuation, and \(p^a\parallel n\) means \(a\ge1\), \(p^a\mid n\), and \(p^{a+1}\nmid n\). The integer \(b\) is positive and not divisible by \(p\). The logarithm occurs only when \(b\ge2\). No assertion concerns \(k<2\).

The proof uses the classical carry-counting theorem of Kummer and two previously proved facts for this exact gcd: every prime divisor of \(D(k)\) divides \(k+1\), and \(p\mid D(k)\) for \(p^a\parallel(k+1)\) precisely when \((k+1)/p^a\le p^a\). These are Lemmas 4 and 9, respectively, of Guo et al. [2]. The new step is the exact valuation, not the previously known divisibility criterion.

## Proof

**1. Prime support and the zero-valuation case.** Lemma 4 of [2] shows that no prime outside \(n=k+1\) divides \(D(k)\). Its Lemma 9 gives \(\nu_p(D(k))=0\) whenever \(b>p^a\). In this case \(b-1\ge p^a\), so \(\lfloor\log_p(b-1)\rfloor\ge a\), as required. It remains to treat \(b\le p^a\).

**2. Lower bound for every coefficient.** First suppose \(b>1\), and write
\[
c=\lfloor\log_p(b-1)\rfloor<a.
\]
Because \(p\nmid b\), the inequalities \(b-1<p^{c+1}\) imply \(b<p^{c+1}\). Fix any \(2\le q\le n\), let \(r=q-1\), and set \(s=\nu_p(r)\). Kummer's theorem interprets \(\nu_p\binom{qk}{k}\) as the number of carries when adding \(k\) and \(rk\) in base \(p\).

For every \(j\) with \(s<j\le a\), the congruences \(k\equiv-1\pmod{p^j}\) and \(rk\equiv-r\pmod{p^j}\) show a carry at position \(j\): the least residues are \(p^j-1\) and a nonzero integer. This yields \(\max\{0,a-s\}\) carries.

For every \(t\) with \(c<t\le s\), take \(j=a+t\). Since \(1\le r\le n-1\) and \(n=p^ab<p^{a+t}\), the least residue of \(k\) modulo \(p^{a+t}\) is \(n-1\). Moreover \(p^{a+t}\mid rn\), so the least residue of \(rk=r(n-1)\) is \(p^{a+t}-r\). Their sum is at least \(p^{a+t}\), yielding another \(\max\{0,s-c\}\) carries. The two sets of positions are disjoint. Therefore
\[
\nu_p\binom{qk}{k}\ge\max\{0,a-s\}+\max\{0,s-c\}\ge a-c.
\]
This is uniform over all admissible \(q\).

**3. A coefficient attaining the bound.** Choose an integer \(t\) with \(1\le t\le b-1\), and set \(q=1+p^at\). This satisfies \(2\le q\le n\). Compare the factors of
\[
\binom{qk}{k}=\prod_{j=1}^{k}\frac{p^atk+j}{j}.
\]
All factors with \(p^a\nmid j\) have cancelling \(p\)-adic valuations; the remaining factors give
\[
\nu_p\binom{qk}{k}=\nu_p\binom{tk+b-1}{b-1}.
\]
Since \(tk=t(p^ab-1)\), the numerator factors in the right-hand binomial are \(tp^ab-t+j\), for \(1\le j\le b-1<p^a\). For \(j\ne t\) their valuations equal those of \(j-t\); for \(j=t\) the valuation equals \(a+\nu_p(t)\). Cancelling factorial valuations proves the exact identity
\[
\boxed{\nu_p\binom{qk}{k}=a-\nu_p\binom{b-1}{t}.}
\]

If \(c=0\), choose \(t=1\). Then \(1\le b-1<p\), and \(\nu_p\binom{b-1}{1}=0\). If \(c\ge1\), write \(b=Lp^c+t\) with \(1\le L<p\) and \(1\le t<p^c\), using \(p\nmid b\). Lucas's theorem gives \(p\nmid\binom bt\) because the base-\(p\) digits of \(t\) are exactly the low \(c\) digits of \(b\). From
\[
\binom{b-1}{t}=\frac{b-t}{b}\binom bt
\]
and \(\nu_p(b-t)=c\), we get \(\nu_p\binom{b-1}{t}=c\). In either case the selected coefficient has valuation \(a-c\), matching the universal lower bound.

**4. The pure-prime-power case.** If \(b=1\), then \(k=p^a-1\), and \(p\)-adic carries below positions \(j\le a\) occur for every \(q\ge2\) whose \(q-1\) is not divisible by \(p^j\). The preceding lower-bound argument with \(c=0\) yields at least \(a\) carries, using the additional positions above \(a\) when \(q-1\) is divisible by \(p\). Taking \(q=2\), the sum \((p^a-1)+(p^a-1)\) has exactly \(a\) carries, so the minimum equals \(a\).

**5. Single-prime support.** For each \(p^a\parallel n\), positivity of its gcd valuation requires \(b\le p^a\), equivalently \(p^a\ge\sqrt n\). Two distinct exact prime-power components cannot both satisfy this because their product divides \(n\) and they are both at least \(\sqrt n\). Combined with step 1, this finishes the proof. \(\square\)

## Verification

The companion `verify.py` performs exact integer-gcd enumeration over all admissible \(q\) for every \(2\le k\le140\), and independent factorial-valuation minimization for every \(3\le n\le2000\) and every prime \(p\mid n\). It reports `VERIFY_OK` with 139 direct-gcd cases and 4453 prime-power valuation cases. These are finite checks; universality is proved above, using cited lemmas for prime support and zero valuation.

## Relationship to prior work

OEIS A080170 [1], originating in 2003, indexes those \(k\) for which \(D(k)=1\). Guo et al. [2] prove the exact condition for \(D(k)=1\) and provide the prime-divisibility criterion and supporting lemmas used here. Neither source states the *nonzero exponent* of a prime dividing \(D(k)\). The displayed valuation theorem refines the binary divisibility condition to an exact value for every \(k\), and establishes the single-prime-power structure directly from its prime support.

## Limitations

The proof depends on two published lemmas for prime support and the zero-valuation case. The new independent argument supplies the exact positive valuations and sharp witnesses. An equivalent formula may exist in literature not found by the targeted comparison; independent mathematical review has not been performed. No claim is made about gcds from other binomial families.

## References

[1] B. Cloitre, OEIS A080170, *Numbers \(k\) such that the gcd of binomial coefficients \(\binom{qk}{k}\) for \(2\le q\le k+1\) equals one*, entry dated January 31, 2003, https://oeis.org/A080170.

[2] D. Guo and collaborators, *A Greatest Common Divisor Criterion of Certain Binomial Coefficients*, arXiv:2606.22997 (first posted June 22, 2026), https://arxiv.org/abs/2606.22997; see especially Lemmas 4 and 9 and the principal criterion.

[3] E. E. Kummer, classical base-\(p\) carry theorem for the valuation of binomial coefficients; E. Lucas, classical digit congruence for binomial coefficients.
