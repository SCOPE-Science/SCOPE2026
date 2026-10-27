# A two-jump Fibonacci–Lucas law for scattered powers in alternating binary words

## Finding
Fix an integer \(q\ge 2\). Let \(w_k=(01)^k\), for every integer \(k\ge0\), and let \(A_q(k)\) count the **distinct nonempty binary roots** \(u\) for which the concatenated power \(u^q\) occurs as a scattered subsequence of \(w_k\). Write \(k=qm+r\), with integers \(m\ge0\) and \(0\le r<q\). With Fibonacci numbers \(F_0=0,F_1=1\) and \(F_{j+2}=F_{j+1}+F_j\), the exact answer is

\[
A_q(k)=\begin{cases}
F_{2m+3}-2,&r=0,\\
2F_{2m+2}-2,&1\le r<q.
\end{cases}
\]

Consequently, the increase in \(A_q(k)\) is supported only at \(k=qm\) and \(k=qm+1\), where \(m\ge1\); the respective increments are the even Lucas number \(L_{2m}=F_{2m-1}+F_{2m+1}\) and \(F_{2m}\). The ordinary generating function is

\[
\sum_{k\ge0}A_q(k)z^k
=\frac{z^q(3+z-2z^q)}{(1-z)(1-3z^q+z^{2q})}.
\]

More precisely, marking root length yields a complete two-variable enumeration:

\[
\sum_{k\ge0}\sum_{\substack{u\in\{0,1\}^{+}\\u^q\preceq w_k}}
y^{|u|}z^k
=\frac{yz^q\bigl(2+y(1+z-2z^q)\bigr)}
{(1-z)\bigl(1-2yz^q+y^2(z^{2q}-z^q)\bigr)}.
\]

Here \(\preceq\) denotes scattered-subsequence containment. Distinct roots yield distinct concatenated powers for a fixed exponent, since the power determines its root length and first root block. In particular, the two possible jump positions within a block of \(q\) host pairs are independent of \(q\), even though root powers have \(q\) copies.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), powers are **concatenated** (not shuffle powers), and different roots are counted once each, irrespective of their numbers of embeddings. Both the root and its power are nonempty. The host word is exactly \(w_k=(01)^k\), with \(k\ge0\), and the exponent is an arbitrary but fixed integer \(q\ge2\). Empty host words contribute zero. These formulas do not assert a count for arbitrary hosts, factor squares, or interleaved/shuffle repetitions.

## Proof
**1. Greedy embedding threshold.** For a nonempty binary word \(v=c_1\cdots c_\ell\), greedy subsequence matching into the infinite alternating word \(0101\cdots\) uses the same \(01\)-pair for consecutive letters precisely when their ordered pair is \(01\). Every other adjacent pair must move to the next \(01\)-pair. This is necessary because each pair contains one \(0\) followed by one \(1\), and sufficient by taking the earliest available occurrence at every step. Hence the smallest number of host pairs needed for \(v\) is

\[
\tau(v)=1+\#\{i:1\le i<\ell,\ (c_i,c_{i+1})\ne(0,1)\}.
\]

**2. Repeated-root threshold.** For a nonempty root \(u\), let \(d(u)\) count internal adjacent pairs of \(u\) unequal to \(01\), and let \(e(u)\) be the indicator that the wraparound pair (last letter, first letter) is unequal to \(01\). The \(q\)-fold concatenation has exactly \(q\) internal copies of each edge and \(q-1\) wraparound edges. Therefore

\[
\tau_q(u):=\tau(u^q)=1+q\,d(u)+(q-1)e(u).
\]

Thus \(\tau_q(u)\) is either \(0\) or \(1\) modulo \(q\); no root enters at another residue. The fact that there is a jump at \(qm+1\) only for \(m\ge1\) follows from the generating function below (and can also be checked directly from \(d,e\)).

**3. Exact weighted transfer matrix.** Set \(x=z^q\), \(h=z^{q-1}\), and index rows and columns by \(0,1\). An internal edge contributes weight \(1\) if it is \(01\), otherwise weight \(x\), so its matrix is

\[
T=\begin{pmatrix}x&1\\x&x\end{pmatrix}.
\]

A closing edge from the root's last letter to its first letter contributes weight \(1\) when it is \(01\), otherwise \(h\), so its matrix is

\[
E=\begin{pmatrix}h&1\\h&h\end{pmatrix}.
\]

For each root length \(\ell\ge1\), the total weight \(\sum_{|u|=\ell}z^{\tau_q(u)}\) equals \(z\operatorname{tr}(T^{\ell-1}E)\): the matrix product traverses its \(\ell-1\) internal edges, and the trace closes its single wraparound edge. At \(z=0\), the matrix \(T\) has square zero, so the formal geometric series is valid. Direct inversion gives

\[
\operatorname{tr}((I-yT)^{-1}E)
=\frac{2h+y(x+h-2xh)}{1-2xy+y^2(x^2-x)}.
\]

Multiplying by \(zy\), summing over root lengths with marker \(y\), and substituting \(x=z^q\), \(h=z^{q-1}\) yields the **first-appearance generating function**

\[
H_q(y,z):=\sum_{u\in\{0,1\}^{+}} y^{|u|}z^{\tau_q(u)}
=\frac{yz^q\bigl(2+y(1+z-2z^q)\bigr)}
{1-2yz^q+y^2(z^{2q}-z^q)}.
\]

Each root with threshold \(\tau_q(u)\) is counted at all host sizes \(k\ge\tau_q(u)\). Consequently the desired two-variable host generating function is \(H_q(y,z)/(1-z)\), proving its formula.

**4. Fibonacci–Lucas specialization.** Put \(y=1\) and \(X=z^q\). The first-appearance generating function simplifies to

\[
H_q(1,z)=\frac{X(3-2X)+zX}{1-3X+X^2}.
\]

The standard generating identities, derivable immediately from the Fibonacci recurrence, are

\[
\sum_{m\ge1}L_{2m}X^m=\frac{X(3-2X)}{1-3X+X^2},\qquad
\sum_{m\ge1}F_{2m}X^m=\frac{X}{1-3X+X^2}.
\]

Thus roots first occur with multiplicity \(L_{2m}\) at \(k=qm\) and multiplicity \(F_{2m}\) at \(k=qm+1\), and nowhere else. Starting from \(A_q(0)=0\), summing these increments gives \(A_q(qm)=F_{2m+3}-2\) and \(A_q(qm+r)=2F_{2m+2}-2\) for \(1\le r<q\). Dividing the first-appearance generating function by \(1-z\) proves the remaining univariate formula. All identities hold for every stated integer parameter, not merely for a finite range.

## Verification
The independent plain-Python script `VERIFY.py` enumerates binary roots and tests ordinary subsequence embedding directly, without using the transfer-matrix threshold, for all \(q\in\{2,\ldots,8\}\) and \(k\in\{0,\ldots,18\}\) (133 pairs). It checks the univariate rational generating-function recurrence at the same parameters, separately tests the prescribed Lucas and Fibonacci jump sizes, and compares the entire root-length distribution against independently extracted two-variable rational-function coefficients for \(2\le q\le6\), \(0\le k\le12\), and root lengths up to \(9\). All checks passed. Execute `python3 VERIFY.py` with a standard Python 3 installation. Finite tests are corroboration; the all-parameter proof is the transfer-matrix argument above.

## Relationship to prior work
Inoue, Inenaga, Hyyrö, Bannai, and Takeda (2018) formulate the longest common **square subsequence** problem and give algorithms to optimize its length in two supplied words. The exact *number of distinct roots* whose powers occur in one alternating host, and the stated two-residue count across all exponents, are not among its theorems. Lai, Liyanage, Zhu, and Zou (2022) study longest **letter-duplicated** subsequences; their blocks consist of repeated individual letters, unlike repetition of an entire unrestricted root. Kosowski's 2004 earlier paper addresses longest tandem scattered subsequences, again an optimization question; its full text was not accessible for a complete comparison. The present enumeration is intended as a distinct exact counting result rather than a restatement of an optimization algorithm.

## Limitations
The result is restricted to alternating binary hosts and integral \(q\ge2\), and does not claim a comparable rational formula for arbitrary hosts. The originality comparison is based on identified primary sources and scientific-literature searches; an unindexed treatment of this very family cannot be excluded. The 2004 paper could only be examined through its abstract and bibliographic information. No independent external validation is claimed.

## References
1. T. Inoue, S. Inenaga, H. Hyyrö, H. Bannai, and M. Takeda, *Computing Longest Common Square Subsequences*, CPM 2018, Article 15, published 2018-05-18. DOI: 10.4230/LIPIcs.CPM.2018.15. https://doi.org/10.4230/LIPIcs.CPM.2018.15
2. W. Lai, A. Liyanage, B. Zhu, and P. Zou, *Beyond the Longest Letter-Duplicated Subsequence Problem*, CPM 2022, Article 7, published 2022-06-22. DOI: 10.4230/LIPIcs.CPM.2022.7. https://doi.org/10.4230/LIPIcs.CPM.2022.7
3. A. Kosowski, *An Efficient Algorithm for the Longest Tandem Scattered Subsequence Problem*, SPIRE 2004, pp. 93–100. DOI: 10.1007/978-3-540-30213-1_13. https://doi.org/10.1007/978-3-540-30213-1_13
