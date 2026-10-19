# Exact minimal flower complexity of finite doubling-invariant sets

## Finding

Let \(E(x)=2x\pmod 1\) act on the circle \(\mathbb T=\mathbb R/\mathbb Z\). For every nonempty finite set \(K\subset\mathbb T\) satisfying \(E(K)=K\), write its points in increasing order as \(0\le y_1<\cdots<y_N<1\). There is exactly one predecessor \(x_i\in K\) with \(E(x_i)=y_i\); define \(b_i=\lfloor 2x_i\rfloor\in\{0,1\}\), using representatives in \([0,1)\).

Define \(P(K)\) to be the least number of connected petals in a doubling flower containing \(K\), where flowers are closures of images of finite-jump preimage selectors as in Harriss--Jenkinson and Brown. Then

\[
\boxed{P(K)=\sum_{i=1}^{N-1}\mathbf1_{b_i\ne b_{i+1}}+\mathbf1_{b_N=b_1}.}
\]

This is a constructive *exact* formula: an optimizing selector has all jumps in the complementary gaps of \(K\), so the points of \(K\) lie in the interiors of petals. In particular \(P(K)\) is always odd.

For the full fixed-point set \(K_n=\operatorname{Fix}(E^n)\), every integer \(n\ge1\) satisfies

\[
\boxed{P(K_n)=2^n-1.}
\]

If \(K\) is one primitive cycle of length \(n>1\), represented by a primitive binary necklace \(w\), and \(L=\operatorname{BWT}(w)\) is the last-column word of the lexicographically sorted cyclic rotations, then

\[
\boxed{P(K)=\operatorname{runs}(L)-1.}
\]

The last identity is an explicit bridge from a geometric optimal-cover problem to the ordinary Burrows--Wheeler run count; results concerning which primitive necklaces have maximally alternating BWT images are previously established, not claimed here.

## Assumptions and scope

A preimage selector is a map \(\eta:\mathbb T\to\mathbb T\) such that \(E\circ\eta=\operatorname{id}\), with finitely many jump discontinuities, no removable discontinuities, and with its value at each jump equal to one lateral limit. Its flower is \(F_\eta=\overline{\eta(\mathbb T)}\). A \(p\)-flower has precisely \(p\) connected components. The invariant set \(K\) is nonempty, finite, and *fully* invariant in the sense \(E(K)=K\); the doubling restriction is necessarily a permutation of \(K\). No claim is made for infinite invariant sets, arbitrary noninvariant point configurations with nonunique predecessors, or selectors for other expansion degrees.

The quantity \(\mathbf1_{\mathcal P}\) equals one if \(\mathcal P\) is true and zero otherwise. The BWT statement concerns one *primitive* cyclic binary word, so the points are distinct and no dyadic binary-expansion ambiguity arises.

## Proof

**1. Forced local inverse branches.** In the coordinate \([0,1)\), the two inverses of \(E\) are \(u_0(y)=y/2\) and \(u_1(y)=(y+1)/2\). Because \(E\) permutes \(K\), each \(y_i\) has a unique prescribed predecessor \(x_i=u_{b_i}(y_i)\). If a flower contains \(K\), then \(x_i\in F_\eta\), and at least one local one-sided limit of \(\eta\) at \(y_i\) must be \(x_i\). The point value at a jump equals a one-sided limit, and there are no removable discontinuities. Since \(K\) is finite, any jump at \(y_i\) may be moved an arbitrarily small distance into the adjacent component of \(\mathbb T\setminus K\), toward the side carrying the other inverse branch. This preserves the selected predecessor near \(y_i\), leaves the total number of jumps unchanged, and can be done in pairwise disjoint neighborhoods. Therefore a minimum over selectors containing \(K\) may be taken over selectors which equal \(u_{b_i}\) throughout a small neighborhood of each \(y_i\), with no jump at any \(y_i\).

**2. Sharp topological lower bound.** Between two successive prescribed points \(y_i<y_{i+1}\) within \((0,1)\), the inverse-branch label is binary and locally constant except at jumps. Hence at least one jump is forced exactly when \(b_i\ne b_{i+1}\). On the circular complementary arc from \(y_N\) to \(y_1\) crossing the coordinate seam, the local sheet coordinates have monodromy: \(u_0(1^-)=u_1(0^+)\) as circle-valued maps, and \(u_1(1^-)=u_0(0^+)\). Thus zero jumps across this arc are possible exactly when \(b_N\ne b_1\); when the bits agree a jump is necessary. These \(N\) disjoint open complementary arcs imply the stated lower bound. It holds even if \(y_1=0\), by choosing neighborhoods on the circle rather than on only one side of the coordinate seam.

**3. Attainment.** Around each \(y_i\) select \(u_{b_i}\), with small disjoint neighborhoods. In every ordinary complementary gap whose endpoint labels differ, insert exactly one jump at any interior point (for example the midpoint); otherwise no jump is inserted. On the gap crossing the coordinate seam insert one jump exactly when the endpoint labels agree. Extend by the chosen inverse branches, ensuring each jump takes one of its two lateral values. The resulting piecewise preimage selector has exactly the lower-bound number of jumps and its image contains all \(x_i\), hence contains \(K\). No jump occurs at \(K\), so \(K\) lies in petal interiors. The ordinary bit-transition count has even parity when \(b_N=b_1\) and odd parity when \(b_N\ne b_1\), proving that \(P(K)\) is odd.

**4. Full-period grids.** Put \(D=2^n-1\). The fixed points of \(E^n\) are precisely \(y_j=j/D\) for integers \(0\le j<D\). The predecessor of \(y_j\) in this set is \(x_j=(2^{n-1}j\bmod D)/D\). The identity \(2^n\equiv1\pmod D\) gives \(2x_j=y_j+c_j\) with \(c_j\equiv j\pmod2\) and \(c_j\in\{0,1\}\). Thus the ordered branch labels are \(0,1,0,1,\ldots,0\), a list of \(D\) entries. There are \(D-1\) ordinary flips and the seam adds one, proving \(P(K_n)=D\) for all \(n\ge1\).

**5. Burrows--Wheeler correspondence.** For a primitive binary periodic orbit \(K\), the usual binary expansions of its points are precisely the distinct cyclic rotations of a primitive word \(w\). Their increasing numerical order agrees with lexicographic order. The first binary digit of the unique predecessor of any point is the last digit of the corresponding rotated word. Hence the ordered list \(b_1\cdots b_N\) is exactly the BWT last column \(L\). The lexicographically least rotation begins at a maximal cyclic run of zeros and must be preceded by \(1\); the greatest begins at a maximal run of ones and must be preceded by \(0\). Consequently \(L_1=1\) and \(L_N=0\). The seam contribution is zero, and the remaining transition count is the number of linear runs minus one. This proves the final identity. \(\square\)

## Verification

Run the self-contained \`python3 verify.py\` (Python standard library only). It uses exact rational arithmetic, enumerates many finite invariant unions, constructs jump locations explicitly, computes sorted cyclic rotations independently, and for small cases independently minimizes jump counts by exhaustively enumerating local side labels. Its reported diagnostic counts are checks of finite instances, not a replacement for the universal proof above. All finite tests performed on the supplied file passed.

## Relationship to prior work

Harriss and Jenkinson (arXiv:0711.0802, Section 2) introduce finite-jump selectors and flowers; Brown (arXiv:2605.06962v1, Sections 2--4) establishes linear symbolic complexity for flower-supported sets and relates flowers to deck-shuffler interval exchanges. Neither inspected statement gives an optimal flower count for an arbitrary prescribed finite invariant set or the sharp exponential count for the full fixed-point sets. Brown's arguments about supports are compatible with the present result; the result is not inferred from a mere failure of keyword search.

A five-petal value for certain unions of reflected mechanical cycles is a special instance of the present invariant formula, not a separately claimed contribution. The new classification concerns every finite invariant union, including unrelated periods and all points fixed by an iterate.

The standard BWT and primitive-root classification of alternating binary BWT images are established word-combinatorial results, reviewed by Kumallagov (arXiv:2606.01267v1, Sections 2 and 8--9). The new mathematical comparison is the explicit equality of their run statistic with a geometrically minimal number of petals; no new classification of BWT images or new number-theoretic infinitude result is asserted.

## Limitations

Only finite supports for the doubling map are covered. The proof supplies no robustness assertion under perturbations of the expanding map, no analogue for degree at least three, and no optimization of the metric length of petals. Published-priority uncertainty remains: earlier work may have implicitly recorded the same finite-support optimization in other terminology, even though the inspected statements did not cover it. The theorem does not assert that the optimal flower has \(K\) as its *entire* maximal invariant set, only that it contains \(K\).

## References

1. E. Harriss and O. Jenkinson, *Flattening Functions on Flowers*, arXiv:0711.0802 (first public posting 2007-11-06), especially Section 2. https://arxiv.org/abs/0711.0802
2. Margaret Brown, *Expanding Maps on Flowers, Interval Exchange Transformations, and Ergodic Optimization*, arXiv:2605.06962v1 (first public posting 2026-05-07), especially Sections 2--4. https://arxiv.org/html/2605.06962v1
3. David Kumallagov, *An extremal problem for completely unclustered Burrows--Wheeler images*, arXiv:2606.01267v1 (first public posting 2026-05-31), especially Sections 2 and 8--9. https://arxiv.org/html/2606.01267v1
