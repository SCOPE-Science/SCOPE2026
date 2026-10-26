# Exact threefold coverage loss after deleting a digit class from a minimal additive basis

## Finding
For every integer \(g\ge4\) and \(k\ge1\), put \(W_r=\{3j+r:j\in\mathbb Z_{\ge0}\}\), for \(r=0,1,2\). Let \(A_g(W)\) be the set of **positive** integers whose nonzero base-\(g\) digits occur only in \(W\), and define \(B_g=A_g(W_0)\cup A_g(W_1)\). For the threefold sumset \(3B_g=\{a+b+c:a,b,c\in B_g\}\), one has
\[
\boxed{\#(3B_g\cap[0,g^{3k}))=(2g^2-g)^k+(3g-2)^k-(2g-1)^k-\binom{k+2}{2}.}
\]
In particular \(\#(3B_g\cap[0,g^{3k}))\sim (2g^2-g)^k\) and the precise power-law exponent along these cutoffs is \(\theta_g=\log_{g^3}(2g^2-g)<1\). The omitted class is \(A_g(W_2)\). In contrast, the full set \(\bigcup_{r=0}^2 A_g(W_r)\) is a minimal asymptotic basis of order three by Tang's theorem.

## Assumptions and scope
The base \(g\) and block count \(k\) are integers with \(g\ge4\), \(k\ge1\). All summands are strictly positive; zero is never a member of \(B_g\). The half-open interval \([0,g^{3k})\) contains integers. No claim is made about an exact formula at arbitrary cutoffs or for irregular position partitions.

## Proof
Put \(H=g^3\). Every \(0\le n<H^k\) has unique block expansion \(n=\sum_{j=0}^{k-1}t_jH^j\) with \(0\le t_j<H\). An integer from \(B_g\) uses either only the first (\(W_0\)) or only the second (\(W_1\)) base-\(g\) position in each block; the third is zero. For three summands, let \(q\in\{0,1,2,3\}\) be the number using \(W_0\). In block \(j\), the total digit contribution has the form \(s_j+gv_j\) with \(0\le s_j\le q(g-1)\) and \(0\le v_j\le(3-q)(g-1)\). Since \(s_j+gv_j\le3g(g-1)<g^3=H\), **no carry crosses a block boundary**. Conversely, every assignment of these block totals can be decomposed into digit values of the assigned \(q\) and \(3-q\) summands, if zeros are permitted.

For \(q\ge1\), the attainable one-block totals form a full interval \([0,(g-1)(q+g(3-q))]\). Indeed, the length of the \(s_j\)-interval is at least \(g\), so the intervals obtained for successive \(v_j\) overlap or touch. These intervals, for \(q=2,3\), are contained in the one for \(q=1\):
\[
T_1=\{0,1,\ldots,2g^2-g-1\},\qquad |T_1|=2g^2-g.
\]
For \(q=0\), the one-block totals are
\[
T_0=\{0,g,2g,\ldots,3g(g-1)\},\qquad |T_0|=3g-2.
\]
Their intersection consists of \(0,g,\ldots,2(g-1)g\) and has cardinality \(2g-1\). Consequently, **allowing zero summands**, the reachable \(k\)-block words are \(T_1^k\cup T_0^k\), of cardinality
\[
(2g^2-g)^k+(3g-2)^k-(2g-1)^k.
\]

It remains to impose positivity of *all three* summands. We use the elementary digit-allocation fact: if \(m\) summands have the same permitted position class, and the prescribed digit sums in the available positions lie between zero and \(m(g-1)\), then all \(m\) summands can be positive if and only if the sum of their prescribed digit sums is at least \(m\). The necessity is immediate. For sufficiency, distribute one unit in an available digit position to each of the \(m\) summands, then allocate remaining units subject to per-position capacity \(g-1\); such an allocation is possible because the total capacity in each column is \(m(g-1)\). Equivalently, fill the \(m\) digit rows column by column, always giving first units to previously empty rows.

For a word in \(T_1^k\), uniquely write \(t_j=gb_j+r_j\) where \(0\le r_j<g\) and \(0\le b_j\le2(g-1)\). Set \(B=\sum_j b_j\) and \(R=\sum_j r_j\). If \(B\ge2\) and \(R\ge1\), a representation using one \(W_0\) summand (with digit sums \(r_j\)) and two \(W_1\) summands (with digit sums \(b_j\)) has all summands positive by the allocation fact. If \(B=1\), choose all three summands from \(W_0\): every \(t_j\le 2g-1\le3(g-1)\), while \(\sum_j t_j\ge g\ge3\). If \(B\ge3\) and \(R=0\), choose all three summands from \(W_1\), whose block digit sums are \(b_j\le2(g-1)\) with total at least three. If \(B=2\) and \(R=0\), instead choose all three summands from \(W_0\): every \(t_j\le2g\le3(g-1)\) and their total is \(2g\ge3\).

Finally, if \(B=0\), every \(t_j=r_j<g\), so all three summands must come from \(W_0\). This is possible precisely when \(R\ge3\). Hence the **only** elements of \(T_1^k\) that are not sums of three positive members of \(B_g\) are the \(k\)-tuples \((r_0,\ldots,r_{k-1})\) of nonnegative integers with \(\sum_j r_j\le2\). Their number is \(\binom{k+2}{2}\), since \(g\ge4\) makes the individual upper bound irrelevant. For a word of \(T_0^k\setminus T_1^k\), at least one quotient \(t_j/g\) exceeds \(2(g-1)\); hence its total \(W_1\)-digit count is at least \(2g-1\ge3\), making three positive \(W_1\) summands possible. There are no additional exceptions. Subtracting the binomial count from the union formula proves the theorem.

Since \(3g-2<2g^2-g\) and \(2g-1<2g^2-g\) for \(g\ge4\), the leading term yields the stated asymptotic and exponent. Finally \(2g^2-g<g^3\), so this exponent is strictly less than one. \(\square\)

## Verification
Run \(\texttt{python3 verify.py}\), using only the Python standard library. The code independently constructs \(B_g\) by testing base-\(g\) digit support, enumerates unordered triples including repeats, and compares the resulting exact count with the formula for \((g,k)=(4,1),(4,2),(4,3),(5,1),(5,2),(6,1),(6,2),(7,1),(7,2)\). The recorded execution returned \(\texttt{CERTIFICATE\_OK}\) for all nine cases. Finite verification is corroboration, not a substitute for the universal proof.

## Relationship to prior work
Min Tang, *Minimal asymptotic \(g\)-adic bases from arbitrary partitions*, arXiv:2610.23152v1 (first posted 2026-10-16), proves that the complete union over all three infinite digit-position classes is a minimal asymptotic basis when \(g>3\), as well as qualitative uniqueness and essentiality facts. The theorem here studies the different object obtained by deleting an **entire** class and counts exactly the integers remaining in its threefold sumset at every full-block cutoff. The source's theorems and corollaries do not give the three-term exponential inclusion–exclusion formula with the positivity correction. Earlier work by Ling and Tang concerns minimal \(g\)-adic bases, rather than this precise infinite-deletion sumset invariant.

## Limitations
The formula is for a three-periodic position partition and the complete cutoffs \(g^{3k}\); other partitions, shorter cutoffs and higher sumset orders are not classified. General results on deleted Cantor-type digit sumsets or carry automata could implicitly imply the formula despite no covering statement having been identified in the checked sources. The proof and finite checks were subject to self-review only, not independent validation.

## References
1. M. Tang, *Minimal asymptotic \(g\)-adic bases from arbitrary partitions*, arXiv:2610.23152v1 (2026-10-16), https://arxiv.org/html/2610.23152v1 .
2. M. Tang and D.-R. Ling, *On asymptotic bases and minimal asymptotic bases*, arXiv:1810.10925 (2018), https://arxiv.org/abs/1810.10925 .
