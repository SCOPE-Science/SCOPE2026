# Exact unbordered-factor language of finite binary Cantor words

## Finding
For each integer \(k\ge1\), define the binary Cantor iterate by \(C_0=1\) and \(C_{k+1}=C_k0^{3^k}C_k\). Let \(S_{m,j}\) denote the suffix of \(C_m\) beginning at its \(j\)-th occurrence of \(1\), where \(1\le j\le2^m\). Put \(T_0=\{1\}\), and for \(m\ge1\) put \(T_m=\{3^{m-1}+1,\ldots,3^m\}\).

**Theorem.** The complete set of distinct nonempty unbordered contiguous factors of \(C_k\) is
\[
\{0,1\}\ \cup\ \bigcup_{m=0}^{k-1}\ \bigcup_{j=1}^{2^m}\ \bigcup_{t\in T_m}
\{S_{m,j}0^t,\ (S_{m,j}0^t)^R\}.
\]
Here \(w^R\) means word reversal. The displayed union is disjoint except for the explicit grouping into reverse pairs. In particular the exact number of distinct nonempty unbordered factors is
\[
U_k=\frac{8\cdot 6^{k-1}+12}{5},
\]
and the maximum unbordered-factor length is \(2\cdot3^{k-1}\), attained only by \(C_{k-1}0^{3^{k-1}}\) and its reversal. Equivalently, because \(|C_k|=3^k\), the total number grows as \(\Theta\bigl(|C_k|^{\log_3 6}\bigr)\).

## Assumptions and scope
A factor means a **contiguous**, nonempty substring, counted only once if it occurs at multiple positions. A nonempty word is *bordered* if a nonempty proper prefix equals a suffix; otherwise it is *unbordered*. The alphabet is \(\{0,1\}\) and no circular wraparound or scattered subsequences are allowed. The word \(C_k\) is a complete finite substitution iterate, not an arbitrary prefix of the infinite fixed point. The recursive identity agrees with the substitution \(1\mapsto101\), \(0\mapsto000\).

## Proof
**Gap ruler law.** There are \(2^k\) occurrences of \(1\) in \(C_k\). Number them from \(1\) to \(2^k\). For each \(1\le i<2^k\), the number of zeros between occurrences \(i\) and \(i+1\) is
\[
g_i=3^{\nu_2(i)},
\]
where \(\nu_2(i)\) is the largest exponent of two dividing \(i\). This follows by induction: the next iterate consists of two copies of \(C_k\) with a central zero gap of length \(3^k\); for \(1\le i<2^k\), \(\nu_2(2^k+i)=\nu_2(i)\). The same recursion shows every \(C_k\) is a palindrome.

**Border criterion.** Consider any factor beginning with \(1\) and ending in zeros. It has the unique form
\[
w=1\,0^{g_a}1\,0^{g_{a+1}}1\cdots0^{g_{b-1}}1\,0^t,
\qquad 1\le a\le b<2^k,\quad1\le t\le g_b.
\]
When \(a=b\), the displayed internal product is empty. We claim that
\[
\boxed{w\text{ is unbordered}\quad\Longleftrightarrow\quad
g_i<t\text{ for every }a\le i<b.}
\]
If every preceding complete zero gap is shorter than \(t\), any proper prefix ending in \(t\) consecutive zeros is impossible. A nonempty border would have to start with \(1\) and end with the final \(t\) zeros, so no border exists.

Conversely assume some internal \(g_i\ge t\). Let \(m\ge0\) be uniquely determined by \(3^{m-1}<t\le3^m\) when \(m\ge1\), and by \(t=1\) when \(m=0\). Then \(g_i\ge t\) if and only if \(2^m\mid i\). Since \(t\le g_b\), also \(2^m\mid b\). Take the **first** multiple \(q\) of \(2^m\) in \([a,b-1]\) and let \(r=q-a\), so \(0\le r<2^m\). The sequences of \(r\) gaps
\[
(g_a,\ldots,g_{q-1})\quad\text{and}\quad
(g_{b-r},\ldots,g_{b-1})
\]
are identical: their indices differ by \(b-q\), a multiple of \(2^m\), while none of the first sequence's indices is divisible by \(2^m\). For such indices, adding a multiple of \(2^m\) leaves the exact \(2\)-adic valuation unchanged. Hence the prefix of \(w\) from its first \(1\) through the \(t\) zeros following its \((r+1)\)-st \(1\) equals the suffix from the \((b-r)\)-th \(1\) through the last \(t\) zeros. As \(q<b\), this is a nonempty proper border. This proves the criterion, including \(r=0\), where the border is \(10^t\).

**Classification.** Fix an unbordered factor \(w\) beginning in \(1\) and ending in \(0\). Define \(m\) from its trailing length \(t\) as above. The last gap index \(b\) is divisible by \(2^m\). By the criterion, none of \(a,\ldots,b-1\) is divisible by \(2^m\). Consequently \(0\le b-a<2^m\). Put \(r=b-a\) and \(j=2^m-r\), so \(1\le j\le2^m\). The complete zero-gap list from \(a\) to \(b-1\) equals the gap list from \(j\) to \(2^m-1\), because the indices are congruent modulo \(2^m\) and none is divisible by \(2^m\). Therefore
\[
w=S_{m,j}0^t.
\]
The index bound \(b<2^k\) forces \(m\le k-1\). Conversely, every such word occurs as a factor: \(C_m0^{3^m}\) is the prefix of \(C_{m+1}\), which in turn is a prefix of \(C_k\); the suffix \(S_{m,j}\) can be extended into that zero gap by any \(t\in T_m\). The complete gaps before its terminal run have lengths at most \(3^{m-1}<t\) (and no complete gap for \(m=0\)), so the criterion makes it unbordered.

Any unbordered factor of length at least two has distinct first and last symbols; otherwise its first symbol is a border of length one. Because \(C_k\) is palindromic, reversal maps factors to factors, preserving unborderedness. Thus the classification also contains exactly all factors beginning in \(0\) and ending in \(1\). The two remaining singleton unbordered factors are \(0\) and \(1\).

**Distinctness and enumeration.** The parameter \(m\) is determined by the number \(t\) of trailing zeros. With \(m,t\) fixed, the distinct values of \(j\) give different numbers of \(1\)'s, namely \(2^m-j+1\), hence different words. Words beginning with \(1\) and ending in \(0\) cannot coincide with their reverse-oriented counterparts. There is one factor at \(m=0\), and for \(m\ge1\) there are \(2^m(3^m-3^{m-1})\). Therefore
\[
U_k=2+2\left(1+\sum_{m=1}^{k-1}2^m(3^m-3^{m-1})\right)
=\frac{8\cdot6^{k-1}+12}{5}.
\]
For each \(m\), the largest possible length of \(S_{m,j}0^t\) is \(2\cdot3^m\), attained only when \(j=1\) and \(t=3^m\). Strict increase with \(m\) gives the asserted two longest factors at \(m=k-1\). This completes the proof.

## Verification
A standalone `checker.py` included with this result builds each \(C_k\), independently enumerates candidate substrings beginning with \(1\) and ending with \(0\), and detects borders through the ordinary prefix-function (KMP) algorithm. Its output sets are compared with the explicit theorem sets, then checked for count and longest length. All ranks \(1\le k\le6\) passed: counts \(4,12,60,348,2076,12444\), with word lengths \(3,9,27,81,243,729\). The infinite-rank conclusion is established by the preceding proof, not by these finite checks. Run `python3 checker.py` with Python 3 and no external packages.

## Relationship to prior work
Goč, Schaeffer, and Shallit (2012) study automatic-sequence factor complexity and identify limitations of synchronization for unbordered-factor counts, including a different power-of-two characteristic word. Goč, Mousavi, and Shallit (2012) count unbordered factors of Thue–Morse and study the period-doubling and Rudin–Shapiro words. The Cantor-like-sequence permutation-complexity work (2016) analyzes ordinary factor and permutation complexity for the same substitution family, but not the explicit unbordered language proved here. Charlier, Harju, Puzynina, and Zamboni (2015) treat abelian and weakly abelian borders, rather than these ordinary exact borders. These distinctions are not a guarantee of exhaustive historical priority.

## Limitations
The classification concerns complete finite binary Cantor iterates, **distinct** nonempty contiguous factors and ordinary exact borders. It does not directly provide the per-length spectrum for every length, an arbitrary-prefix formula, or a classification for other Cantor-like substitutions. Priority comparison is limited to the identified accessible sources and research-record searches. Independent mathematical audit has not been performed.

## References
1. D. Goč, L. Schaeffer, and J. Shallit, *Subword Complexity and \(k\)-Synchronization*, arXiv:1206.5352v1 (first public 2012-06-23), https://arxiv.org/abs/1206.5352.
2. D. Goč, H. Mousavi, and J. Shallit, *On the Number of Unbordered Factors*, arXiv:1211.1301v1 (first public 2012-11-06), https://arxiv.org/html/1211.1301v1.
3. *On the permutation complexity of the Cantor-like sequences*, Theoretical Computer Science 616 (2016), 100–110, DOI:10.1016/j.tcs.2015.12.022, https://doi.org/10.1016/j.tcs.2015.12.022.
4. É. Charlier, T. Harju, S. Puzynina, and L. Q. Zamboni, *Abelian bordered factors and periodicity*, arXiv:1501.07464v1 (2015-01-29), https://arxiv.org/abs/1501.07464.
