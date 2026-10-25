# No perfect squares among the relatively prime subset counts

## Finding
For each integer \(n\ge1\), let \(\Phi(n)\) count the nonempty subsets \(A\subseteq\{1,\ldots,n\}\) for which \(\gcd(n,\gcd(A))=1\). **Theorem:** For every integer \(n\ge2\), the positive integer \(\Phi(n)\) is not a square. The following stronger alternatives establish the result:

\[
\nu_2(\Phi(n))=\frac{n}{\operatorname{rad}(n)}\quad(n\ge3\text{ odd}),
\]
\[
(2^m-1)^2<\Phi(2m)<(2^m)^2\quad(m\ge1).
\]
Consequently, no value \(\Phi(n)\) with \(n\ge2\) is a perfect power of even exponent. Equivalently, the number of aperiodic binary words of length \(n\) is never a square for \(n\ge2\).

## Assumptions and scope
The symbol \(\operatorname{rad}(n)\) denotes the product of the distinct prime divisors of \(n\), and \(\nu_2\) is the usual \(2\)-adic valuation. The empty subset is not counted by \(\Phi\); \(\Phi(1)=1\) is excluded from the theorem. The cited inclusion-exclusion identity, valid for all \(n\ge2\), is
\[
\Phi(n)=\sum_{d\mid n}\mu(d)\,2^{n/d},
\]
where \(\mu\) is the Möbius function. This follows also by partitioning the binary words of length \(n\) according to least period.

## Proof
**Odd arguments.** Fix odd \(n\ge3\). Put \(r=\operatorname{rad}(n)\) and \(t=n/r\). In the displayed Möbius sum, only squarefree divisors \(d\mid r\) contribute. The largest possible \(d\) is uniquely \(r\); hence the exponent \(n/d\) is uniquely smallest at \(d=r\), where it equals \(t\) and has coefficient \(\mu(r)=\pm1\). Every other contributing exponent is a *strictly larger integer* than \(t\). Division by \(2^t\) therefore leaves an odd integer. Thus \(\nu_2(\Phi(n))=t\). Because \(n\) and \(r\) are odd, \(t\) is odd. Every positive square has even \(2\)-adic valuation, proving the claim in this case.

**Even arguments.** Fix \(n=2m\) with \(m\ge1\). Regard all \(2^{2m}\) subsets, including the empty subset, as binary strings. A string is not counted by \(\Phi(2m)\) exactly when its chosen positions are contained in the multiples of some prime dividing \(2m\). For \(p=2\), this gives \(2^m\) strings, so
\[
\Phi(2m)\le 2^{2m}-2^m<2^{2m}.
\]
For the lower bound, let \(r\) be the number of distinct odd primes dividing \(m\). A union bound on the excluded strings yields
\[
2^{2m}-\Phi(2m)\le 2^m+\sum_{\substack{p\mid m\\p\text{ odd prime}}}2^{2m/p}
\le 2^m+r\,2^{2m/3}.
\]
For \(m=1,2\), there are no odd prime divisors, and directly \(\Phi(2m)=2^{2m}-2^m>(2^m-1)^2\).

For \(m\ge3\), the product of the \(r\) distinct odd prime factors (when \(r\ge1\)) is at least \(3^r\ge3r\), and divides \(m\); if \(r=0\), the following inequality is immediate. Thus \(r\le m/3\). The elementary inequality \(2^u\ge u+1\), valid for all real \(u\ge1\), now gives
\[
r\le \frac m3\le 2^{m/3}-1.
\]
Consequently
\[
 r\,2^{2m/3}\le 2^m-2^{2m/3}<2^m-1.
\]
It follows that
\[
\Phi(2m)> 2^{2m}-2^{m+1}+1=(2^m-1)^2.
\]
Since these are the squares of consecutive positive integers \(2^m-1\) and \(2^m\), no intermediate integer is a square. This completes the proof. □

## Verification
The standalone `verify.py` performs two independent finite checks: direct enumeration of all nonempty subsets for \(1\le n\le15\) against the Möbius formula, and exact integer arithmetic for all \(2\le n\le1000\), including the valuation assertion for odd inputs and consecutive-square inequalities for even inputs. It returns `VERIFY_OK: 15 exhaustive and 999 exact Möbius cases`. The unbounded theorem is established by the proof, not by the finite checks.

## Relationship to prior work
Tang, *Relatively Prime Sets and a Phi Function for Subsets of {1, 2, ..., n}* (2010), Remark 6, established that \(\Phi(p)\) and \(\Phi(pq)\) are neither squares nor cubes for primes \(p,q\). The theorem here extends the **square-exclusion** assertion to every integer \(n\ge2\), including arbitrary prime powers and products of three or more primes; it does not extend Tang's cube exclusion. Pongsriiam, *Relatively Prime Sets, Divisor Sums, and Partial Sums* (2013), Question 3.4, asks about perfect powers of \(\Phi(n)\) and \(D(n)\), referring separately to Ayad–Kihel's proof that \(f(n)\) is never a square. Neither the theorem for \(f\) nor Tang's one- and two-prime cases imply the present conclusion for all \(\Phi(n)\). OEIS A038199 and A027375 identify the same integers with aperiodic binary strings for \(n>1\). The 2015/2016 Pongsriiam local-behavior results concern ordering and log-behavior, not this all-index square exclusion.

## Limitations
The theorem does not rule out odd-exponent perfect powers (such as cubes) of \(\Phi(n)\), nor does it address squares or other powers of \(D(n)\). Perfect powers of odd exponent and the other branches of Question 3.4 remain outside the claim. General literature searches and sequence-page inspection do not establish absolute priority; a previously unlocated equivalent proof may exist. The evidence has not undergone independent mathematical review.

## References
1. M. Tang, *Relatively Prime Sets and a Phi Function for Subsets of {1, 2, ..., n}*, Journal of Integer Sequences **13** (2010), Article 10.7.6, Remark 6. https://cs.uwaterloo.ca/journals/JIS/VOL13/Tang/tang2.html
2. P. Pongsriiam, *Relatively Prime Sets, Divisor Sums, and Partial Sums*, arXiv:1306.4891v1 (first public 2013-06-20); J. Integer Sequences **16** (2013), Article 13.9.1, Question 3.4 and Lemma 1. https://arxiv.org/abs/1306.4891
3. M. Ayad and O. Kihel, *On the Number of Subsets Relatively Prime to an Integer*, J. Integer Sequences **11** (2008), Article 08.5.5 (general formula; no all-index square exclusion). https://cs.uwaterloo.ca/journals/JIS/VOL11/Ayad/ayad3.pdf
4. P. Pongsriiam, *Local Behaviors of the Number of Relatively Prime Sets*, International Journal of Number Theory **12** (2016), 1575–1593 (related local inequalities).
5. OEIS A038199 and A027375, sequence definitions and interpretations. https://oeis.org/A038199 and https://oeis.org/A027375
