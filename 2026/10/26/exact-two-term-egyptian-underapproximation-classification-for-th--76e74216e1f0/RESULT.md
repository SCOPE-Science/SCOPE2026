# Exact two-term Egyptian underapproximation classification for the first-denominator-four interval

## Finding

Let \(I_4=(1/4,1/3]\). For every \(\theta\in I_4\), the greedy two-term Egyptian underapproximation is \(1/4+1/a\), where the unique integer \(a\ge13\) is determined by

\[
\theta\in J_a:=\left(\frac14+\frac1a,\;\frac14+\frac1{a-1}\right].
\]

A two-term underapproximation is a sum \(1/x+1/y<\theta\) with integers \(2\le x\le y\); it is best if its sum is maximal among all such pairs.

The greedy pair \((4,a)\) is **not best** exactly in the following six cases, and then exactly on the indicated upper subinterval:

| \(a\) | Exact failure interval within \(J_a\) |
|---:|---|
| \(14\) | \((13/40,\;1/4+1/13]\) |
| \(17\) | \((13/42,\;1/4+1/16]\) |
| \(25\) | \((16/55,\;1/4+1/24]\) |
| \(38\) | \((18/65,\;1/4+1/37]\) |
| \(47\) | \((19/70,\;1/4+1/46]\) |
| \(114\) | \((22/85,\;1/4+1/113]\) |

The greedy pair is best but **not uniquely best** exactly when

\[
a\in\{20,24,28,30,36,56,60,80,132,180,252,380\}.
\]

For every other \(a\ge13\), and every \(\theta\in J_a\), the greedy pair is the unique best two-term underapproximation. At \(a=60\), there are two distinct competing pairs, \((5,15)\) and \((6,10)\), and all three pairs \((4,60),(5,15),(6,10)\) give the same sum \(4/15\).

## Assumptions and scope

The domain is the full real interval \(I_4=(1/4,1/3]\), not only rational \(\theta\). Denominators are positive integers, the two terms are allowed to repeat, and the pair is ordered as \(x\le y\). The underapproximation inequality is strict. The claim concerns exactly two terms and does not assert a result for three or more terms or for other first-denominator intervals.

## Proof

For \(\theta\in I_4\), the first greedy denominator is \(4\). The greedy rule gives \(1/a<\theta-1/4\le1/(a-1)\), so \(a\ge4\cdot3+1=13\) and \(\theta\in J_a\).

Suppose a distinct pair \((x,y)\), with \(2\le x\le y\), can tie or exceed the greedy sum while remaining a valid underapproximation. Then

\[
\frac14+\frac1a\le\frac1x+\frac1y<\theta\le\frac14+\frac1{a-1}.
\]

Nathanson's necessary-condition lemma for two-term underapproximations therefore gives

\[
5\le x\le7\le y<\frac{4x}{x-4}.
\]

This leaves exactly 21 pairs: \((5,y)\) for \(7\le y\le19\), \((6,y)\) for \(7\le y\le11\), and \((7,y)\) for \(7\le y\le9\). For each pair define

\[
A(x,y)=\left\lceil\left(\frac1x+\frac1y-\frac14\right)^{-1}\right\rceil.
\]

By the defining ceiling inequalities, its sum lies in \([1/4+1/A,\;1/4+1/(A-1))\), so it can compete only in the greedy interval with \(a=A(x,y)\). The complete exact enumeration is:

| \(A(x,y)\) | Candidate pair(s) \((x,y)\) | Candidate sum(s) |
|---:|---|---|
| \(11\) | \((5, 7)\) | \(12/35\) |
| \(14\) | \((5, 8)\) | \(13/40\) |
| \(17\) | \((5, 9)\), \((6, 7)\) | \(14/45\), \(13/42\) |
| \(20\) | \((5, 10)\) | \(3/10\) |
| \(24\) | \((6, 8)\) | \(7/24\) |
| \(25\) | \((5, 11)\) | \(16/55\) |
| \(28\) | \((7, 7)\) | \(2/7\) |
| \(30\) | \((5, 12)\) | \(17/60\) |
| \(36\) | \((6, 9)\) | \(5/18\) |
| \(38\) | \((5, 13)\) | \(18/65\) |
| \(47\) | \((5, 14)\) | \(19/70\) |
| \(56\) | \((7, 8)\) | \(15/56\) |
| \(60\) | \((5, 15)\), \((6, 10)\) | \(4/15\), \(4/15\) |
| \(80\) | \((5, 16)\) | \(21/80\) |
| \(114\) | \((5, 17)\) | \(22/85\) |
| \(132\) | \((6, 11)\) | \(17/66\) |
| \(180\) | \((5, 18)\) | \(23/90\) |
| \(252\) | \((7, 9)\) | \(16/63\) |
| \(380\) | \((5, 19)\) | \(24/95\) |

The row \(A=11\) is outside the allowed range \(a\ge13\). Among the remaining rows, the sums equal the greedy sum exactly for \(a\in\{20,24,28,30,36,56,60,80,132,180,252,380\}\); these give ties for every \(\theta\in J_a\), and the table contains no strictly larger candidate at any of those values.

The remaining possible denominators are \(14,17,25,38,47,114\). Their least candidate sums are respectively \(13/40,13/42,16/55,18/65,19/70,22/85\). Each is strictly above its greedy sum and below the upper endpoint of its \(J_a\). A candidate of sum \(C\) is a valid strict improvement precisely when \(\theta>C\). This gives the six failure intervals above, with equality at the left endpoint excluded because the underapproximation must be strictly less than \(\theta\). Every other denominator has no candidate sum at least as large as the greedy sum. The necessary-condition lemma proves that no unlisted competitor can tie or improve it, completing the classification.

## Verification

The standalone file `verify.py` uses only Python's standard library and exact rational arithmetic. It enumerates the 21 admissible pairs, recomputes every ceiling value, checks the 12 tie denominators and 6 strict-failure denominators, and verifies the six exact thresholds and their endpoint inequalities. Running `python3 verify.py` prints `VERIFY_OK`.

The infinite-domain conclusion follows from the cited necessary-condition lemma plus the exhaustive finite candidate set; the verifier alone is not used as an infinite proof. No independent audit has been performed.

## Relationship to prior work

Nathanson gives the general necessary-condition bound and explicitly classifies the first-denominator-two and first-denominator-three intervals. The present result is the next complete all-real interval classification, with the exact candidate table for first denominator four. Chu proves broad rational-number criteria in terms of \(\Upsilon(p,q)\) and includes a non-greedy example at \(\theta=5/16\), which is one instance of the failure region here; those results do not state the complete all-real interval partition above. Kovač proves a measure-zero theorem for eventual greediness and a lower bound on non-greedy sets for large first denominators, not this finite exact classification.

## Limitations

This is a complete two-term classification only on \(I_4\). The candidate-bound method is prior work; the contribution is its explicit exact specialization to the full first-denominator-four interval. It does not settle the classification for any \(I_a=(1/a,1/(a-1)]\) with \(a\ge5\), nor does it address best underapproximations with three or more terms. The novelty assessment is based on the primary sources inspected and a semantic search of the available mathematical-results index; an unindexed equivalent table remains a residual risk.

## References

1. M. B. Nathanson, *Underapproximation by Egyptian fractions*, arXiv:2202.00191 (first public version 2022-02-01), especially the two-term competitor lemma and the explicit classifications for first denominators two and three; published in *Journal of Number Theory* 242 (2023), 208–234.
2. H. V. Chu, *A Threshold for the Best Two-term Underapproximation by Egyptian Fractions*, arXiv:2306.12564v2 (2024); *Indagationes Mathematicae* 35 (2024), 350–375.
3. V. Kovač, *On Eventually Greedy Best Underapproximations by Egyptian Fractions*, arXiv:2406.07218v3 (first public version 2024-06-11); *Journal of Number Theory* 268 (2025), 39–48.
