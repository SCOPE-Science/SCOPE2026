# Sharp one-extra-symbol run-constrained deletion-shadow capacities

## Finding

For a \(q\)-symbol alphabet \(\Sigma_q=\{0,1,\ldots,q-1\}\), let \(D_t(w)\) be the **set of distinct** words produced by deleting exactly \(t\) positions of \(w\). A run is a maximal constant-letter block. For every \(q\ge2\), \(r\ge q\), and \(0\le t<q\),

\[
\max_{\substack{w\in\Sigma_q^{r+1}\\\operatorname{runs}(w)=r}}|D_t(w)|
=\binom{r+1}{t}-\binom{r-1}{t-1},
\]

where \(\binom{r-1}{-1}=0\). At the first alphabet-size deletion order, \(t=q\),

\[
\boxed{\max_{\substack{w\in\Sigma_q^{r+1}\\\operatorname{runs}(w)=r}}|D_q(w)|
=\binom{r+1}{q}-\binom{r-1}{q-1}-\max\{0,r-2q+1\}.}
\]

More precisely, let \(c_i=(i-1)\bmod q\), and let \(W_{q,r,j}=c_1\cdots c_jc_jc_{j+1}\cdots c_r\), with \(1\le j\le r\). For \(0\le t<q\), every \(W_{q,r,j}\) attains the stated maximum. For \(t=q\), its exact shadow size is

\[
|D_q(W_{q,r,j})|=\binom{r+1}{q}-\binom{r-1}{q-1}-(j-q)_+-(r-j-q+1)_+,
\]

where \((a)_+=\max\{a,0\}\). Among these canonical cyclic words, the maximizing double-run positions are precisely the integers between \(q\) and \(r-q+1\), irrespective of endpoint order.

## Assumptions and scope

Alphabet size \(q\) and run count \(r\) are integers with \(2\le q\le r\). Word length is exactly \(r+1\), so **one and only one** of its \(r\) runs has length two, and every other run has length one. Deletion count satisfies \(0\le t\le q\); all shadow cardinalities count output words, not deletion patterns. The optimization is over all \(q\)-ary words with exactly the prescribed number of runs; no restriction that every symbol appear is imposed. The optimum exists since this set is finite.

## Proof

**1. Reduction to cyclic run labels.** Fix a run-length vector of \(r\) positive integers totaling \(r+1\). Lemma 10 of Li–Wang–Fu [1] proves that replacing its run-symbol sequence by a cycle through \(q\) distinct letters cannot decrease the number of distinct \(t\)-deletion outputs, for every \(t\). This monotonicity holds with the run lengths fixed, not just for lengths divisible by the run count. We use this published lemma exactly in that form, for each possible location of the unique doubled run. Consequently a global maximum occurs among the words \(W_{q,r,j}\), \(1\le j\le r\). It remains to compute their shadows and optimize \(j\).

**2. Distinct-subsequence recurrence.** For a finite word \(v\) of length \(m\), set

\[
H_v(z)=\sum_{t=0}^{m}|D_t(v)|z^t.
\]

If an appended symbol \(a\) has no previous occurrence in \(v\), then \(H_{va}(z)=(1+z)H_v(z)\). Otherwise let \(p\) be its last occurrence position in \(v\), counted from one. Then

\[
H_{va}(z)=(1+z)H_v(z)-z^{m-p+1}H_{v_1\cdots v_{p-1}}(z).\tag{1}
\]

To prove (1), first count *all* distinct subsequences by retained length in \(F_v(y)=y^mH_v(1/y)\). The newly formed subsequences that end in \(a\) are obtained by appending \(a\) to a subsequence of \(v\); among these, the ones already present in \(v\) are exactly those already representable using the last occurrence at \(p\), i.e. subsequences of the prefix \(v_1\cdots v_{p-1}\) followed by \(a\). Thus \(F_{va}(y)=(1+y)F_v(y)-yF_{v_1\cdots v_{p-1}}(y)\). Multiplication by \(z^{m+1}\) with \(y=1/z\) yields (1). The degree-zero coefficient of every \(H_v\) is one.

**3. Truncation through deletion order \(q\).** Work modulo \(z^{q+1}\). Before the doubled letter, \(c_1\cdots c_j\) is periodic with repeat spacing \(q\). Each repeat after the first \(q\) positions contributes \(-z^q\) through (1), since the correcting polynomial has constant term one. The other terms are obtained from successive multiplication by \(1+z\). Hence

\[
H_{c_1\cdots c_j}(z)\equiv(1+z)^j-(j-q)_+z^q\pmod{z^{q+1}}.
\]

At position \(j+1\) the symbol \(c_j\) is repeated immediately, so (1) contributes the correction \(-zH_{c_1\cdots c_{j-1}}(z)\). The latter polynomial agrees with \((1+z)^{j-1}\) through degree \(q-1\). Multiplying this correction by the \(r-j\) subsequent factors \(1+z\) therefore contributes exactly \(-z(1+z)^{r-1}\) through degree \(q\).

For the first \(q-1\) original letters after the doubled run, any previous equal letter is separated by at least \(q+1\) positions because the duplication shifts its position. Their recurrence corrections vanish modulo \(z^{q+1}\). For later letters, beginning with the original letter at run \(j+q\), each repeat again has spacing exactly \(q\) and contributes \(-z^q\). There are \((r-j-q+1)_+\) such later letters. The earlier periodic prefix contributed \((j-q)_+\) corrections. We obtain the explicit congruence

\[
\boxed{H_{W_{q,r,j}}(z)\equiv(1+z)^{r+1}-z(1+z)^{r-1}
-\bigl((j-q)_++(r-j-q+1)_+\bigr)z^q\pmod{z^{q+1}}.}\tag{2}
\]

Extracting coefficients from (2) yields the claimed count for each \(0\le t\le q\). The two corrections from the cyclic repeats occur only at degree \(q\), so every \(j\) has the same size below that degree.

**4. Exact optimization at order \(q\).** For integer \(1\le j\le r\), the correction

\[
(j-q)_++(r-j-q+1)_+
\]

has minimum \(\max\{0,r-2q+1\}\). This follows either by considering whether \(q\le r-q+1\) or not, or by observing that the two positive parts have sum at least the positive part of their sum. Equality holds precisely for \(j\) lying between \(q\) and \(r-q+1\), inclusive; this interval may be traversed in either direction. Combining with step 1 proves the global optimum and the claimed canonical maximizing positions. \(\square\)

## Verification

The accompanying `verify.py` enumerates distinct subsequences directly as sets, independently of recurrence (1). It checks formula (2) for 540 canonical words, covering \(2\le q\le7\), \(q\le r\le\min(q+9,16)\), every doubled-run position, and every \(0\le t\le q\). It then exhaustively enumerates 40,680 words (all possible symbols for each run, with adjacent run labels different, and every doubled-run position), at \(q=2,2\le r\le10\), \(q=3,3\le r\le9\), and \(q=4,4\le r\le7\), and compares their maxima at all \(0\le t\le q\) with the closed formulas. Run with `python3 verify.py`; expected output includes `CANONICAL_OK 540` and `GLOBAL_EXHAUSTIVE_OK 40680`. Infinite generality is proved by the recurrence and the cited cyclic-reduction lemma, not by this finite search.

## Relationship to prior work

Li–Wang–Fu [1] establish cyclic monotonicity (their Lemma 10), a sharp maximizer when word length is a multiple of the run count (their Theorem 17), and a general upper bound otherwise (their Corollary 18). They expressly leave complete extremal characterization for nondivisible lengths open. The present theorem settles the natural first nondivisible family \(n=r+1\), through the first alphabet-repeat deletion order \(t=q\), and refines it with an exact doubled-run positional penalty. The cyclic monotonicity lemma is acknowledged as existing work, not a new result. Liron–Langberg [2] focus on the binary setting and divisible lengths for their sharp balanced construction. Mercier–Khabbazian–Bhargava [3] provide general subsequence-counting machinery and formulas for small fixed deletion orders; these do not state the all-alphabet extremal positioning law proved here.

## Limitations

The formula covers exactly one doubled run and deletion orders through \(q\). It does not characterize all possible optimal noncyclic words, nor longer run compositions, nor deletions beyond \(q\). Its global maximality uses the cyclic-operation lemma of [1]; the present proof does not reprove that cited lemma from first principles. An earlier equivalent classification not indexed in the inspected literature remains possible. The full text of [3] was not available in the current source-access channel; its abstract and bibliographic record were checked, but its internal theorems were not individually compared. No independent scientific audit has been performed.

## References

[1] H. Li, X. Wang, F.-W. Fu, *On the Number of Subsequences in the Nonbinary Deletion Channel*, arXiv:2601.06493, initially public 2026-01-10, https://arxiv.org/abs/2601.06493 ; full text https://arxiv.org/html/2601.06493v2 .

[2] Y. Liron, M. Langberg, *A Characterization of the Number of Subsequences Obtained via the Deletion Channel*, arXiv:1202.1644, https://arxiv.org/html/1202.1644v1 .

[3] H. Mercier, M. Khabbazian, V. K. Bhargava, *On the Number of Subsequences When Deleting Symbols From a String*, IEEE Transactions on Information Theory 54(7):3279–3285 (2008), https://doi.org/10.1109/TIT.2008.924730 .
