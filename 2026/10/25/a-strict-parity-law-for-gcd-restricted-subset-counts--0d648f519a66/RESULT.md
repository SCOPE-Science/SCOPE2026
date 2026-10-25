# A strict parity law for gcd-restricted subset counts

## Finding

For a positive integer \(m\), let \(f(m)\) be the number of nonempty subsets of \(\{1,\ldots,m\}\) with greatest common divisor \(1\). For a positive integer \(n\), let \(\Phi(n)\) count the nonempty subsets \(A\subseteq\{1,\ldots,n\}\) satisfying \(\gcd(\gcd(A),n)=1\), and define \(D(n)=\sum_{d\mid n}f(d)\).

**Theorem.** For every integer \(n\ge4\),
\[
(-1)^n\bigl(D(n)-\Phi(n)\bigr)>0.
\]
In particular, \(D(n)>\Phi(n)\) for even \(n\ge4\), and \(D(n)<\Phi(n)\) for odd \(n\ge5\). More precisely, with \(\mathbf{1}_{3\mid n}=1\) when \(3\mid n\) and zero otherwise, the following pointwise expansion holds as \(n\to\infty\):
\[
D(n)-\Phi(n)=(-1)^n2^{\lfloor n/2\rfloor}
+(2\mathbf{1}_{3\mid n}-1)2^{\lfloor n/3\rfloor}
+O(2^{\lfloor n/4\rfloor}).
\]
The implied constant is absolute. Thus the difference has magnitude asymptotic to \(2^{\lfloor n/2\rfloor}\), not merely infinitely many sign changes.

## Assumptions and scope

All sets counted here are nonempty subsets of the finite interval of positive integers indicated; the gcd of a singleton is its single element. Every bound refers to positive integers. The sign result holds without restrictions on the prime factorization of \(n\), starting at \(n=4\). The asymptotic statement is pointwise along all positive integers, not an average.

## Proof

**1. Stratification by exact gcd.** For each integer \(g\) between \(1\) and \(n\), division of every set element by \(g\) gives a bijection between subsets of \(\{1,\ldots,n\}\) having gcd exactly \(g\) and subsets of \(\{1,\ldots,\lfloor n/g\rfloor\}\) having gcd \(1\). Hence the count of the former is \(f(\lfloor n/g\rfloor)\). In particular, the subsets whose gcd divides \(n\) are counted by
\[
\sum_{g\mid n}f(\lfloor n/g\rfloor)
=\sum_{d\mid n}f(d)=D(n).
\]
The subsets whose gcd is coprime to \(n\) are counted by \(\Phi(n)\). The gcd-\(1\) stratum cancels, giving the exact identity
\[
D(n)-\Phi(n)=\sum_{g=2}^n
\bigl(\mathbf1_{g\mid n}-\mathbf1_{\gcd(g,n)=1}\bigr)
 f(\lfloor n/g\rfloor).\tag{1}
\]
Every subset containing \(1\) has gcd \(1\), whereas there are \(2^m-1\) nonempty subsets altogether. Therefore
\[
2^{m-1}\le f(m)\le 2^m-1\qquad(m\ge1).\tag{2}
\]

**2. All sufficiently large odd indices.** Let \(n\ge11\) be odd. The \(g=2\) stratum is included in \(\Phi(n)\) but excluded from \(D(n)\). Any stratum contributing positively to \(D(n)-\Phi(n)\) has \(g\mid n\) and \(g>1\), so \(g\ge3\). Dropping other negative terms and using (2),
\[
\begin{aligned}
\Phi(n)-D(n)
&\ge f(\lfloor n/2\rfloor)-\sum_{\substack{d\mid n\\d>1}}f(n/d)\\
&\ge 2^{(n-3)/2}-\sum_{j=1}^{\lfloor n/3\rfloor}(2^j-1)\\
&>2^{(n-3)/2}-2^{\lfloor n/3\rfloor+1}\ge0.
\end{aligned}
\]
The last inequality follows from \((n-3)/2\ge\lfloor n/3\rfloor+1\) for every odd \(n\ge11\). The preceding inequality is strict, so \(\Phi(n)>D(n)\).

**3. All sufficiently large even indices.** Let \(n=2t\) with \(t\ge8\). The \(g=2\) stratum contributes positively to \(D(n)-\Phi(n)\). Any negative stratum corresponds to \(\gcd(g,n)=1\), forcing \(g\) odd and at least \(3\). There are at most \(t-2\) remaining odd candidates after \(1\) and \(3\). Thus (1) and (2) give
\[
D(n)-\Phi(n)\ge f(t)-2^{\lfloor 2t/3\rfloor}-(t-2)2^{\lfloor 2t/5\rfloor}.
\]
For \(t\ge8\), \(\lfloor2t/3\rfloor\le t-2\). Also
\[
t-2\le 2^{3t/5-2}\quad(t\ge8).\tag{3}
\]
Indeed, at \(t=8\) it is \(6<2^{14/5}\). If true at integer \(t\), it remains true at \(t+1\), because \((t-1)/(t-2)\le7/6<2^{3/5}\). Consequently
\[
2^{\lfloor2t/3\rfloor}\le2^{t-2},\qquad
(t-2)2^{\lfloor2t/5\rfloor}\le2^{t-2}.
\]
Since \(f(t)\ge2^{t-1}\), this estimate alone is weakly nonnegative; strict positivity follows because (3) is actually strict at its base and remains strict in the induction (equivalently, \((t-2)2^{\lfloor2t/5\rfloor}<2^{t-2}\) for every \(t\ge8\)). Hence \(D(2t)>\Phi(2t)\) for all \(t\ge8\).

**4. Remaining finite indices.** Direct evaluation of the gcd-stratum formula yields
\[
\begin{array}{c|rrrrrr}
n&4&6&8&10&12&14\\\hline
D(n)-\Phi(n)&2&7&10&22&68&103
\end{array}
\]
and
\[
\begin{array}{c|rrr}
n&5&7&9\\\hline
\Phi(n)-D(n)&3&9&10
\end{array}.
\]
All these values can be obtained by finite inclusion-exclusion: \(f(m)=\sum_{d=1}^{m}\mu(d)(2^{\lfloor m/d\rfloor}-1)\). This completes the universal sign proof.

**5. Pointwise two-scale expansion.** Summing the exact-gcd strata over all nonempty subsets gives
\[
2^m-1=\sum_{g=1}^m f(\lfloor m/g\rfloor).
\]
By (2),
\[
\left|f(m)-2^m\right|
\le 1+2^{\lfloor m/2\rfloor}+m2^{\lfloor m/3\rfloor}
=O(2^{\lfloor m/2\rfloor}),\tag{4}
\]
because \(m2^{-m/6}\) is bounded as \(m\) varies. From (1), the contribution of \(g=2\) has coefficient \((-1)^n\), while that of \(g=3\) has coefficient \(2\mathbf{1}_{3\mid n}-1\). Replacing their \(f\)-values by powers of two introduces \(O(2^{\lfloor n/4\rfloor})\) error by (4). For \(g\ge4\), (2) gives the uniform bound
\[
\sum_{g=4}^{n} f(\lfloor n/g\rfloor)
\le 2^{\lfloor n/4\rfloor}+n2^{\lfloor n/5\rfloor}
=O(2^{\lfloor n/4\rfloor}),
\]
since \(n2^{-n/20}\) is bounded. This proves the displayed asymptotic expansion.

## Verification

Run `python3 verify.py` using Python's standard library. The verifier evaluates the Möbius formula and both gcd-stratified counts for every \(1\le n\le240\), checks the exact decomposition (1) for every \(2\le n\le240\), and independently enumerates all \(131054\) nonempty subsets in the cases \(1\le n\le16\). Its successful output is `VERIFY_OK mobius_and_gcd_strata=240 brute_force_subsets_n1to16=131054 parity_cases=237`. Finite checks independently corroborate but are not the proof of the unrestricted statements.

## Relationship to prior work

Pongsriiam, *Relatively Prime Sets, Divisor Sums, and Partial Sums* (2013), introduced \(D(n)\), compared partial sums, tabulated initial values, and explicitly asked in Question 3.1 whether the sign of \(D(n)-\Phi(n)\) alternates for every \(n\ge4\). The sign theorem settles exactly this question and therefore also implies the weaker infinite-sign-change question 3.2. The pointwise two-scale expansion adds quantitative information distinct from the source's partial-sum asymptotics. Tang (2010) proves identities for the individual functions \(f\) and \(\Phi\), but not the sign comparison involving \(D\). Łydka (2019) proves different inequalities involving log-concavity of \(f\) and a separate gcd-restricted count \(g\); those claims do not imply this theorem. The OEIS sequence A224840 lists \(D\)-values without an all-index sign theorem.

## Limitations

The theorem concerns the exact definitions above, not arbitrary gcd weighting or subset-size restrictions. It neither derives a closed formula for every value of \(D(n)-\Phi(n)\) nor resolves unrelated questions concerning perfect powers or modular periodicity. Searches may miss unindexed or later equivalent literature; independent mathematical assessment of proof and novelty remains outstanding.

## References

1. P. Pongsriiam, *Relatively Prime Sets, Divisor Sums, and Partial Sums*, Journal of Integer Sequences **16** (2013), Article 13.9.1, arXiv:1306.4891v1 (first public version 2013-06-20). Primary full text: https://www.maths.tcd.ie/EMIS/journals/JIS/VOL16/Pongsriiam/pong2.pdf
2. M. Tang, *Relatively Prime Sets and a Phi Function for Subsets of \(\{1,2,\ldots,n\}\)*, Journal of Integer Sequences **13** (2010), Article 10.7.6. Full text: https://cs.uwaterloo.ca/journals/JIS/VOL13/Tang/tang2.pdf
3. A. Łydka, *On Some Properties of the Function of the Number of Relatively Prime Subsets of \(\{1,2,\ldots,n\}\)*, arXiv:1910.02418v1 (2019). Full text: https://arxiv.org/pdf/1910.02418
4. OEIS Foundation, A224840, divisor sum of the relatively-prime-subset counting function: https://oeis.org/A224840
