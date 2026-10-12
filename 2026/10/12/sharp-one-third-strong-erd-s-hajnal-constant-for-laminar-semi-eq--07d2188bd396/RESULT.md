# Sharp one-third strong Erdős–Hajnal constant for laminar semi-equations
## Finding

Let \(R\subseteq X\times Y\) be a \((2,1)\)-semi-equation. Thus, for any two distinct fibres \(R_y\) and \(R_{y'}\), either they are disjoint or one contains the other. Equivalently, after restriction to any finite \(A\subseteq X\), the family of restricted fibres is laminar.

Then \(R\) satisfies \(1/3\)-strong Erdős–Hajnal. Explicitly, for every finite nonempty \(A\subseteq X\) and \(B\subseteq Y\), there exist \(A_0\subseteq A\) and \(B_0\subseteq B\) such that
\[
|A_0|\ge \frac{|A|}{3},\qquad |B_0|\ge \frac{|B|}{3},
\]
and \(R\cap(A_0\times B_0)\) is either \(A_0\times B_0\) or empty.

The constant is best possible: no uniform constant larger than \(1/3\) works for all \((2,1)\)-semi-equations.

## Assumptions and scope

For \(b\in B\), write
\[
F_b=R_b\cap A.
\]
The only structural hypothesis used is laminarity of the multiset \((F_b:b\in B)\): for every \(b,c\in B\), the sets \(F_b,F_c\) are disjoint or comparable by inclusion. Repeated fibres are allowed and count with their multiplicity in \(B\).

A rectangle \(A_0\times B_0\) is called homogeneous when all its pairs belong to \(R\), or none do. This is exactly the strong Erdős–Hajnal notion used in the motivating literature.

## Proof

Put \(a=|A|\) and \(b=|B|\).

First suppose that some restricted fibre \(S=F_{b_*}\) has intermediate size
\[
\frac a3\le |S|\le \frac{2a}{3}.
\]
Laminarity partitions \(B\) into three classes:
\[
B_{\supseteq}=\{c:F_c\supseteq S\},
\]
\[
B_{\subsetneq}=\{c:F_c\subsetneq S\},
\]
and
\[
B_{\perp}=\{c:F_c\cap S=\varnothing\}.
\]
One class has size at least \(b/3\). If it is \(B_{\supseteq}\), then \(S\times B_{\supseteq}\) is complete. If it is \(B_{\subsetneq}\), then \((A\setminus S)\times B_{\subsetneq}\) is empty, and \(|A\setminus S|\ge a/3\). If it is \(B_{\perp}\), then \(S\times B_{\perp}\) is empty. This proves the claim in the intermediate-fibre case.

Now suppose no restricted fibre has size in \([a/3,2a/3]\). Call a fibre small if its size is less than \(a/3\), and large if its size is greater than \(2a/3\).

Any two large fibres intersect, because their two cardinalities sum to more than \(a\). By laminarity, all large fibres are therefore linearly ordered by inclusion. If at least \(b/3\) members of \(B\) have large fibres, take those members as \(B_0\). Their intersection is the smallest large fibre, so it has size greater than \(2a/3\); using that intersection as \(A_0\) gives a complete rectangle.

It remains to treat the case in which fewer than \(b/3\) fibres are large. Then more than \(2b/3\) fibres are small. Consider the distinct maximal small fibres. They are pairwise disjoint, and every small fibre is contained in one of them. Let \(U_*\) be their union.

If \(|U_*|<a/3\), all small fibres avoid \(A\setminus U_*\), so taking every small-fibre index for \(B_0\) and \(A_0=A\setminus U_*\) gives an empty rectangle with both sides larger than the required fractions.

Suppose instead that \(|U_*|\ge a/3\). Because every maximal small fibre has size less than \(a/3\), a greedy choice of maximal small fibres produces a union \(U\) satisfying
\[
\frac a3\le |U|<\frac{2a}{3}.
\]
Partition the small-fibre indices into
\[
B_{\mathrm{in}}=\{c:F_c\subseteq U\}
\]
and its complement \(B_{\mathrm{out}}\) among the small-fibre indices. Since there are more than \(2b/3\) small-fibre indices, one of \(B_{\mathrm{in}},B_{\mathrm{out}}\) has size greater than \(b/3\). If \(B_{\mathrm{in}}\) is larger, then \((A\setminus U)\times B_{\mathrm{in}}\) is empty and \(|A\setminus U|>a/3\). If \(B_{\mathrm{out}}\) is larger, maximal-small-fibre disjointness implies that every fibre indexed by \(B_{\mathrm{out}}\) is disjoint from \(U\), so \(U\times B_{\mathrm{out}}\) is empty. This completes the lower-bound proof.

For sharpness, fix any positive integer \(m\). Partition \(A\) into three sets \(A_1,A_2,A_3\), each of size \(m\), and partition \(B\) into three sets \(B_1,B_2,B_3\), each of size \(m\). Give every element of \(B_1\) the full fibre \(A\), every element of \(B_2\) the fibre \(A_1\), and every element of \(B_3\) the fibre \(A_2\). These fibres are laminar.

If \(B_0\) has more than \(m\) elements, it contains at least two fibre types. For the pair of types \(A,A_1\) or \(A,A_2\), every homogeneous \(A_0\) has size at most \(m\): a complete one lies inside the smaller fibre, while an empty one cannot avoid the full fibre. For the pair \(A_1,A_2\), a complete \(A_0\) is empty and an empty \(A_0\) lies inside \(A_3\), again of size at most \(m\). Thus any homogeneous rectangle with \(|B_0|>m\) has \(|A_0|\le m\). Since \(|A|=|B|=3m\), no uniform constant \(\delta>1/3\) is possible.

## Verification

The symbolic proof covers arbitrary finite \(A,B\). The accompanying `verify.py` independently enumerates every binary relation on \(A\times B\) for \(1\le |A|,|B|\le4\), filters those whose fibres are laminar, and checks directly that a homogeneous rectangle with side sizes at least \(\lceil |A|/3\rceil\) and \(\lceil |B|/3\rceil\) always exists. It also checks the sharpness construction for several blow-up sizes. Running the file prints `VERIFY_OK`.

The finite enumeration is corroboration only; it is not used as a proof for arbitrary sizes.

## Relationship to prior work

Tong defines \((k,1)\)-semi-equations and notes explicitly that the case \(k=2\) is exactly the laminar-fibre condition. Tong proves that every \((k,1)\)-semi-equation satisfies \(6^{-(k-1)}\)-strong Erdős–Hajnal, giving \(1/6\) when \(k=2\). The same paper records Fu's earlier explicit \(1/64\) bound for \((2,1)\)-semi-equations and Chernikov--Starchenko's ineffective positive constant for general \(1\)-semi-equations.

The theorem here isolates the laminar endpoint and determines its exact uniform constant: \(1/3\), with a matching construction. The proof uses only the laminar decomposition and does not invoke the induction on \(k\) used for the general \(6^{-(k-1)}\) bound.

Targeted searches for the exact constant, for laminar-fibre homogeneous rectangles, and for equivalent bipartite formulations did not locate a published statement of the sharp \(1/3\) theorem. Literature on laminar set systems primarily concerns their tree representation and algorithmic structure rather than this balanced homogeneous-rectangle constant.

## Limitations

The exact constant is proved only for \((2,1)\)-semi-equations. It does not improve the general \(6^{-(k-1)}\) bound for \(k\ge3\), and it does not claim sharp constants for Boolean combinations of semi-equations.

The sharpness construction is a family of finite relations; no model-theoretic definability beyond being a \((2,1)\)-semi-equation is required. The result therefore concerns the uniform combinatorial class, not an optimized constant inside every individual theory.

## References

[1] Mervyn Tong, “Combinatorics in 1-semi-equational theories,” arXiv:2609.07475, first submitted 7 September 2026.

[2] Y. Fu, “A note on the strong Erdős–Hajnal property for graphs with bounded VC-minimal complexity,” *Journal of Symbolic Logic*, 2024, Theorem 3.1 as cited in [1].

[3] Artem Chernikov and Sergei Starchenko, “Combinatorics in one-based and related structures,” arXiv:2606.08740, 2026.

[4] Artem Chernikov and Alex Mennen, “Semi-equational theories,” *Journal of Symbolic Logic* 90 (2025), 391–422.
