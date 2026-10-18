# Exact palindrome-length enumerator and Gaussian law for alternating binary words

## Finding
Let \(W_n\) be the length-\(n\) prefix of \(010101\cdots\). Let \(P_n(t)\) enumerate **distinct nonempty palindromic scattered subsequence words** by length, so \(P_n(t)=\sum_u t^{|u|}\) with each qualifying word counted once. For all \(n\ge0\), the complete length distribution is given by
\[
\sum_{n\ge0}P_n(t)z^n=\frac{tz(1+z)(1+tz^2)}{(1-z)(1-t^2z^2(1+z^2))}.
\]
For \(n\ge1\), choose a distinct nonempty palindromic scattered subsequence uniformly and let \(X_n\) be its length. Set \(\alpha=(1+1/\sqrt5)/2\) and \(\beta=2/(5\sqrt5)\). Then
\[
\mathbb E[X_n]=\alpha n+O(1),\qquad \operatorname{Var}(X_n)=\beta n+O(1),\qquad
\frac{X_n-\alpha n}{\sqrt{\beta n}}\ \xrightarrow{d}\ \mathcal N(0,1).
\]
Numerically, \(\alpha=0.7236067977499789\ldots\) and \(\beta=0.1788854381999832\ldots\).

## Assumptions and scope
A scattered subsequence of a finite word is obtained by selecting strictly increasing positions. A palindrome equals its reversal. Multiple choices of embedding positions producing the same palindrome count only **once**. The generating function is an identity of formal power series in \(z,t\), with \(P_0(t)=0\). The probabilistic assertions use the uniform distribution over **distinct** nonempty palindromic subsequence words, not a distribution over embeddings. No random input word is assumed.

## Proof
**Greedy embedding lemma.** For a nonempty binary word \(u=u_1\cdots u_m\), let \(C(u)\) be the last selected position (one-based) in its earliest greedy embedding into \(010101\cdots\). The first occurrence of symbol zero is at position one, and that of symbol one is at position two. After an embedded symbol, an unequal next symbol lies one position later, while an equal symbol lies two positions later. Therefore
\[
C(u)=m+[u_1=1]+\sum_{i=1}^{m-1}[u_i=u_{i+1}].
\]
The greedy construction is optimal by induction on the next matched symbol, so \(u\) is a scattered subsequence of \(W_n\) exactly when \(C(u)\le n\).

**Classifying palindromes.** Every binary palindrome of length at least two is uniquely either \(vv^R\) or \(vcv^R\), with a nonempty half-word \(v\), and, in the odd case, middle symbol \(c\in\{0,1\}\). Set \(r=|v|\), \(b=[v_1=1]\), and \(e=\sum_{i=1}^{r-1}[v_i=v_{i+1}]\). Then
\[
C(vv^R)=2r+b+2e+1,\qquad
C(vcv^R)=2r+1+b+2e+2[c=v_r].
\]
For fixed \(r,b,e\), precisely \(\binom{r-1}{e}\) half-words \(v\) occur: choose which of the \(r-1\) adjacent transitions are equal. In the odd case the two middle-symbol choices contribute a factor \(1+z^2\). The single-letter palindromes have greedy endpoints one and two. Consequently, summing \(t^{|u|}z^{C(u)}\) over all nonempty palindromes gives
\[
 tz(1+z)+\frac{t^2z^3(1+z)}{1-t^2z^2(1+z^2)}
 +\frac{t^3z^3(1+z)(1+z^2)}{1-t^2z^2(1+z^2)}
 =\frac{tz(1+z)(1+tz^2)}{1-t^2z^2(1+z^2)}.
\]
A palindrome with greedy endpoint \(C\) occurs in precisely those prefixes with \(n\ge C\). Multiplying the endpoint series by \(1/(1-z)\) proves the displayed bivariate identity.

**Limit law.** Split into even and odd prefix lengths using \(v=z^2\):
\[
 \sum_{k\ge0}P_{2k}(t)v^k=\frac{2tv(1+tv)}{(1-v)(1-t^2v(1+v))},\qquad
 \sum_{k\ge0}P_{2k+1}(t)v^k=\frac{t(1+v)(1+tv)}{(1-v)(1-t^2v(1+v))}.
\]
Near \(t=1\), both rational functions have a unique simple dominant pole \(v=R(t)\), where \(R(t)\) is the analytic solution near \(R(1)=(\sqrt5-1)/2\) of \(t^2R(t)(1+R(t))=1\). The other two poles, at \(v=1\) and the negative root of the quadratic, have strictly larger modulus at \(t=1\), so this separation persists in a complex neighborhood. Residue extraction gives, uniformly near \(t=1\), for each parity \(j\in\{0,1\}\),
\[
 P_{2k+j}(t)=A_j(t)R(t)^{-k}(1+O(\theta^k)),
\]
for some \(0<\theta<1\), with analytic nonvanishing amplitudes
\[
 A_0(t)=\frac{2(1+tR(t))}{t(1-R(t))(1+2R(t))},\quad
 A_1(t)=\frac{(1+R(t))(1+tR(t))}{tR(t)(1-R(t))(1+2R(t))}.
\]
Write \(t=e^s\). The normalized moment-generating function is \(\mathbb E[e^{sX_n}]=P_n(e^s)/P_n(1)\); hence its logarithm has the form \(n h(s)+O(1)\), uniformly for complex \(s\) near zero, with an analytic \(O(1)\) correction and
\[
 h(s)=-\frac12\log\frac{R(e^s)}{R(1)}.
\]
Differentiating \(e^{2s}R(e^s)(1+R(e^s))=1\) gives
\[
 h'(0)=\frac{1+R(1)}{1+2R(1)}=\frac{1+1/\sqrt5}{2}=\alpha,\quad
 h''(0)=\frac{2R(1)(1+R(1))}{(1+2R(1))^3}=\frac{2}{5\sqrt5}=\beta>0.
\]
Analytic differentiation of the bounded correction gives the mean and variance assertions. The characteristic functions of the centered and scaled \(X_n\) converge to \(\exp(-u^2/2)\) by Taylor-expanding \(h(iu/\sqrt{\beta n})\); the continuity theorem proves the normal limit.

## Verification
The standalone `verify.py` performs three checks: direct enumeration of every nonempty position subset of \(W_n\) for \(1\le n\le17\) and deduplication of resulting palindrome words; an independent polynomial recurrence extracted from the displayed rational identity matched against the half-word counting formula up to \(n=75\); and specialization at \(t=1\) checked against the known Fibonacci formulas for alternating binary words through \(n=75\). The finite checks corroborate the infinite proof but do not replace its analytic arguments. Run with `python3 verify.py` (standard library only).

## Relationship to prior work
Mahalingam and Pandoh (arXiv:2108.02729v1, 2021) study counts of distinct scattered palindromes and prove Fibonacci-type extremal bounds, including exact **total counts** for alternating binary words. Specializing this theorem at \(t=1\) recovers those total counts; a total-count formula alone does not determine the distinct-palindrome length distribution, the two-parameter rational generating function, or the Gaussian typical-length law. Müllner and Ryzhikov (arXiv:1901.07502, 2019) treat longest palindromic subsequences and related questions, rather than the distribution over all distinct palindromic words. The full text of the first paper and relevant introductory material of the second were compared for the same definitions and logical coverage.

## Limitations
Only binary alternating prefixes are covered. The theorem does not classify palindrome counts for arbitrary binary words, palindromic factors, occurrences with multiplicity, or the longest-palindrome statistic. The exact length enumerator gives asymptotic moments and a weak Gaussian limit, not a local limit theorem or a uniform large-deviation estimate. A previously unindexed equivalent calculation remains a possible priority risk; the mathematical statement itself is independently derived and directly checkable.

## References
- K. Mahalingam and P. Pandoh, *Counting scattered palindromes in a finite word*, arXiv:2108.02729v1 (first public 2021-08-05), https://arxiv.org/abs/2108.02729.
- C. Müllner and A. Ryzhikov, *Palindromic Subsequences in Finite Words*, arXiv:1901.07502 (2019), https://arxiv.org/abs/1901.07502.
- P. Flajolet and R. Sedgewick, *Analytic Combinatorics*, Cambridge University Press (2009), Chapters IV and IX (simple poles and central-limit transfer methodology).
