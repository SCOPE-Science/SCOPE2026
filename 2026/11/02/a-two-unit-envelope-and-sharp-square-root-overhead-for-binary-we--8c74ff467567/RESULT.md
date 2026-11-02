# A two-unit envelope and sharp square-root overhead for binary weight-two subsequence covers

## Finding

For every integer \(k\ge2\), consider the entire constant-weight-two layer
\[
\mathcal T_k=\{0^a1\,0^b1\,0^c:\ a,b,c\in\mathbb Z_{\ge0},\ a+b+c=k-2\}\subset\{0,1\}^k.
\]
Let \(L_k\) be the minimum length of a finite binary word containing **each** member of \(\mathcal T_k\) as a (not necessarily contiguous) scattered subsequence. Define
\[
s_k=\left\lceil 2\sqrt{2(k-1)}\right\rceil.
\]
Then the following *all-length, two-unit envelope* holds:
\[
\boxed{\quad k-3+s_k\ \le\ L_k\ \le\ k-1+s_k\quad}\qquad(k\ge2).
\]
In particular, the leading overhead constant is sharp:
\[
\lim_{k\to\infty}\frac{L_k-k}{\sqrt{k}}=2\sqrt2.
\]
The upper bound is constructive: an explicitly specified host using two residue classes of marker positions modulo a nearly square-root-sized block works for **every** target. The bounds do not assert an exact formula for \(L_k\) at each finite \(k\).

## Assumptions and scope

A scattered subsequence is obtained by deleting positions while preserving their order. The binary alphabet is labeled; there is no cyclic wraparound, wildcard or complement identification. The target length \(k\) is at least two, and the target family contains all \(\binom{k}{2}\) words of length \(k\) with precisely two ones. Hosts may contain any numbers of zeros and ones. Length is counted in symbols, with no requirement to minimize the number of ones separately. The statement concerns an entire target language, not an arbitrary input subfamily.

Write \(K=k-2\) and \(T=K+1=k-1\). For a candidate host \(W\), let \(Z\) be the number of zeros and \(R\) the number of ones. Enumerate the ones in their left-to-right order; write \(z_i\) for the number of preceding zeros, so \(0\le z_1\le\cdots\le z_R\le Z\).

**Marker criterion.** The target \(0^a1\,0^b1\,0^c\), with \(a+b+c=K\), occurs in \(W\) if and only if there are indices \(i<j\) such that
\[
z_i\ge a,\qquad z_j-z_i\ge b,\qquad Z-z_j\ge c.
\]
The forward direction counts zeros in the selected prefix, middle and suffix; the reverse direction greedily chooses the requisite zeros in these disjoint intervals. The criterion allows the two source ones to have equal zero-levels when \(b=0\), provided the one-indices are distinct.

## Proof

**1. Necessary window multiplicity.** Every covered target has \(K\) zeros, so \(Z\ge K\). Put \(d=Z-K+1\ge1\). For every \(a\in\{0,\ldots,K\}\), the target \(0^a11\,0^{K-a}\) requires **two distinct ones** whose zero-levels both belong to
\[
I_a=[a,\,Z-(K-a)]=[a,a+d-1].
\]
There are \(T=K+1\) such intervals, each with at least two ones, counted with multiplicity if a zero-level is shared. A fixed one at zero-level \(z\) belongs to at most \(d\) intervals \(I_a\). Double-counting interval–one incidences therefore yields
\[
R\,d\ge2T,\qquad R\ge\left\lceil\frac{2T}{d}\right\rceil.
\]
Consequently
\[
|W|=Z+R\ge K+d-1+\left\lceil\frac{2T}{d}\right\rceil
=k-3+d+\left\lceil\frac{2(k-1)}d\right\rceil.
\]
For any positive integer \(m\),
\[
\min_{d\ge1,\ d\in\mathbb Z}\left(d+\left\lceil\frac md\right\rceil\right)
=\left\lceil2\sqrt m\right\rceil.
\]
Indeed the left side is the smallest integer \(s\) admitting positive integers \(d,r\) with \(d+r=s\) and \(dr\ge m\); the largest possible product at sum \(s\) is \(\lfloor s^2/4\rfloor\), and the smallest feasible sum is \(\lceil2\sqrt m\rceil\). Taking \(m=2T\) proves the lower bound.

**2. Explicit construction.** Choose an integer \(d\ge2\); put \(h=\lfloor d/2\rfloor\) and \(Z=K+d-1\). Form \(W_{k,d}\) from \(Z\) zeros, placing **exactly one one** at every zero-level
\[
S_{k,d}=\{z\in\{0,1,\ldots,Z\}:z\bmod d\in\{0,h\}\}.
\]
This specification is unambiguous: concatenate a one at each selected level, and one zero between consecutive levels. Because \(1\le h<d\), the two residue classes are distinct.

Every interval consisting of \(d\) consecutive integer zero-levels contains exactly two selected levels. Successive selected levels have gaps alternately \(h\) and \(d-h\). Put \(g=\lceil d/2\rceil\). In a \(d\)-level window beginning at \(t\), let \(\ell(t)\) and \(r(t)\) be the first and last selected levels. A gap is at most \(g\), so
\[
0\le\ell(t)-t\le g-1\le h,
\qquad r(t)-t\ge d-g=h.
\]
Fix arbitrary \(a,b,c\ge0\) with \(a+b+c=K\). Select the one at level \(\ell(a)\), and the one at level \(r(a+b)\). The chosen first one follows at least \(a\) zeros and the chosen last one precedes at least \(c\) trailing zeros, because
\[
a\le\ell(a)\le a+d-1,
\qquad a+b\le r(a+b)\le a+b+d-1=Z-c.
\]
For their intervening zeros,
\[
r(a+b)-\ell(a)=b+[r(a+b)-(a+b)]-[\ell(a)-a]\ge b+h-h=b.
\]
When \(b>0\), the two chosen levels are strictly ordered; when \(b=0\), they are the first and last of the *same* \(d\)-window and are distinct by its two-residue structure. Thus the marker criterion applies to every target, and \(W_{k,d}\) is a cover.

**3. Length of the construction.** Write the number of available integer levels as \(Z+1=K+d=qd+r\), where \(q\ge1\) and \(0\le r<d\). Each full block of \(d\) levels contains two ones; the remainder contains one selected level when \(r\ge1\) and a second when \(r\ge h+1\). Hence
\[
R=2q+\mathbf 1_{\{r\ge1\}}+\mathbf 1_{\{r\ge h+1\}}.
\]
As \(T=(q-1)d+r+1\), elementary consideration of \(r=0\), \(1\le r\le h\), and \(h+1\le r<d\) gives
\[
R\le\left\lceil\frac{2T}{d}\right\rceil+2.
\]
It follows that
\[
|W_{k,d}|=K+d-1+R\le k-1+d+\left\lceil\frac{2T}{d}\right\rceil.
\]
For \(T\ge1\), a minimizer of \(d+\lceil2T/d\rceil\) can be chosen with \(d\ge2\) (including \(T=1\), where \(d=2\) is a minimizer). Choose such a minimizing \(d\). The resulting explicit cover satisfies \(|W_{k,d}|\le k-1+s_k\), proving the upper bound.

**4. Sharp leading constant.** Divide both sides of the proven envelope by \(\sqrt{k}\) after subtracting \(k\). Since \(s_k=2\sqrt{2(k-1)}+O(1)\), both sides converge to \(2\sqrt2\). This proves the limit.

## Verification

The included standalone `verify.py` uses only the Python standard library and is executed as `python3 verify.py`. It performs: (i) complete breadth-first searches of the finite subsequence-matching product automata to obtain the shortest lengths for \(2\le k\le12\), namely \(2,5,7,9,10,12,14,15,17,18,20\); (ii) an independent direct-embedding versus marker-criterion comparison for every binary host of length at most eleven and all applicable \(k\le7\); (iii) exact integer evaluation of the lower and constructive upper bounds, with complete target-pair coverage checks, for every \(2\le k\le100\) and for \(k\in\{150,200,300,500\}\). Its success message begins `VERIFY_OK`.

The finite checks do not establish the infinite statement; the incidence bound, two-residue construction and exact residue count above establish it for all \(k\ge2\).

## Relationship to prior work

Fleischmann et al. study full \(k\)-subsequence universality—coverage of **all** words of length \(k\)—and edit distance to that property [1]. This is stronger as a coverage requirement but does not yield the sharp minimum for the strictly smaller fixed-weight-two language. Lagoutte and Tavenas discuss hardness of common supersequences for *arbitrary selected sets* of fixed-length two-one words, building on Middendorf, and analyze a different restricted one-marker language [2]. Those statements do not imply the two-sided all-length bound or its sharp constant for the **complete** two-one layer. Tan studies permutation supersequences over growing alphabets [3], rather than repeated zero symbols and two binary ones. Related one-marker and full-universality results were compared by their logical implications: the former contains a different target language, and the latter's optimal length \(2k\) gives only a weaker upper bound for our family.

## Limitations

The two-unit envelope determines the optimal leading square-root constant but does **not** determine every finite exact value \(L_k\), describe all optimal hosts, or treat fixed weights greater than two. Complete searches establish finite illustrative values only for \(k\le12\); a finite search is not a proof for larger \(k\). The absence of an explicitly matching published formula from the inspected literature is not a proof of global novelty; older or unindexed work specializing to the complete weight-two language remains a priority risk. No independent scientific audit has been performed.

## References

1. P. Fleischmann, M. Kosche, T. Koß, F. Manea and S. Siemer, *The Edit Distance to k-Subsequence Universality*, arXiv:2007.09192v1, first public 17 July 2020. https://arxiv.org/abs/2007.09192
2. A. Lagoutte and S. Tavenas, *The complexity of Shortest Common Supersequence for inputs with no identical consecutive letters*, arXiv:1309.0422, 2 September 2013. https://arxiv.org/abs/1309.0422
3. O. Tan, *Skip Letters for Short Supersequence of All Permutations*, arXiv:2201.06306, 17 January 2022. https://arxiv.org/abs/2201.06306
