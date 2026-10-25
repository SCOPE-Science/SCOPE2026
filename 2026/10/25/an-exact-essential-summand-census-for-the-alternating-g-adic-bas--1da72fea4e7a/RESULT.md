# An exact essential-summand census for the alternating \(g\)-adic basis

## Finding
For an integer base \(g\ge3\), define the two sets of positive integers whose base-\(g\) nonzero digits occur only in even, respectively only in odd, positions, and let \(A\) be their union. Let \(E_1=(A+A)\setminus((A\setminus\{1\})+(A\setminus\{1\}))\). Then for every integer \(k\ge1\),
\[
\bigl|E_1\cap[0,g^{2k})\bigr|=g^k-2^k+k+1.
\]
Indeed, the entire essentiality fiber below the cutoff is
\[
\{2,3\}\ \cup\ \{1+g^{2j}:1\le j<k\}\ \cup\
\left\{1+\sum_{i=0}^{k-1}c_i g^{2i+1}:0\le c_i<g,\ \max_i c_i\ge2\right\}.
\]
These three families are disjoint. Consequently the number of integers requiring the summand \(1\) has sharp leading coefficient \(1\) at the square-root scale and an explicit exponentially smaller correction along these cutoffs.

## Assumptions and scope
All summands are positive integers; repetitions are allowed, and representation existence is independent of their order. An integer belongs to \(E_1\) precisely when it has at least one two-summand representation from \(A\) and every such representation contains \(1\). A base-\(g\) digit occupies position \(r\) when it multiplies \(g^r\). The theorem holds for every integer \(g\ge3\) and every integer \(k\ge1\); it does not claim a corresponding formula for general digit partitions, larger summand number, or other indispensable summands.

## Proof
Write \(A_0\) for the positive even-position-supported integers and \(A_1\) for the positive odd-position-supported integers. They are disjoint; every member of \(A_1\) is divisible by \(g\). If \(n\in E_1\), it has the form \(n=1+b\) for a unique \(b\in A\).

First suppose \(b\in A_1\). The base-\(g\) units digit of \(n\) is \(1\); therefore a representation by two elements of \(A_1\) is impossible. A mixed pair \(A_0+A_1\) produces no carries because its two nonzero-digit positions are disjoint. Such a pair must consist exactly of \(1\) and \(b\). A representation by two members of \(A_0\), on the other hand, can create a nonzero digit at an odd position only through a carry from the preceding even position, and that carry is at most \(1\). Thus it is impossible if any odd-position digit of \(b\) is at least \(2\).

Conversely, suppose all odd-position digits of \(b\) lie in \(\{0,1\}\). Write them \(\varepsilon_i\) at position \(2i+1\). Choose two even-position-supported summands whose units-column digit sum is \(1+g\varepsilon_0\), and whose digit sum at each later even position \(2i\) is \(g\varepsilon_i\). Each requested sum is between \(0\) and \(2(g-1)\), since \(g\ge3\); it therefore splits into two valid base-\(g\) digits. Carries appear exactly at the designated odd positions, and both summands are positive because \(b>0\) forces at least one requested carry. This gives a representation omitting \(1\). Hence \(1+b\in E_1\) for \(b\in A_1\) exactly when some odd-position digit is at least \(2\).

Now suppose \(b\in A_0\), and let \(d\) be its units digit. If \(d=g-1\), adding \(1\) causes a carry into position \(1\). Whenever \(b>g-1\), the resulting \(n\) has the representation \(g+(b-(g-1))\), with the first term in \(A_1\), the second in \(A_0\), neither equal to \(1\). When \(b=g-1\), \(n=g\). For \(g\ge4\), its representation \(2+(g-2)\) avoids \(1\); for \(g=3\), only \(1+2\) is possible and \(n=3\) is essential.

Suppose instead \(d\le g-2\). Then \(n=1+b\) lies in \(A_0\), and its units digit is positive. No pair from \(A_1\) can sum to it because such sums are divisible by \(g\). No mixed pair can sum to it: the disjoint digit positions force carry-free addition, while its odd digits vanish. Any \(A_0+A_0\) representation also has no carries, since a carry out of an even position would create an odd digit \(1\). Consequently, if \(D_i\) are the even-position digits of \(n\), the number of ordered pairs of nonnegative \(A_0\)-supported integers summing to \(n\) is \(\prod_i(D_i+1)\); exactly two of these have a zero summand, except when \(n=0\), which is excluded. A representation by positive summands is therefore unique up to order precisely when the product is \(3\) or \(4\): there are then one or two positive ordered splits, forming one unordered pair (possibly equal). Since the units digit is positive, this happens precisely for \(n=2\), \(n=3\) when \(g\ge4\), and \(n=1+g^{2j}\) for \(j\ge1\). In these cases the unique positive unordered decomposition contains \(1\); for every other possibility there is a representation avoiding \(1\). The \(g=3\) carry case supplies the same \(n=3\).

Combining both cases yields the displayed disjoint description. Below \(g^{2k}\), the odd-position family allows \(g^k\) digit vectors in all and exactly \(2^k\) vectors with every digit in \(\{0,1\}\). There are \(k-1\) allowed indices \(j\) in the second family and two small exceptional integers. The total is \(g^k-2^k+(k-1)+2=g^k-2^k+k+1\). Since \(g>2\), the correction is \(o(g^k)\), proving the asymptotic assertion.

## Verification
The standalone standard-library script `verify.py` independently enumerates admissible summands, constructs all unordered two-summand representations below specified cutoffs, and compares the observed essentiality fiber—not just its size—with the explicit classification for bases \(3,4,5\) and three even-position blocks, and base \(6\) with two blocks. It is a finite consistency check, not the proof for arbitrary \(g,k\).

## Relationship to prior work
Tang, *Minimal asymptotic \(g\)-adic bases from arbitrary partitions* (arXiv:2610.23152v1, first posted 2026-10-16), establishes general minimality and a quantitative lower bound on \(E_a(x)\); its proof and corollaries do not provide the exact element-specific count here. Tang and Ling's 2018 treatment of minimal \(g\)-adic asymptotic bases addresses minimality and counterexamples for more general partitions, not the essentiality-fiber census. Counting all integers with multiple two-summand representations is a different invariant and does not recover the subset of integers for which \(1\) is indispensable. The present result identifies the complete fiber in the canonical balanced two-partition case, including its sharp constant and second-order correction.

## Limitations
The scope is the alternating two-class partition and the single summand \(1\), with strictly positive summands and base \(g\ge3\). The result neither establishes the same expression for other indispensable summands nor an asymptotic expansion for unrestricted real cutoffs. No claim of an independent assessment is made. The possibility of an unindexed equivalent digit-sum classification remains a literature risk.

## References
1. M. Tang, *Minimal asymptotic \(g\)-adic bases from arbitrary partitions*, arXiv:2610.23152v1 (first public 2026-10-16), https://arxiv.org/abs/2610.23152 ; full text https://arxiv.org/pdf/2610.23152 .
2. M. Tang and D.-R. Ling, *On asymptotic bases and minimal asymptotic bases*, arXiv:1810.10925 (2018), https://arxiv.org/abs/1810.10925 .
