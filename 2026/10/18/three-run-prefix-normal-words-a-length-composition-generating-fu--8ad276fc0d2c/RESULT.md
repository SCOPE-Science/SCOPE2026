# Three-run prefix-normal words: a length-composition generating function and limiting density

## Finding

A binary word \(w\) is **prefix normal** (with respect to symbol \(1\)) when, for each integer \(1\le \ell\le |w|\), every contiguous factor of length \(\ell\) contains at most as many ones as the length-\(\ell\) prefix.

Let \(a_{n,m}\) count such words of length \(n\) having exactly \(m\) ones and **exactly three maximal one-runs**. Define \(t=xy\). The complete joint generating function is
\[
G(x,y)=\sum_{n,m\ge0}a_{n,m}x^ny^m
=\frac{x^2t^3\bigl[1+(1+x)(t+t^2+t^3)\bigr]}{(1-x)^3(1+x)(1-t)^3(1+t)^2(1+t+t^2)}.
\]
This is an identity of formal power series over the rational numbers. In particular, \(a_{n,m}=0\) for \(n<5\).

A word with three one-runs is prefix normal precisely when it has the unique decomposition
\[
w=1^a0^b1^c0^d1^e0^f,
\quad a,b,c,d,e\ge1,\quad f\ge0,
\]
with
\[
a\ge\max(c,e)\quad\text{and}\quad\bigl(d\ge b\text{ or }a\ge c+e\bigr).
\]
The total number of words of length \(n\) with exactly three one-runs and beginning in one is \(\binom n5\) for \(n\ge5\); hence the proportion among those words that are prefix normal satisfies
\[
\frac{\sum_m a_{n,m}}{\binom n5}=\frac7{24}+O(n^{-1}).
\]
The first total counts \(\sum_m a_{n,m}\), for \(n=5,6,\ldots,12\), are \(1,3,10,23,50,94,169,280\).

## Assumptions and scope

Words are finite, linear and labeled over \(\{0,1\}\). Runs are maximal consecutive occurrences of symbol \(1\); three runs implies three nonempty one-blocks separated by two nonempty zero-blocks. A nonempty prefix zero-block is impossible for a prefix-normal word containing a one; the terminal zero-block is allowed to be empty. No cyclic identifications or quotienting by reversal/complement are used. The indeterminates \(x,y\) mark total length and number of ones; equivalently, \(x,t\) mark zero and one counts.

## Proof

**Gap criterion.** For any word beginning in one with ones at positions \(1=p_1<p_2<\cdots<p_M\), put \(g_i=p_{i+1}-p_i\) for \(1\le i<M\). For an integer \(r\) with \(1\le r<M\), the shortest factor containing \(r+1\) consecutive ones has length \(1+\min_i\sum_{j=i}^{i+r-1}g_j\). The prefix contains \(r+1\) ones for the first time at length \(1+\sum_{j=1}^r g_j\). Consequently, prefix normality is equivalent to
\[
\sum_{j=1}^r g_j\le\sum_{j=i}^{i+r-1}g_j
\quad(1\le r<M,\ 1\le i\le M-r).
\]
Indeed, a violation produces a shorter factor containing \(r+1\) ones than the first prefix with that many ones, and every factor with more ones than its equally long prefix gives such a violation.

For \(w=1^a0^b1^c0^d1^e0^f\), the gap list has all entries one, except for an added \(b\) at gap index \(a\) and an added \(d\) at gap index \(a+c\). Its length is \(M-1\), with \(M=a+c+e\).

For \(r<a\), the initial sum contains no added gap and the inequalities hold. At \(r=a\), the initial sum contains \(b>0\); a block of \(a\) unit gaps in the middle or final one-run would contradict prefix normality. Therefore \(a\ge c\) and \(a\ge e\) are necessary. Under these two inequalities, a gap window of length \(r\) with \(a\le r<a+c\) contains either the first exceptional gap or the second; if it contains neither, it is a unit-only window of length at most \(\max(a-1,c-1,e-1)<a\), impossible. A window containing only the second gap occurs at some such \(r\) if and only if the number \(c+e-1\) of gaps after the first exceptional gap is at least \(a\), equivalently \(a<c+e\). If that window exists, its added weight is \(d\), so the inequalities at \(r=a\) require \(d\ge b\); otherwise there is no restriction on \(d\) relative to \(b\). For \(r\ge a+c\), every gap window contains both exceptional gaps: avoiding the first permits at most \(c+e-1\le a+c-1\) consecutive gaps, and avoiding the second permits at most \(a+c-1\). Thus the gap inequalities hold automatically in this last range. This proves the stated if-and-only-if run characterization, including the boundaries \(a=c\), \(a=e\), \(a=c+e\), and \(d=b\).

**Enumeration.** Let
\[
S_{\mathrm{sum}}(t)=\sum_{c,e\ge1}\sum_{a\ge c+e}t^{a+c+e}
=\frac{t^4}{(1-t)(1-t^2)^2},
\]
\[
S_{\mathrm{max}}(t)=\sum_{a\ge1}t^a\left(\sum_{c=1}^a t^c\right)^2
=\frac{t^3(1+t^2)}{(1-t)^3(1+t)(1+t+t^2)}.
\]
All positive zero-gap pairs \((b,d)\) have series \(x^2/(1-x)^2\), whereas pairs with \(d\ge b\ge1\) have series \(x^2/((1-x)(1-x^2))\). The arbitrary final zero-run contributes \(1/(1-x)\). Splitting the one-run lengths into \(a\ge c+e\) and \(\max(c,e)\le a<c+e\) yields
\[
G(x,y)=\frac{x^2}{1-x}\left[\frac{S_{\mathrm{sum}}(t)}{(1-x)^2}
+\frac{S_{\mathrm{max}}(t)-S_{\mathrm{sum}}(t)}{(1-x)(1-x^2)}\right],\qquad t=xy.
\]
Elementary rational simplification gives the displayed bivariate formula. This derivation counts every admissible \((a,b,c,d,e,f)\) exactly once.

**Asymptotics.** Setting \(y=1\) gives
\[
G(z,1)=\frac{z^5(1+z+2z^2+2z^3+z^4)}{(1-z)^6(1+z)^3(1+z+z^2)}.
\]
The coefficient of \((1-z)^{-6}\) at the pole \(z=1\) is \(7/24\); every other singularity on the unit circle has pole order at most three. Consequently, \(\sum_m a_{n,m}=\tfrac7{24}\binom n5+O(n^4)\). The unrestricted three-one-run words starting with one are counted by \(z^5/(1-z)^6\), giving \(\binom n5\); division proves the limit with \(O(n^{-1})\) error.

## Verification

The standalone standard-library program `verify.py` independently tests the run criterion against direct sliding-window prefix-normality for all \(6^5=7776\) positive five-run-parameter tuples with entries at most six; it also tests all admissible parameterizations at lengths \(5\) through \(16\), including the terminal zero-run. The program expands the rational expression by integer coefficient recurrences (without symbolic algebra) and matches every length-and-one-count coefficient against an independently enumerated parameter count for \(5\le n\le26\). Finally it checks that all words with three one-runs beginning in one number \(\binom n5\). The output begins `VERIFY_OK`. These finite checks corroborate, but do not replace, the all-length combinatorial proof.

## Relationship to prior work

Burcsi, Fici, Lipták, Ruskey and Sawada (2014) introduced efficient generation of prefix-normal words using their bubble-language structure; their discussion of critical prefixes does not provide a run-count-refined enumeration. Their 2014 exposition of the subject develops prefix-normal forms and run-based membership filters, again without this distribution. Their later preprint (2016), Proposition 7 and Lemma 8, provides the general gap/position characterization that underlies the first part of the present proof; the general criterion is **not** claimed to be new here. Proposition 16 there derives rational generating functions for *fixed one-counts* up to six, and explains the general rationality of fixed-density enumerators. Fixed density does not fix the number of one-runs, and those formulas do not supply this full bivariate three-run enumerator or its \(7/24\) asymptotic proportion. The new contribution is the complete explicit run-count-conditioned enumeration, including unbounded one-count and its limiting constant.

## Limitations

The formula concerns exactly three one-runs, not arbitrary run count. The asymptotic comparison conditions on the first symbol being one; it is not a limiting fraction among all binary words or among all prefix-normal words. The novelty search does not guarantee that an equivalent closed form has never appeared, especially in unindexed sources.

## References

1. P. Burcsi, G. Fici, Zs. Lipták, F. Ruskey, J. Sawada, *On Combinatorial Generation of Prefix Normal Words*, arXiv:1401.6346, first submitted 24 January 2014. https://arxiv.org/abs/1401.6346
2. P. Burcsi, G. Fici, Zs. Lipták, F. Ruskey, J. Sawada, *Normal, Abby Normal, Prefix Normal*, arXiv:1404.2824, first submitted 1 April 2014. https://arxiv.org/abs/1404.2824
3. P. Burcsi, G. Fici, Zs. Lipták, F. Ruskey, J. Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017, first submitted 28 November 2016, especially Proposition 7, Lemma 8 and Proposition 16. https://arxiv.org/abs/1611.09017
