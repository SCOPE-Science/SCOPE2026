# Exact dyadic-frontier crossing order for Rudin–Shapiro summatory walks

## Finding
Let \(a(n)=(-1)^{c_{11}(n)}\), where \(c_{11}(n)\) counts overlapping binary blocks `11` in the usual binary expansion of \(n\). Put
\[
S(n)=\sum_{j=0}^{n}a(j),\qquad T(n)=\sum_{j=0}^{n}(-1)^j a(j),\qquad T(-1)=0,
\]
and define the integer-lattice walk \(Q_n=((S(n)+T(n))/2,(S(n)-T(n))/2)\) for \(n\ge0\).

**Theorem.** For any integer \(k\ge1\), set \(u=2^k\), \(q=2^{k-1}\), and for each \(0\le p<u\) write \(p=\sum_{j=0}^{k-1}b_j2^j\) with \(b_j\in\{0,1\}\). Define
\[
B_k(p)=\sum_{j=0}^{k-1}(1+2b_j)4^j,
\qquad
h_k(p)=\begin{cases}u-2-2p,&0\le p<q,\\2(p-q)+1,&q\le p<u.\end{cases}
\]
The **entire ordered list** of vertical unit edges of \(Q\) on the line with first coordinate \(u\) consists of
\[
Q_{2B_k(p)}\,Q_{2B_k(p)+1}=\{(u,h_k(p)),(u,h_k(p)+1)\},\qquad p=0,1,\ldots,u-1.
\]
These are all such edges, and they occur in the displayed chronological order. Their lower heights are \(u-2,u-4,\ldots,0,1,3,\ldots,u-1\). The point \((u,v)\) occurs exactly once if \(v=0\) or \(v=u\) and exactly twice if \(0<v<u\), with explicit visit indices as follows. For each \(h\in\{v-1,v\}\cap\{0,\ldots,u-1\}\), put
\[
p(h)=\begin{cases}q-1-h/2,&h\text{ even},\\q+(h-1)/2,&h\text{ odd},\end{cases}
\qquad m_h=B_k(p(h)).
\]
The incident edge of lower height \(h\) contributes index \(2m_h+1\) at its lower endpoint and \(2m_h\) at its upper endpoint if \(h\) is even; these two indices are swapped if \(h\) is odd. Thus every visit index on every dyadic frontier is computable from \(v\) using \(O(k)\) binary-digit operations, without enumerating the earlier walk.

## Assumptions and scope
Indices are nonnegative integers; binary expansions have no extra leading digits. The walk begins with \(Q_0=(1,0)\); the asserted line has first coordinate \(2^k\) for \(k\ge1\). An edge is listed by its two endpoint positions, not an orientation. All visits include endpoint times; the pairs of edges listed above cover every occurrence on that line.

## Proof
**1. Paired-walk identity.** Directly from the digit rule, \(a(2m)=a(m)\) and \(a(2m+1)=(-1)^m a(m)\). Grouping even and odd terms in the two partial sums gives, for all \(m\ge0\),
\[
Q_{2m}=(S(m),T(m-1)),\qquad Q_{2m+1}=(S(m),T(m)).
\]
Consequently every pair of consecutive times \((2m,2m+1)\) constitutes exactly one vertical unit edge, located on the line with first coordinate \(S(m)\), because \(T(m)-T(m-1)=(-1)^m a(m)\in\{-1,1\}\).

**2. Exactly which indices hit the dyadic frontier.** The Rudin–Shapiro summatory recurrence, also obtainable by grouping four terms, reads
\[
S(4r)=2S(r)-a(r),\quad S(4r+1)=S(4r+3)=2S(r),\quad
S(4r+2)=2S(r)+(-1)^r a(r).
\]
It follows inductively that \(S(0)=1\) and \(S(n)\ge2\) for every \(n\ge1\): the odd-index branches are at least two; the even branches for \(r\ge1\) are at least three; \(S(2)=3\). Thus \(S(m)=1\) only at \(m=0\). Also \(S(4r)\) and \(S(4r+2)\) are odd. For \(k\ge1\), the equation \(S(m)=2^k\) therefore forces \(m=4r+1\) or \(4r+3\) and \(S(r)=2^{k-1}\). Repeating gives precisely the \(k\)-digit base-four strings over \(\{1,3\}\), hence precisely the \(u\) indices \(B_k(p)\). They increase with \(p\), since a weight \(4^j\) exceeds the sum of all lower weights \(\sum_{i<j}4^i\).

**3. Orientation.** For a base-four word whose digits lie in \(\{1,3\}\), the parity of the binary `11`-count equals one exactly when its leading base-four digit is \(3\). Indeed, reading each digit as `01` or `11`, a digit \(3\) contributes one internal `11`, while every nonleading digit \(3\) contributes one additional boundary `11`. Therefore \(a(B_k(p))=1\) for \(p<q\), and \(-1\) for \(p\ge q\). As \(B_k(p)\) is odd, the vertical step \(T(m)-T(m-1)=-a(m)\) is downward in the first half and upward in the second. In particular, for first-half edges \(T(m)\) is their lower height and for second-half edges \(T(m-1)\) is their lower height.

**4. Exact heights by induction.** The companion recurrence is
\[
T(4r+1)=2T(r-1),\qquad T(4r+3)=2T(r)
\]
for \(r\ge0\), with \(T(-1)=0\). At \(k=1\), the two indices \(m=1,3\) have lower heights \(0,1\). Suppose an index \(r\) belonging to the \((k-1)\)-st frontier has lower height \(h\). Its consecutive children \(4r+1\) and \(4r+3\) belong to the next frontier. If its leading base-four digit is \(1\), then \(T(r)=h\), \(T(r-1)=h+1\), so the two children have lower heights \(2h+2\) and \(2h\). If the leading digit is \(3\), then \(T(r)=h+1\), \(T(r-1)=h\), so the two child lower heights are \(2h-1\) and \(2h+1\). Inductively the first-half heights \(2^{k-1}-2,2^{k-1}-4,\ldots,0\) become \(2^k-2,2^k-4,\ldots,0\), and the second-half heights \(1,3,\ldots,2^{k-1}-1\) become \(1,3,\ldots,2^k-1\). This is exactly the stated formula for \(h_k(p)\).

**5. Complete inverse.** The list contains each unit interval \([h,h+1]\) for \(0\le h<u\) exactly once, so a lattice point of height \(v\) is incident to precisely the listed edges with \(h=v-1\) or \(h=v\) in the allowed range. Step 3 determines which endpoint is even-indexed and which odd-indexed. Inverting the two affine formulas for \(h_k(p)\) gives \(p(h)\) above. Step 2 excludes all other edges and hence all other visits. This proves both the exact chronological order and every inverse-index statement. \(\square\)

## Verification
Run `python3 verify.py` alongside this document. It independently computes the signs from binary adjacency, then both partial sums and all actual planar visits through the complete frontier of order \(k=7\) (time index \(32767\)). It checks the edge order, exact lower heights, inverse indices at every frontier lattice site, and that no additional visits occur through that horizon. The symbolic induction, not this finite computation, proves all \(k\).

## Relationship to prior work
Rampersad and Shallit (2023), especially Lemmas 6 and 8, give the underlying four-adic recurrences; their theorems concern range, counts, and geometric coverage, not the displayed explicit dyadic crossing-order and direct visit-index formulas. Ryde's 2013 `Math::PlanePath::AlternatePaper` documentation already records the global coverage and boundary/interior multiplicities and provides a general coordinate-to-index routine. The present special-line formulas are *not* a new claim of coverage or of general algorithmic invertibility: they sharpen the description at a natural family of geometric scales to a closed bit-dilation inverse and exact traversal ordering. Mendès France and Tenenbaum (1981) study folding curves, dimension and global coverage without providing this chronological dyadic-frontier law. OEIS A093573 records general cumulative-value hits as sequence data rather than this explicit two-dimensional closed formula.

## Limitations
The formula is specialized to first coordinate \(2^k\) and the stated summatory-walk normalization; it does not give a new general inverse for arbitrary lattice points. Global boundary/interior visit multiplicity and the four-adic recurrences were already established. The complete 1978 Brillhart–Morton paper and the 1996 follow-up were not independently inspected, leaving possible unindexed prior coverage; the exact explicit formula and order were not found in materially inspected sources. No independent mathematical audit has been performed.

## References
1. N. Rampersad and J. Shallit, *Rudin-Shapiro Sums Via Automata Theory and Logic*, arXiv:2302.00405 (first public version 2023-02-01), https://arxiv.org/html/2302.00405v3 .
2. K. Ryde, *Math::PlanePath::AlternatePaper*, documentation (2011–2013), https://metacpan.org/release/KRYDE/Math-PlanePath-102/view/lib/Math/PlanePath/AlternatePaper.pm .
3. M. Mendès France and G. Tenenbaum, *Dimension des courbes planes, papiers pliés et suites de Rudin-Shapiro*, Bull. Soc. Math. France 109 (1981), 207–215, https://www.numdam.org/item/10.24033/bsmf.1937.pdf .
4. OEIS A093573, indices of cumulative Rudin–Shapiro values, https://oeis.org/A093573 .
