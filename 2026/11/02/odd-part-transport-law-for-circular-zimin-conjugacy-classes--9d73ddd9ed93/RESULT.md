# Odd-part transport law for circular Zimin conjugacy classes

## Finding

Let \(Z_0=\varepsilon\) and \(Z_n=Z_{n-1}a_nZ_{n-1}\), with distinct letters \(a_1,a_2,\ldots\). For a nonempty finite word \(w\), let \(\mathcal C_m(w)\) be the set of conjugacy classes (cyclic-rotation orbits) represented by length-\(m\) circular windows of \(w\), and put \(c_n(m)=|\mathcal C_m(Z_n)|\). A circular window starts at a position of \(w\) and is read modulo its length; each window here has length at most \(|w|\).

**Theorem.** For all integers \(n\ge2\) and \(1\le m\le 2^{n-1}-1\),

\[
\boxed{c_n(m)-c_{n-1}(m)=\frac{m}{2^{\nu_2(m)}}.}
\]

More precisely, let \(s=\nu_2(m)\), \(B=2^s\), \(d=m/B\), and \(U=Z_{n-1}\). The classes in \(\mathcal C_m(Z_n)\setminus\mathcal C_m(U)\) are precisely the \(d\) distinct classes of

\[
a_n\operatorname{pre}_{m-1-qB}(U)\operatorname{suf}_{qB}(U),\qquad q=0,1,\ldots,d-1.
\]

Here \(\operatorname{pre}_t\) and \(\operatorname{suf}_t\) denote the length-\(t\) prefix and suffix; the length-zero choice is empty. Among the \(m\) circular windows containing \(a_n\), two belong to the same conjugacy class **if and only if** the number of letters preceding \(a_n\) in their unrotated windows belongs to the same half-open block \([qB,(q+1)B)\).

**Corollary.** For any fixed \(m\ge1\), let \(r=\lceil\log_2(m+1)\rceil\). At every rank \(n\ge r\),

\[
c_n(m)=c_r(m)+(n-r)\frac{m}{2^{\nu_2(m)}}.
\]

Thus cyclic-conjugacy complexity at any fixed admissible window length grows exactly affinely with Zimin rank, with a slope given by the odd part of the length.

## Assumptions and scope

The letters are literal distinct symbols, not variables subjected to substitution. The alphabet grows by one symbol per rank. The factors counted are circular, sentinel-free windows, not merely ordinary linear factors, and equivalence is by cyclic rotation of the window string, not reversal or letter renaming. All quantified window lengths satisfy \(1\le m\le |Z_{n-1}|\); the theorem makes no transport assertion for longer windows. Every \(Z_n\) is a palindrome by induction.

## Proof

Write \(U=Z_{n-1}\), so \(Z_n=Ua_nU\) and \(|U|=2^{n-1}-1\). The middle symbol \(a_n\) occurs exactly once on the circle \(Z_n\). A length-\(m\) circular window therefore either avoids this symbol or contains it exactly once.

**Windows avoiding the new letter.** Removing \(a_n\) from the circle leaves the contiguous path \(UU\) of length \(2|U|\). Every length-\(m\) window avoiding \(a_n\) is a factor of this path. Conversely, for \(m\le |U|\), every length-\(m\) circular window of \(U\) occurs inside \(UU\). Therefore the classes of avoiding windows are exactly \(\mathcal C_m(U)\).

**Windows containing the new letter.** Exactly \(m\) indexed circular windows contain \(a_n\), one for each possible position of that unique symbol in the window. Index them by \(j\in\{0,\ldots,m-1\}\), the number of letters preceding \(a_n\). Their strings are

\[
\operatorname{suf}_j(U)\,a_n\,\operatorname{pre}_{m-1-j}(U).
\]

Each of their conjugacy classes has a unique representative starting at \(a_n\), since \(a_n\) occurs just once. After rotation, this representative is \(a_nQ_j\), where

\[
Q_j=\operatorname{pre}_{m-1-j}(U)\operatorname{suf}_j(U).
\]

By palindromicity of \(U\), \(\operatorname{suf}_j(U)\) is the reverse of \(\operatorname{pre}_j(U)\). Let \(P_t\) denote the letter in position \(t\) of the one-sided ruler word \(a_{1+\nu_2(t)}\), for positive integers \(t\). The first \(|U|\) letters of this ruler word form \(U\); indeed the recursion places \(a_i\) at exactly the positions whose \(2\)-adic valuation is \(i-1\). Consequently

\[
Q_j=P_1P_2\cdots P_{m-1-j}\,P_jP_{j-1}\cdots P_1.
\]

For consecutive values \(j\) and \(j+1\), both words share an initial segment of length \(m-2-j\) and a final segment of length \(j\). The sole potentially different symbol is \(P_{m-1-j}\) versus \(P_{j+1}\). Setting \(t=j+1\),

\[
Q_j=Q_{j+1}\iff\nu_2(m-t)=\nu_2(t).
\]

Write \(m=Bd\) with \(B=2^s\), \(d\) odd. For \(1\le t<m\), if \(B\nmid t\), then \(\nu_2(t)<s\) and \(\nu_2(m-t)=\nu_2(t)\). If \(B\mid t\), then \(t=B h\) with \(1\le h<d\), and \(\nu_2(t)\ne\nu_2(m-t)\) because \(h\) and \(d-h\) have opposite parity. Thus \(Q_j\) is constant on each block of consecutive indices

\[
qB\le j<(q+1)B,\qquad 0\le q<d.
\]

**Different blocks cannot collide.** Suppose \(0\le q<q'<d\), and choose \(j\) in block \(q\) and \(j'\) in block \(q'\). Set \(p=d-q'\), so \(1\le p\le d-1\). Inspect the letter at position \(pB\) in \(Q_j\) and \(Q_{j'}\), using one-based indexing. Since \(p\le d-q-1\), that position in \(Q_j\) lies in the initial prefix and equals

\[
P_{pB}=a_{s+1+\nu_2(p)}.
\]

Since \(p\ge d-q'\), the same position in \(Q_{j'}\) lies in the reversed suffix and equals

\[
P_{(d-p)B}=a_{s+1+\nu_2(d-p)}.
\]

The oddness of \(d\) means \(p\) and \(d-p\) have opposite parity. Their valuations differ, so these letters differ. Therefore the \(d\) blocks produce exactly \(d\) distinct conjugacy classes, represented by their left endpoints \(j=qB\). None is an avoiding-window class because each contains \(a_n\). Adding the old and new disjoint classes proves both the precise classification and the formula. The corollary follows by applying the transport identity successively after rank \(r\), the first rank with \(|Z_r|\ge m\). \(\square\)

## Verification

The accompanying standalone standard-library checker reconstructs the words and computes canonical representatives by explicitly enumerating all cyclic rotations of each circular window. For each rank \(n=2,\ldots,7\) and each admissible length \(m=1,\ldots,2^{n-1}-1\), it independently compares class sets, verifies the odd-part increment, and checks that the \(m\) marker windows partition exactly into consecutive blocks of size \(2^{\nu_2(m)}\). All tested cases passed, covering \(10{,}548\) indexed circular starts. These finite checks are corroboration; the proof above establishes all ranks and lengths in scope.

Reproduce with `python checker.py` using Python 3 and no nonstandard dependencies.

## Relationship to prior work

Cassaigne, Fici, Sciortino and Zamboni introduce cyclic complexity as conjugacy-class counts among factors of infinite words over finite alphabets. Their results primarily treat Sturmian, period-doubling, paperfolding and Thue–Morse words. Here the objects are a **finite sequence of circular Zimin words with a growing alphabet**, and the result is an exact rank-to-rank law with a complete index-block classification; their stated results do not imply it.

Rytter and Shur treat Zimin words as unavoidable patterns, giving algorithms for detecting Zimin-pattern rank and results on Fibonacci factors. Their work supplies the classical recursion and primary combinatorics setting, but not the circular conjugacy transport or odd-part classification. The standard ruler representation alone does not state or imply the new classification without the circular-window analysis and the noncollision argument in the proof.

## Limitations

No formula is claimed for \(m>|Z_{n-1}|\) in the rank-to-rank comparison. This is a literal, growing-alphabet family; no theorem is asserted for fixed-alphabet morphic images, ordinary linear factors, or length-greater-than-one-traversal windows. The comparative literature search is not an exhaustive historical-priority guarantee, and no independent mathematical audit has been performed.

## References

1. J. Cassaigne, G. Fici, M. Sciortino, L. Q. Zamboni, *Cyclic Complexity of Words*, arXiv:1402.5843, initially public 2014-02-24. https://arxiv.org/abs/1402.5843
2. W. Rytter, A. M. Shur, *On Searching Zimin Patterns*, arXiv:1409.8235, initially public 2014-09-29. https://arxiv.org/html/1409.8235v1
