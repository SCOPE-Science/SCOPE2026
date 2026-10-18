# Fibonacci-denominator Farey adjacency has no limiting order density

## Finding

For an integer \(N\ge 1\), let \(\mathcal F_N\) be the **full** Farey sequence of order \(N\), including \(0/1\) and \(1/1\), and put \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\). Let \(\mathscr D=\{F_j:j\ge2\}=\{1,2,3,5,8,\ldots\}\) as a set of distinct integers. Define \(C(N)\) to be the number of adjacent pairs in \(\mathcal F_N\) **whose two denominators both belong to** \(\mathscr D\). Let
\[
E(X)=\#\{1\le N\le X:C(N)=2\}\quad (X\in\mathbb Z_{\ge1}).
\]

**Theorem.** For every integer \(N\ge8\), let \(k\ge6\) be the unique index such that \(F_k\le N<F_{k+1}\). Then
\[
C(N)=2\quad\Longleftrightarrow\quad F_k+F_{k-2}\le N<F_{k+1},
\]
and the following exact counting law holds:
\[
\boxed{\ E(N)=\max\{F_{k-2},\ N-F_k+1\}.\ }
\]
In particular,
\[
\boxed{\liminf_{X\to\infty}\frac{E(X)}X=\frac{5-\sqrt5}{10},\qquad
\limsup_{X\to\infty}\frac{E(X)}X=\frac{3-\sqrt5}{2}.}
\]
Thus the set of Farey orders having exactly two Fibonacci-denominator adjacent pairs **has no natural density**. Both limits are exact and distinct.

## Assumptions and scope

Only positive integer orders \(N\) are considered. Adjacent means consecutive in the *unrestricted full* Farey sequence, not consecutive after deleting fractions with inadmissible denominators. Fibonacci denominators are values, not index labels: the duplicate value \(F_1=F_2=1\) is counted only once. An adjacent fraction pair is counted once in its increasing order. The explicit law is asserted for \(N\ge8\); the initial verification \(E(7)=3\) is used in the induction.

## Proof

**1. The denominator-pair bijection.** The classical Farey-neighbor criterion states that a positive ordered denominator pair \((u,v)\), with \(u,v\le N\), arises from exactly one pair of consecutive elements of \(\mathcal F_N\) if and only if \(\gcd(u,v)=1\) and \(u+v>N\). For completeness: Bézout's identity gives unique numerators in the endpoint ranges for \(uc-av=1\); the mediant has denominator \(u+v\), so no fraction of order \(N\) can lie strictly between precisely when \(u+v>N\). Conversely consecutive Farey neighbors have cross-determinant one and denominator sum exceeding \(N\). The endpoints with denominator \(1\) are included in this correspondence. Consequently
\[
C(N)=\sum_{u,v\in\mathscr D\cap[1,N]}
\mathbf1_{\gcd(u,v)=1}\mathbf1_{u+v>N}.
\]

**2. Sharp threshold for two neighbors.** Fix \(k\ge6\) and \(F_k\le N<F_{k+1}\). The available distinct Fibonacci denominators are exactly \(F_2,F_3,\ldots,F_k\). Equal denominators larger than one cannot be coprime. Among pairs of **distinct** denominators, the largest sum not using \(F_k\) is \(F_{k-1}+F_{k-2}=F_k\le N\). Thus every coprime pair whose sum exceeds \(N\) must use \(F_k\). The largest two possible sums involving \(F_k\) are \(F_k+F_{k-1}=F_{k+1}\) and \(F_k+F_{k-2}\).

The Fibonacci gcd identity \(\gcd(F_i,F_j)=F_{\gcd(i,j)}\) shows that both \((F_k,F_{k-1})\) and \((F_k,F_{k-2})\) are coprime, since their index gcds are \(1\) and \(\gcd(k,2)\), and \(F_1=F_2=1\). The two orders of the first pair always contribute exactly two neighbors, because their sum is \(F_{k+1}>N\). The two orders of the second pair contribute if and only if \(N<F_k+F_{k-2}\). Every remaining admissible pair has smaller sum. This proves the threshold equivalence and the exact number \(F_{k+1}-F_k-F_{k-2}=F_{k-3}\) of orders with \(C(N)=2\) in the block.

**3. Exact counting.** Directly from the first seven Farey sequences, \(C(N)=2\) for \(N=2,4,7\), and for no other \(1\le N\le7\), so \(E(7)=3=F_4\). Suppose inductively that \(E(F_k-1)=F_{k-2}\), starting at \(k=6\). The previous paragraph gives
\[
E(F_{k+1}-1)=E(F_k-1)+F_{k-3}
=F_{k-2}+F_{k-3}=F_{k-1}.
\]
Within the block, the count is constant until \(N=F_k+F_{k-2}-1\), then rises by one at each subsequent order. Hence
\[
E(N)=F_{k-2}+\max\{0,N-F_k-F_{k-2}+1\}
=\max\{F_{k-2},N-F_k+1\}.
\]

**4. Distinct limiting frequencies.** Within each block, \(E(N)/N=F_{k-2}/N\) decreases before the threshold, and \(E(N)/N=1-(F_k-1)/N\) increases afterwards. The minimum is therefore at \(N=F_k+F_{k-2}-1\); the maximum is attained at one of the block ends. Standard Fibonacci ratios \(F_{k-j}/F_k\to\phi^{-j}\), with \(\phi=(1+\sqrt5)/2\), give the lower limiting endpoint
\[
\frac{F_{k-2}}{F_k+F_{k-2}-1}\longrightarrow
\frac1{\phi^2+1}=\frac{5-\sqrt5}{10}.
\]
At both ends, \(E(F_k)/F_k\to\phi^{-2}\) and \(E(F_{k+1}-1)/(F_{k+1}-1)\to\phi^{-2}=(3-\sqrt5)/2\). These bounds apply to every order in every sufficiently large block, establishing both global extremal limits.

## Verification

Run `python3 verify_farey_fibonacci.py` using Python 3.9 or later and no third-party packages. The verifier independently generates denominators of all consecutive fractions of each full Farey sequence through order \(450\), checks their counts against coprime denominator-pair enumeration, and checks the exact threshold/counting formula for every order through \(15{,}000\). The actual run printed `FAREY_FIBONACCI_EXACT_REGRESSION_OK full_farey=450 gcd_pairs=15000`. These finite tests corroborate, but do not replace, the proof for all integers \(N\ge8\).

## Relationship to prior work

The standard denominator-sum Farey criterion and Fibonacci strong-divisibility identity are the inputs. Alladi's 1975 paper constructs a *different* sequence of fractions whose **numerators and denominators** are Fibonacci values, and studies its symmetries; it does not classify consecutive pairs of the full Farey sequence with both denominators Fibonacci. Boca–Cobeli–Zaharescu (2002) and Cobeli–Zaharescu (2005) prove spacing and denominator distributions for **subsequences** restricted by parity, not the exact Fibonacci-value restriction while retaining full Farey adjacency. The OEIS entry A207524 counts fractions relative to a consecutive-Fibonacci quotient, a distinct statistic. Their stated results do not imply the present exact two-neighbor threshold or failure of natural order density without an additional new argument.

## Limitations

The result only characterizes the event \(C(N)=2\), not the full distribution of \(C(N)\) or finer gap statistics. The criterion and exact formula are proved for all \(N\ge8\), while finite tests stop at their specified bounds. Earlier unindexed literature might contain an equivalent consequence of classical Farey and Fibonacci identities. The present scientific review is not independent validation.

## References

1. K. Alladi, “A Farey Sequence of Fibonacci Numbers,” *The Fibonacci Quarterly* **13** (1975), no. 1, pp. 1–10. https://www.fq.math.ca/Scanned/13-1/alladi1.pdf (printed February 1975; exact day not established).
2. F. P. Boca, C. Cobeli and A. Zaharescu, “On the Distribution of the Farey Sequence with Odd Denominators,” arXiv:math/0201046, first submitted 2002-01-07. https://arxiv.org/abs/math/0201046
3. C. Cobeli and A. Zaharescu, “A Density Theorem on Even Farey Fractions,” arXiv:math/0511362, first submitted 2005-11-14. https://arxiv.org/abs/math/0511362
4. OEIS A207524, “Number of rational numbers ... greatest quotient of consecutive Fibonacci numbers ...,” https://oeis.org/A207524 (related, but different, Farey statistic).
