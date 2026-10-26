# Exact codimension-two zero-sum avoidance in elementary binary groups

## Finding
For every integer \(d\geq 2\) and length \(n\geq 2\), let \(G=\mathbb F_2^d\). A sequence means an unordered multiset of \(n\) elements of \(G\), with repetitions allowed; indexed occurrences are distinct when taking subsequences. Let \(B_d(n)\) count sequences with **no zero-sum subsequence of length \(n-2\)**. Define \(N=2^d\), \(m=N/2\), and the following three integer coefficients:

\[
U_m(n)=[z^n]\left(\frac{1+z}{1-z}\right)^m,\quad
V_m(n)=[z^n]\left(\frac{1+z^2}{1-z^2}\right)^m,\quad
W_m(n)=[z^n](1-z^2)^m.
\]

Then the entire length-and-rank distribution is

\[
\boxed{B_d(n)=\frac{1}{N}\left(\binom{N}{n}+(N-1)\left[U_m(n)+W_m(n)-mV_m(n)\right]\right).}
\]

Here \(\binom{N}{n}=0\) for \(n>N\). All coefficients arise from finite binomial expressions; in particular the formula is exact, not asymptotic.

At the first rank-three six-subsequence threshold, \(d=3\) and \(n=8\), there are **exactly \(561\)** avoidance sequences. They split into precisely three orbits under the affine group \(\operatorname{AGL}(3,2)\): one orbit of size \(1\) (all eight elements once), one of size \(224\) (four affinely independent support points with multiplicities \((5,1,1,1)\)), and one of size \(336\) (the same type of support with multiplicities \((3,3,1,1)\)). For example, \(B_4(16)=13{,}032{,}001\).

## Assumptions and scope
The group operation is vector addition over \(\mathbb F_2\); sums and repetitions are interpreted as multisets, not ordered words. In the edge case \(n=2\), the deleted-pair complement has length zero and the empty subsequence has sum zero, so \(B_d(2)=0\). The formula applies uniformly for all integers \(d\geq2\) and \(n\geq2\); it does not assert a distribution for groups of other exponents.

## Proof
**1. Complementary-pair criterion.** Write the sequence sum as \(T=\sum_{x\in S}x\in G\). Deleting two indexed occurrences \(x,y\) leaves a zero-sum sequence of length \(n-2\) if and only if \(x+y=T\), because \(-T=T\) in characteristic two. Thus the avoidance condition is that no available pair of distinct occurrences sums to \(T\).

**2. Sequences with \(T=0\).** A pair sums to zero precisely when its two entries are equal. Therefore an avoiding sequence of sum zero has no repeated entries. Character orthogonality on \(G\) gives the generating series for zero-sum subsets:

\[
\frac1N\sum_{\chi\in\widehat G}\prod_{x\in G}(1+z\chi(x))
=\frac1N\left((1+z)^N+(N-1)(1-z^2)^m\right).
\]

The equality uses the fact that each nontrivial binary character takes \(1\) and \(-1\) exactly \(m\) times. The coefficient of \(z^n\) is \(\bigl(\binom Nn+(N-1)W_m(n)\bigr)/N\).

**3. Sequences with a fixed \(T\neq0\).** Partition \(G\) into the \(m\) disjoint pairs \(\{x,x+T\}\). Avoidance means that no pair has both endpoints occupied; a selected endpoint may have any positive multiplicity. Choose a linear complement \(H\) to \(\langle T\rangle\) in \(G\), so every pair is labelled by \(h\in H\). If its selected endpoint appears \(c_h\) times, its projection to \(H\) contributes \((c_h\bmod2)h\). The projected total must vanish. An even \(c_h>0\) has two endpoint choices, each with zero full-group contribution; an odd \(c_h\) has two endpoint choices, whose contributions differ by \(T\).

For a fixed pair the multiplicity-generating series for even and odd exponents, including endpoint choices, are respectively
\[
E(z)=1+2\sum_{j\geq1}z^{2j}=\frac{1+z^2}{1-z^2},\qquad
O(z)=2\sum_{j\geq0}z^{2j+1}=\frac{2z}{1-z^2}.
\]

Use character orthogonality on \(H\), which has size \(m\), to impose zero projected sum. For the trivial character the product is \((E+O)^m=((1+z)/(1-z))^m\). For every nontrivial \(\chi\in\widehat H\) exactly half the labels have each sign, so the product is
\[
(E+O)^{m/2}(E-O)^{m/2}=(E^2-O^2)^{m/2}=1.
\]

Since \(n\geq2\), the coefficient of \(z^n\) in the sum of these products is \(U_m(n)/m\). This counts all endpoint choices whose **projection** is zero. Those with every \(c_h\) even contribute \(V_m(n)=[z^n]E^m\) and have total zero, not \(T\), so remove them. Every remaining configuration has at least one odd count, and toggling its selected endpoint interchanges total zero and total \(T\), bijectively. Thus exactly half of the remaining choices have total \(T\). The fixed-\(T\) count is
\[
\frac12\left(\frac{U_m(n)}m-V_m(n)\right)
=\frac{U_m(n)-mV_m(n)}N.
\]

There are \(N-1\) choices of nonzero \(T\). Adding them to the zero-total contribution from step 2 proves the formula.

**4. The rank-three inverse classification.** Set \(G=\mathbb F_2^3\) and \(n=8\). If \(T=0\), step 2 requires eight distinct group elements, giving the unique multiset containing the entire group. If \(T\neq0\), at most one endpoint from each of its four \(T\)-pairs may occur, so the support has at most four points. The number of odd multiplicities must be even, since \(n\) is even. It cannot be zero because then \(T=0\); it cannot be two because the two odd-multiplicity points would sum to \(T\), creating a forbidden pair. Consequently all four support points occur with odd multiplicities. Four positive odd integers summing to eight have exactly two unordered patterns: \((5,1,1,1)\) and \((3,3,1,1)\).

Four distinct points of \(\mathbb F_2^3\) have nonzero sum exactly when they are affinely independent (otherwise they form an affine plane). If their sum is nonzero, no two can sum to the total, for that would force the other two to coincide. Among the \(\binom84=70\) four-point subsets, exactly \(14\) are affine planes, giving \(56\) allowed supports. Assigning the first multiplicity pattern to such a support yields \(56\cdot4=224\) sequences, and the second yields \(56\cdot\binom42=336\) sequences. With the all-distinct sequence this totals \(1+224+336=561\). The affine group is transitive on affine bases and induces all permutations of each such base; hence each pattern forms exactly one orbit. No other sequences are possible.

## Verification
The included standalone standard-library program `verify.py` computes the coefficient formula using integer binomial sums, independently checks the complement criterion by brute force for all multisets of ranks \(2\) and \(3\) over finite length ranges, and separately uses a direct XOR-state dynamic program for several rank/length pairs including \((d,n)=(4,16)\). It also checks all \(561\) rank-three extremizers and their multiplicity patterns. Executing `python verify.py` returns `VERIFY_OK`. Exhaustive finite computations verify the implementation and examples only; the proof above establishes the all-rank, all-length assertion.

## Relationship to prior work
The October 15, 2026 preprint by Zhang and Zhang obtains sharp generalized Erdős–Ginzburg–Ziv thresholds in rank-three groups, including \(s_6(\mathbb F_2^3)=9\). A threshold of nine says that length-eight sequences can avoid a six-term zero sum, but it does not enumerate or classify all such sequences. The present result gives both the rank-three inverse enumeration and a length-generating formula for every binary rank. Sidorenko's generalized constants for \(\mathbb F_2^d\) concern maximal lengths and forbidden weights, rather than the displayed exact count. Existing studies of zero-sum multisets and zero-sum polytopes are related; a recent such preprint was only accessible at abstract level during the comparison, so any implicit equivalent formula in that work remains a documented originality risk.

## Limitations
No claim is made about prescribed subsequence lengths other than \(n-2\), non-binary groups, or ordered strings rather than multisets. The rank-three affine orbit statement concerns length eight only. Searches and inspected articles did not identify this precise full-length enumeration, but absence from the examined sources is not a proof of historical priority. In particular, a recent related zero-sum-polytope preprint could not be read in full; independent scholarly review remains necessary.

## References
- H. Zhang and S. Zhang, *Generalized Erdős–Ginzburg–Ziv Constants for finite abelian groups of rank three*, arXiv:2610.21577v1 (first posted October 15, 2026), https://arxiv.org/abs/2610.21577.
- A. Sidorenko, *On generalized Erdős–Ginzburg–Ziv constants for \(\mathbb Z_2^d\)*, arXiv:1808.06555v6; Journal of Combinatorial Theory, Series A 174 (2020), 105254, https://arxiv.org/abs/1808.06555.
- W. Gao and R. Thangadurai, *On the structure of sequences with forbidden zero-sum subsequences* (2003), a related inverse zero-sum problem.
- D. Han et al., *On zero-sum polytopes: reciprocity, rigidity, and cyclic sieving*, arXiv:2606.11005 (2026); abstract-level comparison only, https://arxiv.org/abs/2606.11005.
