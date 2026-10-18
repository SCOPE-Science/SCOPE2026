# Maximal common subsequences collapse to longest ones for reversed periodic permutations

## Finding

Let \(q\ge2\) and \(m\ge1\) be integers. Over the ordered alphabet \(\{0,\ldots,q-1\}\), consider the two words \(U_{q,m}=(0\,1\,\cdots\,(q-1))^m\) and \(V_{q,m}=((q-1)\,\cdots\,1\,0)^m\). Every inclusion-maximal common scattered subsequence of these words is a longest common subsequence, of length exactly \(2m-1\). Their common maximal subsequences are precisely the length-\(2m-1\) words with no equal adjacent letters, exactly \(m-1\) adjacent ascents, and exactly \(m-1\) adjacent descents.

In particular the exact number \(C_{q,m}\) is a balanced-walk transfer-matrix coefficient:
\[
C_{q,m}=[t^{2m-2}z^0]\,\mathbf{1}^{\mathsf T}(I-tM_q(z))^{-1}\mathbf{1},\qquad
(M_q(z))_{ij}=\begin{cases}z&i<j,\\z^{-1}&i>j,\\0&i=j.\end{cases}
\]
For \(q=2\), \(C_{2,m}=2\). For \(q=3\), the coefficient simplifies, for every \(m\ge1\), to
\[
\boxed{C_{3,m}=\binom{2m+2}{m+1}-2\binom{2m}{m}+\binom{2m-2}{m-1}.}
\]
Thus \(C_{3,m}\) begins \(3,10,36,132,490,1836,6930,26312,\ldots\), and \(C_{3,m}\sim 9\,4^m/(4\sqrt{\pi m})\). Equivalently,
\[
\sum_{m\ge1}C_{3,m}x^{m-1}=\frac{(1-x)^2(1-4x)^{-1/2}-1}{x^2}.
\]

## Assumptions and scope

A scattered subsequence of a finite word is obtained by deleting zero or more symbols without changing the order of the remaining symbols. A common subsequence is *maximal* if inserting any additional single symbol at any position produces a word not common to both input words. It is *longest* if its length is maximum among all common subsequences. A strict ascent (descent) is a neighboring ordered pair of distinct letters whose second letter is larger (smaller). An equality is a neighboring pair of identical letters. All statements range over every integer \(q\ge2\) and \(m\ge1\), and distinguish subsequence inclusion from contiguous-factor inclusion.

## Proof

**Greedy block criterion.** Let \(w=w_1\cdots w_\ell\) be a nonempty word. Write \(a(w),d(w),e(w)\) for its numbers of strict adjacent ascents, strict adjacent descents, and equal adjacent pairs. In \(U_{q,m}\), a left-to-right greedy embedding uses one initial increasing block and a new block for each descent or equality, hence the minimum number of blocks is \(1+d(w)+e(w)\). In \(V_{q,m}\), the minimum number is \(1+a(w)+e(w)\). Consequently,
\[
w\preceq U_{q,m},V_{q,m}\quad\Longleftrightarrow\quad d(w)+e(w)\le m-1\ \text{and}\ a(w)+e(w)\le m-1.\tag{1}\]
Since \(\ell=1+a(w)+d(w)+e(w)\), every nonempty common subsequence has length at most \(2m-1-e(w)\). This bound is attained by the length-\(2m-1\) alternating word in the two extreme letters, so the longest length is exactly \(2m-1\). Every common word of that length necessarily has \(e(w)=0\) and \(a(w)=d(w)=m-1\). Conversely each such word meets (1).

**Every shorter common subsequence extends.** If two neighboring letters are both \(i\), insert any letter \(j\ne i\) between them. The old equality is replaced by one ascent and one descent. Both quantities \(a+e\) and \(d+e\) in (1) remain unchanged, so the longer word remains common. Repeat until there are no adjacent equalities. This reduces the problem to strictly changing words.

For a strictly changing common word define its unused ascent and descent budgets as \(r_a=m-1-a(w)\) and \(r_d=m-1-d(w)\). If both are positive, append the alphabet maximum and then minimum when the last letter is below maximum; if it already equals maximum, append minimum and then maximum. The two successive insertions add exactly one ascent and one descent and respect (1) at both intermediate stages. Thus at least one budget can be filled while maintaining commonness.

Suppose next that the descent budget is full but the ascent budget has a positive remainder. Then \(a(w)<d(w)=m-1\). We prove that some insertion adds exactly one ascent and no descent. If no such insertion were possible, the first symbol must be minimum (otherwise a smaller one could be prepended), and the last must be maximum (otherwise a larger one could be appended). Every existing ascent must join consecutive alphabet values (otherwise an intermediate alphabet value could be inserted to split it into two ascents), and every existing descent must go directly from maximum to minimum (otherwise an alphabet value outside the descending interval could be inserted, yielding one ascent and one descent in place of the original descent). The sum of adjacent letter differences would then give
\[
q-1=w_\ell-w_1=a(w)-(q-1)d(w),
\]
so \(a(w)=(q-1)(d(w)+1)>d(w)\), a contradiction. Hence an ascent-only insertion exists. The descending version follows by reversing the alphabet order. Repeating such insertions fills both budgets. Any common word therefore extends to a common word with no equal neighboring symbols and \(a=d=m-1\), necessarily length \(2m-1\). In particular a shorter common word was not maximal, proving the classification.

**Enumeration.** A letter-to-letter transition among unequal symbols contributes \(z\) for an ascent and \(z^{-1}\) for a descent. The displayed transfer matrix therefore counts exactly the characterized words after \(2m-2\) transitions at exponent zero. For \(q=2\), each starting symbol uniquely determines the alternating word, giving two.

For \(q=3\), direct inversion of the three-state transfer matrix yields
\[
F(t,z):=\mathbf1^{\mathsf T}(I-tM_3(z))^{-1}\mathbf1
=\frac{3+3t(z+z^{-1})+t^2(z^2+1+z^{-2})}{1-3t^2-t^3(z+z^{-1})}.
\]
Take the even powers of \(t\), substitute \(x=t^2\) and \(u=z^2\), and write \(B=(1-3x)^2-2x^3\). The even part is
\[
\frac{3-8x+3x^2+x(u+u^{-1})}{B-x^3(u+u^{-1})}.
\]
Its constant term in \(u\) follows from the formal-series identity
\[
\operatorname{CT}_u\frac{1}{B-x^3(u+u^{-1})}
=\frac{1}{\sqrt{B^2-4x^6}}
=\frac{1}{(1-3x)(1-x)\sqrt{1-4x}}.
\]
Using \(x(u+u^{-1})=(B-x^3(u+u^{-1}))x^{-2}-Bx^{-2}\) and simplifying gives
\[
\operatorname{CT}_z F(t,z)\big|_{\text{even }t}
=\frac{(1-x)^2/\sqrt{1-4x}-1}{x^2}.
\]
The coefficient of \(x^{m-1}\) is the indicated combination of three central binomial coefficients, by the usual series for \((1-4x)^{-1/2}\). Its leading coefficient relative to \(\binom{2m}{m}\) tends to \(4-2+1/4=9/4\); Stirling's formula gives the asymptotic. This finishes the proof.

## Verification

The accompanying standalone `checker.py` enumerates common scattered subsequences directly and tests maximality by every possible one-symbol insertion, then independently generates the predicted ascent/descent classes. All \(12\) cells with \(q\in\{2,3,4,5\}\) and \(m\in\{1,2,3\}\), plus three additional ternary cells \(m\in\{4,5,6\}\), give \(15\) matching exhaustive comparisons. An independent dynamic walk count matches the ternary binomial formula in each of \(40\) cells \(1\le m\le40\). The exact recorded output is `checker_output.txt`. These finite computations corroborate but do not prove the infinite theorem; the proof above supplies its general justification.

## Relationship to prior work

Buzzega, Conte, Kobayashi, Kurita, and Punzi (2025) systematically study the enumeration complexity of maximal common subsequences for arbitrary string families. Hirota and Sakai (2023) give algorithms for two-string maximal-subsequence enumeration, while Conte, Grossi, Punzi, and Uno (2023) describe a compact representation. Greenberg (2003) studies counts and bounds for longest common subsequences of arbitrary pairs. Their reviewed statements address general algorithms and global bounds, not the reversed-periodic pair's all-length equality of maximal and longest subsequences nor its ternary closed count. An integer sequence formed by the ternary formula also appears in OEIS A396530 as central-binomial second differences; the numerical sequence by itself is not claimed as newly discovered. The contribution is its explicit combinatorial interpretation and the structural classification for all alphabet sizes.

## Limitations

The result concerns two exact reverse-ordered repeated permutation blocks with equal repetition count, not arbitrary periodic words or arbitrary pairs of strings. It gives a closed elementary binomial expression only for the ternary case; other alphabet sizes are covered by the transfer-matrix formula. A search preview of a 2018 work on string analogies mentions specific reversed-periodic examples, but its full text was not accessible; unknown earlier structural classifications remain a residual originality risk. The finite checker cannot rule out errors beyond the tested ranges or certify originality. Independent scientific validation has not been performed.

## References

- N. Buzzega, A. Conte, Y. Kobayashi, K. Kurita, G. Punzi, *The Complexity of Maximal Common Subsequence Enumeration*, 2025, arXiv:2504.04757 (first public version 2025-04-07).
- H. Hirota and T. Sakai, *Efficient Algorithms for Enumerating Maximal Common Subsequences of Two Strings*, 2023, arXiv:2307.10552.
- A. Conte, R. Grossi, G. Punzi, and T. Uno, *A Compact DAG for Storing and Searching Maximal Common Subsequences*, ISAAC 2023, DOI:10.4230/LIPIcs.ISAAC.2023.21.
- R. I. Greenberg, *Computing the Number of Longest Common Subsequences*, 2003, arXiv:cs/0301034.
- R. I. Greenberg, *Bounds on the Number of Longest Common Subsequences*, 2003, arXiv:cs/0301030.
- OEIS A396530, central-binomial finite differences (numeric comparison only).
