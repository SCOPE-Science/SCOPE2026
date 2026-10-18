# A polylogarithmic short-chord obstruction for consecutive cycle sums

## Finding
For every integer \(n\ge4\), label the vertices of the cycle \(C_n\) consecutively by \(1,2,\ldots,n\), and add exactly one non-cycle edge joining distinct vertices \(u,v\). Write \(d=\min\{|u-v|,n-|u-v|\}\), where \(2\le d\le n/2\), and put \(T_n=n(n+1)/2\). Let \(\mathcal R(n;u,v)\) be the set of sums of labels of all nonempty connected vertex sets of the resulting graph. Define the classical multiplication-table counting function
\[
M(N)=\#\{ab:1\le a,b\le N\}.
\]
Then the following finite, uniform bound holds:
\[
\boxed{\#\mathcal R(n;u,v)\le 2M(2n)+\left(1+\frac{d(d-1)}2\right)(1+2M(2n)).}
\]
Let
\[
\delta=1-\frac{1+\log\log2}{\log2}>0,\qquad
\Lambda(n)=(\log n)^\delta(\log\log n)^{3/2}\quad(n\ge 4).
\]
Ford's multiplication-table theorem implies, uniformly over the added edge,
\[
\boxed{\#\mathcal R(n;u,v)=O\left(\frac{(1+d^2)n^2}{\Lambda(n)}\right).}
\]
Consequently, along any sequence of one-chord cycles with \(n\to\infty\) and \(d=o(\sqrt{\Lambda(n)})\), the fraction \(\#\mathcal R(n;u,v)/T_n\) tends to \(0\), **not merely below \(1\)**. In particular there exists an absolute \(c>0\) such that every sum-completing single chord, for all sufficiently large \(n\), has cyclic span
\[
\boxed{d\ge c(\log n)^{\delta/2}(\log\log n)^{3/4}.}
\]
No assertion is made that a single sum-completing chord exists for each sufficiently large \(n\).

## Assumptions and scope
A vertex set is called connected when its induced subgraph is connected; all sums use each selected label once. A cycle chord joins nonadjacent vertices; its cyclic span \(d\) is the shorter distance measured in original cycle edges. All logarithms are natural. The finite bound is valid for every chord, including chords with a short path crossing the label wrap from \(n\) to \(1\). The analytic constant in the big-O bound is absolute, whereas the threshold for the conclusion can be chosen sufficiently large. The theorem concerns only *one* additional edge and ordinary positive integer sums, not the number of edges required in general.

## Proof
**1. Exact two-gap identity.** Let \(P\) and \(Q\) be the two internally disjoint paths in \(C_n\) from \(u\) to \(v\), with \(P\) having \(d\) edges. Write \(I_P\) and \(I_Q\) for their sequences of internal vertex labels. For such a sequence \(I\), let \(\mathcal G(I)\) comprise \(0\) and all sums of its nonempty contiguous blocks. Let \(\mathcal A_n\) denote all label sums of connected nonempty vertex sets of the original cycle, including the full cycle. Then the exact identity is
\[
\mathcal R(n;u,v)=\mathcal A_n\cup\bigl\{T_n-a-b:a\in\mathcal G(I_P),\ b\in\mathcal G(I_Q)\bigr\}. \tag{1}
\]
To prove this, consider a connected vertex set \(S\) in the chorded graph. If \(S\) is connected already in the original cycle, its sum lies in \(\mathcal A_n\). Otherwise \(S\) contains both \(u\) and \(v\), and removal of the chord leaves exactly two components, one containing each endpoint. On each of \(P,Q\), the vertices *outside* \(S\) therefore form one contiguous block of internal vertices, possibly empty; two omitted blocks on the same path would isolate a selected component from both chord endpoints. The two omitted blocks have sums \(a,b\), so \(\sum_{w\in S}w=T_n-a-b\). Conversely, if one omits independently a contiguous block of internal vertices on each path, the remaining vertices contain \(u,v\), and every remaining vertex is connected along one of the two paths to an endpoint; the chord joins the endpoints. Thus this set is connected, establishing both inclusions in (1). Note that \(a+b<T_n\), since neither endpoint appears in either omitted block.

**2. Multiplication-table control of cyclic interval sums.** If \(1\le i\le j\le n\), put \(k=j-i+1\). The standard consecutive sum is
\[
\sum_{h=i}^jh=\frac{k(2i+k-1)}2.
\]
For odd \(k\) this equals \(k\bigl(i+(k-1)/2\bigr)\); for even \(k\) it equals \((k/2)(2i+k-1)\). Both displayed factors are positive integers at most \(2n\). Therefore all sums of ordinary (nonwrapping) intervals belong to the multiplication table counted by \(M(2n)\). Every wrapping, proper cyclic interval is the complement of a nonwrapping interval, so its sum is \(T_n-s\) for such an \(s\). The full cycle sum already belongs to the standard set. Consequently
\[
\#\mathcal A_n\le 2M(2n).\tag{2}
\]
The same argument shows that the sums of nonempty contiguous blocks along **either** cyclic path occur among cyclic interval sums. Thus
\[
\#\mathcal G(I_Q)\le 1+2M(2n).\tag{3}
\]
The shorter path has exactly \(d-1\) internal vertices; counting possible contiguous blocks directly gives
\[
\#\mathcal G(I_P)\le1+\frac{d(d-1)}2.\tag{4}
\]
From (1)--(4) and \(\#(A+B)\le\#A\,\#B\) the finite bound follows.

**3. Quantitative obstruction.** Ford's classical multiplication-table theorem gives
\[
M(N)=O\!\left(\frac{N^2}{(\log N)^\delta(\log\log N)^{3/2}}\right)
\qquad (N\to\infty).
\]
Applied to \(N=2n\), this and the finite bound yield an absolute \(C\) and \(n_0\) such that, for every \(n\ge n_0\) and every chord,
\[
\#\mathcal R(n;u,v)\le C(1+d^2)n^2/\Lambda(n).\tag{5}
\]
Since \(T_n=n(n+1)/2\ge n^2/2\), division by \(T_n\) proves the density-zero conclusion when \(d=o(\sqrt{\Lambda(n)})\). If the chord is sum-completing, then \(\#\mathcal R=T_n\), so (5) forces \(1+d^2\ge\Lambda(n)/(2C)\). As \(\Lambda(n)\to\infty\), this implies \(d\ge c\sqrt{\Lambda(n)}\) with some absolute \(c>0\) and all sufficiently large \(n\).

## Verification
The standalone script `verify.py` constructs the full set of connected sums by exhaustive induced-subgraph connectivity testing for every chord of every \(C_n\) with \(4\le n\le12\). Independently it constructs the two-gap sum set (1), then asserts equality. It also checks the exact finite bound and the standard-interval membership in the \(2n\)-multiplication table. A successful run prints `VERIFY_OK exact_chord_instances=210 upper_bound_checks=210 n_range=4..12`. These checks validate small instances only; the asymptotic conclusion uses Ford's published theorem and the proof above.

## Relationship to prior work
Marotti and Needleman introduced the sum-completion problem for consecutively labeled cycles and proved that the bare cycle is incomplete for \(n\ge8\). They give an upper bound on the number of added edges; their stated results do not quantify the *span* needed when a single edge is added. Konieczny recalled the connection between sums of consecutive positive integers and Erdős's multiplication-table problem; his results concern linear interval sums in permutations, not the connected-subset sums of a cycle with one chord. Ford established the multiplication-table order used here. The original contributions are the exact two-gap decomposition (1), the uniform finite bound in terms of cyclic span, and the resulting geometric locality obstruction; the multiplication-table estimate itself is not new. A separate construction with multiple chords gives a logarithmic upper bound on the number of added edges, but does not imply a necessary span for one edge.

## Limitations
The exponent \(\delta/2\) is inherited from the multiplication-table upper bound and is not shown optimal. The statement neither excludes distant one-chord completions nor gives an upper bound on the smallest possible one-chord span. It addresses one edge, not arbitrary sparse chord sets. The upper bound is too coarse to be useful numerically at moderate sizes. Earlier literature could have an equivalent local decomposition under other graph terminology; no assertion of exhaustive bibliographic uniqueness or independent validation is made.

## References
1. J. Marotti and J. Needleman, *Consecutive Cycle Sums*, arXiv:2610.08889v1, first posted 2026-10-06, https://arxiv.org/abs/2610.08889.
2. J. Konieczny, *On consecutive sums in permutations*, arXiv:1504.07156v1, 2015, https://arxiv.org/abs/1504.07156.
3. K. Ford, *Integers with a divisor in (y,2y]*, arXiv:math/0607473, 2006, https://arxiv.org/abs/math/0607473. See also *The distribution of integers with a divisor in a given interval*, Ann. of Math. 168 (2008), 367--433.
